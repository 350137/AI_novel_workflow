# Genre Profile — 科幻

```yaml
# ============================================================
# Genre Profile — 科幻
# 版本：genre_profile_spec.md v1.0
# 参考：inkos sci-fi + openclaw genre-knowledge + story-cog 世界观构建
# ============================================================

meta:
  book_title: "<书名>"
  genre_name: "sci_fi"
  created: "2026-05-05"
  version: "1.0"

genre:
  primary: "科幻"
  sub_genres: []
  world_basis: "近未来"

world_rules:
  core_laws:
    - "已确立的科技规则不可为剧情便利而改变——物理/技术一旦建立必须保持一致性"
    - "每项技术必须有明确的局限性和副作用——技术解决问题，也创造新问题"
    - "如果是硬科幻：科学原理必须可解释，推断必须合理（读者会验证）"
    - "如果是太空歌剧：科学可以软，但内部规则必须在全叙事中保持一致"
    - "技术不是万能解——腐败/情感/人性贪婪是无法用技术修复的问题"
  forbidden_concepts:
    - "无视已确立科技规则的'惊喜'技术"
    - "当代人物穿越到数百年后但行为和语言毫无变化"
  forbidden_phrases:
    - "这不科学"
    - "魔法般的"

power_system:
  enabled: false

satisfaction:
  types:
    reversal:       { enabled: false, description: "打脸——不适用" }
    breakthrough:   { enabled: true,  description: "技术突破——新发现/新发明/新理解" }
    acquisition:    { enabled: true,  description: "获得资源/技术/数据/盟友" }
    revenge:        { enabled: false }
    recognition:    { enabled: true,  description: "发现/理论的确认——被科学界/军方/外星文明认可" }
    romance:        { enabled: false }
    mystery_reveal: { enabled: true,  description: "谜题揭晓——宇宙的真相/外星文明的目的/技术的本质" }
    comedy:         { enabled: false }
    horror:         { enabled: true,  description: "面对未知的恐惧——宇宙的浩瀚/技术的反噬/异形的威胁" }
    survival:       { enabled: true,  description: "在极端环境/外星世界/太空灾难中生存" }
  rhythm:
    micro_relief:  { interval_chapters: "2-3", description: "小发现/小突破——一个技术应用或新信息" }
    minor_payoff:  { interval_chapters: "4-6", description: "中揭示——一个谜题的阶段性答案或关键资源获取" }
    major_payoff:  { interval_chapters: "10-15", description: "大高潮——首次接触/技术革命/文明级别的转折" }
  emotion_curve: "渐进上升"
  combat_density: "中"
  humor_ratio: "点缀"

romance:
  weight: "辅助"
  type: null

suspense:
  intensity: "重要辅助"
  hook_weights:
    suspense:    9
    threat:      7
    reversal:    3
    romance:     0
    mystery:     8
    cliffhanger: 5
  hook_emotion_mapping:
    suspense:    "好奇——宇宙的真相是什么？"
    threat:      "紧张——技术/异形/环境的威胁"
    reversal:    "震惊——之前的假设全错了"
    mystery:     "求解欲——那个信号/那个发现意味着什么？"
    cliffhanger: "迫切——关键时刻中断"

characters:
  protagonist_archetypes:
    - "科学家/工程师——用理性和知识面对未知，技术是武器也是枷锁"
    - "探索者/宇航员——在星际边疆发现不该发现的东西"
    - "幸存者——在末日/外星/深层空间中挣扎求生"
    - "反叛者——对抗技术垄断/AI统治/星际帝国的个人"
  relationship_tension_types:
    - "人类与AI/外星文明的信任建立"
    - "科学伦理与人性的冲突"
    - "星际政治中的忠诚与背叛"

language:
  narrative_style: "冷峻克制"
  fatigue_words:
    - "不可思议" - "难以置信" - "匪夷所思" - "前所未有"
    - "突然"   - "瞬间"   - "猛然"   - "陡然"
    - "仿佛"   - "宛如"   - "似乎"   - "好像"
    - "不知为何" - "莫名其妙"
  syntax_rules:
    - "技术解释通过角色互动展示，不通过教科书条目"
    - "硬科幻：每次技术揭示必须与情节关键节点绑定"
    - "禁止在非情节关键时刻倾倒科学/技术说明"
    - "动作场景基于已建立的物理/技术规则——不能出现'惊喜'能力"
  forbidden_patterns:
    - "不使用魔法/玄幻术语解释科技"
    - "不使用'科学家发现了一个惊人的秘密'这种空泛总结"

chapter:
  word_count: { min: 2200, max: 3000, target: 2600 }
  volume:
    chapters_per_volume: 40
    volume_end_requirements:
      - "一个核心谜题或科学问题获得阶段性解答"
      - "主角对宇宙/技术/文明的理解发生质的飞跃"
      - "至少揭示一个改变游戏规则的新信息"
  ending_requirements:
    - "必须有钩子——新发现/新威胁/新谜题"
    - "科学发现型的钩子优先——'这个数据不应该存在'"

audit:
  dimensions:
    script_001_facts_consistency:       true
    script_002_character_state_sync:    true
    script_003_hook_fulfillment:        true
    script_004_hook_debt_check:         true
    script_005_relationship_tracking:   true
    script_006_pov_consistency:         true
    script_007_world_rules_compliance:  true   # 科技规则一致性——核心
    script_008_timeline_check:          true
    script_009_location_continuity:     true
    script_010_item_tracking:           true
    script_011_power_level_check:       false
    script_012_forbidden_words_check:   true
    script_013_memo_compliance:         true
    hybrid_014_character_state_contradiction: true
    hybrid_015_dialogue_consistency:          true
    hybrid_016_emotional_continuity:          true
    hybrid_017_scene_transition_quality:      true
    hybrid_018_pacing_rhythm:                 true
    hybrid_019_info_density:                  true
    hybrid_020_hook_embedding_quality:        true
    hybrid_021_ending_strength:               true
    llm_022_ooc_check:                true
    llm_023_dialogue_naturalness:     true
    llm_024_show_vs_tell:             true
    llm_025_power_breakdown:          false
    llm_026_emotional_depth:          true
    llm_027_sensory_richness:         true
    llm_028_plot_logic:               true    # 科幻：逻辑漏洞是致命伤
    llm_029_character_motivation:     true
    llm_030_world_immersion:          true
    llm_031_prose_quality:            true
    llm_032_narrative_voice:          true
    llm_033_theme_consistency:        true
    llm_034_genre_authenticity:       true    # 科技规则一致性 + 科学合理性
    llm_035_subtext_quality:          true
    llm_036_anticlimax_detection:     true
    llm_037_cliche_detection:         true
    llm_038_description_balance:      true
    llm_039_inner_monologue_quality:  true
    llm_040_reader_emotional_arc:     true
  special_checks:
    - name: "科技规则一致性"
      description: "已确立的科技/物理规则是否被后续章节违反？技术是否有突然的、无解释的能力变化？"
      scoring: "如无铺垫的技术能力变化→CRITICAL"
  chapter_type_weights:
    日常章:  { expectation: "标准", adjustment: 0 }
    过渡章:  { expectation: "可降低5分", adjustment: -5 }
    爆发章:  { expectation: "标准（发现/揭示章）", adjustment: 0 }
    卷末章:  { expectation: "最严格", adjustment: 0 }
  scoring_flexibility:
    - "genre_authenticity——硬科幻与太空歌剧的技术严格程度不同，根据设定判断"

platform:
  target: "起点中文网"
  requirements:
    - "科幻分类：标签准确（硬科幻/太空歌剧/赛博朋克/末世等）"
    - "科技描写需有基本科学素养——起点科幻读者对硬伤容忍度低"

golden_finger:
  ceiling: null
  cost: null
  trigger_condition: null
  growth_path: null
```

