import pytest
from solution import convert


def test_single_I():
    assert convert("I") == 1


def test_single_V():
    assert convert("V") == 5


def test_multiple_II():
    assert convert("II") == 2


def test_multiple_III():
    assert convert("III") == 3


def test_different_VI():
    assert convert("VI") == 6


def test_different_XVI():
    assert convert("XVI") == 16


def test_subtractive_IV():
    assert convert("IV") == 4


def test_subtractive_IX():
    assert convert("IX") == 9


def test_digit_plus_subtractive_XIX():
    assert convert("XIX") == 19

def test_invalid_VX():
    with pytest.raises(ValueError):
        convert("VX")


def test_invalid_VVV():
    with pytest.raises(ValueError):
        convert("VVV")


def test_invalid_XXC():
    with pytest.raises(ValueError):
       convert("XXC")