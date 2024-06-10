import requests
import os
from dotenv import load_dotenv

load_dotenv()

def get_api_request(url: str, params: dict = None, headers: dict = None) -> requests.Response:
    """## Функция для отправки запроса к API
    Аргументы:
        `url (str)`: URL API
        `params (dict)`: Параметры запроса
        `headers (dict)`: Заголовки запроса

    Возвращает:
        `requests.Response`: Ответ API
    """
    pass

def get_api_key(value: str) -> str:
    """## Функция для получения API ключа

    Аргументы:
        `value (str)`: Значение API ключа
    
    Возвращает:
        `str`: API ключ
    """
    pass

def get_exchange_rate(currency: str) -> float:
    """## Функция для получения курса валюты
    Агументы:
        `currency (str)`: Валюта
    
    Возвращает:
        `float`: Курс валюты
    """
    pass

def convert_currency(amount: float, from_currency: str, to_currency: str) -> float:
    """## Функция для конвертации валюты
    Аргументы:
        `amount (float)`: Сумма
        `from_currency (str)`: Изначальная валюта
        `to_currency (str)`: Конечная валюта

    Возвращает:
        `float`: Конвертированная сумма
    """
    pass

def process_transaction(transaction: dict) -> float:
    """## Функция для обработки транзакции
    Аргументы:
        `transaction (dict)`: Транзакция

    Возвращает:
        `float`: Сумма в рублях
    """
    pass

