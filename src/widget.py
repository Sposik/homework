from src.masks import get_mask_account, get_mask_card_number

def mask_account_card(number: str) -> str:
    """Функция обработки счетов и карт"""
    split_number = number.split()
    digits = ""
    alphas = []
    if "Счет" in number:
        for word in split_number:
            if word.isdigit():
                digits = str(word)
        return f"Счет {get_mask_account(digits)}"
    else:
        for word in split_number:
            if word.isdigit():
                digits = str(word)
            elif word.isalpha():
                alphas.append(word)
    full_alphas = " ".join(alphas)
    return f"{full_alphas} {get_mask_card_number(digits)}"

def get_date(date: str) -> str:
    split_date = date[:10].split("-")
    wright_date = ".".join(reversed(split_date))
    return wright_date



print(get_date("2024-03-11T02:26:18.671407"))
print(mask_account_card("Visa Classic 6831982476737658"))

