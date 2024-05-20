from typing import Any, Dict, List, Optional


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



input_list = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
]


output_desc = sort_by_date(input_list)
output_asc = sort_by_date(input_list, "asc")

print(output_desc)
print(output_asc)

output_default = filter_by_state(input_list)
output_canceled = filter_by_state(input_list, "CANCELED")

print(output_default)
print(output_canceled)

