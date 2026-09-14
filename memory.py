import sqlite3


def get_connection():
    return sqlite3.connect("expenses.db")


def create_table():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS expenses (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        amount REAL NOT NULL,
        category TEXT,
        description TEXT
    )
    """)

    connection.commit()
    connection.close()


def save_expense(amount, category, description):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
    INSERT INTO expenses (amount, category, description)
    VALUES (?, ?, ?)
    """, (amount, category, description))

    connection.commit()
    connection.close()

    return "Expense saved successfully"


def get_expenses():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
    SELECT id, amount, category, description
    FROM expenses
    """)

    expenses = cursor.fetchall()

    connection.close()

    return expenses


create_table()