from src.finance import add_expense, total_expenses
from src.storage import load, save
import requests

# 🔹 Função para pegar cotação do dólar
def get_dollar_rate():
    try:
        response = requests.get("https://economia.awesomeapi.com.br/json/last/USD-BRL")
        data = response.json()
        return float(data["USDBRL"]["bid"])
    except:
        return None

# 🔹 Conversão
def convert_to_dollar(valor, cotacao):
    return valor / cotacao


def main():
    expenses = load()

    while True:
        print("\n====== FINANÇAS CLI ======")
        print("1. Adicionar gasto")
        print("2. Listar gastos")
        print("3. Ver total em reais")
        print("4. Ver total em dólar")
        print("0. Sair")
        print("==========================")

        option = input("Escolha: ")

        # ➕ Adicionar gasto
        if option == "1":
            desc = input("Descrição: ")
            try:
                value = float(input("Valor: "))
                expense = add_expense(desc, value)
                expenses.append(expense)
                save(expenses)
                print("✅ Gasto salvo!")
            except ValueError as e:
                print(f"Erro: {e}")

        # 📋 Listar gastos
        elif option == "2":
            if not expenses:
                print("Nenhum gasto registrado.")
                continue

            cotacao = get_dollar_rate()

            for e in expenses:
                if cotacao:
                    valor_dolar = convert_to_dollar(e["amount"], cotacao)
                    print(f"{e['description']} - R${e['amount']:.2f} (≈ ${valor_dolar:.2f})")
                else:
                    print(f"{e['description']} - R${e['amount']:.2f}")

        # 💰 Total em reais
        elif option == "3":
            total = total_expenses(expenses)
            print(f"Total gasto: R${total:.2f}")

        # 💵 Total em dólar
        elif option == "4":
            total = total_expenses(expenses)
            cotacao = get_dollar_rate()

            if cotacao:
                total_dolar = convert_to_dollar(total, cotacao)
                print(f"Total em dólar: ${total_dolar:.2f}")
            else:
                print("Erro ao obter cotação do dólar.")

        # ❌ Sair
        elif option == "0":
            print("Saindo...")
            break

        else:
            print("Opção inválida")


if __name__ == "__main__":
    main()