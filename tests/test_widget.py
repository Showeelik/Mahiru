import pytest

from widget import mask_account_info, format_date



@pytest.mark.parametrize(
    "account_info, expected_masked_info",
    [
        ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
        ("MasterCard 7158300734726758", "MasterCard 7158 30** **** 6758"),
        ("Visa Gold 1234567812345678", "Visa Gold 1234 56** **** 5678"),
        ("Visa Platinum 8990922113665229", "Visa Platinum 8990 92** **** 5229"),
        ("Счет 73654108430135874305", "Счет **4305"),
    ],
)
def test_mask_account_info(account_info, expected_masked_info):
    masked_info = mask_account_info(account_info)
    assert masked_info == expected_masked_info


@pytest.mark.parametrize(
    "input_string, expected_formatted_date",
    [
        ("2018-07-11T02:26:18.671407", "11.07.2018"),
        ("2023-12-25T10:20:30.123456", "25.12.2023"),
        ("2024-05-22T15:43:21.987654", "22.05.2024"),
        ("2019-03-08T23:59:59.999999", "08.03.2019"),
    ],
)
def test_format_date(input_string, expected_formatted_date):
    formatted_date = format_date(input_string)
    assert formatted_date == expected_formatted_date