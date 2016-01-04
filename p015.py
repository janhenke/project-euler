#!/usr/bin/env python3

gridX = 20
gridY = 20

def find_paths(point):
	if point[0] == gridX or point[1] == gridY:
		return point

def main():
	result = find_paths((0,0))

	print(len(result))

if __name__ == '__main__':
	main()