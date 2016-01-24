#!/usr/bin/env python3
"""Solves problem 023 from the Project Euler website"""

from common.divisor import proper_divisors


def is_abundant_number(n):
    return n < sum(proper_divisors(n))


def solve():
    """Solve the problem and return the result"""

    # first find all abundant numbers at or below 28123
    abundant_numbers = set()
    for i in range(1, 28123 + 1):
        if is_abundant_number(i):
            abundant_numbers.add(i)

    # now find all numbers in range [1,28123], which are not the sum of two abundant numbers
    result = set()
    for i in range(1, 28123 + 1):
        for j in abundant_numbers:
            if j >= i:
                result.add(i)
            elif i - j in abundant_numbers:
                break

    return sum(result)


if __name__ == '__main__':
    print(solve())
