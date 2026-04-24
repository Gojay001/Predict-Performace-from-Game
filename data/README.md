# 竞赛数据（本地）

## 获取方式

1. 打开 Kaggle 竞赛 [Data](https://www.kaggle.com/competitions/predict-student-performance-from-game-play/data)。
2. 下载数据包，将所需 CSV 解压到本目录 **`data/`**（与 `README.md` 中的结构一致）。

## 预期文件（以官网为准）

| 文件 | 说明 |
|------|------|
| `train.csv` | 训练事件日志（体积通常很大） |
| `train_labels.csv` | 训练标签（若有） |
| `test.csv` | 测试相关表（若有） |
| `sample_submission.csv` | 提交格式样例 |

## Git 约定

- **勿修改** 官方原始 CSV 内容（分析请复制副件或在 notebook 内处理）。
- 默认 **`.gitignore` 忽略大体积 `train.csv` / `test.csv` / `train_labels.csv`**，避免误提交；若你有小样本脱敏切片需入库，再单独调整 `.gitignore` 并在 PR/提交说明中注明来源。

仓库内 **`sample_submission.csv`** 仅为**占位表头**示例；正式比赛请以你下载的官方文件替换或并存为 `sample_submission.official.csv` 自行对比。
