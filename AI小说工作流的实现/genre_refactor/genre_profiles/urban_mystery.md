# Genre Profile — 都市悬疑

```yaml
# ============================================================
# Genre Profile — 都市·悬疑
# 版本：genre_profile_spec.md v1.0
# 参考：novelist 悬疑线设计 + inkos mystery genre + tomato-novelist
# 日期：2026-05-04
# ============================================================

meta:
  book_title: "<书名>"
  genre_name: "urban_mystery"
  created: "2026-05-04"
  version: "1.0"

genre:
  primary: "悬疑"
  sub_genres: ["都市", "本格推理"]
  world_basis: "平行地球"

world_rules:
  core_laws:
    - "谜题必须有公平线索——读者在揭晓前能通过已给出的线索自行推理出答案"
    - "不允许'凶手从未出现过的角色'——最终解答涉及的所有人物必须在前期登场"
    - "每条线索必须被至少一个角色注意到，但不一定被正确解读"
    - "反转必须在已有线索中埋下伏笔——不能凭空出现新信息制造反转"
    - "信息控制：读者知道的不多于主角知道的（POV一致性）"
  forbidden_concepts: []
  forbidden_phrases:
    - "这不科学"
    # 现代背景可以使用科学概念

power_system:
  enabled: false
  # 都市悬疑无力量体系——以下字段不填写
  name: null
  levels: []
  cross_level_rules: []
  scoring_rubric: {}

satisfaction:
  types:
    reversal:       { enabled: false, description: "打脸——不适用" }
    breakthrough:   { enabled: false, description: "突破——不适用" }
    acquisition:    { enabled: false, description: "获得——不适用" }
    revenge:        { enabled: true,  description: "复仇清算——悬疑中常见的动机" }
    recognition:    { enabled: true,  description: "真相大白——角色/读者意识到真相的震撼" }
    romance:        { enabled: false, description: "情感进展——辅助线" }
    mystery_reveal: { enabled: true,  description: "谜题揭晓——核心爽点，每次线索碎片揭晓都是小爽点" }
    comedy:         { enabled: false, description: "搞笑——点缀" }
    horror:         { enabled: true,  description: "惊悚——营造恐惧/紧张感" }
    survival:       { enabled: true,  description: "绝境求生——主角被凶手/反派追逼的场景" }
  rhythm:
    micro_relief:  { interval_chapters: "1-2", description: "小线索碎片——每章至少给出1个新信息点" }
    minor_payoff:  { interval_chapters: "3-5", description: "中揭示——一个子谜题被解开，引出更大的谜题" }
    major_payoff:  { interval_chapters: "10-15", description: "大反转——核心假设被推翻，真相以完全不同的面貌出现" }
  emotion_curve: "渐进上升"
  combat_density: "低"
  humor_ratio: "点缀"

romance:
  weight: "辅助"
  type: null

suspense:
  intensity: "核心驱动"
  hook_weights:
    suspense:    10   # 核心——"真相是什么？"
    threat:      8    # "下一个受害者是谁？"
    reversal:    3    # "我以为的真相是错的？"
    romance:     0
    mystery:     9    # "这个线索意味着什么？"
    cliffhanger: 7    # 关键时刻断章——敲门声、发现尸体、收到关键证据
  hook_emotion_mapping:
    suspense:    "好奇值↑↑——必须翻下一章"
    threat:      "紧张值↑——担心角色安全"
    reversal:    "震惊——之前的假设全错了"
    romance:     "心动值↑"
    mystery:     "求解欲↑——线索碎片驱动读者自行推理"
    cliffhanger: "焦灼——关键时刻中断的急迫感"

characters:
  protagonist_archetypes:
    - "失忆强者——拥有出色的推理/刑侦能力但失去了关键记忆，自身也是谜题的一部分"
    - "隐世高手——普通身份下隐藏着特殊能力（前刑警/心理侧写师/黑客），被卷入新案件"
    - "双面人生——表面平凡，暗中追查某个真相，必须在两个身份间切换"
    - "旁观者卷入——普通人不小心目击/发现了不该知道的事，被迫成为'侦探'"
  relationship_tension_types:
    - "探案搭档——信任与猜疑交替，每个人都可能是内鬼"
    - "侦探vs嫌疑人——主角调查的所有人都可能是凶手"
    - "知情者vs隐瞒者——有人在隐瞒关键信息，但不一定是恶意的"

language:
  narrative_style: "冷峻克制"
  fatigue_words:
    - "突然"   - "猛然"  - "瞬间"   - "恐怖"   - "诡异"
    - "毛骨悚然" - "不寒而栗" - "脊背发凉" - "莫名的"
    - "似乎"   - "好像"  - "仿佛"   - "隐约"   - "恍惚"
    - "不知为何" - "莫名其妙" - "说不清"
    # 悬疑的疲劳词重点是过度使用模糊词——精确观察 > 模糊感受
  syntax_rules:
    - "单句不超过50字"
    - "一段不超过6句"
    - "观察描写精确具体——不用'诡异的气氛'而写'走廊尽头的灯闪烁了三下，然后熄灭了'"
    - "对话可以较长——审讯/对峙场景的对话是信息传递的核心"
    - "禁止'不知为何'、'莫名其妙地'——悬疑文中角色的一切感受都应有原因"
  forbidden_patterns:
    - "不使用'命运的齿轮'式形而上学总结"
    - "不使用'似乎/好像/仿佛'进行模糊描写——悬疑需要精确的感官细节"
    - "主角不能'恰好'发现线索——每条线索的发现必须有逻辑链条"

chapter:
  word_count: { min: 2000, max: 2500, target: 2200 }
  volume:
    chapters_per_volume: 30
    volume_end_requirements:
      - "本卷核心案件获得阶段性解答——凶手/真相至少部分揭露"
      - "主角获得关键信息，但也付出代价（失去盟友/陷入更大危险/被凶手盯上）"
      - "回收至少3条核心线索"
      - "抛出下一卷的引子——新的案件/更大的阴谋/被掩盖的真相浮出水面"
  ending_requirements:
    - "必须有钩子——悬念/威胁/反转至少1种"
    - "章末钩子以信息揭示（'原来如此'→'但这意味着...'）为主"
    - "断章要在最大悬念点——一个问题被抛出，答案在下一章"

audit:
  dimensions:
    script_001_facts_consistency:       true
    script_002_character_state_sync:    true
    script_003_hook_fulfillment:        true
    script_004_hook_debt_check:         true
    script_005_relationship_tracking:   true
    script_006_pov_consistency:         true
    script_007_world_rules_compliance:  true
    script_008_timeline_check:          true   # 悬疑中时间线至关重要
    script_009_location_continuity:     true
    script_010_item_tracking:           true   # 线索物品追踪
    script_011_power_level_check:       false  # 关闭——无力量体系
    script_012_forbidden_words_check:   true
    script_013_memo_compliance:         true
    hybrid_014_character_state_contradiction: true
    hybrid_015_dialogue_consistency:          true
    hybrid_016_emotional_continuity:          true
    hybrid_017_scene_transition_quality:      true
    hybrid_018_pacing_rhythm:                 true
    hybrid_019_info_density:                  true   # 悬疑：信息密度控制是关键
    hybrid_020_hook_embedding_quality:        true
    hybrid_021_ending_strength:               true
    llm_022_ooc_check:                true
    llm_023_dialogue_naturalness:     true
    llm_024_show_vs_tell:             true    # 悬疑：show>tell 极其重要
    llm_025_power_breakdown:          false   # 关闭——无力量体系
    llm_026_emotional_depth:          true
    llm_027_sensory_richness:         true
    llm_028_plot_logic:               true    # 悬疑：逻辑漏洞是致命伤
    llm_029_character_motivation:     true    # 悬疑：每个角色的每个行为都需要动机
    llm_030_world_immersion:          true
    llm_031_prose_quality:            true
    llm_032_narrative_voice:          true
    llm_033_theme_consistency:        true
    llm_034_genre_authenticity:       true    # 悬疑：谜题公平性检查
    llm_035_subtext_quality:          true    # 悬疑：潜台词/暗示是核心工具
    llm_036_anticlimax_detection:     true
    llm_037_cliche_detection:         true
    llm_038_description_balance:      true
    llm_039_inner_monologue_quality:  true
    llm_040_reader_emotional_arc:     true
  special_checks:
    - name: "谜题公平性检查"
      description: "揭晓的真相是否在之前章节中给出了足够的线索？读者能否在揭晓前自行推理？"
      scoring: "如果关键线索在揭晓前从未出现→CRITICAL"
    - name: "信息控制一致性"
      description: "读者是否被赋予了与主角相同的信息量？是否有'读者不知道但主角知道'或相反的信息不对称？"
      scoring: "如POV角色之外的信息出现在正文中→WARNING"
  chapter_type_weights:
    日常章:  { expectation: "标准", adjustment: 0 }
    过渡章:  { expectation: "可降低5分", adjustment: -5 }
    爆发章:  { expectation: "标准（反转/揭示章）", adjustment: 0 }
    卷末章:  { expectation: "最严格", adjustment: 0 }
  scoring_flexibility:
    - "genre_authenticity 检查——需考虑角色职业/教育背景（刑警vs普通市民的观察细节不同）"

platform:
  target: "起点中文网"
  requirements:
    - "每章≥2000字"
    - "悬疑分类：标签准确（本格/社会派/悬疑+灵异需在简介说明）"
    - "起点悬疑读者对逻辑完整性要求高"

golden_finger:
  # 都市悬疑一般无金手指；如有（如系统/预知）在此填写
  ceiling: null
  cost: null
  trigger_condition: null
  growth_path: null
```

