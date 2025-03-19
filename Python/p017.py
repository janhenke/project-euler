#!/usr/bin/env python3
"""Solves problem xxx from the Project Euler website"""


def solve():
    """Solve the problem and return the result"""
    oneToNine = sum(
            [len('one'),
             len('two'),
             len('three'),
             len('four'),
             len('five'),
             len('six'),
             len('seven'),
             len('eight'),
             len('nine')])
    oneToNintynine = 10 * sum(
            [len('twenty'),
             len('thirty'),
             len('forty'),
             len('fifty'),
             len('sixty'),
             len('seventy'),
             len('eighty'),
             len('ninety')]) + sum(
            [len('ten'),
             len('eleven'),
             len('twelve'),
             len('thirteen'),
             len('fourteen'),
             len('fifteen'),
             len('sixteen'),
             len('seventeen'),
             len('eighteen'),
             len('nineteen')]) + 9 * oneToNine

    result = len('one') + len('thousand') + 100 * (9 * len('hundred') + oneToNine) + 99 * 9 * len(
        'and') + 10 * oneToNintynine
    return result


if __name__ == '__main__':
    print(solve())
