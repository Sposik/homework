from typing import Any, Dict, Generator, Iterable, List

transactions = [
    {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702",
    },
    # ... остальные транзакции
]


def filter_by_currency(transactions: List[Dict[str, Any]], code: str = "USD") -> Generator[Dict[str, Any], None, None]:
    """Фильтрует транзакции по коду валюты."""
    for transaction in transactions:
        if transaction["operationAmount"]["currency"]["code"] == code:
            yield transaction


def transaction_descriptions(transactions: Iterable[Dict[str, Any]]) -> Generator[str, None, None]:
    """Генерирует описания транзакций."""
    for transaction in transactions:
        yield transaction["description"]


def card_number_generator(start: int = 1, end: int = 3) -> Generator[str, None, None]:
    """Генерирует номера карт в заданном диапазоне."""
    current = start
    while current <= end:
        card_number = f"{current:016d}"
        formatted_number = " ".join([card_number[i:i + 4] for i in range(0, 16, 4)])
        yield formatted_number
        current += 1
