import pytest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from strategies.sin import SinusStrategy
from strategies.cos import CosinusStrategy
from strategies.tan import TangensStrategy
from strategies.cot import CotangensStrategy


@pytest.mark.parametrize("n,expected", [(0, 0.0), (90, 1), (180, 0), (-90, -1)])
def test_sinus_valid_input(n, expected):
    assert SinusStrategy().execute(n) == pytest.approx(expected, abs=1e-6)


@pytest.mark.parametrize("n,expected", [(0, 1.0), (90, 0.0), (180, -1), (270, 0.0)])
def test_cosinus_valid_input(n, expected):
    assert CosinusStrategy().execute(n) == pytest.approx(expected, abs=1e-6)


@pytest.mark.parametrize("n,expected", [(0, 0.0), (45, 1.0), (180, 0.0)])
def test_tangent_typical_input(n, expected):
    assert TangensStrategy().execute(n) == pytest.approx(expected, abs=1e-6)


def test_tangens_near_90_degrees():
    val = TangensStrategy().execute(89.999)
    assert abs(val) > 10000


@pytest.mark.parametrize("n,expected", [(45, 1.0), (60, 0.577350269)])
def test_cotangent_typical_input(n, expected):
    assert CotangensStrategy().execute(n) == pytest.approx(expected, abs=1e-6), f"Cot({n}) powinno być ≈ {expected}"


def test_cotangent_with_zero():
    with pytest.raises(ZeroDivisionError):
        CotangensStrategy().execute(0)