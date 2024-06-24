import os
from typing import Any, Dict, List

from src.processing import filter_by_currency, filter_by_description, filter_by_status, sort_by_date
from src.utils import read_data_transactions
from src.widget import format_date, mask_account_info


def print_transactions(transactions: List[Dict[str, Any]]) -> None:
    """
    Вывод транзакций в консоль.
    """
    print(f"Всего банковских операций в выборке: {len(transactions)}")
    for transaction in transactions:
        if str(transaction.get("description")) == "nan":
            continue
        date = format_date(transaction.get("date", ""))
        description = transaction.get("description", "")
        from_account = transaction.get("from", None)
        to_account = transaction.get("to", None)
        operation_amount = transaction.get("operationAmount", None)
        currency = transaction.get("currency", None)
        amount = transaction.get("amount", None)
        currency_name = transaction.get("currency_name", None)
        print(f"{date} {description}")
        if from_account is not None:
            if str(from_account) == "nan":
                print(f"{mask_account_info(to_account)}")
            else:
                print(f"{mask_account_info(from_account)} -> {mask_account_info(to_account)}")
        else:
            print(f"{mask_account_info(to_account)}")
        if operation_amount is not None:
            print(f"Сумма: {operation_amount.get('amount', '')} {operation_amount["currency"]["name"]}")
        else:
            if currency is not None:
                print(f"Сумма: {amount} {currency}")
            else:
                print(f"Сумма: {amount} {currency_name}")
        print()


def main() -> None:
    """
    Основная функция программы.
    """
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")
    print("Выберите необходимый пункт меню:")
    print("1. Получить информацию о транзакциях из JSON-файла")
    print("2. Получить информацию о транзакциях из CSV-файла")
    print("3. Получить информацию о транзакциях из XLSX-файла")

    choice = input("Пользователь: ")

    path_data = os.path.join(os.path.dirname(__file__), "data\\")
    file_path_json = path_data + "operations.json"
    file_path_csv = path_data + "transactions.csv"
    file_path_xlsx = path_data + "transactions_excel.xlsx"

    if choice == "1":
        print("Для обработки выбран JSON-файл.")
        transactions = read_data_transactions(file_path_json)
    elif choice == "2":
        print("Для обработки выбран CSV-файл.")
        transactions = read_data_transactions(file_path_csv)
    elif choice == "3":
        print("Для обработки выбран XLSX-файл.")
        transactions = read_data_transactions(file_path_xlsx)
    else:
        print("Неверный выбор. Пожалуйста, выберите пункт меню из списка.")
        return

    while True:
        print("Введите статус, по которому необходимо выполнить фильтрацию.")
        print("Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING")
        status = input("Пользователь: ")
        if status.upper() in ["EXECUTED", "CANCELED", "PENDING"]:
            transactions = filter_by_status(transactions, status.upper())
            break
        else:
            print(f'Статус операции "{status}" недоступен.')

    print(f'Операции отфильтрованы по статусу "{status}"')

    sort_by_date_choice = input("Отсортировать операции по дате? Да/Нет\nПользователь: ")
    if sort_by_date_choice.lower() == "да":
        order = input("Отсортировать по возрастанию или по убыванию?\nПользователь: ")
        transactions = sort_by_date(transactions, order)

    filter_by_currency_choice = input("Выводить только рублевые тразакции? Да/Нет\nПользователь: ")
    if filter_by_currency_choice.lower() == "да":
        transactions = filter_by_currency(transactions, "RUB")

    filter_by_description_choice = input(
        "Отфильтровать список транзакций по определенному слову в описании? Да/Нет\nПользователь: "
    )
    if filter_by_description_choice.lower() == "да":
        search_string = input("Введите слово для поиска в описании: ")
        transactions = filter_by_description(transactions, search_string)

    print("Распечатываю итоговый список транзакций...")
    if len(transactions) == 0:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
        return
    print_transactions(transactions)


if __name__ == "__main__":
    main()
