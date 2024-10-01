import json

person = {"name": "John", "age": 30, "city": "New York", "hasChildren": False, "titles": ["engineer", "programmer"]}


class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

user = User("yossi", 23)

userJSON = json.dumps(user)
