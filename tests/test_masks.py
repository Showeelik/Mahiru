import pytest

from src.masks import mask_card_number, mask_account_number


@pytest.mark.parametrize(
    "card_number, expected_masked_number",
    [
        ("1234567890123456", "1234 56** **** 3456"),
        ("9876543210987654", "9876 54** **** 7654"),
    ],
)
def test_mask_card_number(card_number, expected_masked_number):
    masked_number = mask_card_number(card_number)
    assert masked_number == expected_masked_number


@pytest.mark.parametrize(
    "account_number, expected_masked_number",
    [
        ("1234567890", "**7890"),
        ("9876543210", "**3210"),
        ("4024893712", "**3712"),
        ("5123456789", "**6789"),
    ],
)
def test_mask_account_number(account_number, expected_masked_number):
    masked_number = mask_account_number(account_number)
    assert masked_number == expected_masked_number
