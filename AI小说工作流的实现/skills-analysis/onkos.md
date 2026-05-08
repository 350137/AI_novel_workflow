# onkos 功能拆解报告

## 基本信息
- **类型**：Claude Code Skill（强制性小说引擎，非普通 skill）
- **版本**：1.6.3
- **依赖**：Python3 + jieba（分词）+ onnxruntime（语义模型，可选~98MB）
- **触发条件**：用户说"写小说/构思故事/续写/改章节/检查连贯性"等——强制激活
- **核心机制**：本地 NLP 引擎（非 LLM 依赖）——SQLite FTS5 全文检索 + ONNX text2vec 语义向量（768维）+ jieba 分词 + 73条命令 + 6级摘要层级 + 8步强制写作工作流

---

## 功能维度分析

### 1. 世界观构建
- **覆盖度**：✅ 核心功能
- **实现方式**：project_initializer.py 初始化项目；settings_importer.py 批量导入 Markdown 设定文档；`add-node`（type: faction/location）添加势力/地点；`import-settings` 自动去后缀（"碧落宫 (faction)"→"碧落宫"）；project_config.json 存储约束条件
- **独特亮点**：知识图谱存储（kg_nodes/kg_edges）——关系型+图数据库双存储；约束条件自动附加到 for-creation 输出；Markdown 设定文档可 Git 追踪

### 2. 人物设定
- **覆盖度**：✅ 核心功能
- **实现方式**：`create-char` 创建角色（protagonist/antagonist/mentor/sidekick/npc 5种类型）；character_simulator.py OOC 检测——增强关键词匹配+语义近似（非 LLM，确定性）；`add-edge` 添加角色关系；entity_extractor.py 自动识别角色名（含置信度：high/medium/low）
- **独特亮点**：OOC 检测用关键词+语义近似——确定性执行，零 LLM 成本；角色模拟器可独立运行；5种角色类型覆盖标准叙事角色

### 3. 情节设计
- **覆盖度**：✅ 核心功能
- **实现方式**：`create-phase`（100-300章粒度）+ `create-arc-am`（30-60章粒度）双层叙事结构；arc_manager.py 进度跟踪和下一步建议；plot_brancher.py 支线管理和分支创建；`suggest-next` 智能建议下一步（自动推断当前章节）
- **独特亮点**：Phase→Arc 双层结构是唯一的结构化叙事管理——比其他 skills 的"卷→章"更细粒度；自动推断当前进度无需手动指定

### 4. 章节创作
- **覆盖度**：✅ 核心功能
- **实现方式**：8步强制写作工作流——for-creation（获取上下文）→读大纲→写→store-chapter（自动分场景存DB）→extract-entities→detect-fact-changes→record-facts/hooks→update-summary；for-creation 返回结构化上下文：book summary→phase/arc summary→previous chapter→related facts→active hooks→engagement context；Agent 仅执行2个创造性任务（读大纲+写文本），其余6步为自动脚本
- **独特亮点**：**最核心设计**——"你不是用自己的记忆写作，你是在 for-creation 返回的上下文中严格创作"；每次写后6步自动化无法跳过（Anti-Pattern 警告5种错误）；场景级存储粒度（store-chapter 自动分场景）

### 5. 一致性审查
- **覆盖度**：✅ 核心功能（最强维度）
- **实现方式**：
  - continuity_checker.py 连续性检查（角色状态矛盾/位置矛盾/能力矛盾）
  - `check-ooc` OOC检测（关键词+语义近似）
  - `check-continuity` 自动从 DB 读取章节内容（不需手动传）
  - `audit` 质量审计（quality_auditor.py）
  - fact_engine.py 事实管理——三级重要性：permanent（永不过期）/ arc-scoped（弧内有效）/ chapter-scoped（仅本章）
  - `detect-fact-changes` 组合操作：脚本提取 + Agent 语义分析 → 识别新事实/更新事实/冲突事实
- **独特亮点**：事实三级重要性——直接决定上下文加载策略（permanent=始终加载，chapter-scoped=仅前3章）；冲突事实自动标注；审查脚本是确定性的（零 LLM 成本）——可作为第一道过滤网

