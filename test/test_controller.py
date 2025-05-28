import sys
import os

import pytest

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Calculator import Calculator
from CalculatorController import CalculatorController


@pytest.fixture
def controller_with_history():
    history = []
    calc = Calculator()
    controller = CalculatorController(calc, history)
    return controller, history


def test_addition(controller_with_history):
    controller, history = controller_with_history

    result = controller.parse("2+3")
    assert result == "Wynik: 2.0 + 3.0 = 5.0"
    assert history[-1] == "2+3 = 2.0 + 3.0 = 5.0"


def test_logarithm(controller_with_history):
    controller, history = controller_with_history

    result = controller.parse("log(1000)")
    assert result == "Wynik: log10(1000.0) = 3.0"
    assert history[-1] == "Wynik: log10(1000.0) = 3.0"


def test_root(controller_with_history):
    controller, history = controller_with_history

    result = controller.parse("r(100,2)")
    assert result == "Wynik: 100.0 √ 2.0 = 10.0"
    assert history[-1] == "Wynik: 100.0 √ 2.0 = 10.0"


def test_quit(controller_with_history):
    controller, history = controller_with_history

    result = controller.parse("x")
    assert result == "Wynik: Koniec obliczeń"
    assert history[-1] == "Wynik: Koniec obliczeń"


def test_invalid_expression(controller_with_history):
    controller, history = controller_with_history

    result = controller.parse("2++2")
    assert result == "Błąd - nieprawidłowe dane"


def test_invalid_log_input(controller_with_history):
    controller, history = controller_with_history

    result = controller.parse("log(abc)")
    assert result == "Błąd - nieprawidłowe dane"


def test_invalid_second_operand(controller_with_history):
    controller, history = controller_with_history

    result = controller.parse("2+abc")
    assert result == "Błąd - nieprawidłowe dane"


def test_missing_second_operand(controller_with_history):
    controller, history = controller_with_history

    result = controller.parse("5+")
    assert result == "Błąd - nieprawidłowe dane"


def test_invalid_root(controller_with_history):
    controller, history = controller_with_history

    result = controller.parse("r(100 2)")
    assert result == "Błąd - nieprawidłowe dane"


def test_invalid_operator(controller_with_history):
    controller, history = controller_with_history

    result = controller.parse("2&2")
    assert result == "Błąd - nieprawidłowe dane"
