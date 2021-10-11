def fibonacci(n):
    """
    The Fibonacci Series is a numeric series starting with the integers 0 and 1. The next integer is determined by summing the previous two.
    """
    array = [0, 1, 1, 2, 3, 5, 8, 13]
    for i in range(0, n):
        number = array[i] + array[i+1]
        array.append(number)
    return str(array[n+1])


def lucas(n):
    """
    The Lucas Numbers are a related series of integers that start with the values 2 and 1. The next integer is determined by summing the previous two.
    """
    array = [2, 1, 3, 4, 7, 11, 18, 29]
    for i in range(0, n):
        number = array[i] + array[i+1]
        array.append(number)
    return str(array[n+1])
