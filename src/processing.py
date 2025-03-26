from datetime import datetime
from typing import Dict, List


def filter_by_state(items: List[Dict], state: str = "EXECUTED") -> List[Dict]:
    """
    Фильтрует список словарей по значению ключа 'state'.
    """
    return list(filter(lambda item: item["state"] == state, items))


def sort_by_date(items: List[Dict], reverse: bool = True) -> List[Dict]:
    """
    Сортирует список словарей по дате в указанном порядке.
    """
    return sorted(items, key=lambda x: datetime.fromisoformat(x["date"]), reverse=reverse)
