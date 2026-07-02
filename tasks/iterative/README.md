# 任务一：迭代法解线性方程组

本模块实现了线性方程组 $Ax = b$ 的迭代求解 (Jacobi 与 Gauss‑Seidel)，并提供直接求解方法 (NumPy 内置求解器、LU 分解) 作为对比。

## 数学模型

### 问题表述

设待求解的线性方程组为

$$
A \mathbf{x} = \mathbf{b}
$$

其中

- $A \in \mathbb {R}^{n \times n}$ 为系数矩阵 (非奇异)

- $\mathbf {x} \in \mathbb {R}^{n}$ 为未知向量

- $\mathbf {b} \in \mathbb {R}^{n}$ 为右端常数向量

## 数学原理

### Jacobi 迭代

将 $A$ 分解为

$$
A = D - L - U
$$

其中

- $D = \mathrm {diag}(a_{11}, \dots, a_{nn})$

- $-L$ 为严格下三角部分 ($L$ 元素为 $-a_{ij}, i > j$)

- $-U$ 为严格上三角部分 ($U$ 元素为 $-a_{ij}, i < j$)

则方程 $A\mathbf {x} = \mathbf {b}$ 可写为

$$
(D - L - U)\mathbf{x} = \mathbf{b} \quad \Rightarrow \quad D\mathbf{x} = (L + U)\mathbf{x} + \mathbf{b}
$$

得到迭代格式

$$
\mathbf{x}^{(k + 1)} = D^{-1}(L + U)\mathbf{x}^{(k)} + D^{-1}\mathbf{b}
$$

故 Jacobi 迭代矩阵

$$
B_J = D^{-1}(L + U), \qquad \mathbf{f}_J = D^{-1}\mathbf{b}
$$

### Gauss-Seidel 迭代

利用分解 $A = D - L - U$，方程写为

$$
(D - L)\mathbf{x} = U\mathbf{x} + \mathbf{b}
$$

迭代时左端 $(D - L)$ 乘以**新向量** $\mathbf {x}^{(k + 1)}$，右端 $U$ 乘以旧向量 $\mathbf {x}^{(k)}$：

$$
(D - L)\mathbf{x}^{(k + 1)} = U\mathbf{x}^{(k)} + \mathbf{b}
$$

解得

$$
\mathbf{x}^{(k + 1)} = (D - L)^{-1}U \,\mathbf{x}^{(k)} + (D - L)^{-1}\mathbf{b}
$$

故 Gauss-Seidel 迭代矩阵

$$
B_G = (D - L)^{-1}U, \qquad \mathbf{f}_G = (D - L)^{-1}\mathbf{b}
$$

### 收敛性分析

充要条件：迭代矩阵 $B$ 的谱半径 $\rho (B) < 1$ 是迭代收敛的充要条件。

$$
\rho (B) = \max\{|\lambda| : \lambda \text { 是 } B \text { 的特征值}\}
$$

### 实例构建

> 挑选一个在热传导、电路网络或差分方程离散化中的具体例子，文案负责。

## 计算实现

设线性方程组为 $A \mathbf {x} = \mathbf {b}$，其中 $A = (a_{ij})$，$b = (b_i)$。

### Jacobi 迭代

- 一般数学形式

  $$
  x_i^{(k + 1)} = \frac{1}{a_{ii}} \left( b_i - \sum_{j \neq i} a_{ij} \, x_j^{(k)} \right), \quad i = 1, 2, \dots, n
  $$

- 计算机实现形式

  $$
  x_i^{(k + 1)} = \frac{b_i - \left( \mathbf{A}_i \cdot \mathbf{x}^{(k)} - a_{ii} x_i^{(k)} \right)}{a_{ii}} = \frac{b_i - \left( \sum_{j = 1}^{i - 1} a_{ij} x_j^{(k)} + \sum_{j = i + 1}^{n} a_{ij} x_j^{(k)} \right)}{a_{ii}}
  $$

### Gauss‑Seidel 迭代

- 一般数学形式

  $$
  x_i^{(k + 1)} = \frac{1}{a_{ii}} \left( b_i - \sum_{j < i} a_{ij} \, x_j^{(k + 1)} - \sum_{j > i} a_{ij} \, x_j^{(k)} \right), \quad i = 1, 2, \dots, n
  $$

- 计算机实现形式

  $$
  x_i^{(k + 1)} =  \frac{b_i - \left( \mathbf{A}_i \cdot \mathbf{x}^{(k + 1)} - a_{ii} x_i^{(k)} \right)}{a_{ii}} = \frac{b_i - \left( \sum_{j = 1}^{i - 1} a_{ij} x_j^{(k + 1)} + \sum_{j = i + 1}^{n} a_{ij} x_j^{(k)} \right)}{a_{ii}}
  $$

  注意此处 $\mathbf {x}^{(k + 1)}$ 在计算 $x_i^{(k + 1)}$ 时，前 $i - 1$ 个分量已更新为最新值。

