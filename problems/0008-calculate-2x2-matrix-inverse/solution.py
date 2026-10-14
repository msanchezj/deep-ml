"""
For this exercise I didn't wanted to just copy the formula from the Reasoning ennunciate. I wanted to take a more programmatic approach, so that's why I decided to use Cayley-Hamilton. From Cayley-Hamilton theorem, we know that each matrix
satisfies their own characteristic polynom. If we develop the formula, we end
up with an explicit function for the inverse 2x2 matrix. For that, we'll need
the square of the matrix, the trace and the determinant. As these functions we're
not developed yet, we'll define them inside the inverse function.

By Cailey-Hamilton theorem after developing the characteristic polynom we have:
    A^-1 = (1/det(A))*(tr(A)*I - A)
"""

def inverse_2x2(matrix: list[list[float]]) -> list[list[float]] | None:
    """
    Calculate the inverse of a 2x2 matrix.
    
    Args:
        matrix: A 2x2 matrix represented as [[a, b], [c, d]]
    
    Returns:
        The inverse matrix as a 2x2 list, or None if the matrix is singular
        (i.e., determinant equals zero)
    """
    def subtract_matrixes(a: list[list[int|float]], b: [list[list[int|float]]]) -> list[list[int|float]]:
        return [[a[i][j] - b[i][j] for j in range(len(a))] for i in range(len(b))]

    def identity_matrix(dim: int) -> list[list[int|float]]:
        return [[1 if i == j else 0 for i in range(dim)] for j in range(dim)]

    def transpose_matrix(a: list[list[int|float]]) -> list[list[int|float]]:
        return [[a[i][j] for i in range(len(a))] for j in range(len(a[0]))]

    "This could've also been a formula..."
    def matrix_det_2x2(matrix: list[list[float]]) -> int:
        return (matrix[0][0]*matrix[1][1]) - (matrix[0][1]*matrix[1][0])

    def matrix_trace(a: list[list[int|float]]) -> int:
        return sum(a[i][i] for i in range(len(a)))

    def scalar_multiply(matrix: list[list[int|float]], scalar: int|float) -> list[list[int|float]]:
        m = len(matrix)
        n = len(matrix[0])
        return [[matrix[j][i]*scalar for i in range(m)] for j in range(n)]
    
    def vector_dot_product(a: list[int|float], b: list[int|float]) -> int|float:
        return -1 if len(a) != len(b) else sum(x * y for x, y in zip(a, b))

    def matrix_dot_product(matrix_a: list[list[int|float]], matrix_b: list[list[int|float]]) -> list[list[int|float]]:
        if (len(matrix_a) != len(matrix_b[0])):
            return []
        else:
            return [[vector_dot_product(a[j], transpose_matrix(b)[i]) for i in range(len(a))] for j in range(len(transpose_matrix(b)))]

    det = matrix_det_2x2(matrix)
    dim = len(matrix)
    if det == 0:
        return None
    else:
        det_div = 1/det
        trace_identity = scalar_multiply(identity_matrix(dim), matrix_trace(matrix))
        subtract = subtract_matrixes(trace_identity, matrix)
        inverse_matrix = scalar_multiply(subtract, det_div)
        return inverse_matrix