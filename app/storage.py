import json

def save_expenses(data):
    with open("data.json", "w") as file:
        json.dump(data, file, indent=4)
    return "Expense saved successfully!"

def load_expenses():
    try:
        with open("data.json", "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []