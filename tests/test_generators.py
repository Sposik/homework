from typing import Union
import pytest

from src.generators import filter_by_currency, transaction_descriptions, card_number_generator
from tests.conftest import transactions_list

"""FILTER BY CURRENCY"""

def test_filter_by_currency(transactions_list):
    generator = filter_by_currency(transactions_list, "USD")
    assert next(generator) == {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {
                "amount": "9824.07",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702"
        }
    assert next(generator) == {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {
                "amount": "79114.93",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188"
        }
@pytest.mark.parametrize(
    "Invalid_code", ["BTC", "ETC", "XRP"])
def test_filter_by_currency_error(transactions_list, Invalid_code):
    generator = filter_by_currency(transactions_list, Invalid_code)
    with pytest.raises(StopIteration):
        next(generator)

def test_filter_by_currency_empty(transactions_list):
    generator = filter_by_currency([], "USD")
    with pytest.raises(StopIteration):
        next(generator)

"""transaction_descriptions"""

def test_transaction_descriptions(transactions_list):
    generator = transaction_descriptions(transactions_list)
    assert next(generator) == "Перевод организации"
    assert next(generator) == "Перевод со счета на счет"
    assert next(generator) == "Перевод со счета на счет"
    assert next(generator) == "Перевод с карты на карту"
    assert next(generator) == "Перевод организации"
    with pytest.raises(StopIteration):
        next(generator)

def test_transaction_descriptions_empty():
    generator = transaction_descriptions([])
    with pytest.raises(StopIteration):
        next(generator)

"""card_number_generator"""

@pytest.mark.parametrize(
    "start, stop", [(11, 13)])
def test_card_number_generator(start, stop):
    generator = card_number_generator(start, stop)
    assert next(generator) == "0000 0000 0000 0011"
    assert next(generator) == "0000 0000 0000 0012"
    assert next(generator) == "0000 0000 0000 0013"

@pytest.mark.parametrize(
    "start, stop", [("11", "13")])
def test_card_number_generator_not_int(start, stop):
    generator = card_number_generator(start, stop)
    with pytest.raises(ValueError):
        next(generator)

def test_card_number_generator_empty():
    generator = card_number_generator()
    assert next(generator) == "0000 0000 0000 0001"
    assert next(generator) == "0000 0000 0000 0002"
    assert next(generator) == "0000 0000 0000 0003"