---

## 题材禁忌（来源：inkos sci-fi + openclaw genre-knowledge）

- 科技规则为剧情便利而改变——一旦物理/技术建立，必须保持一致性
- 技术解决一切——每项技术必须有局限；引入技术无法修复的问题（腐败/情感/人性贪婪）
- 在非情节关键时刻倾倒科学/技术说明
- 无视技术的逻辑后果——FTL/AI/生物技术都应有社会层面的影响
- 角色在数百年后的未来，但行为和语言如同当代人
- Info-dumping——用教科书式段落解释科学概念

## 科技一致性规则（来源：inkos sci-fi Tech Consistency）

- 每项技术必须有明确的局限性和副作用
- 新技术创造新问题——不只解决旧问题
- 硬科幻：解释科学，使其合理，建立后果——读者会验证
- 太空歌剧：科学可以软，但内部规则必须在全叙事中保持一致
- 技术通过角色互动展示，不通过教科书条目
- 时代考据要求：参考真实科学正确，推断合理
- 技术揭示只在情节关键节点——绝不为了炫耀而倾倒规格

## 语言铁律（来源：inkos sci-fi + story-cog）

- 技术解释融入行动和对话——✗"量子纠缠通讯的原理是..."→✓"她看了一眼通讯器的延迟读数——3.7秒。量子纠缠。有人在窃听。"
- 硬科幻：精确的术语和合理的推断——读者会检查每一个数字
- 太空歌剧：科学可以简化，但不能前后矛盾
- 禁止在动作场景中插入长篇技术说明
- 感官描写服务于"异世界感"——外星环境的陌生感通过五感传达

## 叙事指导（来源：inkos sci-fi + story-cog world building）

世界构建通过行动浮现，不通过说明段落。技术揭示与情节关键节点绑定。政治/探索弧线与动作每2-4章交替。

硬科幻：逻辑问题解决驱动节奏——每章应推进理解或创造新约束。太空歌剧：史诗规模需要政治/人际弧线在动作序列之间。

探索章节通过角色体验建立奇观和世界构建。行动场景基于已建立的物理/技术规则——不能出现"惊喜"能力。

### 科幻的独特张力
- 人类vs技术：我们创造的东西正在失控
- 人类vs未知：宇宙的浩瀚和冷漠
- 人类vs人类：在新技术面前，人性不变
- 每个技术突破都应是"双刃剑"——既解决问题又创造新问题
