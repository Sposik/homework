from typing import List, Dict
from datetime import datetime

def filter_by_state(items: List[Dict], state: str = 'EXECUTED') -> List[Dict]:
    """
    Фильтрует список словарей по значению ключа 'state'.
    """
    return list(filter(lambda item: item['state'] == state, items))


def sort_by_date(items: List[Dict], reverse: bool = True) -> List[Dict]:
    """
    Сортирует список словарей по дате в указанном порядке.
    """
    return sorted(items,
                  key=lambda x: datetime.fromisoformat(x['date']), reverse=reverse)


data = [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}, {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]

print(sort_by_date(data, reverse=False))
print(filter_by_state(data, state='CANCELED'))