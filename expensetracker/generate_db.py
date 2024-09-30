import sqlite3


def create_sqlite_database(filename):
    """ create a database connection to an SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(filename)
        cur = conn.cursor()

        # Create categories table with auto-incrementing ID
        cur.execute("""
        CREATE TABLE IF NOT EXISTS categories(
           id INTEGER PRIMARY KEY AUTOINCREMENT,
           category_name TEXT NOT NULL
        );    
        """)

        # Create expenses table with auto-incrementing ID and foreign key to categories
        cur.execute("""
        CREATE TABLE IF NOT EXISTS expenses(
           id INTEGER PRIMARY KEY AUTOINCREMENT,
           category_id INT NOT NULL,
           description TEXT,
           amount FLOAT,
           is_deleted INTEGER DEFAULT 0,
           FOREIGN KEY (category_id) REFERENCES categories(id)
        );    
        """)

        conn.commit()
        print(f"SQLite version: {sqlite3.sqlite_version}")
    except sqlite3.Error as e:
        print(e)
    finally:
        if conn:
            conn.close()


def populate_expenses(filename):
    """Populate the categories and expenses tables with some initial data"""
    conn = None
    try:
        conn = sqlite3.connect(filename)
        cur = conn.cursor()

        # Insert data into categories
        cur.execute("INSERT INTO categories (category_name) VALUES ('Food');")
        cur.execute("INSERT INTO categories (category_name) VALUES ('Transport');")
        cur.execute("INSERT INTO categories (category_name) VALUES ('Entertainment');")

        # Insert data into expenses
        cur.execute("INSERT INTO expenses (category_id, description, amount) VALUES (1, 'Lunch at cafe', 15.00);")
        cur.execute("INSERT INTO expenses (category_id, description, amount) VALUES (2, 'Taxi fare', 8.50);")
        cur.execute("INSERT INTO expenses (category_id, description, amount) VALUES (3, 'Movie ticket', 12.00);")

        conn.commit()
        print("Initial data inserted.")
    except sqlite3.Error as e:
        print(e)
    finally:
        if conn:
            conn.close()


# Example usage:
db_filename = 'expenses.db'
create_sqlite_database(db_filename)
populate_expenses(db_filename)
