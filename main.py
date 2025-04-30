from src.imports import import_csv, import_excel
from src.processing import filter_by_state, sort_by_date
from src.utils import filter_rub_transactions, open_js, search_transactions_by_description
from src.widget import get_date, mask_account_card


def main():
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")
    print("Выберите необходимый пункт меню:")
    print("1. Получить информацию о транзакциях из JSON-файла")
    print("2. Получить информацию о транзакциях из CSV-файла")
    print("3. Получить информацию о транзакциях из XLSX-файла")
    while True:
        choice_input = input("Пользователь: ").strip()
        if choice_input == "1":
            transactions = open_js("Data/operations.json")
            print("Для обработки выбран Json файл")
            break
        elif choice_input == "2":
            transactions = import_csv("Data/transactions.csv")
            print("Для обработки выбран CSV файл")
            break
        elif choice_input == "3":
            transactions = import_excel("Data/transactions_excel.xlsx")
            print("Для обработки выбран Excel файл")
            break
        else:
            print("Некорректный ввод. Пожалуйста, выберите 1, 2 или 3.")
    print("Введите статус, по которому необходимо выполнить фильтрацию.")
    print("Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING")
    available_statuses = ["EXECUTED", "CANCELED", "PENDING"]

    while True:
        choice = input("Пользователь: ").strip().upper()
        if choice in available_statuses:
            filtered_transactions = filter_by_state(transactions, choice)
            break
        else:
            print(f'Статус операции "{choice}" недоступен.')
            print("\nВведите статус, по которому необходимо выполнить фильтрацию.")
            print("Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING")

    print("Отсортировать операции по дате? Да / Нет")
    choice_date = input("Пользователь: ").strip()
    if choice_date.upper() == "ДА":
        print("Отсортировать по возрастанию или по убыванию?")
        choice_direction = input("Пользователь: ").strip()
        if choice_direction.upper() == "ПО УБЫВАНИЮ":
            filtered_transactions = sort_by_date(filtered_transactions)
        elif choice_direction.upper() == "ПО ВОЗРАСТАНИЮ":
            filtered_transactions = sort_by_date(filtered_transactions, reverse=False)

    print("Выводить только рублевые транзакции? Да/Нет")
    choice = input("Пользователь: ").strip().upper()
    if choice == "ДА":
        filtered_transactions = filter_rub_transactions(filtered_transactions)

    print("Отфильтровать список транзакций по определенному слову в описании? Да/Нет")
    choice = input("Пользователь: ").strip().upper()
    if choice == "ДА":
        print("Введите слово для фильтрации")
        pattern = input("Пользователь: ").strip()
        filtered_transactions = search_transactions_by_description(filtered_transactions, pattern)

    print("Распечатываю итоговый список транзакций...\n")
    print(f"Всего банковских операций в выборке: {len(filtered_transactions)}")
    for transaction in filtered_transactions:
        if choice_input == "1":
            print(get_date(transaction.get("date")), " ", transaction.get("description"))
            if transaction.get("description") == "Открытие вклада":
                print(mask_account_card(transaction.get("to")))
            else:
                print(mask_account_card(transaction.get("from")), "->", mask_account_card(transaction.get("to")))
                print(
                    f"""Сумма: {transaction.get('operationAmount', {}).get('amount')}
                    {transaction.get('operationAmount', {}).get('currency', {}).get('code')}"""
                )
        else:
            print(get_date(transaction.get("date")), " ", transaction.get("description"))
            if transaction.get("description") == "Открытие вклада":
                print(mask_account_card(transaction.get("to")))
            else:
                print(mask_account_card(transaction.get("from")), "->", mask_account_card(transaction.get("to")))
                print(f"Сумма: {transaction.get('amount')}," "{transaction.get('currency_code')}")


if __name__ == "__main__":
    main()
