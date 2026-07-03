import pandas as pd

from core import *

data = pd.read_csv("./data/sample_data.csv")


def test_distribution(
    column: str = "previous_scores",
    statistical_function: str = "median",
    iterations: int = 1000,
):
    target = data[column].tolist()
    distribution = generate_distribution(
        target,
        statistical_function,
        iterations,
    )

    print(f"Point Estimate:\t{distribution['point_estimate']:.6f}")
    print(f"bootstrap MD:\t{distribution['median']:.6f}")
    print(f"Bootstrap SE:\t{distribution['standard_error']:.6f}")
    print(
        f"Percentile CI:\t{' ~ '.join(map(lambda x:f'{x:.6f}',distribution['confidence_interval']))}"
    )
    print(
        f"±1 SE Interval:\t{' ~ '.join(map(lambda x:f'{x:.6f}',distribution['standard_error_interval']))}"
    )


if __name__ == "__main__":
    test_distribution(iterations=10)
    test_distribution(iterations=100)
    test_distribution(iterations=1000)
