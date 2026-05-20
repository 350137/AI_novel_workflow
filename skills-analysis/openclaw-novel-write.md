# openclaw-novel-write 功能拆解报告

## 基本信息
- **类型**：Claude Code Skill（OpenClaw 生态，命令驱动型）
- **版本**：0.1.2
- **触发条件**：通过 `/novel <command>` 命令调用，共15个命令（init/constitution/specify/clarify/plan/timeline/track-init/tasks/write/analyze/diagram/feedback/learnings/fail-log/track）
- **核心机制**：7步强制前置工作流（init→constitution→specify→clarify→plan→timeline→track-init→tasks→write）+ 知识库系统（genres/styles/requirements）

## 功能维度分析

### 1. 世界观构建
- **覆盖度**：⚡ 部分覆盖
- **实现方式**：spec/knowledge/ 知识库目录存储世界观；constitution.md 定义创作宪法（核心价值观/质量标准/风格准则）；specification.md 定义故事需求
- **独特亮点**：constitution.md 是宪法级别的约束——所有后续产出必须遵守

### 2. 人物设定
- **覆盖度**：✅ 核心功能
- **实现方式**：spec/tracking/character-state.json（结构化角色状态追踪）；spec/tracking/relationships.json（关系网络矩阵）；clarify-answers.md 澄清角色关键决策
- **独特亮点**：角色状态 JSON 化——结构化、可追踪、可回滚；关系网络独立于角色档案存储

### 3. 情节设计
- **覆盖度**：✅ 核心功能
- **实现方式**：creative-plan.md（创作计划）；timeline.md（时间线——写作前必须对照）；tasks.md（任务分解）+ tasks-volume-*.md（卷级任务）；spec/tracking/plot-tracker.json（情节追踪——plotlines/foreshadowing/milestones）
- **独特亮点**：时间线是独立文件，写作前必须对照——防止时间线矛盾；任务分解到卷级别

### 4. 章节创作
- **覆盖度**：✅ 核心功能
- **实现方式**：6阶段写作流程——预写分析→初稿生成→自检→文笔润色→修订→元数据输出；8个前置条件检查（缺少任一步骤禁止写作）；10步完成后行动（字数验证/追踪验证/质量分析）；context-aware 上下文加载（按优先级：constitution→spec→plan→timeline→tracking→knowledge→content→style）
- **独特亮点**：前置条件强制检查（8步缺一不可）；6阶段写作是最详细的单章流程；自检阶段明确标注"停在阶段3不继续"；字数验证用 bash 脚本而非 LLM（确定性）

### 5. 一致性审查
- **覆盖度**：✅ 核心功能
- **实现方式**：`/novel track --check`（角色一致性/情节进度/线索推进）；`/novel analyze`（每5章强制：一致性/节奏/视角/对话质量）；自检阶段4项（时间线/伏笔揭晓/角色状态/前文连贯）；`/novel fail-log` 记录失败场景
- **独特亮点**：每章追踪验证 + 每5章质量分析的层次化审查；审查失败阻断后续写作（硬门控）

### 6. 文风控制
- **覆盖度**：✅ 核心功能
- **实现方式**：writing-style + writing-requirements YAML 配置（如 natural-voice + anti-ai-v4 + fast-paced）；AI高频词黑名单（9组禁用词+替换方案）；具象化原则（时间/人物/数量三抽象→具体）；单句成段比例 30%-50%；段字数 50-100字；5个风格 knowledge-base requirements 文件（anti-ai-v3/v4/fast-paced/no-poison/romance-angst/sweet/serious-literature/strong-emotion）
- **独特亮点**：反AI检测写作规范最完善（4版本迭代）；风格和规范模块化为独立文件（可组合）；具象化三原则覆盖全面

### 7. 平台适配
- **覆盖度**：❌ 不涉及
- **实现方式**：无特定平台适配
- **独特亮点**：无

### 8. 协作与迭代
- **覆盖度**：✅ 核心功能
- **实现方式**：15个命令构成的完整 CLI 体系；7步前置工作流强制线性执行；progress.json 进度追踪；fail-log.md 失败记录；learnings.md 学习沉淀；spec/tracking 目录下结构化状态文件（JSON）支持程序化读取
- **独特亮点**：命令最多（15个），流水线覆盖最全；结构化状态文件（JSON）最适合程序化集成；learnings 机制从失败中提取可复用模式

## 总结
- **核心优势**：命令最全面（15个）；前置条件强制检查最严格（8步缺一不可）；反AI检测规范最完善（v4版本+5个requirements文件）；结构化追踪文件（JSON）最适合程序化集成；6阶段写作流程最详细
- **主要局限**：依赖 OpenClaw 生态；命令繁多学习曲线陡峭；无本地 NLP 能力（纯 LLM + 文件驱动）；版本尚低（0.1.2）可能在快速迭代
- **最佳适用场景**：需要严格流程管控的长篇小说项目；OpenClaw 生态用户；对AI味零容忍的写作场景
- **在双终端工作流中的建议定位**：Terminal A 策划端 —— 项目初始化+前置工作流管控+风格配置；或作为独立工作流的流程管控参考
