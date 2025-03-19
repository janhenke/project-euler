#! /usr/bin/env python3
"""This module provides functions related to binomials."""

from math import factorial


def binomial_coefficient(n, k):
    """Calculate the binomial coefficient 'n over k'

    :param n: The value of 'n'
    :param k: The value of 'k'
    """
    if k < 0 or n < k:
        raise ValueError('Invariant 0 <= k <= n violated', n, k)

    return factorial(n) // (factorial(k) * factorial(n - k))
