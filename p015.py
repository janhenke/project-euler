#!/usr/bin/env python3
"""Solves problem 015 from the Project Euler website"""

from common.binomial import binomial_coefficient


def solve():
    """Solve the problem and return the result"""
    # the amount of lattice paths from (0, 0) to (n, k) is (n+k) over n (according to Wikipedia)
    return binomial_coefficient(20 + 20, 20)


if __name__ == '__main__':
    print(solve())
