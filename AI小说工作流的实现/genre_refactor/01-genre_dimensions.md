# Phase 0.2：题材配置维度清单

> 提取源：10 个本地小说 skills + inkos 15 Genre Profile
> 目的：定义 Genre Profile Schema 的字段全集（所有题材的最大公约数 + 题材特有扩展）

---

## 一、维度来源矩阵

| 维度 | fiction-crafter | novelist | novel-writer-cn | story-cog | story-writer | my-novel-writer | openclaw-novel-write | tomato-novelist | onkos | inkos |
|------|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
| 题材类型 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | — | ✅ | — | ✅ |
| 世界观规则 | ✅ | — | ✅ | ✅ | ✅ | ✅ | — | — | ✅ | ✅ |
| 力量/数值体系 | ✅ | — | — | ✅ | — | — | — | — | — | ✅ |
| 爽点/节奏模式 | ✅ | ✅ | — | — | — | — | — | ✅ | — | ✅ |
| 人物原型 | — | ✅ | ✅ | ✅ | ✅ | — | — | — | ✅ | ✅ |
| 情感线权重 | — | — | — | — | — | — | — | ✅ | — | ✅ |
| 冲突类型 | — | ✅ | — | ✅ | ✅ | — | — | — | — | — |
| 语言/文风 | ✅ | — | — | — | — | ✅ | ✅ | ✅ | — | ✅ |
| 违禁词/疲劳词 | — | ✅ | — | — | — | ✅ | ✅ | — | ✅ | ✅ |
| 禁止模式 | ✅ | ✅ | — | — | — | — | — | — | — | ✅ |
| 章节结构 | — | — | ✅ | — | — | ✅ | — | ✅ | — | ✅ |
| 钩子/悬念类型 | — | — | — | — | — | — | — | — | ✅ | — |
| 视角/POV | — | — | — | — | ✅ | — | — | — | — | — |
| 平台适配 | ✅ | — | — | — | — | — | — | ✅ | — | ✅ |
| 对话风格 | — | — | — | — | — | — | — | ✅ | — | — |
| 战斗密度 | ✅ | — | — | — | — | — | — | — | — | ✅ |
| 幽默比例 | — | — | — | — | — | — | — | ✅ | — | — |

---

## 二、维度详细定义

### 维度组 A：世界观（World Building）

#### A1. 题材主类型 `genre.primary`
- **说明**：小说的核心题材标签
- **类型**：`enum`（单选自封闭集合）
- **来源**：fiction-crafter, novelist, inkos
- **可选值**：玄幻 / 都市 / 仙侠 / 科幻 / 历史 / 悬疑 / 武侠 / 军事 / 奇幻 / 灵异 / 游戏 / 竞技 / 种田 / 无限流 / 系统流
- **必填**：是

#### A2. 子类型/融合标签 `genre.sub_genres`
- **说明**：题材融合标签（如"玄幻+悬疑"、"都市+修真"）
- **类型**：`array[string]`
- **来源**：fiction-crafter（支持多题材融合）
- **必填**：否

#### A3. 世界观底色 `genre.world_basis`
- **说明**：世界的基础设定
- **类型**：`enum`
- **来源**：inkos（"world basis"字段）, story-cog
- **可选值**：架空异界 / 平行地球 / 近未来 / 远古神话 / 末世 / 虚拟游戏 / 历史演义 / 混合
- **必填**：是

#### A4. 世界观核心规则 `genre.world_rules`
- **说明**：该世界不可违背的基本法则（3-8 条）
- **类型**：`array[string]`
- **来源**：inkos（"world rules"）, onkos（"hard constraints"）
- **必填**：是

#### A5. 禁止概念 `genre.world_rules.forbidden_concepts`
- **说明**：该世界观中不应出现的现代/其他世界观概念
- **类型**：`array[string]`
- **来源**：inkos, Auditor prompt
- **示例**：玄幻 → ["纳米", "量子", "基因", "核弹"]；都市 → 无此约束
- **必填**：否（取决于题材）

