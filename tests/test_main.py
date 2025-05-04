from unittest.mock import patch

import pytest

from main import main


@pytest.fixture
def mock_transactions():
    return [
        {
            "date": "2023-10-01T12:00:00Z",
            "description": "Перевод организации",
            "from": "Счет 12345678901234567890",
            "to": "Visa Classic 2842878893689012",
            "amount": 1000,
            "currency_code": "RUB",
        },
        {
            "date": "2023-09-15T08:30:00Z",
            "description": "Открытие вклада",
            "to": "Счет 55556666777788889999",
            "amount": 5000,
            "currency_code": "USD",
        },
    ]


@patch("main.mask_account_card")
@patch("main.get_date")
@patch("builtins.print")
@patch("builtins.input")
@patch("main.filter_by_state")
@patch("main.import_csv")
def test_main_csv_flow(
    mock_import_csv, mock_filter, mock_input, mock_print, mock_get_date, mock_mask, mock_transactions
):
    mock_get_date.return_value = "01.10.2023"
    mock_mask.side_effect = lambda x: x

    input_values = ["2", "EXECUTED", "Нет", "Нет", "Нет"]
    mock_input.side_effect = input_values
    mock_import_csv.return_value = mock_transactions
    mock_filter.return_value = mock_transactions

    main()

    mock_print.assert_any_call("Всего банковских операций в выборке: 2")


@patch("main.mask_account_card")
@patch("main.get_date")
@patch("builtins.print")
@patch("builtins.input")
@patch("main.sort_by_date")
@patch("main.open_js")
def test_main_json_sorting(
    mock_open_js, mock_sort, mock_input, mock_print, mock_get_date, mock_mask, mock_transactions
):
    mock_get_date.return_value = "01.10.2023"
    mock_mask.side_effect = lambda x: x

    input_values = ["1", "EXECUTED", "Да", "ПО УБЫВАНИЮ", "Нет", "Нет"]
    mock_input.side_effect = input_values
    mock_open_js.return_value = mock_transactions
    mock_sort.return_value = mock_transactions

    main()

    mock_sort.assert_called_once()


# Аналогичные исправления для остальных тестов
