# -*- coding: utf-8 -*-
"""
M2 敏感性分析（P1 quick_estimate · 用 draft 数据先跑）
基准场景：雅加达 120m² 三居室公寓，现代风格，premium 档
方法：对每个参数组单独 ±20%，观察总价波动幅度 → 输出校对优先级
注意：所有基准值来自 obsidian-vault draft 节点（未校对），结论只用于排校对优先级，
      不代表最终估价精度。
"""
import io, json, sys

# ---------- 基准参数（来源：obsidian-vault 各 draft 节点） ----------
PARAMS = {
    # 工时定额 (工时/m²) —— 07_WorkHours
    "wh_waterproof_indo":   4.0,   # 防水沉箱 · 印尼技工
    "wh_screed_china":      0.8,   # 冲筋找平 · 中国技工
    "wh_tiling_indo":       0.8,   # 湿铺常规 · 印尼技工
    "wh_slab_china":        1.2,   # 大板岩板 · 中国技工
    "wh_ceiling_china":     1.0,   # 悬浮吊顶 · 中国技工
    # 日薪中位 (IDR) —— 06_Labor
    "rate_china":           550000,
    "rate_indo":            250000,
    "rate_general":         150000,
    # 材料单价 (IDR/m²) —— Atelier SKU 锚定
    "mat_waterproof":       100000,  # 防水体系材料（估算，无 SKU）
    "mat_screed":           30000,   # 砂浆类（估算，无 SKU）
    "mat_tiles":            280000,  # TILE-GRANITE-101 60×120
    "mat_slab":             650000,  # TILE-SLAB-202 进口岩板
    "mat_ceiling":          150000,  # 轻钢龙骨+石膏板体系（估算，无 SKU）
    # 工程量 (m²) —— 120m² 公寓简化换算
    "qty_waterproof":       10,      # 2 卫 × 5m²
    "qty_screed":           180,     # 墙面 300m² × 60% 高标准
    "qty_tiling":           80,      # 地面通铺
    "qty_slab":             15,      # 背景墙 + 玄关
    "qty_ceiling":          72,      # 60% 吊顶覆盖
    # 其他
    "waste_factor":         1.12,    # Atelier SKU 损耗系数
    "aux_ratio":            0.5,     # 普工辅助配比（技工工日×0.5）
}

def estimate(p):
    """底部向上合成总价（IDR）。返回 (总价, 材料小计, 人工小计)"""
    items = [
        # (工时key, 人工费率key, 材料key, 工程量key, 是否计普工辅助)
        ("wh_waterproof_indo", "rate_indo",  "mat_waterproof", "qty_waterproof", True),
        ("wh_screed_china",    "rate_china", "mat_screed",     "qty_screed",     False),
        ("wh_tiling_indo",     "rate_indo",  "mat_tiles",      "qty_tiling",     True),
        ("wh_slab_china",      "rate_china", "mat_slab",       "qty_slab",       True),
        ("wh_ceiling_china",   "rate_china", "mat_ceiling",    "qty_ceiling",    False),
    ]
    mat_total = lab_total = 0
    for wh_k, rate_k, mat_k, qty_k, aux in items:
        qty = p[qty_k]
        mat_total += p[mat_k] * qty * p["waste_factor"]
        days = p[wh_k] * qty / 8.0
        lab_total += days * p[rate_k]
        if aux:
            lab_total += days * p["aux_ratio"] * p["rate_general"]
    return mat_total + lab_total, mat_total, lab_total

def main():
    base_total, base_mat, base_lab = estimate(PARAMS)
    rows = []
    for key in PARAMS:
        if key in ("waste_factor", "aux_ratio"):
            pass
        swings = []
        for f in (0.8, 1.2):
            p2 = dict(PARAMS); p2[key] = PARAMS[key] * f
            t2, _, _ = estimate(p2)
            swings.append(t2 - base_total)
        impact = max(abs(s) for s in swings) / base_total * 100
        rows.append((key, PARAMS[key], impact))

    rows.sort(key=lambda r: -r[2])
    out = []
    out.append("# M2 敏感性分析报告（draft 数据 · 2026-08-27）\n")
    out.append("基准场景：雅加达 120m² 三居室公寓，现代风格 premium 档（5 道核心工序）\n")
    out.append("## 基准估价\n")
    out.append("- **总价**：Rp {:,.0f}".format(base_total))
    out.append("- 材料费：Rp {:,.0f}（{:.0f}%）".format(base_mat, base_mat/base_total*100))
    out.append("- 人工费（含普工辅助）：Rp {:,.0f}（{:.0f}%）\n".format(base_lab, base_lab/base_total*100))
    out.append("## 参数敏感度排行（单参数 ±20% → 总价最大波动）\n")
    out.append("| 排名 | 参数 | 基准值 | 总价波动 | 校对优先级 |")
    out.append("|---|---|---|---|---|")
    for i, (k, v, imp) in enumerate(rows, 1):
        prio = "🔴 P0" if imp >= 5 else ("🟡 P1" if imp >= 2 else "🟢 P2")
        out.append("| {} | `{}` | {:g} | ±{:.1f}% | {} |".format(i, k, v, imp, prio))
    out.append("\n## 结论与校对建议\n")
    top3 = [r[0] for r in rows[:3]]
    out.append("- 最敏感的 3 个参数：`{}`".format("`, `".join(top3)))
    out.append("- 材料价占基准总价 {:.0f}%——**材料类 ⚠️（尤其岩板/大理石瓷砖单价）优先于工时类校对**；".format(base_mat/base_total*100))
    out.append("- 工程量换算系数（墙面 2.5×面积、吊顶 60% 覆盖等）是隐藏变量，未列入本表但影响同量级，建议 Owner 一并确认；")
    out.append("- 本报告用 draft 数据，仅用于排校对顺序，不构成估价承诺。")
    text = "\n".join(out) + "\n"
    with io.open("docs/M2_敏感性分析报告.md", "w", encoding="utf-8") as f:
        f.write(text)
    print(text[:600])
    print("... written docs/M2_敏感性分析报告.md")

if __name__ == "__main__":
    main()
