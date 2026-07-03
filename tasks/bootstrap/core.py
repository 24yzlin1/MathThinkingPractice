import random
import numpy as np
import typing as t


class Distribution(t.TypedDict):
    samples: list[list[float]]
    bootstrap: list[float]
    median: float
    point_estimate: float
    standard_error: float
    standard_error_interval: tuple[float, float]
    confidence_interval: tuple[float, float]


statistical_functions: dict[str, t.Callable[[list[float]], float]] = {
    "mean": lambda x: sum(x) / len(x),
    "median": lambda x: float(np.median(x)),
    "variance": lambda x: float(np.var(x, ddof=0)),  # 或 ddof=1 样本方差
    "standard": lambda x: float(np.std(x, ddof=0)),
}


def _resample(data: list[float]) -> list[float]:
    return random.choices(
        data,
        k=len(data),
    )


def generate_distribution(
    data: list[float],
    statistical_function: str = "mean",
    iterations: int = 1000,
    confidence_quantile: tuple[float, float] = (2.5, 97.5),
    z_score: float = 1,
) -> Distribution:
    statistical = statistical_functions[statistical_function]

    samples: list[list[float]] = [_resample(data) for _ in range(iterations)]
    bootstrap: list[float] = [statistical(x) for x in samples]

    median: float = float(np.median(bootstrap))
    point_estimate: float = float(statistical(data))
    standard_error: float = float(np.std(bootstrap))

    confidence_quantile_lower, confidence_quantile_upper = confidence_quantile
    confidence_interval_lower: float = float(
        np.percentile(
            bootstrap,
            confidence_quantile_lower,
        )
    )
    confidence_interval_upper: float = float(
        np.percentile(
            bootstrap,
            confidence_quantile_upper,
        )
    )

    return {
        "samples": samples,
        "bootstrap": bootstrap,
        "median": median,
        "point_estimate": point_estimate,
        "standard_error": standard_error,
        "standard_error_interval": (
            point_estimate - standard_error * z_score,
            point_estimate + standard_error * z_score,
        ),
        "confidence_interval": (
            confidence_interval_lower,
            confidence_interval_upper,
        ),
    }
