# inkos 深度拆解报告（基于源码学习）

## 基本信息
- **类型**：外部工作流项目（npm CLI + TypeScript 全栈）
- **版本**：1.3.7
- **仓库**：github.com/Narcooo/inkos
- **包结构**：`@actalk/inkos`（CLI入口）+ `@actalk/inkos-core`（核心引擎）+ `@actalk/inkos-studio`（Studio UI）
- **技术栈**：TypeScript + React（Ink 终端UI）+ Commander CLI + epub-gen-memory
- **许可证**：AGPL-3.0-only
- **核心机制**：10-Agent 自主小说写作 CLI 流水线——写、审计、修订，带连续性追踪

---

## 一、总体架构

```
@actalk/inkos (CLI 入口层)
  ├── dist/index.js                  # CLI 入口
  ├── dist/program.js                # Commander 程序注册
  ├── dist/commands/                 # 28 个命令
  │   ├── init.js/book.js           # 项目管理
  │   ├── plan.js/write.js          # 核心创作流水线
  │   ├── audit.js/review.js/revise.js  # 质量保障
  │   ├── compose.js                # 上下文组装
  │   ├── consolidate.js            # 卷级压缩
  │   ├── detect.js                 # 问题检测
  │   ├── genre.js/style.js         # 类型/风格管理
  │   ├── agent.js                  # Agent 管理
  │   ├── eval.js/radar.js          # 评估/雷达
  │   ├── daemon.js                 # 守护进程
  │   ├── export.js                 # epub 导出
  │   ├── fanfic.js                 # 同人创作
  │   ├── import.js                 # 导入已有作品
  │   └── ...
  ├── dist/tui/                      # 终端 UI（Ink React）
  └── dist/interaction/             # 工具交互

@actalk/inkos-core (核心引擎层)
  ├── dist/agent/                    # Agent 会话管理
  │   ├── agent-session.js          # 会话生命周期
  │   ├── agent-system-prompt.js    # 系统提示词
  │   ├── agent-tools.js            # 工具定义
  │   └── context-transform.js      # 上下文转换
  ├── dist/agents/                   # 10 个 Agent 实现
  │   ├── base.js                   # BaseAgent（LLM调用+Web搜索）
  │   ├── architect.js              # 总架构师
  │   ├── planner.js + planner-prompts.js + planner-context.js
  │   ├── composer.js               # 上下文组装
  │   ├── continuity.js             # 连续性审计
  │   ├── consolidator.js           # 卷级压缩
  │   ├── detector.js               # 问题检测
  │   ├── chapter-analyzer.js       # 章节分析
  │   ├── foundation-reviewer.js    # 基础设定审核
  │   ├── length-normalizer.js      # 字数规范化
  │   ├── fanfic-*.js               # 同人相关
  │   └── ...
  ├── dist/genres/                   # 15 个 Genre Profile（Markdown）
  ├── dist/models/                   # Zod Schema 定义
  └── dist/utils/                    # 工具函数（记忆检索/上下文组装/钩子升级等）
```

---

## 二、10 个 Agent 逐一拆解

### Agent 1：Architect（总架构师）— `architect.js`

**触发时机**：建书初始化 / 导入已有作品 / 架构修订

**输入**：
- 书籍元信息（标题/平台/题材/目标章数/每章字数）
- Genre Profile（15种之一，含题材底色/数值系统/战力体系配置）
- 可选：外部指令/审核反馈/既有架构稿（修订模式）

**核心 Prompt 设计**（`buildChineseFoundationPrompt`）：

**输出结构 — 5 SECTION 强制契约**：

