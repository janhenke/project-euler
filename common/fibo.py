#! /usr/bin/env python3

def fibo(limit):
	a, b = 0, 1
	result = []
	while b < limit:
		result.append(b)
		a, b = b, a+b
	return result
