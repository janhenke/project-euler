#! /usr/bin/env python3
"""Solves problem 006 from the Project Euler website"""


def solve():
    """Solve the problem and return the result"""
    sumsquares = 0
    sumsquared = 0

    for x in range(1, 101):
        sumsquares += (x ** 2)
        sumsquared += x
    sumsquared **= 2

    return (sumsquared - sumsquares)


if __name__ == '__main__':
    print(solve())
