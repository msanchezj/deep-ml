import numpy as np

def cosine_similarity(v1, v2):
	"""
	Calculate the cosine_similarity of two vectors.
	Args:
		vec1 (numpy.ndarray): 1D array representing the first vector.
		vec2 (numpy.ndarray): 1D array representing the second vector.
	Returns:
		The cosine_similarity of the two vectors.
	"""
	def calculate_dot_product(vec1, vec2):
		return -1 if len(vec1) != len(vec2) else sum(x * y for x, y in zip(vec1, vec2))

	def calculate_vector_norm(vec):
		return np.sqrt(sum([np.power(x, 2) for x in vec]))

	return (calculate_dot_product(v2, v1)/(calculate_vector_norm(v1)*calculate_vector_norm(v2)))