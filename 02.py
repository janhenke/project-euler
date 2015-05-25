#! /usr/bin/env python3

from common.fibo import fibo

def main():
	fibs = fibo(4000000)

	sum = 0

	for x in fibs:
		if x%2 == 0:
			sum += x

	print(sum)

if __name__ == '__main__':
	main()
