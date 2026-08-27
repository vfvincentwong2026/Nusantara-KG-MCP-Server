# 校对速查表 · 作战顺序版（自动生成 2026-08-27）

> 按 M2 敏感性分析排序：先打最值钱的。每过完一篇：删 ⚠️ → `status: draft` 改 `verified` → commit。
> 双语文件同一数字有 EN/ZH 两行镜像，全局替换该数值即可。

## 第〇批 · 待你拍板的规则参数（不是 ⚠️，但敏感度最高，先定）

| 参数 | 总价敏感度 | 说明 |
|---|---|---|
| 损耗系数 waste_factor = 1.12 | ±14.6%（全场最敏感） | 来自 Atelier SKU 表，请按你实际损耗确认 |
| 地面工程量 = 建筑面积 × 0.67（80/120） | ±7.3% | 通铺比例按你的项目实际 |
| 吊顶工程量 = 建筑面积 × 60% | ±4.5% | 悬浮吊顶覆盖率 |
| 墙面找平工程量 = 建筑面积 × 2.5 × 60% 高标准 | ±4.2% | 墙面系数 2.5 + 高标准比例 |
| 岩板背景墙工程量 = 15m² | ±3.3% | 背景墙 + 玄关的典型配置量 |
| 普工辅助配比 = 技工工日 × 0.5 | ±0.3% | 大板/防水/贴砖才计辅助 |
| 巴厘岛区域系数 = 1.1 | 未测 | P1 设计文档 §6 问题 2 |
| 工期并行系数 = 0.7 / 斋月系数 = 1.3 | 未测 | 交叉施工压缩率与斋月放大率 |

> 拍板方式：直接在下方表格里填你的值，或回复我逐条确认，我写回对应文件。
| 参数 | 你的确认值 |
|---|---|
| 损耗系数 waste_factor = 1.12 |  |
| 地面工程量 = 建筑面积 × 0.67（80/120） |  |
| 吊顶工程量 = 建筑面积 × 60% |  |
| 墙面找平工程量 = 建筑面积 × 2.5 × 60% 高标准 |  |
| 岩板背景墙工程量 = 15m² |  |
| 普工辅助配比 = 技工工日 × 0.5 |  |
| 巴厘岛区域系数 = 1.1 |  |
| 工期并行系数 = 0.7 / 斋月系数 = 1.3 |  |


## 第一批 · 材料单价（🔴 敏感度最高，先打）（104 处）

### Art Paint艺术漆（16 处）

- [ ] L23: size: 桶装 5-20kg ⚠️
- [ ] L29: per_m2: 45000 ⚠️
- [ ] L57: Art paint is the highest cost-performance premium wall finish: at Rp 45,000–120,000/㎡ ⚠️ it delivers effects that vis...
- [ ] L62: - **Maintenance**: 低-中；局部修补需同批材料 ⚠️
- [ ] L63: - **Durability (Indonesia climate)**: 高湿下需防霉底漆；沿海盐雾环境建议罩面 ⚠️
- [ ] L70: - **前置工序**：[[ribbed-screed-gauging-strips|冲筋找平]]——灯光洗墙场景垂平度 ≤2mm/2m ⚠️
- [ ] L72: - **施工禁忌**：雨季高湿需延长层间干燥 ⚠️；同一墙面必须同批材料连续施工，停工即留接痕 ⚠️
- [ ] L79: ### Supplier Reference (Jakarta) ⚠️
- [ ] L81: - 渠道：本地艺术涂料专营（含施工队打包）⚠️；进口威尼斯灰泥经品牌代理 ⚠️
- [ ] L88: 艺术漆是性价比最高的高端墙面方案：Rp 45,000–120,000/㎡ ⚠️ 即可实现视觉上媲美石材/木饰面的效果，成本仅为其 1/5–1/10。材料本身容错率高，但施工者不容错——同一桶漆，不同手艺人做出的效果天差地别。
- [ ] L93: - **维护**：低-中；局部修补需同批材料 ⚠️
- [ ] L94: - **耐久性（印尼气候）**：高湿需防霉底漆；沿海盐雾建议罩面 ⚠️
- [ ] L101: - **前置工序**：[[ribbed-screed-gauging-strips|冲筋找平]]——洗墙场景垂平度 ≤2mm/2m ⚠️
- [ ] L103: - **施工禁忌**：雨季延长层间干燥 ⚠️；同墙面同批材料连续施工 ⚠️
- [ ] L110: ### 供应商参考（雅加达）⚠️
- [ ] L112: - 渠道：本地艺术涂料专营（含施工打包）⚠️；进口威尼斯灰泥品牌代理 ⚠️

### Epoxy Grout美缝剂（18 处）

- [ ] L23: size: 400ml 双管装（约施工 25-35m 缝）⚠️
- [ ] L26: brand: 进口（MAPEI 类）；国产（卓高/德高类）；本地杂牌 ⚠️
- [ ] L28: per_unit: 150000 ⚠️
- [ ] L29: per_m2: 15000 ⚠️
- [ ] L55: Epoxy grout is the cheapest "premium upgrade" in any tiling project: Rp 15,000–25,000/㎡ of floor area ⚠️, yet it is w...
- [ ] L61: - **Durability (Indonesia climate)**: 高湿环境显著优于水泥填缝；卫浴湿区强制环氧 ⚠️
- [ ] L68: - **推荐人工**：[[indonesian-skilled-labor|印尼技工]]（可独立承担，需培训压缝手法 ⚠️）
- [ ] L69: - **施工禁忌**：砖缝未干透即施工（发白脱落）⚠️；余料擦洗超时（环氧固化后铲不净）⚠️；卫浴禁用水泥填缝替代
- [ ] L76: ### Supplier Reference (Jakarta) ⚠️
- [ ] L77: - **Atelier SKU 锚定**：⚠️ Atelier 51 SKU 中暂无美缝剂条目，建议新增（`ACCESSORY-GROUT-001`，锚定价 Rp 150,000/400ml）
- [ ] L78: - 渠道：建材市场辅料区（本地杂牌多，警惕固化慢/变色）；MAPEI 等品牌经建材代理 ⚠️
- [ ] L85: 美缝剂是铺贴项目中最便宜的"高端升级"：地面每平米仅 Rp 15,000–25,000 ⚠️，却是业主每天目光落点。印尼高湿气候下，水泥填缝数月即在湿区发霉，环氧美缝近乎永久。失败都来自工序而非产品：抢工（砖层未养护）、清缝不净、余料...
- [ ] L91: - **耐久性（印尼气候）**：远优于水泥填缝；卫浴湿区强制环氧 ⚠️
- [ ] L98: - **推荐人工**：[[indonesian-skilled-labor|印尼技工]]（可独立，需培训压缝手法 ⚠️）
- [ ] L99: - **施工禁忌**：缝未干透施工（发白脱落）⚠️；余料擦洗超时 ⚠️；卫浴禁用水泥填缝
- [ ] L106: ### 供应商参考（雅加达）⚠️
- [ ] L107: - **Atelier SKU 锚定**：⚠️ Atelier 暂无美缝剂 SKU，建议新增（`ACCESSORY-GROUT-001`，锚定价 Rp 150,000/400ml）
- [ ] L108: - 渠道：建材市场辅料区（警惕杂牌固化慢/变色）；MAPEI 品牌代理 ⚠️

### Marble Tiles大理石瓷砖（12 处）

- [ ] L23: size: 600×1200mm / 900×1800mm ⚠️
- [ ] L29: per_m2: 280000 ⚠️
- [ ] L64: - **Durability (Indonesia climate)**: 优异；高湿环境配合防碱背涂可杜绝泛碱 ⚠️
- [ ] L70: - **必须工艺**：[[wet-method-tiling|湿铺法贴砖]]（常规规格）；≥900×1800 按 [[large-format-slab-installation|大板铺贴]] 管理 ⚠️
- [ ] L72: - **施工禁忌**：调平器强制使用；雨季测基层含水率 ⚠️；同空间用同批次砖（色差）
- [ ] L79: ### Supplier Reference (Jakarta) ⚠️
- [ ] L81: - 渠道：Roman/Granito 品牌展厅与经销商（雅加达各建材市场均有）⚠️
- [ ] L94: - **耐久性（印尼气候）**：优异；高湿配合防碱背涂杜绝泛碱 ⚠️
- [ ] L100: - **必须工艺**：[[wet-method-tiling|湿铺法贴砖]]；≥900×1800 按 [[large-format-slab-installation|大板铺贴]] 管理 ⚠️
- [ ] L102: - **施工禁忌**：强制调平器；雨季测基层含水率 ⚠️；同空间同批次（色差）
- [ ] L109: ### 供应商参考（雅加达）⚠️
- [ ] L111: - 渠道：Roman/Granito 展厅与经销商 ⚠️

### Microcement微水泥（15 处）

- [ ] L23: size: 桶装 20kg（约 10-12㎡/桶·遍）⚠️
- [ ] L26: brand: 进口（Topciment 类）；本地替代（质量不稳）⚠️
- [ ] L29: per_m2: 450000 ⚠️
- [ ] L60: - **Maintenance**: 低；污渍及时擦拭，定期补罩面 ⚠️
- [ ] L61: - **Durability (Indonesia climate)**: 高湿环境必须低含水率基层 + 除湿养护，否则泛白发花 ⚠️
- [ ] L68: - **前置工序**：[[ribbed-screed-gauging-strips|冲筋找平]]——基层垂平度 ≤2mm/2m 是硬前提 ⚠️
- [ ] L70: - **施工禁忌**：雨季施工必须室内除湿（含水率超标即停工）⚠️；每层间隔时间不可压缩；禁用本地无体系杂牌材料 ⚠️
- [ ] L77: ### Supplier Reference (Jakarta) ⚠️
- [ ] L79: - 渠道：进口品牌印尼代理；警惕本地"微水泥"替代品——成膜体系不完整，一年后开裂案例高发 ⚠️
- [ ] L91: - **维护**：低；定期补罩面 ⚠️
- [ ] L92: - **耐久性（印尼气候）**：高湿必须低含水率基层 + 除湿养护，否则泛白发花 ⚠️
- [ ] L99: - **前置工序**：[[ribbed-screed-gauging-strips|冲筋找平]]——垂平度 ≤2mm/2m 硬前提 ⚠️
- [ ] L101: - **施工禁忌**：雨季必须室内除湿 ⚠️；层间间隔不可压缩；禁用本地无体系杂牌 ⚠️
- [ ] L108: ### 供应商参考（雅加达）⚠️
- [ ] L110: - 渠道：进口品牌印尼代理；警惕本地替代品——成膜体系不完整，一年后开裂高发 ⚠️

### SPC Flooring SPC石塑地板（15 处）

- [ ] L23: size: 1220×180mm 常规 ⚠️
- [ ] L24: thickness: 4-5mm ⚠️
- [ ] L29: per_m2: 160000 ⚠️
- [ ] L58: - **Scratch resistance**: 中-高（取决于耐磨层 0.3-0.5mm）⚠️
- [ ] L60: - **Durability (Indonesia climate)**: 优异——防水防白蚁，一楼/沿海可用；暴晒阳台区需防褪色 ⚠️
- [ ] L63: 远看类木地板；近看与侧光下质感弱于真木——premium 5mm 级（Marvel 类）纹理明显更真 ⚠️。
- [ ] L68: - **施工禁忌**：基层平整度 ≤3mm/2m 仍是铁律（锁扣断裂/响声根源）⚠️；周边 8mm 伸缩缝不可省；避免阳光暴晒区域通铺 ⚠️
- [ ] L75: ### Supplier Reference (Jakarta) ⚠️
- [ ] L77: - 渠道：本地建材市场多品牌；Marvel 等 premium 线经品牌经销 ⚠️
- [ ] L88: - **耐刮性**：中-高（看耐磨层 0.3-0.5mm）⚠️
- [ ] L90: - **耐久性（印尼气候）**：优异——防水防白蚁，一楼/沿海可用；暴晒区防褪色 ⚠️
- [ ] L93: 远看类木；近看与侧光下质感弱于真木——premium 5mm 级纹理明显更真 ⚠️。
- [ ] L98: - **施工禁忌**：基层 ≤3mm/2m 铁律（锁扣断裂/响声根源）⚠️；8mm 伸缩缝不可省；暴晒区勿通铺 ⚠️
- [ ] L105: ### 供应商参考（雅加达）⚠️
- [ ] L107: - 渠道：本地建材市场多品牌；premium 线品牌经销 ⚠️

