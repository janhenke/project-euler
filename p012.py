#! /usr/bin/env python3
"""Solves problem 012 from the Project Euler website"""

from math import ceil, sqrt


def find_devisors(num):
    """Find all divisors of 'num'

    :param num: The number for which the divisors will be found
    """
    limit = ceil(sqrt(num))
    result = []
    temp = []
    for x in range(1, limit):
        if (num % x) == 0:
            result.append(x)

    for i, x in enumerate(result):
        temp.append(int(num / x))

    temp.reverse()
    result += temp

    return result


def solve():
    """Solve the problem and return the result"""
    divs = []
    num = 0
    i = 1

    while len(divs) <= 500:
        num += i
        i += 1
        divs = find_devisors(num)

    return num


if __name__ == '__main__':
    print(solve())
