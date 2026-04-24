# Predict Student Performance from Game Play — 赛题规格与评测说明

> 与 Kaggle **Overview / Data / Evaluation** 官方说明一致；**若冲突以官网为准**。下列部分条目来自公开讨论与二次摘要，**导入数据后请以本地 `head` 与 Data 页为准核对列名**。

来源：[竞赛 Overview](https://www.kaggle.com/competitions/predict-student-performance-from-game-play/overview) | [Data](https://www.kaggle.com/competitions/predict-student-performance-from-game-play/data) | [Evaluation](https://www.kaggle.com/competitions/predict-student-performance-from-game-play/overview/evaluation)

---

## 赛题定位（摘要）

- **任务类型**：以游戏 **事件日志** 为核心输入，预测学生在题目上的结果（常见表述为 **二分类**：`correct` 等；**具体定义以标签文件与 Overview 为准**）。
- **一句话目标**：在隐藏测试集上优化官方指标（常见为 **F1**；是否 **Macro F1** 见 Evaluation 页）。
- **提交**：以 Kaggle **Rules / Submission** 为准；预测文件通常为 **CSV**，列与 `sample_submission.csv` **完全一致**（常见列为 **`session_id`**, **`correct`**）。`session_id` 常编码 **会话 + 题目**（例如 `..._q1` 形式，**以 sample 为准**）。

---

## 数据（以 Data 页为准）

典型竞赛会提供多文件，例如（**名称与列以你下载的数据包为准**）：

| 文件 | 常见用途 |
|------|-----------|
| `train.csv` | 训练集 **事件级** 日志（行数大；多列如 `session_id`、`event_name`、时间/坐标等） |
| `train_labels.csv` | 训练集 **标签**（与 `session_id` 或题目键对齐） |
| `test.csv` | 测试侧用于推理对齐的表（若有） |
| `sample_submission.csv` | **提交列名与行键** 的黄金标准 |

**注意**：本仓库 **不在 git 中托管** 完整 `train.csv`（体积大）。本地分析请将 Kaggle 下载文件放入 `data/`。

---

## 评价指标（Evaluation）

- 请以 **[Evaluation 页](https://www.kaggle.com/competitions/predict-student-performance-from-game-play/overview/evaluation)** 的公式与说明为准。
- 公开资料中常见表述为 **F1**（多类或宏平均等实现细节 **以官网代码/说明为准**）。

---

## 提交方式（Submitting）

- 输出 **CSV**：列名、行数、`session_id` 集合与评测要求一致。
- **Notebook / API**：若为 **Code Competition** 或带 **Inference API**，以 Rules 与官方教程为准。

---

## 与本仓库的关系

- **`data/`**：仅存说明与小样；全量数据从 Kaggle 下载。
- **验证划分**：建议 **按 `session_id`（或等价会话键）分组** 再切分，避免同一 session 同时出现在 train 与 val（见 `memory/data-split-train-val.md`）。

---

**结论**：赛题核心是 **游戏事件日志 → 学生答题表现（二分类为主）**；**指标与提交列** 以官网 **Evaluation + sample_submission** 为最终依据。
