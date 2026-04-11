import json

def save_expense(data):
    with open("data.json", "w") as file:
        json.dump(data, file, indent=4)
    return "Expense saved successfully!"

def show_expense():
    try:
        with open("data.json", "r") as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        return "No expenses found. Please add an expense first."