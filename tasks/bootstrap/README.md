# 任务三：概率论与数理统计实验 —— 采用 Bootstrap 方法解决估计问题

本模块实现了基于 Bootstrap 重采样的统计推断方法，能够对均值、中位数等统计量进行点估计与区间估计，并通过可视化展示估计的不确定性。

## 数学模型

### 问题表述

在数理统计中，我们常常需要根据有限样本对总体参数 (如均值、中位数、比例等) 进行估计，并量化估计的精度。传统方法依赖参数假设 (如正态分布) 和渐近理论，但实际数据可能不满足这些条件。Bootstrap 方法 (Efron, 1979) 提供了一种非参数的重采样技术，通过从原始样本中有放回地反复抽取 “自助样本”，模拟抽样分布，从而在不依赖强分布假设的情况下进行统计推断。

## 数学原理

### 统计泛函

我们感兴趣的总体参数为 $\theta = T (F)$，其中 $F$ 是总体分布，$T$ 是某个统计泛函。其中统计泛函是把整个分布当作输入，提取出该分布的一个整体特征作为输出。

| 统计量              | 总体统计泛函 $T(F)$                                                                         | 经验统计泛函 $T(\hat{F}_n)$                                                                                       |
| :------------------ | :------------------------------------------------------------------------------------------ | :---------------------------------------------------------------------------------------------------------------- |
| **均值 (Mean)**     | $T(F) = \displaystyle \int x \, dF(x)$ <br> (分布的一阶原点矩)                              | $\displaystyle \bar{x} = \frac{1}{n} \sum_{i = 1}^n X_i$ <br> (样本平均数)                                        |
| **中位数 (Median)** | $T(F) = \inf\{ x \mid F(x) \ge 0.5 \}$ <br> (分布的中点，即 0.5 分位数)                     | $T(\hat{F}_n) = X_{(k)}$，其中 $k = \lceil n/2 \rceil$ <br> (排序后居中的观测值)                                  |
| **方差 (Variance)** | $T(F) = \displaystyle \int (x - \mu)^2 \, dF(x)$，其中 $\mu = T(F)$ <br> (分布的二阶中心矩) | $\displaystyle s^2 = \frac{1}{n} \sum_{i = 1}^n (X_i - \bar{X})^2$ <br> (Bootstrap 通常采用 $1/n$ 的总体方差形式) |
| **标准差 (Std)**    | $T(F) = \sqrt{ \displaystyle \int (x - \mu)^2 \, dF(x) }$ <br> (方差的算术平方根)           | $\displaystyle s = \sqrt{ \frac{1}{n} \sum_{i = 1}^n (X_i - \bar{X})^2 }$                                         |

在后续的 Bootstrap 过程中，基于经验分布 $\mathbf{x}^* = (x_1^*, \dots, x_n^*)$ 构造重样本，并针对任意选定的统计泛函 $\hat{F}_n$ 计算其复制值，而不仅限于均值。

### 经验分布与重采样

原始样本 $\mathbf{x} = (x_1,\dots,x_n)$ 的经验分布函数定义为

$$
\hat{F}_n(t) = \frac{1}{n}\sum_{i = 1}^n \mathbf{1}_{\{x_i \le t\}}
$$

Bootstrap 样本 $\mathbf{x}^* = (x_1^*, \dots, x_n^*)$ 是从 $\hat{F}_n$ 中独立同分布抽取的，等价于从原始样本中有放回地随机抽取 $n$ 个观测值。

### Bootstrap 估计

- 重采样：独立地抽取 $B$ 个 Bootstrap 样本，记为 $\mathbf{x}^{*(1)}, \mathbf{x}^{*(2)}, \dots, \mathbf{x}^{*(B)}$

- 计算统计量：对每个 Bootstrap 样本计算相同的统计量 $T(\mathbf{x}^{*(b)})$，得到 Bootstrap 复制值

  $$
  \hat{\theta}^{*(1)}, \hat{\theta}^{*(2)}, \dots, \hat{\theta}^{*(B)}
  $$

- 点估计：通常直接采用原始样本的经验泛函值 $\hat{\theta} = T(\hat{F}_n)$ 作为 $\theta$ 的点估计；Bootstrap 复制值本身并不直接用于点估计 (除非进行偏差校正)，它们主要用于评估 $\hat{\theta}$ 的精度和构建置信区间

- 标准误估计：Bootstrap 标准误为所有复制值的样本标准差

  $$
  \widehat{\mathrm{SE}}_{\mathrm{boot}} = \sqrt{\frac{1}{B-1}\sum_{b=1}^B \left(\hat{\theta}^{*(b)} - \bar{\theta}^*\right)^2},
  \quad \bar{\theta}^* = \frac{1}{B}\sum_{b=1}^B \hat{\theta}^{*(b)}
  $$

- 置信区间 (百分位数法)：取复制值的 $100\alpha/2$ 和 $100(1-\alpha/2)$ 百分位数作为双侧置信区间
  $$
  \left[ \hat{\theta}_{(\alpha/2)}^*, \ \hat{\theta}_{(1-\alpha/2)}^* \right]
  $$

其中 $\hat{\theta}_{(p)}^*$ 表示复制值的第 $p$ 百分位数。另外也可采用正态近似区间 $\bar{\theta}^* \pm z_{1-\alpha/2} \cdot \widehat{\mathrm{SE}}_{\mathrm{boot}}$ 或标准误区间等。

## 实例构建

> 估计某校全体学生的平均考试成绩的具体例子，文案负责。

## 核心函数说明

### `generate_distribution`

- 说明：执行完整的 Bootstrap 过程，生成统计量分布。

- 参数：
  - `data`：原始样本列表

  - `statistical_function`：要估计的统计泛函值

  - `iterations`：重采样次数 $B$

  - `confidence_quantile`：置信区间百分位数

- 返回：`Distribution` 字典
  - `samples`：所有 Bootstrap 样本及其均值的列表

  - `bootstrap`：所有 Bootstrap 均值组成的列表

  - `median`：原始数据的中位数

  - `point_estimate`：原始数据的均值

  - `standard_error`：Bootstrap 标准误差

  - `standard_error_interval`：基于标准误差的区间

  - `confidence_interval`：百分位数置信区间
