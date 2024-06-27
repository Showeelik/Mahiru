from src.utils import setup_logger

logger = setup_logger("masks")


def mask_account_number(account_number: str) -> str:
    """
    ### Маскирует номер карты/счёта
    #### Для номера карты, показывая только первые 4 цифры, последние 4 цифры и скрывая остальные.
    #### Для номера счёта, показывая только последние 4 цифры.


    Аргументы:
        account_number (str): Номер карты/счёта, который нужно замаскировать.

    Возвращается:
        str: Замаскированный номер карты/счёта.
    """
    logger.info(f"Исходный номер карты: {account_number}")

    if not account_number.isdigit():
        logger.error("Номер карты должен содержать только цифры")
        raise ValueError("Номер должен содержать только цифры")

    if isinstance(account_number, int):
        logger.error("Номер карты должен быть строкой")
        raise ValueError("Номер должен быть строкой")

    if len(account_number) == 16:

        front_part = account_number[:4]
        middle_part = account_number[4:6]
        end_part = account_number[-4:]

        masked_number = f"{front_part} {middle_part}** **** {end_part}"
        logger.info(f"Замаскированный номер карты: {masked_number}")
        return masked_number

    if len(account_number) == 20:
        masked_number = f"**{account_number[-4:]}"
        logger.info(f"Замаскированный номер счёта: {masked_number}")
        return masked_number

    logger.error("Неверный формат номера")
    raise ValueError("Неверный формат номера")
