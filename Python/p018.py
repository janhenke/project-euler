#!/usr/bin/env python3
"""Solves problem 018 from the Project Euler website"""

triangle = [[95, 64],
            [17, 47, 82],
            [18, 35, 87, 10],
            [20, 4, 82, 47, 65],
            [19, 1, 23, 75, 3, 34],
            [88, 2, 77, 73, 7, 63, 67],
            [99, 65, 4, 28, 6, 16, 70, 92],
            [41, 41, 26, 56, 83, 40, 80, 70, 33],
            [41, 48, 72, 33, 47, 32, 37, 16, 94, 29],
            [53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14],
            [70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57],
            [91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48],
            [63, 66, 4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31],
            [4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23]]


def solve():
    """Solve the problem and return the result"""
    result = 75
    row = 0
    position = 0
    left = 0
    right = 0

    while row < len(triangle):
        left = triangle[row][position]
        right = triangle[row][position + 1]

        if row + 1 < len(triangle):
            if triangle[row + 1][position] >= triangle[row + 1][position + 1]:
                left += triangle[row + 1][position]
            else:
                left += triangle[row + 1][position + 1]
            if triangle[row + 1][position + 1] >= triangle[row + 1][position + 2]:
                right += triangle[row + 1][position + 1]
            else:
                right += triangle[row + 1][position + 2]

        if left >= right:
            result += triangle[row][position]
        else:
            result += triangle[row][position + 1]
            position += 1

        row += 1

    return result


if __name__ == '__main__':
    print(solve())
