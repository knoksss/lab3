from src.fb.fib_func import fibonacci
from src.fb.fib_r_func import fibonacci_recursive
from src.fac.fact_func import factorial
from src.fac.fact_r_func import factorial_recursive
from src.errors import FlagError
import pytest


def test_fibonacci_0():
    assert fibonacci(0) == 0


def test_fibonacci_1():
    assert fibonacci(1) == 1


def test_fibonacci_2():
    assert fibonacci(9) == 34


def test_fibonacci_0_r():
    assert fibonacci_recursive(0) == 0


def test_fibonacci_1_r():
    assert fibonacci_recursive(1) == 1


def test_fibonacci_2_r():
    assert fibonacci_recursive(9) == 34 


def test_factorial_0():
    assert factorial(0) == 1


def test_factorial_1():
    assert factorial(1) == 1


def test_factorial_2():
    assert factorial(9) == 362880


def test_factorial_0_r():
    assert factorial_recursive(0) == 1


def test_factorial_1_r():
    assert factorial_recursive(1) == 1


def test_factorial_2_r():
    assert factorial_recursive(9) == 362880


def test_fib_error():
    with pytest.raises(Exception, match="ERROR: Ошибка при вычислении числа Фибоначчи"):
        fibonacci(-5)


def test_fib_error_r():
    with pytest.raises(Exception, match="ERROR: Ошибка при вычислении числа Фибоначчи рекурсивно"):
        fibonacci_recursive(-5)


def test_fact_error():
    with pytest.raises(Exception, match="ERROR: Ошибка при вычислении факториала"):
        factorial(-5)


def test_fact_error_r():
    with pytest.raises(Exception, match="ERROR: Ошибка при вычислении факториала рекурсивно"):
        factorial_recursive(-5)