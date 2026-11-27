import numpy as np

def cross_product(a, b):
    return (np.roll(a, -1) * np.roll(b, 1)) - (np.roll(a, 1) * np.roll(b, -1))