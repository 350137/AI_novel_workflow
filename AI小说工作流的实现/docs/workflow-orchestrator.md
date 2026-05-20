# 工作流编排逻辑

> 本文档是当前工作流的唯一权威编排说明。Skill 文件和 Agent prompt 以此为准。

---

## 一、系统总览

### 两个 Skill

| Skill         | 用途                                                   | 入口                      |
| ------------- | ---------------------------------------------------- | ----------------------- |
| `story-init`  | 新书初始化：头脑风暴 → 卷大纲 → 状态文件                              | `/story-init "想法"`      |
| `story-still` | 逐章写作：Plan → Write → Audit → Revise → Polish → Settle | `/story-still N --to M` |

### 七个 Agent

| Agent | 职责 | 核心 Reference |
|-------|------|---------------|
| Advisor | 收敛提问 → 方案生成 → 矛盾标记 → Genre Profile | `references/advisor/` (5个) |
| Planner | Phase A 卷大纲 + Phase B 逐章 Memo + ContextPackage | `references/planner/大纲设计.md` |
| Writer | ChapterMemo → 章节正文 | `references/writer/` (4个) |
| Auditor | 42维三层审计 → AuditReport | `references/auditor/维度表.md` |
| Reviser | LOCAL修补 / STRUCTURAL重写 | `references/reviser/修订规则.md` |
| Polisher | 文笔润色（不改内容，±30字） | `references/polisher/润色规则.md` |
| Settler | 读终稿 → 更新全部 state MD 文件 | `references/临时格式.md` |

---

## 二、目录结构

```
项目根目录/
├── agents/                          # 7 个 Agent prompt
├── references/                      # 领域知识 Reference
│   ├── advisor/                     # 题材/剧情/世界观/人物/校验
│   ├── planner/                     # 大纲设计
│   ├── writer/                      # 写作技法/hook/自查
│   ├── auditor/                     # 维度表
│   ├── reviser/                     # 修订规则
│   ├── polisher/                    # 润色规则
│   ├── golden-lines-guide.md        # 金句锻造
│   └── 临时格式.md                  # MD 状态文件格式定义
├── .claude/skills/
│   ├── story-init/SKILL.md
│   └── story-still/SKILL.md
├── scripts/
│   └── check_wordcount.py           # 字数统计工具
├── genre_refactor/genre_profiles/   # 多题材模板库
├── docs/
│   ├── 输入输出统计.md               # 每个 Agent 的 I/O 详表
│   └── workflow-orchestrator.md     # 本文档
└── novel_memory/
    ├── story/
    │   ├── outline/                 # story_frame / act_structure / volume_map / volume_N_outline
    │   ├── roles/<角色名>.md         # 静态档案 + 状态追踪表
    │   ├── style/genre_profile.md   # 本书 Genre Profile
    │   ├── pending_hooks.md         # 初始伏笔池
    │   └── writing_tips.md          # 创作建议
    ├── state/                       # Settler 写入，Planner/Auditor 读取
    │   ├── hooks.md                 # 伏笔台账
    │   ├── chapter_summaries.md     # 章节摘要
    │   ├── relationship_tracker.md  # 关系追踪
    │   ├── volumes.md               # 卷进度
    │   └── workflow_state.md        # 工作流状态
    └── output/chapters/chapter_NNN/ # 逐章产出
```

---

## 三、story-init 流程

```
/story-init "我想写一个废材逆袭玄幻小说"
        │
   Step 0：冲突检测
     已有文件？→ 逐文件问：保留/覆盖/参考
        │
   Step 1：Advisor Phase 1 — 多轮收敛提问
     Q0 题材锚定 → Q1-Q7 → 1-3轮追问
        │
   Step 2：Advisor Phase 2+3 — 方案生成 + 矛盾标记
     产出：story_frame / act_structure / volume_map（前3卷）
           roles / pending_hooks / writing_tips
        │
   ┌─ 闸门1：逐文件审批 ───────────────────┐
   │  story_frame → act_structure → volume_map
   │  → 每个角色 → pending_hooks → writing_tips
   └────────────────────────────────────────┘
        │ 确认
   Step 3：Advisor Phase 4+5 — 迭代定稿 + Genre Profile
        │
   Step 4：Planner Phase A — 前3卷卷大纲
        │
   ┌─ 闸门2：卷大纲审批 ───────────────────┐
   │  卷理解 / 情节单元表 / 节奏分布 /
   │  情绪曲线 / 伏笔分配 / 钩子轮换表
   └────────────────────────────────────────┘
        │ 确认
   Step 5：状态文件初始化
     创建 hooks.md / chapter_summaries.md /
     relationship_tracker.md / volumes.md /
     workflow_state.md
        │
   ✅ story-init 完成 → /story-still 1
```

---

## 四、story-still 流程

### 单章（`/story-still N`）

