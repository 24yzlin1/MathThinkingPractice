import numpy as np
import typing as t

from core import *


class Dataset(t.TypedDict):
    a_matrix: np.ndarray
    b_vector: np.ndarray


set1: Dataset = {
    "a_matrix": np.array(
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
    ),
    "b_vector": np.array([180, 100, 120, 80, 0, 20, 80, 0, 20]),
}


set2: Dataset = {
    "a_matrix": np.array(
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
    ),
    "b_vector": np.array([350, 200, 300, 150, 0, 100, 200, 50, 150]),
}


set3: Dataset = {
    "a_matrix": np.array(
        [
            [4, -1.5, 0, -1, 0, 0, 0, 0, 0],
            [-1.5, 4, -1, 0, -1, 0, 0, 0, 0],
            [0, -1, 4, 0, 0, -1, 0, 0, 0],
            [-1, 0, 0, 4, -1, 0, -1, 0, 0],
            [0, -1, 0, -1, 4, -1.5, 0, -1, 0],
            [0, 0, -1, 0, -1.5, 4, 0, 0, -1],
            [0, 0, 0, -1, 0, 0, 4, -1, 0],
            [0, 0, 0, 0, -1, 0, -1, 4, -1],
            [0, 0, 0, 0, 0, -1, 0, -1, 4],
        ]
    ),
    "b_vector": np.array([310, 180, 250, 130, 0, 70, 170, 40, 110]),
}


def test_iterative_methods(set: Dataset) -> None:
    np.set_printoptions(
        precision=2,
        suppress=True,
        floatmode="fixed",
    )

    a_matrix = set["a_matrix"]
    b_vector = set["b_vector"]

    print(f"Coefficient matrix A:\n{a_matrix}")
    print(f"Constant vector b:\n{b_vector}")
    print()

    x_np = solve_with_np_builtin(a_matrix, b_vector)
    print("NumPy built-in solution (np.linalg.solve):")
    print(f"\tSolution vector: {x_np}")
    print()

    converged, iteration, x_gs = iterate_solution(a_matrix, b_vector, "GS")
    print("Gauss-Seidel iteration:")
    print(f"\tConverged: {converged}\tIterations: {iteration}")
    print(f"\tSolution vector: {x_gs}")
    print()

    converged, iteration, x_jacobi = iterate_solution(a_matrix, b_vector, "JACOBI")
    print("Jacobi iteration:")
    print(f"\tConverged: {converged}\tIterations: {iteration}")
    print(f"\tSolution vector: {x_jacobi}")
    print()


# def test_visualize(set: Dataset) -> None:
#     ()


# Run the test on all three provided datasets
# test_iterative_methods(set1)
# test_iterative_methods(set2)
# test_iterative_methods(set3)
