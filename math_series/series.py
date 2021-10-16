def fibonacci(n):
    """
    The Fibonacci Series is a numeric series starting with the integers 0 and 1. The next integer is determined by summing the previous two.
    This function will solve the Fibonacci series by taking one parameter (integer) and will return the results by using a recursion formula.
    """
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)


def lucas(n):
    """
    The Lucas Numbers are a related series of integers that start with the values 2 and 1. The next integer is determined by summing the previous two.
    This function will solve the Lucas series by taking one parameter (integer) and will return the results by using a recursion formula.
    """
    if n == 0:
        return 2
    if n == 1:
        return 1
    return lucas(n-1) + lucas(n-2)


def sum_series(n, number_one=0, number_two=1):
    """
    Sum series function with one required parameter and two optional parameters. The required parameter will determine which element in the series to print. The two optional parameters will have default values of 0 and 1 and will determine the first two values for the series to be produced. And will return the results by using a recursion formula.
    """
    if n == 0:
        return number_one
    if n == 1:
        return number_two
    return sum_series(n-1, number_one, number_two) + sum_series(n-2, number_one, number_two)


if __name__ == "__main__":
    """
    fibonacci( )
    lucas( )
    sum_series( )
    """
