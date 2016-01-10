#! /usr/bin/env python3
"""Solves problem 008 from the Project Euler website"""

def solve():
    """Solve the problem and return the result"""
    # Invariants:
    # a**2+b**2=c**2
    # a < b < c
    # a+b+c=1000 -> c = 1000 - a - b
    for b in range(1, 501):
        for a in range(1, b):
            c = 1000 - a - b
            if a ** 2 + b ** 2 == c ** 2:
                return (a * b * c)


if __name__ == '__main__':
    print(solve())
