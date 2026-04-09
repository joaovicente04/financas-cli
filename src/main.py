from finance import add_expense, total_expenses
from storage import load, save

def main():
    expenses = load()

    print("1 - Adicionar gasto")
    print("2 - Listar gastos")
    print("3 - Ver total")

    option = input("Escolha: ")

    if option == "1":
        desc = input("Descrição: ")
        try:
            value = float(input("Valor: "))
            expense = add_expense(desc, value)
            expenses.append(expense)
            save(expenses)
            print("Gasto salvo!")
        except ValueError as e:
            print(f"Erro: {e}")

    elif option == "2":
        if not expenses:
            print("Nenhum gasto registrado.")
        for e in expenses:
            print(f"{e['description']} - R${e['amount']}")

    elif option == "3":
        total = total_expenses(expenses)
        print(f"Total gasto: R${total}")

    else:
        print("Opção inválida")

if __name__ == "__main__":
    main()