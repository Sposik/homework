import json
import logging
import re
from collections import Counter
from typing import Dict, List

logger = logging.getLogger("utils")
file_handler = logging.FileHandler("Logs/utils.log", "w", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s %(filename)s %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)


def open_js(path):
    """Получение списка транзакций из файла"""
    logger.info("Старт функции импорта")
    try:
        with open(path, "r", encoding="utf8") as f:
            data = json.load(f)
        logger.info("Данные загружены")
        return data
    except Exception as e:
        logger.error(f"Произошла ошибка: {e}")
        return []
    finally:
        logger.info("Завершение работы")


def search_transactions_by_description(transactions, search_pattern):
    """
    Ищет транзакции по заданному шаблону в описании операции
    с использованием регулярных выражений
    """
    try:
        pattern = re.compile(search_pattern, re.IGNORECASE)
    except re.error:
        raise ValueError("Некорректный шаблон регулярного выражения")

    found_transactions = []

    for transaction in transactions:
        description = transaction.get("description", "")
        if pattern.search(description):
            found_transactions.append(transaction)

    return found_transactions


def count_operations_by_category(transactions: List[dict], counts: Dict[str, int]) -> Dict[str, int]:
    """
    Подсчитывает количество операций по категориям, используя переданный словарь для аккумуляции результатов.
    """
    descriptions = [t.get("description") for t in transactions if t.get("description") is not None]

    # Считаем вхождения с помощью Counter
    current_counts = Counter(descriptions)

    # Обновляем переданный словарь
    for category, count in current_counts.items():
        counts[category] = counts.get(category, 0) + count

    return counts


def filter_rub_transactions(transactions: list) -> list:
    """Фильтрует транзакции с валютой RUB"""
    rub_transactions = []

    for transaction in transactions:
        # Для CSV данных
        if "currency_code" in transaction:
            currency = transaction.get("currency_code", "").upper()

        # Для JSON данных
        elif "operationAmount" in transaction:
            currency = transaction.get("operationAmount", {}).get("currency", {}).get("code", "").upper()

        # Для других форматов
        else:
            currency = transaction.get("currency", "").upper()

        if currency == "RUB":
            rub_transactions.append(transaction)

    return rub_transactions
