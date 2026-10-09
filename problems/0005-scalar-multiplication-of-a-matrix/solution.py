def scalar_multiply(matrix: list[list[int|float]], scalar: int|float) -> list[list[int|float]]:
	"""
    There are different ways to solve this (simple) exercise.
	As there's no default import I think the purpose is to think
	for the algorithm. This could be easily solved with numpy
	or product from itertools, but I've decided to solve it
	using pure Python (double list comprehension)
    """
	m = len(matrix)
	n = len(matrix[0])
	return [[matrix[j][i]*scalar for i in range(m)] for j in range(n)]