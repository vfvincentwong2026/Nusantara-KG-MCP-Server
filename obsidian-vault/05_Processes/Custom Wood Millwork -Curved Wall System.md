---
id: custom-wood-millwork-curved
type: process
category: 01_construction_process
name:
  en: Custom Wood Millwork / Curved Wall System
  zh: 木作造型/弧形墙面系统
summary:
  en: A high-end millwork system for custom wood paneling, curved walls, and feature walls using engineered timber products. Requires CNC-precision fabrication, on-site templating, and specialized installation with concealed fixings. Critical for luxury residential and commercial interiors.
  zh: 采用工程木制品实现定制木饰面、弧形墙及造型墙的高端木作系统。需要CNC精密加工、现场复尺及带隐藏式紧固件的专业安装。适用于豪华住宅及商业室内空间。
tags:
  - millwork
  - curved-wall
  - custom-paneling
  - wood-veneer
  - cnc-fabrication
  - concealed-fixing
  - indonesia
domain:
  - Construction
hierarchy: Processes/Millwork/Custom-Wood
pantheon: N/A
relations:
  - type: requires_pretreatment
    target: [[ribbed-screed-gauging-strips]]
  - type: mandatory_material
    target: [[engineered-timber-panels]]
  - type: mandatory_material
    target: [[concealed-clips]]
  - type: mandatory_material
    target: [[flexible-adhesive]]
  - type: requires_tool
    target: [[laser-level]]
  - type: recommended_for
    target: [[living-room]]
  - type: recommended_for
    target: [[bedroom]]
locations:
  - indonesia
  - java
  - bali
cultural_elements: []
created_at: 2026-08-27
updated_at: 2026-08-27
status: published
---
# Custom Wood Millwork / Curved Wall System（木作造型/弧形墙面系统）

> 🤖 本文件为高端木作造型工法。弧形墙面须在工厂预制弯板，严禁现场湿法弯曲。所有木质材料须经防白蚁处理。

---

## English（EN）

### Core Parameters

|Parameter|Specification|Note|
|---|---|---|
|**Panel Thickness**|12–18mm (engineered timber)|—|
|**Veneer Thickness**|0.6–1.2mm (real wood veneer)|—|
|**Radius of Curvature (Min.)**|≥ 5 x panel thickness|Factory pre-bent|
|**Substrate Flatness**|≤2mm/2m|[[ribbed-screed-gauging-strips]]|
|**Fixing Type**|Concealed clips / magnetic system|No visible screws|
|**Expansion Gap**|2–3mm at all panel junctions|—|

### Key Workflow

1. **Site Templating** → Laser measure all walls. Create digital template for CNC cutting. Include allowance for curves.
    
2. **Factory Fabrication** → CNC-cut panels; pre-bend curved panels in press; veneer applied in factory.
    
3. **Substrate Preparation** → Ensure wall flatness ≤2mm/2m. Install moisture barrier if required.
    
4. **Panel Fixing** → Install concealed clips on substrate. Hang panels and lock into clips. For curved sections, use flexible adhesive + concealed clips.
    
5. **Joint Management** → Leave 2–3mm expansion gaps between panels. Fill with flexible color-matched filler.
    
6. **Edge Treatment** → Veneer all exposed edges. Sand and finish to match panels.
    

### QC Standards

|Criterion|Standard|Method|
|---|---|---|
|**Panel Flatness**|≤1mm/2m|2m straightedge|
|**Joint Gap**|2–3mm uniform|Feeler gauge|
|**Curvature Accuracy**|≤2mm deviation from template|Template overlay|
|**Veneer Match**|No visible color difference|Raking light test|
|**Fixing Security**|No movement under 10kg pull|Pull test|

### Common Issues

|Issue|Cause|Solution|
|---|---|---|
|**Panel Warping (Humidity)**|Insufficient acclimatization|7-day on-site acclimatization|
|**Joint Opening**|Expansion gap insufficient|Allow 2–3mm + flexible filler|
|**Curve Cracking**|Radius too tight / Not pre-bent|Minimum radius 5× thickness; pre-bend in press|
|**Visible Fixings**|No concealed system|Use concealed clips / magnetic mounts|

### Related Knowledge

- **Labor**: [[millwork-specialist]]
    
- **Materials**: [[engineered-timber-panels]], [[concealed-clips]], [[flexible-adhesive]]
    
- **Prerequisite**: [[ribbed-screed-gauging-strips]]
    

---

## 中文（ZH）

### 核心参数

|参数|规格指标|备注|
|---|---|---|
|**面板厚度**|12–18mm（工程木）|—|
|**木皮厚度**|0.6–1.2mm（实木贴皮）|—|
|**最小弯曲半径**|≥ 5倍板厚|工厂预制弯板|
|**基层平整度**|≤2mm/2m|[[ribbed-screed-gauging-strips\|冲筋找平]]|
|**固定方式**|隐藏式卡扣/磁吸系统|无外露螺丝|
|**伸缩缝**|板缝2–3mm|—|

### 工序要点

1. **现场复尺** → 激光测量全线；生成CNC切割数字模板（含曲线放样）。
    
2. **工厂预制** → CNC切割；弧形板冷压机预弯；工厂贴木皮。
    
3. **基层准备** → 墙面平整度≤2mm/2m；必要时安装防潮层。
    
4. **面板固定** → 基层安装隐藏式卡扣；挂装面板入扣；弧线段用柔性胶+隐藏卡扣组合。
    
5. **接缝管理** → 预留2–3mm伸缩缝；填充柔性调色填缝料。
    
6. **边部处理** → 所有裸露边缘贴木皮；打磨至与面板一致。
    

### 验收标准

|验收项|标准|方法|
|---|---|---|
|**面板平整度**|≤1mm/2m|2m靠尺|
|**接缝宽度**|2–3mm均匀|塞尺|
|**弧度精度**|较模板偏差≤2mm|模板比对|
|**木皮色差**|无可视色差|侧光检查|
|**固定牢固度**|10kg拉力无位移|拉拔测试|

### 关联知识

- **人力**：[[millwork-specialist|木作造型专项技师]]
    
- **材料**：[[engineered-timber-panels|工程木面板]]、[[concealed-clips|隐藏式卡扣]]、[[flexible-adhesive|柔性胶粘剂]]
    
- **前置**：[[ribbed-screed-gauging-strips|冲筋找平]]
    

---

## 双链闭环结构

```text
[[custom-wood-millwork-curved]]（木作造型核心节点）
├── 前置 → [[ribbed-screed-gauging-strips]]（墙面平整度≤2mm/2m）
├── 强制 → 弧形板工厂预制（严禁现场湿弯）· 防白蚁处理
├── 关键 → 隐藏式固定（无可见螺丝）· 伸缩缝2–3mm
└── 人力 → [[millwork-specialist]]（CNC+预制弯板专项技师）
```
