import json

def get_data(data_str: str) -> list:
    """
    ## Возвращает список словарей из JSON-строки
    Аргументы:
        `data_str (str)`: Путь к JSON-файлу
    Возвращает:
        `list`: список словарей
    """
    with open(data_str, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data
