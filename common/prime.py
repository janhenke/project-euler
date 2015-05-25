#! /usr/bin/env python3
"""A module defining prime number related functions.
"""

def is_prime(n):
	"""Returns True if n is a prime number.
	"""
	if n == 2 or n == 3: return True
	if n < 2 or n%2 == 0: return False
	if n < 9: return True
	if n%3 == 0: return False
	r = int(n**0.5)
	f = 5
	while f <= r:
		if n%f == 0: return False
		if n%(f+2) == 0: return False
		f +=6
	return True

def prime_factors(n):
	"""Returns the list of prime factors of n.
	"""
	result = []
	x = 2
	while x <= n:
		if n%x == 0:
			result.append(x)
			n = n/x
		else:
			x += 1
	return result
