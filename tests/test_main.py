import pytest
from src.main import add_numbers


def test_add_numbers():
    result = add_numbers("1")
    assert result is 0
