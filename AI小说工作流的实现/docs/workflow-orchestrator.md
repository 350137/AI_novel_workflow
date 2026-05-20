# 工作流编排逻辑

> 本文档定义单一真相来源的编排规则。所有 skill 的 SKILL.md 引用本文档的逻辑。

---

## 零、Genre Profile 加载（所有流水线前置步骤）

在启动任何流水线之前，必须先加载 Genre Profile。

### Genre Profile 解析规则

1. 如果用户指定 `--genre <name>` → 加载 `genre_refactor/genre_profiles/<name>.md`
2. 否则 → 加载 `novel_memory/story/style/genre_profile.md`
3. 如果两者都不存在 → **报错**，提示先运行 Advisor 初始化 Genre Profile

### Genre Profile 注入

加载后的 Genre Profile 按 Section 分发到各 Agent：

| Genre Profile Section | 注入目标 Agent |
|----------------------|---------------|
| `genre`, `world_rules`, `satisfaction`, `suspense`, `characters`, `language`, `chapter`, `audit`, `platform`, `golden_finger` | Planner（全局约束） |
| `satisfaction`, `suspense`, `language`, `chapter`, `world_rules`, `genre.primary` | Writer（写作约束） |
| `audit.dimensions`, `audit.special_checks`, `audit.chapter_type_weights`, `world_rules`, `language`, `power_system` | Auditor（审计配置） |
| `language.fatigue_words`, `language.forbidden_patterns`, `power_system`, `world_rules.core_laws` | Reviser（修订参考） |
| `language.fatigue_words`, `language.syntax_rules`, `language.forbidden_patterns`, `language.narrative_style` | Polisher（润色参考） |

---

## 一、完整流水线（一章的旅程）

