# -*- coding: utf-8 -*-
"""
P1 quick_estimate 数据导出脚本
解析 obsidian-vault 中的三类节点（markdown + frontmatter），输出 data/kg_estimate.json：
  - 05_Processes/*.md  工艺节点：id / name / status / relations / difficulty / 工序步骤数
  - 06_Labor/*.md      人工节点：id / 日薪区间（正文「Rp xxx–xxx」）
  - 07_WorkHours/*.md  工时节点：id / 关联工艺与人工 / 单位工时数值 / 日薪参考 / status
说明：
  - 工时节点中「N/A——严禁普工上手」属于合法业务结论（普工禁止上手），
    记为 value=null + na=true，不算解析失败。
  - 带 ⚠️ 的数字为模型估算值（status: draft），导出时如实保留 status 供下游标注。
运行：py -3 scripts/export_estimate_data.py
"""
import io
import json
import re
import sys
from datetime import datetime
from pathlib import Path

# Windows 控制台默认 GBK，强制 UTF-8 输出避免中文乱码
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

try:
    import yaml  # PyYAML 可用则走完整 frontmatter 解析
except ImportError:  # pragma: no cover - 兜底：极简 YAML 子集解析
    yaml = None

ROOT = Path(__file__).resolve().parent.parent
VAULT = ROOT / "obsidian-vault"
OUT = ROOT / "data" / "kg_estimate.json"

# 三个人工节点 id（用于从工时节点 relations 里区分工艺 / 人工）
LABOR_IDS = {"china-skilled-labor", "indonesian-skilled-labor", "local-indonesian-labor"}

# 正文正则
RE_DAILY_RATE = re.compile(r"Rp\s*([\d,]+)\s*[–-]\s*([\d,]+)")      # 日薪参考：Rp 200,000–300,000
RE_WORKHOUR_LINE = re.compile(r"单位工时[^\n]*")                       # 先捞「单位工时」整行
RE_WORKHOUR_VAL = re.compile(r"([\d.]+)\s*工时\s*/\s*([^\s⚠️（(；;，,]+)")  # 数值 + 单位
RE_STEP_NO = re.compile(r"^(\d+)\.\s", re.M)                          # 工序步骤编号（1. 2. 3. ...）
RE_DIFFICULTY = re.compile(r"难度[^\d]{0,10}(\d)")                     # 正文「难度」相关字段（目前没有，兜底）


def strip_wikilink(s):
    """relations target 有 [[xxx]] 与裸 id 两种写法，统一成裸 id。
    注意：PyYAML 会把 [[xxx]] 解析成嵌套列表 [['xxx']]，需要先解包。"""
    # YAML flow 嵌套列表解包：[['xxx']] → ['xxx'] → 'xxx'
    while isinstance(s, list) and len(s) == 1:
        s = s[0]
    if not isinstance(s, str):
        return s
    m = re.match(r"^\[\[([^\]|]+)(?:\|[^\]]+)?\]\]$", s.strip())
    return m.group(1) if m else s.strip()


def parse_frontmatter(text):
    """拆分 frontmatter / 正文；frontmatter 用 PyYAML，失败则走简易子集解析"""
    m = re.match(r"^---\n(.*?)\n---\n?(.*)$", text, re.S)
    if not m:
        return {}, text
    raw, body = m.group(1), m.group(2)
    if yaml is not None:
        try:
            return yaml.safe_load(raw) or {}, body
        except Exception:
            pass  # 落入简易解析
    # 简易 YAML 子集解析：只认顶层 key: value 与 relations 列表（够用即可）
    fm = {}
    cur_list = None
    cur_item = None
    for line in raw.splitlines():
        if re.match(r"^\S[^:]*:", line):
            k, _, v = line.partition(":")
            k, v = k.strip(), v.strip()
            cur_list = None
            if k == "relations":
                fm[k] = []
                cur_list = fm[k]
            elif v:
                fm[k] = v
        elif cur_list is not None and line.strip().startswith("- "):
            kv = line.strip()[2:]
            k, _, v = kv.partition(":")
            cur_item = {k.strip(): v.strip()}
            cur_list.append(cur_item)
        elif cur_item is not None and ":" in line:
            k, _, v = line.partition(":")
            cur_item[k.strip()] = v.strip()
    return fm, body


def parse_int(s):
    return int(s.replace(",", ""))


def load_nodes(subdir):
    nodes = []
    for f in sorted((VAULT / subdir).glob("*.md")):
        text = f.read_text(encoding="utf-8")
        fm, body = parse_frontmatter(text)
        nodes.append((f.name, fm, body))
    return nodes


def export_processes():
    """05_Processes：id / name / status / relations / difficulty / 工序步骤数"""
    out = []
    for fname, fm, body in load_nodes("05_Processes"):
        # 工序步骤数：中英文两节各自从 1 编号，取全文最大编号即步骤数
        steps = max([int(n) for n in RE_STEP_NO.findall(body)], default=0)
        difficulty = fm.get("difficulty")
        if difficulty is None:
            m = RE_DIFFICULTY.search(body)
            difficulty = int(m.group(1)) if m else None
        out.append({
            "id": fm.get("id"),
            "name": fm.get("name") or {},
            "status": fm.get("status"),
            "relations": [
                {"type": r.get("type"), "target": strip_wikilink(r.get("target"))}
                for r in (fm.get("relations") or [])
                if isinstance(r, dict)
            ],
            "difficulty": difficulty,
            "steps": steps,
        })
    return out


