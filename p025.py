#!/usr/bin/env python3
"""Solves problem 025 from the Project Euler website"""
from common.fibonacci import fibonacci_numbers_until_n_digits


def solve():
    """Solve the problem and return the result"""
    fibonacci_numbers = fibonacci_numbers_until_n_digits(1000)
    result = len(fibonacci_numbers)

    return result


if __name__ == '__main__':
    print(solve())
