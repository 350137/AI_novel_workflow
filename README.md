# AI 小说工作流

基于 Claude Code 的多 Agent 协作式 AI 长篇小说创作流水线。将自然语言小说创作分解为可编排、可审计、可迭代的结构化步骤，由 7 个专业化 AI Agent 在人类关键节点把关下协作完成。

## 设计理念

- **职责分离**：Writer 不审自己的稿，Auditor 不动笔改文，Reviser 不做润色——每个 Agent 只做一件事，避免认知盲区
- **人类把关**：创意定型、大纲确认等关键节点设置审批闸门，人类始终拥有最终决定权
- **受控上下文**：Writer 只看到当前章节需要的 ContextPackage，而非全部真相，防止信息越界
- **工业化流水线**：借鉴 inkos（37维审计、OKR大纲）和 onkos（脚本化审计层）的工程化思路

## 项目结构

```
.
├── agents/                    # 7 个 Agent 的 prompt 定义
│   ├── hjw-novel-advisor.prompt.md    # 创意顾问 — 头脑风暴、8维创意方案
│   ├── hjw-novel-planner.prompt.md    # 大纲规划师 — 卷大纲、ChapterMemo
│   ├── hjw-novel-writer.prompt.md     # 章节生成器 — 2200-2500字正文
│   ├── hjw-novel-auditor.prompt.md    # 质量审计官 — 42维三层审计
│   ├── hjw-novel-reviser.prompt.md    # 修订官 — LOCAL修补/STRUCTURAL重写
│   ├── hjw-novel-polisher.prompt.md   # 润色官 — 仅修饰文笔，不改变内容
│   └── hjw-novel-settler.prompt.md    # 落定官 — 更新所有状态文件
│
├── .claude/skills/            # Claude Code Skill 定义
│   ├── story-init/SKILL.md           # 新书初始化（头脑风暴 + 大纲规划）
│   └── story-still/SKILL.md          # 逐章写作流水线
│
├── references/                # 领域知识参考文档
│   ├── advisor/               # 题材、剧情、世界观、人物、校验
│   ├── planner/               # 大纲设计、实战经验
│   ├── writer/                # 写作技法、钩子设计、自查清单
│   ├── auditor/               # 42维审计维度表
│   ├── reviser/               # 修订规则
│   └── polisher/              # 润色规则
│
├── novel_memory/              # 小说记忆系统（当前小说的实际数据）
│   ├── story/                 # 故事框架、角色文件、风格配置、伏笔池
│   └── state/                 # 运行时状态（钩子、摘要、关系追踪）
│
├── genre_refactor/            # 多题材通用化重构
│   ├── genre_profiles/        # 8 个题材预设模板
│   └── *.md                   # 重构方案与 Schema 定义
│
├── skills-analysis/           # 对 9 个 Claude Skills + inkos 的深度分析
├── scripts/                   # 辅助脚本
│   └── check_wordcount.py     # 章节字数检查
└── docs/                      # 工作流文档
```

## 两大工作流

### `/story-init` — 新书初始化

输入一句话想法，输出完整的故事框架与大纲：

```
Step 0  冲突检测（已有文件逐一确认）
Step 1  Advisor Phase 1 — 多轮收敛提问
Step 2  Advisor Phase 2+3 — 生成故事框架 / 三幕结构 / 卷地图 / 角色 / 伏笔池
闸门1   逐文件人工审批
Step 3  Advisor Phase 4+5 — 迭代定稿 + Genre Profile
Step 4  Planner Phase A — 前3卷卷大纲
闸门2   卷大纲人工审批
Step 5  状态文件初始化
```

用法：`/story-init "一句话想法"`

### `/story-still` — 逐章写作

按卷按章逐章生成、审计、修订、润色、落定：

```
Step 0  PRE_FLIGHT_CHECK
Step 1  Planner → ChapterMemo + ContextPackage
Step 2  Writer → 正文 v1（2200-2500字）
Step 3  Auditor → 42维三层审计报告
路由     PASS → 润色 / PASS_WITH_WARNINGS → 修订 / FAIL → 重写或人工升级
Step 4  Reviser → 修订稿（最多3轮）
Step 5  Polisher → 润色稿
Step 6  Settler → 更新所有状态文件
Step 7  写回 workflow_state
```

用法：`/story-still N --to M --kp K`

## Agent 架构

| Agent | 角色 | Temperature | 核心职责 |
|-------|------|-------------|---------|
| Advisor | 创意顾问 | 0.7 | 头脑风暴 → 8维创意方案 + Genre Profile |
| Planner | 大纲规划师 | 0.5 | 创意 → 卷级大纲 → ChapterMemo + ContextPackage |
| Writer | 章节生成器 | 0.7 | ChapterMemo → 2200-2500字正文 |
| Auditor | 质量审计官 | 0.3 | 42维三层审计 → AuditReport |
| Reviser | 修订官 | 0.5-0.8 | AuditReport → LOCAL修补或STRUCTURAL重写 |
| Polisher | 润色官 | 0.5 | 仅修饰文笔，禁改内容（字数变动 ≤30字） |
| Settler | 落定官 | 0.3 | 更新所有状态文件（伏笔/摘要/关系/进度） |

## 42维审计体系

| 层 | 名称 | 维度数 | 方法 |
|----|------|--------|------|
| Layer 1 | 脚本层 | 13维 | 正则/jieba/统计（疲劳词、违禁词、套话密度、感官分布） |
| Layer 2 | 混合层 | 8维 | 脚本预检 + LLM确认（OOC、成长停滞、备忘偏离） |
| Layer 3 | LLM层 | 19维 | 单次LLM调用（战力崩坏、信息越界、读者期待、配角工具化） |

评分公式：`overallScore = 0.15 × scriptHealth + 0.20 × hybridScore + 0.65 × llmScore`

## 当前状态

- **Agent Prompt**：全部 7 个已完成（共 ~1790 行）
- **题材模板**：8 个题材预设模板已完成
- **流水线编排**：scripts/ 和状态文件初始化待完成
- **脚本化审计**：Layer 1 正则审计脚本待实现

## 来源与致谢

本项目综合了以下来源的精华：

| 来源 | 核心贡献 |
|------|---------|
| [inkos](https://github.com/inksoul/inkos) | 37维审计、OKR大纲、ChapterMemo格式、审改润分离 |
| onkos | 脚本化审计层、6级摘要、快照回滚、五感分布 |
| fiction-crafter | 爽点节奏公式、套路重复检测 |
| novelist | 句法红线、黑名单词汇、心理锚点剥离 |
| tomato-novelist | 爆款基因、钩子轮换、情绪标签、金句锻造 |
| my-novel-writer | 写前自检、字数强制策略、违禁词替换 |
| openclaw-novel-write | 5视角读者反馈、反AI写作、时间线验证 |

## 许可

MIT
