#! /usr/bin/env python3

def main():
    # Invarianten:
    # a**2+b**2=c**2
    # a < b < c
    # a+b+c=1000 -> c = 1000 - a - b
    for b in range(1, 501):
        for a in range(1, b):
            c = 1000 - a - b
            if a ** 2 + b ** 2 == c ** 2:
                print(a, b, c)
                print(a * b * c)
                return


if __name__ == '__main__':
    main()
