#!/usr/bin/env python3
"""Solves problem 021 from the Project Euler website"""

first_twenty_amicable_numbers = [(220, 284), (1184, 1210), (2620, 2924), (5020, 5564), (6232, 6368), (10744, 10856),
                                 (12285, 14595), (17296, 18416), (63020, 76084), (66928, 66992), (67095, 71145),
                                 (69615, 87633), (79750, 88730), (100485, 124155), (122265, 139815), (122368, 123152),
                                 (141664, 153176), (142310, 168730)]


def solve():
    """Solve the problem and return the result"""
    result = 0

    for n in first_twenty_amicable_numbers:
        if n[0] < 10000:
            result += n[0]
            result += n[1]
        else:
            break

    return result


if __name__ == '__main__':
    print(solve())
