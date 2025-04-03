from typing import Any, Dict, List

import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions

"""ФИЛЬТРАЦИЯ ПО ВАЛЮТЕ"""


def test_filter_by_currency(transactions_list: List[Dict[str, Any]]) -> None:
    """Проверяет фильтрацию транзакций по валюте USD."""
    generator = filter_by_currency(transactions_list, "USD")
    assert next(generator) == {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702",
    }
    assert next(generator) == {
        "id": 142264268,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188",
    }


@pytest.mark.parametrize("invalid_code", ["BTC", "ETC", "XRP"])
def test_filter_by_currency_error(transactions_list: List[Dict[str, Any]], invalid_code: str) -> None:
    """Проверяет, что несуществующая валюта вызывает StopIteration."""
    generator = filter_by_currency(transactions_list, invalid_code)
    with pytest.raises(StopIteration):
        next(generator)


def test_filter_by_currency_empty(transactions_list: List[Dict[str, Any]]) -> None:
    """Проверяет, что пустой список транзакций вызывает StopIteration."""
    generator = filter_by_currency([], "USD")
    with pytest.raises(StopIteration):
        next(generator)


"""ОПИСАНИЯ ТРАНЗАКЦИЙ"""


def test_transaction_descriptions(transactions_list: List[Dict[str, Any]]) -> None:
    """Проверяет генератор описаний транзакций."""
    generator = transaction_descriptions(transactions_list)
    assert next(generator) == "Перевод организации"
    assert next(generator) == "Перевод со счета на счет"
    assert next(generator) == "Перевод со счета на счет"
    assert next(generator) == "Перевод с карты на карту"
    assert next(generator) == "Перевод организации"
    with pytest.raises(StopIteration):
        next(generator)


def test_transaction_descriptions_empty() -> None:
    """Проверяет, что пустой список вызывает StopIteration."""
    generator = transaction_descriptions([])
    with pytest.raises(StopIteration):
        next(generator)


"""ГЕНЕРАТОР НОМЕРОВ КАРТ"""


@pytest.mark.parametrize("start, stop", [(11, 13)])
def test_card_number_generator(start: int, stop: int) -> None:
    """Проверяет генератор номеров карт в заданном диапазоне."""
    generator = card_number_generator(start, stop)
    assert next(generator) == "0000 0000 0000 0011"
    assert next(generator) == "0000 0000 0000 0012"
    assert next(generator) == "0000 0000 0000 0013"


@pytest.mark.parametrize("start, stop", [("11", "13")])
def test_card_number_generator_not_int(start: str, stop: str) -> None:
    """Проверяет, что нечисловые входные данные вызывают ValueError."""
    generator = card_number_generator(start, stop)
    with pytest.raises(ValueError):
        next(generator)


def test_card_number_generator_empty() -> None:
    """Проверяет генератор номеров карт без аргументов (начинает с 1)."""
    generator = card_number_generator()
    assert next(generator) == "0000 0000 0000 0001"
    assert next(generator) == "0000 0000 0000 0002"
    assert next(generator) == "0000 0000 0000 0003"
