def mask_account_info(account_info: str) -> str:
    """
    ### Маскирует номер карты, показывая только имя карты, первые 10 цифры, последние 4 цифры и скрывая остальные
    ### или имя счета и последние 4 цифры.

    ----------------
    * Аргументы:
            * account_info (str): Номер карты/счёта, который нужно замаскировать.

    ----------------
    * Возвращается:
            * str: Замаскированный номер карты/счёта.
    """
    masked_info = (
        f"Счет **{account_info[-4:]}"
        if "Счет" in account_info
        else f"{account_info[:-12]} {account_info[-12:-10]}** **** {account_info[-4:]}"
    )
    return masked_info


def format_date(input_string: str) -> str:
    """
    ### Преобразует дату в формате "XXXX-XX-XXTXX:XX:XX.XXXXXX" в "XX.XX.XXXX".

    ----------------
    * Аргументы:
            * input_string (str): Дата в формате "XXXX-XX-XXTXX:XX:XX.XXXXXX".

    ----------------
    * Возвращается:
            * str: Дата в формате "XX.XX.XXXX".
    """
    return input_string[8:10] + "." + input_string[5:7] + "." + input_string[0:4]
