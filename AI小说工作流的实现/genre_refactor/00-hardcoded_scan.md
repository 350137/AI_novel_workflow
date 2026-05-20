# Phase 0.1：硬编码题材内容扫描报告

> 扫描范围：`agents/` `protocols/` `templates/` `.claude/skills/` `docs/`
> 扫描日期：2026-05-04

---

## 一、扫描结果总表

### 1.1 Agent Prompts（6 文件，命中 80+ 处）

| 文件 | 行号（示例） | 硬编码内容 | 类型 | 替换为 Genre Profile 字段 |
|------|-------------|-----------|------|--------------------------|
| **advisor** | 26 | "废材逆袭流的玄幻小说" | 题材示例 | `genre.examples` |
| advisor | 66 | "玄幻/都市/仙侠/科幻/历史/悬疑/武侠/军事/奇幻/灵异" | 题材枚举 | `genre.available_genres`（外置） |
| advisor | 73 | "打脸逆袭/扮猪吃虎/降维打击" | 爽点模式枚举 | `genre.satisfaction_types` |
| advisor | 96 | "扮猪吃虎（表面废材实则大佬）" | 爽点模式 | `genre.satisfaction_types.reversal` |
| advisor | 99 | "重生复仇（前世记忆+今生逆袭）" | 爽点模式 | `genre.satisfaction_types.revenge` |
| advisor | 117 | "'废材逆袭'，废材的原因是什么——天生废脉、被封印、还是被夺走天赋？" | 题材特定追问 | `genre.advisor_questions.q1_followups` |
| advisor | 133 | "'废材'标签是社会用来控制人的工具" | 题材示例 | 保留为示例，标注 `<!-- example: xuanhuan -->` |
| advisor | 286,306,340 | "废材 + 金手指" / "证明废材标签是谎言" / "被封印的废材 + 三年从未停止修炼" | 主角设定示例 | `genre.protagonist_archetypes` |
| advisor | 373 | `primary: "<主类型：玄幻>"` | Genre Profile YAML | `genre.primary` |
| advisor | 375 | "玄幻世界不能出现科幻元素如'纳米机器人'" | 禁止元素 | `genre.world_rules.forbidden_elements` |
| advisor | 437 | "战力体系 vs 爽点节奏" | 审计一致性检查 | `genre.audit_consistency_checks` |
| advisor | 442 | "情感型爽点为主→战斗型玄幻" | 题材匹配检查 | `genre.satisfaction_type_constraints` |
| advisor | 493 | "疲劳词表（来源：inkos 玄幻预设 + onkos 脚本检测，≥15词）" | 疲劳词表 | `genre.fatigue_words` |
| advisor | 558 | `reversal: { enabled: true, description: "逆袭型：从底层到巅峰的身份跃迁" }` | 爽点配置 | `genre.satisfaction_types.reversal` |
| advisor | 569,573 | "战力体系规则" / "境界间战力差距明确：高1境=2-3个低境合力" | 战力体系 | `genre.power_system` |
| advisor | 594 | "不使用现代网络用语（玄幻/古风）" | 语言禁止 | `genre.language_rules` |
| advisor | 607 | `卷末章: { strictDimensions: ["战力崩坏", "伏笔回收"] }` | 审计维度 | `genre.volume_end_strict_dimensions` |
| advisor | 738 | "战力体系规则（如适用）" | 条件配置 | `genre.power_system`（可为 null） |
| advisor | 813 | `genre/xuanhuan.md` | Genre Profile 路径 | `genre/{genre_name}.md` |
| **auditor** | 35 | "战力崩坏、伏笔回收、爽点结构完整性" | 卷末审计维度 | `genre.volume_end_strict_dimensions` |
| auditor | 168 | "林云'开元巅峰'但 current_state 说'开元中境'" | 审计示例 | 保留为示例 |
| auditor | 248 | "林云的核心特质=隐忍克制" | 审计示例 | 保留为示例 |
| auditor | 266-267 | "师兄故意安排了这场测试——他知道林云隐藏了实力" | 审计示例 | 保留为示例 |
| auditor | 284 | "25. 战力崩坏" | 审计维度名 | `genre.power_system` 非 null 时启用 |
| auditor | 304-305 | "POV=林云" | 审计示例 | 保留为示例 |
| auditor | 327 | "不是'灵力暴涨'四个字——分解为感官层次" | 审计示例 | 保留为示例 |
| auditor | 385,389 | "林云（少言冷峻）" / "林云心想" | 审计示例 | 保留为示例 |
| auditor | 463 | "玄幻世界是否出现了'纳米'、'量子'、'基因'" | 世界观一致性 | `genre.world_rules.forbidden_concepts` |
| auditor | 468 | "'这不科学'→ 玄幻世界不以此为标准" | 世界观一致性 | `genre.world_rules.forbidden_phrases` |
| auditor | 481 | "玄幻世界特有检查" | 题材特定审计 | `genre.special_audit_checks` |
| auditor | 543-549 | "战力体系严格一致：跨境≥2项条件..." | 战力评分标准 | `genre.power_system.scoring_rubric` |
| auditor | 656 | "玄幻世界角色可能这样说" | 评分弹性 | `genre.scoring_flexibility` |
| auditor | 744,785 | "战力崩坏（违反战力体系硬规则）" | 严重问题定义 | `genre.critical_issues` |
| auditor | 826 | "爆发章天然难度最高（爽点结构+节奏+战力+对话）" | 章节类型权重 | `genre.chapter_type_weights` |
| auditor | 873 | "林云和沈清雪的对话" | 审计示例 | 保留为示例 |
| auditor | 925 | "林云在坊市找到七号门的实证" | 审计示例 | 保留为示例 |
| auditor | 938 | "林云确认灵气纹路与混沌珠纹路一致" | 审计示例 | 保留为示例 |
| auditor | 951 | "林云上次在坊市是第10章" | 审计示例 | 保留为示例 |
| **planner** | 34 | `genre_profile.md` — 节奏规则/爽点公式/战力规则/禁止事项 | Genre Profile 引用 | Ok（已正确引用外置文件） |
| planner | 69 | "被封印的废材能否在无人知晓的情况下暗中恢复实力？" | 卷命题示例 | 保留为示例 |
| planner | 97 | "打脸/突破/获得/逆袭/认知颠覆/情感" | 爽点类型枚举 | `genre.satisfaction_types` |
| planner | 226 | "逆袭钩子" | 钩子类型 | `genre.hook_types` |
| planner | 280 | "境界成长节点（哪些章涉及突破/战力提升）" | 大纲字段 | `genre.outline_fields`（power_system 非 null 时添加） |
| planner | 720 | `genre_profile.md` — 类型配置 | Genre Profile 引用 | Ok |
| **reviser** | 148 | "战力崩坏" | STRUCTURAL 问题类型 | `genre.structural_issue_types` |
| reviser | 162 | "战力崩坏 → 重写战斗段落（遵守 powerSystem 硬规则）" | 修订策略 | `genre.revision_strategies` |
| reviser | 230 | "战力崩坏：跨境战斗未满足≥2项条件" | 修订示例 | 保留为示例 |
| **writer** | 120 | "灵力如潮水般涌来" | 写作示例 | 保留为示例 |
| writer | 191 | "灵力温热" | 写作示例 | 保留为示例 |
| writer | 357 | "逆袭钩子：下一章是打脸/突破/实力展示" | 钩子类型 | `genre.hook_types` |
| writer | 384 | "废材逆袭正式开始" | 写作示例 | 保留为示例 |
| writer | 429 | "悬念钩子→好奇值高 / 威胁钩子→不安值高 / 逆袭钩子→期待值高" | 钩子-情绪映射 | `genre.hook_emotion_mapping` |