```
=== SECTION: story_frame ===    （散文骨架，≤3000字）
  段1：主题与基调
    - 具体的命题（不是"从弱到强"的空话）
    - 基调（温情/冷冽/悲壮/肃杀）及理由
    - 结尾指向主角 roles 文件
  
  段2：核心冲突 + 前台/后台双层故事
    - 主要矛盾（因为A相信X、B相信Y，所以必然在对撞）
    - 至少2个对手：1显性 + 1结构性/体制
    - 前台故事：读者每章看到的表层冲突
    - 后台故事：贯穿全书的暗线机器（幕后黑手/阴谋/身世）
    - 两层因果关联：每段前台冲突都能追溯到后台齿轮
  
  段3：世界观底色
    - 3-5条不可违反的铁律（prose，不bullet）
    - 质感锚点（湿/干/快/慢/噪/静）
    - 合并了原 book_rules 的散文部分
  
  段4：终局方向 + 全书 Objective
    - 最后一个镜头长什么样
    - 一句可验证的 Book Objective（例："从杂役成为宗门长老并公开父辈冤案"）

=== SECTION: volume_map ===    （分卷散文地图，≤5000字）
  段1：各卷主题与情绪曲线
  段2：卷间钩子与回收承诺（前台+后台双层覆盖）
  段3：各卷 OKR（Objective + 3 Key Results）
    - 每卷 O：本卷结束时主角必须达成的可验证状态
    - 每卷 3 KR：可量化/可观察的关键子成果
    - KR 是 Planner 分解章节任务的直接依据
  段4：卷尾必须发生的改变（不可逆事件）
  段5：节奏原则（6条，至少3条具体化到本书）
    - 高潮间距/喘息频率/钩子密度/信息释放节奏/爽点节奏/情感节点递进

=== SECTION: roles ===         （一人一卡 prose，≤8000字总）
  主要角色（≥3个：主角+主要对手+主要协作者）：
    ---ROLE---
    tier: major
    name: <角色名>
    ---CONTENT---
    ## 核心标签（3-5个关键词）
    ## 反差细节（1-2个与标签反差的具体细节——"冷酷杀手但给流浪猫留鱼骨"）
    ## 人物小传（关键过往）
    ## 主角弧线（起点→终点→代价）【主角必须，其他可选】
    ## 当前现状（第0章初始状态）
    ## 关系网络
    ## 内在驱动（想要什么/为什么/愿付什么代价）
    ## 成长弧光
  
  次要角色（3-5个，简化版：核心标签/反差细节/当前现状/与主角关系）

=== SECTION: book_rules ===    （仅 YAML，≤500字，零散文）
  protagonist: { name, personalityLock, behavioralConstraints }
  genreLock: { primary, forbidden }
  numericalSystemOverrides: { hardCap, resourceTypes }
  prohibitions: [3-5条]
  chapterTypesOverride / fatigueWordsOverride / additionalAuditDimensions

=== SECTION: pending_hooks === （初始伏笔池，≤2000字）
  Markdown 表格，Phase 7 扩展12列：
  hook_id | start_chapter | type | status | last_advanced_chapter
  | expected_payoff | payoff_timing | depends_on | pays_off_in_arc
  | core_hook | half_life | notes
```

**关键设计约束**：
1. **去重铁律**：同一事实禁止在多段重复。主角弧线只写在 roles，世界铁律只写在 story_frame，节奏原则只写在 volume_map 尾段
2. **预算超限必删**：每段有严格字数上限
3. **散文密度 > bullet**：story_frame/volume_map/roles 必须是可读的段落散文，禁止退化为条目表格
4. **5段完整性检查**：必须输出全部5个 SECTION，不允许因为前段写长就跳过后段
5. **角色反差细节公式**："核心标签 + 反差细节 = 立体人物"——这是 inkos 的固定公式

---

### Agent 2：Planner（大纲规划师）— `planner.js` + `planner-prompts.js`

**触发时机**：每章开始前的规划阶段

**输入流程**（`planChapter`）：
1. 加载种子材料（seedMaterials）：当前状态/故事圣经/卷纲/摘要/前章结尾
2. 从 volume_map 找到本章在大纲树中的节点（`findOutlineNode`——支持精确章号匹配和范围匹配）
3. 推导目标（`deriveGoal`——优先级：外部指令 > 局部覆盖 > 大纲节点 > 当前焦点 > 作者意图）
4. 收集约束（mustKeep/mustAvoid/styleEmphasis）
5. 组装规划材料（`gatherPlanningMaterials`——含记忆检索/活跃伏笔/上下文）
6. 生成 ChapterIntent（确定性，非LLM）
7. 调用 LLM 生成 ChapterMemo（YAML frontmatter + 7-section body）

**ChapterMemo 结构**（来自 `PLANNER_MEMO_SYSTEM_PROMPT`）：

