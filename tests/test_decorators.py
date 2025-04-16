import pytest

from src.decorators import log


def test_log_to_console(capsys):
    """Тестируем логирование в консоль с новым форматом"""

    @log()
    def add(a, b):
        return a + b

    result = add(2, 3)

    captured = capsys.readouterr()
    assert "Начало выполнения функции add." in captured.out
    assert " add ok" in captured.out
    assert result == 5


def test_log_error_to_console(capsys):
    """Тестируем логирование ошибок в консоль с новым форматом"""

    @log()
    def divide(a, b):
        return a / b

    with pytest.raises(ZeroDivisionError):
        divide(10, 0)

    captured = capsys.readouterr()
    assert "divide error ZeroDivisionError" in captured.out
    assert "inputs: (10, 0)" in captured.out


def test_log_to_file(tmp_path):
    """Тестируем логирование в файл с новым форматом"""
    filename = tmp_path / "test.log"

    @log(filename=str(filename))
    def multiply(a, b):
        return a * b

    result = multiply(3, 4)

    with open(filename, "r", encoding="utf-8") as f:
        content = f.read()
        assert "Начало выполнения функции multiply." in content
        assert " multiply ok" in content
    assert result == 12


def test_log_error_to_file(tmp_path):
    """Тестируем логирование ошибок в файл с новым форматом"""
    filename = tmp_path / "errors.log"

    @log(filename=str(filename))
    def fail_function():
        raise ValueError("Custom error")

    with pytest.raises(ValueError):
        fail_function()
