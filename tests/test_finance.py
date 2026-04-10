import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.finance import add_expense, total_expenses


def test_add_expense():
    expense = add_expense("lanche", 10)
    assert expense["description"] == "lanche"
    assert expense["amount"] == 10


def test_total_expenses():
    expenses = [
        {"description": "a", "amount": 10},
        {"description": "b", "amount": 20}
    ]
    assert total_expenses(expenses) == 30