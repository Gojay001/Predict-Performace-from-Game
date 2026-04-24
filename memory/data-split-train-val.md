# 数据划分约定（按 Session）

本赛题日志通常以 **`session_id`**（或等价 **游戏会话** 键）串联多条事件。若随机对**事件行**做 train/val 划分，容易把**同一会话**同时放进训练与验证，造成 **信息泄漏**（验证分数虚高）。

---

## 1. 推荐做法

1. 从 `train.csv`（或聚合后的 session 表）提取 **唯一 `session_id` 集合**。
2. 在 **唯一 session** 上做 `GroupKFold` / `train_test_split(..., groups=session_id)` 等，保证 **同一会话只出现在 train 或 val 一侧**。
3. 若标签粒度为 **`session_id` + 题目**（与 `sample_submission` 行一一对应），划分键需与评测粒度一致（例如按 session 分组时，该 session 下所有题目行同属 train 或 val）。

---

## 2. 指标对齐

- 官方指标见 [docs/competition-spec.md](../docs/competition-spec.md) 与 [Evaluation 页](https://www.kaggle.com/competitions/predict-student-performance-from-game-play/overview/evaluation)。
- 本地验证请使用与官网一致的 **F1** 实现（含宏平均、二值化阈值等细节）。

---

## 3. 复现检查项

- [ ] 划分单位是 **session（或题目键，与赛题一致）** 而非 **无分组随机行**
- [ ] `SEED` 与 notebook 一致
- [ ] 数据文件版本与 Kaggle 当前 Data 版本一致

---

更新日期：2026-04-23
