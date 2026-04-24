# TASKS.md — 实验方向与进度追踪

## 文档维护

- 本文件为**实验主记录**（版本表、Public Score、`EXP-xxx` 日志）。
- **新增或更新实验**、或**仓库目录/数据文件有变**时，应同步更新：
  - **`README.md`**：项目结构树与入口说明；
  - **`AGENTS.md`**：项目结构、协作步骤、禁止事项；
  - **本文件**：表格、`当前最优` 摘要、关键结论与交叉引用。
- 详见 [AGENTS.md](AGENTS.md) 工作流第 6 步（文档同步）。

---

## 竞赛目标

在官方评测下优化竞赛指标（常见为 **F1**；是否 **Macro**、是否多列以 [Evaluation](https://www.kaggle.com/competitions/predict-student-performance-from-game-play/overview/evaluation) 为准）。摘要见 [docs/competition-spec.md](docs/competition-spec.md)。

---

## 当前状态

| 版本 | 描述 | Public Score | 状态 |
|------|------|--------------|------|
| — | （待填写） | — | — |

**当前最优**：—

---

## 优化方向（待讨论）

### 方向 1：验证策略

- 日志按 **session_id**（或等价会话键）聚合；划分时宜 **按 session 分组**，避免同一局游戏泄漏到 train/val
- 若存在多题目行，需明确 **session_id × 题目** 粒度与 `sample_submission` 一致

### 方向 2：特征与模型

- **事件序列**：计数 / 时间差 / 关卡进度 / 点击路径等聚合特征；或 **RNN / Transformer / GBDT** 混合
- **表格元数据**：若赛方提供 session 级元信息，注意与日志对齐键

### 方向 3：损失与指标

- 二分类常用 **BCEWithLogits** / **Focal**；本地验证实现与官网一致的 **F1**（含宏平均方式）

### 方向 4：数据规模

- `train.csv` 行数可达千万级量级（以 Data 页为准）；注意 **分块读取、下采样调试、Kaggle 内存与时限**

---

## 实验日志

### EXP-000: 仓库初始化

- **说明**：参照 `Image2Biomass-Prediction/` 目录结构初始化；赛题链接见 [README.md](README.md)。
- **数据**：大文件不纳入 git；请将 Kaggle Data 下载至 `data/` 并阅读 [data/README.md](data/README.md)。
- **后续**：建立 `notebooks/v01-*.ipynb` baseline 后在此追加 EXP 记录。
