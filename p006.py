#! /usr/bin/env python3



def main():
	sumsquares = 0
	sumsquared = 0

	for x in range(1,101):
		sumsquares += (x**2)
		sumsquared += x
	sumsquared = sumsquared ** 2

	print(sumsquared - sumsquares)

if __name__ == '__main__':
	main()