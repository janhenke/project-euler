#!/usr/bin/env python3
"""Solves problem 020 from the Project Euler website"""


from math import factorial

def solve():
    """Solve the problem and return the result"""
    result = 0

    for i in str(factorial(100)):
        result += int(i)

    return result


if __name__ == '__main__':
    print(solve())
