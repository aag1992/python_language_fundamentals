import time
from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

# Database connection
DATABASE = 'expenses.db'


def query_db(query, args=(), one=False):
    """Helper function to interact with the database."""
    conn = sqlite3.connect(DATABASE)
    cur = conn.cursor()
    cur.execute(query, args)
    rv = cur.fetchall()
    conn.close()
    return (rv[0] if rv else None) if one else rv


@app.route('/expenses', methods=['GET', 'POST', 'DELETE'])
def expenses():
    if request.method == 'GET':
        # Get category filter from query params
        category = request.args.get('category')

        # If a category is specified, filter by it
        if category:
            query = """SELECT e.id, c.category_name, e.description, e.amount 
                       FROM expenses e 
                       JOIN categories c ON e.category_id = c.id 
                       WHERE c.category_name = ? AND e.is_deleted = 0"""
            expenses = query_db(query, [category])
        else:
            # Return all expenses if no category is provided
            query = """SELECT e.id, c.category_name, e.description, e.amount 
                       FROM expenses e 
                       JOIN categories c ON e.category_id = c.id 
                       WHERE e.is_deleted = 0"""
            expenses = query_db(query)

        # Convert the result into JSON-friendly format
        result = [{'id': row[0], 'category': row[1], 'description': row[2], 'amount': row[3]} for row in expenses]

        return jsonify({'expenses': result, 'time': time.time()})

    if request.method == 'POST':
        data = request.get_json()  # Expecting JSON input like {'category_id': 1, 'description': 'Taxi fare', 'amount': 8.50}

        if not data or 'category_id' not in data or 'description' not in data or 'amount' not in data:
            return jsonify({'error': 'Invalid input'}), 400

        category_id = data['category_id']
        description = data['description']
        amount = data['amount']

        try:
            conn = sqlite3.connect(DATABASE)
            cur = conn.cursor()
            cur.execute("INSERT INTO expenses (category_id, description, amount) VALUES (?, ?, ?)",
                        (category_id, description, amount))
            conn.commit()
            conn.close()
            return jsonify({'message': 'Expense added', 'time': time.time()})
        except sqlite3.Error as e:
            return jsonify({'error': str(e)}), 500

    if request.method == 'DELETE':
        expense_id = request.args.get('id')

        if not expense_id:
            return jsonify({'error': 'Expense ID is required'}), 400

        try:
            conn = sqlite3.connect(DATABASE)
            cur = conn.cursor()
            cur.execute("UPDATE expenses SET is_deleted = 1 WHERE id = ?", (expense_id,))
            conn.commit()
            conn.close()
            return jsonify({'message': 'Expense deleted', 'time': time.time()})
        except sqlite3.Error as e:
            return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)
