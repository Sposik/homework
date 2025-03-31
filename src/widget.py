from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(number: str) -> str:
    """Функция обработки счетов и карт с дополнительной информацией"""
    words = [word for word in number.split() if word]

    digits = ""
    alphas = []
    account_type = None

    for word in words:
        if word.isdigit():
            digits = word
        elif word.lower() == "счет":
            account_type = "account"
        elif word.isalpha():
            alphas.append(word)

    if account_type == "account":
        if not digits:
            raise ValueError("Номер счета не найден")
        return f"Счет {get_mask_account(digits)}"
    else:
        if not digits:
            raise ValueError("Номер карты не найден")
        card_name = " ".join(alphas) if alphas else "Карта"
        return f"{card_name} {get_mask_card_number(digits)}"


def get_date(date: str) -> str:
    if len(date) < 19 or date[4] != "-" or date[7] != "-" or date[10] not in ("T", " "):
        raise ValueError("Дата должна быть в формате YYYY-MM-DDThh:mm:ss")

    date_part = date[:10]
    year, month, day = date_part.split("-")
    return f"{day}.{month}.{year}"
