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
