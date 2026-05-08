# audit-chapter — 单步审计

> 仅运行 Auditor Agent。要求正文 + Memo 已存在。

---

## 调用方式

```
/audit-chapter <章节号>
/audit-chapter 11

/audit-chapter 11 --version v2    # 审计特定版本
```

---

## 前置条件

- 正文文件存在（`chapter_NNN.md` 或指定版本）
- `chapter_NNN_memo.md` 存在
- 如果不存在 → 报错

---

## 执行流程

### Step 1：确定审计目标

如果指定 `--version v2`，审计 `chapter_NNN_v2.md`。
否则审计当前最新版本（从 workflow_state 获取）。

---

### Step 2：运行 Auditor

**加载 Agent**：使用 `Agent` 工具。

**Agent 输入**：
- 加载 `agents/hjw-novel-auditor.prompt.md` 作为 system prompt
- 读取：
  - 目标正文文件
  - `chapter_NNN_memo.md`
  - `novel_memory/state/hooks.json`
  - `novel_memory/state/character_states.json`
- 指令：执行40维三层审计

**Agent 产出**：
- `novel_memory/output/chapters/chapter_NNN/chapter_NNN_audit.json`

---

### Step 3：报告

展示：
- overallScore + verdict
- issues 列表（按 severity 排序，CRITICAL/HIGH 醒目）
- Layer 分数分解
- 路由推荐（LOCAL_PATCH / STRUCTURAL_REWRITE / POLISH）
- 如果 FAIL：列出所有需要修复的 issue

---

### Step 4：更新 workflow_state

```
追加到 active_chapter.audit_history[]
active_chapter.step = "audited"
```