```yaml
---
chapter: 12
goal: 把七号门被动过手脚从猜测钉成现场实证  # ≤50字
isGoldenOpening: false
threadRefs: [H03, S004]
---

## 当前任务
<一句话：主角要完成的具体动作>

## 读者此刻在等什么
1) 读者现在期待什么
2) 本章对这个期待做什么——制造缺口/部分兑现/完全兑现/暗示

## 该兑现的 / 暂不掀的
- 该兑现：X → 兑现程度
- 暂不掀：Y → 压到第N章

## 日常/过渡承担什么任务
<非高压章：每段非冲突段落的功能说明。高压章：写"不适用">

## 关键抉择过三连问
- 主角本章最关键的选择：为什么/符合利益吗/符合人设吗
- 对手/配角本章最关键的选择：为什么/符合利益吗/符合人设吗

## 章尾必须发生的改变
<1-3条，维度：信息改变/关系改变/物理改变/权力改变>

## 本章 hook 账
open:       [new] 新钩子描述 || 理由（上限≤2，推荐 resolve N→open 2N）
advance:    H007 "胖虎借条" → 林秋第一次想撕（planted→pressured）
resolve:    H003 "杂役腰牌" → 林秋主动摘下（clear）
defer:      H009 "守拙诀来历" → 时机不到，等到第N章

## 不要做
<2-4条硬约束>
```

**14 条工作原则**（内化到系统提示词，不在 memo 中引用条目号）：
1. 3-5章一个小目标周期
2. 主动塑造读者期待（兑现必须超过预期70%）
3. 万物皆饵（日常/过渡每笔都是未来伏笔）
4. 人设防崩（行为=过往经历+当前利益+性格底色）
5. 1主线+1支线（不同时推3条以上支线）
6. 爽点密集化（3-5章一小爽点）
7. 高潮前3-5章埋伏笔
8. 高潮后1-2章写改变
9. 人物立体化（核心标签+反差细节）
10. 五感具体化
11. 钩子承接（每章章尾留钩）
12. 钩子账本必须结账（每章对活跃hook做明确动作）
13. 圆心法同场多视角（核心事件聚拢多角色时，每人独立内心反应）
14. 揭1埋2推荐（resolve 1个hook → 尽量埋2个新hook，硬底线是 resolve N → open ≥ N）

**重试策略**：解析失败最多3次重试，每次将错误注入用户提示词让 LLM 自我修正。3次失败后抛出 `PlannerParseError`

---

### Agent 3：Composer（上下文组装师）— `composer.js`

**职责**：为 Writer 组装受控上下文切片（Governed Context 的实现）

**上下文来源**（`collectSelectedContext`）：
1. **chapter_memo**：Planner 产出的完整 ChapterMemo
2. **current_focus.md**：当前任务焦点
3. **audit_drift.md**：上章审计漂移指导
4. **current_state.md**：硬状态事实（含检索提示过滤）
5. **outline/story_frame.md**：正典约束（含检索提示过滤）
6. **outline/volume_map.md**：当前大纲节点锚定
7. **parent_canon.md / fanfic_canon.md**：同人/续写正典约束
8. **近期章节轨迹**（3项）：
   - 最近章节标题序列（防标题重复）
   - 最近章节情绪/类型序列
   - 最近3章结尾句（防结尾结构重复）
9. **Hook 债务简报**（`buildHookDebtEntries`）：
   - 每个 memo-referenced hook 的原始种子文本 + 最新推进文本
   - 读者承诺 + 已开章数
10. **记忆检索结果**（`retrieveMemorySelection`）：
    - 相关摘要（episodic memory）
    - 相关事实（current-state facts）
    - 活跃伏笔
    - 卷级摘要（长程弧线记忆）

**输出格式**：`ContextPackage`（Zod Schema 验证）——包含 `chapter` + `selectedContext[]`

---

### Agent 4：Writer（章节生成器）

Writer 在 inkos 中不是独立 Agent 文件——它通过 `write.js` 命令调用，基于 Composer 的 ContextPackage + Planner 的 ChapterMemo 进行生成。核心约束：
- 只能看到 Composer 预选的上下文切片（不能直接读真相文件）
- 产出正文 + RuntimeStateDelta（结构化状态变更）
- 严格遵守 ChapterMemo 的 Don'ts 和 Held-Back

---

### Agent 5：Continuity Auditor（连续性审计官）— `continuity.js`

**37 维审计体系**（`DIMENSION_LABELS`）：

