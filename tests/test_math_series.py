from math_series import __version__
from math_series.series import fibonacci, lucas, sum_series


def test_version():
    assert __version__ == '0.1.0'


def test_fibonacci():
    actual = fibonacci(5)
    expected = "3"
    assert actual == expected


def test_lucas():
    actual = lucas(6)
    expected = "11"
    assert actual == expected


def test_sum_series1():
    actual = sum_series(6, 2, 1)
    expected = "11"
    assert actual == expected


def test_sum_series2():
    actual = sum_series(7, 0, 1)
    expected = "8"
    assert actual == expected