---

## 题材禁忌（来源：inkos 都市 + openclaw mystery + chinese-novelist）

- 无逻辑的商业奇迹（没有铺垫的暴富）
- 反派降智配合主角表演——每个嫌疑人都应有合理的动机和自洽的行为逻辑
- 无视现实法律和商业规则——金融操作、公司运营必须有基本可信度
- 用"一个电话搞定"跳过具体操作过程
- 女性角色沦为花瓶或奖励
- 混入玄幻/仙侠战力体系

## 年代与现实约束（来源：inkos 都市 eraResearch）

- 涉及法律、政策、商业规则必须符合设定年代
- 人物身份、职位、权限不能超出现实合理范围
- 地名、机构名、行业术语必须准确
- 物价、收入、生活水平符合时代设定
- 主角不是全知全能，必须在前5章内至少出现一次判断失误或信息偏差

## 悬疑特定规则（来源：openclaw mystery + chinese-novelist）

### 公平游戏原则
- 凶手必须在故事前期（前30%）出场——不能在最后突然冒出一个"从未出现的神秘人"
- 不可用意外或直觉解决谜题——主角必须通过逻辑推理破案
- 所有线索必须公开——读者理论上可以提前猜到真相
- 可以有红鲱鱼（误导线索）但必须在真相揭晓时有合理解释

