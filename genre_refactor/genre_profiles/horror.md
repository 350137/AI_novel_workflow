# Genre Profile — 恐怖/灵异

```yaml
# ============================================================
# Genre Profile — 恐怖/灵异
# 版本：genre_profile_spec.md v1.0
# 参考：inkos horror.md（恐惧4层级 + 语言铁律）+ chinese-novelist
# ============================================================

meta:
  book_title: "<书名>"
  genre_name: "horror"
  created: "2026-05-05"
  version: "1.0"

genre:
  primary: "灵异"
  sub_genres: []
  world_basis: "平行地球"

world_rules:
  core_laws:
    - "恐怖世界的规则一旦建立不可违反——发现规则是生存的关键"
    - "未知比已知更恐怖——信息揭示必须克制，'看不见的'永远比'看见的'可怕"
    - "每个安全区都是暂时的——喘息之后是更深的恐惧"
    - "日常的扭曲比凭空出现的怪物更恐怖——好的恐怖来自熟悉事物的异化"
    - "每3章必须打破一次已建立的模式——规则矛盾/可信来源说谎/安全区失效"
  forbidden_concepts: []
  forbidden_phrases:
    - "这不科学"
    - "一切都会好起来的"

power_system:
  enabled: false

satisfaction:
  types:
    reversal:       { enabled: false }
    breakthrough:   { enabled: false }
    acquisition:    { enabled: false }
    revenge:        { enabled: false }
    recognition:    { enabled: false }
    romance:        { enabled: false }
    mystery_reveal: { enabled: true,  description: "真相揭示——恐怖源头的本质被理解（但理解不意味着安全）" }
    comedy:         { enabled: false }
    horror:         { enabled: true,  description: "核心爽点——恐惧本身就是吸引力。成功的逃脱/反杀是爽点释放" }
    survival:       { enabled: true,  description: "绝境求生——从恐怖中活下来就是最大的胜利" }
  rhythm:
    micro_relief:  { interval_chapters: "2-3", description: "小喘息——发现一个规则/找到一个临时安全区" }
    minor_payoff:  { interval_chapters: "4-6", description: "中揭示——理解恐怖的一个侧面/一次成功的逃脱" }
    major_payoff:  { interval_chapters: "10-15", description: "大揭示——恐怖源头的真相/最终对决" }
  emotion_curve: "渐进上升"
  combat_density: "低"
  humor_ratio: "无"

romance:
  weight: "辅助"
  type: null

suspense:
  intensity: "核心驱动"
  hook_weights:
    suspense:    10   # 核心——"到底是什么？"
    threat:      9    # "它在哪里？下次什么时候出现？"
    reversal:    3
    romance:     0
    mystery:     8
    cliffhanger: 7
  hook_emotion_mapping:
    suspense:    "恐惧的期待——不知道下一刻会发生什么"
    threat:      "紧张——威胁正在逼近"
    reversal:    "震惊——之前的规则被打破"
    mystery:     "不安——那个细节意味着什么？"
    cliffhanger: "毛骨悚然——在最恐怖的瞬间中断"

characters:
  protagonist_archetypes:
    - "普通人卷入——最普通的人面对最不普通的恐怖"
    - "调查者——记者/侦探/好奇的邻居，一步步深入不该触碰的领域"
    - "幸存者——从恐怖事件中生还的人，带着创伤继续前行"
    - "知情者——知道真相但无人相信的人"
  relationship_tension_types:
    - "同伴之间的信任与猜疑——谁可能是怪物？谁是安全的？"
    - "保护与牺牲——在恐怖面前，谁选择保护谁？"

language:
  narrative_style: "冷峻克制"
  fatigue_words:
    - "毛骨悚然" - "不寒而栗" - "浑身发冷" - "头皮发麻"
    - "鸡皮疙瘩" - "心跳加速" - "脊背发凉"
    - "莫名的"   - "说不清的" - "似乎"   - "仿佛"
    - "不知为何" - "莫名其妙" - "诡异"
  syntax_rules:
    - "恐怖用事实传达，不用情绪标签。✗'他感到一阵恐惧'→✓'他后颈的汗毛一根根立起来'"
    - "禁止过度解释恐怖。异常现象只需呈现，不需叙述者出来总结"
    - "克制叙事：越恐怖越冷静。句子随恐惧升级而变短，但叙述者语气始终平稳"
    - "被伤害/淘汰的角色必须有至少一个暗示个人故事的细节——让淘汰有重量"
  forbidden_patterns:
    - "不使用'毛骨悚然''不寒而栗'等情绪标签替代真实描写"
    - "不使用大量血腥描写替代心理恐惧"
    - "不使用'一切都会好起来的'式虚假安慰"

chapter:
  word_count: { min: 2000, max: 2500, target: 2200 }
  volume:
    chapters_per_volume: 30
    volume_end_requirements:
      - "恐怖源头被部分揭示——理解提升但恐惧未必减少"
      - "至少一个角色的命运发生不可逆的变化（死亡/失踪/精神崩溃）"
      - "安全区被打破——读者知道'没有哪里是安全的'"
  ending_requirements:
    - "在不安中结束——不是'解决了'而是'暂时安全但...'"
    - "章末钩子以不安/新异常为主——让读者带着毛骨悚然翻下一章"
    - "一个好的恐怖章末钩子让读者犹豫要不要现在翻下一页"

audit:
  dimensions:
    script_001_facts_consistency:       true
    script_002_character_state_sync:    true
    script_003_hook_fulfillment:        true
    script_004_hook_debt_check:         true
    script_005_relationship_tracking:   true
    script_006_pov_consistency:         true
    script_007_world_rules_compliance:  true    # 恐怖规则一致性——核心
    script_008_timeline_check:          true
    script_009_location_continuity:     true
    script_010_item_tracking:           true
    script_011_power_level_check:       false
    script_012_forbidden_words_check:   true    # 情绪标签替代——重要
    script_013_memo_compliance:         true
    hybrid_014_character_state_contradiction: true
    hybrid_015_dialogue_consistency:          true
    hybrid_016_emotional_continuity:          true
    hybrid_017_scene_transition_quality:      true
    hybrid_018_pacing_rhythm:                 true    # 恐惧递进节奏——核心
    hybrid_019_info_density:                  true    # 信息释放克制——核心
    hybrid_020_hook_embedding_quality:        true
    hybrid_021_ending_strength:               true
    llm_022_ooc_check:                true
    llm_023_dialogue_naturalness:     true
    llm_024_show_vs_tell:             true    # 恐怖必须用事实传达
    llm_025_power_breakdown:          false
    llm_026_emotional_depth:          true
    llm_027_sensory_richness:         true    # 五感是恐怖的载体——核心
    llm_028_plot_logic:               true
    llm_029_character_motivation:     true    # 角色的恐惧反应是否真实
    llm_030_world_immersion:          true    # 氛围
    llm_031_prose_quality:            true
    llm_032_narrative_voice:          true    # 克制叙事的语气
    llm_033_theme_consistency:        true
    llm_034_genre_authenticity:       true
    llm_035_subtext_quality:          true
    llm_036_anticlimax_detection:     true
    llm_037_cliche_detection:         true
    llm_038_description_balance:      true
    llm_039_inner_monologue_quality:  true
    llm_040_reader_emotional_arc:     true
  special_checks:
    - name: "恐惧层级递进"
      description: "不安是否按 不适→不安→恐惧→绝望 的四层级递进？是否跳过了必要层级？"
      scoring: "直接跳过层级→WARNING；全程同一层→节奏单调"
    - name: "情绪标签替代检测"
      description: "是否用'他感到恐惧'代替了具体描写？"
      scoring: "每出现1次→WARNING"
  chapter_type_weights:
    日常章:  { expectation: "标准", adjustment: 0 }
    过渡章:  { expectation: "可降低5分", adjustment: -5 }
    爆发章:  { expectation: "标准（揭示/逃脱章）", adjustment: 0 }
    卷末章:  { expectation: "最严格", adjustment: 0 }
  scoring_flexibility:
    - "氛围章允许较慢的节奏——恐怖需要铺垫"

platform:
  target: "起点中文网"
  requirements:
    - "灵异分类——需与悬疑区分明确"
    - "审核注意：不能宣扬封建迷信（'这个故事纯属虚构'可作为免责声明）"

golden_finger:
  ceiling: null
  cost: null
  trigger_condition: null
  growth_path: null
```

