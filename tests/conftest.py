import pytest

@pytest.fixture
def card_correct_return ():
    return "1234 56 ** **** 3456"

@pytest.fixture
def account_correct_return ():
    return "**7890"
