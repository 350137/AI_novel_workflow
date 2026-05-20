# 协作与迭代 — 跨 Skills/项目比对报告

## 覆盖度矩阵

| 分析对象 | 类型 | 覆盖度 | 实现方式 | 亮点 |
|----------|------|--------|---------|------|
| fiction-crafter | skill | ⚡ | 续写/中断恢复（8文件读取）；失败记录 ERRORS.md（6种类型）；init-novel.sh 初始化 | 失败记录沉淀为创作模式（捕获→记录→沉淀→复用） |
| novelist | skill | ⚡ | 精修输出格式（原文→精修→修改说明）；4工作区通过 memory/ 传递状态 | 修改说明列出"为什么这么改" |
| novel-writer-cn | skill | ⚡ | 框架可随反馈调整；多版本结局 | 多版本结局是迭代思维 |
| story-cog | skill | ⚡ | 跨 Agent 平台远程调用；fire-and-forget 异步模式 | 跨平台+异步 |
| story-writer | skill | ❌ | bash 脚本提供基本自动化 | — |
| my-novel-writer | skill | ✅ | 7个 CLI 命令；`--status` 进度；`--update-outline` 动态调整；JSON 记忆增量更新 | CLI 命令体系最完善；JSON 最易程序化集成 |
| openclaw-novel-write | skill | ✅ | 15个命令；7步前置工作流（线性强制）；结构化状态文件（JSON）；learnings 沉淀 | 命令最多(15)；状态文件最适合程序化 |
| tomato-novelist | skill | ✅ | 6问确认→规划确认→每章确认→每5章数据反馈；TODO list 进度管理 | 人机协作节奏最尊重人类决策权 |
| onkos | skill | ✅ | 73条命令（command_executor.py统一入口）；修订工作流（analyze→revise→clear→re-store）；engagement 系统；6级摘要；快照回滚 | 命令最多(73)；快照最安全；统一入口最整洁 |
| inkos | 项目 | ✅ | 10-Agent 编排；Consolidator 卷级压缩；Hook 全生命周期（dependsOn/coreHook/promoted/urgency公式）；快照；Daemon 模式 | 编排最精细；Consolidator 解决长篇小说核心瓶颈 |

## 共同模式

1. **CLI/命令驱动是高级 skills 的共性**：onkos（73命令）、openclaw-novel-write（15命令）、my-novel-writer（7命令）都用命令体系而非纯对话
2. **状态持久化是基础共识**：JSON/Markdown/SQLite/快照——各种存储方式但目标一致
3. **人机协作确认点**：tomato-novelist（每步确认）、openclaw-novel-write（前置检查）、onkos（Pre-flight Check）都设计了人机交互节点
4. **记忆管理是高端能力**：onkos（6级摘要+快照）、inkos（Consolidator 卷压缩）、fiction-crafter（.learnings/）都解决了长篇小说记忆衰退问题

## 差异化分析

| 特色做法 | 采用者 | 优劣分析 |
|---------|--------|---------|
| 73条命令统一入口 | onkos | ✅ 最全面 ❌ 学习曲线最陡 |
| 10-Agent 编排 | inkos | ✅ 最精细拆分 ❌ 编排复杂度最高 |
| Consolidator 卷压缩 | inkos | ✅ 解决长篇小说上下文核心瓶颈 ❌ 需LLM调用 |
| 快照回滚 | onkos + inkos | ✅ 安全 ❌ 存储成本 |
| 人机节奏设计 | tomato-novelist | ✅ 最尊重人类决策 ❌ 效率最低 |
| Hook 依赖链 | inkos | ✅ A伏笔揭晓依赖B ❌ 维护复杂度 |
| 失败记录系统 | fiction-crafter | ✅ 持续改进 ❌ 需人工维护 |
| 修订工作流 | onkos | ✅ analyze→revise→clear 防级联错误 ❌ 步骤多 |

## onkos/inkos 工作流视角

- **onkos**：这个维度的王者——73条命令、6级摘要、快照回滚、修订工作流、engagement 系统、command_executor 统一入口。onkos 的定位就是"基础设施层"，在此维度优势最大
- **inkos**：Consolidator 卷级压缩是最重要的长篇小说基础设施——每写完一卷，将240章的摘要压缩为叙事段落，释放上下文。Hook 模型的 promoted/coreHook/dependsOn 是最完善的伏笔管理

## 最佳实践推荐

- **首选方案**：**onkos**（基础设施层——命令/记忆/摘要/快照/修订/engagement）+ **inkos Hook模型**（dependsOn/coreHook/promoted/urgency公式）+ **inkos Consolidator**（卷级压缩）
- **推荐理由**：onkos 在此维度综合最强（73命令+6级摘要+快照+统一入口），inkos 贡献了两个最重要的上层设计（Hook依赖链+卷压缩）
- **可组合方案**：
  - 数据层：onkos（SQLite+6级摘要+快照+command_executor）
  - 编排层：inkos-style Orchestrator（流水线编排+Gate决策）
  - 协作层：tomato-novelist-style 确认节点（人类在每个关键节点审批）

## 空白地带

1. **无多用户协作**：没有 skill 支持多个作者同时编辑不同章节并合并
2. **无 Git 原生集成**：虽然 onkos 用 Markdown 文件（Git 可追踪），但没有 skill 提供 Git 工作流（分支/PR/合并冲突解决）
3. **无 Agent 间通信协议**：没有统一的协议让不同 skill 的 Agent 交换消息（inkos 10-Agent 是内部编排，不跨系统）
4. **无创作分析仪表盘**：没有 skill 提供全局仪表盘（进度/质量趋势/伏笔回收率/角色出场频率等可视化）
5. **无成本追踪**：没有 skill 追踪每次 LLM 调用的 token 消耗和费用