def export_labors():
    """06_Labor：id / 日薪区间（正文 Rp 正则，取 low/high/mid）"""
    out, warn = [], []
    for fname, fm, body in load_nodes("06_Labor"):
        m = RE_DAILY_RATE.search(body)
        if m:
            low, high = parse_int(m.group(1)), parse_int(m.group(2))
            rate = {"low": low, "high": high, "mid": (low + high) // 2}
        else:
            rate = None
            warn.append(f"人工节点未提取到日薪：{fname}（id={fm.get('id')}）")
        out.append({
            "id": fm.get("id"),
            "name": fm.get("name") or {},
            "status": fm.get("status"),
            "daily_rate": rate,
        })
    return out, warn


def export_workhours():
    """07_WorkHours：id / 关联工艺+人工 / 单位工时 / 日薪参考 / status"""
    out, warn = [], []
    for fname, fm, body in load_nodes("07_WorkHours"):
        process_id = None
        labor_candidates = []
        for r in (fm.get("relations") or []):
            if not isinstance(r, dict):
                continue
            t = strip_wikilink(r.get("target"))
            if t in LABOR_IDS:
                labor_candidates.append(t)  # 可能挂多个人工节点（对比链接），先收集
            elif r.get("type") in ("related_to", "requires_process", "mandatory_prerequisite_for"):
                process_id = process_id or t  # 首个非人工 related_to 视为工艺
        # 人工归属以节点自身 id 后缀为准（id 后缀 → 人工节点 id），兜底取首个候选
        node_id = fm.get("id") or ""
        ID_HINT = {
            "china-skilled": "china-skilled-labor",
            "indonesian-skilled": "indonesian-skilled-labor",
            "local-general": "local-indonesian-labor",
        }
        labor_id = next(
            (v for k, v in ID_HINT.items() if node_id.endswith(k) and v in labor_candidates),
            None,
        ) or (labor_candidates[0] if labor_candidates else None)
        # 单位工时：先捞整行；N/A（严禁普工上手）为合法结论，记 na=true
        value = unit = None
        na = False
        line_m = RE_WORKHOUR_LINE.search(body)
        if line_m:
            line = line_m.group(0)
            if "N/A" in line:
                na = True
            else:
                v_m = RE_WORKHOUR_VAL.search(line)
                if v_m:
                    value = float(v_m.group(1))
                    unit = v_m.group(2)
        if value is None and not na:
            warn.append(f"工时节点未提取到数值：{fname}（id={fm.get('id')}）")
        # 日薪参考（正文 Rp 正则）
        rate = None
        r_m = RE_DAILY_RATE.search(body)
        if r_m:
            low, high = parse_int(r_m.group(1)), parse_int(r_m.group(2))
            rate = {"low": low, "high": high, "mid": (low + high) // 2}
        out.append({
            "id": fm.get("id"),
            "process": process_id,
            "labor": labor_id,
            "value": value,
            "unit": unit,
            "na": na,  # True = 该工艺严禁此级人工上手（业务结论，非解析失败）
            "daily_rate_ref": rate,
            "status": fm.get("status"),
        })
    return out, warn


def main():
    processes = export_processes()
    labors, labor_warn = export_labors()
    workhours, wh_warn = export_workhours()

    data = {
        "generated_at": datetime.now().isoformat(timespec="seconds"),
        "source": "obsidian-vault（05_Processes / 06_Labor / 07_WorkHours），由 scripts/export_estimate_data.py 生成",
        "processes": processes,
        "labors": labors,
        "workhours": workhours,
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")

    # ---------- 解析统计（质量门槛） ----------
    wh_ok = [w for w in workhours if w["value"] is not None]
    wh_na = [w for w in workhours if w["na"]]
    labor_ok = [l for l in labors if l["daily_rate"] is not None]
    print("=" * 60)
    print(f"工艺节点 processes：{len(processes)} 个")
    print(f"人工节点 labors   ：{len(labor_ok)}/{len(labors)} 提取到日薪")
    print(f"工时节点 workhours：{len(wh_ok)} 个提取到数值 + {len(wh_na)} 个 N/A（严禁普工）"
          f" = {len(wh_ok) + len(wh_na)}/{len(workhours)} 覆盖")
    warns = labor_warn + wh_warn
    if warns:
        print("\n⚠️ 解析警告：")
        for w in warns:
            print(f"  - {w}")
    else:
        print("✅ 无解析失败（数值节点全部提取成功，N/A 节点均为业务上严禁普工）")
    print(f"\n输出：{OUT}")
    # 质量门槛：工时全覆盖（数值或 N/A）、人工全部有日薪，否则退出码 1
    if wh_warn or labor_warn:
        sys.exit(1)


if __name__ == "__main__":
    main()
