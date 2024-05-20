# Mahiru

**Mahiru** - это проект на Python, предназначенная для упрощения задач обработки данных. Она предоставляет функции для фильтрации и сортировки списков словарей по определенным критериям.

## Особенности

- **filter_by_state**: Фильтрует список словарей на основе значения ключа 'state'.
- **sort_by_date**: Сортирует список словарей по ключу 'date' в порядке возрастания или убывания.

## Использование

Примеры использования и демонстрации функциональности функции **filter_by_state**:

```python
def filter_by_state(dict_list: List[Dict[str, Any]], state: Optional[str] = "EXECUTED") -> List[Dict[str, Any]]:
    return [d for d in dict_list if d.get("state") == state]

# Пример использования функции
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

>>> [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]

>>> [{'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]
```

Примеры использования и демонстрации функциональности функции **sort_by_date**:
```python
def sort_by_date(dict_list: List[Dict[str, Any]], order: Optional[str] = "desc") -> List[Dict[str, Any]]:
    return sorted(dict_list, key=lambda x: x.get("date", ""), reverse=True if order == "asc" else False)

# Пример использования функции
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

>>> [{'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
{'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
{'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}]

>>> [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
{'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
{'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
{'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]
```