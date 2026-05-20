# story-init — 新书初始化：头脑风暴 + 大纲规划

> 一条命令完成：题材确定 → 世界观搭建 → 角色创建 → 卷大纲 → 状态文件初始化
> 对应 Agent：hjw-novel-advisor → hjw-novel-planner（Phase A）

---

## 调用方式

```
/story-init "一句话创作想法"
```

如果已完成部分初始化，直接 `/story-init` 会检测已有文件并询问如何处理。

---

## 执行流程

### Step 0：启动检查与冲突处理

检测 `novel_memory/story/` 下已有文件：

- **完全空** → 继续 Step 1
- **部分存在** → 列出已有文件清单，逐文件询问用户：
  - 保留（不动）
  - 覆盖（重新生成）
  - 参考（基于它重新生成，保留可用的部分）
- 用户逐文件确认后继续

---

### Step 1：Advisor Phase 1 — 多轮收敛提问

**加载 Agent**：`D:\小说\AI小说工作流的实现/agents/hjw-novel-advisor.prompt.md`

交互式对话：
- Q0 题材锚定 → 用户回答
- Q1-Q7 根据题材自适应追问（1-3 轮，每轮 ≤4 题）
- Advisor 判断信息充分后 → 进入 Step 2

---

### Step 2：Advisor Phase 2+3 — 方案生成 + 矛盾标记

生成 Foundation 并做综合校验：
- `novel_memory/story/outline/story_frame.md`
- `novel_memory/story/outline/act_structure.md`
- `novel_memory/story/outline/volume_map.md`（前 3 卷）
- `novel_memory/story/roles/<角色名>.md`（≥3 主要 + 3-5 次要）
- `novel_memory/story/pending_hooks.md`
- `novel_memory/story/writing_tips.md`
- 矛盾标记列表（如有）

---

### 闸门1：逐文件审批

按以下顺序逐一展示每个产出文件的摘要，人工审阅讨论：

| 顺序 | 文件 | 展示要点 |
|------|------|---------|
| 1 | `story_frame` | 核心命题 / 世界观铁律 / 终局方向 / 4 种结局选项 |
| 2 | `act_structure` | 三幕节拍 / Save the Cat 5 个 ★ 节拍 |
| 3 | `volume_map`（前 3 卷） | 各卷主题 / OKR / 不可逆事件 / 卷间钩子 |
| 4 | 每个角色 | 核心标签 / 性格剖面 / 成长弧线 / 禁止行为 |
| 5 | `pending_hooks` | 核心伏笔列表（core_hook=true 的 3-7 条） |
| 6 | `writing_tips` | 风险预警 / 对标差异点 |
| 7 | 矛盾标记 | 维度矛盾 + 3 选 1 方案 |

每文件确认后进入下一个。用户可对任一文件选择：确认 / 修改 / 重做。

全部确认后 → Step 3（Advisor Phase 4 迭代 + Phase 5）。如有修改意见 → Advisor 只改被指出的部分，重新输出后再次闸门确认。

---

### Step 3：Advisor Phase 4+5 — 迭代定稿 + Genre Profile

全部确认后，Advisor 执行：
- Phase 4：根据闸门1的修改意见调整被指出的部分
- Phase 5：生成 `novel_memory/story/style/genre_profile.md`

---

### Step 4：Planner Phase A — 卷大纲 + 状态文件初始化

**加载 Agent**：`D:\小说\AI小说工作流的实现/agents/hjw-novel-planner.prompt.md`

**输入**：Advisor 产出的全部 Foundation + Genre Profile

执行：
- Step A1-A6：卷理解 → 情节单元表 → 节奏分布+情绪曲线 → 伏笔分配 → 三幕映射 → 时间线验证
- 前 3 卷的卷级大纲（`volume_1_outline.md` / `volume_2_outline.md` / `volume_3_outline.md`）

---

### 闸门2：卷大纲审批

展示：
- 每卷核心命题 + 情绪弧线
- 情节单元分解表
- 节奏分布 + 情绪曲线（章号×情绪值）
- 伏笔分配计划（core_hook 推进节点）
- 钩子轮换表

确认 → Step 5。有修改 → Planner 根据反馈调整，重新输出。

---

### Step 5：状态文件初始化（Planner Step A8）

卷大纲审批通过后，创建 `novel_memory/state/` 下的状态文件骨架：

| 文件 | 内容 |
|------|------|
| `novel_memory/state/hooks.md` | 从 `pending_hooks.md` 导入初始伏笔，填充活跃表 |
| `novel_memory/state/chapter_summaries.md` | 表头——后续 Settler 逐章追加 |
| `novel_memory/state/relationship_tracker.md` | 为已有角色对创建关系线骨架 |
| `novel_memory/state/volumes.md` | 从 `volume_map.md` 提取前 3 卷信息 |
| `novel_memory/state/workflow_state.md` | 初始进度：当前章=1，状态=idle |

格式见 `references/临时格式.md`。

---

### Step 6：完成

```
📊 《<书名>》story-init 完成

✅ 世界观铁律：<N> 条
✅ 主要角色：<N> 个
✅ Genre Profile：已生成
✅ 卷大纲：前 3 卷已规划
✅ 状态文件：5 个 state MD 已初始化

📋 下一步：使用 /story-still 1 开始逐章写作
```

---

## 设计说明

### 为什么只出前 3 卷

前 3 卷通常覆盖 100-200 章，足够规划主角的完整成长弧线。后续卷的结构会在写作过程中根据实际演化调整。

### 如果部分文件已存在

Step 0 检测到已有文件时，逐文件询问。不会自动覆盖。

### 角色文件格式

角色文件包含静态档案（Advisor 产出）+ 状态追踪表（Settler 逐章追加）。格式见 `references/advisor/人物.md` 和 `references/临时格式.md`。

### book_rules

`book_rules` 不是独立输出文件——其内容分散在 `genre_profile`（世界铁律/战力/禁止事项）和各角色文件（性格锁定/行为约束）中。
