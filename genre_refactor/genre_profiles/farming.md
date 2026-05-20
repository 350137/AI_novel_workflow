# Genre Profile — 种田

```yaml
# ============================================================
# Genre Profile — 种田/慢生活
# 版本：genre_profile_spec.md v1.0
# 参考：inkos cozy.md（情感弧线 + 社区感）+ tomato-novelist 治愈甜宠
# ============================================================

meta:
  book_title: "<书名>"
  genre_name: "farming"
  created: "2026-05-05"
  version: "1.0"

genre:
  primary: "种田"
  sub_genres: []
  world_basis: "架空异界"

world_rules:
  core_laws:
    - "成长的节奏是缓慢但持续的——每一章都要有可感知的小进步"
    - "冲突来自资源匮乏/人际关系/自然挑战——不是生死存亡"
    - "社区是角色——村民/邻居/同僚的日常生活和关系线与主角同等重要"
    - "压抑之后必有温暖的释放——种田文的核心情感契约"
    - "世界规则轻量化——不需要复杂的政治/军事体系"
  forbidden_concepts:
    - "世界末日的威胁——违反了种田文的情感契约"
    - "大规模暴力/战争——冲突应保持在社区层面"
  forbidden_phrases: []

power_system:
  enabled: false

satisfaction:
  types:
    reversal:       { enabled: false, description: "打脸——不适用（种田文不需要强势碾压）" }
    breakthrough:   { enabled: true,  description: "技能突破——学会了新手艺/新技能" }
    acquisition:    { enabled: true,  description: "收获——庄稼丰收/店铺盈利/资源积累" }
    revenge:        { enabled: false }
    recognition:    { enabled: true,  description: "被认可——邻居/社区的肯定和感谢" }
    romance:        { enabled: true,  description: "情感进展——踏实温暖的关系升温" }
    mystery_reveal: { enabled: false }
    comedy:         { enabled: true,  description: "轻松幽默——生活中的小确幸和小搞笑" }
    horror:         { enabled: false }
    survival:       { enabled: false }
  rhythm:
    micro_relief:  { interval_chapters: "1-2", description: "小收获——一茬庄稼/一笔小生意/一次小互动" }
    minor_payoff:  { interval_chapters: "5-8", description: "中节点——新建筑落成/关系确认/季末丰收" }
    major_payoff:  { interval_chapters: "15-20", description: "大高潮——村庄升级/大生意成功/人生大事" }
  emotion_curve: "波浪式"
  combat_density: "无"
  humor_ratio: "辅助"

romance:
  weight: "主线"
  type: "甜宠"

suspense:
  intensity: "点缀"
  hook_weights:
    suspense:    3
    threat:      2
    reversal:    2
    romance:     8
    mystery:     2
    cliffhanger: 3
  hook_emotion_mapping:
    suspense:    "温和的期待——明天会发生什么好事？"
    threat:      "轻微担忧——今年的收成会不会出问题？"
    reversal:    "小惊喜——意外的好运"
    romance:     "心动——他们的关系又近了一步"
    cliffhanger: "温暖的悬念——下一章继续看他们如何解决问题"

characters:
  protagonist_archetypes:
    - "穿越者用现代知识改善生活——不是征服世界，是种出更好的番茄"
    - "退隐者——从前线/权力中心退出，在平凡中寻找快乐"
    - "普通人——在平凡岗位上用双手创造美好生活"
    - "守护者——用平静的方式保护自己的社区/家园"
  relationship_tension_types:
    - "邻里之间的互助与摩擦"
    - "新来者与原有社区的融合过程"
    - "手艺传承——师父与学徒之间的温暖羁绊"

language:
  narrative_style: "细腻描写"
  fatigue_words:
    - "不可思议" - "难以置信" - "震惊"
    - "猛然"   - "陡然"   - "瞬间"
    - "似乎"   - "仿佛"   - "宛如"
    - "不知为何"
  syntax_rules:
    - "节奏舒缓——允许较长的描写段落"
    - "感官细节丰富——食物/温度/季节/质感是种田文的核心魅力"
    - "对话温暖自然——不需要刀光剑影的语言交锋"
    - "可以写'日常'——但每段日常都应该推动关系或建设进程"
  forbidden_patterns:
    - "不使用战斗/战争/碾压等相关词汇的大量堆砌"
    - "不使用恐怖/惊悚的情绪渲染"
    - "不使用'这只是开始'式的大格局暗示（种田文不需要拯救世界）"

chapter:
  word_count: { min: 2000, max: 2500, target: 2200 }
  volume:
    chapters_per_volume: 40
    volume_end_requirements:
      - "一个季节的轮回完成——春种秋收/一个建设项目完工"
      - "主角的生活方式发生了可感知的改善"
      - "至少一段关系线获得温暖的推进"
      - "社区面貌有正向变化"
  ending_requirements:
    - "以温暖/期待收尾——不是焦虑和悬念"
    - "可以用'小小的悬念'——如'明天要去镇上买种子，不知道价钱怎么样'"
    - "不能用恐惧/威胁/危机结尾——好的种田文章末让读者'嘴角上扬'翻下一页"

audit:
  dimensions:
    script_001_facts_consistency:       true
    script_002_character_state_sync:    true
    script_003_hook_fulfillment:        true
    script_004_hook_debt_check:         true
    script_005_relationship_tracking:   true    # 社区关系线——核心
    script_006_pov_consistency:         true
    script_007_world_rules_compliance:  true
    script_008_timeline_check:          true    # 季节时间线——重要
    script_009_location_continuity:     true
    script_010_item_tracking:           true    # 资源/物品追踪——核心
    script_011_power_level_check:       false
    script_012_forbidden_words_check:   true
    script_013_memo_compliance:         true
    hybrid_014_character_state_contradiction: true
    hybrid_015_dialogue_consistency:          true
    hybrid_016_emotional_continuity:          true    # 温暖基调——核心
    hybrid_017_scene_transition_quality:      true
    hybrid_018_pacing_rhythm:                 true    # 节奏不是'快'是'稳'
    hybrid_019_info_density:                  true
    hybrid_020_hook_embedding_quality:        true
    hybrid_021_ending_strength:               true    # 温暖收尾质量
    llm_022_ooc_check:                true
    llm_023_dialogue_naturalness:     true
    llm_024_show_vs_tell:             true
    llm_025_power_breakdown:          false
    llm_026_emotional_depth:          true    # 情感深度不靠虐——靠温暖
    llm_027_sensory_richness:         true    # 五感是种田文的核心
    llm_028_plot_logic:               true
    llm_029_character_motivation:     true
    llm_030_world_immersion:          true
    llm_031_prose_quality:            true
    llm_032_narrative_voice:          true
    llm_033_theme_consistency:        true
    llm_034_genre_authenticity:       true    # 种田文的情感契约——不出现毁灭性威胁
    llm_035_subtext_quality:          true
    llm_036_anticlimax_detection:     true
    llm_037_cliche_detection:         true
    llm_038_description_balance:      true
    llm_039_inner_monologue_quality:  true
    llm_040_reader_emotional_arc:     true
  special_checks:
    - name: "情感契约检查"
      description: "是否出现了违反种田文情感契约的内容（世界末日/大规模暴力/持续的压抑无释放）"
      scoring: "如出现→WARNING（提醒作者这是种田文不是末世文）"
    - name: "建设进度追踪"
      description: "连续3章以上是否展示了生活/社区/技能的改善"
      scoring: "如停滞→INFO"
  chapter_type_weights:
    日常章:  { expectation: "标准", adjustment: 0 }
    过渡章:  { expectation: "可降低5分", adjustment: -5 }
    爆发章:  { expectation: "标准（丰收/落成/告白章）", adjustment: 0 }
    卷末章:  { expectation: "最严格", adjustment: 0 }
  scoring_flexibility:
    - "日常章允许更慢的节奏——这就是种田文的魅力所在"
    - "情感深度不依赖虐——温暖也可以有深度"

platform:
  target: "番茄小说"
  requirements:
    - "种田文分类——读者期待温暖/收获/建设，不要挂羊头卖狗肉"
    - "每章字数2000-2500——番茄平台的种田文读者更偏好轻松短章"

golden_finger:
  ceiling: null
  cost: null
  trigger_condition: null
  growth_path: null
```

