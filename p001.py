#! /usr/bin/env python3

def main():
    sum = 0

    for x in range(1, 1000):
        if x % 3 == 0 or x % 5 == 0:
            sum += x

    print(sum)


if __name__ == '__main__':
    main()
