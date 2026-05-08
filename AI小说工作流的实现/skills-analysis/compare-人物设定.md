# 人物设定 — 跨 Skills/项目比对报告

## 覆盖度矩阵

| 分析对象 | 类型 | 覆盖度 | 实现方式 | 亮点 |
|----------|------|--------|---------|------|
| fiction-crafter | skill | ⚡ | 提示词定义+CHARACTERS.md 状态追踪+配角消失预警(>15章) | 角色成长曲线追踪（连续5章无成长=预警） |
| novelist | skill | ✅ | 6要素角色卡（姓名/身份/执念/缺陷/口头禅/关系）；强调底层执念+性格缺陷 | 底层执念是驱动角色行动的核心欲望 |
| novel-writer-cn | skill | ✅ | 三层角色体系（主角/配角/反派）+ 关系矩阵 | 每个配角有"独特功能"防工具人化 |
| story-cog | skill | ⚡ | 角色圣经（背景/心理/关系/语言/行为/自我欺骗/改变点） | 角色心理学深度（恐惧/欲望/防御机制） |
| story-writer | skill | ⚡ | 对话式引导 | 双语支持 |
| my-novel-writer | skill | ✅ | `--set-character` + character_card 7段模板 + JSON 状态追踪 | 模板最结构化（7段） |
| openclaw-novel-write | skill | ✅ | character-state.json + relationships.json + clarify-answers | JSON 结构化状态可追踪可回滚 |
| tomato-novelist | skill | ✅ | 6种反差点模板 + 人物档案 | 反差点设计直接对应算法推荐 |
| onkos | skill | ✅ | create-char(5种类型) + character_simulator OOC检测 + entity_extractor | OOC检测确定性脚本零LLM成本 |
| inkos | 项目 | ⚡ | MemoryDB 存储 + 大五人格OOC + 事实时间有效性 | valid_from/until 精确事实生命周期 |

## 共同模式

1. **角色卡是标配**：几乎所有 skills 都有角色信息存储（文件/JSON/DB）
2. **关系管理是共识**：novel-writer-cn（关系矩阵）、openclaw（relationships.json）、onkos（add-edge）都在独立管理角色关系
3. **状态追踪是趋势**：fiction-crafter（CHARACTERS.md更新）、my-novel-writer（novel_context.json）、openclaw（character-state.json）都追踪角色状态变化
4. **配角问题被广泛关注**：fiction-crafter（>15章未出现预警）、novel-writer-cn（配角独特功能）、novelist（性格缺陷让角色真实）

## 差异化分析

| 特色做法 | 采用者 | 优劣分析 |
|---------|--------|---------|
| 底层执念+性格缺陷 | novelist | ✅ 角色深度 ✅ 防纸片人 ❌ 需人类判断执念合理性 |
| 反差点模板 | tomato-novelist | ✅ 快速生成爆款人设 ❌ 模板化可能千篇一律 |
| 心理学深度 | story-cog | ✅ 恐惧/欲望/防御机制三维 ❌ 仅适合严肃文学 |
| OOC确定性检测 | onkos | ✅ 零LLM成本+快速 ❌ 仅关键词+语义近似，非深度学习 |
| 大五人格OOC | inkos | ✅ 科学人格模型 ❌ 需要人格评分数据 |
| 事实时间有效性 | inkos | ✅ 精确管理"第X-Y章有效的状态" ❌ 实现复杂 |

## onkos/inkos 工作流视角

- **onkos**：character_simulator.py 的 OOC 检测是唯一可独立运行的自动角色一致性检查。entity_extractor.py 可自动从正文提取角色名，减少人工录入
- **inkos**：大五人格模型提供更科学的 OOC 判断维度。事实时间有效性（valid_from/until）确保"第5章受伤→第10章恢复"这个时间窗口内的状态是正确的

## 最佳实践推荐

- **首选方案**：**novelist**（底层执念+性格缺陷的设计深度）+ **onkos**（OOC自动检测+entity_extractor自动提取）+ **openclaw-novel-write**（JSON结构化状态追踪）
- **推荐理由**：novelist 提供最深的角色设计哲学，onkos 提供最可靠的自动一致性保障，openclaw 提供最整洁的状态数据格式
- **可组合方案**：my-novel-writer（character_card 模板初始化角色）→ novelist（补充底层执念和性格缺陷）→ onkos（OOC检测+实体提取+追踪）→ openclaw（JSON状态文件供其他工具读取）

## 空白地带

1. **无角色弧光自动检查**：没有 skill 自动检测"角色的成长弧线是否完整"（仅 fiction-crafter 有手动追踪）
2. **无角色互动频率分析**：没有 skill 统计"各角色出场频率和互动密度"
3. **无角色声音（voice）区分检测**：没有 skill 自动检测"不同角色的对话是否有足够的语言风格差异"
4. **无群像平衡检查**：多主角/群像场景下，各自的戏份和弧线进度无法自动平衡
