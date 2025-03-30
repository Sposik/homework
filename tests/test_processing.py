from typing import Any, Dict, List, Literal

import pytest

from src.processing import filter_by_state, sort_by_date


# Тесты для filter_by_state
@pytest.mark.parametrize(
    "state, expected_ids",
    [
        ("EXECUTED", [1, 3]),
        ("PENDING", [2]),
        ("CANCELED", [4]),
        ("COMPLETED", []),
    ],
)
def test_filter_by_state(
    sample_transactions: List[Dict[str, Any]],
    state: Literal["EXECUTED", "PENDING", "CANCELED", "COMPLETED"],
    expected_ids: List[int],
) -> None:
    """Тестирование фильтрации транзакций по статусу."""
    filtered = filter_by_state(sample_transactions, state)
    assert [item["id"] for item in filtered] == expected_ids


def test_filter_by_state_default(sample_transactions: List[Dict[str, Any]]) -> None:
    """Тестирование фильтрации с параметром по умолчанию (EXECUTED)."""
    filtered = filter_by_state(sample_transactions)
    assert [item["id"] for item in filtered] == [1, 3]


def test_filter_by_state_empty_list() -> None:
    """Тестирование обработки пустого списка транзакций."""
    assert filter_by_state([]) == []


# Тесты для sort_by_date
def test_sort_by_date_descending(sample_transactions: List[Dict[str, Any]]) -> None:
    """Тестирование сортировки по дате (по убыванию)."""
    sorted_items = sort_by_date(sample_transactions, reverse=True)
    assert [item["id"] for item in sorted_items] == [2, 1, 4, 3]


def test_sort_by_date_ascending(sample_transactions: List[Dict[str, Any]]) -> None:
    """Тестирование сортировки по дате (по возрастанию)."""
    sorted_items = sort_by_date(sample_transactions, reverse=False)
    assert [item["id"] for item in sorted_items] == [3, 1, 4, 2]


def test_sort_by_date_same_date(transactions_with_same_date: List[Dict[str, Any]]) -> None:
    """Тестирование сортировки при одинаковых датах."""
    sorted_items = sort_by_date(transactions_with_same_date)
    assert [item["id"] for item in sorted_items] == [1, 2, 3]


def test_sort_by_date_empty_list() -> None:
    """Тестирование сортировки пустого списка."""
    assert sort_by_date([]) == []


def test_sort_by_date_invalid_format() -> None:
    """Тестирование обработки неверного формата даты."""
    with pytest.raises(ValueError):
        sort_by_date([{"date": "invalid-date-format"}])


def test_sort_by_date_missing_key() -> None:
    """Тестирование обработки отсутствия ключа даты."""
    with pytest.raises(KeyError):
        sort_by_date([{"id": 1}])