#### A6. 禁止口头禅 `genre.world_rules.forbidden_phrases`
- **说明**：该世界观中角色不应说的口头禅
- **类型**：`array[string]`
- **来源**：Auditor prompt（"这不科学" → 玄幻不应出现）
- **必填**：否

---

### 维度组 B：力量/数值体系（Power System）

#### B1. 是否有力量体系 `genre.power_system.enabled`
- **说明**：该题材是否有等级化的力量/战力体系
- **类型**：`boolean`
- **来源**：inkos, fiction-crafter
- **必填**：是
- **影响**：如果 `false`，以下 B2-B5 全部跳过；Auditor 的"战力崩坏"维度关闭

#### B2. 力量体系名称 `genre.power_system.name`
- **说明**：如"修真境界"、"斗气等级"、"异能分级"、"职业段位"
- **类型**：`string`
- **来源**：inkos（"power system type"）
- **必填**：当 `enabled = true`

#### B3. 等级序列 `genre.power_system.levels`
- **说明**：从低到高的完整等级名称列表
- **类型**：`array[string]`
- **来源**：inkos（"levels"）
- **必填**：当 `enabled = true`

#### B4. 跨境规则 `genre.power_system.cross_level_rules`
- **说明**：跨越境界战斗的硬性条件（如"高1境=2-3个低境合力"）
- **类型**：`array[string]`
- **来源**：Advisor prompt（已有）, inkos
- **必填**：当 `enabled = true`

#### B5. 战力评分标准 `genre.power_system.scoring_rubric`
- **说明**：Auditor 维度 25"战力崩坏"的 10/7/4/1/0 评分细则
- **类型**：`object`（每个分数段的描述）
- **来源**：Auditor prompt
- **必填**：当 `enabled = true`

---

### 维度组 C：爽点与节奏（Satisfaction & Rhythm）

#### C1. 爽点类型 `genre.satisfaction_types`
- **说明**：该题材的核心爽点模式及其是否启用
- **类型**：`map[string, {enabled: boolean, description: string}]`
- **来源**：fiction-crafter, novelist（双结构模型）, inkos（"satisfaction types"）
- **标准键**：
  - `reversal` — 打脸逆袭 / 扮猪吃虎
  - `breakthrough` — 实力突破 / 境界提升
  - `acquisition` — 获得宝物 / 机缘
  - `revenge` — 复仇 / 清算
  - `recognition` — 被认可 / 身份揭露
  - `romance` — 情感进展 / 甜蜜互动
  - `mystery_reveal` — 谜题揭晓 / 真相大白
  - `comedy` — 幽默 / 搞笑
  - `horror` — 恐怖 / 惊悚
  - `survival` — 绝境求生
- **必填**：是（至少启用 2 种）

#### C2. 爽点节奏公式 `genre.satisfaction_rhythm`
- **说明**：多少章一次什么级别的爽点
- **类型**：`object`
- **来源**：tomato-novelist（番茄平台的章节节奏）, novelist
- **结构**：
  ```yaml
  micro_relief: {interval_chapters: 1-2, description: "小爽点"}
  minor_payoff: {interval_chapters: 3-5, description: "中爽点"}
  major_payoff: {interval_chapters: 10-15, description: "大高潮"}
  ```
- **必填**：是

#### C3. 情绪曲线 `genre.emotion_curve`
- **说明**：章节间的情绪起伏模式
- **类型**：`enum`
- **来源**：tomato-novelist, novelist
- **可选值**：过山车式（玄幻/爽文）/ 渐进上升（悬疑）/ 波浪式（言情）/ 锯齿式（竞技）
- **必填**：是

#### C4. 战斗密度 `genre.combat_density`
- **说明**：战斗场景在总章节中的比例
- **类型**：`enum`
- **来源**：inkos, fiction-crafter
- **可选值**：极高（>50%章有战斗，如纯玄幻）/ 高（30-50%）/ 中（15-30%）/ 低（<15%，如纯悬疑）/ 无
- **必填**：是

#### C5. 幽默比例 `genre.humor_ratio`
- **说明**：幽默/轻松内容的比例
- **类型**：`enum`
- **来源**：tomato-novelist
- **可选值**：主打（喜剧向）/ 辅助（严肃主线+轻松支线）/ 点缀 / 无
- **必填**：否

