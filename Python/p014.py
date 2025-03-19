#!/usr/bin/env python3
"""Solves problem 014 from the Project Euler website"""

availableNumbers = set()


def generate_collatz_sequence(start):
    """Generates the collatz sequence from the given start value

    :param start: The start value
    """
    result = [start]
    current = start
    while current != 1:
        if current % 2 == 0:
            current = current // 2
        else:
            current = current * 3 + 1

        result.append(current)
        availableNumbers.discard(current)

    return result


def solve():
    """Solve the problem and return the result"""
    count = 999999
    result = []
    temp = []

    # Fill set with all numbers
    for x in range(1000000):
        availableNumbers.add(x)

    while count >= 1:
        temp = generate_collatz_sequence(count)
        if len(temp) > len(result):
            result = temp

        count -= 1
        while not count in availableNumbers:
            count -= 1

    return result[0]


if __name__ == '__main__':
    print(solve())
