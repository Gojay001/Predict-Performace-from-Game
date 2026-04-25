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
| `v1.0-catboost-lb_0.554.ipynb` | 公开 CatBoost inference baseline；Polars 聚合大量 session 级统计特征，按题加载预训练 CatBoost，固定阈值 `0.63` 生成提交 | `0.554` | 已记录 |
| `v2.0-catboost+nn-lb_0.648.ipynb` | 两套 CatBoost + Event-Aware TConv NN 融合；按题选择单模型或加权融合，`q5/q10` 使用 NN 结果 | `0.648` | 已记录 |
| `v1.1-catboost-lb_0.699.ipynb` | CatBoost 特征筛选/题目级建模版本；基于 `feature_sort.csv` 构造题目专属时间与计数特征，按 `level_group` 分段推理 | `0.699` | 待进一步复现实验细节 |
| `v3.0-cat+xgb+mlp-lb_0.699.ipynb` | 在 `v1.1` 题目级特征上训练 CatBoost、XGBoost、MLP 三类模型，并以 `0.92/0.04/0.04` 概率加权融合 | `0.699` | 待验证融合收益 |

**当前最优**：`v1.1-catboost-lb_0.699.ipynb` / `v3.0-cat+xgb+mlp-lb_0.699.ipynb`（Public Score `0.699`）

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

### EXP-001: `v1.0-catboost-lb_0.554.ipynb`

- **Notebook**：[`notebooks/v1.0-catboost-lb_0.554.ipynb`](notebooks/v1.0-catboost-lb_0.554.ipynb)
- **Public Score**：`0.554`
- **说明**：复制并加速公开 CatBoost baseline；使用 Polars 对在线测试批次构造 session 级聚合特征，再按题目调用预训练 CatBoost 模型。
- **特征**：`event_name`、`name`、`fqid`、`room_fqid`、`text_fqid` 的出现次数与耗时统计；数值字段分位数/均值/标准差；关键词、房间、关卡及部分 bingo 任务链 duration。
- **推理**：按 `level_group` 预测对应题号，使用 `importance_dict.pkl` 做题目级特征筛选，概率阈值为 `0.63`。

### EXP-002: `v2.0-catboost+nn-lb_0.648.ipynb`

- **Notebook**：[`notebooks/v2.0-catboost+nn-lb_0.648.ipynb`](notebooks/v2.0-catboost+nn-lb_0.648.ipynb)
- **Public Score**：`0.648`
- **说明**：融合两套 CatBoost 表格模型与一套 Event-Aware TConv 序列神经网络，目标是提升不同题目的稳定性。
- **模型组合**：
  - CatBoost 1：Polars 大量聚合特征 + 题目级重要特征筛选。
  - CatBoost 2：`delt_time`、事件计数、关键文本/`fqid`/房间-关卡组合等题目专属特征。
  - TConv NN：取最近 `1000` 个事件，以 `et_diff`、`event_comb_code`、`room_fqid_code` 建模事件序列。
- **推理**：多数题使用 CatBoost 或两套 CatBoost 加权融合；`q5/q10` 使用 NN 输出；统一阈值 `0.63`。

### EXP-003: `v1.1-catboost-lb_0.699.ipynb`

- **Notebook**：[`notebooks/v1.1-catboost-lb_0.699.ipynb`](notebooks/v1.1-catboost-lb_0.699.ipynb)
- **Public Score**：`0.699`
- **说明**：题目级 CatBoost 方案；从 `train_labels.csv` 拆出 `session` 与 `q`，按 `level_group` 分段训练/推理不同题目。
- **特征**：基础 session 时间统计、`hover_duration` 聚合、从 `session_id` 解析出的时间特征，以及基于 `feature_sort.csv` 的题目专属事件条件特征。
- **推理**：对已建模题目按题生成特征并调用对应 CatBoost；部分题目使用默认规则填充；阈值为 `0.63`。
- **后续**：建议补充本地验证方式、外部输入依赖（如 `/kaggle/input/featur/`）和与 `v2.0` 的可复现实验对比。

### EXP-004: `v3.0-cat+xgb+mlp-lb_0.699.ipynb`

- **Notebook**：[`notebooks/v3.0-cat+xgb+mlp-lb_0.699.ipynb`](notebooks/v3.0-cat+xgb+mlp-lb_0.699.ipynb)
- **Public Score**：`0.699`
- **说明**：复制并改造 Vadim Kamaev 的 CatBoost 方案；沿用 `v1.1` 的题目级特征工程与 `feature_sort.csv`，但每道题同时训练 CatBoost、XGBoost、MLP 三个模型。
- **特征**：继续使用 `d_time`、`delt_time`、`delt_time_next`、`hover_duration`、session 时间特征，以及按题筛选的事件条件特征；相较 `v1.1`，部分题的 `list_kol_f` 数量增加（如 `q4/q6/q10/q14/q16`）。
- **模型组合**：
  - CatBoost：`n_estimators=300`、`learning_rate=0.045`、`depth=6`。
  - XGBoost：`n_estimators=300`、`learning_rate=0.25`、`max_depth=6`，并设置 `gamma/alpha` 正则。
  - MLP：`hidden_layer_sizes=(60, 30, 10)`、`activation='logistic'`、`solver='sgd'`。
- **推理**：对已建模题目按 `0.92 * CatBoost + 0.04 * XGBoost + 0.04 * MLP` 融合概率，再用阈值 `0.63` 转为 `correct`；未建模题仍沿用默认规则。
- **后续**：Public Score 与 `v1.1` 持平，建议在本地按 session 分组验证三模型融合是否稳定优于纯 CatBoost，并尝试按题单独调融合权重。
