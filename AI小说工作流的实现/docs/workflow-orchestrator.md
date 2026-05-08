# 工作流编排逻辑

> 本文档定义单一真相来源的编排规则。所有 skill 的 SKILL.md 引用本文档的逻辑。

---

## 一、完整流水线（一章的旅程）

```
用户触发: /write-chapter 11（或 /write-volume 1 --from 11）

STEP 1: PLAN ─────────────────────────────────────────
  输入：
    novel_memory/story/outline/volume_map.md
    novel_memory/state/hooks.json
    novel_memory/state/current_state.json（如存在）
    novel_memory/state/character_states.json
    novel_memory/state/chapter_summaries.json
    novel_memory/state/workflow_state.json

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
    novel_memory/story/style/genre_profile.md（如有）

  Agent: hjw-novel-writer（加载 agents/hjw-novel-writer.prompt.md）

  产出：
    novel_memory/output/chapters/chapter_011/chapter_011.md（初稿 v1）
    novel_memory/output/chapters/chapter_011/chapter_011_delta.json

  验证：字数 2200-2500 / PRE_WRITE_CHECK 全通过


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
      └─ ROUTE: NEEDS_HUMAN → 暂停，输出3轮快照供选择

  LOCAL_PATCH：temperature 0.5，原地修补
  STRUCTURAL_REWRITE：temperature 0.7，重写标记段落


STEP 4a: REVISE ───────────────────────────────────────
  输入：
    output/chapters/chapter_011/chapter_011.md（当前版本）
    output/chapters/chapter_011/chapter_011_audit.json
    output/chapters/chapter_011/chapter_011_memo.md
    output/chapters/chapter_011/chapter_011_context.json

  Agent: hjw-novel-reviser（加载 agents/hjw-novel-reviser.prompt.md）

  产出：
    output/chapters/chapter_011/chapter_011_v{N+1}.md（版本号递增）
    output/chapters/chapter_011/revision_notes.md

  然后 → 回到 STEP 3（重新审计，revision_round + 1）


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
  □ 读取 chapter_011_delta.json（如 Structual 重写过，读最新版）
  □ 更新 novel_memory/state/hooks.json
    - 新增伏笔 → active_hooks[]
    - 推进伏笔 → advanced_count++, last_advanced_chapter, status
    - 回收伏笔 → 移至 resolved_hooks[]
    - 重新计算 budget
  □ 更新 novel_memory/state/character_states.json
    - 写入 state_history["chapter_011"] = 本章末状态
    - 更新 current_state = 本章末状态
  □ 更新 novel_memory/state/relationship_tracker.json
    - 追加 relationshipChanges 到对应关系线
  □ 更新 novel_memory/state/chapter_summaries.json
    - 追加 summaries["chapter_011"] = delta.chapterSummary
  □ 更新 novel_memory/story/character_map.md
    - 刷新人物状态总览表
    - 刷新关系矩阵
    - 追加关系变更日志行
  □ 创建快照：
    - 复制 state/ 到 snapshots/ch011/
  □ 更新 novel_memory/state/workflow_state.json
    - chapter_history["11"] = { status: "done", ... }
    - current_chapter = 12
    - current_step = "idle"
    - active_chapter 重置
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
    2. 如果 verdict = NEEDS_HUMAN → 暂停，等人类处理
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
      "simple_plan": "卷1目标：废材恢复实力，获得金手指第一层（初稿规划时生成，300字以内）",
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
