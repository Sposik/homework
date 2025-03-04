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



print(mask_account_card("Visa Classic 6831982476737658"))

