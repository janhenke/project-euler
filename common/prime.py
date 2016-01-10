#! /usr/bin/env python3
"""A module defining prime number related functions."""


def is_prime(n):
    """Returns True if n is a prime number.

    :param n: The nummer to test
    """
    if n == 2 or n == 3: return True
    if n < 2 or n % 2 == 0: return False
    if n < 9: return True
    if n % 3 == 0: return False
    r = int(n ** 0.5)
    f = 5
    while f <= r:
        if n % f == 0: return False
        if n % (f + 2) == 0: return False
        f += 6
    return True


def prime_factors(n):
    """Returns the list of prime factors of n.

    :param n: The number for which the prime factors are returned
    """
    result = []
    x = 2
    while x <= n:
        if n % x == 0:
            result.append(x)
            n = n / x
        else:
            x += 1
    return result


def first_n_prime_numbers(n):
    """Returns the list of the first n prime numbers.

    :param n: The number of the prime numbers, so that len(result) == n
    """
    result = []
    count = 0
    x = 2
    while count < n:
        if is_prime(x):
            result.append(x)
            count += 1
        x += 1
    return result


def prime_numbers_below(n):
    """Returns the list of all prime numbers smaller than n.

    :param n: The limit for the prime numbers, so that result[-1] < n
    """
    result = []
    x = 2
    while x < n:
        if is_prime(x):
            result.append(x)
        x += 1
    return result
