# -*- coding: utf-8 -*-
"""
校对速查表生成器（作战顺序版 · 按 M2 敏感性分析排优先级）
扫描 obsidian-vault 全部 ⚠️ 行，按敏感度批次分组输出 CHECKLIST.md
"""
import io, os

root = "obsidian-vault"

# 批次定义：(目录, 行关键词过滤 or None=全部)
BATCHES = [
    ("第一批 · 材料单价（🔴 敏感度最高，先打）", "04_Materials", None),
    ("第二批 · 人工日薪与效率（🟡 中国技工日薪优先）", "06_Labor", None),
    ("第三批 · 工时定额（🟢 可最后过）", "07_WorkHours", None),
    ("第四批 · 工艺标准与容差（🟢 多为施工标准，扫读即可）", "05_Processes", None),
]

# 静态：待 Owner 拍板的非 ⚠️ 条目（来自 M2 敏感性分析）
DECISION_ITEMS = [
    ("损耗系数 waste_factor = 1.12", "±14.6%（全场最敏感）", "来自 Atelier SKU 表，请按你实际损耗确认"),
    ("地面工程量 = 建筑面积 × 0.67（80/120）", "±7.3%", "通铺比例按你的项目实际"),
    ("吊顶工程量 = 建筑面积 × 60%", "±4.5%", "悬浮吊顶覆盖率"),
    ("墙面找平工程量 = 建筑面积 × 2.5 × 60% 高标准", "±4.2%", "墙面系数 2.5 + 高标准比例"),
    ("岩板背景墙工程量 = 15m²", "±3.3%", "背景墙 + 玄关的典型配置量"),
    ("普工辅助配比 = 技工工日 × 0.5", "±0.3%", "大板/防水/贴砖才计辅助"),
    ("巴厘岛区域系数 = 1.1", "未测", "P1 设计文档 §6 问题 2"),
    ("工期并行系数 = 0.7 / 斋月系数 = 1.3", "未测", "交叉施工压缩率与斋月放大率"),
]

def collect(dirpath):
    rows = []
    if not os.path.isdir(dirpath):
        return rows
    for fn in sorted(os.listdir(dirpath)):
        if not fn.endswith(".md"):
            continue
        with io.open(os.path.join(dirpath, fn), encoding="utf-8") as f:
            lines = f.read().split("\n")
        hits = [(i + 1, l.strip()) for i, l in enumerate(lines)
                if "⚠️" in l and not l.strip().startswith(">")]
        if hits:
            rows.append((fn[:-3], hits))
    return rows

def main():
    out = []
    total = 0
    out.append("# 校对速查表 · 作战顺序版（自动生成 2026-08-27）\n")
    out.append("> 按 M2 敏感性分析排序：先打最值钱的。每过完一篇：删 ⚠️ → `status: draft` 改 `verified` → commit。")
    out.append("> 双语文件同一数字有 EN/ZH 两行镜像，全局替换该数值即可。\n")

    # 第〇批
    out.append("## 第〇批 · 待你拍板的规则参数（不是 ⚠️，但敏感度最高，先定）\n")
    out.append("| 参数 | 总价敏感度 | 说明 |")
    out.append("|---|---|---|")
    for name, imp, note in DECISION_ITEMS:
        out.append("| %s | %s | %s |" % (name, imp, note))
    out.append("")
    out.append("> 拍板方式：直接在下方表格里填你的值，或回复我逐条确认，我写回对应文件。")
    out.append("| 参数 | 你的确认值 |")
    out.append("|---|---|")
    for name, _, _ in DECISION_ITEMS:
        out.append("| %s |  |" % name)
    out.append("")

    # 批次 1-4
    for title, d, _ in BATCHES:
        rows = collect(os.path.join(root, d))
        batch_total = sum(len(h) for _, h in rows)
        total += batch_total
        out.append("\n## %s（%d 处）\n" % (title, batch_total))
        for fn, hits in rows:
            out.append("### %s（%d 处）\n" % (fn, len(hits)))
            for n, l in hits:
                if len(l) > 120:
                    l = l[:117] + "..."
                out.append("- [ ] L%d: %s" % (n, l))
            out.append("")

    out.append("\n---")
    out.append("全库共 **%d 处 ⚠️**。校对完重跑 `scripts/generate_checklist.py` 核对清零。" % total)

    with io.open("CHECKLIST.md", "w", encoding="utf-8") as f:
        f.write("\n".join(out) + "\n")
    print("total:", total)

if __name__ == "__main__":
    main()
