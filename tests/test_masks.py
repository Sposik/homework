import pytest
from typing import Union
from src.masks import get_mask_card_number, get_mask_account
from tests.conftest import card_correct_return


@pytest.mark.parametrize("card_number", [
    "1234567890123456",
    1234567890123456,
    "1234 5678 9012 3456",
    " 1234567890123456 ",
])

def test_get_mask_card_number(card_number, card_correct_return):
    assert get_mask_card_number(card_number) == card_correct_return


@pytest.mark.parametrize("card_number", [
    "1234567890",
    "12345678901234567890",
    "",
    "1234ABCD5678efgh"
])
def test_get_mask_card_number_raises(card_number):
    """Проверяем, что ошибка возникает, без уточнения типа."""
    with pytest.raises(ValueError):
        get_mask_card_number(card_number)

@pytest.mark.parametrize("account_number", [
    "12345678901234567890",
    12345678901234567890,
    "1234 5678 9012 3456 7890",
    " 12345678901234567890 ",
])

def test_get_mask_account(account_number, account_correct_return):
    assert get_mask_account(account_number) == account_correct_return


@pytest.mark.parametrize("account_number", [
    "123456789012",
    "123456789012345678901234",
    "",
    "1234ABCD5678efgh9012"
])
def test_get_mask_card_number_raises(account_number):
    """Проверяем, что ошибка возникает, без уточнения типа."""
    with pytest.raises(ValueError):
        get_mask_account(account_number)

