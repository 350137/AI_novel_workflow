# Genre Profile — 仙侠言情

```yaml
# ============================================================
# Genre Profile — 仙侠·言情
# 版本：genre_profile_spec.md v1.0
# 参考：tomato-novelist 女频节奏 + story-cog 情感线设计 + inkos romance genre
# 日期：2026-05-04
# ============================================================

meta:
  book_title: "<书名>"
  genre_name: "xianxia_romance"
  created: "2026-05-04"
  version: "1.0"

genre:
  primary: "仙侠"
  sub_genres: ["言情", "虐恋", "三世轮回"]
  world_basis: "远古神话"

world_rules:
  core_laws:
    - "因果法则：任何改变命运的行为都有对应的果报——这是世界观的核心机制"
    - "三世轮回：前世今生的记忆不会自然恢复——必须通过特定触发条件（法器/地点/关键时刻）"
    - "仙凡之隔：仙人不能直接干涉凡间事务——必须通过化身/梦境/预言等方式"
    - "情感即力量：真挚的情感可以跨越仙凡、生死、轮回的界限——但每次跨越都有代价"
    - "天道不容私情：仙人相恋违反天道，必须付出代价（失去法力/打入轮回/永世不得相见）"
  forbidden_concepts:
    - "现代科技产品名称"
    - "现代政治概念"
  forbidden_phrases:
    - "这不科学"
    - "科学的"
    - "系统化"

power_system:
  enabled: true
  name: "灵力层次/仙阶"
  levels:
    - "凡人（无灵力）"
    - "筑基（初窥灵力）"
    - "金丹（灵力凝丹）"
    - "元婴（灵婴初成）"
    - "化神（神念合一）"
    - "渡劫（天劫临身）"
    - "大乘（半步真仙）"
    - "真仙（位列仙班）"
    - "上仙（执掌一方）"
    - "帝君（天道之下）"
  cross_level_rules:
    - "仙凡之间不可直接交互——高仙阶对低仙阶的干涉有代价"
    - "为情违反天道→降低仙阶或打入轮回"
    - "修为突破需要'悟'——情感经历可以是悟的触发，但不是悟本身"
  scoring_rubric:
    score_10: "灵力体系一致，因果法则贯彻，仙阶转换有明确代价"
    score_7_9: "基本一致，1处小瑕疵"
    score_4_6: "1处明显违反——如高仙阶无故干涉凡间"
    score_1_3: "多处违反仙凡规则"
    score_0: "体系完全被忽视"

satisfaction:
  types:
    reversal:       { enabled: false, description: "打脸——仙侠言情不以此为主" }
    breakthrough:   { enabled: true,  description: "修为突破——但通常与情感转折同步" }
    acquisition:    { enabled: true,  description: "获得机缘/法宝——常与回忆/前世触发绑在一起" }
    revenge:        { enabled: false, description: "复仇——不是主要爽点" }
    recognition:    { enabled: true,  description: "身份揭露——前世身份/真实仙阶被揭露" }
    romance:        { enabled: true,  description: "情感进展——核心爽点。甜→虐→更甜的三段式" }
    mystery_reveal: { enabled: true,  description: "前世揭秘——前世发生了什么，为什么被分离" }
    comedy:         { enabled: false, description: "搞笑——点缀" }
    horror:         { enabled: false, description: "恐怖——不适用" }
    survival:       { enabled: true,  description: "为情/为守护而战斗的绝境" }
  rhythm:
    micro_relief:  { interval_chapters: "1-2", description: "小甜蜜——互动小细节/暧昧/吃醋" }
    minor_payoff:  { interval_chapters: "3-5", description: "中情感节点——告白/误会/和好" }
    major_payoff:  { interval_chapters: "8-12", description: "大高潮——前世记忆恢复/为爱逆天/生离死别" }
  emotion_curve: "波浪式"
  combat_density: "中"
  humor_ratio: "辅助"

romance:
  weight: "主线"
  type: "虐恋"  # 甜宠/虐恋/日久生情/破镜重圆/欢喜冤家/禁忌

suspense:
  intensity: "重要辅助"
  hook_weights:
    suspense:    7    # "他们的前世到底发生了什么？"
    threat:      5    # "天道会怎样惩罚他们？"
    reversal:    3
    romance:     10   # "他们会在一起吗？"
    mystery:     6    # "那个梦/那片景/那首歌意味着什么？"
    cliffhanger: 5
  hook_emotion_mapping:
    suspense:    "好奇值↑——前世之谜"
    threat:      "担忧值↑——天道不容"
    reversal:    "心碎/惊喜——他/她竟然是..."
    romance:     "心动值↑/心碎值↑——甜和虐交织"
    mystery:     "求解欲↑——记忆碎片"
    cliffhanger: "急切——关键时刻中断"

characters:
  protagonist_archetypes:
    - "被贬仙子——因前世恋情被贬下凡，轮回多次后记忆开始觉醒"
    - "痴情守护者——看似普通但暗中守护女主数世，每世付出巨大代价"
    - "双重身份——凡间一个身份+仙界一个身份，两界之间的拉扯"
    - "命定之人——天道安排的天命但主角选择了不同的道路"
  relationship_tension_types:
    - "三生三世——前世相爱但分离，今生相遇但不识，来世能否相守？"
    - "仙凡禁忌——相恋违反天道，每一步都在对抗天命"
    - "记忆不对等——一人觉醒前世记忆但另一人没有，信息差制造虐感"
    - "情敌即天命——情敌是天道的化身/天道的执行者"

language:
  narrative_style: "细腻描写"
  fatigue_words:
    - "泪如雨下" - "心如刀绞" - "撕心裂肺" - "痛彻心扉"
    - "苦笑"     - "凄然"   - "决绝"     - "颤声"
    - "喉头一甜" - "眼前一黑" - "浑身冰凉" - "指尖微颤"
    - "深深望"   - "转身离去" - "沉默良久"
    - "一眼万年" - "命中注定"
  syntax_rules:
    - "单句不超过50字"
    - "情感场景允许稍长的句群——但一段不超过8句"
    - "对话中情感克制——用动作和细节传达情绪，而非对话中直说'我爱你/我恨你'"
    - "感官描写丰富——触觉/温度/气味在情感场景中尤其重要"
  forbidden_patterns:
    - "不使用现代网络用语"
    - "不使用英文缩写"
    - "不能'眼泪像断了线的珠子'——情感描写需克制而有力量"
    - "不能'心里一痛'——直接写身体反应（手指泛白/呼吸停滞）"

chapter:
  word_count: { min: 2000, max: 2800, target: 2400 }
  volume:
    chapters_per_volume: 40
    volume_end_requirements:
      - "一段情感弧线收束——甜/虐的一个完整周期完成"
      - "前世记忆恢复至少一个重要片段"
      - "人物关系发生不可逆变化——告白/分离/选择"
      - "下一卷的情感张力线布局——新的障碍/更大的代价"
  ending_requirements:
    - "必须有钩子——情感钩子优先（关系变化/新角色入场/记忆觉醒）"
    - "在情感最浓处断章——吻/那句没说出口的话/转身离开的背影"
    - "不预告——情感钩子靠情节本身，不靠'下章预告'"

audit:
  dimensions:
    script_001_facts_consistency:       true
    script_002_character_state_sync:    true
    script_003_hook_fulfillment:        true
    script_004_hook_debt_check:         true
    script_005_relationship_tracking:   true   # 言情：关系追踪是核心
    script_006_pov_consistency:         true
    script_007_world_rules_compliance:  true
    script_008_timeline_check:          true
    script_009_location_continuity:     true
    script_010_item_tracking:           true
    script_011_power_level_check:       true
    script_012_forbidden_words_check:   true
    script_013_memo_compliance:         true
    hybrid_014_character_state_contradiction: true
    hybrid_015_dialogue_consistency:          true
    hybrid_016_emotional_continuity:          true   # 言情：情感连续性是核心
    hybrid_017_scene_transition_quality:      true
    hybrid_018_pacing_rhythm:                 true   # 言情：甜虐节奏是关键
    hybrid_019_info_density:                  true
    hybrid_020_hook_embedding_quality:        true
    hybrid_021_ending_strength:               true
    llm_022_ooc_check:                true    # 言情：OOC是致命伤
    llm_023_dialogue_naturalness:     true
    llm_024_show_vs_tell:             true
    llm_025_power_breakdown:          true    # 启用——有仙阶体系
    llm_026_emotional_depth:          true    # 言情：情感深度是核心维度
    llm_027_sensory_richness:         true
    llm_028_plot_logic:               true
    llm_029_character_motivation:     true
    llm_030_world_immersion:          true
    llm_031_prose_quality:            true
    llm_032_narrative_voice:          true
    llm_033_theme_consistency:        true
    llm_034_genre_authenticity:       true
    llm_035_subtext_quality:          true    # 言情：潜台词/暗示是情感描写的核心
    llm_036_anticlimax_detection:     true
    llm_037_cliche_detection:         true
    llm_038_description_balance:      true
    llm_039_inner_monologue_quality:  true
    llm_040_reader_emotional_arc:     true    # 言情：读者情感弧线是最重要的维度
  special_checks:
    - name: "仙凡法则一致性"
      description: "仙凡交互是否符合 world_rules 定义的代价和限制"
      scoring: "如高仙阶无故直接干涉凡间→WARNING"
    - name: "情感节奏有效性"
      description: "甜/虐交替是否符合 romance.type 的预期节奏"
      scoring: "连续>5章无情感推进→WARNING；虐的长度超过预期但无'觉醒时刻'→WARNING"
    - name: "女频叙事特征"
      description: "是否具备女频读者期待的叙事特征（细腻情感描写、关系推进、暧昧空间）"
      scoring: "如连续3章纯战斗/修炼而零情感互动→INFO（不扣分但标记）"
  chapter_type_weights:
    日常章:  { expectation: "标准", adjustment: 0 }
    过渡章:  { expectation: "可降低5分", adjustment: -5 }
    爆发章:  { expectation: "可降低5分（情感爆发章天然高难度）", adjustment: -5 }
    卷末章:  { expectation: "最严格", adjustment: 0 }
  scoring_flexibility:
    - "emotional_depth 和 reader_emotional_arc ——在情感爆发章期望分数可降低3分（高难度场景）"
    - "genre_authenticity 检查——女频仙侠允许更自由的世界观设定（核心是情感，世界观为情感服务）"

platform:
  target: "番茄小说"
  requirements:
    - "每章≥2000字（番茄推荐2000-2800）"
    - "女频标签：仙侠+言情+虐恋"
    - "番茄女频读者对情感节奏敏感——虐的密度要精准控制"

golden_finger:
  ceiling: null  # 仙侠言情中金手指通常不是重点
  cost: null
  trigger_condition: null
  growth_path: null
```

