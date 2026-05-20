# Genre Profile — 玄幻废材逆袭

```yaml
# ============================================================
# Genre Profile — 玄幻·废材逆袭
# 版本：genre_profile_spec.md v1.0
# 基于：林云小说（第1-10章）+ inkos 玄幻预设 + fiction-crafter
# 日期：2026-05-04
# ============================================================

meta:
  book_title: "<书名>"
  genre_name: "xuanhuan_feicai"
  created: "2026-05-04"
  version: "1.0"

genre:
  primary: "玄幻"
  sub_genres: ["修炼", "废材逆袭"]
  world_basis: "架空异界"

world_rules:
  core_laws:
    - "跨境战斗胜利需要≥2项条件支撑（环境/法宝/战术/代价/属性克制）——Auditor会检查"
    - "从当前大境界突破到下一大境界需要的不仅是力量积累——必须有一个具体的'顿悟触发'"
    - "金手指只重塑能力基础，不能凭空创造力量——修为来自修炼，不是外挂"
    - "境界间战力差距明确：高1境=2-3个低境合力（无法靠'意志力'跨境）"
    - "宗门内冲突不能用暴力解决——规则是宗门大比，违反规则会被逐出宗门"
  forbidden_concepts:
    - "纳米"
    - "量子"
    - "基因"
    - "核弹"
    - "克隆"
    - "机器人"
    - "AI"
    - "互联网"
  forbidden_phrases:
    - "这不科学"
    - "从概率上来说"
    - "科学依据"
    - "分子结构"

power_system:
  enabled: true
  name: "修真境界"
  levels:
    - "开元境（初境/中境/巅峰）"
    - "化灵境（初境/中境/巅峰）"
    - "天罡境（初境/中境/巅峰）"
    - "元婴境（初境/中境/巅峰）"
    - "化神境（初境/中境/巅峰）"
    - "合道境（初境/中境/巅峰）"
    - "大乘境（初境/中境/巅峰）"
    - "飞升境"
  cross_level_rules:
    - "跨境战斗需要≥2项条件支撑（环境/法宝/战术/代价/属性克制）"
    - "境界间战力差距明确：高1境=2-3个低境合力（无法靠'意志力'跨境）"
    - "突破必须有铺垫（≥3章的积累描写/感悟/资源获取）"
    - "禁止战斗中临时觉醒新能力——除非此前≥5章埋了伏笔且伏笔被Tracker记录"
    - "每次突破后必须有'适应期'（≥1章）——不能连续突破"
  scoring_rubric:
    score_10: "战力体系严格一致：跨境≥2项条件、突破有≥3章铺垫、无临时觉醒、有适应期"
    score_7_9: "战力基本一致，1处战力细节可商榷但不过分"
    score_4_6: "1处战力崩坏——如跨境战斗未满足条件/突破无铺垫"
    score_1_3: "多处战力崩坏——数值体系被系统性违反"
    score_0: "战力体系完全崩溃——境界失去意义"

satisfaction:
  types:
    reversal:       { enabled: true,  description: "打脸逆袭——被轻视→实力碾压→身份揭露的三段式" }
    breakthrough:   { enabled: true,  description: "实力突破——境界提升的感官化描写" }
    acquisition:    { enabled: true,  description: "获得宝物/传承/机缘——资源升级" }
    revenge:        { enabled: false, description: "复仇清算——非本Profile主打" }
    recognition:    { enabled: true,  description: "认知颠覆——配角发现主角真实实力的震撼" }
    romance:        { enabled: false, description: "情感进展——玄幻废材流通常不以此为主" }
    mystery_reveal: { enabled: true,  description: "身世揭秘——封印/金手指/幕后黑手的真相揭露" }
    comedy:         { enabled: false, description: "搞笑——点缀性使用" }
    horror:         { enabled: false, description: "恐怖——不适用" }
    survival:       { enabled: true,  description: "绝境求生——在资源匮乏/封印状态下突破" }
  rhythm:
    micro_relief:  { interval_chapters: "1-2", description: "小爽点——段评槽点/小打脸/小展示" }
    minor_payoff:  { interval_chapters: "3-5", description: "中爽点——阶段性打脸/实力展示/资源获取" }
    major_payoff:  { interval_chapters: "10-15", description: "大高潮——境界突破/核心打脸/身世揭露" }
  emotion_curve: "过山车式"
  combat_density: "极高"
  humor_ratio: "点缀"

romance:
  weight: "辅助"
  type: null

suspense:
  intensity: "辅助"
  hook_weights:
    suspense:    6
    threat:      7
    reversal:    9
    romance:     0
    mystery:     4
    cliffhanger: 5
  hook_emotion_mapping:
    suspense:    "好奇值↑"
    threat:      "不安值↑"
    reversal:    "期待值↑"
    romance:     "心动值↑"
    mystery:     "困惑→求解欲↑"
    cliffhanger: "迫切想翻下一章"

characters:
  protagonist_archetypes:
    - "被封印者——天赋被封印，暗中恢复实力，每一步突破都在逼近被封印的真相"
    - "废材逆袭——被标签为'废材'，用三年苦功证明废材是谎言"
    - "天才陨落再起——曾经的天才因封印沦为底层，逐步恢复昔日荣光"
  relationship_tension_types:
    - "师徒暗中博弈——导师寄居金手指中，帮助主角但也有自己的目的"
    - "同门竞争——实力至上的宗门环境中考验信任与背叛"
    - "掌权者vs棋子——高层以封印控制天赋人才，主角是体制的反抗者"

language:
  narrative_style: "白描快节奏"
  fatigue_words:
    - "冷笑"   - "不屑"   - "嘲讽"   - "猛然"   - "陡然"
    - "瞬间"   - "恐怖如斯" - "倒吸一口凉气" - "瞳孔猛缩"
    - "沉声"   - "淡淡道" - "森然"   - "嘴角扬起" - "眼中闪过"
    - "浑身一震" - "不可思议" - "难以置信" - "前所未有"
  syntax_rules:
    - "单句不超过50字"
    - "一段不超过4句（行动段落）/ 6句（描写段落）"
    - "对话句不超过20字（冷峻主角）；辅助角色可放宽至30字"
    - "最多1个比喻/页（2000字约3个比喻上限）"
    - "肯定句式为主——不用'没有不'、'不可否认'这类双重否定"
    - "短句+句号——动作场景不插破折号和省略号"
    - "中文语感——不能出现西式从句堆叠"
  forbidden_patterns:
    - "不使用现代网络用语（玄幻古风背景）"
    - "不使用英文缩写"
    - "不出现机械降神式救援"
    - "剥离心理锚点——不用'他知道/感觉到/意识到'，直接写事实"
    - "禁止全知形而上学总结（'这就是命运的齿轮...'）"

chapter:
  word_count: { min: 2200, max: 2800, target: 2500 }
  volume:
    chapters_per_volume: 50
    volume_end_requirements:
      - "核心悬念阶段性收束——本卷的核心冲突获得解决"
      - "主角实力有质的飞跃——至少提升1-2个大境界"
      - "至少回收3条核心伏笔（core_hook=true）"
      - "埋下下一卷的主悬念——卷末钩子必须让读者想立刻翻到下一卷"
      - "至少发生1件不可逆事件（信息/关系/物理/权力改变）"
  ending_requirements:
    - "必须有钩子（悬念/威胁/逆袭至少1种）"
    - "不能以'未完待续'、'且听下回分解'结尾"
    - "钩子应自然嵌入最后1-2段"

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
    llm_025_power_breakdown:          true
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
    - name: "战力体系一致性"
      description: "境界名称、跨境规则、突破条件是否与 power_system 定义一致"
      scoring: "一票否决——如违反 cross_level_rules 即 CRITICAL"
  chapter_type_weights:
    日常章:  { expectation: "标准", adjustment: 0 }
    过渡章:  { expectation: "可降低5分", adjustment: -5 }
    爆发章:  { expectation: "可降低5分（天然高难度）", adjustment: -5 }
    卷末章:  { expectation: "最严格", adjustment: 0 }
  scoring_flexibility:
    - "genre_authenticity 检查 forbidden_concepts 时，乡野出身角色可放宽"

platform:
  target: "番茄小说"
  requirements:
    - "每章≥2000字（番茄推荐2200-2800）"
    - "敏感内容需规避"
    - "章节标题有吸引力（番茄书架页展示标题前十章）"

golden_finger:
  ceiling: "重塑天赋根基——到达此天花板后封印全部解除，金手指使命完成"
  cost: "使用金手指重塑能力→承受经脉撕裂级别的剧痛，重塑期间完全失去战斗力（持续数天至数周）"
  trigger_condition: "需要在特定环境或特定触发条件下——不是任何时候都能用"
  growth_path: "初始：修复被封印的经脉→中期：重塑天赋根基→完全体：解除所有封印，回归完整天赋"
```

