#! /usr/bin/env python3

from math import ceil, sqrt


def find_devisors(num):
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


def main():
    divs = []
    num = 0
    i = 1

    while len(divs) <= 500:
        num += i
        i += 1
        divs = find_devisors(num)

    print(num)


if __name__ == '__main__':
    main()