```
用户触发: /write-chapter 11（或 /write-volume 1 --from 11）

STEP 0: GENRE PROFILE LOAD ────────────────────────────
  解析 --genre 参数 → 加载 Genre Profile YAML → 注入后续所有 Agent


STEP 1: PLAN ─────────────────────────────────────────
  输入：
    novel_memory/story/style/genre_profile.md（题材配置——注入 Planner）
    novel_memory/story/outline/volume_map.md
    novel_memory/state/hooks.json
    novel_memory/state/character_states.json（如存在）
    novel_memory/state/chapter_summaries.json
    novel_memory/state/workflow_state.json

  如果是第一章且 volume_map.md / story_frame.md 不存在：
    → 先触发 Advisor 生成完整 Foundation（story_frame + act_structure + volume_map
      + roles + book_rules + pending_hooks + writing_tips + genre_profile.md）
    → 然后继续 Planner

  Agent: hjw-novel-planner（加载 agents/hjw-novel-planner.prompt.md）

  产出：
    novel_memory/output/chapters/chapter_011/chapter_011_memo.md
    novel_memory/output/chapters/chapter_011/chapter_011_context.json

  验证：ContextPackage 符合 5 条硬规则


STEP 2: WRITE ─────────────────────────────────────────
  输入：
    output/chapters/chapter_011/chapter_011_memo.md
    output/chapters/chapter_011/chapter_011_context.json
    novel_memory/story/style/style_profile.json
    novel_memory/story/style/genre_profile.md（题材约束——注入 Writer）

  Agent: hjw-novel-writer（加载 agents/hjw-novel-writer.prompt.md）

  产出：
    novel_memory/output/chapters/chapter_011/chapter_011.md（初稿 v1）
    novel_memory/output/chapters/chapter_011/chapter_011_delta.json

  验证：字数符合 Genre Profile chapter.word_count 定义 / PRE_WRITE_CHECK 全通过


STEP 3: AUDIT ─────────────────────────────────────────
  输入：
    output/chapters/chapter_011/chapter_011.md（当前版本）
    output/chapters/chapter_011/chapter_011_memo.md
    novel_memory/state/hooks.json
    novel_memory/state/character_states.json
    novel_memory/story/style/genre_profile.md

  Agent: hjw-novel-auditor（加载 agents/hjw-novel-auditor.prompt.md）

  产出：
    novel_memory/output/chapters/chapter_011/chapter_011_audit.json
    （追加到 workflow_state.json active_chapter.audit_history）

  验证：AuditReport 格式符合 schema


STEP 4: DECISION GATE ────────────────────────────────
  硬编码路由逻辑（不调用LLM）：

  读取 chapter_011_audit.json.verdict

  ┌─ verdict = "PASS"（≥90分，无CRITICAL）
  │   └─ 跳转 STEP 5（POLISH）
  │
  ├─ verdict = "PASS_WITH_WARNINGS"（≥70分）
  │   ├─ 全部 issues.category = LOCAL
  │   │   └─ ROUTE: LOCAL_PATCH → STEP 4a
  │   └─ 任一 issues.category = STRUCTURAL
  │       └─ ROUTE: STRUCTURAL_REWRITE → STEP 4a
  │
  ├─ verdict = "FAIL"（<70分 或 有CRITICAL）
  │   ├─ 含有 CRITICAL + dimension = "敏感内容"
  │   │   └─ ROUTE: HUMAN_ESCALATE → 暂停
  │   └─ 其他
  │       └─ ROUTE: STRUCTURAL_REWRITE → STEP 4a
  │
  └─ revision_round = 3 且 verdict ≠ PASS
      └─ ROUTE: HUMAN_ESCALATE → 暂停，输出3轮快照供选择

  LOCAL_PATCH：temperature 0.5，原地修补
  STRUCTURAL_REWRITE：temperature 0.7，重写标记段落


STEP 4a: REVISE ───────────────────────────────────────
  输入：
    novel_memory/story/style/genre_profile.md（题材配置——注入 Reviser）
    output/chapters/chapter_011/chapter_011.md（当前版本）
    output/chapters/chapter_011/chapter_011_audit.json
    output/chapters/chapter_011/chapter_011_memo.md
    output/chapters/chapter_011/chapter_011_context.json

  Agent: hjw-novel-reviser（加载 agents/hjw-novel-reviser.prompt.md）

  产出：
    output/chapters/chapter_011/chapter_011_v{N+1}.md（版本号递增）
    output/chapters/chapter_011/revision_notes.md

  然后 → 回到 STEP 3（重新审计，revision_round + 1）


### 修订影响分析（来源：onkos analyze_revision_impact）

在 STEP 4a 修订完成后、回到 STEP 3 重新审计前，执行影响分析。**仅在 STRUCTURAL_REWRITE（非 LOCAL_PATCH）时执行。**

#### 算法（5 步）

```
步骤 1：实体对比
  从旧版正文和新版正文中提取实体（角色/地点/物品）：
    added_characters   = new_chars - old_chars
    removed_characters = old_chars - new_chars
    added_locations    = new_locs - old_locs
    removed_locations  = old_locs - new_locs
    added_items        = new_items - old_items
    removed_items      = old_items - new_items
  changed_entities = 所有出现变化的实体名并集

步骤 2：后续章节搜索
  对每个 changed_entity → 搜索 chapter+1 到 chapter+500 的正文
  → 去重排序 → affected_chapters[{chapter, entity, match_text, relevance}]

步骤 3：受影响事实检测
  遍历 character_states.json → 所有 entity ∈ changed_entities 的事实
  → affected_facts[{entity, attribute, value, importance, chapter}]

步骤 4：受影响伏笔检测
  遍历 hooks.json → description 包含 changed_entity 或 related_characters 与之重叠
  → affected_hooks[{hook_id, desc, status}]

步骤 5：风险判定
  high:   removed_characters/locations/items 非空（有实体被删除）
  medium: affected_chapters/facts/hooks 非空（存在受影响内容）
  low:    无任何受影响内容
```

#### 输出格式

```
📋 修订影响分析报告 — 第 N 章修订

风险等级: HIGH / MEDIUM / LOW

实体变化:
  新增角色: [...]    删除角色: [...]
  新增地点: [...]    删除地点: [...]
  新增物品: [...]    删除物品: [...]

