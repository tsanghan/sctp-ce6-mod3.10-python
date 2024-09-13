import pytest
from mymath import add, subtract, multiply, divide

# Import the functions from the module where they are defined
# For this example, let's assume the functions are in a file named 'math_operations.py'
# from math_operations import add, subtract, multiply, divide

# def add(a: int, b: int) -> int:
#     return a + b

# def subtract(a: int, b: int) -> int:
#     return a - b

# def multiply(a: int, b: int) -> int:
#     return a * b

# def divide(a: int, b: int) -> float:
#     return a / b

def test_add():
    assert add(1, 2) == 3
    assert add(-1, -1) == -2
    assert add(0, 0) == 0
    assert add(999, 1) == 1000

def test_subtract():
    assert subtract(2, 1) == 1
    assert subtract(-1, -1) == 0
    assert subtract(0, 1) == -1
    assert subtract(1, 0) == 1

def test_multiply():
    assert multiply(2, 3) == 6
    assert multiply(-1, 1) == -1
    assert multiply(0, 100) == 0
    assert multiply(-2, -3) == 6

def test_divide():
    assert divide(6, 3) == 2
    assert divide(-6, 3) == -2
    assert divide(0, 1) == 0
    with pytest.raises(ZeroDivisionError):
        divide(1, 0)

# Run the tests
if __name__ == "__main__":
    pytest.main()
