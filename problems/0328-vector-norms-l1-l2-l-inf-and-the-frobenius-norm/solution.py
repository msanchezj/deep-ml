"""
I've tried to avoid Numpy as much as possible as, for me, the idea here is to
refresh algorithmic concepts rather than to blindly use (amazing) mathematics
libraries
"""

import numpy as np

def compute_norm(arr: np.ndarray, norm_type: str) -> float:
    """
    Compute the specified norm of the input array.

    'l1', 'l2' and 'linf' are entrywise norms and accept a 1D or 2D array.
    'frobenius' is a matrix norm and must raise a ValueError if arr is not 2D.

    Args:
        arr: Input numpy array (1D or 2D)
        norm_type: Type of norm ('l1', 'l2', 'linf', or 'frobenius')

    Returns:
        The computed norm as a float
    """
    def l1_norm(arr):
        return sum([abs(x) for x in arr.flat])

    def l2_norm(arr):
        return np.sqrt(sum([x**2 for x in arr.flat]))

    def linf_norm(arr):
        return max([abs(x) for x in arr.flat])

    def frobenius_norm(arr):
        if arr.ndim != 2:
            raise ValueError("ValueError")
            
        return np.sqrt(sum([abs(arr[i][j]**2) for i in range(len(arr)) for j in range(len(arr[0]))]))

    switcher = {
        'l1': l1_norm,
        'l2': l2_norm,
        'linf': linf_norm,
        'frobenius': frobenius_norm,
    }

    if norm_type not in switcher:
        raise ValueError(f"Invalid norm: {norm_type}")

    return float(switcher[norm_type](arr))
        
