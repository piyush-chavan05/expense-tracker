from storage import load_expenses

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


    
def format_expense(expense, index):
    return print(f'''
    Index: {index} 
          ₹{expense.get('amount', 0)}/-      |      {expense.get('category', 'Unknown')}
    ---------------------------------------  
    Description:
    {expense.get('description', 'No description')}
    ---------------------------------------
    ''')

def format_expenses_list(expenses):
    formatted_listt = []
    for i, expense in enumerate(expenses, start=1):
        formatted_listt.append(format_expense(expense, i))
    return formatted_listt