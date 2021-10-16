from math_series import __version__
from math_series.series import fibonacci, lucas, sum_series


def test_version():
    assert __version__ == '0.1.0'


"""
Fibonacci Series test
"""


def test_fibonacci():
    actual = fibonacci(5)
    expected = 5
    assert actual == expected


"""
Lucas Numbers test
"""


def test_lucas():
    actual = lucas(6)
    expected = 18
    assert actual == expected


"""
Sum series tests with and without the two optional parameters
"""


def test_sum_series1():
    actual = sum_series(4, 2, 1)
    print(actual)
    expected = 7
    assert actual == expected


def test_sum_series2():
    actual = sum_series(7)
    expected = 13
    assert actual == expected


def test_sum_series3():
    actual = sum_series(3, 4, 5)
    print(actual)
    expected = 14
    assert actual == expected
