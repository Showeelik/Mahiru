from src.utils import setup_logger

logger = setup_logger("masks")


def mask_card_number(card_number: str) -> str:
    """
    ### Маскирует номер карты, показывая только первые 4 цифры, последние 4 цифры и скрывая остальные.

    Аргументы:
        card_number (str): Номер карты, который нужно замаскировать.

    Возвращается:
        str: Замаскированный номер карты.
    """
    logger.info(f"Исходный номер карты: {card_number}")
    if len(card_number) != 16:
        logger.error("Неверный формат номера карты")
        raise ValueError("Неверный формат номера карты")

    if not card_number.isdigit():
        logger.error("Номер карты должен содержать только цифры")
        raise ValueError("Номер карты должен содержать только цифры")

    if isinstance(card_number, int):
        logger.error("Номер карты должен быть строкой")
        raise ValueError("Номер карты должен быть строкой")

    front_part = card_number[:4]
    middle_part = card_number[4:6]
    end_part = card_number[-4:]

    masked_number = f"{front_part} {middle_part}** **** {end_part}"
    logger.info(f"Замаскированный номер карты: {masked_number}")
    return masked_number


def mask_account_number(account_number: str) -> str:
    """
    ## Маскирует номер счета, показывая только последние 4 цифры.

    Аргументы:
        account_number (str): Номер счета для маскировки.

    Возвращает:
        str: Замаскированный номер счета.
    """
    logger.info(f"Исходный номер счета: {account_number}")
    if len(account_number) != 10:
        logger.error("Неверный формат номера счета")
        raise ValueError("Неверный формат номера счета")

    if not account_number.isdigit():
        logger.error("Номер счета должен содержать только цифры")
        raise ValueError("Номер счета должен содержать только цифры")

    if isinstance(account_number, int):
        logger.error("Номер счета должен быть строкой")
        raise ValueError("Номер счета должен быть строкой")

    masked_number = f"**{account_number[-4:]}"
    logger.info(f"Замаскированный номер счета: {masked_number}")

    return masked_number