---

## 题材禁忌（来源：inkos 玄幻 + openclaw revenge）

- 主角为推剧情突然仁慈、犯蠢、讲武德
- 同质资源不写衰减默认全额结算
- 用"暴涨""海量"跳过数值结算
- 无铺垫的能力觉醒（战斗中突然突破→需≥5章伏笔）
- 反派像木桩一样排队送死——核心对手必须有脑子，有试探、有误判、有反扑
- 无铺垫强行让退场角色回归
- 把所有章节都写成高爆裂战斗章
- 风格混入都市腔、科幻腔、游戏系统播报腔、轻小说吐槽腔

## 数值规则（来源：inkos 玄幻）

- 设定不可吃书：前文确立的设定数值后文不可无升级过程地随意改变
- 金手指四维约束：能力上限/附加代价/触发条件/成长路径——缺一不可
- 同质资源重复吞噬必须写明衰减：收益 = 基础值 × max(0.3, 1 - 0.15×(N-1))
- 期初值从账本取（不凭记忆），增量逐笔列出并注明来源
- 消耗逐笔列出并注明用途，期末 = 期初 + 增量 - 消耗，不得跳步
- 数值连续性必须可追溯：同层级、同类型样本的增量不得无说明跨越一个数量级

## 语言铁律（来源：inkos 玄幻 + novelist 句法红线）

