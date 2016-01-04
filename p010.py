#! /usr/bin/env python3

from common.prime import prime_numbers_below


def main():
    result = 0
    primes = prime_numbers_below(2000000)
    for x in primes:
        result += x
    print(result)


if __name__ == '__main__':
    main()
