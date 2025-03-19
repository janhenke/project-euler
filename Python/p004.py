#! /usr/bin/env python3
"""Solves problem 004 from the Project Euler website"""


def is_palindrome(number):
    """Test if 'number' is a palindrome

    :param number: The number to test
    """
    n = str(number)
    reverse = n[::-1]
    return n == reverse


def solve():
    """Solve the problem and return the result"""
    candidates = []
    for x in range(999, 1, -1):
        for y in range(999, 1, -1):
            if is_palindrome(x * y):
                candidates.append(x * y)
    candidates.sort()
    return candidates[-1]


if __name__ == '__main__':
    print(solve())
