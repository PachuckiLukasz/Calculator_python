from math_core import compute
import pytest


def test_addition():
    assert compute(2, 3, "A") == 5


def test_subtraction():
    assert compute(4, 3, "S") == 1


def test_multiply():
    assert compute(4, 3, "M") == 12


def test_power():
    assert compute(5, 2, "P") == 25


def test_divide():
    assert compute(6, 2, "D") == 3.0


def test_modulo():
    assert compute(8, 3, "MOD") == 2


def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        compute(1, 0, "D")


def test_root():
    assert compute(2, 9, "R") == 3.0


def test_root_by_zero():
    with pytest.raises(ZeroDivisionError):
        compute(0, 9, "R")


def test_unknown_operator():
    with pytest.raises(ValueError):
        compute(2, 2, "Z")


def test_root_from_negative_with_even_degree():
    with pytest.raises(ValueError):
        compute(2, -9, "R")


def test_root_from_negative_with_odd_degree():
    result = compute(3, -8, "R")
    assert result == pytest.approx(-2.0)