受影响章节（共 M 章）:
  - 第 X 章: 提及 [entity]（匹配: "...相关文本..."）

受影响事实（共 K 条）:
  - [entity].[attribute] = [value]（importance: X, chapter: Y）

受影响伏笔（共 J 条）:
  - [hook_id]: [desc]（status: X）

建议:
  - HIGH: 建议重读所有受影响章节，确认是否需要连带修订
  - MEDIUM: 建议检查受影响的事实和伏笔，更新状态
  - LOW: 无需额外操作
```

#### 后续行动

```
risk = HIGH   → 暂停，人工确认是否继续（实体删除可能导致连锁断裂）
risk = MEDIUM → 自动更新受影响事实（如状态已变），标记受影响伏笔需重新评估
risk = LOW    → 直接继续 STEP 3（重新审计）
```


STEP 5: POLISH ────────────────────────────────────────
  输入：
    output/chapters/chapter_011/chapter_011_v{N}.md（审计通过的版本）
    output/chapters/chapter_011/chapter_011_audit.json
    novel_memory/story/style/genre_profile.md
    novel_memory/story/style/style_profile.json

  Agent: hjw-novel-polisher（加载 agents/hjw-novel-polisher.prompt.md）

  产出：
    output/chapters/chapter_011/chapter_011_v{N}_polished.md
    output/chapters/chapter_011/polish_notes.md

  约束：字数变化 ≤ ±30字 / 不改情节 / 不改台词含义


STEP 6: SETTLE ────────────────────────────────────────
  纯 Claude Code 工具操作，不调用LLM。

  操作清单：

  【6a — 实体验证（来源：onkos extract-entities）】
  □ 读取 delta.entities_extracted，对比现有 character_states.json / hooks.json：
    - 标记"first_appearance=true"的实体——确认它们是否已被现有状态追踪
    - 如果新实体未被追踪 → 自动初始化（新角色→创建空白 character_state / 新地点→记录到 locations）
    - 如果 Writer 标记的实体缺失 → 提示"Writer 可能遗漏了实体提取"

  【6b — 事实变更检测（来源：onkos detect-fact-changes）】
  □ 读取 delta.factOps，逐条对比现有 character_states.json：
    识别 3 类变更：
    - 新事实(NEW)：delta.factOps 中的 subject+predicate 在现有状态中无记录 → 直接录入
    - 更新事实(UPDATED)：同一 subject+predicate 已有值但值不同 → 更新 + 旧值归档到 state_history
    - 冲突事实(CONFLICT)：delta.factOps 中的值与现有状态矛盾但 Writer 未标记为 modify/retire
      → 暂停 → 报告冲突："[实体]的[属性]在事实库中为[X]，但 Wwriter 产出为[Y]，未标记变更操作"
      → 如为合理变更(如本章发生了突破)→确认为 UPDATED
      → 如为遗忘(Writer 忘了之前的状态)→标记为 WRITER_ERROR，记录到 error_log

  【6c — 事实自动替代（来源：onkos record-facts auto-supersede）】
  □ 对于 UPDATED 和 NEW 类型的事实：
    - 同一 subject+predicate 的旧值 → 标记为 superseded，保留在 state_history 中
    - 新值写入 current_state
    - importance 分配规则（来源：onkos 事实3级重要性）：
      · 角色核心属性(姓名/身份/阵营/核心性格)→permanent
      · 阶段性状态(修为/关系/归属)→arc_scoped
      · 临时状态(位置/情绪/伤势)→chapter_scoped
    - valid_from = 当前章节号

  【6d — 伏笔更新（来源：onkos record-hooks）】
  □ 读取 delta.hookOps，更新 hooks.json：
    - plant → 新增伏笔，初始化 hint_count=0, partial_resolve_count=0, strength=0.5(默认)
    - advance → advanced_count++, last_advanced_chapter=当前章, 重新计算 urgency
    - resolve → status=resolved, resolution=描述
    - defer → status=deferred, 记录原因
    - hint → hint_count++, last_hint_chapter=当前章(维持读者记忆,不推进)
    - partial_resolve → partial_resolve_count++, 记录本次揭示的侧面
  □ 重新计算 forget_risk：距上次推进章数 / half_life
  □ urgency 衰减：5 × (0.5 ^ (距上次推进章数 / halfLifeChapters))
  □ 检查 promoted：advanced_count ≥ 2 → promoted=true

  【6e — 状态文件更新】
  □ 更新 novel_memory/state/character_states.json
    - 写入 state_history["chapter_011"] = 本章末状态
    - 更新 current_state = 本章末状态
  □ 更新 novel_memory/story/roles/<角色名>.md（每个出场角色）
    - 追加 "### 第 N 章" 段（境界/功法/武器/道具/位置/伤势/关系变化）
    - 记录本章起始行号和结束行号
    - 更新 novel_memory/story/roles/<角色名>_index.md：新增 "| 第 N 章 | L-start-L-end |"
    - 格式见 protocols/character_inventory.schema.md
  □ 更新 novel_memory/state/relationship_tracker.json
    - 追加 relationshipChanges 到对应关系线
  □ 更新 novel_memory/state/chapter_summaries.json
    - 追加 summaries["chapter_011"] = delta.chapterSummary

  【6f — 文档与快照】
  □ 更新 novel_memory/story/character_map.md
    - 刷新人物状态总览表 / 刷新关系矩阵 / 追加关系变更日志行
  □ 创建快照：复制 state/ 到 snapshots/ch011/
  □ 更新 novel_memory/state/workflow_state.json
    - chapter_history["11"] = { status: "done", ... }
    - current_chapter = 12 / current_step = "idle" / active_chapter 重置

  【6g — 错误记录】
  □ 更新 novel_memory/state/error_log.json
    - 将 AuditReport 中 severity≥high 的问题追加到 error_log
    - 将冲突事实（CONFLICT）记录到 error_log
    - 更新 stats 计数（by_severity + by_type）
```

