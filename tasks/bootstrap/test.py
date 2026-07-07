import pandas as pd
import numpy as np

try:
    from .core import *
    from .visualize import *
except:
    from core import *
    from visualize import *


def test_bootstrap_workflow(
    column: str = "exam_score",
    statistical_function: str = "median",
    iterations: int = 1000,
):

    print(f"\n{'='*50}")
    print(f" Bootstrap Analysis")
    print(f" Column: {column} | Statistic: {statistical_function} | Iterations: {iterations}")
    print(f"{'='*50}")

    data = pd.read_csv("./data/sample_data.csv")
    target_data = data[column].dropna().tolist()
    result = generate_distribution(
        target_data,
        statistical_function,
        iterations=iterations,
    )

    point_estimate = result["point_estimate"]
    ci_lower = result["confidence_interval"][0]
    ci_upper = result["confidence_interval"][1]
    bootstrap_stats = result["bootstrap"]

    print(f"\n Results:")
    print(f"   Point Estimate ({statistical_function}): {point_estimate:.4f}")
    print(f"   95% CI: [{ci_lower:.4f}, {ci_upper:.4f}]")

    plot_original_distribution(
        target_data,
        column,
        iterations=iterations,
    )

    plot_bootstrap_distribution(
        np.array(bootstrap_stats),
        point_estimate,
        iterations=iterations,
    )

    plot_confidence_interval(
        (ci_lower, ci_upper),
        point_estimate,
        iterations=iterations,
    )

    plot_evolution_curve(
        result["bootstrap"],
        iterations=iterations,
    )

if __name__ == "__main__":
    test_bootstrap_workflow(iterations=100)
    test_bootstrap_workflow(iterations=500)
    test_bootstrap_workflow(iterations=1000)
