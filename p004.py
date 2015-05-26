#! /usr/bin/env python3

def is_palindrome(number):
	n = str(number)
	for x in range(1,len(n)):
		if n[x-1] != n[-x]:
			return False
	return True

def main():
	candidates = []
	for x in range(999,1,-1):
		for y in range (999,1,-1):
			if is_palindrome(x*y):
				candidates.append(x*y)
	candidates.sort()
	print(candidates[-1])

if __name__ == '__main__':
	main()