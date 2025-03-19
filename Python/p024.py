#!/usr/bin/env python3
"""Solves problem 024 from the Project Euler website"""
from common.permutation import nth_permute_lexicographically


def solve():
    """Solve the problem and return the result"""
    sequence = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    nth_permute_lexicographically(sequence, 1000000)

    result = ''
    for i in range(len(sequence)):
        result += str(sequence[i])

    return result


if __name__ == '__main__':
    print(solve())