---

## 题材禁忌（来源：inkos 恐怖 + chinese-novelist）

- 恐怖源头过早完全暴露——未知才恐怖，"看不见的"永远比"看见的"更可怕
- 主角无脑刚正面解决一切——求生本能驱动行为，不是英雄主义
- 用打脸/升级等爽文套路替代恐怖氛围
- 恐怖元素与日常场景割裂——好的恐怖来自日常的扭曲，凭空出现的怪物不可怕
- 角色面对恐怖事件完全不害怕——颤抖/口干/思维混乱/判断力下降是真实反应
- 用大量血腥描写替代心理恐惧——血腥是刺激，不是恐怖
- 每3章必须打破一次已建立的模式——规则矛盾/可信来源说谎/安全区失效

## 恐惧层级递进（来源：inkos 恐怖）

不要跳过层级直达高潮——递进才有力量。

| 层级 | 状态 | 写法 |
|:--:|------|------|
| 1 | 不适感 | 微妙的错位、违和——日常中有东西"不对" |
| 2 | 不安 | 确认有异常，但看不清全貌——读者和角色一起猜 |
| 3 | 恐惧 | 威胁明确化——逃生本能启动——心跳加速、手心出汗 |
| 4 | 绝望 | 规则被打破，安全感彻底崩塌——"没有哪里是安全的" |

## 语言铁律（来源：inkos 恐怖）

- 恐怖用事实传达，不用情绪标签。✗"他感到一阵恐惧"→✓"他后颈的汗毛一根根立起来"
- 禁止过度解释恐怖。异常现象只需呈现，不需叙述者出来总结"这一切都太不正常了"
- 克制叙事：越恐怖越冷静。句子随恐惧升级而变短，但叙述者语气始终平稳
- 被淘汰/伤害的配角必须有至少一个暗示个人故事的细节（书包里的补习班收据、手机壳上的贴纸）——让淘汰有重量
- 五感是恐怖的载体：声音（不该有声音的地方有声音）、气味（腐败/潮湿/金属）、触觉（冷/湿/黏）、温度（突然变冷）、视觉（阴影/轮廓/什么东西在动）

## 叙事指导（来源：inkos 恐怖 + chinese-novelist）

氛围是第一生产力。用五感细节建立不安。信息揭示要克制——读者和角色一起发现真相。

规则感：恐怖世界有自己的规则，发现规则是生存的关键。但规则可以被打破——这才是最恐怖的时刻。

信息管理制造的张力：读者知道但角色不知道→焦虑。角色知道但读者不知道→悬念。

每个安全区都是暂时的，喘息之后是更深的恐惧。日常的扭曲比凭空出现的怪物更恐怖——把熟悉的东西变陌生。

### 恐惧的节奏
不安建立（2-3章）→确认异常（1章）→恐惧升级（1-2章）→暂时喘息（0.5章）→更深恐惧（循环）。不要在恐惧中待太久——读者会麻木。不要在安全中待太久——读者会放松。