### 续写恢复自检（来源：fiction-crafter 续写恢复流程）

每次从断点继续写作（新会话/中断恢复）时，在 STEP 1 之前执行以下检查：

```
续写前自检：
  □ 已读取 novel_memory/state/workflow_state.json（确认当前章节号）
  □ 已读取 novel_memory/story/style/genre_profile.md（确认题材配置）
  □ 已读取 novel_memory/state/hooks.json（确认待回收伏笔）
  □ 已读取 novel_memory/state/character_states.json（确认所有角色当前状态）
  □ 已读取 novel_memory/state/chapter_summaries.json（确认已发生的剧情）
  □ 已读取 novel_memory/state/relationship_tracker.json（确认关系现状）
  □ 已读取最新3章的正文（确认衔接）
  □ 已检查消失角色——任何配角出场后>15章未出现→预警
  □ 已读取 novel_memory/state/error_log.json（确认历史问题模式，避免重复）
```

---

## 二、版本命名规则

```
Writer 产出       → chapter_011.md           （v1）
Reviser 第1轮     → chapter_011_v2.md         （v2）
Reviser 第2轮     → chapter_011_v3.md         （v3）
Polisher          → chapter_011_v3_polished.md （最终稿）

如果审计直通（无修订）：
Writer → chapter_011.md → Polisher → chapter_011_polished.md
```

`workflow_state.json` 的 `chapter_history[N].final_file` 始终指向最终稿路径。

---

## 三、Settle 详细操作

### 3.1 更新 hooks.json

从 `chapter_011_delta.json.hookOps` 读取：

```
for each hookOp:
  if action = "plant":
    → 在 active_hooks[] 中新增记录
    → 初始化字段：planted_chapter=N, status="planted", advanced_count=0
  if action = "advance":
    → 对应 hook.advanced_count += 1
    → hook.last_advanced_chapter = N
    → hook.status = hookOp.newStatus
    → 如果 advanced_count ≥ 2 → hook.promoted = true
  if action = "resolve":
    → 从 active_hooks[] 移除
    → 追加到 resolved_hooks[]，记录 resolution
  if action = "defer":
    → hook.status = "deferred"
    → 记录 defer 原因（从 hookOp.description）
```

