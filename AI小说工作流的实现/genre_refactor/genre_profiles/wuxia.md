# Genre Profile — 武侠

```yaml
# ============================================================
# Genre Profile — 武侠
# 版本：genre_profile_spec.md v1.0
# 参考：openclaw wuxia.md + inkos xianxia + entity-keywords 武侠配置
# ============================================================

meta:
  book_title: "<书名>"
  genre_name: "wuxia"
  created: "2026-05-05"
  version: "1.0"

genre:
  primary: "武侠"
  sub_genres: []
  world_basis: "架空异界"

world_rules:
  core_laws:
    - "没有无敌的武功——所有武功有克制关系，相生相克"
    - "内力/真气有限——消耗必须合理，不是无限能量"
    - "绝招有代价——使用后虚弱/反噬/冷却，不能连续使用"
    - "江湖规则高于朝堂规则——恩怨分明、长幼有序、以武会友"
    - "天赋+努力+机缘=成长——缺一不可"
  forbidden_concepts:
    - "现代科技产品"
    - "现代政治概念"
    - "修仙/玄幻式的飞升成仙（武侠的天花板是'武林神话'级别）"
  forbidden_phrases:
    - "这不科学"

power_system:
  enabled: true
  name: "武学层次"
  levels:
    - "三流——普通江湖人的水平"
    - "二流——门派精英的水平"
    - "一流——掌门/长老的水平"
    - "后天——内功登堂入室"
    - "先天——真气贯通，百脉俱通"
    - "宗师——开宗立派"
    - "大宗师——武林泰斗"
    - "绝顶——武林神话"
  cross_level_rules:
    - "以弱胜强需有计谋/环境/克制武功——不能靠'意志力'"
    - "境界突破需要：内功积累+招式领悟+实战磨砺——三者缺一不可"
    - "重伤后恢复期≥1章——不能下章就满状态"
  scoring_rubric:
    score_10: "武学体系严格一致，境界差异有可感知的强弱对比，绝招代价始终如一"
    score_7_9: "基本一致，1处小瑕疵"
    score_4_6: "1处明显违反——如低境界轻松战胜高境界但无合理战术解释"
    score_1_3: "多处违反武学规则"
    score_0: "体系完全被忽视"

satisfaction:
  types:
    reversal:       { enabled: true,  description: "打脸——被轻视的武者展露真正实力" }
    breakthrough:   { enabled: true,  description: "武功突破——领悟新招式/内功精进" }
    acquisition:    { enabled: true,  description: "获得秘籍/神兵/灵药——江湖机缘" }
    revenge:        { enabled: true,  description: "复仇——为师父/师门/家人报仇" }
    recognition:    { enabled: true,  description: "身份揭露——隐藏的高手身份被揭示" }
    romance:        { enabled: false, description: "情感——辅助线，不是主线" }
    mystery_reveal: { enabled: true,  description: "身世揭秘/阴谋揭露——江湖背后的阴谋" }
    comedy:         { enabled: false }
    horror:         { enabled: false }
    survival:       { enabled: true,  description: "绝境求生——重伤/被围困/绝地反击" }
  rhythm:
    micro_relief:  { interval_chapters: "2-3", description: "小交手/小领悟——展示新学招式" }
    minor_payoff:  { interval_chapters: "5-8", description: "中战斗——击败阶段性对手/获得重要秘籍" }
    major_payoff:  { interval_chapters: "15-20", description: "大对决——门派大战/复仇决战/武林大会" }
  emotion_curve: "过山车式"
  combat_density: "高"
  humor_ratio: "点缀"

romance:
  weight: "辅助"
  type: null

suspense:
  intensity: "重要辅助"
  hook_weights:
    suspense:    7
    threat:      6
    reversal:    8
    romance:     0
    mystery:     5
    cliffhanger: 6
  hook_emotion_mapping:
    suspense:    "好奇——这个神秘高手的真实身份？"
    threat:      "紧张——追兵/仇家逼近"
    reversal:    "期待——被小看的主角何时出手？"
    mystery:     "求解——幕后黑手的真实目的？"
    cliffhanger: "迫切——关键时刻中断"

characters:
  protagonist_archetypes:
    - "复仇者——背负师门/家族血仇，在江湖中寻找仇人"
    - "无名小子——出身底层的武学奇才，机缘巧合获得传承"
    - "隐世高手——曾为绝顶高手，因故退隐，被江湖恩怨重新拉回"
    - "侠之大者——心怀天下的游侠，劫富济贫、惩恶扬善"
  relationship_tension_types:
    - "师徒恩情——师父的期望与主角的独立选择"
    - "惺惺相惜的对决——与旗鼓相当的对手既敌对又相互尊重"
    - "正邪之间的灰色地带——亦正亦邪的角色挑战主角的道德判断"
    - "帮派/门派忠诚与个人良知的冲突"

language:
  narrative_style: "白描快节奏"
  fatigue_words:
    - "冷笑"   - "不屑"   - "嘲讽"   - "猛然"   - "陡然"
    - "瞬间"   - "不可思议" - "难以置信" - "倒吸凉气"
    - "沉声"   - "淡淡道" - "森然"   - "眼中闪过"
    - "仿佛"   - "不禁"   - "宛如"   - "竟然"
  syntax_rules:
    - "单句不超过50字"
    - "动作场景用短句（5-15字），白描为主，不作渲染"
    - "一招一式有名称，但不过度渲染——'黑虎掏心'足矣，不必写成'他使出一招黑虎掏心如同猛虎下山般——'"
    - "禁止西式从句堆叠——中文语感，主谓宾短促有力"
  forbidden_patterns:
    - "不使用现代网络用语"
    - "不使用英文缩写"
    - "不使用玄幻/修仙术语（灵气/渡劫/飞升等）——这是武侠，不是仙侠"

chapter:
  word_count: { min: 2200, max: 2800, target: 2500 }
  volume:
    chapters_per_volume: 40
    volume_end_requirements:
      - "主角武学层次有质的飞跃——至少提升1-2个层次"
      - "一条主线恩怨获得阶段性了结"
      - "江湖格局发生不可逆的变化"
      - "埋下下一卷的新恩怨/新阴谋"
  ending_requirements:
    - "必须有钩子——新敌人/新阴谋/新秘籍线索"
    - "如本章有战斗——战后必须有反应（伤势/旁人的震惊/战利品）"

audit:
  dimensions:
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
    script_011_power_level_check:       true
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
    llm_025_power_breakdown:          true    # 武学体系一致性
    llm_026_emotional_depth:          true
    llm_027_sensory_richness:         true
    llm_028_plot_logic:               true
    llm_029_character_motivation:     true
    llm_030_world_immersion:          true
    llm_031_prose_quality:            true
    llm_032_narrative_voice:          true
    llm_033_theme_consistency:        true
    llm_034_genre_authenticity:       true
    llm_035_subtext_quality:          true
    llm_036_anticlimax_detection:     true
    llm_037_cliche_detection:         true
    llm_038_description_balance:      true
    llm_039_inner_monologue_quality:  true
    llm_040_reader_emotional_arc:     true
  special_checks:
    - name: "武学体系一致性"
      description: "招式威力、内功层次、境界差距是否与 power_system 定义一致"
      scoring: "无铺垫跨境界战胜→WARNING；绝招连续使用无代价→WARNING"
  chapter_type_weights:
    日常章:  { expectation: "标准", adjustment: 0 }
    过渡章:  { expectation: "可降低5分", adjustment: -5 }
    爆发章:  { expectation: "可降低5分", adjustment: -5 }
    卷末章:  { expectation: "最严格", adjustment: 0 }
  scoring_flexibility:
    - "战斗场景中允许短句密集——不算节奏单调"

platform:
  target: "起点中文网"
  requirements:
    - "武侠分类——需与仙侠/玄幻区分明确"
    - "武学体系需有真实感——读者对过于夸张的武力容忍度低"

golden_finger:
  ceiling: null
  cost: null
  trigger_condition: null
  growth_path: null
```

