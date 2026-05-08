# write-chapter-only — 单步写作

> 仅运行 Writer Agent。要求 ChapterMemo + ContextPackage 已存在。

---

## 调用方式

```
/write-chapter-only <章节号>
/write-chapter-only 11
```

---

## 前置条件

- `chapter_NNN_memo.md` 存在
- `chapter_NNN_context.json` 存在
- 如果不存在 → 报错，提示先运行 `/plan-chapter NNN`

---

## 执行流程

### Step 1：运行 Writer

**加载 Agent**：使用 `Agent` 工具。

**Agent 输入**：
- 加载 `agents/hjw-novel-writer.prompt.md` 作为 system prompt
- 读取：
  - `output/chapters/chapter_NNN/chapter_NNN_memo.md`
  - `output/chapters/chapter_NNN/chapter_NNN_context.json`
  - `novel_memory/story/style/style_profile.json`
  - `novel_memory/story/style/genre_profile.md`（如有）
- 指令：生成第 N 章正文

**Agent 产出**：
- `novel_memory/output/chapters/chapter_NNN/chapter_NNN.md`（v1 初稿）
- `novel_memory/output/chapters/chapter_NNN/chapter_NNN_delta.json`

---

### Step 2：验证

- 字数 2200-2500
- 包含作者说 + 隐藏情节追踪卡
- PRE_WRITE_CHECK 全部通过（检查 Agent 输出中的 writerNotes）

---

### Step 3：更新 workflow_state

```
workflow_state.active_chapter.step = "written"
workflow_state.active_chapter.current_version = 1
workflow_state.active_chapter.source_file = "chapter_NNN.md"
```

---

### Step 4：报告

展示：字数 / 钩子类型 / 本章摘要（从 delta 提取）/ 伏笔活动概要