## 核心代码说明

### `solve_with_np_builtin`

- 说明：调用 NumPy 的 `np.linalg.solve` 求解线性方程组。适用于系数矩阵非奇异的情形，效率高且数值稳定。

- 参数
  - `coefficient` – 系数矩阵 $A$

  - `constant` – 常数向量 $b$

- 返回：方程组的解向量 $x$

### `solve_with_triangular_decompose`

- 说明：使用 LU 分解手动求解方程组。先分解矩阵，再分别解 $Ly = b$ 和 $Ux = y$。

- 参数
  - `coefficient` – 系数矩阵 $A$

  - `constant` – 常数向量 $b$

- 返回：方程组的解向量 $x$

### `iterate_solution`

- 说明：使用迭代法近似求解线性方程组。迭代直至收敛或达到最大迭代次数。

- 参数
  - `coefficient` – 系数矩阵 $A$

  - `constant` – 常数向量 $b$

  - `function` – 迭代方法
    - `JACOBI`

    - `GS`

  - `init_solution` – 初始迭代向量

  - `max_iterations` – 最大迭代次数

  - `tolerance` – 收敛判据

- 返回：三元组
  - `bool` – 是否在 `max_iterations` 内收敛

  - `int` – 实际迭代次数

  - `np.ndarray` – 最终的近似解向量

### `iterate_solution_alt`

- 说明：使用迭代法求解线性方程组的另一种实现。显式构造迭代矩阵与常数向量，并采用矩阵乘法 $\mathbf{x}^{(k+1)} = B\mathbf{x}^{(k)} + \mathbf{f}$ 进行迭代。

- 参数
  - `coefficient` – 系数矩阵 $A$

  - `constant` – 常数向量 $b$

  - `function` – 迭代方法
    - `JACOBI`

    - `GS`

  - `init_solution` – 初始迭代向量

  - `max_iterations` – 最大迭代次数

  - `tolerance` – 收敛判据

- 返回：三元组
  - `bool` – 是否在 `max_iterations` 内收敛

  - `int` – 实际迭代次数

  - `np.ndarray` – 最终的近似解向量

### `calculate_spectral_radius`

- 说明：计算给定迭代法的迭代矩阵的谱半径。

- 参数
  - `coefficient` – 系数矩阵 $A$

  - `function` – 迭代方法
    - `JACOBI`

    - `GS`

- 返回：迭代矩阵的谱半径

## 可视化代码说明

### `plot_matrix_heatmap`

- 说明：生成系数矩阵 $A$ 的结构热力图。该函数利用颜色深浅直观展示矩阵元素的数值分布情况，有助于分析矩阵的稀疏性、对称性或特殊结构 (如三对角矩阵)。

- 参数
  - `A` – 系数矩阵 $A$(通常为二维 NumPy 数组)

- 返回：无返回值。函数会自动创建 `figures` 目录 (如果不存在)，将图像保存为 `task1_heatmap.png` 并调用 `plt.show()` 显示

### `plot_error_curves`

- 说明：绘制迭代算法的收敛曲线。该函数使用半对数坐标系 (Y 轴为对数坐标) 展示 Jacobi 和 Gauss-Seidel 方法的相对误差随迭代步数的变化趋势，并绘制收敛阈值参考线，用于直观判断算法的收敛速度。

- 参数
  - `jacobi_hist` – Jacobi 迭代过程中的误差历史列表 (`List` 或 `Array`)

  - `gs_hist` – Gauss-Seidel 迭代过程中的误差历史列表 (可选，默认为 `None`)

  - `tol` – 收敛阈值 (`float`)，用于在图中绘制水平参考线 (默认为 `1e-8`)

- 返回：无返回值。图像将被保存为 `task1_convergence_curve.png` 并显示

### `plot_solution_comparison`

- 说明：绘制数值解与精确解的对比图。该函数将直接法 (如 LU 分解) 求得的精确解作为基准折线，将迭代法求得的近似解以散点形式叠加，用于验证迭代解的精度。

- 参数
  - `x_exact` – 精确解向量 (由直接法求得)

  - `jacobi_x` – Jacobi 迭代求得的近似解向量

  - `gs_x` – Gauss-Seidel 迭代求得的近似解向量 (可选，默认为 `None`)

- 返回：无返回值。图像将被保存为 `task1_solution_comparison.png` 并显示