### 线索系统
- 核心线索 3-5 条直接指向真相
- 红鲱鱼 2-3 条指向错误答案
- 每条线索在正文中出现时，至少一个角色注意到但不一定正确解读
- 不能让主角"恰好"发现线索——必须有逻辑链条

## 语言铁律（来源：inkos 都市 + novelist）

- 人物内心独白必须口语化、直觉化，禁止商业分析/博弈论术语渗入叙事
- ✗"他迅速分析了当前的债务状况"→✓"他把那叠皱巴巴的白条翻了三遍"
- ✗"信息落差就在这儿"→✓"他们不知道的，他知道"
- 主角的判断通过行动和对话体现，不通过上帝视角的分析段落
- 钱权必须落地：通过物、势、地位变化和小人物反应兑现爽点

## 叙事指导（来源：inkos 都市 + openclaw mystery）

以商战、社交博弈和信息差驱动剧情。权力来自人脉、资本、信息和制度位置，不来自武力。

冲突解决靠谈判、交易、威慑、法律手段和利益交换。人物关系网是核心资产，每次社交互动都应有利益计算。

悬疑节奏：谜题引入→初步调查+红鲱鱼→首次突破线索→复杂化→关键揭示→最终推理+对峙→解决+揭示。每1-2章给出至少1个新信息点。

时代厚重感、人情债与制度摩擦是都市悬疑的灵魂。用场面、气味、动作、交易、压迫感切入，不要历史课件式开头。
