# 数学思维实践 —— CDIO 二级项目

本项目为《数学思维实践》课程 (CST4822A) 的 CDIO 二级项目实践，围绕**线性代数**、**离散数学**和**概率论与数理统计**三个核心数学领域，完成从工程建模、算法实现、可视化验证到结果分析的完整流程。每个任务均采用 “数学模型层 — 计算实现层 — 可视化验证层” 的统一结构，强调数学知识与编程实践的结合。

## 任务概览

### 任务一：迭代法解线性方程组 (线性代数实验)

- **目标**：将实际问题或模拟场景表示为线性方程组 $Ax = b$，使用迭代法 (Jacobi 或 Gauss-Seidel) 求解，并分析收敛性与误差。

- **实现**：
  - 设置初值、误差阈值和最大迭代次数。

  - 记录每步残差，比较不同迭代方法的收敛速度。

- **可视化**：
  - 系数矩阵结构热力图 (展示稀疏性或元素分布)。

  - 迭代误差随步数变化的收敛曲线。

  - 数值解与直接求解 (如 `numpy.linalg.solve`) 的对比图。

- **分析**：讨论矩阵性质 (如对角占优、条件数) 对迭代收敛的影响，以及不同方法的效率差异。

### 任务二：三控开关的设计与实现 (离散数学实验)

- **目标**：设计一个三控开关逻辑，使得任意一个开关状态发生变化时，灯的输出状态均切换 (即异或逻辑的推广)。

- **实现**：
  - 枚举三个开关 $S_1, S_2, S_3$ 的全部 8 种状态 (0 / 1)。

  - 建立真值表，推导灯输出 $L$ 的布尔表达式 (如 $L = S_1 \oplus S_2 \oplus S_3$)。

  - 编写程序验证任意单开关切换时输出是否正确翻转。

- **可视化**：
  - 状态空间图 (展示 8 个状态及其转移关系)。

  - 真值表颜色矩阵 (用颜色表示输出 0 / 1)。

  - 逻辑门结构图 (可选)。

- **分析**：验证布尔表达式的正确性，确认程序输出与真值表完全一致，并讨论逻辑简洁性。

### 任务三：采用 Bootstrap 方法解决估计问题 (概率统计实验)

- **目标**：基于样本数据，使用 Bootstrap 重采样方法估计总体统计量 (如均值、中位数或比例)，并计算置信区间，量化估计不确定性。

- **实现**：
  - 从原始样本中有放回地重采样 $B$ 次 (如 1000 次)，每次采样大小与原样本相同。

  - 计算每个 Bootstrap 样本的统计量，得到经验分布。

  - 计算点估计 (如原始样本统计量) 和百分位数置信区间 (如 95%)。

- **可视化**：
  - 原始样本分布图 (直方图或箱线图)。

  - Bootstrap 统计量分布直方图 / 密度曲线。

  - 置信区间示意图 (标明上下限)。

- **分析**：解释点估计和置信区间的含义，评估估计稳定性 (如标准误)，讨论 Bootstrap 方法在该问题中的适用性与局限性。

## 文件结构

