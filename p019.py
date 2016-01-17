#!/usr/bin/env python3
"""Solves problem 019 from the Project Euler website"""

days_in_month = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)


def solve():
    """Solve the problem and return the result"""
    result = 0
    # January 1st 1901 is a Tuesday
    day_of_week = 1
    year = 1901

    while year <= 2000:
        for month in range(12):
            day_of_week += days_in_month[month]
            day_of_week %= 7
            # Add one extra day in February if it is a leap year
            if month == 1 and year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
                day_of_week += 1
                day_of_week %= 7

            if day_of_week == 6:
                result += 1

        year += 1

    return result


if __name__ == '__main__':
    print(solve())
