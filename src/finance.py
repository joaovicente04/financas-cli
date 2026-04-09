def add_expense(description, amount):
    if not description:
        raise ValueError("Descrição não pode ser vazia")
    
    if amount <= 0:
        raise ValueError("Valor deve ser positivo")
    
    return {
        "description": description,
        "amount": amount
    }

def total_expenses(expenses):
    return sum(e["amount"] for e in expenses)