#! /usr/bin/env python3
"""Solves problem 007 from the Project Euler website"""

from common.prime import first_n_prime_numbers


def solve():
    """Solve the problem and return the result"""
    primes = first_n_prime_numbers(10001)
    return primes[-1]


if __name__ == '__main__':
    print(solve())