---

## 题材禁忌（来源：openclaw wuxia + inkos xianxia）

- 主角依靠神兵/秘籍无代价碾压——绝招必须有代价（使用后虚弱/反噬/冷却）
- 江湖规则被随意打破——恩怨分明、长幼有序、以武会友
- 武功体系前后矛盾——没有无敌的武功，相生相克
- 用"天赋异禀"跳过修炼过程——天赋+努力+机缘，缺一不可
- 混入修仙/玄幻式的飞升成仙——武侠的天花板是"武林神话"
- 反派纯粹的恶——在江湖中，每个人都有自己相信的"义"

## 武学体系规则（来源：openclaw wuxia + inkos 仙侠修炼规则）

- 武学类型：内功（真气修炼）+ 外功（招式技巧）+ 轻功（身法）+ 暗器（远程）
- 层次分明：三流→二流→一流→后天→先天→宗师→大宗师→绝顶——每层有可感知的强弱差距
- 相生相克：没有无敌的武功——每种武功都有克制的武功
- 境界突破三要素：内功积累+招式领悟+实战磨砺——缺一不可
- 绝招代价：使用后衰弱≥1章的恢复期；某些禁忌武功有永久性代价（折寿/残废）
- 重伤恢复必须合理——不能下章就满状态

## 语言铁律（来源：chinese-novelist 白描 + openclaw wuxia）

- 白描为主——一招一式有名称但不过度渲染。"黑虎掏心"足矣，不必写成"他使出一招黑虎掏心如猛虎下山般——"
- 动作场景用短句（5-15字）——"他侧身。刀锋擦过鼻尖。左脚蹬地。剑尖刺出。"
- 禁止西式从句堆叠——主谓宾短促有力，中文语感
- 对话有江湖味——"阁下""请赐教""得罪了""后会有期"——但不过度文绉绉
- 禁止使用玄幻/修仙术语（灵气/渡劫/飞升）——这是武侠，不是仙侠

## 叙事指导（来源：openclaw wuxia + chinese-novelist 节奏控制）

江湖是核心舞台——不是单纯的武力对决，是人情债与道义约束。

恩怨情仇驱动剧情：复仇→结仇→化解→新的恩怨。每一段恩怨都应该有可以理解的动机——不是"因为他是坏人"。

战斗节奏：紧张→短暂缓解→更紧张→高潮→战后反应（伤势/旁人的震惊/战利品意义）。

### 江湖政治的独特魅力
- 门派之间的合纵连横——不是单纯的打斗
- 正邪之间的灰色地带——最好的反派有自己相信的"义"
- 隐世高人的登场——不是"开挂"，是江湖格局的改变
- 师徒关系是情感的深层纽带——"教会徒弟，饿死师父"的张力
