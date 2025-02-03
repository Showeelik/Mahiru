import pytest

from src.masks import mask_account_number


@pytest.mark.parametrize(
    "card_number, expected_masked_number",
    [
        ("1234567890123456", "1234 56** **** 3456"),
        ("9876543210987654", "9876 54** **** 7654"),
        ("12345678901234567890", "**7890"),
        ("98765432104385834588", "**4588"),
        ("40248937123495923959", "**3959"),
        ("51234567893290854238", "**4238"),
    ],
)
def test_mask_card_number(card_number, expected_masked_number):
    masked_number = mask_account_number(card_number)
    assert masked_number == expected_masked_number

