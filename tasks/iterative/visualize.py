import os
import numpy as np
import matplotlib.pyplot as plt

# 全局配置：防止中文乱码
plt.rcParams["font.sans-serif"] = ["SimHei", "Arial Unicode MS"]
plt.rcParams["axes.unicode_minus"] = False


SAVE_DIR = "figures"


def plot_matrix_heatmap(A):

    plt.figure(figsize=(7, 6))
    plt.imshow(A, cmap="coolwarm", aspect="auto")
    plt.colorbar(label="元素值")

    plt.title("系数矩阵 A 结构热力图", fontsize=14)
    plt.xlabel("列索引")
    plt.ylabel("行索引")
    plt.tight_layout()

    save_path = os.path.join(SAVE_DIR, "task1_heatmap.png")
    plt.savefig(save_path, dpi=300)
    plt.show()
    print(f"热力图已保存至: {save_path}")


def plot_error_curves(jacobi_hist, gs_hist=None, tol=1e-8):

    plt.figure(figsize=(9, 6))

    # 绘制 Jacobi 误差曲线
    plt.semilogy(
        range(len(jacobi_hist)),
        jacobi_hist,
        marker="o",
        linestyle="-",
        markersize=4,
        label="Jacobi",
    )

    # 绘制 Gauss-Seidel 误差曲线 (如果提供了的话)
    if gs_hist is not None:
        plt.semilogy(
            range(len(gs_hist)),
            gs_hist,
            marker="s",
            linestyle="--",
            markersize=4,
            label="Gauss-Seidel",
        )

    # 绘制收敛阈值参考线
    plt.axhline(y=tol, color="r", linestyle="--", alpha=0.7, label=f"收敛阈值 ({tol})")

    plt.title("迭代误差随步数变化曲线 (对数坐标)", fontsize=14)
    plt.xlabel("迭代步数 (Iterations)")
    plt.ylabel("相对误差 (Log Scale)")
    plt.legend()
    plt.grid(True, which="both", ls="-", alpha=0.5)
    plt.tight_layout()

    save_path = os.path.join(SAVE_DIR, "task1_convergence_curve.png")
    plt.savefig(save_path, dpi=300)
    plt.show()
    print(f"收敛曲线已保存至: {save_path}")


def plot_solution_comparison(x_exact, jacobi_x, gs_x=None):

    plt.figure(figsize=(9, 6))
    indices = np.arange(len(x_exact))

    # 参考解使用折线图作为基准
    plt.plot(
        indices, x_exact, "k-o", linewidth=2, label="参考解 (Direct Solve)", zorder=10
    )

    # Jacobi 数值解使用散点图
    plt.scatter(
        indices,
        jacobi_x,
        marker="s",
        s=80,
        color="blue",
        label="Jacobi 数值解",
        zorder=5,
    )

    # Gauss-Seidel 数值解使用散点图 (如果提供了的话)
    if gs_x is not None:
        plt.scatter(
            indices, gs_x, marker="^", s=80, color="green", label="G-S 数值解", zorder=5
        )

    plt.title("数值解与参考解对比", fontsize=14)
    plt.xlabel("未知量索引")
    plt.ylabel("变量值")
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()

    save_path = os.path.join(SAVE_DIR, "task1_solution_comparison.png")
    plt.savefig(save_path, dpi=300)
    plt.show()
    print(f"解对比图已保存至: {save_path}")
