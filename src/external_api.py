from typing import List, Union
import requests
import os
from dotenv import load_dotenv
from utils import read_transactions

load_dotenv()

def get_api_request(url: str, params: dict = None, headers: dict = None) -> Union[requests.Response, None]:
    """## Функция для отправки запроса к API
    Аргументы:
        `url (str)`: URL API
        `params (dict)`: Параметры запроса
        `headers (dict)`: Заголовки запроса

    Возвращает:
        `requests.Response`: Ответ API
    """
    try:
        response = requests.get(url, params=params, headers=headers)
        response.raise_for_status()  # This will raise HTTPError for bad responses
    except requests.exceptions.ConnectionError as e:
        raise requests.exceptions.ConnectionError("API connection error: " + str(e))
    except requests.exceptions.HTTPError as e:
        raise requests.exceptions.HTTPError("API request error: " + str(e))
    except requests.exceptions.Timeout as e:
        raise requests.exceptions.Timeout("API request timeout: " + str(e))
    except requests.exceptions.RequestException as e:
        raise requests.exceptions.RequestException("API request error: " + str(e))
    else:
        if not response.content:
            raise ValueError("API request returned an empty response")
    return response


def get_api_key(value: str) -> str:
    """## Функция для получения API ключа

    Аргументы:
        `value (str)`: Значение API ключа
    
    Возвращает:
        `str`: API ключ
    """
    try:
        return os.getenv(value)
    except KeyError:
        raise KeyError("API key not found in environment variables")


def get_exchange_rate(amount: float, from_currency: str, to_currency: str = 'RUB') -> Union[float, None]:
    """## Функция для конвертации валюты
    Аргументы:
        `amount (float)`: Сумма
        `from_currency (str)`: Изначальная валюта
        `to_currency (str)`: Конечная валюта

    Возвращает:
        `float`: Конвертированная сумма
    """
    api_url = "https://api.apilayer.com/exchangerates_data/convert"
    headers = {
        "apikey": get_api_key('API_KEY_APILAYER')
    }
    params = {
        "from": from_currency,
        "to": to_currency,
        "amount": amount
    }
    response = get_api_request(api_url, params=params, headers=headers)
    data = response.json()
    try:
        return data["result"]
    except KeyError as e:
        raise KeyError(f"Key {e} not found in JSON data.")


def convert_transaction_amount(transaction: dict) -> float:
    """## Функция для обработки транзакции
    Аргументы:
        `transaction (dict)`: Транзакция

    Возвращает:
        `float`: Сумма в рублях
    """
    try:
        amount = transaction["operationAmount"]["amount"]
        from_currency = transaction["operationAmount"]["currency"]["code"]
        if from_currency != "RUB":
            return get_exchange_rate(amount, from_currency)
        return amount
    except KeyError as e:
        raise KeyError(f"Key {e} not found in JSON data.")