---

## 题材禁忌（来源：inkos 仙侠 + openclaw romance）

- 主角为推剧情突然仁慈、犯蠢
- 修为无铺垫跳跃式突破
- 法宝凭空出现解决危机
- 天道规则前后矛盾
- 用"大道无形""天道感应"跳过具体修炼过程
- 同质资源不写衰减默认全额结算
- 风格混入都市腔、游戏系统播报腔

## 修炼规则（来源：inkos 仙侠）

- 境界突破必须有积累过程：悟道、丹药、战斗领悟、机缘——不能"坐着就突破了"
- 同质资源重复炼化必须写明衰减
- 法宝体系分品级，使用有代价（灵力、寿元、因果）
- 金手指/功法四维约束：能力上限/附加代价/触发条件/成长路径
- 天道规则一旦设定不可违反，除非有明确的特殊机制
- 跨大境界突破需要天劫或特殊条件

## 言情特定规则（来源：openclaw romance + chinese-novelist dialogue）

### 关系弧线是主情节
- 删除关系线后故事不成立——每个重大情节都同时推进关系
- 读者更关心"他们会在一起吗"而非"发生了什么"
- 情感节奏点（必备）：初次相遇→障碍建立→亲密加深→关系危机→黑暗时刻→大团圆(HEA)

