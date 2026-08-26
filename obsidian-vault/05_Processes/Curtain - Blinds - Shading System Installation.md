---
id: curtain-blinds-shading-installation
type: process
category: 01_construction_process
name:
  en: Curtain / Blinds / Shading System Installation
  zh: 窗帘/百叶/遮阳系统安装
summary:
  en: A high-end window treatment installation system for curtains, roman blinds, roller blinds, vertical blinds, and motorized shading systems. Mandatory for residential and commercial interiors. Requires precise bracketing, level alignment, and integration with smart home systems (if motorized).
  zh: 涵盖窗帘、罗马帘、卷帘、垂直百叶及电动遮阳系统的高端窗饰安装系统。适用于住宅及商业室内空间。要求精确支架安装、水平对齐及智能家居系统集成（电动款）。
tags:
  - curtains
  - blinds
  - motorized-shading
  - smart-home
  - window-treatment
  - indonesia
domain:
  - Construction
hierarchy: Processes/Installation/Window-Treatment
pantheon: N/A
relations:
  - type: requires_pretreatment
    target: [[wall-paint]]
  - type: requires_pretreatment
    target: [[premium-wall-paint-art-finish]]
  - type: requires_pretreatment
    target: [[electrical-wiring-first-fix]]
  - type: mandatory_material
    target: [[stainless-steel-brackets]]
  - type: mandatory_material
    target: [[motorized-curtain-track]]
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
# Curtain / Blinds / Shading System Installation（窗帘/百叶/遮阳系统安装）

> 🤖 本文件为窗饰安装工法。电动遮阳系统须在电气一次预埋阶段预留电源及控制线。

---

## English（EN）

### Core Parameters

|Parameter|Specification|Note|
|---|---|---|
|**Mounting Type**|Ceiling / Wall / Recessed|—|
|**Bracket Spacing**|≤ 600mm (curtain tracks) / ≤ 800mm (blinds)|—|
|**Level Tolerance**|≤ 2mm over full length|Laser level|
|**Motorized System**|230V hardwired or battery|Pre-wire required|
|**Smart Integration**|KNX / Zigbee / Wi-Fi|—|

### Key Workflow

1. **Site Measurement** → Measure window width/height. Verify recess depth for flush-mount systems.
    
2. **Bracket Installation** → Mark bracket positions with laser level. Install stainless steel brackets into substrate (concrete/wood).
    
3. **Track / Rail Installation** → Mount track/rail into brackets. Test smooth operation before hanging curtains/blinds.
    
4. **Curtain/Blind Hanging** → Hang curtains/blinds onto track. Test operation (manual or motorized).
    
5. **Motorized Setup** → Connect to power; pair with remote/App; program scenes if integrated with smart home.
    
6. **Final Adjustment** → Adjust curtain folds, stack-back position, and limit stops.
    

### QC Standards

|Criterion|Standard|Method|
|---|---|---|
|**Level**|≤2mm over full length|Laser level|
|**Bracket Security**|No movement under 5kg pull|Pull test|
|**Operation**|Smooth; no binding|Hand test|
|**Motorized Response**|≤500ms (if motorized)|Timer test|
|**Stack-back Alignment**|Uniform folds|Visual|

### Common Issues

|Issue|Cause|Solution|
|---|---|---|
|**Uneven Curtain Hanging**|Track not level|Laser-level track installation|
|**Motor Not Working**|No power / Not paired|Pre-wire power; pair remote|
|**Brackets Pulling Out**|Insufficient anchor depth|≥60mm embedment into concrete|
|**Fabric Fading (UV)**|No UV-protective lining|Specify UV-blocking lining for sun-exposed windows|

### Related Knowledge

- **Labor**: [[window-treatment-specialist]]
    
- **Materials**: [[curtain-track]], [[stainless-steel-brackets]], [[motorized-curtain-track]]
    
- **Prerequisite**: [[wall-paint]] / [[premium-wall-paint-art-finish]] (wall finish complete)
    

---

## 中文（ZH）

### 核心参数

|参数|规格指标|备注|
|---|---|---|
|**安装方式**|天花/墙面/嵌入式|—|
|**支架间距**|轨道≤600mm / 百叶≤800mm|—|
|**水平公差**|全长≤2mm|激光水平仪|
|**电动系统**|230V硬线或电池|需预留电源|
|**智能集成**|KNX / Zigbee / Wi-Fi|—|

### 工序要点

1. **现场测量** → 测量窗宽/高；核对嵌入式安装的凹槽深度。
    
2. **支架安装** → 激光标线；不锈钢支架固定于基层（混凝土/木）。
    
3. **轨道安装** → 轨道入支架；挂窗帘前测试滑行顺畅度。
    
4. **挂装窗帘/百叶** → 挂装；手动/电动操作测试。
    
5. **电动调试** → 通电；遥控/App配对；智能场景编程（如适用）。
    
6. **最终调整** → 调节窗帘皱褶、堆叠位置及限位。
    

### 验收标准

|验收项|标准|方法|
|---|---|---|
|**水平度**|全长≤2mm|激光水平仪|
|**支架牢固度**|5kg拉力无位移|拉拔测试|
|**操作顺畅度**|无卡滞|手测|
|**电动响应**|≤500ms|计时测试|
|**堆叠对齐**|褶皱均匀|目视|

### 关联知识

- **人力**：[[window-treatment-specialist|窗饰安装专项技师]]
    
- **材料**：[[curtain-track|窗帘轨道]]、[[stainless-steel-brackets|不锈钢支架]]、[[motorized-curtain-track|电动窗帘轨道]]
    
- **前置**：[[wall-paint|墙面涂料]] / [[premium-wall-paint-art-finish|高端涂料/艺术漆]]
    

---

## 双链闭环结构


[[curtain-blinds-shading-installation]]（窗帘/遮阳系统安装核心节点）
├── 前置 → [[wall-paint]] / [[premium-wall-paint-art-finish]]（墙面完成）
├── 电动款 → [[electrical-wiring-first-fix]]（预留电源/控制线）
├── 强制 → 激光水平校准（≤2mm）· 不锈钢支架（防锈）
├── 智能集成 → [[smart-home-system-installation]]（KNX/Zigbee）
└── 禁忌 → 禁止使用普通铁支架（锈蚀）· 禁止无预留电源安装电动款