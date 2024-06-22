import json
from unittest.mock import mock_open, patch

import pandas as pd

from src.utils import read_data_from_json


# Тест на успешный загрузку json файла
@patch('os.path.exists', return_value=True)
@patch('builtins.open', new_callable=mock_open, read_data='[{"key": "value"}]')
@patch('json.load', return_value=[{"key": "value"}])
@patch('src.utils.logger')
def test_read_json_success(mock_logger, mock_json_load, mock_open, mock_exists):
    result = read_data_from_json('test.json')
    assert result == [{"key": "value"}]
    mock_exists.assert_called_once_with('test.json')
    mock_open.assert_called_once_with('test.json', 'r', encoding='utf-8')
    mock_json_load.assert_called_once()
    mock_logger.info.assert_called_once_with('Файл test.json успешно загружен')


# Тест на случай, когда файл не найден
@patch('os.path.exists', return_value=False)
@patch('src.utils.logger')
def test_file_not_found(mock_logger, mock_exists):
    result = read_data_from_json('missing.json')
    assert result == []
    mock_exists.assert_called_once_with('missing.json')
    mock_logger.warning.assert_called_once_with('Файл missing.json не найден')


# Тест на случай, когда файл содержит некорректные данные
@patch('os.path.exists', return_value=True)
@patch('builtins.open', new_callable=mock_open, read_data='invalid json')
@patch('json.load', side_effect=json.JSONDecodeError("Expecting value", "invalid json", 0))
@patch('src.utils.logger')
def test_json_decode_error(mock_logger, mock_json_load, mock_open, mock_exists):
    result = read_data_from_json('test.json')
    assert result == []
    mock_exists.assert_called_once_with('test.json')
    mock_open.assert_called_once_with('test.json', 'r', encoding='utf-8')
    mock_json_load.assert_called_once()
    mock_logger.error.assert_called_once_with('Файл test.json содержит некорректные данные')


# Тест на успешный загрузку csv файла
@patch('os.path.exists', return_value=True)
@patch('pandas.read_csv')
@patch('src.utils.logger')
def test_read_csv_success(mock_logger, mock_read_csv, mock_exists):
    mock_read_csv.return_value = pd.DataFrame({'col1': [1, 2], 'col2': [3, 4]})
    result = read_data_from_json('test.csv')
    assert result == [{'col1': 1, 'col2': 3}, {'col1': 2, 'col2': 4}]
    mock_exists.assert_called_once_with('test.csv')
    mock_read_csv.assert_called_once_with('test.csv')
    mock_logger.info.assert_called_once_with('Файл test.csv успешно загружен')

# Тест на успешный загрузку xlsx файла
@patch('os.path.exists', return_value=True)
@patch('pandas.read_excel')
@patch('src.utils.logger')
def test_read_xlsx_success(mock_logger, mock_read_excel, mock_exists):
    mock_read_excel.return_value = pd.DataFrame({'col1': [1, 2], 'col2': [3, 4]})
    result = read_data_from_json('test.xlsx')
    assert result == [{'col1': 1, 'col2': 3}, {'col1': 2, 'col2': 4}]
    mock_exists.assert_called_once_with('test.xlsx')
    mock_read_excel.assert_called_once_with('test.xlsx')
    mock_logger.info.assert_called_once_with('Файл test.xlsx успешно загружен')


# Тест на случай, когда файл неподдерженного формата
@patch('os.path.exists', return_value=True)
@patch('src.utils.logger')
def test_read_transactions_file_unsupported_format(mock_logger, mock_exists):
    result = read_data_from_json('test.txt')
    assert result == []
    mock_exists.assert_called_once_with('test.txt')
    mock_logger.error.assert_called_once_with('Неподдерживаемый формат файла test.txt')

