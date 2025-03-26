import pytest
from src.widget import mask_account_card, get_date




# Фикстуры для валидных данных
@pytest.fixture
def valid_card_input() -> str:
    return "Visa Platinum 1234567890123456"

@pytest.fixture
def valid_account_input() -> str:
    return "Счет 12345678901234567890"

# Параметризованные тесты для карт
@pytest.mark.parametrize("input_str, expected", [
    ("Visa 1234567890123456", "Visa 1234 56 ** **** 3456"),
    ("Mastercard Gold 1234567890123456", "Mastercard Gold 1234 56 ** **** 3456"),
    ("МИР 1234567890123456", "МИР 1234 56 ** **** 3456"),
    ("  Visa Classic  1234567890123456  ", "Visa Classic 1234 56 ** **** 3456"),
])
def test_card_masking(input_str: str, expected: str):
    assert mask_account_card(input_str) == expected

# Параметризованные тесты для счетов
@pytest.mark.parametrize("input_str, expected", [
    ("Счет 12345678901234567890", "Счет **7890"),
    ("Счет  12345678901234567890", "Счет **7890"),
    ("  Счет 12345678901234567890  ", "Счет **7890"),
])
def test_account_masking(input_str: str, expected: str):
    assert mask_account_card(input_str) == expected

# Тесты с использованием фикстур
def test_card_with_fixture(valid_card_input: str):
    assert mask_account_card(valid_card_input) == "Visa Platinum 1234 56 ** **** 3456"

def test_account_with_fixture(valid_account_input: str):
    assert mask_account_card(valid_account_input) == "Счет **7890"

@pytest.mark.parametrize("invalid_input", [
    "Счет abcdef",  # невалидный номер счета
     "",  # пустая строка
])
def test_invalid_inputs(invalid_input: str):
    with pytest.raises(ValueError):
        mask_account_card(invalid_input)

"""
GET DATE
"""


# Корректные
@pytest.mark.parametrize("input_date, expected", [
    ("2024-03-11T02:26:18.671407", "11.03.2024"),
    ("2023-12-31T23:59:59.999999", "31.12.2023"),
    ("2023-01-01T00:00:00.000000", "01.01.2023"),
    ("2020-02-29T12:00:00", "29.02.2020"),
    ("2023-12-31 23:59:59", "31.12.2023"),
])
def test_valid_datetime_formats(input_date: str, expected: str):
    """Тестируем корректное преобразование дат"""
    assert get_date(input_date) == expected

# некорректные
@pytest.mark.parametrize("invalid_date", [
    "2024-03-11",
    "11.03.2024",
    "hello",
    "",
])
def test_invalid_datetime_formats(invalid_date: str):
    """Тестируем обработку некорректных форматов"""
    with pytest.raises((ValueError, IndexError)):
        get_date(invalid_date)


