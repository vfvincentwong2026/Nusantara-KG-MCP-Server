# 数据模型详解

## 📊 实体类型一览

| 类型 | 文件名前缀 | 目录 | 说明 |
| :--- | :--- | :--- | :--- |
| `case` | 案例_ | `01_Cases/` | 真实落地项目 |
| `style` | — | `02_Styles/` | 设计风格 |
| `space` | — | `03_Spaces/` | 功能空间 |
| `material` | 材料_ | `04_Materials/` | 建材 |
| `process` | 工艺_ | `05_Processes/` | 施工工艺 |
| `labor` | — | `06_Labor/` | 人工配置 |
| `workhour` | 工时_ | `07_WorkHours/` | 工时定额 |
| `effect` | 效果_ | `08_Effects/` | 效果矩阵 |

---

## 📝 完整字段定义

### Case (案例)

```typescript
interface Case {
  id: string;                    // case_jakarta_selatan_01
  name: {
    en: string;                  // South Jakarta French Apartment
    zh: string;                  // 雅加达南区法式公寓
    id: string;                  // Apartemen Prancis Jakarta Selatan
  };
  style: string;                 // 关联风格 ID
  location: string;              // 地区
  total_area: number;            // 总面积 (m²)
  budget: number;                // 总造价 (IDR)
  spaces: string[];              // 关联空间 ID 列表
  tags: string[];                // 标签
  images: string[];              // 图片文件名列表
  description: string;           // 项目描述 (Markdown)
  highlights: string[];          // 设计亮点
  materials: {                   // 材料配置
    space: string;
    material: string;
    brand: string;
    spec: string;
  }[];
  processes: string[];           // 关联工艺 ID 列表
}
Process (工艺)
typescript
interface Process {
  id: string;                    // process_tiling_wet
  name: {
    en: string;                  // Wet Method Tiling
    zh: string;                  // 湿铺法地砖铺贴
    id: string;                  // Pemasangan Ubin Metode Basah
  };
  process_type: string;          // 铺贴 | 木工 | 油漆 | 水电
  difficulty_level: 1-5;         // 难度等级
  space_applicable: string[];    // 适用空间
  material_applicable: string[]; // 适用材料
  images: string[];
  parameters: {                  // 工艺参数
    thickness: { value: number; unit: string };
    flatness_tolerance: { value: number; unit: string };
    hollow_ratio_standard: string;
  };
  workflow: {                    // 工序流程
    step: number;
    description: string;
    tools: string[];
    checkpoint: string;
    images: string[];
  }[];
  quality_check: string[];       // 验收标准
  issues: {                      // 常见问题
    problem: string;
    cause: string;
    solution: string;
  }[];
  relations: {                   // 关联关系
    recommended_labor: string;   // 推荐人工
    alternatives: string[];      // 替代工艺
    related_materials: string[]; // 相关材料
  };
}
Labor (人工)
typescript
interface Labor {
  id: string;                    // labor_chinese_master
  name: {
    en: string;                  // Chinese Master Craftsman
    zh: string;                  // 中国技工
    id: string;                  // Tukang Ahli Tiongkok
  };
  level: string;                 // 高级 | 中级 | 普通
  skills: string[];              // 擅长工艺/技能
  daily_rate: {                  // 日薪
    min: number;                 // IDR
    max: number;                 // IDR
  };
  efficiency: {                  // 效率
    per_10sqm: number;           // 每10平米工日
    unit: string;
  };
  notes: string;                 // 备注
  suitable_for: string[];        // 适用场景
  not_suitable_for: string[];    // 不适用场景
  comparison: {                  // 与其它人工对比
    vs: string;
    score: {                     // 1-5 评分
      skill: number;
      quality: number;
      cost_efficiency: number;
    };
  }[];
}
WorkHour (工时)
typescript
interface WorkHour {
  id: string;                    // workhour_tiling_wet
  name: {
    en: string;
    zh: string;
    id: string;
  };
  process: string;               // 关联工艺 ID
  labor_level: string;           // 人工等级
  value: number;                 // 工时值
  unit: string;                  // 工时/m² | 工时/项
  notes: string;                 // 备注/数据来源
}
Material (材料)
typescript
interface Material {
  id: string;                    // material_marble_tile
  name: {
    en: string;                  // Marble Tile
    zh: string;                  // 大理石瓷砖
    id: string;                  // Ubin Marmer
  };
  category: string;              // 石材 | 木材 | 涂料 | 金属
  specs: {                       // 规格
    size: string;                // 120x60cm
    thickness: string;           // 9mm
    finish: string;              // 柔光 | 高光 | 哑光
  };
  brand: string;                 // 品牌
  price: {                       // 价格
    per_unit: number;            // IDR/片
    per_m2: number;              // IDR/m²
  };
  properties: {                  // 特性
    slip_resistance: string;     // 防滑性: 高/中/低
    scratch_resistance: string;  // 耐刮性
    maintenance: string;         // 维护说明
    durability: string;          // 耐久性
  };
  visual_effect: string;         // 视觉效果描述
  suitable_for: string[];        // 适用场景
  images: string[];
  suppliers: {                   // 供应商信息
    name: string;
    location: string;
    contact: string;
  }[];
}
🔗 关系定义
关系类型表
关系类型	源节点类型	目标节点类型	说明
has_style	case	style	案例拥有某风格
has_space	case/process	space	包含某空间/适用于某空间
uses_material	case/process	material	使用某材料
requires_process	material	process	材料需要某工艺施工
recommends_labor	process	labor	工艺推荐某人工
has_workhour	process	workhour	工艺有工时定额
produces_effect	material × process	effect	材料×工艺产生某效果
alternative_of	process/material	process/material	某实体的替代方案
similar_to	case	case	案例之间的相似性
关系权重
typescript
// 关系强度评分 (0-1)
const RELATION_WEIGHTS = {
  'has_style': 0.8,
  'uses_material': 0.9,
  'requires_process': 1.0,      // 强依赖
  'recommends_labor': 0.7,
  'alternative_of': 0.6,
  'similar_to': 0.5,
};
📊 查询示例
查询某个风格的所有案例
cypher
// Cypher 语法 (Neo4j 风格)
MATCH (c:case)-[:has_style]->(s:style {id: '法式轻奢'})
RETURN c.id, c.name, c.budget
查询某个工艺所需的人工和工时
cypher
MATCH (p:process {id: 'process_tiling_wet'})
MATCH (p)-[:recommends_labor]->(l:labor)
MATCH (p)-[:has_workhour]->(w:workhour)
RETURN l.name, w.value, w.unit
查询某个材料的完整施工方案
cypher
MATCH (m:material {id: 'material_marble_tile'})
MATCH (m)-[:requires_process]->(p:process)
MATCH (p)-[:recommends_labor]->(l:labor)
MATCH (p)-[:has_workhour]->(w:workhour)
RETURN p, l, w
💡 扩展建议
增加供应商节点：建立 supplier 类型，与 material 建立 supplies 关系

增加工具节点：建立 tool 类型，与 process 建立 uses_tool 关系

增加项目阶段节点：建立 phase 类型，与 process 建立 belongs_to_phase 关系

增加费用节点：建立 cost 类型，关联材料费/人工费/管理费

text

---

以上 5 个文档构成了完整的项目文档体系：

| 文档 | 用途 | 目标读者 |
| :--- | :--- | :--- |
| `README.md` | 项目首页/概览 | 所有人 |
| `CONTRIBUTING.md` | 贡献指南 | 外部贡献者 |
| `ARCHITECTURE.md` | 架构设计 | 开发者 |
| `LOCAL_SETUP.md` | 本地开发 | 开发者 |
| `DEPLOYMENT.md` | 部署指南 | 运维/DevOps |
| `DATA_MODEL.md` | 数据模型 | 数据维护者 |
