import json


def open_js(path):
    """Получение списка транзакций из файла"""
    try:
        with open(path, "r", encoding="utf8") as f:
            data = json.load(f)
        return data
    except (FileNotFoundError, json.JSONDecodeError, TypeError, ValueError, KeyError):
        return {}
