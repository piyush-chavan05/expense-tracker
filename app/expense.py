def create_expense(amount, category, description):
    categories = {
        '1': 'Food',
        '2': 'Travel',
        '3': 'Entertainment',
        '4': 'Study',
        '5': 'Personal',
        '6': 'Other'
    }
    return{
        'amount': amount,
        'category': categories[category],
        'description': description}
    
def format_expense(expense):
    return print(f"₹{expense['amount']}/- | {expense['category']} | {expense['description']}")

def format_expenses_list(expenses):
    formatted_listt = []
    for expense in expenses:
        formatted_listt.append(format_expense(expense))
    return formatted_listt