### 1.2 Protocols（6 文件，命中 2 处）

| 文件 | 行号 | 硬编码内容 | 类型 | 替换方案 |
|------|------|-----------|------|---------|
| chapter_memo.schema.md | 17 | `pov: "第一人称（林云）"` | 示例 | 改为 `pov: "第一人称（{{protagonist_name}}）"` |
| character_state.schema.json | 65 | "已掌握的功法/技能" | 字段描述 | 保留（通用描述） |

### 1.3 Templates（6 文件，命中 2 处）

| 文件 | 行号 | 硬编码内容 | 类型 | 替换方案 |
|------|------|-----------|------|---------|
| character-template-tomato.md | 18 | "杂役弟子但暗中恢复实力的废材" | 角色示例 | 添加多题材示例 |
| golden-opening-template.md | 41 | "穿越成废材被退婚那天，我绑定了满级神豪系统。" | 开头示例 | 添加多题材示例 |

### 1.4 Skills（7 文件，命中 2 处）

| 文件 | 行号 | 硬编码内容 | 类型 | 替换方案 |
|------|------|-----------|------|---------|
| write-volume/SKILL.md | 88 | "林云 \| 开元中境 \| 开元巅峰 \| 15, 19" | 角色状态示例 | `{{protagonist_name}} \| {{state_before}} \| {{state_after}}` |
| write-volume/SKILL.md | 95 | "林云×沈清雪 \| 初识 \| 信任初建 \| 13, 17" | 关系示例 | `{{relationship_example}}` |

