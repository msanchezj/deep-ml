import numpy as np

def vstack(a: np.ndarray, b: np.ndarray) -> np.ndarray:
    return [[(a if i == 0 else b)[j] for j in range(len(a))] for i in range(2)]
