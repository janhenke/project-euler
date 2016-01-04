#! /usr/bin/env python3

from common.prime import prime_factors


def main():
    result = 1
    map = dict()
    for x in range(2, 20):
        temp = prime_factors(x)
        for n in range(2, 20):
            if n in temp:
                if n in map:
                    map[n] = max(temp.count(n), map[n])
                else:
                    map[n] = temp.count(n)

    for x in map:
        result *= (x ** map[x])
    print(result)


if __name__ == '__main__':
    main()