### 仙侠与言情的融合
- 修炼突破与情感转折应同步——不是"修炼一段然后谈一段恋爱"
- 天道与情感的冲突是仙侠言情的核心张力——"为情逆天"是最高潮
- 三世轮回的节奏：每一世的情感发展阶段需不同（甜/虐/遗憾递进）

### 对话特征
- 告白场景：迟疑、停顿、寻找词语
- 暧昧场景：双关语、试探、暗示、话里有话
- 告别场景：未尽之言、克制、表面平静下的暗涌

## 语言铁律（来源：inkos 仙侠 + tomato-novelist 女频）

- 情感描写需克制而有力量——不能"眼泪像断了线的珠子"
- 不能"心里一痛"——直接写身体反应（手指泛白/呼吸停滞）
- 对话中情感克制——用动作和细节传达情绪，而非对话中直说"我爱你/我恨你"
- 感官描写丰富——触觉/温度/气味在情感场景中尤其重要
- 女频读者对AI味极度敏感——成语和四字格律需严格控制

## 叙事指导（来源：inkos 仙侠 + openclaw romance）

修炼与悟道是叙事核心，但必须融入情感线而非独立说教。

仙侠世界的规则感与情感的不可控性之间的张力是最大看点——"天道说不能在一起，但我偏要"。

门派政治、宗门博弈是布局手段。战斗以法术、法宝、阵法为核心，但在情感高潮时——战斗是为保护所爱之人。

甜虐节奏：每3-5章甜一次（小心动/小暧昧），每8-12章虐一次（误会/阻碍/危机），卷末大甜或大虐（情感收束或为情逆天）。连续>5章无情感推进→读者弃书预警。