### Sintered Stone岩板（15 处）

- [ ] L23: size: 1200×2400mm / 900×1800mm ⚠️
- [ ] L24: thickness: 6-12mm ⚠️
- [ ] L29: per_m2: 650000 ⚠️
- [ ] L57: Sintered stone is the flagship material of Indonesian premium interiors — the default choice for living-room feature ...
- [ ] L63: - **Durability (Indonesia climate)**: 高湿高盐雾（巴厘岛沿海）下表现优异；基层湿气须用防潮底涂隔离 ⚠️
- [ ] L71: - **施工禁忌**：严禁普通切割机手动切割（崩边）；需水刀/桥切 ⚠️；搬运必须吸盘架双人作业；印尼雨季进场注意包装防潮
- [ ] L78: ### Supplier Reference (Jakarta) ⚠️
- [ ] L80: - 渠道：雅加达建材进口商（Tanjung Priok 港清关）、品牌代理展厅（MKG/PIK 区域）⚠️
- [ ] L81: - 国产岩板（新明珠类）价格约进口的 50-60%，纹理与平整度有差距 ⚠️
- [ ] L88: 岩板是印尼高端室内的旗舰材料——客厅背景墙与大面无缝地面的默认选项。物理性能极佳（莫氏 6+ 硬度、吸水率趋零、耐高温），但施工失败会抹平一切优势：单片 1200×2400 岩板价值 Rp 2–4 百万 ⚠️，破损不可修复。
- [ ] L94: - **耐久性（印尼气候）**：高湿高盐雾（巴厘岛沿海）表现优异；基层湿气需防潮底涂隔离 ⚠️
- [ ] L102: - **施工禁忌**：严禁手动切割（崩边），需水刀/桥切 ⚠️；吸盘架双人搬运；雨季进场防包装受潮
- [ ] L109: ### 供应商参考（雅加达）⚠️
- [ ] L111: - 渠道：雅加达建材进口商（Tanjung Priok 港清关）、品牌代理展厅 ⚠️
- [ ] L112: - 国产岩板价格约进口的 50-60%，纹理与平整度有差距 ⚠️

### Wood Flooring木地板（13 处）

- [ ] L23: size: 1200×190mm 常规 ⚠️
- [ ] L24: thickness: 8-15mm ⚠️
- [ ] L29: per_m2: 300000 ⚠️
- [ ] L60: - **Maintenance**: 中——忌积水，拖地半干 ⚠️
- [ ] L61: - **Durability (Indonesia climate)**: 高湿是头号敌人：必须防潮垫 + 周边 8-10mm 伸缩缝；一楼/地面层慎用，优先楼上 ⚠️
- [ ] L69: - **施工禁忌**：基层含水率超标即停工（雨季重点）⚠️；伸缩缝不足必起拱；到货后现场适应 48-72 小时 ⚠️
- [ ] L76: ### Supplier Reference (Jakarta) ⚠️
- [ ] L78: - 渠道：Golden Crown/Kendo 经销商；进口实木复合经品牌代理 ⚠️
- [ ] L90: - **维护**：中——忌积水 ⚠️
- [ ] L91: - **耐久性（印尼气候）**：高湿头号敌人：防潮垫 + 周边 8-10mm 伸缩缝；一楼慎用 ⚠️
- [ ] L99: - **施工禁忌**：基层含水率超标停工 ⚠️；伸缩缝不足必起拱；现场适应 48-72 小时 ⚠️
- [ ] L106: ### 供应商参考（雅加达）⚠️
- [ ] L108: - 渠道：Golden Crown/Kendo 经销商；进口品牌代理 ⚠️


## 第二批 · 人工日薪与效率（🟡 中国技工日薪优先）（69 处）

### China Skilled Labor中国技工（23 处）

- [ ] L32: min: 450000 ⚠️
- [ ] L33: max: 650000 ⚠️
- [ ] L34: efficiency_per_10sqm: 1.5 ⚠️
- [ ] L89: - **Daily rate**: Rp 450,000–650,000 ⚠️
- [ ] L90: - **Efficiency**: ~1.5 man-days per 10m² (large-format tiling) ⚠️
- [ ] L91: - **Cost logic**: slow but precise; rework rate near zero, so total cost is optimal on premium work ⚠️
- [ ] L96: | Daily rate | Rp 450k–650k ⚠️ | Rp 200k–300k ⚠️ | Rp 120k–180k ⚠️ |
- [ ] L99: | Communication cost | Needs translator / drawings ⚠️ | Local language, no barrier | Local language, no barrier |
- [ ] L100: | Schedule stability | Stable, but usually booked out ⚠️ | Ramadan/holiday delays possible | Ramadan/holiday delays p...
- [ ] L101: | Compliance note | Foreign worker permits (KITAS/IMTA) must be verified ⚠️ | — | — |
- [ ] L112: - Extremely tight schedules — senior crews are typically booked in advance ⚠️
- [ ] L134: - **日薪**：Rp 450,000–650,000 ⚠️
- [ ] L135: - **效率**：大板铺贴约 1.5 工日/10m² ⚠️
- [ ] L136: - **成本逻辑**：慢工出细活，返工率趋零，高端工序总成本最优 ⚠️
- [ ] L141: | 日薪 | Rp 450k–650k ⚠️ | Rp 200k–300k ⚠️ | Rp 120k–180k ⚠️ |
- [ ] L144: | 沟通成本 | 需翻译/图纸沟通 ⚠️ | 本地语言无障碍 | 本地语言无障碍 |
- [ ] L145: | 工期稳定性 | 稳定但排期常满 ⚠️ | 斋月/节假日可能延误 | 斋月/节假日可能延误 |
- [ ] L146: | 合规提醒 | 外籍劳工证件（KITAS/IMTA）须核实 ⚠️ | — | — |
- [ ] L157: - 工期极紧的项目——高级技工通常排期较满 ⚠️
- [ ] L186: │   ├── 日薪 Rp 450k-650k ⚠️ → 对比 [[indonesian-skilled-labor]] · [[local-indonesian-labor]]
- [ ] L187: │   └── 效率 1.5 工日/10m² ⚠️ → [[large-format-slab-installation]]
- [ ] L199: │   └── 极紧工期 → 排期风险 ⚠️
- [ ] L201: └── 外籍劳工证件（KITAS/IMTA）⚠️

### Indonesian Skilled Labor印尼本地技工（23 处）

- [ ] L32: min: 200000 ⚠️
- [ ] L33: max: 300000 ⚠️
- [ ] L34: efficiency_per_10sqm: 1.0 ⚠️
- [ ] L90: - **Daily rate**: Rp 200,000–300,000 ⚠️
- [ ] L91: - **Efficiency**: ~1.0 man-day per 10m² (standard tiling) ⚠️
- [ ] L92: - **Cost logic**: best cost-performance on standard work; rework risk rises sharply on high-precision finishes ⚠️
- [ ] L97: | Daily rate | Rp 200k–300k ⚠️ | Rp 450k–650k ⚠️ | Rp 120k–180k ⚠️ |
- [ ] L100: | Communication cost | Local language, no barrier | Needs translator / drawings ⚠️ | Local language, no barrier |
- [ ] L101: | Schedule stability | Ramadan/holiday delays possible ⚠️ | Stable but booked out ⚠️ | Ramadan/holiday delays possibl...
- [ ] L102: | Availability | High across major islands ⚠️ | Limited, advance booking | Very high |
- [ ] L113: - Unsupervised precision work — QC drift risk ⚠️
- [ ] L135: - **日薪**：Rp 200,000–300,000 ⚠️
- [ ] L136: - **效率**：常规贴砖约 1.0 工日/10m² ⚠️
- [ ] L137: - **成本逻辑**：标准工序性价比最优；高精度面层返工风险显著上升 ⚠️
- [ ] L142: | 日薪 | Rp 200k–300k ⚠️ | Rp 450k–650k ⚠️ | Rp 120k–180k ⚠️ |
- [ ] L145: | 沟通成本 | 本地语言无障碍 | 需翻译/图纸 ⚠️ | 本地语言无障碍 |
- [ ] L146: | 工期稳定性 | 斋月/节假日可能延误 ⚠️ | 稳定但排期满 ⚠️ | 斋月/节假日可能延误 ⚠️ |
- [ ] L147: | 可获得性 | 各主要岛屿较充足 ⚠️ | 有限，需预约 | 非常充足 |
- [ ] L158: - 无监督的精度工序——质量漂移风险 ⚠️
- [ ] L188: │   ├── 日薪 Rp 200k-300k ⚠️ → 对比 [[china-skilled-labor]] · [[local-indonesian-labor]]
- [ ] L189: │   └── 效率 1.0 工日/10m² ⚠️ → [[wet-method-tiling]]
- [ ] L201: │   ├── 斋月/节假日延误 ⚠️ → [[indonesia-ramadan]]
- [ ] L202: │   └── 无监督精度漂移 ⚠️ → [[quality-control]]

### Local Indonesian Labor印尼本地普工（23 处）

- [ ] L31: min: 120000 ⚠️
- [ ] L32: max: 180000 ⚠️
- [ ] L33: efficiency_per_10sqm: 0.8 ⚠️
- [ ] L74: - **Daily rate**: Rp 120,000–180,000 ⚠️
- [ ] L75: - **Efficiency**: ~0.8 man-day per 10m² (auxiliary tasks) ⚠️
- [ ] L76: - **Cost logic**: cheapest per head, but unsupervised output is unreliable — supervision cost must be budgeted ⚠️
- [ ] L81: | Daily rate | Rp 120k–180k ⚠️ | Rp 200k–300k ⚠️ | Rp 450k–650k ⚠️ |
- [ ] L84: | Communication cost | Local language, no barrier | Local language, no barrier | Needs translator / drawings ⚠️ |
- [ ] L85: | Schedule stability | Ramadan/holiday delays possible ⚠️ | Ramadan/holiday delays possible ⚠️ | Stable but booked ou...
- [ ] L86: | Supervision need | Constant, on-site ⚠️ | Periodic inspection | Minimal for their trade |
- [ ] L98: - Working unsupervised on site ⚠️
- [ ] L117: - **日薪**：Rp 120,000–180,000 ⚠️
- [ ] L118: - **效率**：辅助工序约 0.8 工日/10m² ⚠️
- [ ] L119: - **成本逻辑**：人头最便宜，但无监督产出不可靠——必须把监督成本计入预算 ⚠️
- [ ] L124: | 日薪 | Rp 120k–180k ⚠️ | Rp 200k–300k ⚠️ | Rp 450k–650k ⚠️ |
- [ ] L127: | 沟通成本 | 本地语言无障碍 | 本地语言无障碍 | 需翻译/图纸 ⚠️ |
- [ ] L128: | 工期稳定性 | 斋月/节假日可能延误 ⚠️ | 斋月/节假日可能延误 ⚠️ | 稳定但排期满 ⚠️ |
- [ ] L129: | 监督需求 | 全程现场监督 ⚠️ | 定期巡检 | 本工种内极少 |
- [ ] L141: - 无监督在场作业 ⚠️
- [ ] L169: │   ├── 日薪 Rp 120k-180k ⚠️ → 对比 [[indonesian-skilled-labor]] · [[china-skilled-labor]]
- [ ] L170: │   └── 效率 0.8 工日/10m² ⚠️（辅助工序）
- [ ] L180: │   ├── 斋月/节假日延误 ⚠️ → [[indonesia-ramadan]]
- [ ] L181: │   └── 无监督产出不可靠 ⚠️ → 监督成本入预算


## 第三批 · 工时定额（🟢 可最后过）（350 处）

### WorkHour Bathroom Waterproofing - China Skilled（12 处）

