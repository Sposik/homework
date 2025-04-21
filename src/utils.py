import json
import logging

logger = logging.getLogger("utils")
file_handler = logging.FileHandler("../Logs/utils.log", "w", encoding="utf-8")
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



