#! /usr/bin/env python3
"""Solves problem 005 from the Project Euler website"""

from common.prime import prime_factors


def solve():
    """Solve the problem and return the result"""
    result = 1
    map = dict()
    for x in range(2, 20):
        temp = prime_factors(x)
        for n in range(2, 20):
            if n in temp:
                if n in map:
                    map[n] = max(temp.count(n), map[n])
                else:
                    map[n] = temp.count(n)

    for x in map:
        result *= (x ** map[x])

    return result


if __name__ == '__main__':
    print(solve())