```
math-thinking-practice
│  .gitignore
│  .python-version
│  ISSUES.md
│  LICENSE
│  main.py
│  o.txt
│  pyproject.toml
│  README.md
│  TASK.md
│  uv.lock
│
├─data
│      sample_data.csv
│      task1.md
│      task3.md
│
├─figures
│  ├─task1
│  │      task1_convergence_curve_set1.svg
│  │      task1_convergence_curve_set2.svg
│  │      task1_convergence_curve_set3.svg
│  │      task1_heatmap_set1.svg
│  │      task1_heatmap_set2.svg
│  │      task1_heatmap_set3.svg
│  │      task1_runtime_comparison_set1.svg
│  │      task1_runtime_comparison_set2.svg
│  │      task1_runtime_comparison_set3.svg
│  │      task1_solution_comparison_set1.svg
│  │      task1_solution_comparison_set2.svg
│  │      task1_solution_comparison_set3.svg
│  │
│  ├─task2
│  │      task2_state_space.svg
│  │      task2_state_space_path.svg
│  │      task2_truth_table_matrix.svg
│  │
│  └─task3
│          task3_bootstrap_distribution_100.svg
│          task3_bootstrap_distribution_1000.svg
│          task3_bootstrap_distribution_500.svg
│          task3_confidence_interval_100.svg
│          task3_confidence_interval_1000.svg
│          task3_confidence_interval_500.svg
│          task3_evolution_curve_100.svg
│          task3_evolution_curve_1000.svg
│          task3_evolution_curve_500.svg
│          task3_original_distribution_100.svg
│          task3_original_distribution_1000.svg
│          task3_original_distribution_500.svg
│
└─tasks
    ├─bootstrap
    │      core.py
    │      README.md
    │      test.py
    │      visualize.py
    │      __init__.py
    │
    ├─iterative
    │      core.py
    │      README.md
    │      test.py
    │      visualize.py
    │      __init__.py
    │
    └─three_switch
            core.py
            README.md
            test.py
            visualize.py
            __init__.py
```

核心目录说明如下：

- `tasks/` —— 三个任务的独立模块，每个任务包含算法实现、可视化和测试脚本。

- `data/` —— 存放任务三所需的原始样本数据 (CSV 格式)。

- `figures/` —— 所有任务生成的可视化图表 (自动输出)。

- `reports/` —— 实践报告与实践过程文档 (Markdown 格式，按课程模板填写)。

- `main.py` —— 统一入口，可一键运行全部任务并生成图表。

## 环境与依赖

本项目使用 **Python 3.13**，主要依赖库：

- `numpy` —— 数值计算

- `matplotlib` —— 绘图

### 安装依赖

**方式一 (使用 pip + requirements.txt)**：

```bash
pip install -r requirements.txt
```

**方式二 (使用 pyproject.toml，推荐)**：

```bash
pip install -e .
```

`requirements.txt` 内容示例：

```
numpy>=1.24
matplotlib>=3.7
pandas>=2.0
seaborn>=0.12
```

## 运行指南

### 1. 一键运行全部任务

在项目根目录下执行：

```bash
python main.py
```

该脚本会依次执行三个任务的 `visualize.py`，生成所有图表并保存至 `figures/`，同时将关键结果打印到控制台。

### 2. 单独运行某个任务

进入 `tasks/` 下对应任务文件夹，运行其可视化脚本：

```bash
cd tasks/task1_iterative
python visualize.py
```

每个任务的 `visualize.py` 独立运行，不会干扰其他任务。

## 报告与过程文档

- **`reports/实践报告.md`** ：按照课程提供的报告模板，完整填写三个任务的模型建立、算法实现、可视化图表和结果分析。

- **`reports/实践过程.md`** ：记录资料查阅、问题解决、分工协作和阶段性推进情况，体现项目实施的完整过程。

建议使用 Markdown 编辑器 (如 Typora、VS Code) 编写，并导出为 PDF 提交。所有图表均在 `figures/` 中，可直接在报告中引用 (相对路径)。

## 结果复现与参数调整

- 若需修改算法参数 (如迭代误差阈值、Bootstrap 重采样次数)，请直接编辑各任务模块中的常量定义 (通常位于 `solver.py` / `bootstrap.py` 文件头部)。

- 所有随机过程 (如 Bootstrap 重采样) 均设置了随机种子 (`np.random.seed(42)`)，以保证结果可重复。

- 图表输出格式默认为 PNG，分辨率 300 dpi，可在可视化脚本中调整。

## 许可证

本项目采用 **MIT 许可证**，详情请参阅 [LICENSE](LICENSE) 文件。

## 贡献者

- 小组：第 51 组

## 致谢

感谢《数学思维实践》课程提供的任务书、报告模板及指导要求，使本项目得以规范开展。
