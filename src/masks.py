from typing import Union
import logging

logger = logging.getLogger('masks')
file_handler = logging.FileHandler('../Logs/masks.log', 'w', encoding='utf-8')
file_formatter = logging.Formatter('%(asctime)s %(filename)s %(levelname)s: %(message)s')
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)

def get_mask_card_number(number: Union[int, str]) -> str:
    """Функция маскировки номера банковской карты"""
    logger.info('Старт функции маскировки номера карты')
    number = str(number).replace(" ", "")
    if not number.isdigit():
        logger.error('Ошибка ввода данных карты')
        raise ValueError("Номер карты должен содержать только цифры")
    if len(number) != 16:
        logger.error('Ошибка ввода данных карты')
        raise ValueError("Проверьте номер карты")
    result = f"{number[:4]} {number[4:6]} ** **** {number[-4:]}"
    logger.info(f'функция завершила работу с результатом {result}')
    return result


def get_mask_account(number: Union[int, str]) -> str:
    """Функция маскировки номера банковского счета"""
    logger.info('Старт функции маскировки счета')
    number = str(number).replace(" ", "")
    if not number.isdigit():
        logger.error('Ошибка ввода данных счета')
        raise ValueError("Номер счета должен содержать только цифры")
    if len(number) != 20:
        logger.error('Ошибка ввода данных счета')
        raise ValueError("Проверьте номер счета")
    result = f"**{number[-4:]}"
    logger.info(f'функция завершила работу с результатом {result}')
    return result

print(get_mask_card_number(1234567890123456))
print(get_mask_account(12345678901234567890))