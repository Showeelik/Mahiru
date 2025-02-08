# Mahiru

**Mahiru** - это проект на Python, представляет собой набор утилит для работы с банковскими транзакциями и номерами карт. Он включает функции для фильтрации, сортировки, маскирования и форматирования данных. Ниже приведено описание каждой функции в проекте:


## Обновление:

### 2024-06-24:
- Новые функции для обработки данных о банковских операциях
В проект добавлены новые функции для работы с данными о банковских операциях, а также обновлена основная логика проекта. https://github.com/Showeelik/Mahiru/pull/11

### 2024-06-21:
- Добавлена поддержка расширений файлов `csv` и `xlsx` для функции **`read_data_from_json`** https://github.com/Showeelik/Mahiru/pull/9

### 2024-06-15:
- Были добавлены логи к фунциям: `masks` и `utils` https://github.com/Showeelik/Mahiru/pull/8


## Модули: 

- **`processing.py`**
    - **`filter_by_status`**: *Фильтрация транзакций по статусу.*
    - **`sort_by_date`**: *Сортирует список словарей по ключу 'date' в порядке возрастания или убывания.*
    - **`filter_by_currency`**: *Фильтрация транзакций по валюте.*
    - **`filter_by_description`**: *Фильтрация транзакций по описанию.*
    - **`count_transactions_by_category`**: *Подсчитывает количество операций в каждой категории.*

- **`masks.py`**
    - **`mask_account_number`**: *Маскирует номер карты/счёта Для номера карты, показывая только первые 4 цифры, последние 4 цифры и скрывая остальные. Для номера счёта, показывая только последние 4 цифры.*

- **`widget.py`**
    - **`mask_account_info`**: *Маскирует номер карты, показывая только имя карты, первые 10 цифры, последние 4 цифры и скрывая остальные или имя счета и последние 4 цифры.*
    - **`format_date`**: *Преобразует дату в формате "XXXX-XX-XXTXX:XX:XX.XXXXXX" в "XX.XX.XXXX".*

- **`external_api.py`**
    - **`get_api_request`**: *Функция для отправки запроса к API*
    - **`get_api_key`**: *Функция для получения API ключа* 
    - **`get_exchange_rate`**: *Функция для конвертации валюты*
    - **`convert_transaction_amount`**: *Функция для обработки транзакции*

- **`utils.py`**
    - **`read_data_transactions`**: *Возвращает список словарей из JSON/CSV/XLSX*
    - **`setup_logger`**: *Настройка логгера*

- **`generators.py`**
    - **`filter_by_currency`**: *Функция принимает список словарей с банковскими операциями и возвращает итератор, который выдает по очереди операции, в которых указана заданная валюта.*
    - **`transaction_descriptions`**: *Функция принимает список словарей с банковскими операциями и возвращает генератор, который выдает описание каждой операции по очереди.*
    - **`card_number_generator`**: *Функция принимает диапазон номеров карт и возвращает генератор, который генерирует номера карт в формате XXXX XXXX XXXX XXXX, где X — цифра.*


- **`decorators.py`**
    - **`log`**: *Декоратор для логирования вызовов функций и их результатов.*



## Тестирование

Этот проект использует pytest для автоматизированного тестирования кода. pytest - это популярный фреймворк для тестирования, который помогает писать простые, читаемые и надежные тесты.

### Установка pytest

Чтобы запустить тесты, вам потребуется установить pytest. Вы можете сделать это с помощью следующей команды:

```bash
poetry add pytest
```

В pytest для анализа покрытия кода надо поставить библиотеку 
pytest-cov:
```bash
poetry add pytest-cov
```

### Запуск тестов

Чтобы запустить все тесты в проекте, выполните следующую команду:

```bash
pytest --cov
```

### Что тестируется

Тесты в этом проекте покрывают следующие функции и компоненты:

- Функция **`filter_by_state`**
- Функция **`sort_by_date`**
- Функция **`mask_card_number`**
- Функция **`mask_account_number`**
- Функция **`mask_account_info`**
- Функция **`format_date`**
- Функция **`get_api_request`**
- Функция **`get_api_key`**
- Функция **`get_exchange_rate`**
- Функция **`convert_transaction_amount`**
- Функция **`read_data_from_json`**
- Декоратор: **`log`**
