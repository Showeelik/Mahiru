import json
import os
from typing import Union


def read_data_from_json(file_path: str) -> list:
    """
    ## Возвращает список словарей из JSON-строки
    Аргументы:
        `data_str (str)`: Путь к JSON-файлу
    Возвращает:
        `list`: список словарей
    """
    if not os.path.exists(file_path):
        return []

    with open(file_path, "r", encoding="utf-8") as file:
        try:
            data = json.load(file)
            if isinstance(data, Union[list, dict]):
                return data
            else:
                return []
        except json.JSONDecodeError:
            return []
