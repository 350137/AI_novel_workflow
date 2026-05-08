# 世界观构建 — 跨 Skills/项目比对报告

## 覆盖度矩阵

| 分析对象 | 类型 | 覆盖度 | 实现方式 | 亮点 |
|----------|------|--------|---------|------|
| fiction-crafter | skill | ⚡ | 提示词自动补全力量体系+社会规则；STORY_BIBLE.md 持续沉淀 | 力量体系要求明确层级（便于体现碾压感） |
| novelist | skill | ✅ | 力量体系层级设计（标志+代价+天花板）；核心矛盾三问；金手指必有代价 | 境界突破不是"经验值满了就升级"；天花板可控 |
| novel-writer-cn | skill | ❌ | 仅在"第一幕-铺垫"中提及 | — |
| story-cog | skill | ⚡ | prompt 模板覆盖7个子维度（地理/魔法/社会/历史/势力/科技/地点） | 世界构建 prompt 模板结构化程度高 |
| story-writer | skill | ⚡ | 对话式引导，无结构化模板 | 双语支持 |
| my-novel-writer | skill | ✅ | `--set-world` + world_building.md 模板（9子维度） | pydantic 模型验证配置完整性 |
| openclaw-novel-write | skill | ⚡ | spec/knowledge/ + constitution.md（宪法级约束） | constitution.md 是所有后续产出的最高约束 |
| tomato-novelist | skill | ❌ | 无独立世界观模块 | — |
| onkos | skill | ✅ | 知识图谱（kg_nodes/kg_edges）+ import-settings + add-node | 关系型+图数据库双存储；约束自动附加到上下文 |
| inkos | 项目 | ⚡ | 15个 Genre Profile（每种类型定义设定规范） | 类型覆盖最广（15种预设） |

## 共同模式

1. **力量/等级体系是共同关注点**：fiction-crafter、novelist、my-novel-writer 都要求明确层级
2. **设定与正文分离存储**：所有 ✅ 级 skill 都有独立的设定存储（文件或DB）
3. **设定驱动创作**：设定在写作前被加载为上下文约束
4. **缺乏跨章设定验证**：无 skill 自动检测"本章是否违反已建立的世界规则"（onkos 的部分 continuity_check 除外）

## 差异化分析

| 特色做法 | 采用者 | 优劣分析 |
|---------|--------|---------|
| 金手指必须有代价 | novelist | ✅ 防止无敌流崩坏 ❌ 仅限爽文 |
| 知识图谱双存储 | onkos | ✅ 图遍历查询关系 ❌ 复杂度高 |
| Genre Profile 预设 | inkos | ✅ 快速启动 ❌ 英文为主，中文须适配 |
| 宪法级最高约束 | openclaw-novel-write | ✅ 不偏离核心 ❌ 约束过多可能限制创作 |
| pydantic 模型验证 | my-novel-writer | ✅ 配置完整性 ❌ 仅限 Python 生态 |

## onkos/inkos 工作流视角

- **onkos**：知识图谱 + 约束自动附加，可使世界观设定在每次写作时被自动加载为约束。`import-settings` 支持批量导入已有设定文档
- **inkos**：Genre Profile 定义了每种类型的设定规范，Planner 在生成 ChapterMemo 时会参考。但 Genre Profile 是英文网文向

## 最佳实践推荐

- **首选方案**：**onkos**（知识图谱+约束系统）作为设定存储和约束注入层 + **novelist**（金手指代价+天花板设计哲学）作为设定质量原则
- **推荐理由**：onkos 提供最可靠的技术基础设施（图数据库+自动约束注入），novelist 提供最严谨的设定质量原则（有代价/有天花板）
- **可组合方案**：onkos（存储+约束）+ my-novel-writer（模板初始化）+ novelist（设计原则）+ inkos Genre Profile（中文玄幻类型预设参考）

## 空白地带

1. **无自动设定矛盾检测**：没有 skill 能在写作后自动检测"本章是否违反世界观规则"（onkos continuity_checker 最近似但不专门为此设计）
2. **无设定可视化**：没有 skill 能生成世界观地图或势力关系图（fiction-crafter 的 Mermaid 图解最近似）
3. **无设定版本管理**：世界观变更历史无法追踪和回滚（onkos 快照系统可用于此但非专门设计）
4. **无跨书设定复用**：不能将一个项目的世界观模板复用到新项目