收尾：
```
- count = len(active_hooks)
- budget.active = count
- budget.can_plant = max(0, 12 - count)
- 计算 openVsResolved: 本章 open 数 / 本章 resolve 数
- 如果 open < resolve → 记录警告（但继续）
```

### 3.2 更新 character_states.json

从 `chapter_011_delta.json.characterStateChanges` 读取：

```
for each change in characterStateChanges:
  character = characters[change.character]
  
  → 追加 state_history["chapter_011"]:
    { cultivation, injuries, location, emotional_state, relationships_summary, key_events }
  
  → 更新 character.current_state:
    根据 change.field 设置对应字段
```

### 3.3 更新 relationship_tracker.json

从 `chapter_011_delta.json.relationshipChanges` 读取：

```
for each relChange:
  → 查找或创建 relationship_line
  → 追加 progression 条目：
    { chapter: N, from_stage, to_stage, trigger_event, evidence }
  → 更新 current_stage = to_stage
```

### 3.4 更新 character_map.md

```
- 读入 character_states.json 中所有角色的 current_state
- 刷新"人物状态总览"表
- 读入 relationship_tracker.json
- 刷新"关系矩阵"
- 追加"每章关系变更日志"行
```

### 3.5 创建快照

```
复制以下文件到 snapshots/ch011/：
  hooks.json
  character_states.json
  relationship_tracker.json
  chapter_summaries.json
  workflow_state.json（快照时点）
```

---

## 四、批量模式（/write-volume）

```
/write-volume 1 --from 11

流程：
  for chapter in 11..20:
    1. 运行 STEP 1-6（完整流水线）
    2. 如果 verdict = HUMAN_ESCALATE → 暂停，等人类处理
    3. 如果 chapter % 5 == 0 → 暂停 5 分钟让人类抽查
    4. 人类确认继续 → 继续下一章
    5. 如果 chapter == 20（卷末）→ 强制暂停，输出卷末报告
```

卷末报告内容：
- 本卷所有章审计分数趋势
- 伏笔回收率（resolved / total_active）
- 境界成长曲线
- 关系线推进摘要
- 人物状态变化摘要

---

## 五、人类介入协议

### 5.1 强制暂停点

| 触发条件 | 暂停后输出 | 人类可选操作 |
|---------|-----------|------------|
| Advisor 产出创意方案 | 8维设定 + Genre Profile | 修改/通过 |
| Planner 产出卷大纲 | 卷级规划 + ChapterMemo预览 | 修改/通过 |
| Auditor 3轮仍FAIL | 3轮快照 + 审计趋势 + 根因分析 | 选高分版/跳过/手动修改 |
| 卷末章落定后 | 卷末报告 | 审批/调整下卷 |
| 每5章批量暂停 | 最近5章摘要 + 审计分数 | 继续/抽查某章 |

### 5.2 人类可选操作

| 操作 | 命令 |
|------|------|
| 抽查某章 | `/audit-chapter N` |
| 重写某章 | `/write-chapter N --force` |
| 查看状态 | `/status` |
| 手动调整 Memo | 直接编辑 `chapter_N_memo.md` 后 `/write-chapter N --from-memo` |

---

## 六、错误处理

| 错误场景 | 处理 |
|---------|------|
| Agent 调用失败（超时/API错误） | 重试1次，仍失败→暂停，保留已有产出 |
| Writer 字数不足2200 | 如果 Auditor 未标记字数问题→继续。否则→LOCAL扩充 |
| StateDelta 缺失 evidence | Auditor Layer 2 标记→Reviser 补充→重新审计 |
| hooks.json 活跃超12条 | 暂停，通知人类决定哪些伏笔 defer |
| character_states.json 与章节矛盾 | Auditor Layer 2 检测→状态矛盾→Reviser 修正 |
| 快照创建失败 | 重试1次，仍失败→警告但不阻塞流水线 |

---

## 七、volumes.json 卷规划追踪

