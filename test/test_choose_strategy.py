import pytest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from strategies.choose import ChooseStrategy


def test_choose_strategy_valid():
    choose_strategy = ChooseStrategy()
    result = choose_strategy.execute(5, 2)
    assert result == 10


def test_choose_strategy_invalid_range():
    choose_strategy = ChooseStrategy()
    with pytest.raises(ValueError):
        choose_strategy.execute(3, 5)


def test_choose_strategy_invalid_type():
    choose_strategy = ChooseStrategy()
    with pytest.raises(ValueError):
        choose_strategy.execute("trzy", 5)
