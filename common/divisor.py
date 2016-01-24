#!/usr/bin/env python3
"""This module provides functions to find the divisors of numbers"""
from math import floor,sqrt


def proper_divisors(n):
    """Return the set of proper divisors of 'n'.

    That is the set of divisors without 'n' itself (divisors(n)/n)
    :param n: The number to find the proper divisors of
    :return: The set of proper divisors
    """
    result = set()
    if n == 0 or n < 0:
        return result
    else:
        result.add(1)

    r = floor(sqrt(n))
    # handle square numbers
    if r * r == n:
        result.add(r)
        r -= 1
    # odd numbers cannot divided by even numbers
    if n % 2 != 0:
        f = 3
        step = 2
    else:
        f = 2
        step = 1

    while f <= r:
        if n % f == 0:
            result.add(f)
            result.add(n // f)
        f += step
    return result


def divisors(n):
    """Return the set of divisors of 'n'.

    :param n: The number to find the divisors of
    :return: The set of divisors
    """
    result = proper_divisors(n)
    result.add(n)
    return result
