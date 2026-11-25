import numpy as np

def diag(A: np.ndarray) -> np.ndarray:
    """Return the main diagonal of square matrix A."""
    m, n = A.shape
    flat = A.flatten()

    return [flat[i*m+i] for i in range(m)]
