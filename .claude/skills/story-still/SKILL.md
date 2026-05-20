# story-still — 逐章写作流水线

> 单章全自动流程：Plan → Write → Audit → [Revise] → Polish → Settle
> 支持批量模式和中断恢复

---

## 调用方式

```
/story-still N                      → 单章
/story-still N --to M               → 批量 N 到 M 章
/story-still N --to M --kp K → 每 K 章暂停（默认 5）
```

无参数时，读取 `workflow_state.md` 从中断点恢复。

---

## 前置条件

- `novel_memory/story/style/genre_profile.md` 必须存在
- `novel_memory/state/` 下 5 个 MD 文件必须存在（由 story-init 创建）
- 如缺失 → 阻断，提示先运行 `/story-init`

---

## 执行流程（单章）

### Step 0：PRE_FLIGHT_CHECK

```
检查第 N 章目录下：
□ memo.md 存在？ → 跳过 Step 1
□ memo.md 不存在？ → 执行 Step 1（自动运行 Planner Phase B）
```

### Step 1：Planner Phase B（自动）

**Agent**：`D:\小说\AI小说工作流的实现/agents/hjw-novel-planner.prompt.md`（Phase B）

读入：N-1 章状态文件（hooks.md / chapter_summaries.md / roles 状态表）→ 产出 memo.md + context.md

### Step 2：Writer

**Agent**：`D:\小说\AI小说工作流的实现/agents/hjw-novel-writer.prompt.md`

产出：`chapter_NNN_v1.md`

### Step 3：Auditor

**Agent**：`D:\小说\AI小说工作流的实现/agents/hjw-novel-auditor.prompt.md`

产出：`chapter_NNN_audit_round{N}.json`

读取 `audit_round{N}.json` 的 `verdict` 和 `routeRecommendation`：

```
verdict = PASS → Step 5（Polisher）

verdict = PASS_WITH_WARNINGS：
  ├─ 全部 issues.category = LOCAL → Step 4（Reviser → LOCAL_PATCH）
  └─ 任一 issues.category = STRUCTURAL → Step 4（Reviser → STRUCTURAL_REWRITE）

verdict = FAIL：
  ├─ 含 CRITICAL + dimension = "敏感内容" → HUMAN_ESCALATE
  └─ 其他 → Step 4（Reviser → STRUCTURAL_REWRITE）
```

### Step 4：Reviser

**Agent**：`D:\小说\AI小说工作流的实现/agents/hjw-novel-reviser.prompt.md`

- LOCAL_PATCH → temp 0.5，原地修补
- STRUCTURAL_REWRITE → temp 0.7，重写

产出：`chapter_NNN_v{N+1}.md` + `revision_notes_v{N}.md`

**迭代控制**：
- 修订后回到 Step 3（重审计）
- 第 3 轮审计后仍 FAIL → HUMAN_ESCALATE
- 判断依据：`audit_round3.json` 存在且 verdict ≠ PASS

### Step 5：Polisher

**Agent**：`D:\小说\AI小说工作流的实现/agents/hjw-novel-polisher.prompt.md`

读入：当前最高版本 `v{N}.md` + 最新 `audit_round{N}.json` + `revision_notes_v{N}.md`（如存在）

产出：`chapter_NNN_v{N+1}.md` + `polish_notes_v{N}.md`

### Step 6：Settler（自动，不确认）

**Agent**：`D:\小说\AI小说工作流的实现/agents/hjw-novel-settler.prompt.md`

读入：目录下最高版本 `v{N}.md`

更新：hooks.md / chapter_summaries.md / relationship_tracker.md / volumes.md / workflow_state.md / roles 状态表

### Step 7：写回 workflow_state

```
当前章：N+1（批量模式）/ idle（单章完成）
状态：idle
已落定：追加 N
```

---

## 批量模式

```
for chapter in N..M:
    执行 Step 0-7（单章完整流程）
    Settler 完成后：
        workflow_state.当前章 = chapter + 1
        → 自动进入 Planner Phase B（chapter + 1）
    如果 chapter % checkpoint == 0：
        → Checkpoint 暂停
```

### Checkpoint 展示

```
📊 Checkpoint — 第 X-Y 章（共 K 章）

审计趋势：
  第 N 章  XX  PASS/PASS_WITH_WARNINGS/FAIL

角色状态：
  <角色名>：<旧状态> → <新状态>（第 X 章）

角色关系：
  <角色A>↔<角色B>：<旧阶段> → <新阶段>（第 X 章）

伏笔：
  活跃 X/12  |  本期回收 H00X, H00Y  |  逾期 H00Z

卷进度：
  卷 N  X/T 章完成  |  KR1 XX%  KR2 XX%  KR3 XX%

选项：
  A. 继续
  B. 暂停抽查某章
  C. 调整后续节奏
```

---

## 中断处理

### 用户主动打断

```
当前进度：第 N 章 — [当前 Agent 名]
已完成：v{X}.md / audit_round{N}.json（如适用）
下一步：[Agent 名] — [做什么]

请选择：
  A. 继续
  B. 回到 Planner — 重新规划 Memo
  C. 回到 Writer — 重新生成正文
  D. 回到 Auditor — 重新审计
  E. 跳到 Polisher — 跳过审计直接润色
  F. 跳到 Settler — 直接落定当前版本
  G. 暂停 — 手动修改文件后重新触发
```

### 中断恢复

```
/story-still（无参数）

→ 读取 workflow_state.md：
    当前章 = 8, 状态 = Auditor, 版本 = v1
→ 自动从第 8 章 Auditor 步骤继续
```

---

## 版本号规则

```
Writer   → v1.md（始终第一版）
Auditor  → 读 v{N}.md（取目录下最大号）
Reviser  → 读 v{N}.md → 写 v{N+1}.md
Polisher → 读 v{N}.md → 写 v{N+1}.md
Settler  → 读 v{N}.md（取目录下最大号）
```

`audit_round{N}.json` / `revision_notes_v{N}.md` / `polish_notes_v{N}.md` 不跟随版本号——始终覆盖或按 round 编号。

---

## 文件结构（第 8 章示例）

```
novel_memory/output/chapters/chapter_008/
├── chapter_008_memo.md                   # Planner Phase B 产出
├── chapter_008_context.md                # Planner Phase B 产出
├── chapter_008_v1.md                     # Writer 产出
├── chapter_008_v2.md                     # Reviser 产出（如修订）
├── chapter_008_v3.md                     # Polisher 产出
├── chapter_008_audit_round1.json         # Auditor 第 1 轮
├── chapter_008_audit_round2.json         # Auditor 第 2 轮（如重审计）
├── revision_notes_v2.md                  # Reviser 产出（v2=修订后版本号）
└── polish_notes_v3.md                    # Polisher 产出（v3=润色后版本号）
```
