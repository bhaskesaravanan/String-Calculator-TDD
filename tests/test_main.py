import pytest
from src.main import add_numbers


def test_empty_string():
    result = add_numbers("")
    assert result is 0


def test_single_number():
    result = add_numbers("5")
    assert result is 5


def test_add_number():
    result = add_numbers("5,5,5")
    assert result is 15


def test_add_newline_with_number():
    result = add_numbers("5\n5,5")
    assert result is 15


def test_add_custom_delimiter():
    result = add_numbers("//;\n5;5;5")
    assert result is 15
    result = add_numbers("//_\n5_5_5")
    assert result is 15


def test_add_custom_delimiter_with_newline():
    result = add_numbers("//;\n5;5\n5")
    assert result is 15
    result = add_numbers("//;\n5;5\n5,5")
    assert result is 20


def test_negative_numbers():
    with pytest.raises(ValueError, match="negative numbers not allowed: -5"):
        add_numbers("-5,5,5")
    with pytest.raises(ValueError, match="negative numbers not allowed: -5, -3"):
        add_numbers("-5,5,-3")
