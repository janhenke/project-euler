#! /usr/bin/env python3
"""A module defining fibonacci number related functions."""


def first_n_fibonacci_numbers(n):
    """Return the list of the first 'n' fibonacci numbers.

    :param n: The number of the fibonacci numbers, so that len(result) == n
    :return: The list of the first fibonacci numbers with length 'n'
    """
    result = []
    count = 0
    a, b = 0, 1
    while count < n:
        result.append(b)
        count += 1
        a, b = b, a + b
    return result


def fibonacci_numbers_below(n):
    """Return the list of fibonacci numbers smaller than 'n'.

    :param n: The limit of the generated number, so that result[-1] < n
    """
    a, b = 0, 1
    result = []
    while b < n:
        result.append(b)
        a, b = b, a + b
    return result


def fibonacci_numbers_until_n_digits(n):
    """Return the list fibonacci numbers until the latest has at lest n digits

    :type n: The minimum amount of digits for the last fibonacci number in the list
    """
    result = []
    a, b = 0, 1
    while len(str(b)) < n:
        result.append(b)
        a, b = b, a + b
    result.append(b)
    return result
