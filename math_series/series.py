

def fibonacci(n):
    """
    The Fibonacci Series is a numeric series starting with the integers 0 and 1. The next integer is determined by summing the previous two.
    """
    array = [0, 1, 1, 2, 3, 5, 8, 13]
    for i in range(0, n):
        number = array[i] + array[i+1]
        array.append(number)
    return str(array[n+1])
