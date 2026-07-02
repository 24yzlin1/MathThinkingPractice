import numpy as np

from core import *

a_matrix: np.ndarray = np.array(
    [
        [4, -1, 0, -1, 0, 0, 0, 0, 0],
        [-1, 4, -1, 0, -1, 0, 0, 0, 0],
        [0, -1, 4, 0, 0, -1, 0, 0, 0],
        [-1, 0, 0, 4, -1, 0, -1, 0, 0],
        [0, -1, 0, -1, 4, -1, 0, -1, 0],
        [0, 0, -1, 0, -1, 4, 0, 0, -1],
        [0, 0, 0, -1, 0, 0, 4, -1, 0],
        [0, 0, 0, 0, -1, 0, -1, 4, -1],
        [0, 0, 0, 0, 0, -1, 0, -1, 4],
    ]
)

b_vector: np.ndarray = np.array([180, 100, 120, 80, 0, 20, 80, 0, 20])

print(solve_with_np_builtin(a_matrix, b_vector))
print(solve_with_triangular_decompose(a_matrix, b_vector))
print(iterate_solution(a_matrix, b_vector, "GS"))
