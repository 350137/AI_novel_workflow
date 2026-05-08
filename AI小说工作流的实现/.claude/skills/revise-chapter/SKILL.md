# revise-chapter — 单步修订

> 仅运行 Reviser Agent。要求 AuditReport 已存在。

---

## 调用方式

```
/revise-chapter <章节号>
/revise-chapter 11
```

---

## 前置条件

- 正文文件存在
- `chapter_NNN_audit.json` 存在（verdict ≠ PASS）
- `chapter_NNN_memo.md` 存在
- 如果 verdict = PASS → 拒绝修订，提示直接运行 `/polish-chapter NNN`

---

## 执行流程

### Step 1：确定路由

读取 `chapter_NNN_audit.json`：
- 所有 issues LOCAL → LOCAL_PATCH（temperature 0.5）
- 存在 issues STRUCTURAL → STRUCTURAL_REWRITE（temperature 0.7）
- 存在 CRITICAL + 敏感内容 → 拒绝，提示 HUMAN_ESCALATE

---

### Step 2：运行 Reviser

**加载 Agent**：使用 `Agent` 工具。

**Agent 输入**：
- 加载 `agents/hjw-novel-reviser.prompt.md` 作为 system prompt
- 读取：
  - 当前最新版本正文
  - `chapter_NNN_audit.json`
  - `chapter_NNN_memo.md`
  - `chapter_NNN_context.json`（STRUCTURAL 重写时需要）
- 指令：根据 AuditReport 执行 LOCAL 修补或 STRUCTURAL 重写

**Agent 产出**：
- `chapter_NNN_v{N+1}.md`（版本号 +1）
- `revision_notes.md`
- `chapter_NNN_delta_revised.json`（仅 STRUCTURAL 重写时需要）

---

### Step 3：更新 workflow_state

```
active_chapter.current_version = N+1
active_chapter.source_file = "chapter_NNN_v{N+1}.md"
active_chapter.revision_round += 1
active_chapter.step = "revised"
```

---

### Step 4：报告

展示修订摘要：
- 修订类型（LOCAL / STRUCTURAL）
- 处理了哪些 issue
- 版本号
- 发现的 [reviser-note] 问题（如有）
- 提示：需要运行 `/audit-chapter NNN --version v{N+1}` 重新审计
