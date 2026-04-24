# EDA：竞赛 CSV 只读分析

## 脚本

| 文件 | 说明 |
|------|------|
| `analyze_train_csv.py` | 只读统计行数、列名；若存在 `session_id` / `correct` / `event_name` 等列则做简单聚合 |

## 运行

在项目根目录执行（Python 3.9+，**仅标准库**）：

```bash
python experiments/eda/analyze_train_csv.py
```

指定路径或输出报告：

```bash
python experiments/eda/analyze_train_csv.py --csv data/train.csv
python experiments/eda/analyze_train_csv.py --output experiments/eda/output/train_report.txt
```

## 约定

- **不修改** `data/` 下原始竞赛文件（见 `AGENTS.md`）。
- 生成报告放在 `experiments/eda/output/`（默认 gitignore）。
