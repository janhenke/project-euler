#!/usr/bin/env python3
"""Solves problem 022 from the Project Euler website"""

characters_to_numbers = {'A': 1,
                         'B': 2,
                         'C': 3,
                         'D': 4,
                         'E': 5,
                         'F': 6,
                         'G': 7,
                         'H': 8,
                         'I': 9,
                         'J': 10,
                         'K': 11,
                         'L': 12,
                         'M': 13,
                         'N': 14,
                         'O': 15,
                         'P': 16,
                         'Q': 17,
                         'R': 18,
                         'S': 19,
                         'T': 20,
                         'U': 21,
                         'V': 22,
                         'W': 23,
                         'X': 24,
                         'Y': 25,
                         'Z': 26}


def solve():
    """Solve the problem and return the result"""
    result = 0
    temp = 0

    with open('p022_names.txt') as file:
        names = file.read().split(',')
        names.sort()

    for i, name in enumerate(names):
        for c in name.replace('"', ''):
            temp += characters_to_numbers[c]
        result += (i + 1) * temp
        temp = 0

    return result


if __name__ == '__main__':
    print(solve())