- [ ] L42: - **Unit work hour**: 3.5 man-hours/m² ⚠️（按卫生间地面面积计，含墙面翻边）
- [ ] L43: - **Reference duration**: ~4.5 man-days per 10m² ⚠️（含两道防水、二次排水、LECA 回填、配筋找平；**不含**两次 24h 闭水试验的等待时间）
- [ ] L44: - **Daily rate reference**: Rp 450,000–650,000 ⚠️
- [ ] L47: - **Ramadan / holidays**: 中国技工不受斋月影响，但混编班组的整体进度受印尼工友出勤影响 ⚠️
- [ ] L48: - **Rainy season**: 基层含水率高，第一道防水前需延长晾基层时间，可能 +0.5 工日/间 ⚠️
- [ ] L49: - **Difficulty adjustment**: 沉箱深度 >400mm 或异形管井多时，工时上浮 15–20% ⚠️
- [ ] L59: - **单位工时**：3.5 工时/m² ⚠️（按卫生间地面面积计，含墙面翻边）
- [ ] L60: - **参考工期**：10m² 约 4.5 工日 ⚠️（含两道防水、二次排水、LECA 回填、配筋找平；**不含**两次 24 小时闭水试验等待时间）
- [ ] L61: - **日薪参考**：Rp 450,000–650,000 ⚠️
- [ ] L64: - **斋月/节假日**：中国技工不受斋月影响，但混编班组整体进度受印尼工友出勤影响 ⚠️
- [ ] L65: - **雨季**：基层含水率高，第一道防水前需延长晾基层时间，可能 +0.5 工日/间 ⚠️
- [ ] L66: - **难度折算**：沉箱深度 >400mm 或异形管井较多时，工时上浮 15–20% ⚠️

### WorkHour Bathroom Waterproofing - Indonesian Skilled（12 处）

- [ ] L42: - **Unit work hour**: 4.0 man-hours/m² ⚠️（精细度训练成本略高于中国技工）
- [ ] L43: - **Reference duration**: ~5.0 man-days per 10m² ⚠️（不含闭水试验等待时间）
- [ ] L44: - **Daily rate reference**: Rp 200,000–300,000 ⚠️
- [ ] L47: - **Ramadan / holidays**: 斋月期间有效工时下降约 20–30%，工期排期需按 1.3 倍系数放大 ⚠️
- [ ] L48: - **Rainy season**: 同中国技工，晾基层 +0.5 工日/间 ⚠️
- [ ] L49: - **Difficulty adjustment**: 本地技工对二次排水口细部处理经验参差，**闭水试验必须两次全做**，渗漏返工风险计入 10% 余量 ⚠️
- [ ] L59: - **单位工时**：4.0 工时/m² ⚠️
- [ ] L60: - **参考工期**：10m² 约 5.0 工日 ⚠️（不含闭水试验等待时间）
- [ ] L61: - **日薪参考**：Rp 200,000–300,000 ⚠️
- [ ] L64: - **斋月/节假日**：斋月期间有效工时下降约 20–30%，排期按 1.3 倍系数放大 ⚠️
- [ ] L65: - **雨季**：晾基层 +0.5 工日/间 ⚠️
- [ ] L66: - **难度折算**：二次排水口细部经验参差，**两次闭水试验必须全做**，渗漏返工风险计入 10% 余量 ⚠️

### WorkHour Bathroom Waterproofing - Local General（10 处）

- [ ] L43: - **Unit work hour**: N/A for waterproofing application — **forbidden** ⚠️
- [ ] L44: - **Auxiliary reference**: LECA transport & placement assistance ~1.5 man-days per 10m² cistern ⚠️（在技工直接指挥下）
- [ ] L45: - **Daily rate reference**: Rp 120,000–180,000 ⚠️
- [ ] L48: - **Ramadan / holidays**: 斋月期间搬运类体力工序效率下降约 30%，宜安排在上午 ⚠️
- [ ] L50: - **Difficulty adjustment**: 严禁独立摊铺压实陶粒——级配与坡度由技工把控，普工仅供料 ⚠️
- [ ] L60: - **单位工时**：防水涂刷 **N/A——严禁普工上手** ⚠️
- [ ] L61: - **辅助参考**：陶粒运输与摊铺辅助约 1.5 工日/10m² 沉箱 ⚠️（技工直接指挥下）
- [ ] L62: - **日薪参考**：Rp 120,000–180,000 ⚠️
- [ ] L65: - **斋月/节假日**：斋月体力工序效率下降约 30%，宜安排上午作业 ⚠️
- [ ] L67: - **难度折算**：严禁独立摊铺压实陶粒——级配与坡度由技工把控，普工仅供料 ⚠️

### WorkHour Floating Ceiling - China Skilled（12 处）

- [ ] L42: - **Unit work hour**: 1.0 man-hour/m² ⚠️（按吊顶投影面积，含龙骨、封板、阴影缝型材）
- [ ] L43: - **Reference duration**: ~1.25 man-days per 10m² ⚠️
- [ ] L44: - **Daily rate reference**: Rp 450,000–650,000 ⚠️
- [ ] L47: - **Ramadan / holidays**: 本人不受影响 ⚠️
- [ ] L48: - **Rainy season**: 无显著影响（室内工序）；石膏板进场注意防潮 ⚠️
- [ ] L49: - **Difficulty adjustment**: 弧形/异形悬浮吊顶上浮 50%；双层悬浮或多级跌级上浮 30%；无主灯预埋联动工序另计 ⚠️
- [ ] L59: - **单位工时**：1.0 工时/m² ⚠️（按吊顶投影面积，含龙骨、封板、阴影缝型材）
- [ ] L60: - **参考工期**：10m² 约 1.25 工日 ⚠️
- [ ] L61: - **日薪参考**：Rp 450,000–650,000 ⚠️
- [ ] L64: - **斋月/节假日**：本人不受影响 ⚠️
- [ ] L65: - **雨季**：无显著影响（室内工序）；石膏板进场注意防潮 ⚠️
- [ ] L66: - **难度折算**：弧形/异形上浮 50%；双层悬浮/多级跌级上浮 30%；无主灯预埋联动另计 ⚠️

### WorkHour Floating Ceiling - Indonesian Skilled（12 处）

- [ ] L44: - **Unit work hour**: 1.5 man-hours/m² ⚠️（标准平面吊顶）
- [ ] L45: - **Reference duration**: ~1.9 man-days per 10m² ⚠️
- [ ] L46: - **Daily rate reference**: Rp 200,000–300,000 ⚠️
- [ ] L49: - **Ramadan / holidays**: 斋月有效工时下降 20–30%，排期按 1.3 倍系数 ⚠️
- [ ] L50: - **Rainy season**: 无显著影响 ⚠️
- [ ] L51: - **Difficulty adjustment**: 阴影缝型材细部精度不足，悬浮造型返工风险计 20% 余量 ⚠️；弧形悬浮**禁止**本级独立承担，转 [[china-skilled-labor]]
- [ ] L61: - **单位工时**：1.5 工时/m² ⚠️（标准平面吊顶）
- [ ] L62: - **参考工期**：10m² 约 1.9 工日 ⚠️
- [ ] L63: - **日薪参考**：Rp 200,000–300,000 ⚠️
- [ ] L66: - **斋月/节假日**：斋月有效工时下降 20–30%，排期按 1.3 倍系数 ⚠️
- [ ] L67: - **雨季**：无显著影响 ⚠️
- [ ] L68: - **难度折算**：阴影缝型材细部精度不足，悬浮造型返工风险计 20% 余量 ⚠️；弧形悬浮**禁止**本级独立承担，转 [[china-skilled-labor]]

### WorkHour Floating Ceiling - Local General（10 处）

- [ ] L42: - **Unit work hour**: N/A for ceiling installation — **forbidden** ⚠️
- [ ] L43: - **Auxiliary reference**: board lifting & material transport ~0.5 man-day per 10m² ⚠️（技工直接指挥下）
- [ ] L44: - **Daily rate reference**: Rp 120,000–180,000 ⚠️
- [ ] L47: - **Ramadan / holidays**: 斋月体力工序效率下降约 30%，高空举升作业尤需避开午后疲劳时段 ⚠️
- [ ] L49: - **Difficulty adjustment**: 龙骨定位与封板固定涉及测量/容差，普工全程不得上手；板材传递需防边角磕碰 ⚠️
- [ ] L59: - **单位工时**：吊顶安装 **N/A——严禁普工上手** ⚠️
- [ ] L60: - **辅助参考**：板材举升与材料搬运约 0.5 工日/10m² ⚠️（技工直接指挥下）
- [ ] L61: - **日薪参考**：Rp 120,000–180,000 ⚠️
- [ ] L64: - **斋月/节假日**：斋月体力工序效率下降约 30%，高空举升避开午后疲劳时段 ⚠️
- [ ] L66: - **难度折算**：龙骨定位与封板固定涉及测量/容差，普工全程不得上手；板材传递防边角磕碰 ⚠️

### WorkHour Large-Format Slab - China Skilled（12 处）

- [ ] L42: - **Unit work hour**: 1.2 man-hours/m² ⚠️（含双人抬铺、吸盘架作业、调平器系统）
- [ ] L43: - **Reference duration**: ~1.5 man-days per 10m² ⚠️
- [ ] L44: - **Daily rate reference**: Rp 450,000–650,000 ⚠️
- [ ] L47: - **Ramadan / holidays**: 本人不受影响 ⚠️
- [ ] L48: - **Rainy season**: 室内工序，影响小；石材类材料需注意进场防潮 ⚠️
- [ ] L49: - **Difficulty adjustment**: 1.2m×2.4m 以上岩板背景墙（立面）工时上浮 50%；无缝拼接（密缝）上浮 30%；损耗率按 8–10% 另计材料 ⚠️
- [ ] L59: - **单位工时**：1.2 工时/m² ⚠️（含双人抬铺、吸盘架作业、调平器系统）
- [ ] L60: - **参考工期**：10m² 约 1.5 工日 ⚠️
- [ ] L61: - **日薪参考**：Rp 450,000–650,000 ⚠️
- [ ] L64: - **斋月/节假日**：本人不受影响 ⚠️
- [ ] L65: - **雨季**：室内工序影响小；石材进场注意防潮 ⚠️
- [ ] L66: - **难度折算**：1.2m×2.4m 以上岩板立面上浮 50%；密缝无缝拼接上浮 30%；材料损耗率 8–10% 另计 ⚠️

### WorkHour Large-Format Slab - Indonesian Skilled（12 处）

- [ ] L44: - **Unit work hour**: 2.0 man-hours/m² ⚠️（**不推荐**——缺乏大板专用工具与抬铺经验）
- [ ] L45: - **Reference duration**: ~2.5 man-days per 10m² ⚠️
- [ ] L46: - **Daily rate reference**: Rp 200,000–300,000 ⚠️
- [ ] L49: - **Ramadan / holidays**: 斋月有效工时下降 20–30% ⚠️
- [ ] L50: - **Rainy season**: 同常规铺贴 ⚠️
- [ ] L51: - **Difficulty adjustment**: 空鼓/破损返工风险按 30–40% 计入 ⚠️——大板单片材料成本高，一次破损的材料损失即超过与中国技工的工费差价，**经济性上不成立**
- [ ] L61: - **单位工时**：2.0 工时/m² ⚠️（**不推荐**——缺乏大板专用工具与抬铺经验）
- [ ] L62: - **参考工期**：10m² 约 2.5 工日 ⚠️
- [ ] L63: - **日薪参考**：Rp 200,000–300,000 ⚠️
- [ ] L66: - **斋月/节假日**：斋月有效工时下降 20–30% ⚠️
- [ ] L67: - **雨季**：同常规铺贴 ⚠️
- [ ] L68: - **难度折算**：空鼓/破损返工风险按 30–40% 计入 ⚠️——大板单片材料成本高，一次破损的材料损失即超过与中国技工的工费差价，**经济性上不成立**

### WorkHour Large-Format Slab - Local General（8 处）

- [ ] L42: - **Unit work hour**: N/A — **strictly forbidden** ⚠️
- [ ] L43: - **Auxiliary reference**: packaging removal & cleanup only, ~0.3 man-day per 10m² ⚠️
- [ ] L44: - **Daily rate reference**: Rp 120,000–180,000 ⚠️
- [ ] L49: - **Difficulty adjustment**: 大板单片价值高、破损不可逆——普工触碰即构成风险敞口，抬铺仅限受过训练的技工双人组合 ⚠️
- [ ] L59: - **单位工时**：**N/A——严禁承担** ⚠️
- [ ] L60: - **辅助参考**：仅拆包装与现场清理，约 0.3 工日/10m² ⚠️
- [ ] L61: - **日薪参考**：Rp 120,000–180,000 ⚠️
- [ ] L66: - **难度折算**：大板单片价值高、破损不可逆——普工触碰即构成风险敞口，抬铺仅限受过训练的技工双人组合 ⚠️

### WorkHour Microcement - China Skilled（14 处）

