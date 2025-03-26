import pytest
from typing import Union
from src.masks import get_mask_card_number, get_mask_account

@pytest.fixture
def valid_card_number() -> str:
    """Возвращает валидный номер карты"""
    return "1234567890123456"

@pytest.fixture
def valid_account_number() -> str:
    """Возвращает валидный номер счета (20 цифр)"""
    return "12345678901234567890"

@pytest.mark.parametrize("input_number, expected", [
    ("1234567890123456", "1234 56 ** **** 3456"),  # строка
    (1234567890123456, "1234 56 ** **** 3456"),    # число
    (" 1234567890123456 ", "1234 56 ** **** 3456"),  # с пробелами
    ("1234 5678 9012 3456", "1234 56 ** **** 3456"),  # с пробелами внутри
],)
def test_valid_card_numbers(input_number: Union[str, int], expected: str):
    """Тестирует функцию с валидными номерами карт"""
    assert get_mask_card_number(input_number) == expected

# Параметризованные тесты для проверки невалидных номеров карт
@pytest.mark.parametrize("invalid_number, expected_error", [
    ("1234567890", ValueError),  #  короткий
    ("12345678901234567890", ValueError),  #  длинный
    ("abcdefghijklmnop", ValueError),  # буквы
    ("1234-5678-9012-3456", ValueError),  # дефисы
    ("1234 5678 9012 345", ValueError),  # неполный номер с пробелами
    ("", ValueError),  # пустая строка
    ],)
def test_invalid_card_numbers(invalid_number: str, expected_error: type ):
    """Тестирует функцию с невалидными номерами карт"""
    with pytest.raises(expected_error):
        get_mask_card_number(invalid_number)

# Параметризованные тесты для проверки валидных номеров счетов
@pytest.mark.parametrize("input_number, expected", [
    ("12345678901234567890", "**7890"),  # строка
    (12345678901234567890, "**7890"),    # число (если Python поддерживает такие большие числа)
    (" 12345678901234567890 ", "**7890"),  # с пробелами вокруг
    ("1234 5678 9012 3456 7890", "**7890"),  # с пробелами внутри
])
def test_valid_account_numbers(input_number: Union[str, int], expected: str):
    """Тестирует функцию с валидными номерами счетов"""
    assert get_mask_account(input_number) == expected

# Параметризованные тесты для проверки невалидных номеров счетов
@pytest.mark.parametrize("invalid_number, expected_error", [
    ("1234567890", ValueError),  # короткий
    ("123456789012345678901234567890", ValueError),  #  длинный
    ("abcdefghijklmnopqrst", ValueError),  # буквы
    ("1234-5678-9012-3456-7890", ValueError),  # дефисы
    ("", ValueError),  # пустая строка
    ])
def test_invalid_account_numbers(invalid_number: str, expected_error: type):
    """Тестирует функцию с невалидными номерами счетов"""
    with pytest.raises(expected_error):
        get_mask_account(invalid_number)