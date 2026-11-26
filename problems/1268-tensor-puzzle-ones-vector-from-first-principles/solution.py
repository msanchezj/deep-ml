import numpy as np

def ones(n: int) -> np.ndarray:
    """Return a length-n float vector of ones without calling np.ones."""
    return np.array([i/i for i in np.arange(1, n+1)])
    
