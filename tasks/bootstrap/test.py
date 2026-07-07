import pandas as pd
import numpy as np

# 导入核心计算逻辑
from tasks.bootstrap.core import generate_distribution

# 导入可视化函数
from tasks.bootstrap.visualize import (
    plot_original_distribution,
    plot_bootstrap_distribution,
    plot_confidence_interval,
    plot_evolution_curve,
)

def test_bootstrap_workflow(
    column: str = "previous_scores",
    statistical_function: str = "median",
    iterations: int = 1000,
):

    print(f"\n{'='*50}")
    print(f" 开始 Bootstrap 分析")
    print(f" 列名: {column} | 统计量: {statistical_function} | 次数: {iterations}")
    print(f"{'='*50}")

    # 1. 准备数据
    try:
        data = pd.read_csv("./data/sample_data.csv")
        target_data = data[column].dropna().tolist()
    except FileNotFoundError:
        print(" 错误: 找不到 ./data/sample_data.csv，请检查路径。")
        return


    result = generate_distribution(target_data, statistical_function, iterations)
    
    point_estimate = result['point_estimate']
    ci_lower = result['confidence_interval'][0]
    ci_upper = result['confidence_interval'][1]
    bootstrap_stats = result['bootstrap'] 
    
    print(f" 计算完成:")
    print(f" 点估计 ({statistical_function}): {point_estimate:.4f}")
    print(f" 95% 置信区间: [{ci_lower:.4f}, {ci_upper:.4f}]")

    # 3. 可视化部分
    
    # --- 任务 42: 原始样本分布 ---
    print(" 正在生成图 42: 原始样本分布...")
    plot_original_distribution(target_data, column)

    # --- 任务 43: Bootstrap 分布 ---
    print(" 正在生成图 43: Bootstrap 分布...")
    plot_bootstrap_distribution(np.array(bootstrap_stats), point_estimate)

    # --- 任务 44: 置信区间 ---
    print(" 正在生成图 44: 置信区间...")
    plot_confidence_interval((ci_lower, ci_upper), point_estimate)

    # --- 任务 45: 演化曲线 ---
    print(" 任务 45: core.py 暂未返回演化数据，跳过收敛曲线绘制。")

    print("\n 所有图表已生成！")

if __name__ == "__main__":
    test_bootstrap_workflow(iterations=1000)