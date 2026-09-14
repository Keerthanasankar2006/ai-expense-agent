def validate_expense(amount, category, description):

    if amount <= 0:
        return False, "Amount must be greater than 0."

    if not category.strip():
        return False, "Category cannot be empty."

    if not description.strip():
        return False, "Description cannot be empty."

    return True, "Expense is valid."

