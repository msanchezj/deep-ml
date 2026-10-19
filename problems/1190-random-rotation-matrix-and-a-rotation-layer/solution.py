import math
import numpy as np

def rotation_layer(X, angle):
    def build_2d_rotation_matrix(angle: int|float) -> list[list[int|float]]:
        return [[math.cos(angle), -1*math.sin(angle)] if i == 0 else [math.sin(angle), math.cos(angle)] for i in range(2)]

    rotation_matrix = build_2d_rotation_matrix(angle)
    return np.dot(X, np.array(rotation_matrix).T)