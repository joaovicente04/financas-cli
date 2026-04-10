import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.finance import add_expense, total_expenses


def test_add_expense():
    result = add_expense("lanche", 10)
    assert result["description"] == "lanche"
    assert result["amount"] == 10


def test_total_expenses():
    expenses = []
    expenses.append(add_expense("a", 10))
    expenses.append(add_expense("b", 20))

    total = total_expenses(expenses)
    assert total == 30