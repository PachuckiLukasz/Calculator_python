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
    result = controller.parse("r(2,100)")
    assert result == "Wynik: 2.0 √ 100.0 = 10.0"
    assert history[-1] == "Wynik: 2.0 √ 100.0 = 10.0"


def test_invalid_root(controller_with_history):
    controller, history = controller_with_history

    result = controller.parse("r(100 2)")
    assert result.startswith("Błąd - nieprawidłowe dane")


def test_controller_handles_root():
    calc = Calculator()
    history = []
    calc_contr = CalculatorController(calc, history)
    result = calc_contr.parse("r(2,9)")
    assert "3.0" in result


def test_quit(controller_with_history):
    controller, history = controller_with_history

    result = controller.parse("x")
    assert result == "Wynik: Koniec obliczeń"
    assert history[-1] == "Wynik: Koniec obliczeń"


def test_invalid_expression(controller_with_history):
    controller, history = controller_with_history

    result = controller.parse("2++2")
    assert result.startswith("Błąd - nieprawidłowe dane")


def test_invalid_log_input(controller_with_history):
    controller, history = controller_with_history

    result = controller.parse("log(abc)")
    assert "Błąd - nieprawidłowe dane" in result


def test_invalid_second_operand(controller_with_history):
    controller, history = controller_with_history

    result = controller.parse("2+abc")
    assert "Błąd - nieprawidłowe dane" in result


def test_missing_second_operand(controller_with_history):
    controller, history = controller_with_history

    result = controller.parse("5+")
    assert result.startswith("Błąd - nieprawidłowy format")


def test_invalid_root(controller_with_history):
    controller, history = controller_with_history

    result = controller.parse("r(100 2)")
    assert "Błąd - nieprawidłowe dane" in result


def test_invalid_operator(controller_with_history):
    controller, history = controller_with_history

    result = controller.parse("2&2")
    assert "błąd - nieznany operator" in result.lower()


def test_controller_handles_invalid_text():
    calc = Calculator()
    history = []
    calc_contr = CalculatorController(calc, history)
    result = calc_contr.parse("abc")
    assert "Błąd - nieznany operator" in result


def test_controller_handles_end_of_work():
    calc = Calculator()
    history = []
    calc_contr = CalculatorController(calc, history)
    result = calc_contr.parse("x")
    assert calc.keep_going == False
    assert "Koniec obliczeń" in result