| ID | 维度 | ID | 维度 | ID | 维度 |
|----|------|----|------|----|------|
| 1 | OOC检查 | 14 | 配角工具人化 | 27 | 敏感词检查 |
| 2 | 时间线检查 | 15 | 爽点虚化 | 28 | 正传事件冲突 |
| 3 | 设定冲突 | 16 | 台词失真 | 29 | 未来信息泄露 |
| 4 | 战力崩坏 | 17 | 流水账 | 30 | 跨书世界规则 |
| 5 | 数值检查 | 18 | 知识库污染 | 31 | 番外伏笔隔离 |
| 6 | 伏笔检查(Hook-debt) | 19 | 视角一致性 | 32 | 读者期待管理 |
| 7 | 节奏检查(波形) | 20 | 段落等长 | 33 | 章节备忘偏离 |
| 8 | 文风检查 | 21 | 套话密度 | 34 | 角色还原度(同人) |
| 9 | 信息越界 | 22 | 公式化转折 | 35 | 世界规则遵守(同人) |
| 10 | 词汇疲劳 | 23 | 列表式结构 | 36 | 关系动态(同人) |
| 11 | 利益链断裂 | 24 | 支线停滞 | 37 | 正典事件一致性 |
| 12 | 年代考据 | 25 | 弧线平坦 | | |
| 13 | 配角降智 | 26 | 节奏单调 | | |

**Genre Profile 感知**：
- 疲劳词表来自 Genre Profile（可被 book_rules.fatigueWordsOverride 覆盖）
- 爽点类型来自 Genre Profile（`satisfactionTypes`）
- 年代约束来自 book_rules.eraConstraints

**v10 增强维度**（包含写作方法论意识）：
- **维度7（节奏波形）**：检查"蓄压→升级→爆发→后效"完整周期；连续5章无爆发→节奏停滞；高潮后跳转新蓄压而无后效→"高潮后影响缺失"
- **维度15（爽点虚化）**：检查欲望驱动——制造了情绪缺口还是完成≥70%期待的兑现；后效阶段需展示具体改变（地位/关系/资源）
- **维度6（伏笔检查 Phase 7）**：Hook-debt 升级规则——critical 仅适用于 promoted=true 的伏笔；promoted+core_hook+stale>10章→CRITICAL；promoted+blocked≥6章→WARNING

**Fanfic 专属维度**（28-37）：正传事件冲突/未来信息泄露/跨书世界规则/番外伏笔隔离/角色还原度/世界规则遵守/关系动态/正典事件一致性

---

### Agent 6：Reviser（修订官）— `revise.js`

基于 AuditReport 的问题分类进行修订：
- **LOCAL 问题**：原地修补（措辞/疲劳词/违禁词替换）
- **STRUCTURAL 问题**：重写（OOC/主线偏离/伏笔遗漏/信息越界/战力崩坏/备忘偏离）
- 迭代控制：最多3轮，每轮 temperature+0.1，取最高分版本

---

### Agent 7：Polisher（润色官）

审计通过后的文笔润色：
- ✅ 可做：句子节奏优化/对话自然度/AI腔移除/五感强化/标点统一
- ❌ 禁止：改动情节/改动台词含义/新增或删除人物事件设定/字数变化超±30字

---

### Agent 8：Consolidator（卷级压缩官）— `consolidator.js`

**触发时机**：每写完一卷（volume_map 中该卷所有章节完成）

**流程**：
1. 从 volume_map 解析卷边界（`parseVolumeBoundaries`）
2. 判断哪些卷已完成（`vol.endCh <= maxChapter`）
3. 对每个已完成卷：LLM 将该卷所有章节摘要压缩为一段叙事段落（max 500 words）
4. 写入 volume_summaries.md（追加该卷段落）
5. 归档详细摘要到 summaries_archive/
6. 重写 chapter_summaries.md（仅保留当前卷的行）
7. Phase 7 hotfix：重新运行伏笔升级判定（`rerunAdvancedCountPromotion`）

**效果**：写第241章时，前240章的上下文从 ~48000字 压缩到 ~2000字 + 当前卷详细摘要

---

### Agent 9：Detector（问题检测器）— `detector.js`

周期性扫描已有章节，检测：AI痕迹/疲劳词/桥段重复/节奏问题/伏笔逾期/风格漂移

