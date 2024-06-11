import functools
import time
from typing import Any, Callable, Optional


def log(filename: Optional[str] = None) -> Callable[[Callable[..., Any]], Callable[..., Any]]:
    """
    Декоратор для логирования вызовов функций и их результатов.

    Args:
        filename (str, optional): Путь к файлу для записи логов. Если не указан, логи выводятся в консоль.

    Returns:
        Callable: Декорированная функция с добавленным логированием.
    """

    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            """
            Обёртка для декорируемой функции, которая выполняет логирование.

            Args:
                *args: Позиционные аргументы функции.
                **kwargs: Именованные аргументы функции.

            Returns:
                Any: Результат выполнения декорируемой функции.
            """
            log_message = ""
            try:
                result = func(*args, **kwargs)
                log_message = f"{func.__name__} ok"
                return result
            except Exception as e:
                log_message = f"{func.__name__} error: {e.__class__.__name__}. Inputs: {args}, {kwargs}"
                raise
            finally:
                if filename:
                    with open(filename, "a") as f:
                        f.write(log_message + "\n")
                else:
                    print(log_message)

        return wrapper

    return decorator


def retry(max_attempts: Optional[int] = None) -> Callable[[Callable[..., Any]], Callable[..., Any]]:
    """
    Декоратор для автоматического повторения функции в случае ошибки соединения.

    :param max_attempts: Максимальное количество попыток (для тестирования).
    """

    def decorator_retry(func: Callable[..., Any]) -> Callable[..., Any]:
        @functools.wraps(func)
        def wrapper_retry(*args: Any, **kwargs: Any) -> Any:
            attempts = 0
            while max_attempts is None or attempts < max_attempts:
                try:
                    return func(*args, **kwargs)
                except ConnectionError:
                    attempts += 1
                    print(f"Connection error occurred. Retrying {attempts} time(s)...")
                    time.sleep(1)
            raise ConnectionError(f"Failed to connect after {attempts} attempts")

        return wrapper_retry

    return decorator_retry


def unstable_function() -> None:
    raise ConnectionError("Failed to connect to the API")
