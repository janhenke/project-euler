#! /usr/bin/env python3
"""A module defining fibonacci number related functions."""


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