---

## 题材禁忌（来源：inkos cozy + tomato-novelist 治愈甜宠）

- 引入世界末日/毁灭性威胁——违反了种田文的情感契约（读者来寻求温暖不是来紧张）
- 冲突解决不费吹灰之力——问题不能自己解决，主角需要付出努力
- "挂羊头卖狗肉"——标了种田文但写的是战斗爽文
- 幽默建立在别人的痛苦之上——种田文的幽默是温暖的自嘲，不是残酷的玩笑
- 紫色散文描述食物/自然但不推进角色或社区弧线——描写要有功能
- 压抑太久没有温暖的释放——种田文的情感契约是"压抑之后必有阳光"

## 情感弧线规则（来源：inkos cozy Emotional Arc）

- 赌注在情感上很高但并非存在级——角色在乎，世界不会毁灭
- 冲突类型：个人成长、社区问题、关系张力、小危险、道德困境
- 社区是角色——环境和关系与个体主角同等重要
- 希望必须始终存在——即使悲伤时刻也不以绝望告终
- 找到的家人/社区纽带驱动情感核心
- 角色弧线：孤立/悲伤→微小互动→逐渐敞开心扉→情感突破→融入
- 舒适的感官细节很重要：茶、烘焙食品、温暖的空间、季节的质地

## 语言铁律（来源：inkos cozy + tomato-novelist）

- 感官细节丰富——食物/温度/季节/质感是种田文的核心魅力
- 节奏舒缓——允许较长的描写段落，允许"日常"——但每段日常都应推动关系或建设
- 对话温暖自然——不需要刀光剑影的语言交锋，需要的是日常的关心和默契
- 可以写小幽默——但幽默是温和的，不是讽刺/讥笑
- 禁止战斗/战争/碾压等词汇的大量堆砌——种田读者不是来看这些的
- 五感聚焦：食物的香气、泥土的触感、阳光的温度、丰收的颜色、柴火的声音

## 叙事指导（来源：inkos cozy + tomato-novelist 治愈甜宠）

种田文的核心魅力在于"建设的过程"——读者来看着主角一砖一瓦地建立生活，然后自己也感到治愈。

### 建设与收获的节奏
- 每个阶段：种子播种→日常照料→遇到小问题→努力解决→收获
- 每次收获后应有短暂的"庆祝时刻"——让读者感受成就
- 建设是渐进式的——不要一章就从茅草屋变成大宅

### 关系的温度
- 社区关系是核心资产——邻居/村民/同僚都有自己的小故事
- 恋爱线是温水煮青蛙——不是一见钟情，是日常积累的好感
- "互相帮忙"是种田文的浪漫——一起修篱笆>烛光晚餐

### 章节节奏
- 没有"爆发章"概念——最"激动"的时刻是丰收/落成/告白
- 章末以温暖/期待收尾——让读者嘴角上扬翻下一页
- "小小的悬念"可以存在——如"明天要去镇上，不知道价钱怎么样"——但不是恐惧/威胁
