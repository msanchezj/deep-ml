import numpy as np

def flip(a: np.ndarray) -> np.ndarray:
    """Reverse 1-D array a without slicing a[::-1]."""
    return np.array([a[len(a)-1-i] for i in np.arange(len(a))])
