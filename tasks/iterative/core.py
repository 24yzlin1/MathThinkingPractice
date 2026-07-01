import numpy as np


def _decompose_triangular(
    coefficient: np.ndarray,
) -> tuple[np.ndarray, np.ndarray]:
    unknown: int = coefficient.shape[0]
    l_matrix: np.ndarray = np.eye(unknown)
    u_matrix: np.ndarray = np.zeros((unknown, unknown))

    for i in range(unknown):
        for j in range(i, unknown):
            sum: float = 0
            for k in range(i):
                sum += l_matrix[i][k] * u_matrix[k][j]

            u_matrix[i][j] = coefficient[i][j] - sum

        for j in range(i + 1, unknown):
            sum: float = 0
            for k in range(i):
                sum += l_matrix[j][k] * u_matrix[k][i]

            l_matrix[j][i] = (coefficient[j][i] - sum) / u_matrix[i][i]

    return (
        l_matrix,
        u_matrix,
    )


def _iterate_jacobi(
    coefficient: np.ndarray,
    constant: np.ndarray,
    old_solution: np.ndarray,
) -> np.ndarray:
    unknown: int = coefficient.shape[0]
    solution: np.ndarray = np.zeros((unknown,))

    for i in range(unknown):
        sum_except_diag = (
            constant[i]
            - np.dot(coefficient[i, :], old_solution)
            + coefficient[i, i] * old_solution[i]
        )
        solution[i] = sum_except_diag / coefficient[i, i]

    return solution


def _iterate_gauss_seidel(
    coefficient: np.ndarray,
    constant: np.ndarray,
    old_solution: np.ndarray,
) -> np.ndarray:
    unknown: int = coefficient.shape[0]
    solution = old_solution.copy()

    for i in range(unknown):
        sum1 = np.dot(coefficient[i, :i], solution[:i])
        sum2 = np.dot(coefficient[i, i + 1 :], old_solution[i + 1 :])
        solution[i] = (constant[i] - sum1 - sum2) / coefficient[i, i]

    return solution


def solve_with_np_builtin(
    coefficient: np.ndarray,
    constant: np.ndarray,
) -> np.ndarray:
    return np.linalg.solve(coefficient, constant)


def solve_with_triangular_decompose(
    coefficient: np.ndarray,
    constant: np.ndarray,
) -> np.ndarray:
    unknown: int = coefficient.shape[0]
    l_matrix, u_matrix = _decompose_triangular(coefficient)

    partial_solution: np.ndarray = np.zeros((unknown,))
    for i in range(unknown):
        sum: float = 0
        for j in range(i):
            sum += l_matrix[i][j] * partial_solution[j]

        partial_solution[i] = constant[i] - sum

    true_solution: np.ndarray = np.zeros((unknown,))
    for i in range(unknown - 1, -1, -1):
        sum: float = 0
        for j in range(i, unknown):
            sum += u_matrix[i][j] * true_solution[j]

        true_solution[i] = (partial_solution[i] - sum) / u_matrix[i][i]

    return true_solution


def iterate_solution(
    coefficient: np.ndarray,
    constant: np.ndarray,
    function: str,
    init_solution: np.ndarray | None = None,
    max_iterations: int = 1000,
    tolerance: float = 1e-8,
) -> tuple[bool, int, np.ndarray]:
    unknown: int = coefficient.shape[0]
    solution = init_solution if init_solution else np.zeros(unknown)

    iteration = None
    match function:
        case "JACOBI":
            iteration = _iterate_jacobi
        case "GS":
            iteration = _iterate_gauss_seidel
        case _:
            raise

    for i in range(max_iterations):
        old_solution = solution.copy()
        solution = iteration(
            coefficient,
            constant,
            solution,
        )

        if np.linalg.norm(solution - old_solution) < tolerance:
            return (
                True,
                i + 1,
                solution,
            )

    return (
        False,
        max_iterations,
        solution,
    )


def calculate_spectral_radius(
    coefficient: np.ndarray,
    function: str,
) -> float:
    d_matrix = np.diag(np.diag(coefficient))
    l_matrix = -np.tril(coefficient, -1)
    u_matrix = -np.triu(coefficient, 1)

    iteration = None
    match function:
        case "JACOBI":
            iteration = np.linalg.inv(d_matrix) @ (l_matrix + u_matrix)
        case "GS":
            D_minus_L = d_matrix - l_matrix
            iteration = np.linalg.inv(D_minus_L) @ u_matrix
        case _:
            raise

    return np.max(np.abs(np.linalg.eigvals(iteration)))
