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
    