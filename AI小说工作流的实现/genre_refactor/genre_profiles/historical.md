# Genre Profile — 历史

```yaml
# ============================================================
# Genre Profile — 历史
# 版本：genre_profile_spec.md v1.0
# 参考：openclaw historical.md（大事不虚小事不拘 + 时代氛围）
# ============================================================

meta:
  book_title: "<书名>"
  genre_name: "historical"
  created: "2026-05-05"
  version: "1.0"

genre:
  primary: "历史"
  sub_genres: []
  world_basis: "混合"

world_rules:
  core_laws:
    - "大事不虚：重大历史事件的时间、结果、著名人物的基本设定不可改变"
    - "小事不拘：虚构的小人物、历史缝隙中的日常、合理细节填充可以虚构"
    - "时代氛围必须真实：服饰/语言/社会结构/价值观必须符合设定时代"
    - "角色的思想观念必须符合时代——不能用现代价值观直接批判古代角色"
    - "历史考据保证30%底线——不能出现明代物品在宋代、唐代官职在汉代"
  forbidden_concepts:
    - "现代科技/产品/制度概念出现在古代"
    - "现代政治术语/意识形态"
    - "违反时代的社会流动性（古代阶层流动性极低——不能'卖菜三年变首富'）"
  forbidden_phrases:
    - "科学的"
    - "民主/自由/平等（作为现代政治概念时）"

power_system:
  enabled: false

satisfaction:
  types:
    reversal:       { enabled: true,  description: "打脸——被轻视的谋士/将领展示才华" }
    breakthrough:   { enabled: false, description: "突破——不适用" }
    acquisition:    { enabled: true,  description: "获得权力/资源/人脉/情报" }
    revenge:        { enabled: true,  description: "复仇——国仇家恨" }
    recognition:    { enabled: true,  description: "身份揭露——隐藏的身份/血脉/才能被揭示" }
    romance:        { enabled: false }
    mystery_reveal: { enabled: true,  description: "阴谋揭露——朝堂/战场上的幕后真相" }
    comedy:         { enabled: false }
    horror:         { enabled: false }
    survival:       { enabled: true,  description: "战争/围城/政变中的生存" }
  rhythm:
    micro_relief:  { interval_chapters: "3-5", description: "小收获——一个计谋成功/一场小胜利" }
    minor_payoff:  { interval_chapters: "8-12", description: "中节点——朝堂博弈的关键回合/战役转折" }
    major_payoff:  { interval_chapters: "20-30", description: "大高潮——改朝换代/国战终局/身世大白" }
  emotion_curve: "渐进上升"
  combat_density: "中"
  humor_ratio: "点缀"

romance:
  weight: "辅助"
  type: null

suspense:
  intensity: "重要辅助"
  hook_weights:
    suspense:    7
    threat:      6
    reversal:    5
    romance:     0
    mystery:     7
    cliffhanger: 5
  hook_emotion_mapping:
    suspense:    "好奇——那个人的真实身份/真实目的？"
    threat:      "紧张——敌军压境/政敌逼近"
    reversal:    "震惊——立场反转/身份揭露"
    mystery:     "求解欲——历史背后的真相"
    cliffhanger: "迫切——关键时刻（战前/朝堂表决/密使到达前）"

characters:
  protagonist_archetypes:
    - "谋士/军师——以智谋在乱世中立足，运筹帷幄"
    - "寒门子弟——在门阀等级中逆流而上"
    - "没落贵族——背负家族荣耀在时代洪流中挣扎"
    - "穿越者——现代人用知识在历史中生存（架空历史）"
  relationship_tension_types:
    - "君臣之间的信任与猜忌"
    - "家族利益与个人抱负的冲突"
    - "敌国之间的惺惺相惜与战场对立"

language:
  narrative_style: "细腻描写"
  fatigue_words:
    - "不可思议" - "难以置信" - "匪夷所思"
    - "仿佛"   - "宛如"   - "似乎"
    - "突然"   - "猛然"   - "瞬间"
    - "不禁"   - "心中暗想"
  syntax_rules:
    - "适度古语——不是全文文言文，但对话和叙事应有时代语感"
    - "禁止现代口语渗入角色对话——'好的''没问题''OK'等"
    - "称谓必须符合时代：不同朝代/场合的称谓体系不同"
    - "度量衡/货币/时间描述必须使用当时的标准"
  forbidden_patterns:
    - "不使用现代网络用语"
    - "不使用现代科技术语"
    - "不使用现代政治/经济学术语"

chapter:
  word_count: { min: 2500, max: 3500, target: 3000 }
  volume:
    chapters_per_volume: 50
    volume_end_requirements:
      - "一个历史阶段的事件获得收束"
      - "主角地位/权力有质的飞跃或坠落"
      - "至少揭示一个隐藏的历史真相"
      - "时代格局发生不可逆的变化"
  ending_requirements:
    - "必须有钩子——新威胁/新阴谋/新情报"
    - "避免'欲知后事如何'式结尾——用具体信息暗示下一章的冲突"

audit:
  dimensions:
    script_001_facts_consistency:       true
    script_002_character_state_sync:    true
    script_003_hook_fulfillment:        true
    script_004_hook_debt_check:         true
    script_005_relationship_tracking:   true
    script_006_pov_consistency:         true
    script_007_world_rules_compliance:  true    # 时代考据——核心
    script_008_timeline_check:          true    # 历史时间线——关键
    script_009_location_continuity:     true
    script_010_item_tracking:           true
    script_011_power_level_check:       false
    script_012_forbidden_words_check:   true
    script_013_memo_compliance:         true
    hybrid_014_character_state_contradiction: true
    hybrid_015_dialogue_consistency:          true    # 时代语感一致性
    hybrid_016_emotional_continuity:          true
    hybrid_017_scene_transition_quality:      true
    hybrid_018_pacing_rhythm:                 true
    hybrid_019_info_density:                  true
    hybrid_020_hook_embedding_quality:        true
    hybrid_021_ending_strength:               true
    llm_022_ooc_check:                true
    llm_023_dialogue_naturalness:     true    # 是否符合时代语感
    llm_024_show_vs_tell:             true
    llm_025_power_breakdown:          false
    llm_026_emotional_depth:          true
    llm_027_sensory_richness:         true
    llm_028_plot_logic:               true
    llm_029_character_motivation:     true    # 是否符合时代价值观
    llm_030_world_immersion:          true    # 时代氛围
    llm_031_prose_quality:            true
    llm_032_narrative_voice:          true
    llm_033_theme_consistency:        true
    llm_034_genre_authenticity:       true    # 时代准确性——核心维度
    llm_035_subtext_quality:          true
    llm_036_anticlimax_detection:     true
    llm_037_cliche_detection:         true
    llm_038_description_balance:      true
    llm_039_inner_monologue_quality:  true
    llm_040_reader_emotional_arc:     true
  special_checks:
    - name: "时代考据一致性"
      description: "物品/服饰/称谓/度量衡/官职/社会制度是否与设定时代一致"
      scoring: "明代物品出现在宋代→WARNING；错误的朝代称谓→WARNING"
    - name: "思想观念时代性"
      description: "角色的思想观念是否超越时代"
      scoring: "角色用现代价值观直接批判古代制度→INFO（架空历史可放宽）"
  chapter_type_weights:
    日常章:  { expectation: "标准", adjustment: 0 }
    过渡章:  { expectation: "可降低5分", adjustment: -5 }
    爆发章:  { expectation: "标准", adjustment: 0 }
    卷末章:  { expectation: "最严格", adjustment: 0 }
  scoring_flexibility:
    - "架空历史（如《琅琊榜》类型）对具体朝代考据可放宽，但时代氛围仍需维持"

platform:
  target: "起点中文网"
  requirements:
    - "历史分类——需标注正史向/戏说向/架空历史"
    - "涉及真实历史人物需谨慎——避免对真实人物的负面描写"

golden_finger:
  ceiling: null
  cost: null
  trigger_condition: null
  growth_path: null
```

