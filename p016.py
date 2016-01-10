#!/usr/bin/env python3
"""Solves problem xxx from the Project Euler website"""


def solve():
    """Solve the problem and return the result"""
    number = 2 ** 1000
    result = 0

    for i in str(number):
        result += int(i)

    return result


if __name__ == '__main__':
    print(solve())
