from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

from tools import add_expense as add_expense_tool
from memory import get_expenses


app = FastAPI(
    title="AI Expense Agent API"
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)


class ExpenseRequest(BaseModel):
    amount: float
    category: str
    description: str


@app.get("/")
def home():
    return {
        "message": "AI Expense Agent API is running"
    }


@app.post("/expenses")
def add_expense_api(expense: ExpenseRequest):

    return add_expense_tool(
        expense.amount,
        expense.category,
        expense.description
    )


@app.get("/expenses")
def get_all_expenses():

    expenses = get_expenses()

    return {
        "success": True,
        "expenses": expenses
    }