from unittest.mock import Mock, patch
from src.external_api import transaction_amount


# Тесты для успешных сценариев
def test_rub_transaction(rub_transaction):
    """Тест обработки рублевой транзакции"""
    result = transaction_amount(rub_transaction)
    assert result == 1000.00
    assert isinstance(result, float)


@patch("requests.get")
def test_usd_transaction(mock_get, usd_transaction):
    """Тест конвертации USD в RUB"""
    # Мокаем ответ API
    mock_response = Mock()
    mock_response.json.return_value = {"result": 7500.00}
    mock_get.return_value = mock_response

    result = transaction_amount(usd_transaction)
    assert result == 7500.00
    assert isinstance(result, float)


@patch("requests.get")
def test_eur_transaction(mock_get, eur_transaction):
    """Тест конвертации EUR в RUB"""
    # Мокаем ответ API
    mock_response = Mock()
    mock_response.json.return_value = {"result": 4500.00}
    mock_get.return_value = mock_response

    result = transaction_amount(eur_transaction)
    assert result == 4500.00
    assert isinstance(result, float)
