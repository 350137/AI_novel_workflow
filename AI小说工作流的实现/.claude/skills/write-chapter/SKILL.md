# write-chapter — 全自动单章流水线

> 一条命令跑完整章：Plan → Write → Audit → (Revise)×N → Polish → Settle

---

## 调用方式

```
/write-chapter <章节号>
/write-chapter 11
```

---

## 执行流程

### Step 0：读取状态

读取 `novel_memory/state/workflow_state.json`，确认当前进度。如果 active_chapter 不是 idle 状态（说明上一章流水线中断），先报告中断点，让人类决定从哪步继续。

---

### Step 1：PLAN

如果 `chapter_N_memo.md` 已存在且人类要求复用，跳过此步。

**加载 Agent**：使用 `Agent` 工具，subagent_type 为通用 agent。

**Agent 输入**：
- 加载 `agents/hjw-novel-planner.prompt.md` 作为 system prompt
- 读取以下文件作为上下文：
  - `novel_memory/story/outline/volume_map.md`
  - `novel_memory/state/hooks.json`
  - `novel_memory/state/character_states.json`
  - `novel_memory/state/chapter_summaries.json`
  - `novel_memory/state/relationship_tracker.json`
  - 前3章 Memo（如存在）
- 指令：为第 N 章生成 ChapterMemo 和 ContextPackage

**Agent 产出**：
- `novel_memory/output/chapters/chapter_NNN/chapter_NNN_memo.md`
- `novel_memory/output/chapters/chapter_NNN/chapter_NNN_context.json`

**验证**：
- Memo 包含完整 7 段
- ContextPackage 的 selectedContexts 和 excludedContexts 符合 5 条硬规则

---

### Step 2：WRITE

**加载 Agent**：使用 `Agent` 工具。

**Agent 输入**：
- 加载 `agents/hjw-novel-writer.prompt.md` 作为 system prompt
- 读取：
  - `output/chapters/chapter_NNN/chapter_NNN_memo.md`
  - `output/chapters/chapter_NNN/chapter_NNN_context.json`
  - `novel_memory/story/style/style_profile.json`
  - `novel_memory/story/style/genre_profile.md`（如有）
- 指令：生成第 N 章正文 + StateDelta

**Agent 产出**：
- `novel_memory/output/chapters/chapter_NNN/chapter_NNN.md`（初稿 v1）
- `novel_memory/output/chapters/chapter_NNN/chapter_NNN_delta.json`

**验证**：
- 字数 2200-2500（正文，不计作者说和追踪卡）
- 章节格式包含：正文 + 作者说 + 隐藏情节追踪卡

---

### Step 3：AUDIT

**加载 Agent**：使用 `Agent` 工具。

**Agent 输入**：
- 加载 `agents/hjw-novel-auditor.prompt.md` 作为 system prompt
- 读取：
  - `output/chapters/chapter_NNN/chapter_NNN.md`（当前最新版本）
  - `output/chapters/chapter_NNN/chapter_NNN_memo.md`
  - `novel_memory/state/hooks.json`
  - `novel_memory/state/character_states.json`
- 指令：审计本章正文

**Agent 产出**：
- `novel_memory/output/chapters/chapter_NNN/chapter_NNN_audit.json`

---

### Step 4：GATE 决策（硬编码，不调 Agent）

读取 `chapter_NNN_audit.json`：

```
revision_round = workflow_state.active_chapter.revision_round

如果 verdict = "PASS":
  → 进入 Step 5（POLISH）

如果 verdict = "PASS_WITH_WARNINGS":
  - 所有 issues.category = LOCAL → LOCAL_PATCH → Step 4a
  - 存在 issues.category = STRUCTURAL → STRUCTURAL_REWRITE → Step 4a

如果 verdict = "FAIL":
  - 存在 CRITICAL + dimension = "敏感内容" → HUMAN_ESCALATE，暂停汇报
  - 其他 → STRUCTURAL_REWRITE → Step 4a

如果 revision_round >= 3:
  → NEEDS_HUMAN，暂停，输出3轮审计历史和快照路径
```

---

### Step 4a：REVISE

**加载 Agent**：使用 `Agent` 工具。

**Agent 输入**：
- 加载 `agents/hjw-novel-reviser.prompt.md` 作为 system prompt
- 读取：
  - 当前最新版本的正文（`chapter_NNN.md` 或 `chapter_NNN_vN.md`）
  - `chapter_NNN_audit.json`
  - `chapter_NNN_memo.md`
  - `chapter_NNN_context.json`
- 指令：根据 AuditReport 修订正文

**Agent 产出**：
- `chapter_NNN_v{N+1}.md`（版本号递增）
- `revision_notes.md`

**然后**：
- 追加 audit_history
- revision_round += 1
- 回到 Step 3（重新审计）

---

### Step 5：POLISH

**加载 Agent**：使用 `Agent` 工具。

**Agent 输入**：
- 加载 `agents/hjw-novel-polisher.prompt.md` 作为 system prompt
- 读取：
  - 审计通过的正文版本
  - `chapter_NNN_audit.json`
  - `novel_memory/story/style/genre_profile.md`
- 指令：文笔润色，不改内容

**Agent 产出**：
- `chapter_NNN_v{N}_polished.md`（或 `chapter_NNN_polished.md` 如果 v1 直通）
- `polish_notes.md`

---

### Step 6：SETTLE（纯工具调用，不调 Agent）

依次执行以下操作：

```
□ 读取 delta.json
□ 更新 hooks.json（plant/advance/resolve/defer + 重算 budget + promoted 升格检查）
□ 更新 character_states.json（追加 state_history + 更新 current_state）
□ 更新 relationship_tracker.json（追加 progression）
□ 更新 chapter_summaries.json（追加本章摘要）
□ 更新 character_map.md（刷新状态表 + 关系矩阵 + 变更日志）
□ 创建快照：复制 state/*.json 到 snapshots/chNNN/
□ 更新 workflow_state.json：
    chapter_history[N] = { status: "done", audit_score, revisions, final_file }
    current_chapter = N+1
    current_step = "idle"
    active_chapter 重置
```

---

### Step 7：报告

向用户汇报：
- 本章标题 + 最终审计分数
- 经历了多少轮修订
- 最终稿路径
- 如有 [polisher-note] 发现的结构问题，醒目提示
- 伏笔状态变更摘要
- 下一章 ready
