# Predict Student Performance from Game Play

[Kaggle 竞赛 Overview](https://www.kaggle.com/competitions/predict-student-performance-from-game-play/overview) | [Data](https://www.kaggle.com/competitions/predict-student-performance-from-game-play/data) | [Evaluation](https://www.kaggle.com/competitions/predict-student-performance-from-game-play/overview/evaluation)

## 任务

基于教育游戏中的 **事件级日志（时序 / 表格）**，预测学生在各题目上的表现（**二分类**：是否答对等；具体标签定义以 [docs/competition-spec.md](docs/competition-spec.md) 与官网为准）。

## 工作流

```
本地讨论方案 → 确认 → 修改 notebook → git commit → Kaggle Notebook 训练与提交 → 反馈结果
```

- **训练与提交**：以 Kaggle **Rules / Notebooks** 当前说明为准（部分赛题为 **Code Competition** 或带 **API 提交** 流程）。
- **本地**：方案讨论、版本管理、EDA、实验记录。

详见 [AGENTS.md](AGENTS.md) 了解 AI 协作规则、git 规范与**文档同步**约定。

## 项目结构

```
├── AGENTS.md                    # AI 协作规则 & git 规范
├── TASKS.md                     # 实验进度、分数、EXP 日志（主记录）
├── README.md                    # 本文件
├── data/
│   ├── README.md                # 从 Kaggle 下载数据的说明（勿提交大文件）
│   ├── train.csv                # 官方训练日志（下载后放入；勿改）
│   ├── test.csv                 # 官方测试相关表（若有；勿改）
│   ├── train_labels.csv         # 训练标签（若有；勿改）
│   └── sample_submission.csv    # 提交列名样例（可由官网复制）
├── docs/
│   ├── competition-spec.md      # 赛题规格与评测（链接官网）
│   └── superpowers/plans/       # 规划类文档（可选）
├── memory/                      # 约定备忘：seed、按 session 划分等
├── notebooks/                   # Kaggle 训练 notebook（版本化命名）
└── experiments/eda/             # 本地 EDA 脚本
```

**文档同步**：新增实验或变更目录时，请同步更新 [TASKS.md](TASKS.md)、本文件与 [AGENTS.md](AGENTS.md)（见 AGENTS 工作流第 6 步）。

## 赛题要点（摘要）

- **数据**：游戏内 **事件日志** 与 **标签表** 多文件组织；完整列名与行数以 [Data 页](https://www.kaggle.com/competitions/predict-student-performance-from-game-play/data) 为准。
- **提交**：通常为 **`session_id` + `correct`** 的 **CSV**（`session_id` 常含题目维度，如 `..._q1`）；与 `sample_submission.csv` 严格对齐。
- **指标**：常见表述为 **F1**（是否 **Macro F1** 以 [Evaluation](https://www.kaggle.com/competitions/predict-student-performance-from-game-play/overview/evaluation) 为准）。

详见 [docs/competition-spec.md](docs/competition-spec.md)。
