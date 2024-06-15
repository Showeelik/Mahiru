import json
import logging
import os


def setup_logger(name: str) -> logging.Logger:
    """
    ## Настройка логгера
    Аргументы:
        `name (str)`: Имя логгера
    Возвращает:
        `logging.Logger`: Объект логгера
    """
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s %(levelname)-7s %(name)s:%(lineno)d -> %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        filename=f"logs\\{name}.log",
        filemode="w",
        encoding="utf-8",
    )
    logger = logging.getLogger(name)
    return logger


logger = setup_logger("utils")


def read_data_from_json(file_path: str) -> list:
    """
    ## Возвращает список словарей из JSON-строки
    Аргументы:
        `data_str (str)`: Путь к JSON-файлу
    Возвращает:
        `list`: список словарей
    """
    if not os.path.exists(file_path):
        logger.warning(f"Файл {file_path} не найден")
        return []

    with open(file_path, "r", encoding="utf-8") as file:
        try:
            data = json.load(file)
            if isinstance(data, list):
                logger.info(f"Файл {file_path} успешно загружен")
                return data
            else:
                logger.error(f"Файл {file_path} содержит некорректные данные")
                return []
        except json.JSONDecodeError:
            logger.error(f"Файл {file_path} содержит некорректные данные")
            return []
