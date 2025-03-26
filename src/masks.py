from typing import Union


def get_mask_card_number(number: Union[int, str]) -> str:
    """Функция маскировки номера банковской карты"""
    number = str(number).replace(" ", "")
    if not number.isdigit():
        raise ValueError ("Номер карты должен содержать только цифры" )
    if len(number) != 16:
        raise ValueError ("Проверьте номер карты")
    return f"{number[:4]} {number[4:6]} ** **** {number[-4:]}"


def get_mask_account(number: Union[int, str]) -> str:
    """Функция маскировки номера банковского счета"""
    number = str(number).replace(" ", "")
    if not number.isdigit():
        raise ValueError("Номер счета должен содержать только цифры")
    if len(number) != 20:
        raise ValueError("Проверьте номер счета")
    return f"**{number[-4:]}"