```
Step 0：PRE_FLIGHT_CHECK
  memo.md 不存在？→ Step 1 自动执行 Planner Phase B
  memo.md 存在？→ 跳过 Step 1

Step 1：Planner Phase B → memo.md + context.md

Step 2：Writer → v1.md

Step 3：Auditor → audit_round{N}.json
    ├─ PASS → Step 5
    ├─ PASS_WITH_WARNINGS（全 LOCAL）→ Step 4 → 回 Step 3
    ├─ PASS_WITH_WARNINGS（含 STRUCTURAL）→ Step 4 → 回 Step 3
    ├─ FAIL（含敏感内容）→ HUMAN_ESCALATE
    └─ FAIL（其他）→ Step 4 → 回 Step 3

Step 4：Reviser
    LOCAL_PATCH → temp 0.5，原地修补
    STRUCTURAL_REWRITE → temp 0.7，重写
    → v{N+1}.md + revision_notes_v{N}.md → 回 Step 3

Step 5：Polisher → v{N+1}.md + polish_notes_v{N}.md

Step 6：Settler → 更新 6 个 state MD 文件

Step 7：workflow_state.md 写回 → idle
```

### 批量（`/story-still N --to M --kp K`）

```
for chapter in N..M:
    执行单章完整流程
    Settler 完成 → 自动 Planner Phase B(chapter+1)
    每 K 章 → Checkpoint 暂停（展示审计趋势/角色状态/关系变化/伏笔/卷进度）
```

### 版本号规则

```
Writer   → v1.md（始终第一版）
Auditor  → 读 v{N}.md（目录下最大号）→ 写 audit_round{N}.json
Reviser  → 读 v{N}.md → 写 v{N+1}.md + revision_notes_v{N+1}.md
Polisher → 读 v{N}.md → 写 v{N+1}.md + polish_notes_v{N+1}.md
Settler  → 读 v{N}.md（目录下最大号）
```

### 3 轮上限

```
audit_round3.json 存在且 verdict ≠ PASS → HUMAN_ESCALATE
暂停，展示 v1/v2/v3 快照供人类选择
```

---

## 五、路由逻辑（硬编码，不依赖 LLM）

```
Auditor 产出 audit_round{N}.json，包含：
  - verdict: PASS / PASS_WITH_WARNINGS / FAIL
  - routeRecommendation: POLISH / LOCAL_PATCH / STRUCTURAL_REWRITE / HUMAN_ESCALATE
  - issues[].category: LOCAL / STRUCTURAL

路由判定：
  PASS → Polisher
  PASS_WITH_WARNINGS + 全 LOCAL → LOCAL_PATCH → Reviser
  PASS_WITH_WARNINGS + 含 STRUCTURAL → STRUCTURAL_REWRITE → Reviser
  FAIL + 含敏感内容 → HUMAN_ESCALATE
  FAIL（其他）→ STRUCTURAL_REWRITE → Reviser
  3 轮后仍 FAIL → HUMAN_ESCALATE
```

---

## 六、状态文件维护

| 文件 | Planner 创建 | Settler 更新 | 消费者 |
|------|:---:|:---:|--------|
| `hooks.md` | 初始化（从 pending_hooks） | 每章追加/修改 | Planner B, Auditor |
| `chapter_summaries.md` | 创建表头 | 每章追加一行 | Planner B |
| `relationship_tracker.md` | 创建骨架 | 有实质变化时追加 | Auditor |
| `volumes.md` | 创建初始行 | 更新完成数+KR% | Planner B |
| `workflow_state.md` | 写入初始值 | 每章更新进度 | Skill（恢复） |
| `roles/<X>.md` 状态表 | — | 每章追加一行 | Planner B, Writer, Auditor, Reviser |

---

## 七、人工闸门

| 位置 | 触发点 |
|------|--------|
| story-init 闸门1 | Advisor 方案产出后——逐文件审批 |
| story-init 闸门2 | Planner 卷大纲产出后——卷理解/节奏/伏笔审批 |
| story-still 用户打断 | 任意步骤——告知当前进度+下一步，给 A-G 选项 |
| Auditor HUMAN_ESCALATE | 敏感内容 / 3轮仍 FAIL |
| Checkpoint | 批量模式每 K 章暂停 |

---

## 八、文件命名一览

### 章节目录（`chapter_NNN/`）

| 文件 | 产出者 |
|------|--------|
| `chapter_NNN_memo.md` | Planner |
| `chapter_NNN_context.md` | Planner |
| `chapter_NNN_v1.md` | Writer |
| `chapter_NNN_v{N}.md` | Reviser / Polisher（版本递增） |
| `chapter_NNN_audit_round1.json` | Auditor |
| `revision_notes_v{N}.md` | Reviser |
| `polish_notes_v{N}.md` | Polisher |

### 卷大纲

| 文件 | 产出者 |
|------|--------|
| `novel_memory/story/outline/volume_N_outline.md` | Planner |
