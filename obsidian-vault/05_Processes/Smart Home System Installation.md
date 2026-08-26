---
id: smart-home-system-installation
type: process
category: 01_construction_process
name:
  en: Smart Home System Installation
  zh: 全屋智能家居系统安装
summary:
  en: Integrated installation of smart lighting, curtain control, HVAC, security, and audio-visual systems with centralized gateway and scene automation. Mandatory pre-wiring during first-fix electrical phase.
  zh: 集成智能灯光、窗帘控制、暖通空调、安防及影音系统的集中式网关与场景自动化安装。须在电气一次预埋阶段完成布线预留。
tags:
  - smart-home
  - KNX
  - zigbee
  - lighting-control
  - automation
  - indonesia
domain:
  - Construction
hierarchy: Processes/Electrical/Smart-Home
pantheon: N/A
relations:
  - type: requires_pretreatment
    target: [[electrical-wiring-first-fix]]
  - type: requires_pretreatment
    target: [[electrical-switch-socket-installation]]
  - type: mandatory_material
    target: [[smart-gateway]]
  - type: mandatory_material
    target: [[shielded-cable]]
  - type: requires_tool
    target: [[network-analyzer]]
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
# Smart Home System Installation（全屋智能家居系统安装）

> 🤖 本文件为智能家居安装标准。所有弱电布线须采用屏蔽线缆，强电与弱电间距 ≥300mm 防干扰。

---

## English（EN）

### Core Parameters

|Parameter|Specification|Note|
|---|---|---|
|**Communication Protocol**|KNX / Zigbee / Wi-Fi / Z-Wave|KNX preferred for new builds|
|**Gateway**|Centralized with backup power|UPS mandatory|
|**Shielded Cable**|CAT6A / CAT7 (for data)|—|
|**Cable Separation**|≥300mm from 230V cables|EMI prevention|
|**Scene Programming**|Minimum 4 scenes per room|—|

### Key Workflow

1. **Pre-wire (First-Fix)** → Run all sensor/control cables to central panel. Use CAT6A shielded for all controls.
    
2. **Gateway Installation** → Mount central controller in electrical panel. Install UPS backup.
    
3. **Device Wiring** → Connect dimmers, relays, curtain motors, and sensors to gateway.
    
4. **Configuration** → Set IP addresses, group addresses, and scene logic. Program minimum 4 scenes per room.
    
5. **Testing** → Verify all functions; app connectivity; voice assistant integration.
    

### QC Standards

|Criterion|Standard|Method|
|---|---|---|
|**Cable Continuity**|All pairs continuous|Network tester|
|**Shield Ground**|<1Ω to earth|Multimeter|
|**Signal Strength**|≥ -70 dBm (Wi-Fi/Zigbee)|Spectrum analyzer|
|**Scene Response**|≤500ms delay|Stopwatch test|

### Common Issues

|Issue|Cause|Solution|
|---|---|---|
|**Interference**|Cable too close to power lines|Maintain ≥300mm separation|
|**Device Offline**|Weak signal|Add repeaters; check gateway power|
|**Scene Not Triggering**|Programming error|Re-map scene logic in software|

### Related Knowledge

- **Labor**: [[smart-home-specialist]]
    
- **Materials**: [[smart-gateway]], [[shielded-cable]], [[dimmer-module]]
    
- **Prerequisite**: [[electrical-wiring-first-fix]]
    

---

## 中文（ZH）

### 核心参数

|参数|规格指标|备注|
|---|---|---|
|**通讯协议**|KNX / Zigbee / Wi-Fi|KNX优先|
|**网关**|集中式 + UPS备电|强制|
|**屏蔽线缆**|CAT6A / CAT7|数据用|
|**强弱电间距**|≥300mm|防干扰|
|**场景数量**|每房间≥4种|—|

### 工序要点

1. **一次预埋** → 所有控制线缆集中引至配电箱。使用CAT6A屏蔽线。
    
2. **网关安装** → 配电箱内安装主控器 + UPS备电。
    
3. **设备接线** → 调光模块、继电器、窗帘电机、传感器接入网关。
    
4. **系统编程** → 配置IP地址、组地址、场景逻辑。每房间≥4场景。
    
5. **系统测试** → 功能验证；App控制；语音助手集成测试。
    

### 验收标准

|验收项|标准|方法|
|---|---|---|
|**线缆通断**|8芯全通|网络测试仪|
|**屏蔽接地**|<1Ω|万用表|
|**信号强度**|≥ -70 dBm|频谱分析仪|
|**场景响应**|≤500ms|秒表测试|

### 关联知识

- **人力**：[[smart-home-specialist|智能家居专项技师]]
    
- **材料**：[[smart-gateway|智能网关]]、[[shielded-cable|屏蔽线缆]]、[[dimmer-module|调光模块]]
    
- **前置**：[[electrical-wiring-first-fix|电气一次预埋]]
    

---

## 双链闭环结构


[[smart-home-system-installation]]（智能家居核心节点）
├── 前置 → [[electrical-wiring-first-fix]]（一次预埋）
├── 强制 → 强弱电间距≥300mm · CAT6A屏蔽线 · UPS备电
├── 验收 → 信号≥-70dBm · 场景响应≤500ms
└── 场景 → [[living-room]] · [[bedroom]]（每房间≥4场景）