def mask_card_number(card_number: str) -> str:
    """
    Маскирует номер карты, показывая только первые 4 цифры, последние 4 цифры и скрывая остальные.

    Аргументы:
        card_number (str): Номер карты, который нужно замаскировать.

    Возвращается:
        str: Замаскированный номер карты.
    """
    front_part = card_number[:4]
    middle_part = card_number[4:6]
    end_part = card_number[-4:]

    masked_number = f"{front_part} {middle_part}** **** {end_part}"
    return masked_number


def mask_account_number(account_number: str) -> str:
    """
    Маскирует номер счета, показывая только последние 4 цифры.

    Аргументы:
        account_number (str): Номер счета для маскировки.

    Возвращает:
        str: Замаскированный номер счета.
    """
    return f"**{account_number[-4:]}"
