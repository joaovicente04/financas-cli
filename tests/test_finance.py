from src.finance import add_expense, total_expenses

def test_add_expense():
    expenses = []
    expenses.append(add_expense("lanche", 10))
    assert len(expenses) == 1

def test_total():
    expenses = [
        {"description": "a", "amount": 10},
        {"description": "b", "amount": 20}
    ]
    assert total_expenses(expenses) == 30