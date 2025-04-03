from src.generators import card_number_generator, transaction_descriptions, transactions, filter_by_currency
from src.masks import get_mask_card_number
from src.processing import filter_by_state, sort_by_date
from src.widget import get_date, mask_account_card

data = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
]



print(mask_account_card("Visa Classic 6831982476737658"))
print(sort_by_date(data, reverse=False))
print(filter_by_state(data, state="CANCELED"))
print(get_mask_card_number("1234567890123456"))

for card_number in card_number_generator("-", "0"):
    print(card_number)

descriptions = transaction_descriptions(transactions)
for _ in range(5):
    print(next(descriptions))

usd_transactions = filter_by_currency(transactions, "USD")
for _ in range(2):
    print(next(usd_transactions))
