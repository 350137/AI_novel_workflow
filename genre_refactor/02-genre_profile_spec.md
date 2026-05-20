# Phase 0.3：Genre Profile 标准 Schema

> 基于：Advisor prompt 现有 Genre Profile YAML + inkos 15 Genre + 10 skills 维度分析
> 格式：YAML（可嵌入 Markdown frontmatter）+ Markdown 补充说明
> 每个字段标注来源

---

## 一、Schema 设计原则

1. **渐进式复杂度**：必填字段最小化，可选字段在需要时才展开
2. **题材无关核心 + 题材特定扩展**：所有题材共享 A/D/E/F/G/H 组；B/C/I/J 组按题材开关
3. **从 Advisor prompt 现有模板平滑升级**：保留已定义的字段结构，补充缺失维度
4. **可被 Agent 直接消费**：每个 Agent 的"Genre Profile 注入"段引用本文件中的具体 section

---

## 二、完整 Schema

```yaml
# ============================================================
# Genre Profile — <书名>
# 版本：基于 genre_profile_spec.md v1.0
# 生成者：hjw-novel-advisor（Phase 5）
# ============================================================

# ========== A. 基础元信息（必填） ==========
meta:
  book_title: "<书名>"
  genre_name: "<genre_profile 标识符，如 xuanhuan_feicai>"
  created: "<YYYY-MM-DD>"
  version: "1.0"

# ========== B. 题材定义（必填） ==========
genre:
  # 主类型（来源：fiction-crafter + inkos）
  primary: "玄幻"  # enum: 玄幻|都市|仙侠|科幻|历史|悬疑|武侠|军事|奇幻|灵异|游戏|竞技|种田|无限流|系统流

  # 子类型/融合标签（来源：fiction-crafter）
  sub_genres: []  # 如: ["悬疑", "修真"]

  # 世界观底色（来源：inkos world_basis）
  world_basis: "架空异界"  # enum: 架空异界|平行地球|近未来|远古神话|末世|虚拟游戏|历史演义|混合

# ========== C. 世界观规则（必填） ==========
world_rules:
  # 核心法则（3-8条，不可违背）（来源：inkos + onkos hard_constraints）
  core_laws:
    - "<法则1>"
    - "<法则2>"
    - "<法则3>"

  # 禁止概念——该世界观不应出现的现代/其他世界观概念（来源：inkos + Auditor维度34）
  forbidden_concepts: []
  # 玄幻示例: ["纳米", "量子", "基因", "核弹", "克隆"]
  # 都市示例: []

  # 禁止口头禅——该世界观角色不应说的话（来源：Auditor维度34）
  forbidden_phrases: []
  # 玄幻示例: ["这不科学", "从概率上来说"]
  # 都市示例: []

# ========== D. 力量/数值体系（条件必填） ==========
power_system:
  # 是否有等级化力量体系（来源：inkos + fiction-crafter）
  enabled: true  # 玄幻=true, 都市悬疑=false, 仙侠言情=true

  # --- 以下仅 enabled=true 时填写 ---
  name: "修真境界"  # 如: 修真境界|斗气等级|异能分级|职业段位|灵力层次

  # 从低到高的完整等级序列（来源：inkos levels）
  levels:
    - "炼气期"
    - "筑基期"
    - "金丹期"
    - "元婴期"
    - "化神期"

  # 跨境战斗硬规则（来源：Advisor prompt Phase 5 + inkos）
  cross_level_rules:
    - "高1境=2-3个低境合力（仅限同阶初期对巅峰）"
    - "跨境≥2个条件：属性克制 + 战斗经验碾压 + 对方重伤"
    - "跨境胜利后需≥3章适应期/后遗症（不能连续跨境）"
    - "禁忌：'意志力爆发送跨境'——必须满足至少1项客观条件"

  # Auditor 维度25"战力崩坏"评分细则（来源：Auditor prompt）
  scoring_rubric:
    score_10: "战力体系严格一致：跨境≥2项条件、突破有≥3章铺垫、无临时觉醒、有适应期"
    score_7_9: "战力基本一致，1处细节可商榷但不过分"
    score_4_6: "1处战力崩坏——如跨境战斗未满足条件/突破无铺垫"
    score_1_3: "多处战力崩坏——数值体系被系统性违反"
    score_0: "战力体系完全崩溃——境界失去意义"

# ========== E. 爽点与节奏（必填） ==========
satisfaction:
  # 爽点类型（来源：fiction-crafter + novelist双结构 + inkos satisfactionTypes）
  types:
    reversal:       { enabled: true,  description: "打脸逆袭/扮猪吃虎——从被轻视到实力展示" }
    breakthrough:   { enabled: true,  description: "实力突破/境界提升——修炼成果具象化" }
    acquisition:    { enabled: true,  description: "获得宝物/机缘/传承——资源升级" }
    revenge:        { enabled: false, description: "复仇清算——前世/过去的仇敌被解决" }
    recognition:    { enabled: true,  description: "身份被认可——隐藏实力被揭露的爽感" }
    romance:        { enabled: false, description: "情感进展/甜蜜互动——男女主关系升温" }
    mystery_reveal: { enabled: false, description: "谜题揭晓/真相大白——悬疑线收束" }
    comedy:         { enabled: false, description: "幽默/搞笑——轻松章节的情绪价值" }
    horror:         { enabled: false, description: "恐怖/惊悚——恐惧驱动的沉浸感" }
    survival:       { enabled: false, description: "绝境求生——生死边缘的紧张感" }

  # 节奏公式（来源：tomato-novelist + novelist）
  rhythm:
    micro_relief:  { interval_chapters: "1-2", description: "小爽点——段评槽点/小反转" }
    minor_payoff:  { interval_chapters: "3-5", description: "中爽点——打脸/突破/获得" }
    major_payoff:  { interval_chapters: "10-15", description: "大高潮——卷末大战/核心谜题揭晓" }

  # 情绪曲线（来源：tomato-novelist + novelist）
  emotion_curve: "过山车式"  # enum: 过山车式|渐进上升|波浪式|锯齿式

  # 战斗密度（来源：inkos + fiction-crafter）
  combat_density: "极高"  # enum: 极高(>50%)|高(30-50%)|中(15-30%)|低(<15%)|无

  # 幽默比例（来源：tomato-novelist）
  humor_ratio: "点缀"  # enum: 主打|辅助|点缀|无

# ========== F. 情感线（必填） ==========
romance:
  # 情感线权重（来源：tomato-novelist男女频差异 + inkos）
  weight: "辅助"  # enum: 主线|重要副线|辅助|无

  # 情感线类型（来源：story-cog + tomato-novelist）
  # 当 weight="无" 时可为 null
  type: null  # enum: 甜宠|虐恋|日久生情|破镜重圆|欢喜冤家|禁忌|多角|null

# ========== G. 悬念与钩子（必填） ==========
suspense:
  # 悬念强度（来源：novelist悬疑线）
  intensity: "辅助"  # enum: 核心驱动|重要辅助|点缀|无

  # 各钩子类型权重 0-10（来源：onkos hook状态机 + Writer prompt）
  hook_weights:
    suspense:    6   # 悬念钩子——"到底是什么..."
    threat:      7   # 威胁钩子——"接下来会发生什么危险..."
    reversal:    9   # 逆袭钩子——"下一章打脸/突破/实力展示..."
    romance:     0   # 情感钩子——"他们的关系会怎样..."
    mystery:     4   # 谜题钩子——"这个谜题的答案是什么..."
    cliffhanger: 5   # 断章——在关键时刻中断

  # 钩子→目标读者情绪的映射（来源：Writer prompt）
  hook_emotion_mapping:
    suspense:    "好奇值↑"
    threat:      "不安值↑"
    reversal:    "期待值↑"
    romance:     "心动值↑"
    mystery:     "困惑→求解欲↑"
    cliffhanger: "迫切想翻下一章"

# ========== H. 人物（必填） ==========
characters:
  # 主角原型（来源：fiction-crafter + novelist + story-writer）
  protagonist_archetypes:
    - "废材逆袭——表面废材实则暗中恢复实力"
    - "被封印者——力量被封印，逐步解封"
    # 都市示例: ["隐世高手——普通人外表下有特殊能力", "重生者——前世记忆+今生逆袭"]

  # 人物关系张力类型（来源：story-cog + tomato-novelist）
  relationship_tension_types:
    - "师徒暗中博弈"
    - "同门竞争"
    # 可选；不同题材差异大

# ========== I. 语言与文风（必填） ==========
language:
  # 叙述风格（来源：inkos + openclaw-novel-write）
  narrative_style: "白描快节奏"  # enum: 白描快节奏|细腻描写|诗意|冷峻克制|热血燃|诙谐

  # 疲劳词表（≥15词）（来源：inkos Genre Profile + onkos + novelist黑名单）
  fatigue_words:
    - "冷笑"   - "不屑"   - "嘲讽"
    - "猛然"   - "陡然"   - "瞬间"
    - "恐怖如斯" - "倒吸一口凉气" - "瞳孔猛缩"
    - "沉声"   - "淡淡道" - "森然"
    - "嘴角扬起" - "眼中闪过" - "浑身一震"
    - "不可思议" - "难以置信" - "前所未有"
    # 至少15个；不同题材共性高但细节不同

  # 句法红线（来源：inkos + my-novel-writer）
  syntax_rules:
    - "单句不超过50字"
    - "一段不超过4句（行动段落）/ 6句（描写段落）"
    - "对话句不超过20字（冷峻主角）；辅助角色可放宽至30字"
    # 可选；如不填写则使用通用默认

  # 禁止语言模式（来源：Advisor prompt + inkos）
  forbidden_patterns:
    - "不使用现代网络用语（玄幻/古风背景）"
    - "不使用英文缩写"

# ========== J. 章节要求（必填） ==========
chapter:
  # 字数范围（来源：tomato-novelist + inkos）
  word_count:
    min: 2200
    max: 2800
    target: 2500

  # 卷结构（来源：Planner prompt + inkos）
  volume:
    chapters_per_volume: 50  # 预估，可按实际创作调整
    volume_end_requirements:
      - "核心悬念阶段性收束"
      - "主角实力/地位有质的飞跃"
      - "至少回收3条伏笔"
      - "埋下下一卷的主悬念"

  # 章末要求（来源：Writer prompt + tomato-novelist）
  ending_requirements:
    - "必须有钩子（悬念/威胁/逆袭/情感/谜题至少1种）"
    - "不能以'未完待续'、'且听下回分解'结尾"
    - "钩子应自然嵌入最后1-2段，不应单列'下集预告'"

# ========== K. 审计配置（必填） ==========
audit:
  # 启用的审计维度（来源：Auditor prompt 40维设计）
  # true=启用, false=本题材不适用
  dimensions:
    # Layer 1: 脚本审计（13维）—— 全部通用，始终启用
    script_001_facts_consistency:       true
    script_002_character_state_sync:    true
    script_003_hook_fulfillment:        true
    script_004_hook_debt_check:         true
    script_005_relationship_tracking:   true
    script_006_pov_consistency:         true
    script_007_world_rules_compliance:  true
    script_008_timeline_check:          true
    script_009_location_continuity:     true
    script_010_item_tracking:           true
    script_011_power_level_check:       true  # 由 power_system.enabled 控制
    script_012_forbidden_words_check:   true
    script_013_memo_compliance:         true

    # Layer 2: 混合审计（8维）—— 按题材开关
    hybrid_014_character_state_contradiction: true
    hybrid_015_dialogue_consistency:          true
    hybrid_016_emotional_continuity:          true
    hybrid_017_scene_transition_quality:      true
    hybrid_018_pacing_rhythm:                 true
    hybrid_019_info_density:                  true
    hybrid_020_hook_embedding_quality:        true
    hybrid_021_ending_strength:               true

    # Layer 3: LLM审计（19维）—— 按题材开关
    llm_022_ooc_check:                true
    llm_023_dialogue_naturalness:     true
    llm_024_show_vs_tell:             true
    llm_025_power_breakdown:          true  # ⚠️ 仅 power_system.enabled=true 时启用
    llm_026_emotional_depth:          true
    llm_027_sensory_richness:         true
    llm_028_plot_logic:               true
    llm_029_character_motivation:     true
    llm_030_world_immersion:          true
    llm_031_prose_quality:            true
    llm_032_narrative_voice:          true
    llm_033_theme_consistency:        true
    llm_034_genre_authenticity:       true  # ⚠️ 题材核心维度——重度依赖 Genre Profile
    llm_035_subtext_quality:          true
    llm_036_anticlimax_detection:     true
    llm_037_cliche_detection:         true
    llm_038_description_balance:      true
    llm_039_inner_monologue_quality:  true
    llm_040_reader_emotional_arc:     true

  # 题材特定审计（来源：Auditor prompt "玄幻世界特有检查"）
  special_checks:
    # 仅当 power_system.enabled=true 时：
    - name: "力量体系一致性"
      description: "境界名称、跨境规则、突破条件是否与 power_system 定义一致"
      scoring: "一票否决——如违反 cross_level_rules 即 CRITICAL"
    # 仅当 romance.weight != "无" 时：
    # - name: "情感线节奏"
    #   description: "情感进展是否符合 romance.type 的预期节奏"
    #   scoring: "按维度 016 emotional_continuity 评估"

  # 章节类型权重调整（来源：Auditor prompt）
  chapter_type_weights:
    日常章:  { expectation: "标准", adjustment: 0 }
    过渡章:  { expectation: "可降低5分", adjustment: -5 }
    爆发章:  { expectation: "可降低5分（天然高难度）", adjustment: -5 }
    卷末章:  { expectation: "最严格", adjustment: 0, strict_dimensions: ["power_breakdown", "hook_fulfillment"] }

  # 评分弹性（来源：Auditor prompt）
  scoring_flexibility:
    - dimension: "genre_authenticity"
      note: "检查禁止概念和禁止口头禅时，需考虑角色教育背景（如乡野角色可能不知道某些概念）"

# ========== L. 平台（可选） ==========
platform:
  target: "番茄小说"  # enum: 番茄小说|起点中文网|微信读书|通用
  requirements:
    - "每章≥2000字（番茄推荐2200-2800）"
    - "敏感内容需要规避"
    # 不同平台差异大，由 human 在 Advisor Phase 1 指定

# ========== M. Advisor 工作流配置（内部使用） ==========
advisor_config:
  # Q1-Q5 问题清单（根据题材动态生成）
  # 此段由 Advisor 根据 genre.primary 自动选择模板
  question_template: "xuanhuan"  # 引用 genre_refactor/advisor_question_templates/xuanhuan.yaml
```

