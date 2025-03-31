from typing import Dict, List

import pytest


@pytest.fixture
def card_correct_return() -> str:
    return "1234 56 ** **** 3456"


@pytest.fixture
def account_correct_return() -> str:
    return "**7890"


@pytest.fixture
def valid_card_output() -> str:
    return "Visa Platinum 1234567890123456"


@pytest.fixture
def valid_account_output() -> str:
    return "Счет **7890"


@pytest.fixture
def sample_transactions() -> List[Dict]:
    return [
        {"id": 1, "state": "EXECUTED", "date": "2023-10-01T12:00:00"},
        {"id": 2, "state": "PENDING", "date": "2023-10-02T12:00:00"},
        {"id": 3, "state": "EXECUTED", "date": "2023-09-01T12:00:00"},
        {"id": 4, "state": "CANCELED", "date": "2023-10-01T12:00:00"},
    ]


@pytest.fixture
def transactions_with_same_date() -> List[Dict]:
    return [
        {"id": 1, "state": "EXECUTED", "date": "2023-10-01T12:00:00"},
        {"id": 2, "state": "EXECUTED", "date": "2023-10-01T12:00:00"},
        {"id": 3, "state": "EXECUTED", "date": "2023-10-01T12:00:00"},
    ]
