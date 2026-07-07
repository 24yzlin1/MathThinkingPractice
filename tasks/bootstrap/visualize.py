import os
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# 设置绘图风格
sns.set_theme(style="whitegrid")
plt.rcParams["font.sans-serif"] = [
    "SimHei",
    "Arial Unicode MS",
    "DejaVu Sans",
]  # 防止中文乱码
plt.rcParams["axes.unicode_minus"] = False  # 正常显示负号

# 设置默认保存目录
FIGURES_DIR = "figures/task3"
os.makedirs(FIGURES_DIR, exist_ok=True)


def plot_original_distribution(data: list[float], column_name: str, iterations: int):

    fig, axes = plt.subplots(2, 1, figsize=(10, 8), sharex=True)

    # 直方图 + 密度曲线
    sns.histplot(data, kde=True, ax=axes[0], color="skyblue", alpha=0.7)
    axes[0].set_title(f"原始数据分布: {column_name}")
    axes[0].set_ylabel("频数")

    # 箱线图
    sns.boxplot(x=data, ax=axes[1], color="lightgreen")
    axes[1].set_title("箱线图 (检测异常值)")
    axes[1].set_xlabel("数值")

    plt.tight_layout()
    save_path = os.path.join(
        FIGURES_DIR, f"task3_original_distribution_{iterations}.svg"
    )
    plt.savefig(save_path)
    print(f"原始分布图已保存至: {save_path}")
    plt.show()


def plot_bootstrap_distribution(
    bootstrap_stats: list[float], point_estimate: float, iterations: int
):

    plt.figure(figsize=(10, 6))
    sns.histplot(bootstrap_stats, kde=True, color="salmon", alpha=0.7, stat="density")

    # 标出点估计位置
    plt.axvline(
        point_estimate,
        color="red",
        linestyle="--",
        linewidth=2,
        label=f"点估计值: {point_estimate:.4f}",
    )

    plt.title("Bootstrap 统计量抽样分布")
    plt.xlabel("统计量数值")
    plt.ylabel("密度")
    plt.legend()

    save_path = os.path.join(
        FIGURES_DIR, f"task3_bootstrap_distribution_{iterations}.svg"
    )
    plt.savefig(save_path)
    print(f"Bootstrap分布图已保存至: {save_path}")
    plt.show()


def plot_confidence_interval(
    ci: tuple[float, float],
    point_estimate: float,
    iterations: int,
    se_interval: tuple[float, float] = None,
):

    plt.figure(figsize=(10, 2))

    # 绘制置信区间线段
    plt.errorbar(
        point_estimate,
        1,
        xerr=[[point_estimate - ci[0]], [ci[1] - point_estimate]],
        fmt="o",
        color="black",
        capsize=10,
        label="95% 置信区间 (Percentile)",
    )

    if se_interval:
        plt.errorbar(
            point_estimate,
            1.2,
            xerr=[[point_estimate - se_interval[0]], [se_interval[1] - point_estimate]],
            fmt="s",
            color="blue",
            alpha=0.6,
            capsize=5,
            label="±1 SE 区间",
        )

    plt.yticks([])
    plt.title("置信区间可视化")
    plt.xlabel("数值")
    plt.legend(loc="lower center", bbox_to_anchor=(0.5, -0.5))
    plt.grid(axis="x", linestyle="--", alpha=0.7)

    save_path = os.path.join(FIGURES_DIR, f"task3_confidence_interval_{iterations}.svg")
    plt.savefig(save_path, bbox_inches="tight")
    print(f"置信区间图已保存至: {save_path}")
    plt.show()


def plot_evolution_curve(
    bootstrap_stats: list[float], iterations: int, true_value: float = None
):

    # 计算累积均值以观察收敛性
    cum_mean = np.cumsum(bootstrap_stats) / np.arange(1, len(bootstrap_stats) + 1)

    plt.figure(figsize=(10, 6))
    plt.plot(cum_mean, label="累积均值", color="purple")

    if true_value:
        plt.axhline(true_value, color="red", linestyle="--", label="真实值/点估计")

    plt.title("Bootstrap 统计量收敛演化曲线")
    plt.xlabel("重采样次数 (Iterations)")
    plt.ylabel("统计量数值")
    plt.legend()
    plt.grid(True)

    save_path = os.path.join(FIGURES_DIR, f"task3_evolution_curve_{iterations}.svg")
    plt.savefig(save_path)
    print(f"演化曲线图已保存至: {save_path}")
    plt.show()
