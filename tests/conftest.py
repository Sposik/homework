import pytest

@pytest.fixture
def card_correct_return ():
    return "1234 56 ** **** 3456"

@pytest.fixture
def account_correct_return ():
    return "**7890"

@pytest.fixture
def valid_card_output() -> str:
    return "Visa Platinum 1234567890123456"

@pytest.fixture
def valid_account_output() -> str:
    return "Счет **7890"