---

### 维度组 D：情感线（Romance/Emotional Arc）

#### D1. 情感线权重 `genre.romance_weight`
- **说明**：情感/爱情线在主线中的占比
- **类型**：`enum`
- **来源**：tomato-novelist（男女频差异）, inkos
- **可选值**：主线（言情为主）/ 重要副线 / 辅助（点缀）/ 无
- **必填**：是

#### D2. 情感线类型 `genre.romance_type`
- **说明**：情感线的核心模式
- **类型**：`enum`
- **来源**：story-cog, tomato-novelist
- **可选值**：甜宠 / 虐恋 / 日久生情 / 破镜重圆 / 欢喜冤家 / 禁忌 / 多角 / 无
- **必填**：当 `romance_weight != "无"`

---

### 维度组 E：悬念与钩子（Suspense & Hooks）

#### E1. 悬念强度 `genre.suspense_intensity`
- **说明**：悬念/谜题在叙事中的驱动力强度
- **类型**：`enum`
- **来源**：novelist（悬疑线设计）
- **可选值**：核心驱动（悬疑为主）/ 重要辅助 / 点缀 / 无
- **必填**：是

#### E2. 钩子类型权重 `genre.hook_types`
- **说明**：各类型钩子的使用频率权重
- **类型**：`map[string, number]`（0-10）
- **来源**：onkos（hook 状态机）, Writer prompt
- **标准键**：`suspense`（悬念钩子）, `threat`（威胁钩子）, `reversal`（逆袭钩子）, `romance`（情感钩子）, `mystery`（谜题钩子）, `cliffhanger`（断章）
- **必填**：是

#### E3. 钩子-情绪映射 `genre.hook_emotion_mapping`
- **说明**：钩子类型 → 目标读者情绪的映射
- **类型**：`map[string, string]`
- **来源**：Writer prompt（已有），需参数化
- **示例**：
  ```yaml
  suspense: "好奇"
  threat: "不安"
  reversal: "期待"
  romance: "心动"
  mystery: "困惑→求解"
  ```
- **必填**：是

---

### 维度组 F：人物（Characters）

#### F1. 主角原型 `genre.protagonist_archetypes`
- **说明**：该题材常见的主角人设原型
- **类型**：`array[string]`
- **来源**：fiction-crafter, novelist, story-writer
- **示例**：玄幻 → ["废材逆袭", "重生复仇", "天才陨落再起"]；都市 → ["普通人不普通", "隐世高手", "重生经商"]
- **必填**：是

#### F2. 人物关系张力类型 `genre.relationship_tension_types`
- **说明**：该题材中常见的人物关系冲突模式
- **类型**：`array[string]`
- **来源**：story-cog, tomato-novelist
- **必填**：否

---

### 维度组 G：语言与文风（Language & Style）

#### G1. 叙述风格 `genre.narrative_style`
- **说明**：基本叙述风格
- **类型**：`enum`
- **来源**：inkos, openclaw-novel-write
- **可选值**：白描快节奏（网文主流）/ 细腻描写 / 诗意 / 冷峻克制 / 热血燃 / 诙谐
- **必填**：是

#### G2. 疲劳词表 `genre.fatigue_words`
- **说明**：该题材最容易滥用的词汇（≥15 词）
- **类型**：`array[string]`
- **来源**：inkos（Genre Profile 疲劳词表）, onkos（脚本检测）, novelist（黑名单）, openclaw-novel-write（9组禁用词）
- **必填**：是

#### G3. 句法红线 `genre.syntax_rules`
- **说明**：句子层面的硬约束
- **类型**：`array[string]`
- **来源**：inkos, my-novel-writer
- **示例**：
  - "单句不超过 50 字"
  - "对话句不超过 20 字（冷峻主角）"
  - "一段不超过 4 句"
- **必填**：否

#### G4. 禁止语言模式 `genre.language_rules.forbidden_patterns`
- **说明**：该题材不应使用的语言风格
- **类型**：`array[string]`
- **来源**：Advisor prompt, inkos
- **示例**：玄幻 → ["不使用现代网络用语", "不使用英文缩写"]；都市 → 无此约束
- **必填**：否

