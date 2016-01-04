#! /usr/bin/env python3

from common.prime import prime_numbers


def main():
    primes = prime_numbers(10001)
    print(primes[-1])


if __name__ == '__main__':
    main()