---

## 题材禁忌（来源：openclaw historical）

- 重大历史事件的时间/结果被随意改变——"大事不虚"是底线
- 著名历史人物的基本设定（生卒年/功绩/定位）被颠覆
- 时代大背景错误——宋代出现火枪/唐代使用明代官制
- 用现代价值观直接批判古代角色——角色的思想观念必须符合时代
- 历史人物沦为背景板——如果写了真实历史人物，就不能让他们只是"路过的NPC"

## 时代考据规则（来源：openclaw historical + chinese-novelist）

### 大事不虚，小事不拘
- 大事（不可虚构）：重大历史事件/著名人物基本设定/时代大背景
- 小事（可以虚构）：虚构小人物/历史缝隙中的日常/合理细节填充/史书未载的"可能性"
- 考据保证30%底线——不能出现明代物品在宋代、唐代官职在汉代的硬伤

### 时代氛围维度
- 角色的思想观念是否符合时代——不能用现代价值观直接批判古代
- 物品/服饰/称谓是否准确——称谓因朝代/场合而异
- 社会阶层是否合理——古代阶层流动性极低
- 日常生活细节是否准确——照明/交通/通讯方式的时代限制
- 语言是否有时代感——适度古语，不是全文文言文，但不能出现现代口语

## 语言铁律（来源：chinese-novelist 白描 + inkos）

- 适度古语：对话需有时代语感——不同阶层角色的用词不一样
- 称谓严格按时代：宋代"相公"=对官员的尊称，不是"丈夫"
- 禁止：现代网络用语、科技术语、政治/经济学术语
- 白描为主——"她坐在窗边绣花"比"她优雅地坐在窗前做着精致的手工"好一万倍
- 时代的质感通过细节传达——一盏茶的冲泡方式、一件衣服的规矩、一间屋子的陈设

## 叙事指导（来源：openclaw historical + chinese-novelist）

时代氛围是历史小说的灵魂——读者来读历史小说不只是为了剧情，更是为了"走入那个时代"。

政治大背景通过微观生活折射——不要写"朝堂之上党争激烈"，写角色今天买菜发现盐价涨了一倍。用角色的菜篮子讲朝堂上的风云。

### 朝代选择的影响
- 正史向：严格的朝代考据——读者会检查每一个细节
- 戏说向：架空部分历史——主要人物和大事件不变，细节可以发挥
- 架空历史：借鉴历史但完全虚构——考据要求最低，但时代氛围仍需维持

### 节奏特点
- 历史小说的节奏比爽文慢——读者来"沉浸"不是来"冲刺"
- 战争/政变是爆发点——平时是朝堂博弈、人情往来、日常生活的质地
- 每个人物都应该有除了"推动剧情"之外的生活细节——这是时代感的来源
