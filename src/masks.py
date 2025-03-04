from typing import Union


def get_mask_card_number(number: Union[int, str]) -> str:
    """Функция маскировки номера банковской карты"""
    number = str(number)
    return f"{number[:4]} {number[4:6]} ** **** {number[-4:]}"


def get_mask_account(number: Union[int, str]) -> str:
    """Функция маскировки номера банковского счета"""
    number = str(number)
    return f"**{number[-4:]}"
