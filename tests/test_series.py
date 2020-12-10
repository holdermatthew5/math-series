from math_series import __version__
from math_series.series import fibonacci
from math_series.series import lucas
from math_series.series import sum_series

def test_version():
    assert __version__ == '0.1.0'

def test_fibonacci():
    assert fibonacci(7) == 8

def test_fibonacci_two():
    assert fibonacci(20) == 4181

def test_lucas():
    assert lucas(6) == 11

def test_lucas_two():
    assert lucas(8) == 29

def test_sum_series():
    assert sum_series(5) == 3

def test_sum_series_two():
    assert sum_series(11, 3, 4) == 322