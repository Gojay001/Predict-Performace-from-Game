#!/usr/bin/env python3
"""只读分析竞赛 CSV：行数、列名、session_id 基数、correct 分布、event_name 高频（若存在）。"""

from __future__ import annotations

import argparse
import csv
import math
import sys
from collections import Counter, defaultdict
from pathlib import Path


def _quantiles(sorted_vals: list[float], qs: tuple[float, ...]) -> dict[float, float]:
    if not sorted_vals:
        return {q: float("nan") for q in qs}
    n = len(sorted_vals)
    out: dict[float, float] = {}
    for q in qs:
        if n == 1:
            out[q] = sorted_vals[0]
            continue
        pos = q * (n - 1)
        lo = int(math.floor(pos))
        hi = int(math.ceil(pos))
        if lo == hi:
            out[q] = sorted_vals[lo]
        else:
            t = pos - lo
            out[q] = sorted_vals[lo] * (1 - t) + sorted_vals[hi] * t
    return out


def analyze(path: Path, max_event_samples: int = 30) -> str:
    lines: list[str] = []
    with path.open(newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        if not reader.fieldnames:
            return "错误：CSV 无表头\n"
        fieldnames = list(reader.fieldnames)
        rows = list(reader)

    n = len(rows)
    lines.append(f"文件: {path}")
    lines.append(f"行数（不含表头）: {n}")
    lines.append(f"列: {', '.join(fieldnames)}")

    if "session_id" in fieldnames:
        sess = {r.get("session_id", "") for r in rows}
        lines.append(f"\n[session_id] 唯一值数量: {len(sess)}（基于抽样全表时请自行流式统计）")

    if "correct" in fieldnames:
        c = Counter()
        bad = 0
        for r in rows:
            s = (r.get("correct") or "").strip()
            if s == "":
                bad += 1
                continue
            c[s] += 1
        lines.append("\n[correct] 取值计数（若二分类常见为 0/1）:")
        for k, v in sorted(c.items(), key=lambda x: (-x[1], str(x[0]))):
            lines.append(f"  {k!r}: {v}")
        if bad:
            lines.append(f"  空值/缺失: {bad}")

    if "event_name" in fieldnames:
        ec = Counter(r.get("event_name", "") for r in rows)
        lines.append(f"\n[event_name] 唯一事件类型数: {len(ec)}")
        lines.append("  Top 频率（最多列 {} 项）:".format(max_event_samples))
        for k, v in ec.most_common(max_event_samples):
            lines.append(f"  {k!r}: {v}")

    # 若存在 question 或 level 类列，列唯一值数量
    for col in ("level", "question", "fqid", "room_fqid"):
        if col in fieldnames:
            u = {r.get(col, "") for r in rows}
            lines.append(f"\n[{col}] 唯一值数量: {len(u)}")

    lines.append("")
    return "\n".join(lines)


def main() -> int:
    p = argparse.ArgumentParser(description="Analyze competition train CSV (stdlib only).")
    p.add_argument("--csv", type=Path, default=Path("data/train.csv"), help="Path to CSV")
    p.add_argument("--output", type=Path, default=None, help="Write report to file")
    args = p.parse_args()

    if not args.csv.is_file():
        print(f"找不到文件: {args.csv}", file=sys.stderr)
        print("请从 Kaggle 下载数据到 data/，见 data/README.md", file=sys.stderr)
        return 1

    report = analyze(args.csv)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(report, encoding="utf-8")
        print(f"已写入: {args.output}")
    else:
        print(report, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
