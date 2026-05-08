# polish-chapter — 单步润色

> 仅运行 Polisher Agent。要求正文已通过审计（verdict = PASS）。

---

## 调用方式

```
/polish-chapter <章节号>
/polish-chapter 11
```

---

## 前置条件

- 审计通过的正文版本存在
- `chapter_NNN_audit.json` 存在且 verdict = PASS（或 PASS_WITH_WARNINGS 且已由 Reviser 修复后通过）
- 如果 verdict = FAIL → 拒绝，提示先修订

---

## 执行流程

### Step 1：运行 Polisher

**加载 Agent**：使用 `Agent` 工具。

**Agent 输入**：
- 加载 `agents/hjw-novel-polisher.prompt.md` 作为 system prompt
- 读取：
  - 审计通过的正文版本（`chapter_NNN.md` 或 `chapter_NNN_vN.md`）
  - `chapter_NNN_audit.json`（了解被标记过的区域）
  - `revision_notes.md`（如有修订，了解改了什么）
  - `novel_memory/story/style/genre_profile.md`
  - `novel_memory/story/style/style_profile.json`
- 指令：文笔润色，不改内容（±30字上限）

**Agent 产出**：
- `chapter_NNN_v{N}_polished.md` 或 `chapter_NNN_polished.md`
- `polish_notes.md`

---

### Step 2：验证

- 字数差值 ≤ ±30 字
- 作者说区域未被修改
- 隐藏情节追踪卡未被修改
- [polisher-note] 如有结构问题发现，汇报给用户

---

### Step 3：更新 workflow_state

```
active_chapter.step = "polished"
active_chapter.final_file = "chapter_NNN_*_polished.md"
```

---

### Step 4：报告

展示：
- 润色操作统计（AI腔移除 X 处 / 句子节奏 X 处 / 感官强化 X 处 ...）
- [polisher-note] 发现的内容（如有）
- 最终稿路径
- 提示：运行 Settle 落定（`/settle-chapter NNN`）或直接用 `/write-chapter` 全流程时会自动落定
