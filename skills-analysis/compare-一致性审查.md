# 一致性审查 — 跨 Skills/项目比对报告

## 覆盖度矩阵

| 分析对象 | 类型 | 覆盖度 | 实现方式 | 亮点 |
|----------|------|--------|---------|------|
| fiction-crafter | skill | ✅ | 9维完整审查（含穿帮检测4类/套路重复相似度/伏笔管理/角色成长追踪）；2种模式（快速3维/完整9维） | 审查维度最多（9维）；历史趋势追踪 |
| novelist | skill | ❌ | 伏笔追踪卡提供基础连续性保障 | — |
| novel-writer-cn | skill | ❌ | 无 | — |
| story-cog | skill | ❌ | 无 | — |
| story-writer | skill | ❌ | 无 | — |
| my-novel-writer | skill | ⚡ | 5类生成时约束（字数/伏笔/状态/战力/违禁词）；plot_tracker.py 检查未关闭伏笔 | 战斗结果逻辑约束（跨境需≥1项支撑） |
| openclaw-novel-write | skill | ✅ | `/novel track --check`（每章追踪验证）+ `/novel analyze`（每5章质量分析）；自检4项；失败阻断后续写作 | 审查失败硬门控——阻断后续写作 |
| tomato-novelist | skill | ⚡ | 连贯性检查 + 质量自查（>60分）+ 字数脚本检查 | 质量自查有量化分数 |
| onkos | skill | ✅ | continuity_checker.py + check-ooc + check-continuity + audit + fact_engine 三级重要性 + detect-fact-changes | 确定性脚本审查（零LLM成本）；冲突事实自动标注 |
| inkos | 项目 | ✅ | Auditor 37维审计 + Reviser 修订 + Polisher 润色（三者分离）；LOCAL/STRUCTURAL 路由；备忘偏离分析；Hook-debt 升级规则 | 审/改/润分离是工程验证的最佳实践 |

## 共同模式

1. **审查与创作分离是趋势**：fiction-crafter（独立审查步骤）、openclaw-novel-write（独立 analyze 命令）、onkos（独立 audit 命令）、inkos（独立 Auditor Agent）都走向审创分离
2. **穿帮检测是基本要求**：覆盖角色/地点/时间线/能力四个维度
3. **伏笔管理是共识**：从简单的"埋设→回收"到复杂的生命周期模型
4. **字数检查是硬性指标**：my-novel-writer、tomato-novelist、openclaw-novel-write 都有字数验证

## 差异化分析

| 特色做法 | 采用者 | 优劣分析 |
|---------|--------|---------|
| 9维审查体系 | fiction-crafter | ✅ 覆盖最全 ❌ 纯LLM执行，成本高 |
| 确定性脚本审查 | onkos | ✅ 零LLM成本+快速 ❌ 仅覆盖可脚本化维度 |
| 审/改/润三阶段分离 | inkos | ✅ 职责清晰 ❌ 编排复杂 |
| LOCAL/STRUCTURAL 路由 | inkos | ✅ 小修不引发大bug ❌ 需要准确的问题分类 |
| 审查失败硬门控 | openclaw-novel-write | ✅ 质量保障 ❌ 可能阻塞流水线 |
| 备忘偏离分析 | inkos | ✅ 防止实际产出偏离ChapterMemo ❌ 依赖完整Memo |
| 事实三级重要性 | onkos | ✅ 精确管理事实生命周期 ❌ 分类需要人工判断 |

## onkos/inkos 工作流视角

- **onkos**：13个可脚本化审查维度（词汇疲劳/违禁词/对话标签/句首重复等）是零成本的第一道过滤网。fact_engine 的三级重要性决定了"什么事实需要被检查"
- **inkos**：40维三层审计架构（13💻脚本+8🔀混合+19🤖LLM）是市面上最系统化的审查方案。审/改/润三阶段分离是最重要的结构创新——"自己写的自己查不出问题"的原则被彻底执行

## 最佳实践推荐

- **首选方案**：**inkos 审/改/润三阶段分离架构** + **onkos 确定性脚本审查**（第一道过滤网）+ **fiction-crafter 9维审查维度参考**（补充中文网文特有维度）
- **推荐理由**：inkos 的架构设计最合理（审改润分离），onkos 的脚本层最实用（零成本第一道过滤），fiction-crafter 的9维最全面（中文网文特有维度如爽点结构完整性）
- **可组合方案**：Layer 1: onkos 脚本审查（13维，零成本）→ Layer 2: 混合审查（脚本预检+LLM确认）→ Layer 3: LLM 全维审查（含中文特有维度）→ 问题路由（LOCAL→修补 / STRUCTURAL→重写）→ 润色

## 空白地带

1. **无跨章因果链自动验证**：没有 skill 能自动检测"第5章的事件X是否必然导致第10章的结果Y"
2. **无读者视角一致性模拟**：没有 skill 能模拟"第10章的新读者"看到的世界观是否与第1章一致
3. **无时间流逝一致性检查**：自动检测"从第3章到第8章经过了多长时间，角色年龄/季节是否正确"
4. **无跨书质量基准对比**：无法将一个项目的审查数据与同类型项目的基准对比