### Agent 10：Observer（事实提取器）— `observer-prompts.js`

从 Writer 产出的正文中提取结构化事实（subject/predicate/object + temporal validity），供 MemoryDB 存储

---

## 三、核心设计模式

### 1. OKR 递归大纲法
```
Book Objective（全书根 O）
  └─ Volume 1 Objective → 3 KR
      └─ Chapter 1-5: KR1 推进
      └─ Chapter 6-10: KR2 推进
      └─ ...
  └─ Volume 2 Objective → 3 KR
  ...
```
每卷 3 个 KR 是 Planner 分解章节任务的直接依据（每3-5章推进一个 KR）

### 2. 前台/后台双层故事
- **前台**：读者每章看到的表层冲突（查案/打怪/升级/恋爱）
- **后台**：贯穿全书的暗线机器（幕后黑手/阴谋/身世/体制）
- 两层因果关联——前台冲突追溯到后台齿轮

### 3. ChapterMemo 的"稀疏 Memo 合法"原则
喘息章/后效章/过渡章的 Memo 可以只有 goal + 骨架 body，不因 Memo 稀疏而判 incomplete——只对照 Memo 实际写出的内容

### 4. Hook-debt 升级门控
- `promoted` 是 critical 的门控开关——非升级伏笔永远不触发 critical
- 升级条件：advancedCount ≥ 2（由 Consolidator 和 Architect 的自动判定）

### 5. 角色反差细节公式
"核心标签 + 反差细节 = 立体人物"——固定公式，每个主要角色强制包含。例："冷酷杀手但给流浪猫留鱼骨"

---

## 四、与当前 AI 小说工作流的关系

| inkos 设计模式 | 我们的采纳状态 | 备注 |
|---------------|-------------|------|
| 5 SECTION 架构输出 | ✅ 已纳入全流程文档 | story_frame/volume_map/roles 三段式已融入阶段一+二 |
| ChapterMemo 7段 | ✅ 已纳入全流程文档 | 调整为中文网文习惯（去方法论术语） |
| OKR 递归大纲 | ⚡ 部分采纳 | Book Objective + Volume OKR 概念已融入 |
| 前台/后台双层 | ⚡ 待显式化 | 当前流程中隐含但未显式标注 |
| 审/改/润分离 | ✅ 已采纳 | 阶段四的三层审计 + Reviser + Polisher |
| Governed Context | ✅ 已纳入 | ContextPackage 5条硬规则 |
| Consolidator 卷压缩 | ✅ 已纳入 | 阶段五卷级压缩 |
| Hook 12列模型 | ✅ 已纳入 | dependsOn/coreHook/promoted/urgency公式 |
| 37维审计 | ⚡ 参考中 | 我们的40维三层审计借鉴了其分类和增强维度 |
| 角色反差细节公式 | ✅ 可纳入 | 简化为"核心标签+反差细节" |
| 稀疏 Memo 合法 | ✅ 已纳入 | 审计时不因过渡章任务少而扣分 |
| 15 Genre Profiles | ⚡ 需中文化 | 目前只有玄幻一个 Genre Profile |

---

## 五、总结

- **核心优势**：10-Agent 拆分是市面上最精细的小说工作流架构；ChapterMemo 7段 + Hook 账本是最结构化的章节级写作指令；前台/后台双层故事解决了"散成独立事件集"和"憋闷看不到爽感"的两难；OKR 递归大纲让每章都有明确的"为什么存在"；角色反差细节公式是人物立体化的可操作公式
- **主要局限**：英文网文为主（15 Genre Profiles 全是英文类型）；TypeScript/Node.js 生态——无法直接复用 Python 本地 NLP（jieba/ONNX）；10-Agent 编排仍需人类决策触发；AGPL-3.0 许可证
- **最佳适用场景**：架构设计的参考实现（取其设计模式，不直接运行）；ChapterMemo 格式和 Planner prompt 可直接翻译适配；Hook 12列模型和升级规则可直接采用；OKR 大纲法适用于任何长篇创作
- **在双终端工作流中的建议定位**：**架构参考**——ChapterMemo 格式 + Governed Context 协议 + 审/改/润分离 + Hook 模型 + OKR 大纲法是核心借鉴。具体执行由 onkos（数据层）+ my-novel-writer（生成引擎）+ novelist（文风控制）组合实现
