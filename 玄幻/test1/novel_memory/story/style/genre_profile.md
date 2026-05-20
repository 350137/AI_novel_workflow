# Genre Profile — 《帝弈》

```yaml
# ============================================================
# Genre Profile — 《帝弈》
# 版本：genre_profile_spec.md v1.0
# 生成者：hjw-novel-advisor（Phase 5）
# 日期：2026-05-05
# ============================================================

# ========== A. 基础元信息 ==========
meta:
  book_title: "帝弈"
  genre_name: "xuanhuan_xuanyi_gaoxiao"  # 玄幻+悬疑+搞笑
  created: "2026-05-05"
  version: "1.0"

# ========== B. 题材定义 ==========
genre:
  primary: "玄幻"
  sub_genres: ["悬疑", "烧脑", "搞笑"]
  world_basis: "架空异界"

# ========== C. 世界观规则 ==========
world_rules:
  core_laws:
    - "造化恒定律：天地造化总量恒定。大帝占据的造化+其他修士占据的造化+游离灵气+大帝尸体中暂存的造化=恒定值"
    - "帝位独占律：同一时间有且仅有一个帝位。证道成帝=杀死或继承现任大帝——不存在绕过当前大帝的路径"
    - "后手触发条件约束律：前世的林剑设置的后手只能在触发条件恰好满足时被激活——不能主动搜索、提前预知或强行触发"
    - "跨境非绝对律：跨境战斗胜负不由境界决定。低境界获胜需要≥2项条件支撑（功法克制/灵气环境有利/神通针对性/法宝品质碾压/战术信息差）"
    - "分解独立律：每位大帝陨落后的尸体分解速率由其生前道统决定——道统越接近天道规则分解越慢，越物质化分解越快。不同大帝尸体的分解时间线无法被外力干预"
  forbidden_concepts:
    - "灵气无缘无故增多（违反造化恒定律）"
    - "绕过当前大帝直接证道（违反帝位独占律）"
    - "在触发条件不满足时主动搜索或启用后手（违反后手触发约束律）"
    - "单凭蛮力跨境战胜高境界对手（违反跨境非绝对律）"
    - "外力加速大帝尸体分解（违反分解独立律）"
  forbidden_phrases:
    - "天意如此"（天道在此世界观中是可被计算的系统，不是神秘意志）
    - "区区XX境也敢..."（禁止脸谱化反派语言）

# ========== D. 力量/数值体系 ==========
power_system:
  enabled: true
  name: "修真境界"
  levels:
    - "炼气"
    - "筑基"
    - "金丹"
    - "元婴"
    - "化神"
    - "合体"
    - "大乘"
    - "渡劫"
    - "准帝"
    - "大帝"
  cross_level_rules:
    - "低境界胜高境界需≥2项条件：功法克制/灵气环境/神通针对性/法宝碾压/战术信息差"
    - "准帝可短期爆发达大帝级战力但每次使用后需漫长恢复——不能常态化"
    - "大帝对一切低境界有规则性压制（非单纯力量差距，而是天道加持的绝对优势）"
  scoring_rubric:
    score_10: "战力体系严格一致——所有跨境胜利均有≥2项条件支撑并明确描写；所有境界突破均符合设定的突破条件"
    score_7_9: "基本一致——跨境胜利有条件支撑但某次描写不够清晰；境界突破有触发但细节不足"
    score_4_6: "1处战力崩坏——某次跨境胜利仅凭单一因素或蛮力取胜"
    score_1_3: "多处崩坏——≥2处战力体系违反，境界差距被无视"
    score_0: "体系完全崩溃——大帝被越级挑战无特殊条件，或境界逻辑矛盾"

# ========== E. 爽点与节奏 ==========
satisfaction:
  types:
    reversal:       { enabled: true, description: "扮猪吃虎——林剑作为废材突然用前世后手/本能拆解碾压对手" }
    breakthrough:   { enabled: true, description: "境界突破——每次跨境触发前世后手，双层成就感" }
    acquisition:    { enabled: true, description: "发现前世后手——每次后手触发都是一次智力快感" }
    revenge:        { enabled: true, description: "对帝庭的复仇——打脸帝庭巡查使和苍天帝代理人" }
    recognition:    { enabled: true, description: "身份被揭示——前世帝下第一人的身份逐渐暴露" }
    romance:        { enabled: true, description: "三女主情感进展——重要副线影响主线" }
    mystery_reveal: { enabled: true, description: "棋局真相揭露——每次揭开一层苍天帝的棋局都是大爽点" }
    comedy:         { enabled: true, description: "搞笑渗透——林剑的犯贱吐槽、沐灵儿的碎嘴、沈清霜的冷脸崩坏" }
    horror:         { enabled: false, description: "" }
    survival:       { enabled: true, description: "帝苍降临后的绝境求生——天渊城毁灭后的逃亡与重建" }
  rhythm:
    micro_relief:  { interval_chapters: "1-3", description: "单次打脸/单次后手触发/搞笑闪光/线索碎片" }
    minor_payoff:  { interval_chapters: "3-5", description: "跨境战斗/中等后手触发/角色关系进展" }
    major_payoff:  { interval_chapters: "10-15", description: "核心后手揭秘/境界突破/帝庭节点破坏/情感线重大进展" }
  emotion_curve: "过山车式——搞笑与悬疑交替，线索堆积→集中揭秘，日常→紧张→高潮→回落→新线索"
  combat_density: "中(15-30%)——战斗不是主角，但每次战斗都有智力层"
  humor_ratio: "渗透式(30-50%)——搞笑是叙事方式而非独立段落"

# ========== F. 情感线 ==========
romance:
  weight: "重要副线"
  type: "日久生情"  # 三女主各自不同类型：沈清霜是日久生情/苏念卿是从恨到爱/沐灵儿是从友到爱

# ========== G. 悬念与钩子 ==========
suspense:
  intensity: "核心驱动"  # 悬疑是全书核心驱动力之一
  hook_weights:
    suspense:    10  # 每章结尾悬念钩子
    threat:      7   # 帝苍熔炼计划的威胁
    reversal:    6   # 身份揭示和势力反转
    romance:     4   # 情感线钩子
    mystery:     10  # 棋局真相的谜团
    cliffhanger: 8   # 后手发现的章末钩子
  hook_emotion_mapping:
    suspense:    "好奇心——每章结尾让读者想知道'然后呢'"
    threat:      "紧张——对帝苍降临和熔炼计划的恐惧"
    reversal:    "满足——打脸和身份揭示带来的正义感"
    romance:     "暖——情感线的柔和张力"
    mystery:     "好奇心——对万年前棋局的探索欲"
    cliffhanger: "悬疑——后手发现引发的新问题"

# ========== H. 人物 ==========
characters:
  protagonist_archetypes:
    - "废材逆袭——表面犯贱废材实则万年前帝下第一人转世"
    - "棋手——前世布局今生执行的跨时空双人对弈"
    - "反套路——在严肃的悬疑内核外包裹搞笑表达"
  relationship_tension_types:
    - "冷面天才 vs 犯贱废材（沈清霜与林剑）"
    - "被绑定者的反抗（苏念卿与林剑/前世林剑）"
    - "直觉的自由灵魂 vs 计划中的角色（沐灵儿 vs 棋局的严肃性）"
    - "镜面对面——两种信念的碰撞（帝苍与林剑）"

# ========== I. 语言与文风 ==========
language:
  narrative_style: "白描快节奏——搞笑时句短而快，揭秘时精准如刀"
  fatigue_words:
    - 微微一笑  - 淡淡一笑  - 心中一惊  - 浑身一震  - 眼中精光
    - 倒吸一口  - 闷哼一声  - 冷喝一声  - 一声冷哼  - 怒极反笑
    - 一声叹息  - 面沉如水  - 不怒反笑  - 瞳孔一缩  - 脸色一变
    # ≥15词
  syntax_rules:
    - "打斗/搞笑段落：句短，段短，节奏快。少用形容词，多用具体动作和对话"
    - "悬疑揭秘段落：信息密度高，回指前文章节的线索，让读者体会'回看发现此处埋伏笔'的快感"
    - "情感段落：保留克制——不写'他心疼'，写'他看着她背影，这次没说话'"
  forbidden_patterns:
    - "禁止战斗中的冗长内心独白——战斗时不要插入大段思考"
    - "禁止搞笑打断真正的情感时刻——只在情感收束后释放搞笑压力"
    - "禁止用'其实''原来''却不知'等暴露叙事者存在的上帝视角词汇"
    - "禁止一段话内混用两个林剑的视角——同一段落只能用一种语气（前世冷=今生贱=不可同时出现）"

# ========== J. 章节要求 ==========
chapter:
  word_count: { min: 2000, max: 2800, target: 2500 }
  volume:
    chapters_per_volume: 80  # 10卷 × 80章 = 800章
    volume_end_requirements:
      - "卷末必须有1个高水平钩子（前台+后台双层覆盖）"
      - "卷末必须发生≥1个不可逆事件（信息/关系/物理/权力改变）"
      - "卷末OKR的三个KR至少70%达成为可验证状态"
      - "卷末必须回答本卷首提出的核心问题（但答案引出下一卷的更大问题）"
  ending_requirements:
    - "每章结尾必须有钩子——微悬念/新问题/新线索/后手触发预告"
    - "后手发现章结尾必须是后手内容+发现引发的下一个问题"

# ========== K. 审计配置 ==========
audit:
  dimensions:
    # Layer 1: 脚本审计（13维，全题材启用）
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
    # Layer 2: 混合审计（8维，全题材启用）
    hybrid_014_character_state_contradiction: true
    hybrid_015_dialogue_consistency:          true
    hybrid_016_emotional_continuity:          true
    hybrid_017_scene_transition_quality:      true
    hybrid_018_pacing_rhythm:                 true
    hybrid_019_info_density:                  true
    hybrid_020_hook_embedding_quality:        true
    hybrid_021_ending_strength:               true
    # Layer 3: LLM审计（19维，按题材开关）
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
  # 题材特定审计
  special_checks:
    - "搞笑+悬疑节奏平衡检测——连续烧脑章节超过3章→标记 pacing 警告"
    - "两个林剑的区分度检测——前世林剑的语言指纹应与今生林剑有明确差异"
    - "三女主各自的感情线推进不低于每2卷1次的频率"
    - "后手触发规则的逻辑一致性——每次后手触发的满足条件必须可追溯到设定中的触发逻辑"
  # 章节类型权重调整
  chapter_type_weights:
    日常章:  { expectation: "标准", adjustment: 0 }
    过渡章:  { expectation: "可降低5分", adjustment: -5 }
    爆发章:  { expectation: "可降低5分（天然高难度）", adjustment: -5 }
    卷末章:  { expectation: "最严格", adjustment: 0 }
  # 评分弹性
  scoring_flexibility:
    - "搞笑章节的战斗逻辑评分可适当宽松（搞笑场景中战力精确性非核心要求）"
    - "悬疑揭秘章节的文风评分加权提升"

# ========== L. 平台（可选） ==========
platform:
  target: "番茄小说"
  requirements:
    - "每章2000-2800字（番茄最佳阅读长度）"
    - "每5-10章设置一个高潮断章点"
    - "章节标题具有点击吸引力（可使用悬念/反差/吐槽）"

# ========== M. 金手指约束 ==========
golden_finger:
  ceiling: "前世后手不能凭空创造力量——只提供条件、信息、时机、法器、功法。修为必须自己修炼得来"
  cost: "每个后手的触发条件不可更改——林剑不能在条件不满足时强行获取后手辅助；后手触发总会增加帝苍在天道棋局上感知异常的几率"
  trigger_condition: "境界突破/遇到特定人物/特定事件发生/进入特定地点——由万年前林剑预设，不可变更"
  growth_path: "从单个碎片→碎片覆盖单领域（功法/炼丹/符箓/阵法）→碎片连接成完整的'前世完整记忆块'→两个林剑意志融合→证道时完全是一体"

# ========== N. 书级YAML约束（SECTION 4: book_rules） ==========
book_rules:
  protagonist:
    personalityLock: |
      1. 林剑在任何外人面前不自爆前世身份或后手内容——除非触发条件强制激活
      2. 林剑面对真正的力量碾压时（帝苍级），搞笑外壳自动脱落——暴露前世的冷峻准确——但危险过后会以更激烈的搞笑来消解创伤
      3. 林剑对普通弱者不展示力量碾压——他的基准行为模式是"用力量对抗力量，用搞笑对抗日常"
    behavioralConstraints:
      - "林剑不会主动对陌生人建立信任——搞笑友善≠信任"
      - "林剑不会在无≥2项条件支撑下挑战跨境对手——他的战术是'找到条件再出手'"
      - "林剑不会在同伴重伤时说搞笑的话——只会沉默或精准的行动——但会在同伴恢复后吐槽当时的自己"
  genreLock:
    primary: "玄幻"
    forbidden:
      - "不能出现与本书世界观设定不符的外来概念（如科幻元素、现代科技、平行宇宙）"
      - "不能出现'没有代价的力量突破'——所有跨境必须有具体代价（功法克制/灵气环境/神通/法宝/信息差中≥2项）"
  prohibitions:
    - "宗门内的冲突不能用私刑——规则是大比或决斗，违反规则会被宗门驱逐"
    - "大帝不能被越级单挑战胜——必须通过系统性瓦解（连锁反应+天道自行审判）"
    - "后手不能被主动搜索或提前触发——必须严格在自然触发条件下激活"
    - "搞笑不能打断真正的生死危及时刻——搞笑只在危险前/危险后出现"
  numericalSystem:
    realms:
      - "炼气"
      - "筑基"
      - "金丹"
      - "元婴"
      - "化神"
      - "合体"
      - "大乘"
      - "渡劫"
      - "准帝"
      - "大帝"
    subRealms:
      炼气:     ["初入", "中期", "后期", "巅峰"]
      筑基:     ["初入", "中期", "后期", "巅峰"]
      金丹:     ["初入", "中期", "后期", "巅峰"]
      元婴:     ["初入", "中期", "后期", "巅峰"]
      化神:     ["初入", "中期", "后期", "巅峰"]
      合体:     ["初入", "中期", "后期", "巅峰"]
      大乘:     ["初入", "中期", "后期", "巅峰"]
      渡劫:     ["一劫", "二劫", "三劫", "四劫", "五劫", "六劫", "七劫", "八劫", "九劫"]
      准帝:     ["初成", "稳固", "巅峰"]
      大帝:     ["证道", "稳固"]
    breakConditions:
      "炼气→筑基": "炼气巅峰+筑基丹或稀薄灵脉环境"
      "筑基→金丹": "筑基巅峰+顿悟一次自我之道+金丹雷劫"
      "金丹→元婴": "金丹巅峰+心魔考验+元婴雷劫"
      "元婴→化神": "元婴巅峰+三次天地交感+化神大劫"
      "化神→合体": "化神巅峰+领域完善+合体天劫"
      "合体→大乘": "合体巅峰+领悟一条完整法则+大乘天劫"
      "大乘→渡劫": "大乘巅峰+度过九次天劫"
      "渡劫→准帝": "渡劫圆满+窥见天道+有人愿证道但被帝位占位"
      "准帝→大帝": "杀死或继承现任大帝+天道承认"
  styleConstraints:
    perspective: "第三人称"
    sentencePersonality: "搞笑时句短快/揭秘时句精准/情感时句克制——6条句法红线中这3条对本书最重要"
    dialogueRatio: "30-50%"
    chapterLength: "2200-2500字"
```

---

## 修订记录

- [轮次1] 2026-05-05：Phase 1 Q0-Q7 完整收敛提问完成 → Phase 2 生成7段Foundation初版