- [ ] L42: - **Unit work hour**: 0.7 man-hours/m² ⚠️（底层批刮+抗裂网铺设+面层 2 遍+罩面剂，按展开面积计）
- [ ] L43: - **Reference duration**: ~0.9 man-days per 10m² ⚠️（不含层间干燥等待）
- [ ] L44: - **Daily rate reference**: Rp 450,000–650,000 ⚠️
- [ ] L47: - **Ramadan / holidays**: 本人不受影响；混编班组进度受印尼工友出勤影响 ⚠️
- [ ] L48: - **Rainy season**: 层间干燥时间延长（湿度 >80% RH），总工期 +1 工日/10m²；罩面前含水率强制检测 ⚠️
- [ ] L49: - **Difficulty adjustment**: 弧形/异形面上浮 50%；墙地一体无缝收边上浮 30%；基层平整度 >2mm/2m 须先冲筋找平（另计 [[workhour-screed-leveling-china-ski...
- [ ] L52: 行业经验估算：微水泥熟练工完整四遍体系效率约 10–15 m²/工日（含批刮与罩面，不含干燥等待），取中值 12 m²/工日 ≈ 0.67 工时/m²，取整 0.7 ⚠️（与 [[china-skilled-labor]] 效率字段一...
- [ ] L59: - **单位工时**：0.7 工时/m² ⚠️（底层批刮+抗裂网铺设+面层 2 遍+罩面剂，按展开面积计）
- [ ] L60: - **参考工期**：10m² 约 0.9 工日 ⚠️（不含层间干燥等待）
- [ ] L61: - **日薪参考**：Rp 450,000–650,000 ⚠️
- [ ] L64: - **斋月/节假日**：本人不受影响；混编班组进度受印尼工友出勤影响 ⚠️
- [ ] L65: - **雨季**：层间干燥时间延长（湿度 >80% RH），总工期 +1 工日/10m²；罩面前含水率强制检测 ⚠️
- [ ] L66: - **难度折算**：弧形/异形面上浮 50%；墙地一体无缝收边上浮 30%；基层平整度 >2mm/2m 须先冲筋找平（另计 [[workhour-screed-leveling-china-skilled]]）⚠️
- [ ] L69: 行业经验估算：微水泥熟练工完整四遍体系效率约 10–15 m²/工日（含批刮与罩面，不含干燥等待），取中值 12 m²/工日 ≈ 0.67 工时/m²，取整 0.7 ⚠️（与 [[china-skilled-labor]] 效率字段一...

### WorkHour Microcement - Indonesian Skilled（12 处）

- [ ] L43: - **Unit work hour**: 1.2 man-hours/m² ⚠️（**不推荐**——四遍批刮依赖熟练手感，本级仅限中国技工指导下的底层批刮；面层纹理效果无法保证，返工风险计 25% 余量）
- [ ] L44: - **Reference duration**: ~1.5 man-days per 10m² ⚠️
- [ ] L45: - **Daily rate reference**: Rp 200,000–300,000 ⚠️
- [ ] L48: - **Ramadan / holidays**: 斋月有效工时下降 20–30%，排期按 1.3 倍系数 ⚠️
- [ ] L49: - **Rainy season**: 层间干燥时间延长，总工期 +1 工日/10m² ⚠️
- [ ] L50: - **Difficulty adjustment**: KG 共识——微水泥为**强制中国技工**工艺（[[microcement-wall-finishing]]）。派本级仅适用于：底层批刮工序分包、且面层由中国技工收光。整套派本...
- [ ] L60: - **单位工时**：1.2 工时/m² ⚠️（**不推荐**——四遍批刮依赖熟练手感，本级仅限中国技工指导下的底层批刮；面层纹理效果无法保证，返工风险计 25% 余量）
- [ ] L61: - **参考工期**：10m² 约 1.5 工日 ⚠️
- [ ] L62: - **日薪参考**：Rp 200,000–300,000 ⚠️
- [ ] L65: - **斋月/节假日**：斋月有效工时下降 20–30%，排期按 1.3 倍系数 ⚠️
- [ ] L66: - **雨季**：层间干燥时间延长，总工期 +1 工日/10m² ⚠️
- [ ] L67: - **难度折算**：KG 共识——微水泥为**强制中国技工**工艺（[[microcement-wall-finishing]]）。派本级仅适用于底层批刮分包、面层由中国技工收光；整套派本级等于主动接受返工 ⚠️

### WorkHour Microcement - Local General（12 处）

- [ ] L42: - **Unit work hour**: Microcement application **N/A — forbidden for general labor** ⚠️
- [ ] L43: - **Auxiliary reference**: material mixing & transport ~0.4 man-day per 10m² ⚠️（技工直接指挥下；微水泥可施工窗口短，供料须连续）
- [ ] L44: - **Daily rate reference**: Rp 120,000–180,000 ⚠️
- [ ] L47: - **Ramadan / holidays**: 斋月体力工序效率下降约 30%，宜安排上午作业 ⚠️
- [ ] L48: - **Rainy season**: 无显著影响（室内工序），但材料须防潮存放 ⚠️
- [ ] L49: - **Difficulty adjustment**: 微水泥拌料水灰比由技工定量，普工不得自行加水——搅拌不均是面层色差的高发诱因 ⚠️
- [ ] L59: - **单位工时**：微水泥施工 **N/A——严禁普工上手** ⚠️
- [ ] L60: - **辅助参考**：拌料搬运约 0.4 工日/10m² ⚠️（技工直接指挥下；微水泥可施工窗口短，供料须连续）
- [ ] L61: - **日薪参考**：Rp 120,000–180,000 ⚠️
- [ ] L64: - **斋月/节假日**：斋月体力工序效率下降约 30%，宜安排上午作业 ⚠️
- [ ] L65: - **雨季**：无显著影响（室内工序），材料须防潮存放 ⚠️
- [ ] L66: - **难度折算**：拌料水灰比由技工定量，普工不得自行加水——搅拌不均是面层色差的高发诱因 ⚠️

### WorkHour Recessed Lighting - China Skilled（12 处）

- [ ] L42: - **Unit work hour**: 1.5 man-hours per meter of track run ⚠️（含预埋框安装与封板收口，筒灯点位按每 2m 轨道 1 个折算）
- [ ] L43: - **Reference duration**: ~2 man-days per 10m track run（约 1 个客厅）⚠️
- [ ] L44: - **Daily rate reference**: Rp 450,000–650,000 ⚠️
- [ ] L47: - **Ramadan / holidays**: 本人不受影响；混编班组进度受印尼工友出勤影响 ⚠️
- [ ] L48: - **Rainy season**: 吊顶空腔凝露检查可能 +0.5 工日/项目 ⚠️
- [ ] L49: - **Difficulty adjustment**: 弧形轨道走向上浮 40%；多分区调光（≥4 区）上浮 20%；与智能调光联动调试另计 ⚠️
- [ ] L59: - **单位工时**：1.5 工时/延米轨道 ⚠️（含预埋框与封板收口；筒灯点位按每 2m 轨道 1 个折算）
- [ ] L60: - **参考工期**：10m 轨道（约 1 个客厅）约 2 工日 ⚠️
- [ ] L61: - **日薪参考**：Rp 450,000–650,000 ⚠️
- [ ] L64: - **斋月/节假日**：本人不受影响；混编班组进度受印尼工友出勤影响 ⚠️
- [ ] L65: - **雨季**：吊顶空腔凝露检查可能 +0.5 工日/项目 ⚠️
- [ ] L66: - **难度折算**：弧形轨道上浮 40%；多分区调光（≥4 区）上浮 20%；智能联动调试另计 ⚠️

### WorkHour Recessed Lighting - Indonesian Skilled（12 处）

- [ ] L44: - **Unit work hour**: 2.2 man-hours per meter of track run ⚠️（标准直线段）
- [ ] L45: - **Reference duration**: ~2.8 man-days per 10m track run ⚠️
- [ ] L46: - **Daily rate reference**: Rp 200,000–300,000 ⚠️
- [ ] L49: - **Ramadan / holidays**: 斋月有效工时下降 20–30%，排期按 1.3 倍系数 ⚠️
- [ ] L50: - **Rainy season**: 同中国技工，空腔凝露检查 ⚠️
- [ ] L51: - **Difficulty adjustment**: 型材边缘批灰精细度不足，返工风险计 15% 余量 ⚠️；**弧形轨道禁止本级独立承担**，转 [[china-skilled-labor]]
- [ ] L61: - **单位工时**：2.2 工时/延米轨道 ⚠️（标准直线段）
- [ ] L62: - **参考工期**：10m 轨道约 2.8 工日 ⚠️
- [ ] L63: - **日薪参考**：Rp 200,000–300,000 ⚠️
- [ ] L66: - **斋月/节假日**：斋月有效工时下降 20–30%，排期按 1.3 倍系数 ⚠️
- [ ] L67: - **雨季**：空腔凝露检查 ⚠️
- [ ] L68: - **难度折算**：型材边缘批灰精细度不足，返工风险计 15% 余量 ⚠️；**弧形轨道禁止本级独立承担**，转 [[china-skilled-labor]]

### WorkHour Recessed Lighting - Local General（10 处）

- [ ] L42: - **Unit work hour**: N/A for installation — **forbidden**（毫米级容差工序）⚠️
- [ ] L43: - **Auxiliary reference**: material transport & cleanup ~0.3 man-day per 10m track run ⚠️（技工直接指挥下）
- [ ] L44: - **Daily rate reference**: Rp 120,000–180,000 ⚠️
- [ ] L47: - **Ramadan / holidays**: 斋月体力工序效率下降约 30% ⚠️
- [ ] L49: - **Difficulty adjustment**: 轨道/预埋框为精密件，搬运需防磕碰变形——变形的轨道装上去就是波浪弯 ⚠️
- [ ] L59: - **单位工时**：安装施工 **N/A——严禁普工上手** ⚠️
- [ ] L60: - **辅助参考**：材料搬运与清理约 0.3 工日/10m 轨道 ⚠️（技工直接指挥下）
- [ ] L61: - **日薪参考**：Rp 120,000–180,000 ⚠️
- [ ] L64: - **斋月/节假日**：斋月体力工序效率下降约 30% ⚠️
- [ ] L66: - **难度折算**：轨道/预埋框为精密件，搬运防磕碰变形——变形轨道装上即波浪弯 ⚠️

### WorkHour Ribbed Screed Leveling - China Skilled（12 处）

- [ ] L42: - **Unit work hour**: 0.8 man-hours/m² ⚠️（按墙面面积计）
- [ ] L43: - **Reference duration**: ~1.0 man-day per 10m² ⚠️（含冲筋条设置与刮平，不含养护等待）
- [ ] L44: - **Daily rate reference**: Rp 450,000–650,000 ⚠️
- [ ] L47: - **Ramadan / holidays**: 本人不受影响；混编班组进度受印尼工友出勤影响 ⚠️
- [ ] L48: - **Rainy season**: 高湿环境养护期延长，后续工序需顺延，不增加本工时但影响总工期 ⚠️
- [ ] L49: - **Difficulty adjustment**: 垂平度要求 ≤2mm/2m（艺术漆基层）时工时上浮 20%；原墙平整度极差（偏差 >20mm）上浮 25% ⚠️
- [ ] L59: - **单位工时**：0.8 工时/m² ⚠️（按墙面面积计）
- [ ] L60: - **参考工期**：10m² 约 1.0 工日 ⚠️（含冲筋条设置与刮平，不含养护等待）
- [ ] L61: - **日薪参考**：Rp 450,000–650,000 ⚠️
- [ ] L64: - **斋月/节假日**：本人不受影响；混编班组进度受印尼工友出勤影响 ⚠️
- [ ] L65: - **雨季**：高湿养护期延长，影响总工期但不增加本工时 ⚠️
- [ ] L66: - **难度折算**：垂平度 ≤2mm/2m（艺术漆基层）上浮 20%；原墙偏差 >20mm 上浮 25% ⚠️

### WorkHour Ribbed Screed Leveling - Indonesian Skilled（12 处）

- [ ] L42: - **Unit work hour**: 1.2 man-hours/m² ⚠️
- [ ] L43: - **Reference duration**: ~1.5 man-days per 10m² ⚠️
- [ ] L44: - **Daily rate reference**: Rp 200,000–300,000 ⚠️
- [ ] L47: - **Ramadan / holidays**: 斋月有效工时下降 20–30%，排期按 1.3 倍系数 ⚠️
- [ ] L48: - **Rainy season**: 养护期延长，影响总工期 ⚠️
- [ ] L49: - **Difficulty adjustment**: 本地技工对冲筋条工艺熟练度参差，垂平度要求 ≤3mm/2m 以上时不建议独立承担；返工风险计 15% 余量 ⚠️
- [ ] L59: - **单位工时**：1.2 工时/m² ⚠️
- [ ] L60: - **参考工期**：10m² 约 1.5 工日 ⚠️
- [ ] L61: - **日薪参考**：Rp 200,000–300,000 ⚠️
- [ ] L64: - **斋月/节假日**：斋月有效工时下降 20–30%，排期按 1.3 倍系数 ⚠️
- [ ] L65: - **雨季**：养护期延长，影响总工期 ⚠️
- [ ] L66: - **难度折算**：冲筋条工艺熟练度参差，垂平度 ≤3mm/2m 以上不建议独立承担；返工风险计 15% 余量 ⚠️

### WorkHour Ribbed Screed Leveling - Local General（10 处）

- [ ] L43: - **Unit work hour**: N/A for leveling execution — **forbidden** ⚠️
- [ ] L44: - **Auxiliary reference**: mortar mixing & supply ~0.5 man-day per 10m² ⚠️（技工直接指挥下）
- [ ] L45: - **Daily rate reference**: Rp 120,000–180,000 ⚠️
- [ ] L48: - **Ramadan / holidays**: 斋月体力工序效率下降约 30% ⚠️
- [ ] L50: - **Difficulty adjustment**: 冲筋条定位与刮平为测量/容差工序，普工全程不得上手 ⚠️
- [ ] L60: - **单位工时**：找平施工 **N/A——严禁普工上手** ⚠️
- [ ] L61: - **辅助参考**：拌浆供料约 0.5 工日/10m² ⚠️（技工直接指挥下）
- [ ] L62: - **日薪参考**：Rp 120,000–180,000 ⚠️
- [ ] L65: - **斋月/节假日**：斋月体力工序效率下降约 30% ⚠️
- [ ] L67: - **难度折算**：冲筋条定位与刮平涉及测量/容差判断，普工全程不得上手 ⚠️

### WorkHour Trimless Edge - China Skilled（12 处）

- [ ] L42: - **Unit work hour**: 0.6 man-hours per linear meter ⚠️（型材安装 + 批嵌 + 清缝；不含基层找平）
- [ ] L43: - **Reference duration**: ~1.5 man-days per 20m room perimeter ⚠️
- [ ] L44: - **Daily rate reference**: Rp 450,000–650,000 ⚠️
- [ ] L47: - **Ramadan / holidays**: 本人不受影响 ⚠️
- [ ] L48: - **Rainy season**: 高湿膨胀预留缝按上限取 5mm；不影响工时 ⚠️
- [ ] L49: - **Difficulty adjustment**: 阴阳角密集（每间房 >6 角）上浮 25%；无框门套每樘 +0.5 工日 ⚠️
- [ ] L59: - **单位工时**：0.6 工时/延米 ⚠️（型材安装 + 批嵌 + 清缝；不含基层找平）
- [ ] L60: - **参考工期**：20m 房间周长约 1.5 工日 ⚠️
- [ ] L61: - **日薪参考**：Rp 450,000–650,000 ⚠️
- [ ] L64: - **斋月/节假日**：本人不受影响 ⚠️
- [ ] L65: - **雨季**：膨胀缝按上限 5mm；不影响工时 ⚠️
- [ ] L66: - **难度折算**：阴阳角密集（>6 角/间）上浮 25%；无框门套每樘 +0.5 工日 ⚠️

### WorkHour Trimless Edge - Indonesian Skilled（12 处）

- [ ] L44: - **Unit work hour**: 0.9 man-hours per linear meter ⚠️（**仅限批嵌埋入段**；型材安装转 [[china-skilled-labor]]）
- [ ] L45: - **Reference duration**: ~2.2 man-days per 20m ⚠️
- [ ] L46: - **Daily rate reference**: Rp 200,000–300,000 ⚠️
- [ ] L49: - **Ramadan / holidays**: 斋月有效工时下降 20–30%，排期按 1.3 倍系数 ⚠️
- [ ] L50: - **Rainy season**: 无显著影响 ⚠️
- [ ] L51: - **Difficulty adjustment**: 侧光验收标准下棱线返工风险计 20% 余量 ⚠️；角部细部必须由高等级技工收
- [ ] L61: - **单位工时**：0.9 工时/延米 ⚠️（**仅限批嵌埋入段**；型材安装转 [[china-skilled-labor]]）
- [ ] L62: - **参考工期**：20m 约 2.2 工日 ⚠️
- [ ] L63: - **日薪参考**：Rp 200,000–300,000 ⚠️
- [ ] L66: - **斋月/节假日**：斋月有效工时下降 20–30%，排期按 1.3 倍系数 ⚠️
- [ ] L67: - **雨季**：无显著影响 ⚠️
- [ ] L68: - **难度折算**：侧光验收下棱线返工风险计 20% 余量 ⚠️；角部细部必须高等级技工收

### WorkHour Trimless Edge - Local General（10 处）

- [ ] L42: - **Unit work hour**: N/A for profile/finishing — **forbidden** ⚠️
- [ ] L43: - **Auxiliary reference**: protection film & cleanup ~0.2 man-day per 20m ⚠️
- [ ] L44: - **Daily rate reference**: Rp 120,000–180,000 ⚠️
- [ ] L47: - **Ramadan / holidays**: 斋月体力工序效率下降约 30% ⚠️
- [ ] L49: - **Difficulty adjustment**: 型材为精密外露件，搬运防磕碰——磕凹的型材装上去整面墙报废 ⚠️
- [ ] L59: - **单位工时**：型材/面层施工 **N/A——严禁普工上手** ⚠️
- [ ] L60: - **辅助参考**：贴保护膜与清理约 0.2 工日/20m ⚠️
- [ ] L61: - **日薪参考**：Rp 120,000–180,000 ⚠️
- [ ] L64: - **斋月/节假日**：斋月体力工序效率下降约 30% ⚠️
- [ ] L66: - **难度折算**：型材为精密外露件，搬运防磕碰——磕凹型材上墙即整面报废 ⚠️

### WorkHour Wall Paint - China Skilled（14 处）

- [ ] L42: - **Unit work hour**: 0.15 man-hours/m² ⚠️（含底漆 1 遍 + 面漆 2 遍；艺术漆肌理效果另计上浮）
- [ ] L43: - **Reference duration**: ~0.2 man-days per 10m² ⚠️
- [ ] L44: - **Daily rate reference**: Rp 450,000–650,000 ⚠️
- [ ] L47: - **Ramadan / holidays**: 本人不受影响；混编班组进度受印尼工友出勤影响 ⚠️
- [ ] L48: - **Rainy season**: 环境湿度 >80% RH 时须停工或除湿——印尼雨季涂装间隔期延长，总工期 +0.5 工日/10m² ⚠️
- [ ] L49: - **Difficulty adjustment**: 威尼斯石膏/金属漆等艺术效果上浮 50%；深色漆遮盖力差需增加一遍面漆上浮 30%；基层含水率 >8% 强制停工 ⚠️
- [ ] L52: 行业经验估算：熟练涂装工辊涂效率约 60–80 m²/工日（含底漆与两遍面漆），取中高值 67 m²/工日 ≈ 0.12 工时/m²，叠加艺术漆收边与纹理施工余量至 0.15 ⚠️（与 [[china-skilled-labor]] ...
- [ ] L59: - **单位工时**：0.15 工时/m² ⚠️（含底漆 1 遍 + 面漆 2 遍；艺术漆肌理效果另计上浮）
- [ ] L60: - **参考工期**：10m² 约 0.2 工日 ⚠️
- [ ] L61: - **日薪参考**：Rp 450,000–650,000 ⚠️
- [ ] L64: - **斋月/节假日**：本人不受影响；混编班组进度受印尼工友出勤影响 ⚠️
- [ ] L65: - **雨季**：湿度 >80% RH 须停工或除湿，涂装间隔期延长，总工期 +0.5 工日/10m² ⚠️
- [ ] L66: - **难度折算**：威尼斯石膏/金属漆等艺术效果上浮 50%；深色漆增加一遍面漆上浮 30%；基层含水率 >8% 强制停工 ⚠️
- [ ] L69: 行业经验估算：熟练涂装工辊涂效率约 60–80 m²/工日（含底漆与两遍面漆），取中高值 67 m²/工日 ≈ 0.12 工时/m²，叠加艺术漆收边与纹理施工余量至 0.15 ⚠️（与 [[china-skilled-labor]] ...

### WorkHour Wall Paint - Indonesian Skilled（14 处）

- [ ] L42: - **Unit work hour**: 0.28 man-hours/m² ⚠️（含底漆 1 遍 + 面漆 2 遍；仅限常规平涂效果）
- [ ] L43: - **Reference duration**: ~0.35 man-days per 10m² ⚠️
- [ ] L44: - **Daily rate reference**: Rp 200,000–300,000 ⚠️
- [ ] L47: - **Ramadan / holidays**: 斋月有效工时下降 20–30%，排期按 1.3 倍系数 ⚠️
- [ ] L48: - **Rainy season**: 湿度 >80% RH 须停工或除湿，涂装间隔期延长，总工期 +0.5 工日/10m² ⚠️
- [ ] L49: - **Difficulty adjustment**: 艺术漆肌理/威尼斯石膏效果**不推荐**本级施工（纹理手感依赖长期训练），如坚持派本级需上浮 50% 并接受效果折扣 ⚠️
- [ ] L52: 行业经验估算：印尼本地涂装工常规效率约 30–40 m²/工日（含底漆与两遍面漆），取中值 35 m²/工日 ≈ 0.23 工时/m²，叠加高端涂装基层检查与收边余量至 0.28 ⚠️（与 [[indonesian-skilled-l...
- [ ] L59: - **单位工时**：0.28 工时/m² ⚠️（含底漆 1 遍 + 面漆 2 遍；仅限常规平涂效果）
- [ ] L60: - **参考工期**：10m² 约 0.35 工日 ⚠️
- [ ] L61: - **日薪参考**：Rp 200,000–300,000 ⚠️
- [ ] L64: - **斋月/节假日**：斋月有效工时下降 20–30%，排期按 1.3 倍系数 ⚠️
- [ ] L65: - **雨季**：湿度 >80% RH 须停工或除湿，涂装间隔期延长，总工期 +0.5 工日/10m² ⚠️
- [ ] L66: - **难度折算**：艺术漆肌理/威尼斯石膏效果**不推荐**本级施工，坚持派本级需上浮 50% 并接受效果折扣 ⚠️
- [ ] L69: 行业经验估算：印尼本地涂装工常规效率约 30–40 m²/工日（含底漆与两遍面漆），取中值 35 m²/工日 ≈ 0.23 工时/m²，叠加高端涂装基层检查与收边余量至 0.28 ⚠️（与 [[indonesian-skilled-l...

### WorkHour Wall Paint - Local General（12 处）

- [ ] L43: - **Unit work hour**: Painting application **N/A — forbidden for general labor** ⚠️
- [ ] L44: - **Auxiliary reference**: masking & sanding assistance ~0.3 man-day per 10m² ⚠️（技工直接指挥下）
- [ ] L45: - **Daily rate reference**: Rp 120,000–180,000 ⚠️
- [ ] L48: - **Ramadan / holidays**: 斋月体力工序效率下降约 30%，宜安排上午作业 ⚠️
- [ ] L49: - **Rainy season**: 无显著影响（室内工序），但打磨粉尘在潮湿环境沉降慢，需加强通风 ⚠️
- [ ] L50: - **Difficulty adjustment**: 遮蔽不到位是高端涂装污染成品的高发诱因——遮蔽标准由技检验收后方可开涂 ⚠️
- [ ] L60: - **单位工时**：涂装施工 **N/A——严禁普工上手** ⚠️
- [ ] L61: - **辅助参考**：遮蔽保护+打磨辅助约 0.3 工日/10m² ⚠️（技工直接指挥下）
- [ ] L62: - **日薪参考**：Rp 120,000–180,000 ⚠️
- [ ] L65: - **斋月/节假日**：斋月体力工序效率下降约 30%，宜安排上午作业 ⚠️
- [ ] L66: - **雨季**：无显著影响（室内工序），打磨粉尘在潮湿环境沉降慢，需加强通风 ⚠️
- [ ] L67: - **难度折算**：遮蔽不到位是高端涂装污染成品的高发诱因——遮蔽标准由技检验收后方可开涂 ⚠️

### WorkHour Wet Method Tiling - China Skilled（12 处）

- [ ] L42: - **Unit work hour**: 1.2 man-hours/m² ⚠️（大板场景，含调平器系统与养护）
- [ ] L43: - **Reference duration**: ~1.5 man-days per 10m² ⚠️
- [ ] L44: - **Daily rate reference**: Rp 450,000–650,000 ⚠️
- [ ] L47: - **Ramadan / holidays**: 本人不受影响；混编班组进度受印尼工友出勤影响 ⚠️
- [ ] L48: - **Rainy season**: 基层含水率高需延长晾置，养护期除湿，总工期可能 +0.5 工日/10m² ⚠️
- [ ] L49: - **Difficulty adjustment**: 岩板（烧结石材）或大规格薄板需两人抬铺，工时上浮 30%；斜铺/拼花上浮 40% ⚠️
- [ ] L59: - **单位工时**：1.2 工时/m² ⚠️（大板场景，含调平器系统与养护）
- [ ] L60: - **参考工期**：10m² 约 1.5 工日 ⚠️
- [ ] L61: - **日薪参考**：Rp 450,000–650,000 ⚠️
- [ ] L64: - **斋月/节假日**：本人不受影响；混编班组进度受印尼工友出勤影响 ⚠️
- [ ] L65: - **雨季**：基层晾置与养护除湿，总工期可能 +0.5 工日/10m² ⚠️
- [ ] L66: - **难度折算**：岩板/大规格薄板两人抬铺上浮 30%；斜铺/拼花上浮 40% ⚠️

### WorkHour Wet Method Tiling - Indonesian Skilled（12 处）

- [ ] L42: - **Unit work hour**: 0.8 man-hours/m² ⚠️（常规规格 ≤800×800mm）
- [ ] L43: - **Reference duration**: ~1.0 man-day per 10m² ⚠️
- [ ] L44: - **Daily rate reference**: Rp 200,000–300,000 ⚠️
- [ ] L47: - **Ramadan / holidays**: 斋月有效工时下降 20–30%，排期按 1.3 倍系数 ⚠️
- [ ] L48: - **Rainy season**: 基层含水率控制同中国技工，总工期 +0.5 工日/10m² ⚠️
- [ ] L49: - **Difficulty adjustment**: 强制使用调平器可压缩空鼓返工；未用调平器的班组返工风险计 15% 余量 ⚠️；**≥1.2m 大板禁止派本级**
- [ ] L59: - **单位工时**：0.8 工时/m² ⚠️（常规规格 ≤800×800mm）
- [ ] L60: - **参考工期**：10m² 约 1.0 工日 ⚠️
- [ ] L61: - **日薪参考**：Rp 200,000–300,000 ⚠️
- [ ] L64: - **斋月/节假日**：斋月有效工时下降 20–30%，排期按 1.3 倍系数 ⚠️
- [ ] L65: - **雨季**：基层含水率控制，总工期 +0.5 工日/10m² ⚠️
- [ ] L66: - **难度折算**：强制调平器可压缩空鼓返工；未用调平器返工风险计 15% 余量 ⚠️；**≥1.2m 大板禁止派本级**

### WorkHour Wet Method Tiling - Local General（10 处）

- [ ] L43: - **Unit work hour**: N/A for tile laying — **forbidden** ⚠️
- [ ] L44: - **Auxiliary reference**: mortar mixing & tile transport ~0.6 man-day per 10m² ⚠️（技工直接指挥下）
- [ ] L45: - **Daily rate reference**: Rp 120,000–180,000 ⚠️
- [ ] L48: - **Ramadan / holidays**: 斋月体力工序效率下降约 30%，宜安排上午作业 ⚠️
- [ ] L50: - **Difficulty adjustment**: 拌浆水灰比由技工定量，普工不得自行加水——这是空鼓的高发诱因 ⚠️
- [ ] L60: - **单位工时**：铺贴施工 **N/A——严禁普工上手** ⚠️
- [ ] L61: - **辅助参考**：拌浆搬砖约 0.6 工日/10m² ⚠️（技工直接指挥下）
- [ ] L62: - **日薪参考**：Rp 120,000–180,000 ⚠️
- [ ] L65: - **斋月/节假日**：斋月体力工序效率下降约 30%，宜安排上午作业 ⚠️
- [ ] L67: - **难度折算**：拌浆水灰比由技工定量，普工不得自行加水——空鼓高发诱因 ⚠️

### WorkHour Wood SPC Flooring - China Skilled（12 处）

- [ ] L42: - **Unit work hour**: 0.5 man-hours/m²（直拼）⚠️；0.9 man-hours/m²（人字拼/鱼骨拼）⚠️
- [ ] L43: - **Reference duration**: 直拼 ~0.6 man-day per 10m² ⚠️；人字拼 ~1.1 man-days per 10m² ⚠️
- [ ] L44: - **Daily rate reference**: Rp 450,000–650,000 ⚠️
- [ ] L47: - **Ramadan / holidays**: 本人不受影响 ⚠️
- [ ] L48: - **Rainy season**: 基层含水率等待与材料现场适应（48-72h）不计入工时，但影响总工期 ⚠️
- [ ] L49: - **Difficulty adjustment**: 人字拼 45° 收边复杂户型上浮 25%；楼梯踏步另计 ⚠️
- [ ] L59: - **单位工时**：0.5 工时/m²（直拼）⚠️；0.9 工时/m²（人字拼/鱼骨拼）⚠️
- [ ] L60: - **参考工期**：直拼 10m² 约 0.6 工日 ⚠️；人字拼 10m² 约 1.1 工日 ⚠️
- [ ] L61: - **日薪参考**：Rp 450,000–650,000 ⚠️
- [ ] L64: - **斋月/节假日**：本人不受影响 ⚠️
- [ ] L65: - **雨季**：含水率等待与材料适应期（48-72h）不计工时但影响总工期 ⚠️
- [ ] L66: - **难度折算**：人字拼复杂收边上浮 25%；楼梯踏步另计 ⚠️

### WorkHour Wood SPC Flooring - Indonesian Skilled（12 处）

- [ ] L42: - **Unit work hour**: 0.4 man-hours/m²（直拼，含防潮层与地垫）⚠️
- [ ] L43: - **Reference duration**: ~0.5 man-day per 10m² ⚠️
- [ ] L44: - **Daily rate reference**: Rp 200,000–300,000 ⚠️
- [ ] L47: - **Ramadan / holidays**: 斋月有效工时下降 20–30%，排期按 1.3 倍系数 ⚠️
- [ ] L48: - **Rainy season**: 同中国技工，等待期影响总工期 ⚠️
- [ ] L49: - **Difficulty adjustment**: 伸缩缝省略是本级最常见的偷工点——验收必须卡尺检查 ⚠️；人字拼禁止本级独立承担，转 [[china-skilled-labor]]
- [ ] L59: - **单位工时**：0.4 工时/m²（直拼，含防潮层与地垫）⚠️
- [ ] L60: - **参考工期**：10m² 约 0.5 工日 ⚠️
- [ ] L61: - **日薪参考**：Rp 200,000–300,000 ⚠️
- [ ] L64: - **斋月/节假日**：斋月有效工时下降 20–30%，排期按 1.3 倍系数 ⚠️
- [ ] L65: - **雨季**：等待期影响总工期 ⚠️
- [ ] L66: - **难度折算**：伸缩缝省略是本级最常见偷工点——验收卡尺检查 ⚠️；人字拼禁止本级，转 [[china-skilled-labor]]

### WorkHour Wood SPC Flooring - Local General（12 处）

- [ ] L42: - **Unit work hour**: N/A for laying — **forbidden** ⚠️
- [ ] L43: - **Auxiliary reference**: unpacking & plank transport ~0.2 man-day per 10m² ⚠️
- [ ] L44: - **Daily rate reference**: Rp 120,000–180,000 ⚠️
- [ ] L47: - **Ramadan / holidays**: 斋月体力工序效率下降约 30% ⚠️
- [ ] L48: - **Rainy season**: 材料搬运需注意防淋雨（从货车到室内段）⚠️
- [ ] L49: - **Difficulty adjustment**: 板材锁扣边脆，搬运防摔——锁扣摔损的板铺上去就是日后开缝源 ⚠️
- [ ] L59: - **单位工时**：铺设施工 **N/A——严禁普工上手** ⚠️
- [ ] L60: - **辅助参考**：拆包与板材搬运约 0.2 工日/10m² ⚠️
- [ ] L61: - **日薪参考**：Rp 120,000–180,000 ⚠️
- [ ] L64: - **斋月/节假日**：斋月体力工序效率下降约 30% ⚠️
- [ ] L65: - **雨季**：货车到室内段搬运防淋雨 ⚠️
- [ ] L66: - **难度折算**：锁扣边脆，搬运防摔——锁扣摔损的板即日后开缝源 ⚠️


## 第四批 · 工艺标准与容差（🟢 多为施工标准，扫读即可）（218 处）

### Custom Built-in Wardrobe -Millwork Installation 定制集成（6 处）

- [ ] L74: | **Panel Moisture Content (Pre-install)** | **≤ 12%** ⚠️ | Acclimatize on-site for 7 days |
- [ ] L78: | **Shelf Deflection Limit** | ≤ 1.5mm per 300mm span ⚠️ | Under full load (20kg) |
- [ ] L79: | **Door Gap Tolerance** | 2–3mm uniform gap ⚠️ | Prevents binding due to humidity swelling |
- [ ] L171: | **板材含水率（安装前）** | **≤ 12%** ⚠️ | 现场适应7天 |
- [ ] L175: | **层板挠度限值** | 每300mm跨度≤1.5mm ⚠️ | 满载（20kg）条件下 |
- [ ] L176: | **门板间隙公差** | 2–3mm均匀缝隙 ⚠️ | 防止高湿膨胀后卡滞 |

### Electrical Switch & Socket -Low-Voltage Panel Installation（4 处）

- [ ] L82: |**Wire Stripping Length**|8–10mm (screw terminals) / 10–12mm (push-in) ⚠️|Based on terminal spec|
- [ ] L83: |**Torque for Screw Terminals**|0.4–0.8 Nm (depending on wire gauge) ⚠️|Use calibrated screwdriver|
- [ ] L240: |**导线剥线长度**|8–10mm（螺丝端子）/ 10–12mm（快接式）⚠️|依端子规格|
- [ ] L241: |**螺丝端子扭矩**|0.4–0.8 Nm（依线径）⚠️|使用校准螺丝刀|

### Floating - Suspended Ceiling 轻钢龙骨悬浮吊顶（12 处）

- [ ] L64: | **Main Keel Spacing** | ≤ 1200mm ⚠️ | Load-bearing standard |
- [ ] L65: | **Secondary Keel Spacing** | **≤ 400mm** ⚠️ | Prevents gypsum board sagging in high humidity |
- [ ] L67: | **Screw Spacing (Periphery)** | ≤ 150mm ⚠️ | Critical for edge anchoring |
- [ ] L68: | **Screw Spacing (Internal)** | ≤ 200mm ⚠️ | — |
- [ ] L70: | **Seismic Joint Width** | 5–8mm (at corners & intervals >12m) ⚠️ | Filled with flexible sealant |
- [ ] L112: | **Structural Safety** | Hanger rod pull-out strength ≥ 1.5kN ⚠️ | Random tensile pull-test |
- [ ] L135: | **主龙骨间距** | ≤ 1200mm ⚠️ | 承载标准 |
- [ ] L136: | **副龙骨间距** | **≤ 400mm** ⚠️ | 防止高湿下石膏板下挠 |
- [ ] L138: | **螺丝边距** | ≤ 150mm ⚠️ | 边缘锚固关键 |
- [ ] L139: | **螺丝中距** | ≤ 200mm ⚠️ | — |
- [ ] L141: | **抗震缝宽度** | 5–8mm（转角及长度>12m处）⚠️ | 柔性密封胶填充 |
- [ ] L183: | **结构安全性** | 吊杆抗拔承载力≥1.5kN ⚠️ | 随机拉拔测试 |

### Large-Format Slab -Sintered Stone Installation铺贴工艺（12 处）

- [ ] L75: | **Total Installation Height** | 20–40mm ⚠️ | Leveling bed + adhesive layer |
- [ ] L76: | **Flatness Tolerance** | **≤ 1mm / 2m** ⚠️ | Twice as strict as standard tiles |
- [ ] L77: | **Hollow Ratio** | **0% (Strictly Forbidden)** ⚠️ | Full-contact bedding required |
- [ ] L78: | **Adhesive Open Time** | ≤ 20 mins (at 30°C) ⚠️ | Indonesia's heat shortens working time |
- [ ] L79: | **Joint Width** | 1.5–3.0mm ⚠️ | Allows for seismic movement |
- [ ] L106: - *Acceptance*: Flatness ≤ 1mm/2m; adjacent slab lippage ≤ 0.3mm ⚠️; clips fully engaged.
- [ ] L157: | **安装总厚度** | 20–40mm ⚠️ | 找平层+粘结层 |
- [ ] L158: | **平整度公差** | **≤ 1mm / 2m** ⚠️ | 为普通砖标准的2倍 |
- [ ] L159: | **空鼓率** | **0%（绝对禁止）** ⚠️ | 必须满粘 |
- [ ] L160: | **胶粘剂开放时间** | ≤ 20 分钟（30°C环境）⚠️ | 印尼高温缩短可操作时间 |
- [ ] L161: | **留缝宽度** | 1.5–3.0mm ⚠️ | 为抗震预留变形空间 |
- [ ] L188: - *验收*：平整度≤1mm/2m；相邻板高低差≤0.3mm ⚠️；卡扣到位。

### Metal Baseboard Installation金属踢脚线安装工艺（2 处）

- [ ] L64: |**Material Thickness**|1.2–2.0mm ⚠️|—|
- [ ] L139: |**材料厚度**|1.2–2.0mm ⚠️|—|

### Microcement Wall Finishing微水泥墙面工艺（12 处）

- [ ] L66: | **Total Finished Thickness** | 2.0–3.5mm ⚠️ | Depending on substrate flatness |
- [ ] L67: | **Substrate Flatness (Pre-work)** | ≤ 1.5mm / 2m ⚠️ | Must be smoother than tile substrate |
- [ ] L68: | **Crack-Bridging Mesh** | **Mandatory** for all walls (≥ 160g/m²) ⚠️ | Anti-seismic / anti-shrinkage |
- [ ] L69: | **Ambient Temp. for Curing** | 15–30°C ⚠️ | Avoid direct sunlight and rain |
- [ ] L70: | **Relative Humidity (RH)** | **≤ 75%** during application ⚠️ | Critical for Indonesia's rainy season |
- [ ] L108: | **Adhesion Strength** | ≥ 1.0 MPa ⚠️ | Cross-cut tape test (ISO 2409) |
- [ ] L131: | **总完成厚度** | 2.0–3.5mm ⚠️ | 依基层平整度调整 |
- [ ] L132: | **施工前基层平整度** | ≤ 1.5mm / 2m ⚠️ | 须比铺砖基层更平 |
- [ ] L133: | **抗裂网格布** | **强制使用**（≥160g/m²）⚠️ | 抗震/抗收缩 |
- [ ] L134: | **养护环境温度** | 15–30°C ⚠️ | 避免阳光直射和雨水 |
- [ ] L135: | **施工相对湿度（RH）** | **≤ 75%** ⚠️ | 对印尼雨季至关重要 |
- [ ] L173: | **附着强度** | ≥1.0 MPa ⚠️ | 划格法（ISO 2409） |

### Minimalist Trimless Edge极简收口（28 处）

- [ ] L68: - **Shadow gap width**: 10–15mm, deviation ≤ 0.5mm over full run ⚠️
- [ ] L69: - **Substrate verticality**: ≤ 2mm per 2m (mandatory, via [[ribbed-screed-gauging-strips]]) ⚠️
- [ ] L70: - **Profile embed depth**: flush ±0.5mm with finished wall plane ⚠️
- [ ] L71: - **Floor junction clearance**: 3–5mm (Indonesia humidity expansion) ⚠️
- [ ] L81: - *Acceptance*: Line deviation ≤ 0.5mm over full perimeter ⚠️.
- [ ] L85: - *Acceptance*: Profile flush ±0.5mm; fixing spacing ≤ 400mm ⚠️.
- [ ] L106: | Gap width uniformity | 10–15mm, ±0.5mm ⚠️ | Caliper at 1m intervals |
- [ ] L107: | Profile flush | ±0.5mm to wall plane ⚠️ | Straightedge + feeler |
- [ ] L108: | Substrate verticality | ≤ 2mm/2m ⚠️ | Pre-gate, Step 1 |
- [ ] L109: | Edge cracking | Zero cracks at profile junction after 28d ⚠️ | Raking light |
- [ ] L119: | Profile dented | Site traffic after install | Protection film until handover ⚠️ |
- [ ] L120: | Humidity swelling | Gap < 3mm in wet season | 3–5mm clearance, flexible sealant at wet zones ⚠️ |
- [ ] L127: - **Materials**: recessed aluminum shadow-gap profile (Atelier SKU 缺口 ⚠️), corner profiles.
- [ ] L137: - **阴影缝宽度**：10–15mm，全程偏差 ≤0.5mm ⚠️
- [ ] L138: - **基层垂平度**：≤2mm/2m（强制，经 [[ribbed-screed-gauging-strips|冲筋找平]]）⚠️
- [ ] L139: - **型材嵌入齐平**：与完成墙面 ±0.5mm ⚠️
- [ ] L140: - **地面交接预留**：3–5mm（印尼高湿膨胀）⚠️
- [ ] L150: - *验收*：全线偏差 ≤0.5mm ⚠️。
- [ ] L154: - *验收*：齐平 ±0.5mm；固定间距 ≤400mm ⚠️。
- [ ] L175: | 缝宽均匀度 | 10–15mm，±0.5mm ⚠️ | 每 1m 卡尺测 |
- [ ] L176: | 型材齐平 | ±0.5mm ⚠️ | 靠尺+塞尺 |
- [ ] L177: | 基层垂平 | ≤2mm/2m ⚠️ | Step 1 生死门 |
- [ ] L178: | 边缘开裂 | 28 天后零裂缝 ⚠️ | 侧光检查 |
- [ ] L188: | 型材磕凹 | 安装后现场通行 | 保护贴膜至交付 ⚠️ |
- [ ] L189: | 高湿膨胀卡死 | 雨季缝 <3mm | 3–5mm 预留，湿区柔性密封 ⚠️ |
- [ ] L196: - **材料**：内嵌铝合金阴影缝型材（Atelier SKU 缺口 ⚠️）、角型材。
- [ ] L229: │   ├── 缝宽 ±0.5mm ⚠️ → [[quality-control]]
- [ ] L245: └── 高湿膨胀 → 3-5mm 预留 ⚠️

### Natural Stone Flooring Installation 天然石材地面安装（8 处）

- [ ] L63: | **Stone Moisture Content (Pre-install)** | **≤ 3%** ⚠️ | Store in ventilated area for 7 days before use |
- [ ] L65: | **Substrate Moisture** | **< 6%** (stricter than tiles) ⚠️ | High moisture = efflorescence risk |
- [ ] L68: | **Epoxy Pot Life** | ≤ 30 minutes (at 30°C) ⚠️ | Small-batch mixing required |
- [ ] L69: | **Joint Width** | 2–3mm (floor) / 3–5mm (commercial) ⚠️ | Allows for thermal/seismic expansion |
- [ ] L133: | **石材含水率（铺贴前）** | **≤ 3%** ⚠️ | 到场后通风放置7天平衡 |
- [ ] L135: | **基层含水率** | **< 6%**（严于瓷砖）⚠️ | 含水率=泛碱风险指标 |
- [ ] L138: | **环氧可操作时间** | ≤ 30分钟（30°C环境）⚠️ | 必须小批量拌合 |
- [ ] L139: | **留缝宽度** | 2–3mm（地面）/ 3–5mm（商业）⚠️ | 预留热胀/地震伸缩 |

### Premium Wall Paint -Art Paint Finish（14 处）

- [ ] L67: | **Substrate Moisture Content** | **< 8%** (mandatory test) ⚠️ | Higher = efflorescence risk |
- [ ] L68: | **Substrate pH Value** | **< 10** (neutralized) ⚠️ | High alkalinity causes yellowing |
- [ ] L69: | **Substrate Flatness (Pre-paint)** | **≤ 1mm / 2m** ⚠️ | Prepared by [[ribbed-screed-gauging-strips]] + fine putty |
- [ ] L70: | **Ambient Temperature** | 15–30°C ⚠️ | — |
- [ ] L71: | **Relative Humidity (RH)** | **≤ 80%** (ideal <75%) ⚠️ | High RH causes bubbling & mold |
- [ ] L75: | **Recoat Interval** | 4–6 hours (at 30°C, 70% RH) ⚠️ | — |
- [ ] L76: | **Full Cure Before Use** | 7 days (for chemical curing) ⚠️ | — |
- [ ] L145: | **基层含水率** | **< 8%**（强制检测）⚠️ | 超标=泛碱风险 |
- [ ] L146: | **基层pH值** | **< 10**（中和处理）⚠️ | 高碱导致黄变 |
- [ ] L147: | **基层平整度（涂装前）** | **≤ 1mm / 2m** ⚠️ | 由冲筋找平+细面墙泥实现 |
- [ ] L148: | **环境温度** | 15–30°C ⚠️ | — |
- [ ] L149: | **相对湿度（RH）** | **≤ 80%**（理想<75%）⚠️ | 高湿导致起泡和霉变 |
- [ ] L153: | **重涂间隔** | 4–6小时（30°C，70% RH）⚠️ | — |
- [ ] L154: | **使用前完全固化** | 7天（化学固化）⚠️ | — |

### Recessed Lighting Pre-Embedding无主灯预埋（35 处）

- [ ] L69: - **Track straightness**: ≤ 2mm deviation per 3m run ⚠️
- [ ] L70: - **Track flush tolerance**: rail face flush with finished ceiling plane, ±0.5mm ⚠️
- [ ] L71: - **Downlight spacing**: 800–1200mm typical, per lighting design ⚠️
- [ ] L72: - **Clearance above rail**: ≥ 50mm for heat dissipation ⚠️
- [ ] L80: Run conduits and pull wires to each track feed point and downlight loop; leave 300mm service loops ⚠️.
- [ ] L90: - *Acceptance*: Straightness ≤ 2mm/3m ⚠️; hanger spacing ≤ 600mm ⚠️.
- [ ] L94: - *Acceptance*: Plane error ≤ 0.5mm ⚠️.
- [ ] L98: - *Acceptance*: Board edge gap to profile ≤ 2mm, uniform ⚠️.
- [ ] L106: - *Acceptance*: All circuits energized; dimming smooth; no flicker ⚠️.
- [ ] L111: | Track straightness | ≤ 2mm per 3m ⚠️ | Laser line check |
- [ ] L112: | Profile flush | ±0.5mm to ceiling plane ⚠️ | Feeler + straightedge |
- [ ] L113: | Edge cracking | Zero cracks at profile edges after 28 days ⚠️ | Raking light inspection |
- [ ] L114: | Opening precision | Board-to-profile gap ≤ 2mm uniform ⚠️ | Visual + caliper |
- [ ] L123: | Dead spots after closing | Wiring loop too short / buried junction | 300mm service loops; junction map photographed...
- [ ] L125: | Rainy-season condensation in rails | Humid ceiling void | Ventilate void; check before fit-off ⚠️ |
- [ ] L131: - **Materials**: magnetic track rail (Atelier `LIGHT-TRACK-101` Rp 350,000/m ⚠️), trimless frames, premium downlights...
- [ ] L142: - **轨道顺直度**：3m 内偏差 ≤ 2mm ⚠️
- [ ] L143: - **轨道齐平度**：轨道面与完成吊顶面齐平，±0.5mm ⚠️
- [ ] L144: - **射灯间距**：常规 800–1200mm，按灯光设计 ⚠️
- [ ] L145: - **轨道上方净空**：≥ 50mm（散热）⚠️
- [ ] L153: 布管穿线至各轨道供电点与筒灯回路，预留 300mm 检修线余量 ⚠️。
- [ ] L163: - *验收*：顺直度 ≤2mm/3m ⚠️；吊件间距 ≤600mm ⚠️。
- [ ] L167: - *验收*：平面误差 ≤0.5mm ⚠️。
- [ ] L171: - *验收*：板边与型材缝隙 ≤2mm 且均匀 ⚠️。
- [ ] L179: - *验收*：全部回路通电；调光顺滑无频闪 ⚠️。
- [ ] L184: | 轨道顺直度 | ≤2mm/3m ⚠️ | 激光线检查 |
- [ ] L185: | 型材齐平 | ±0.5mm ⚠️ | 塞尺+靠尺 |
- [ ] L186: | 边缘开裂 | 28 天后型材边缘零裂缝 ⚠️ | 侧光检查 |
- [ ] L187: | 开口精度 | 板与型材缝 ≤2mm 均匀 ⚠️ | 目测+卡尺 |
- [ ] L196: | 封板后死灯 | 线余量不足/接头被埋 | 留 300mm 余量；封板前拍照留底 ⚠️ |
- [ ] L198: | 雨季轨道内凝露 | 吊顶空腔潮湿 | 空腔通风；安装灯具前检查 ⚠️ |
- [ ] L204: - **材料**：磁吸轨道（Atelier `LIGHT-TRACK-101` Rp 350,000/m ⚠️）、无边框预埋框、防眩筒灯（`LIGHT-DOWNLIGHT-101` Rp 137,000/个 ⚠️）。
- [ ] L239: │   ├── 顺直度 ≤2mm/3m ⚠️ → [[quality-control]]
- [ ] L240: │   └── 齐平度 ±0.5mm ⚠️ → [[premium-wall-paint-art-finish]]
- [ ] L256: └── 雨季空腔凝露 → 装灯前检查 ⚠️

### Ribbed Screed -Gauging Strips Leveling 冲筋找平（10 处）

- [ ] L60: | **Rib (Gauging Strip) Spacing** | **≤ 1.2m** (vertical) ⚠️ | Ensures straightedge rigidity without bowing |
- [ ] L61: | **Rib Cross-Section** | 30–50mm wide × 10–25mm thick ⚠️ | Thickness = maximum substrate deviation + 5mm minimum |
- [ ] L62: | **Final Plane Flatness** | **≤ 2mm / 2m** ⚠️ | Critical baseline for large slabs/microcement |
- [ ] L63: | **Final Plane Verticality** | **≤ 2mm / 2m** ⚠️ | For vertical wall applications |
- [ ] L65: | **Open Working Time** | ≥ 45 minutes (at 32°C) ⚠️ | Without retarder, sets in < 20 mins |
- [ ] L131: | **筋条（冲筋）间距** | **≤ 1.2m** ⚠️ | 保证2m刮杠刚性不挠曲 |
- [ ] L132: | **筋条截面尺寸** | 30–50mm宽 × 10–25mm厚 ⚠️ | 厚度=基层最大偏差+5mm余量 |
- [ ] L133: | **完成面平整度** | **≤ 2mm / 2m** ⚠️ | 大板/微水泥硬性门槛 |
- [ ] L134: | **完成面垂直度（墙面）** | **≤ 2mm / 2m** ⚠️ | — |
- [ ] L136: | **可操作时间** | ≥ 45分钟（32°C环境）⚠️ | 无缓凝剂时<20分钟即凝结 |

### Sanitary Ware Installation卫浴洁具安装工艺（4 处）

- [ ] L75: |**Basin Mounting Height**|800–850mm (finished floor to basin rim) ⚠️|User comfort standard|
- [ ] L76: |**Faucet Flow Rate**|≤ 9 L/min (Indonesia water pressure: 1–3 bar) ⚠️|—|
- [ ] L203: |**洗手盆安装高度**|800–850mm（完成面至盆沿）⚠️|人体工学标准|
- [ ] L204: |**龙头流量**|≤ 9 L/min（印尼水压：1–3 bar）⚠️|—|

### Wallpaper - Fabric Wallcovering Installation铺贴工艺（12 处）

- [ ] L60: | **Substrate Flatness (Pre-work)** | **≤ 1.5mm / 2m** ⚠️ | Any deviation >1.5mm will show through |
- [ ] L61: | **Substrate Moisture Content** | **< 8%** (mandatory test) ⚠️ | Critical for Indonesia's humid climate |
- [ ] L62: | **Ambient Temperature** | 15–30°C ⚠️ | — |
- [ ] L63: | **Relative Humidity (RH)** | **≤ 75%** during application ⚠️ | Use dehumidifier if exceeding |
- [ ] L64: | **Adhesive Open Time** | 5–10 minutes (at 30°C) ⚠️ | Indonesia's heat shortens working window |
- [ ] L66: | **Drying Time Before Trimming** | 24–48 hours ⚠️ | Prevents shrinkage gaps |
- [ ] L125: | **施工前基层平整度** | **≤ 1.5mm / 2m** ⚠️ | 偏差>1.5mm会透出 |
- [ ] L126: | **基层含水率** | **< 8%（强制检测）** ⚠️ | 印尼高湿气候关键指标 |
- [ ] L127: | **环境温度** | 15–30°C ⚠️ | — |
- [ ] L128: | **施工相对湿度（RH）** | **≤ 75%** ⚠️ | 超标须使用除湿机 |
- [ ] L129: | **胶粘剂开放时间** | 5–10分钟（30°C环境）⚠️ | 高温缩短可操作窗口 |
- [ ] L131: | **裁切前干燥时间** | 24–48小时 ⚠️ | 防止收缩产生缝隙 |

### Wet Method Tiling湿铺法地砖铺贴（18 处）

- [ ] L64: - **Thickness**: 30–50mm ⚠️
- [ ] L65: - **Flatness Tolerance**: < 3mm per 2m straightedge ⚠️
- [ ] L66: - **Hollow Ratio Standard**: < 3% per tile (main corridors must have zero hollow spots) ⚠️
- [ ] L75: - *Acceptance*: Flatness tolerance ≤ 3mm per 2m ⚠️.
- [ ] L83: - *Acceptance*: All corners flush; adjacent tile height difference ≤ 0.5mm ⚠️.
- [ ] L95: - *Acceptance*: Joint width uniform (1.5–2.5mm) ⚠️; sealant color matched to tile.
- [ ] L99: | Hollow Ratio | Corner hollow < 3% per tile; **zero hollow** on main walkways ⚠️ | Tapping sound test |
- [ ] L100: | Flatness | Gap ≤ 1mm under 2m straightedge ⚠️ | — |
- [ ] L102: | Joint Width | Uniform 1.5–2.5mm ⚠️ | Visual + caliper |
- [ ] L122: - **铺贴厚度**：30–50mm ⚠️
- [ ] L123: - **平整度公差**：2m 靠尺检查，误差 < 3mm ⚠️
- [ ] L124: - **空鼓率标准**：单块砖边角空鼓 < 3%，主要通道严禁空鼓 ⚠️
- [ ] L133: - *验收*：平整度误差 < 3mm/2m ⚠️。
- [ ] L141: - *验收*：四角平整，相邻砖高差 < 0.5mm ⚠️。
- [ ] L153: - *验收*：缝宽 1.5–2.5mm 均匀 ⚠️，美缝颜色与砖色协调。
- [ ] L157: | 空鼓率 | 单块砖边角空鼓 < 3%，主要通道**严禁空鼓** ⚠️ | 敲击听音法 |
- [ ] L158: | 平整度 | 2m 靠尺检查，缝隙 < 1mm ⚠️ | — |
- [ ] L160: | 缝宽 | 1.5–2.5mm 均匀一致 ⚠️ | 目测 + 卡尺 |

### Wood & SPC Flooring Installation木地板SPC铺设（31 处）

- [ ] L68: - **Substrate flatness**: ≤ 3mm per 2m ⚠️
- [ ] L69: - **Substrate moisture**: ≤ 12% CM reading before laying ⚠️
- [ ] L70: - **Expansion gap**: 8–10mm at all walls and fixed elements ⚠️
- [ ] L71: - **Acclimatization**: 48–72 hours on site before laying ⚠️
- [ ] L87: Plan plank direction (along main light/long axis), stagger pattern ≥300mm, first/last row width ≥ 50mm ⚠️.
- [ ] L97: - *Acceptance*: Joints closed, no lifted edges; drift ≤ 2mm per 5m ⚠️.
- [ ] L110: | Substrate flatness | ≤ 3mm/2m ⚠️ | Pre-gate |
- [ ] L111: | Expansion gap | 8–10mm continuous ⚠️ | Spacer check before trims |
- [ ] L113: | Walk test | Silent, no vertical movement ⚠️ | Full-area walk |
- [ ] L114: | Pattern drift | ≤ 2mm per 5m ⚠️ | Straightedge |
- [ ] L119: | Buckling (起拱) | Expansion gap too small / wet season swelling | 8-10mm gaps mandatory; rainy season use upper bound...
- [ ] L122: | Swollen edges | Water mopping / no moisture barrier | PE barrier mandatory; damp-mop only ⚠️ |
- [ ] L124: | Fading near windows | UV exposure (SPC) | Curtains/film in sun-exposed zones ⚠️ |
- [ ] L141: - **基层平整度**：≤3mm/2m ⚠️
- [ ] L142: - **基层含水率**：铺设前 ≤12%（CM 仪）⚠️
- [ ] L143: - **伸缩缝**：周边及固定构件处 8–10mm ⚠️
- [ ] L144: - **现场适应**：铺设前 48–72 小时 ⚠️
- [ ] L160: 板向顺主光源/长轴；错缝 ≥300mm；首末排板宽 ≥50mm ⚠️。
- [ ] L170: - *验收*：缝闭合无翘边；跑偏 ≤2mm/5m ⚠️。
- [ ] L183: | 基层平整度 | ≤3mm/2m ⚠️ | 前置门 |
- [ ] L184: | 伸缩缝 | 8–10mm 连续 ⚠️ | 收边前卡尺检查 |
- [ ] L186: | 行走测试 | 无声、无上下浮动 ⚠️ | 全区行走 |
- [ ] L187: | 图案跑偏 | ≤2mm/5m ⚠️ | 靠尺 |
- [ ] L192: | 起拱 | 伸缩缝不足/雨季膨胀 | 8-10mm 强制；雨季取上限 ⚠️ |
- [ ] L195: | 边缘泡发 | 湿拖把/无防潮层 | PE 膜强制；半干拖 ⚠️ |
- [ ] L197: | 窗边褪色 | 紫外线暴晒（SPC） | 暴晒区窗帘/贴膜 ⚠️ |
- [ ] L237: │   ├── 平整度 ≤3mm/2m ⚠️ → 前置门
- [ ] L238: │   ├── 含水率 ≤12% ⚠️ → 雨季重点
- [ ] L239: │   └── 伸缩缝 8-10mm ⚠️ → [[floor-buckling]] 防线
- [ ] L252: ├── 高湿 → PE 防潮层强制 ⚠️
- [ ] L253: └── 雨季 → 伸缩缝取上限 ⚠️

### Wood Veneer Panel Wall Installation木饰面挂板工艺（10 处）

- [ ] L64: | **Veneer Panel Thickness** | 3–6mm (backed with plywood/MDF) ⚠️ | — |
- [ ] L65: | **Substrate Flatness** | ≤ 2mm / 2m ⚠️ | For direct-bond method |
- [ ] L66: | **Expansion Joint Width** | **3–5mm** (at all panel junctions) ⚠️ | Mandatory for humidity movement |
- [ ] L67: | **Expansion Joint Spacing** | ≤ 2.4m (horizontal) / ≤ 1.2m (vertical) ⚠️ | — |
- [ ] L68: | **Moisture Content of Veneer** | **8–12%** (at installation) ⚠️ | Must match ambient equilibrium |
- [ ] L132: | **饰面板厚度** | 3–6mm（背衬胶合板/MDF）⚠️ | — |
- [ ] L133: | **基层平整度** | ≤ 2mm / 2m ⚠️ | 直接粘贴法适用 |
- [ ] L134: | **伸缩缝宽度** | **3–5mm**（所有板缝处）⚠️ | 湿度变形强制项 |
- [ ] L135: | **伸缩缝间距** | 水平≤2.4m / 垂直≤1.2m ⚠️ | — |
- [ ] L136: | **饰面板含水率** | **8–12%**（安装时）⚠️ | 须与环境平衡含水率匹配 |


---
全库共 **741 处 ⚠️**。校对完重跑 `scripts/generate_checklist.py` 核对清零。
