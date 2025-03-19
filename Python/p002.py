#! /usr/bin/env python3
"""Solves problem 002 from the Project Euler website"""

from common.fibonacci import fibonacci_numbers_below


def solve():
    """Solve the problem and return the result"""
    fibs = fibonacci_numbers_below(4000000)

    result = 0

    for x in fibs:
        if x % 2 == 0:
            result += x

    return result


if __name__ == '__main__':
    print(solve())
