import pytest
from src/calculator import *

@pytest.fixture
def calculator():
    return Calculator()

@pytest.fixture
def plus(a,b):
    result = a + b;
    return result

@pytest.fixture
def minus(a,b):
    result = a - b;
    return result

@pytest.fixture
def multiply(a,b):
    result = a * b;
    return result

def test_plus(calculator):
    result = calculator.plus(2, 3)
    assert result == 5

    result = calculator.plus(20, 35)
    assert result == 55

    result = calculator.plus(12, 33)
    assert result == 45

    result = calculator.plus(25, 50)
    assert result == 75

def test_minus(calculator):
    result = calculator.minus(2, 3)
    assert result == -1

    result = calculator.minus(3, 3)
    assert result == 0

    result = calculator.minus(22, 3)
    assert result == 19

    result = calculator.minus(3, 8)
    assert result == -5

    result = calculator.minus(2, 18)
    assert result == -16

def test_multiply(calculator):
    result = calculator.multiply(2, 3)
    assert result == 6

    result = calculator.multiply(4, 3)
    assert result == 12

    result = calculator.multiply(56, 1)
    assert result == 56

class TestCalculatorOperations:

    #сложение
    @pytest.mark.parametrize("a, b, expected", [
        (5, 3, 8),
        (-5, -3, -8),
        (5, -3, 2),
        (0, 0, 0),
        (2.5, 3.5, 6.0),
    ])
    def test_plus(self, calculator, a, b, expected):
        result = calculator.plus(a, b)
        assert result == expected

    #minus

    @pytest.mark.parametrize("a, b, expected", [
        (10, 5, 5),
        (5, 10, -5),
        (-5, -3, -2),
        (0, 5, -5),
        (5.5, 2.5, 3.0),
    ])
    def test_minus(self, calculator, a, b, expected):
        result = calculator.minus(a, b)
        assert result == expected

#умножение
    @pytest.mark.parametrize("a, b, expected", [
        (5, 3, 15),
        (-5, 3, -15),
        (-5, -3, 15),
        (5, 0, 0),
        (2.5, 4, 10.0),
    ])
    def test_multiply(self, calculator, a, b, expected):
        result = calculator.multiply(a, b)
        assert result == expected

    @pytest.mark.parametrize("a, b, expected", [
        (10, 2, 5),
        (10, -2, -5),
        (-10, -2, 5),
        (5, 2, 2.5),
        (0, 5, 0),
    ])
    def test_divide(self, calculator, a, b, expected):
        result = calculator.divide(a, b)
        assert result == expected

 #возведение в степень
    @pytest.mark.parametrize("a, b, expected", [
        (2, 3, 8),
        (5, 2, 25),
        (10, 0, 1),
        (2, -1, 0.5),
        (4, 0.5, 2.0),
    ])
    def test_power(self, calculator, a, b, expected):
        result = calculator.power(a, b)
        assert result == pytest.approx(expected)

#статок от деления
    @pytest.mark.parametrize("a, b, expected", [
        (10, 2, 0),
        (10, -2, 0),
        (-10, -2, 0),
        (5, 2, 1),
        (6, 5, 1),
        (8, 3, 2),
        (10, 4, 2),
        (13, 6, 1),
    ])
    def test_sec_divide(self, calculator, a, b, expected):
        result = calculator.sec_divide(a, b)
        assert result == expected
