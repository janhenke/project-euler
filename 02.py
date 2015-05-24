#! /usr/bin/env python3

fibs = [1]

def genFibs(limit):
	a = 1
	b = 1
	temp = 0

	while b <= limit:
		temp = a + b
		a = b
		b = temp
		fibs.append(b)

def main():
	genFibs(4000000)

	sum = 0

	for x in fibs:
		if x%2 == 0:
			sum += x

	print(sum)

if __name__ == '__main__':
	main()