#! /usr/bin/env python3
"""Solves problem 010 from the Project Euler website"""

from common.prime import prime_numbers_below


def solve():
    """Solve the problem and return the result"""
    result = 0
    primes = prime_numbers_below(2000000)
    for x in primes:
        result += x

    return result


if __name__ == '__main__':
    print(solve())
