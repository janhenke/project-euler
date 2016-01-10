#! /usr/bin/env python3
"""Solves problem 003 from the Project Euler website"""

from common import prime


def solve():
    """Solve the problem and return the result"""
    num = prime.prime_factors(600851475143)
    return num[-1]


if __name__ == '__main__':
    print(solve())
