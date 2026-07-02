import numpy as np
from core import iterate_solution, solve_with_np_builtin
from visualize import plot_matrix_heatmap, plot_error_curves, plot_solution_comparison

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


exact_x = solve_with_np_builtin(a_matrix, b_vector)


success_j, steps_j, jacobi_x, jacobi_hist = iterate_solution(
    coefficient=a_matrix,
    constant=b_vector,
    function="JACOBI"
)


success_gs, steps_gs, gs_x, gs_hist = iterate_solution(
    coefficient=a_matrix,
    constant=b_vector,
    function="GS"
)


plot_matrix_heatmap(a_matrix)

plot_error_curves(jacobi_hist, gs_hist)

plot_solution_comparison(exact_x, jacobi_x, gs_x)