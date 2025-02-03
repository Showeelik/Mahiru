from unittest.mock import patch, Mock
import requests
from src.external_api import get_api_request, get_exchange_rate, convert_transaction_amount

# Тестирование функции get_api_request на различные исключения
@patch('requests.get')
def test_get_api_request_connection_error(mock_get):
    mock_get.side_effect = requests.exceptions.ConnectionError("Connection error")
    try:
        get_api_request("https://api.example.com/data")
    except requests.exceptions.ConnectionError as e:
        assert str(e) == "API connection error: Connection error"

@patch('requests.get')
def test_get_api_request_http_error(mock_get):
    mock_get.side_effect = requests.exceptions.HTTPError("HTTP error")
    try:
        get_api_request("https://api.example.com/data")
    except requests.exceptions.HTTPError as e:
        assert str(e) == "API request error: HTTP error"

@patch('requests.get')
def test_get_api_request_timeout(mock_get):
    mock_get.side_effect = requests.exceptions.Timeout("Timeout error")
    try:
        get_api_request("https://api.example.com/data")
    except requests.exceptions.Timeout as e:
        assert str(e) == "API request timeout: Timeout error"

@patch('requests.get')
def test_get_api_request_request_exception(mock_get):
    mock_get.side_effect = requests.exceptions.RequestException("Request error")
    try:
        get_api_request("https://api.example.com/data")
    except requests.exceptions.RequestException as e:
        assert str(e) == "API request error: Request error"

@patch('requests.get')
def test_get_api_request_empty_response(mock_get):
    mock_response = Mock()
    mock_response.content = b''
    mock_response.status_code = 200
    mock_get.return_value = mock_response

    try:
        get_api_request("https://api.example.com/data")
    except ValueError as e:
        assert str(e) == "API request returned an empty response"

# Тестирование функции get_exchange_rate на исключение KeyError
@patch('external_api.get_api_request')
def test_get_exchange_rate_key_error(mock_get_api_request):
    mock_get_api_request.return_value.json.return_value = {}
    try:
        get_exchange_rate(100, 'USD')
    except KeyError as e:
        assert e.args[0] == "Key 'result' not found in JSON data."

# Тестирование функции convert_transaction_amount на исключение KeyError
def test_convert_transaction_amount_key_error():
    transaction = {
        "id": 207126257,
        "state": "EXECUTED",
        "date": "2019-07-15T11:47:40.496961",
        "operationAmount": {
            "amount": "92688.46",
            "currency": {
                "name": "USD"
                # Missing "code" key
            }
        },
        "description": "Открытие вклада",
        "to": "Счет 35737585785074382265"
    }
    try:
        convert_transaction_amount(transaction)
    except KeyError as e:
        assert e.args[0] == "Key 'code' not found in JSON data."
