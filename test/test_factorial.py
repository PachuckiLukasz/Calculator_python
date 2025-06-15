import pytest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from strategies.fac import FactorialStrategy


@pytest.mark.parametrize("n,expected", [(0, 1), (5, 120), (10, 3628800)])
def test_factorial_valid_input(n, expected):
    assert FactorialStrategy().execute(n) == expected


def test_factorial_invalid_input_lower_than_zero():
    factorial_strategy = FactorialStrategy()
    with pytest.raises(ValueError):
        factorial_strategy.execute(-1)


def test_factorial_invalid_input_float():
    factorial_strategy = FactorialStrategy()
    with pytest.raises(ValueError):
        factorial_strategy.execute(2.5)
