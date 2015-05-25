#! /usr/bin/env python3

from common import prime

def main():
	num = prime.prime_factors(600851475143)
	print(num[-1])

if __name__ == '__main__':
	main()