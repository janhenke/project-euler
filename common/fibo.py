#! /usr/bin/env python3
"""A module defining fibonacci number related functions.
"""


def fibo(limit):
    """Returns the list of fibonacci numbers smaller than limit.
    """
    a, b = 0, 1
    result = []
    while b < limit:
        result.append(b)
        a, b = b, a + b
    return result
