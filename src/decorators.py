import functools
import time
from typing import Optional, Callable, Any



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

def retry() -> Callable[[Callable[..., Any]], Callable[..., Any]]:
    """
    Декоратор для повторного выполнения функций с указанным количеством попыток.

    Returns:
        Callable: Декорированная функция с повторным выполнением.
    
    Raises:
        ValueError: Если max_attempts не является целым числом.
    """
    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            """
            Обёртка для декорируемой функции, которая выполняет повторное выполнение до тех пор, пока не будет выполнена успешно.
            
            Args:
                *args: Позиционные аргументы функции.
                **kwargs: Именованные аргументы функции.

            Returns:
                Any: Результат выполнения декорируемой функции.

            """
            while True:
                try:
                    result = func(*args, **kwargs)
                    return result
                except Exception as e:
                    print(f"{e.__class__.__name__}. Retrying...")
                    time.sleep(1)

        return wrapper

    return decorator
