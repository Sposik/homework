from src.utils import open_js


def test_open_js_success(temp_json_file):
    """Тест успешного чтения корректного JSON-файла"""
    result = open_js(temp_json_file)
    assert isinstance(result, list)
    assert len(result) == 2
    assert result[0]["id"] == 1


def test_open_js_file_not_found():
    """Тест обработки отсутствующего файла"""
    result = open_js("nonexistent_file.json")
    assert result == []


def test_open_js_invalid_json(broken_json_file):
    """Тест обработки битого JSON-файла"""
    result = open_js(broken_json_file)
    assert result == []
