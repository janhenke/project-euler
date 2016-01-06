#!/usr/bin/env python3

from common.binomial import binomial_coefficient


def main():
    # the amount of lattice paths from (0, 0) to (n, k) is (n+k) over n (according to Wikipedia)
    print(binomial_coefficient(20 + 20, 20))


if __name__ == '__main__':
    main()