### 1.5 Docs（1 文件，命中 1 处）

| 文件 | 行号 | 硬编码内容 | 类型 | 替换方案 |
|------|------|-----------|------|---------|
| workflow-orchestrator.md | 319 | "废材恢复实力，获得金手指第一层" | 卷计划示例 | `{{volume_1_goal}}` |

---

## 二、硬编码类型分布统计

| 类型 | 命中次数 | 严重程度 | 处理策略 |
|------|---------|---------|---------|
| **题材示例（角色名/情节）** | ~45 处 | 🟡 中等 | 保留为示例，添加 `<!-- example: xuanhuan -->` 标注，并补充其他题材示例 |
| **题材枚举列表** | 3 处 | 🔴 关键 | 外置到 Genre Profile Spec |
| **爽点模式配置** | 6 处 | 🔴 关键 | 全部参数化为 `genre.satisfaction_types.*` |
| **战力体系** | 8 处 | 🔴 关键 | 参数化为 `genre.power_system`，非玄幻题材可为 `null` |
| **疲劳词表** | 1 处 | 🟠 重要 | 已部分外置（引用 inkos 玄幻预设），需改为通用注入 |
| **禁止模式/元素** | 4 处 | 🟠 重要 | 参数化为 `genre.world_rules.forbidden_*` |
| **审计维度** | 6 处 | 🟠 重要 | 分为通用维度（始终启用）和题材维度（Genre Profile 配置） |
| **钩子类型** | 3 处 | 🟡 中等 | 参数化为 `genre.hook_types` |
| **语言/句法规则** | 2 处 | 🟡 中等 | 参数化为 `genre.language_rules` |
| **Genre Profile 路径引用** | 5 处 | 🟢 良好 | 已正确引用外置文件，需标准化命名 |

---

## 三、关键发现

### 3.1 好消息：架构已有 Genre Profile 概念

- Advisor prompt 已有 Phase 5（Genre Profile 初始化），包含结构化的 YAML 模板
- Planner prompt 已引用 `story/style/genre_profile.md`
- 多个 Agent 在输入段列出了 Genre Profile 作为数据源

**但**：Genre Profile 的 Schema 只在 Advisor prompt 中定义（未独立），且字段偏玄幻。

### 3.2 坏消息：示例全部来自同一小说

- 约 45 处硬编码了"林云"、"废材"、"灵力"、"开元"等特定小说的内容
- 这些是作为**示例**存在的，不影响逻辑，但会让其他题材的 Agent 产生混乱
- 策略：保留为带标签的示例，并补充 2-3 个其他题材的等效示例

### 3.3 最关键的 5 个重构点

1. **Advisor 的 Q1-Q5**：问题内容需要根据题材动态调整
2. **Auditor 的战力崩坏维度**：玄幻特有，都市悬疑不应启用
3. **Planner 的爽点类型枚举**：当前硬编码 6 种，需从 Genre Profile 注入
4. **Writer 的钩子-情绪映射表**：逆袭→期待 / 悬念→好奇，这是题材相关的
5. **Reviser 的 STRUCTURAL 问题类型**：战力崩坏是玄幻特有的严重问题
