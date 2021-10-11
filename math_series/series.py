def fibonacci(n):
    """
    The Fibonacci Series is a numeric series starting with the integers 0 and 1. The next integer is determined by summing the previous two.
    """
    array = [0, 1, 1, 2, 3, 5, 8, 13]
    for i in range(0, n):
        number = array[i] + array[i+1]
        array.append(number)
    return str(array[n-1])


def lucas(n):
    """
    The Lucas Numbers are a related series of integers that start with the values 2 and 1. The next integer is determined by summing the previous two.
    """
    array = [2, 1, 3, 4, 7, 11, 18, 29]
    for i in range(0, n):
        number = array[i] + array[i+1]
        array.append(number)
    return str(array[n-1])


number_one = 0
number_two = 1


def sum_series(n, number_one, number_two):
    """
    Sum series function with one required parameter and two optional parameters. The required parameter will determine which element in the series to print. The two optional parameters will have default values of 0 and 1 and will determine the first two values for the series to be produced.
    """
    array = [number_one, number_two]
    for i in range(0, n):
        number = array[i] + array[i+1]
        array.append(number)
    return str(array[n-1])


if __name__ == "__main__":
    """
    fibonacci( )
    lucas( )
    sum_series( )
    """
