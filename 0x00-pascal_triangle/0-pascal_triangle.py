"""
Module that returns a list of lists
of integers representing the Pascal's
triangle of n
"""

def pascal_triangle(n):
	"""
	Function that returns a list of lists
	of integers representing the Pascal's
	triangle of n
	"""
	triangle = [[1]]
	if n <= 0:
		return [[]]
	else:
		for _ in range(1,n):
			temp = [1]
			for i in range(len(triangle[-1])):
				if i+1 < len(triangle[-1]):
					temp.append(triangle[-1][i] + triangle[-1][1+i])
			temp.append(1)
			triangle.append(temp)
		return triangle