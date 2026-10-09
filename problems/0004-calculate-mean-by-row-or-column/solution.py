import numpy as np

def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
	matrix_np = np.array(matrix)
	if mode == 'column':
		matrix_np = matrix_np.T
	means = [np.mean(matrix_np[i]) for i in range(matrix_np.shape[0])]
	return means