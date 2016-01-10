#! /usr/bin/env python3
"""Solves problem 001 from the Project Euler website"""


def solve():
    """Solve the problem and return the result"""
    result = 0

    for x in range(1, 1000):
        if x % 3 == 0 or x % 5 == 0:
            result += x

    return result


if __name__ == '__main__':
    print(solve())
