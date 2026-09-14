from memory import save_expense
from validation import validate_expense


def calculate_total(amounts):
    return sum(amounts)


def add_expense(amount, category, description):

    # Validate
    is_valid, message = validate_expense(
        amount,
        category,
        description
    )

    if not is_valid:
        return {
            "success": False,
            "error": message
        }

    # Save to database
    try:
        save_expense(
            amount,
            category,
            description
        )

        return {
            "success": True,
            "message": "Expense saved successfully"
        }

    except Exception as e:
        return {
            "success": False,
            "error": str(e)
        }