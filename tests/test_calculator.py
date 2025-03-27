import pytest
from src.calculator import add, subtract, multiply, divide

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0
    assert add(1.5, 2.5) == 4.0
    assert add(-3, -7) == -10

def test_subtract():
    assert subtract(5, 3) == 2
    assert subtract(10, 20) == -10
    assert subtract(0, 0) == 0
    assert subtract(2.5, 1.5) == 1.0
    assert subtract(-5, -3) == -2

def test_multiply():
    assert multiply(4, 5) == 20
    assert multiply(0, 10) == 0
    assert multiply(-3, 3) == -9
    assert multiply(1.5, 2) == 3.0
    assert multiply(-2, -4) == 8

def test_divide():
    assert divide(10, 2) == 5
    assert divide(9, 3) == 3
    assert divide(1, 4) == 0.25
    assert divide(-6, 2) == -3
    assert divide(-6, -2) == 3
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        divide(5, 0)