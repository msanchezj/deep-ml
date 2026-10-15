import numpy as np

def make_diagonal(x):
	def identity_matrix(dim: int) -> list[list[int|float]]:
		return [[1 if i == j else 0 for i in range(dim)] for j in range(dim)]
	dim = len(x)
	identity = identity_matrix(dim)
	diagonal = [[identity[i][j]*x[i] if i == j else identity[i][j] for i in range(dim)] for j in range(dim)]
	return diagonal