import random
import numpy as np
import typing as t


class BootstrapSample(t.TypedDict):
    sample: list[float]
    mean: float
    median: float
    variance: float
    standard: float


class Distribution(t.TypedDict):
    samples: list[BootstrapSample]
    bootstrap: list[float]
    median: float
    point_estimate: float
    standard_error: float
    standard_error_interval: tuple[float, float]
    confidence_interval: tuple[float, float]


def _resample(data: list[float]) -> BootstrapSample:
    sample: list[float] = random.choices(
        data,
        k=len(data),
    )

    return {
        "sample": sample,
        "mean": sum(sample) / len(sample),
        "median": float(np.median(sample)),
        "variance": float(np.var(sample)),
        "standard": float(np.std(sample)),
    }


def generate_distribution(
    data: list[float],
    statistical_function: str = "mean",
    iterations: int = 1000,
    confidence_quantile: tuple[float, float] = (2.5, 97.5),
) -> Distribution:
    samples: list[BootstrapSample] = [_resample(data) for _ in range(iterations)]
    bootstrap: list[float] = [x[statistical_function] for x in samples]

    median: float = float(np.median(data))
    point_estimate: float = sum(data) / len(data)
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
            point_estimate - standard_error,
            point_estimate + standard_error,
        ),
        "confidence_interval": (
            confidence_interval_lower,
            confidence_interval_upper,
        ),
    }