### 6. 文风控制
- **覆盖度**：✅ 核心功能
- **实现方式**：style_learner.py 风格分析和学习；统计指纹（句长/TTR/高频模式）存入 style_profile.json；`analyze-style` / `compare-style` 风格对比；for-creation 输出自动附加 constraints；creation_guide.md + agent_roles.md 提供8种角色模板
- **独特亮点**：统计指纹是量化风格指标——句长/TTR/高频模式，可数学对比（非主观"感觉风格变了"）；风格对比功能可检测章节间文风漂移

### 7. 平台适配
- **覆盖度**：❌ 不涉及
- **实现方式**：无特定平台适配
- **独特亮点**：无

### 8. 协作与迭代
- **覆盖度**：✅ 核心功能（最强维度）
- **实现方式**：
  - 73条命令统一入口 command_executor.py（参数名自动映射）
  - 修订工作流：analyze-revision→revise→clear-chapter→re-store→re-extract→re-detect
  - engagement_tracker.py 读者追读力追踪——4指标评分（engagement/hook_strength/tension_level/pace_type）→`reader_pull = 0.4*engagement + 0.35*hook + 0.25*tension`
  - hook_tracker.py 伏笔追踪——plant→hint→partial-resolve→resolve 状态机，支持 strength(0-1) 和 urgency 衰减
  - 6级摘要层级：book→phase→arc→volume→chapter→scene
  - memory_engine.py 记忆引擎：FTS5全文搜索+ONNX语义搜索（768维向量）
  - 快照系统支持回滚
- **独特亮点**：73条命令是最大规模的命令体系；6级摘要是最细粒度的上下文管理；engagement 系统量化读者体验（`reader_pull`公式）；快照系统支持安全回滚；修订工作流的 analyze-revision 防止级联错误

---

## 特殊分析（onkos 专属）

### 工作流触发机制
- **3条强制规则（NON-NEGOTIABLE）**：
  1. 所有小说请求必须使用此 skill——LLM 本质上无法维护跨章节一致性
  2. 必须完成完整流水线——部分使用导致孤儿数据
  3. 必须用 command_executor.py 调用所有脚本
- **Pre-flight Check**：每次写作前验证3条件——for-creation 已执行/上下文可见/严格按上下文创作
- **反模式警告**：5种常见错误——仅调用 for-creation 跳过后处理/挑选上下文忽略约束/不调用 for-creation 直接写/忽略返回上下文用自己记忆写/修订不先 analyze-revision

### 状态管理方式
- **SQLite 统一存储**（novel_memory.db）：知识图谱 + hooks + arcs + 场景 + facts + embeddings
- **Markdown 真相文件**：人类可读 + Git 可追踪
- **快照系统**：每章边界创建完整状态快照
- **事实三级重要性**：permanent → arc_scoped → chapter_scoped（决定上下文加载优先级）

### 与其他 skills 的集成接口
- command_executor.py 统一入口——外部工具可程序化调用
- JSON 格式的事实/伏笔/状态可被外部程序读取
- ONNX 768维语义搜索可被其他工具用于上下文检索
- 实体提取结果（含置信度）可被 Planner/Writer 使用

---

## 总结
- **核心优势（Top 5）**：
  1. 唯一拥有完整本地 NLP 引擎——jieba+ONNX+SQLite FTS5（零外部 API 依赖）
  2. 73条命令覆盖小说创作全生命周期
  3. 6级摘要层级——最细粒度上下文管理
  4. 强制工作流+Pre-flight Check——质量保障机制最严格
  5. 确定性审查脚本——OOC/连续性/事实冲突检测零 LLM 成本
- **主要局限**：
  1. 学习曲线最陡（73条命令+3条强制规则+5种反模式）
  2. 依赖 Python 环境配置（jieba+onnxruntime）
  3. ONNX 模型需额外下载（~98MB）
  4. 无平台适配和章节正文生成能力（依赖 LLM 的 Agent 写作部分）
- **最佳适用场景**：长篇小说基础设施层（记忆/事实/伏笔/审查）；需要确定性一致性检查；作为其他 skills 的共享数据后端
- **在双终端工作流中的建议定位**：**底层基础设施（贯穿所有阶段）**——Memory Manager + Foreshadowing Tracker + Continuity Checker + Engagement Tracker 的数据层
