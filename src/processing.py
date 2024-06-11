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


def calculate_sales_by_day_of_week(data: List[Dict[str, Any]]) -> Dict[str, float]:
    """
    ## Вычисляет общую сумму продаж за каждый день недели.

    Аргументы:
        data (List[Dict[str, Any]]): Список словарей с данными о продажах.

    Возвращает:
        Dict[str, float]: Словарь, где ключи - дни недели, а значения - общая сумма продаж за этот день.
    """
    sales_by_day: dict[Any, Any] = {}
    for sale in data:
        date = datetime.datetime.strptime(sale["date"], "%Y-%m-%d")
        day_of_week = date.strftime("%A")
        price = sale["price"]
        quantity = sale["quantity"]
        total_price = price * quantity
        if day_of_week in sales_by_day:
            sales_by_day[day_of_week] += total_price
        else:
            sales_by_day[day_of_week] = total_price
    return sales_by_day


def output_price_day_week_data_json() -> None:
    """
    ### Выводит в консоль общую сумму продаж за каждый день недели.
    """

    data = read_data_from_json("data\\data.json")
    sales_by_day = calculate_sales_by_day_of_week(data["sales"])
    for day, total_price in sales_by_day.items():
        print(f"День недели: {day}, Общая сумма продаж: {total_price}")
