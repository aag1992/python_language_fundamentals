from queue import LifoQueue

parentheses_dict = {'{': '}', '(': ')', '[': ']'}


def check_valid_parantheses(str):
    q = LifoQueue(maxsize=len(str) // 2)
    for char in str:
        if char in parentheses_dict.keys():
            q.put(char)
        elif char in parentheses_dict.values():
            if q.empty() or char != parentheses_dict[q.get()]:
                return False
    return True


expression = "[[{(([]))}({[]}){{()}}]][[{()}]{{[]}}](({{[]}}){{[()]}})"
result = check_valid_parantheses(expression)

print(f"Expression {expression} is {"a " if result else "not a "} valid expression")
