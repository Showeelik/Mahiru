import re
from collections import Counter
from typing import Any, Dict, List, Optional


def sort_by_date(transactions: List[Dict[str, Any]], order: Optional[str] = "desc") -> List[Dict[str, Any]]:
    """
    ## Сортирует список словарей по ключу 'date' в порядке возрастания или убывания.

    Аргументы:
        transactions (List[Dict[str, Any]]): Список словарей с ключом 'date' для сортировки.
        order (Optional[str]): Метод сортировки ('desc' по умолчанию; 'asc' для возрастающего, 'desc' для убывающего).

    Возвращает:
        List[Dict[str, Any]]: Новый список словарей, отсортированный по ключу 'date' в указанном порядке.
    """
    return sorted(transactions, key=lambda x: x.get("date", ""), reverse=True if order == "asc" else False)


def filter_by_status(transactions: List[Dict[str, Any]], state: str) -> List[Dict[str, Any]]:
    """
    Фильтрация транзакций по статусу.

    Аргументы:
        transactions (List[Dict[str, Any]]): Список словарей с данными о банковских операциях.
        status (str): Статус операции.

    Возвращает:
        List[Dict[str, Any]]: Список словарей, удовлетворяющих условию фильтрации.
    """
    return [t for t in transactions if t.get("state", "") == state]


def filter_by_currency(transactions: List[Dict[str, Any]], currency: str) -> List[Dict[str, Any]]:
    """
    Фильтрация транзакций по валюте.

    Аргументы:
        transactions (List[Dict[str, Any]]): Список словарей с данными о банковских операциях.
        currency (str): Валюта операции.
        file_extension (str): Расширение файла

    Возвращает:
        List[Dict[str, Any]]: Список транзакций, удовлетворяющих условию фильтрации.
    """
    transaction = [t for t in transactions if t.get("currency", "") == currency]

    for t in transactions:
        if t.get("operationAmount", None) is not None:
            if t["operationAmount"]["currency"]["code"] == currency:
                transaction.append(t)
            else:
                continue
        else:
            if t.get("currency_code") == currency:
                transaction.append(t)
            else:
                continue
    return transaction


def filter_by_description(transactions: List[Dict[str, Any]], search_string: str) -> List[Dict[str, Any]]:
    """
    Фильтрация транзакций по описанию.

    Аргументы:
        transactions (List[Dict[str, Any]]): Список словарей с данными о банковских операциях.
        search_string (str): Строка для поиска в описании операции.

    Возвращает:
        List[Dict[str, Any]]: Список транзакций, удовлетворяющих условию фильтрации.
    """
    return [t for t in transactions if re.search(search_string, t.get("description", ""), flags=re.IGNORECASE)]


def count_transactions_by_category(transactions: List[Dict[str, Any]], categories: List[str]) -> Dict[str, int]:
    """
    ## Подсчитывает количество операций в каждой категории.

    Аргументы:
        transactions (List[Dict[str, Any]]): Список словарей с данными о банковских операциях.
        categories (List[str]): Список категорий операций.

    Возвращает:
        Dict[str, int]: Словарь, где ключи - категории, а значения - количество операций в каждой категории.
    """
    return Counter(t.get("description", "") for t in transactions if t.get("description", "") in categories)
