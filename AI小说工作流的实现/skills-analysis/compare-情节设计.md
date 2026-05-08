# 情节设计 — 跨 Skills/项目比对报告

## 覆盖度矩阵

| 分析对象 | 类型 | 覆盖度 | 实现方式 | 亮点 |
|----------|------|--------|---------|------|
| fiction-crafter | skill | ✅ | 全局大纲→卷级章节规划（树状分解）；爽点节拍器（3/5/8-12/15-20章节奏） | 卷级章节规划"防止剧情写偏"；情绪曲线标注 |
| novelist | skill | ✅ | 双结构模型（爽文：目标-障碍-代价-反转 / 传统：起承转合）；爽点节拍器（3章小高潮/10章大反转）；卡文急救 | 双模型适配不同类型；卡文急救机制 |
| novel-writer-cn | skill | ✅ | 三幕式（铺垫/对抗/解决）+ 4版本结局 | "一切尽失"低谷点唯一明确标注 |
| story-cog | skill | ⚡ | 大纲生成+情节漏洞修复；支持 agent team 模式处理复杂叙事 | 情节漏洞修复对话式交互 |
| story-writer | skill | ⚡ | 三幕式情节大纲 | — |
| my-novel-writer | skill | ⚡ | `--add-outline`/`--update-outline` 大纲管理；plot_tracker.py 伏笔追踪 | 大纲支持动态调整 |
| openclaw-novel-write | skill | ✅ | creative-plan + timeline + tasks + plot-tracker.json | 时间线独立文件，写作前强制对照 |
| tomato-novelist | skill | ✅ | 7种核心冲突类型；情绪过山车循环；每3章"压-小扬-压-爆" | 情绪标签→算法推荐映射 |
| onkos | skill | ✅ | create-phase(100-300章)+create-arc-am(30-60章) 双层结构；arc_manager 进度；plot_brancher 支线 | Phase→Arc 双层是唯一的结构化粒度 |
| inkos | 项目 | ✅ | Planner→ChapterMemo 7段 YAML；三问测试；Held-Back 段（扣留信息） | ChapterMemo 是最结构化的章节指令；Held-Back 是唯一"标明不写什么" |

## 共同模式

1. **大纲驱动创作**：所有 ✅ 级 skills 都先规划大纲再写作
2. **章节级分解**：fiction-crafter（卷→章任务）、onkos（Phase→Arc→Scene）、inkos（ChapterMemo）都做逐章分解
3. **节奏控制是核心关切**：fiction-crafter（章数间隔公式）、novelist（节拍器）、tomato-novelist（情绪过山车）都有明确的节奏规则
4. **冲突设计被强调**：novelist（核心矛盾三问）、novel-writer-cn（冲突升级线）、tomato-novelist（7种冲突类型）

## 差异化分析

| 特色做法 | 采用者 | 优劣分析 |
|---------|--------|---------|
| 树状分解（卷→阶段→子阶段→情节单元→章） | fiction-crafter | ✅ 最细粒度 ❌ 人工维护成本高 |
| 双结构模型（爽文vs传统） | novelist | ✅ 灵活适配 ❌ 分类可能过度简化 |
| 多版本结局 | novel-writer-cn | ✅ 探索可能性 ❌ 仅框架无执行 |
| ChapterMemo 7段YAML | inkos | ✅ 最结构化 ❌ 生成成本高（每章需LLM调用） |
| 情绪标签驱动 | tomato-novelist | ✅ 直接对接平台算法 ❌ 仅番茄平台 |
| Phase→Arc 双层叙事 | onkos | ✅ 最佳粒度控制 ❌ 概念门槛高 |
| 情节漏洞修复对话 | story-cog | ✅ 互动式 ❌ 依赖远程API |
| 三问测试 | inkos | ✅ 确保每章有存在价值 ❌ 每章都答可能机械 |

## onkos/inkos 工作流视角

- **onkos**：Phase→Arc 双层结构 + arc_manager 自动推断进度 + plot_brancher 支线管理——提供最完整的叙事结构管理
- **inkos**：ChapterMemo 7段是情节设计的最结构化输出——Planner 输出不是"大纲"而是"写作指令"。Held-Back 段特别有价值——明确标注"本章绝对不写的内容"，防止 Writer 越界

## 最佳实践推荐

- **首选方案**：**inkos ChapterMemo**（7段结构化章节指令，含Held-Back和三问测试）+ **onkos**（Phase→Arc 结构管理 + 进度追踪）+ **fiction-crafter**（卷级章节规划模板）
- **推荐理由**：ChapterMemo 是市面上最精确的章节级写作指令，onkos 提供最完整的结构管理基础设施，fiction-crafter 的卷级规划是中文网文验证过的实践
- **可组合方案**：onkos（创建Phase→Arc结构）→ inkos-style Planner（为每章生成ChapterMemo）→ Writer（严格按Memo写作）

## 空白地带

1. **无因果链自动验证**：没有 skill 能自动检测"事件A是否必然导致事件B"的因果合理性
2. **无情节复杂度评分**：没有 skill 能量化"支线交织密度""反转频率"等情节复杂度指标
3. **无读者预期管理工具**：没有 skill 能建模"当前读者最期待的3件事"并追踪兑现率
4. **无跨卷情节线平衡**：多条故事线（实力线/身份线/感情线）的进展速度无法自动平衡
