# this method returns processor time; by substracting time measured at the begining of function
# from the time measured at the end of it we get precise time of calculation, without slowing down calculations
from time import clock


def fibonacciRec(n):
    ''' returns (n+1)th number of fibonacci series recursion '''

    if n == 0:
        return 1

    elif n == 1:
        return 1

    else:
        return fibonacciRec(n-1)+fibonacciRec(n-2)


def fibonacciIte(n):
    ''' return (n+1)th number of Fibonacci series iteration'''
    first = 0
    second = 1
    i = 0
    value = 1
    start = clock()  # measurement of processor time just as calculation begins
    while (i < n):
        value = first + second
        first = second
        second = value
        i += 1

    end = clock()  # measurement of processor time just as calculation ends
    diff = end - start  # this is the time of our calculation
    return value, diff


if __name__ == '__main__':
    # fibonacciRec(number) returnes value of (number+1) value of fibonacci series
    value = fibonacciRec(6)
    assert value == 13

    # fibonacciIte(number) returnes value of (number+1) value of fibonacci series
    # and the time in which it was calculated
    value2, time = fibonacciIte(6)
    assert value2 == 13, 0.0 < time
