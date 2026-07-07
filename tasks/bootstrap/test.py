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
    print(f" 开始 Bootstrap 分析")
    print(f" 列名: {column} | 统计量: {statistical_function} | 次数: {iterations}")
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

    print(f" 计算完成:")
    print(f" 点估计 ({statistical_function}): {point_estimate:.4f}")
    print(f" 95% 置信区间: [{ci_lower:.4f}, {ci_upper:.4f}]")

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
