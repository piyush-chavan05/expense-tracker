from storage import load_expenses

def create_expense(amount, category, description, id=None):
    categories = {
        '1': 'Food',
        '2': 'Travel',
        '3': 'Entertainment',
        '4': 'Study',
        '5': 'Personal',
        '6': 'Other'
    }
    id = len(load_expenses()) + 1
    return{
        'id': id,
        'amount': amount,
        'category': categories[category],
        'description': description}
    
def format_expense(expense):
    return print(f'''
    Index: {expense.get('id', 'N/A')} 
          ₹{expense.get('amount', 0)}/-      |      {expense.get('category', 'Unknown')}
    ---------------------------------------  
    Description:
    {expense.get('description', 'No description')}
    ---------------------------------------
    ''')

def format_expenses_list(expenses):
    formatted_listt = []
    for expense in expenses:
        formatted_listt.append(format_expense(expense))
    return formatted_listt