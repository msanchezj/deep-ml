import numpy as np

def row_normalize(counts: list[list[float]]) -> list[list[float]]:
    """Convert a count matrix into a row-stochastic probability matrix."""
    m = len(counts)
    n = len(counts[0])
    return [[float(counts[j][i]/np.sum(counts[j])) if np.sum(counts[j]) > 0 else [0 for i in range(m)][0] for i in range(m)] for j in range(n)]