---

### 维度组 H：章节要求（Chapter Requirements）

#### H1. 标准章节字数 `genre.chapter_word_count`
- **说明**：推荐每章字数范围
- **类型**：`{min: number, max: number, target: number}`
- **来源**：tomato-novelist, inkos
- **必填**：是

#### H2. 卷结构 `genre.volume_structure`
- **说明**：卷的典型长度和结构
- **类型**：`{chapters_per_volume: number, volume_end_requirements: array[string]}`
- **来源**：Planner prompt, inkos
- **必填**：是

#### H3. 章末要求 `genre.chapter_ending_requirements`
- **说明**：每章结尾必须包含的元素
- **类型**：`array[string]`
- **来源**：Writer prompt, tomato-novelist
- **必填**：是

---

### 维度组 I：审计配置（Audit Configuration）

#### I1. 启用的审计维度 `genre.audit_dimensions`
- **说明**：40 维审计中哪些适用本题材（其余关闭）
- **类型**：`map[string, boolean]`
- **来源**：Auditor prompt（40 维设计）
- **必填**：是
- **特殊规则**：`power_breakdown`（战力崩坏）仅当 `power_system.enabled = true` 时启用

#### I2. 题材特定审计项 `genre.special_audit_checks`
- **说明**：该题材特有的审计检查（超出 40 维通用列表的）
- **类型**：`array[{name, description, scoring}]`
- **来源**：Auditor prompt（"玄幻世界特有检查"）
- **必填**：否

#### I3. 章节类型权重 `genre.chapter_type_weights`
- **说明**：不同章节类型的期望分数调整
- **类型**：`map[string, number]`
- **来源**：Auditor prompt
- **必填**：否

#### I4. 评分弹性 `genre.scoring_flexibility`
- **说明**：某些维度可根据题材放宽评分
- **类型**：`map[string, string]`
- **来源**：Auditor prompt
- **必填**：否

---

### 维度组 J：平台适配（Platform）

#### J1. 目标平台 `genre.target_platform`
- **说明**：主要发布平台
- **类型**：`enum`
- **来源**：tomato-novelist, inkos
- **可选值**：番茄小说 / 起点中文网 / 微信读书 / 通用
- **必填**：否

#### J2. 平台特定要求 `genre.platform_requirements`
- **说明**：目标平台对内容/格式的特定要求
- **类型**：`array[string]`
- **来源**：tomato-novelist
- **必填**：否

---

## 三、维度启用策略

| 维度组 | 玄幻 | 都市悬疑 | 仙侠言情 | 种田 | 无限流 |
|--------|:--:|:--:|:--:|:--:|:--:|
| A 世界观 | ✅ | ✅ | ✅ | ✅ | ✅ |
| B 力量体系 | ✅ (完整) | ❌ | ✅ (简化) | ❌ | ✅ (特殊) |
| C 爽点节奏 | ✅ (打脸+突破) | ✅ (悬念+反转) | ✅ (情感+甜) | ✅ (收获+建设) | ✅ (生存+突破) |
| D 情感线 | 辅助 | 辅助 | **主线** | 辅助 | 点缀 |
| E 悬念 | 辅助 | **核心** | 辅助 | 点缀 | **核心** |
| F 人物 | ✅ | ✅ | ✅ | ✅ | ✅ |
| G 语言 | 白描+燃 | 冷峻+紧张 | 细腻+甜 | 轻松+温馨 | 紧张+燃 |
| H 章节 | 2200-2800 | 2000-2500 | 2000-2800 | 2000-2500 | 2200-3000 |
| I 审计 | 全 40 维 | 关闭战力维度 | 关闭战力维度 | 关闭战力/悬念 | 特殊战力规则 |
| J 平台 | 番茄 | 起点/微信 | 番茄/微信 | 番茄 | 起点/番茄 |

---

## 四、默认值设定原则

1. 如果某个维度有 ≥60% 的题材共享相同值 → 设为默认值
2. 如果维度分布均匀 → 不设默认值，要求用户选择
3. `enabled` 字段统一默认为 `false`（opt-in 而非 opt-out）
