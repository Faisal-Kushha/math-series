from math_series import __version__
from math_series.series import fibonacci, lucas, sum_series


def test_version():
    assert __version__ == '0.1.0'


def test_fibonacci():
    actual = fibonacci(5)
    expected = "3"
    assert actual == expected
