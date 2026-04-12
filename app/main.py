
from expense import create_expense, format_expense, format_expenses_list
from storage import save_expenses, load_expenses

def add_expense():
    amount = float(input('Enter the amount of the expense: '))
    category = input('''Select the category of the expense 
                      1. Food
                      2. Travel
                      3. Entertainment
                      4. Study
                      5. Personal
                      6. Other
                      Enter the category number: ''')
    categories = {
        '1': 'Food',
        '2': 'Travel',
        '3': 'Entertainment',
        '4': 'Study',
        '5': 'Personal',
        '6': 'Other'
    }
    if category not in categories:
        print('Invalid category. Please select a valid option.')
        return

    description = input('Enter a description for the expense: ')
    description=description.capitalize()

    expense=create_expense(amount, category, description)
    data=load_expenses()
    data.append(expense)
    save_expenses(data)
    print(save_expenses(data))
    formatted = format_expense(expense)

def view_expenses():
    print('''\n\n''')
    print('Your Expenses:')
    expenses = load_expenses()
    if not expenses:
        print('No expenses found. Please add an expense first.')
        return
    formatted_list = format_expenses_list(expenses)

    return formatted_list
    


    
while True:
    print('''\n\nSelect an operation:
        1. Add Expense
        2. View Expenses
        3. Delete Expense
        4. Give Total Expenses
        5. Exit''')

    choice=input('Enter your choice number: ')

    if choice=='1':
        add_expense()
    elif choice=='2':
        view_expenses()
    elif choice=='5':
        print('Exiting the program. Goodbye!')
        break
    else:
        print('Invalid choice. Please select a valid option.')
        
