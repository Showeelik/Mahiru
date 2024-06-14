import datetime
from typing import Any, Dict, List, Optional

from src.utils import read_data_from_json


def filter_by_state(dict_list: List[Dict[str, Any]], state: Optional[str] = "EXECUTED") -> List[Dict[str, Any]]:
    """
    ## Фильтрует список словарей на основе значения ключа 'state'.

    Аргументы:
        dict_list (List[Dict[str, Any]]): Список словарей для фильтрации.
        state (Optional[str]): Значение для фильтрации словарей. По умолчанию установлено на 'EXECUTED'.

    Возвращает:
        List[Dict[str, Any]]: Новый список словарей, удовлетворяющих условию фильтрации.
    """
    return [d for d in dict_list if d.get("state") == state]


def sort_by_date(dict_list: List[Dict[str, Any]], order: Optional[str] = "desc") -> List[Dict[str, Any]]:
    """
    ## Сортирует список словарей по ключу 'date' в порядке возрастания или убывания.

    Аргументы:
        dict_list (List[Dict[str, Any]]): Список словарей с ключом 'date' (дата и время в формате ISO) для сортировки.
        order (Optional[str]): Метод сортировки ('desc' по умолчанию; 'asc' для возрастающего, 'desc' для убывающего).

    Возвращает:
        List[Dict[str, Any]]: Новый список словарей, отсортированный по ключу 'date' в указанном порядке.
    """
    return sorted(dict_list, key=lambda x: x.get("date", ""), reverse=True if order == "asc" else False)


