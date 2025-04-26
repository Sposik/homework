from unittest.mock import patch

import pandas

from src.imports import import_excel, import_csv


@patch("pandas.read_excel")
def test_import_excel(mock_excel):
    mock_excel.return_value.to_dict.return_value = [{"test": "test"}, {"test2": "test2"}]
    assert import_excel("test_path") == [{"test": "test"}, {"test2": "test2"}]
    mock_excel.assert_called_once_with("test_path")

@patch("pandas.read_csv")
def test_import_csv(mock_csv):
    mock_csv.return_value.to_dict.return_value = [{"test": "test"}, {"test2": "test2"}]
    assert import_csv("test_path") == [{"test": "test"}, {"test2": "test2"}]
    mock_csv.assert_called_once_with("test_path", sep=';')