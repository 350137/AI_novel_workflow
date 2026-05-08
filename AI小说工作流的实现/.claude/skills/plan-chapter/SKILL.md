# plan-chapter — 单步规划

> 仅运行 Planner Agent，产出 ChapterMemo + ContextPackage。不继续后续步骤。

---

## 调用方式

```
/plan-chapter <章节号>
/plan-chapter 11
```

---

## 执行流程

### Step 0：读取状态

读取 `novel_memory/state/workflow_state.json`。

如果是开卷第一章（如卷2第21章），检查该卷是否有 `detailed_plan`：
- 如果 `volume_N_detailed_plan.md` 不存在 → 先执行开卷详细规划（综合初始大纲 + 前文实际状态）

---

### Step 1：运行 Planner

**加载 Agent**：使用 `Agent` 工具。

**Agent 输入**：
- 加载 `agents/hjw-novel-planner.prompt.md` 作为 system prompt
- 读取：
  - `novel_memory/story/outline/volume_map.md`
  - `novel_memory/state/hooks.json`
  - `novel_memory/state/character_states.json`
  - `novel_memory/state/chapter_summaries.json`
  - `novel_memory/state/relationship_tracker.json`
  - 前3章 Memo + ContextPackage
- 指令：为第 N 章生成 ChapterMemo（7段完整）和 ContextPackage

**Agent 产出**：
- `novel_memory/output/chapters/chapter_NNN/chapter_NNN_memo.md`
- `novel_memory/output/chapters/chapter_NNN/chapter_NNN_context.json`

---

### Step 2：验证

- Memo 7 段完整性
- ContextPackage 5 条硬规则
- 钩子类型与前章不重复（不连续3章同类型）
- 伏笔预算不超（活跃≤12，本章新埋≤2）

---

### Step 3：报告

向用户展示 Memo 摘要（goal + 任务列表 + 钩子类型 + 扣留项），让人类可快速审阅。不阻塞——如果人类不干预，可以直接 `/write-chapter-only N` 继续。