---

## 三、字段统计

| 分组 | 必填字段数 | 条件字段数 | 可选字段数 |
|------|----------|----------|----------|
| A 基础元信息 | 4 | 0 | 0 |
| B 题材定义 | 3 | 0 | 1 (sub_genres) |
| C 世界观规则 | 1 (core_laws) | 0 | 2 (forbidden_*) |
| D 力量体系 | 1 (enabled) | 4 | 0 |
| E 爽点节奏 | 10 (types ×10 + rhythm×6 + curve + density + humor) | 0 | 0 |
| F 情感线 | 1 (weight) | 1 (type) | 0 |
| G 悬念钩子 | 6 (hook_weights ×6 + mapping ×6 + intensity) | 0 | 0 |
| H 人物 | 1 (archetypes) | 0 | 1 (tension_types) |
| I 语言文风 | 15+ (fatigue_words) + 1 (style) | 0 | 2 (syntax, patterns) |
| J 章节要求 | 7 | 0 | 0 |
| K 审计配置 | 40 (dimensions) | 0 | 2 (special, weights, flexibility) |
| L 平台 | 0 | 0 | 2 |
| **合计** | **~90** | **5** | **10** |

---

## 四、与 Advisor 现有模板的变更对照

| 现有字段 | 变更 | 说明 |
|---------|------|------|
| `genre.primary` | 保留，扩展 enum | 原来只有"玄幻"示例 |
| `genre.forbidden` | 拆分为 `world_rules.forbidden_concepts` + `world_rules.forbidden_phrases` | 语义更精确 |
| `book_rules` | 拆分为 `world_rules.core_laws` + `language.forbidden_patterns` | 世界观规则和语言规则分离 |
| `fatigueWords` | 移到 `language.fatigue_words` | 归类到语言组 |
| `satisfactionTypes` | 扩展为 `satisfaction.types` 10 种模式 | 原来只覆盖玄幻常用 4-5 种 |
| (新增) `satisfaction.rhythm` | 新增 | 番茄平台节奏公式 |
| (新增) `satisfaction.emotion_curve` | 新增 | tomato-novelist + novelist |
| (新增) `satisfaction.combat_density` | 新增 | inkos |
| (新增) `romance` | 新增整组 | tomato-novelist 男女频差异 |
| (新增) `suspense` | 新增整组 | novelist + onkos |
| (新增) `characters.protagonist_archetypes` | 新增 | fiction-crafter |
| `powerSystem` | 扩展为 `power_system` 完整组 | 增加 levels, cross_level_rules, scoring_rubric |
| (新增) `audit` | 新增整组 | 40 维开关 + 题材特定检查 |
| (新增) `platform` | 新增 | 为多平台分发做准备 |
| (新增) `advisor_config` | 新增 | Advisor 内部使用的题材模板选择 |

---

## 五、Agent 注入方式

每个 Agent 启动时，从其输入段的"Genre Profile 注入"步骤读取本文件的具体 section：

| Agent | 需要的 Section | 用途 |
|-------|---------------|------|
| Advisor | 全部（生成；`advisor_config` 指导提问） | Phase 1-5 |
| Planner | B, C, D, E, F, G, H, J | 生成 ChapterMemo + 大纲 |
| Writer | E, F, G, H, I, J | 写作约束 + 钩子选择 + 疲劳词过滤 |
| Auditor | C, D, E, G, I, K | 审计维度选择 + 题材特定检查 |
| Reviser | D, G, I | 修订策略选择（STRUCTURAL 类型判断） |
| Polisher | G, I | 疲劳词替换 + 句法红线 + 文风一致性 |