- 力量体系的量级感用体感传达，不用抽象数字。✗"火元从12缕增加到24缕"→✓"手臂比先前有力了，握拳时指骨发紧"
- 同一高潮段（吞火/突破/觉醒）中，同一意象域的渲染不超过两轮，第三轮必须切入新信息或新动作
- 搜尸/清点/装备段落禁止清单式列举，必须带入角色判断或取舍
- 短句+句号——动作场景不插破折号和省略号
- 剥离心理锚点——不用"他知道/感觉到/意识到"，直接写事实

## 叙事指导（来源：inkos 玄幻 + fast-paced + satisfaction-formulas）

以战斗和资源获取驱动剧情。主角行为由利益驱动，杀伐果断。

三章内应有明确反馈——但不限于杀人：打脸、收益兑现、信息反转、地位变化都是反馈。

用动作、伤势、声音、重量、冲击、温度来落地"强"，少用空泛判断。每个场景至少推进一项：信息、地位、资源、伤亡、仇恨、境界。

### 打脸节奏
打脸公式（7步）：质疑→嘲讽→展示→初步震惊→真相揭示→打脸→主角淡定。每3-5章一次。

### 升级节奏
升级公式（6步）：遇强敌→压力巨大→顿悟/机缘→突破→实力展示→反杀。小突破每3-5章，中突破每10-15章，大突破每30-50章（卷级）。

### 装逼节奏
装逼公式（5步）：低调隐藏→被迫出手→一招制敌→众人震惊→淡定离开。主角的淡定比任何台词都有力量。