```json
{
  "volumes": {
    "1": {
      "status": "in_progress",
      "simple_plan": "卷1目标：<根据本书Genre Profile生成，300字以内>（初稿规划时生成）",
      "detailed_plan": "开卷时综合前文+大纲+人物现状生成（见 volume_1_detailed_plan.md）",
      "chapters": "1-20",
      "chapters_completed": 10,
      "kr_tracking": {
        "KR1": "50%",
        "KR2": "20%",
        "KR3": "0%"
      }
    },
    "2": {
      "status": "planned",
      "simple_plan": "卷2目标：揭露阴谋+建立势力（初稿规划时生成）",
      "chapters": "21-40",
      "detailed_plan": null
    }
  }
}
```

规则：
- 初次大纲时：所有卷生成 `simple_plan`（每卷≤300字）
- 即将开卷时（如上卷写到第18章）：生成该卷的 `detailed_plan`（独立文件 `volume_N_detailed_plan.md`）
- `detailed_plan` 综合：初始大纲 + 前文实际事件 + 人物当前状态 + 关系线现状 + 活跃伏笔

---

## 八、题材切换与多书并行

### 8.1 题材切换流程

当开始一本新书（或切换题材）时，按以下流程初始化：

```
1. Advisor Phase 1：Q0 选择题材 → Q1-Q6 根据题材自适应追问
2. Advisor Phase 5：生成 Genre Profile YAML → 写入 novel_memory/story/style/genre_profile.md
3. 同时：将 Genre Profile 复制到 genre_refactor/genre_profiles/<genre_name>.md 作为可复用模板
4. 后续所有 /write-chapter 调用自动加载 novel_memory/story/style/genre_profile.md
```

**已有书切换题材**（不推荐，但支持）：
- 在 `novel_memory/story/style/` 下创建新的 `genre_profile.md`
- 后续章节使用 `--genre` 参数指定新 Profile
- 前文章节不重新审计

### 8.2 多书并行

同一套 Agent 流水线可同时服务多本书。每本书维护独立的 `novel_memory/` 实例。

**多书目录结构**：
```
D:\小说\AI小说工作流的实现\
├── agents/                          # 共享 Agent Prompts（题材无关）
├── protocols/                       # 共享 Protocol Schemas
├── templates/                       # 共享 Templates
├── genre_refactor/genre_profiles/   # 共享 Genre Profile 模板库
│   ├── xuanhuan_feicai.md
│   ├── urban_mystery.md
│   └── xianxia_romance.md
├── .claude/skills/                  # 共享 Skills
├── books/                           # 每本书独立目录
│   ├── book_01_林云/                # 玄幻废材逆袭
│   │   └── novel_memory/
│   │       ├── story/
│   │       │   ├── outline/
│   │       │   ├── roles/
│   │       │   └── style/genre_profile.md  → 链接或复制自 xuanhuan_feicai.md
│   │       ├── state/
│   │       ├── output/
│   │       └── snapshots/
│   ├── book_02_悬疑/                # 都市悬疑
│   │   └── novel_memory/
│   │       └── story/style/genre_profile.md  → 链接或复制自 urban_mystery.md
│   └── book_03_仙侠/                # 仙侠言情
│       └── novel_memory/
│           └── story/style/genre_profile.md  → 链接或复制自 xianxia_romance.md
```

**当前状态**：仅有一本书（林云玄幻），`novel_memory/` 在项目根目录下。
**迁移时机**：当开始第二本书时，将现有 `novel_memory/` 迁移到 `books/book_01_林云/` 下。

### 8.3 跨书经验积累

每完成一本书（≥50章），将运行数据回写到 Genre Profile 模板：

```
□ 该书 fatigue_words 的实际命中率 → 优化 genre_refactor/genre_profiles/ 中的词表
□ 该书审计分数的维度分布 → 调整 audit.dimensions 的权重
□ 该题材用户修正模式 → 优化 Advisor 的同题材追问策略
□ 该题材最常见的矛盾对 → 更新 Advisor Phase 3 的矛盾检测优先级
```

校准数据存储在 `novel_memory/state/advisor_calibration.json`，按 `genre.primary` 分组。
