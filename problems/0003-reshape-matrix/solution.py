import numpy as np

def reshape_matrix(a: list[list[int|float]], new_shape: tuple[int, int]) -> list[list[int|float]]:
	#Write your code here and return a python list after reshaping by using numpy's tolist() method
	m = len(a)
	n = len(a[0])
	m_new = new_shape[0]
	n_new = new_shape[1]
	if ((m_new*n_new) == (m*n)):
		flat = np.ravel(a)
		reshaped_matrix = [flat[i:i+n_new].tolist() for i in range(0, m_new*n_new, n_new)]
	else:
		reshaped_matrix = []
	return reshaped_matrix