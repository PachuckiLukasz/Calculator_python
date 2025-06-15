import pytest
import math

from strategies.arcsin import ArcSinusStrategy
from strategies.arccos import ArcCosinusStrategy
from strategies.arctan import ArcTangensStrategy


@pytest.mark.parametrize("x, expected", [
    (0.0, 0.0),
    (0.5, math.asin(0.5)),
    (-1.0, math.asin(-1.0)),
])
def test_arcsin_valid_input(x, expected):
    assert ArcSinusStrategy().execute(x) == pytest.approx(expected, abs=1e-6)


@pytest.mark.parametrize("x", [1.1, -1.1])
def test_arcsin_invalid_input(x):
    with pytest.raises(ValueError):
        ArcSinusStrategy().execute(x)


@pytest.mark.parametrize("x, expected", [
    (1.0, 0.0),
    (0.0, math.acos(0.0)),
    (-1.0, math.pi),
    (0.5, math.acos(0.5)),
    (-0.5, math.acos(-0.5)),
])
def test_arccos_valid_input(x, expected):
    assert ArcCosinusStrategy().execute(x) == pytest.approx(expected, abs=1e-6)


@pytest.mark.parametrize("x", [-1.1, 1.1, 2, -999])
def test_arccos_invalid_input(x):
    with pytest.raises(ValueError):
        ArcCosinusStrategy().execute(x)


@pytest.mark.parametrize("x, expected", [
    (0.0, 0.0),
    (1.0, math.atan(1.0)),
    (-1.0, math.atan(-1.0)),
    (1000.0, math.atan(1000.0)),
    (-1000.0, math.atan(-1000.0)),
    (0.5, math.atan(0.5)),
    (-0.5, math.atan(-0.5)),
])
def test_arctan_valid_input(x, expected):
    assert ArcTangensStrategy().execute(x) == pytest.approx(expected, abs=1e-6)
