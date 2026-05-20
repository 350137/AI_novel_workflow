# 章节创作 — 跨 Skills/项目比对报告

## 覆盖度矩阵

| 分析对象 | 类型 | 覆盖度 | 实现方式 | 亮点 |
|----------|------|--------|---------|------|
| fiction-crafter | skill | ✅ | 固定模板（章名→概要→爽点→情绪曲线→正文→钩子）；2000-3000字；生成前读6个记忆文件；爽文节奏公式 | 生成前强制读取全部记忆防穿帮 |
| novelist | skill | ✅ | 场景渲染工作区：推镜法则（感官切入）→展示代替告知→单场景闭环1000-1500字→伏笔追踪卡→状态回写 | 推镜法则是最专业的场景写作指导 |
| novel-writer-cn | skill | ❌ | 仅输出框架，不生成正文 | — |
| story-cog | skill | ✅ | 全类型创作（闪小说/短篇/剧本/同人）；agent/agent team 双模式 | 唯一支持剧本格式 |
| story-writer | skill | ⚡ | 对话式生成+续写；也支持视频脚本 | 视频脚本是唯一的非纯文学格式 |
| my-novel-writer | skill | ✅ | `--generate <章> <字数>` CLI命令；每次只生成一章防上下文超限；自动摘要存JSON | 最完善的CLI生成命令；支持批量 |
| openclaw-novel-write | skill | ✅ | 6阶段写作流程（预写分析→初稿→自检→润色→修订→元数据输出）；前置8步强制检查 | 6阶段是最详细的单章流程 |
| tomato-novelist | skill | ✅ | 4步骤（分析→撰写→优化→收尾）；2200-2800字；10种钩子类型轮换；前50字强制抓人 | 字数脚本检查（非LLM估算） |
| onkos | skill | ✅ | 8步强制工作流（for-creation→写→store→extract→detect→record→update）；场景级DB存储 | 6步自动化脚本无法跳过 |
| inkos | 项目 | ✅ | Writer 基于 ChapterMemo+ContextPackage；Governed Context（5条硬规则）；RuntimeStateDelta 结构化输出 | 受控上下文防信息越界；StateDelta 可追溯 |

## 共同模式

1. **上下文加载是前提**：所有 skills 都在生成前加载已有记忆/大纲/人物状态
2. **字数控控制是标配**：2000-3000字是共识区间；my-novel-writer（2200-2500硬指标）、tomato-novelist（2200-2800脚本检查）
3. **章末钩子是必选项**：fiction-crafter、novelist、my-novel-writer、tomato-novelist、openclaw-novel-write 都强制要求章末钩子
4. **模板化生成**：大多数 skills 使用固定模板确保输出格式统一

## 差异化分析

| 特色做法 | 采用者 | 优劣分析 |
|---------|--------|---------|
| 推镜法则（感官→宏观） | novelist | ✅ 最佳场景开头方式 ❌ 非所有场景适用 |
| 展示代替告知 | novelist | ✅ 文学品质最高 ❌ 与爽文快节奏可能冲突 |
| 6阶段写作流程 | openclaw-novel-write | ✅ 最详细 ❌ 每章6阶段耗时长 |
| 单场景闭环 | novelist | ✅ 防上下文膨胀 ❌ 1000-1500字限制可能太紧 |
| Governed Context | inkos | ✅ 防信息越界+上下文膨胀 ❌ 需要Planner预先组装 |
| RuntimeStateDelta | inkos | ✅ 状态变更可追溯可回滚 ❌ 需要结构化解析 |
| 批量生成支持 | my-novel-writer | ✅ 效率高 ❌ 质量漂移风险 |
| 10种钩子轮换 | tomato-novelist | ✅ 防钩子公式化 ❌ 维护负担 |

## onkos/inkos 工作流视角

- **onkos**：8步工作流的第1步（for-creation）是最强的上下文保障——每次写作前强制获取结构化上下文。6步自动化确保数据不会丢失。但**onkos 本身不生成文字**——它依赖 Agent（Claude）的写作能力
- **inkos**：Governed Context 协议是 onkos for-creation 的"预选切片"版本——Writer 看不到全部真相，只看到 Planner 挑选的切片。这比 onkos"全量+constraints"更激进地控制上下文

## 最佳实践推荐

- **首选方案**：**novelist**（推镜法则+展示代替告知的写作品质）+ **onkos**（for-creation 上下文保障+自动化后处理）+ **inkos Governed Context**（受控上下文协议，防信息越界）
- **推荐理由**：novelist 提供最强的单场景写作指导，onkos 提供最可靠的上下文和记忆基础设施，inkos Governed Context 提供最安全的上下文控制
- **可组合方案**：onkos for-creation（获取上下文+constraints）→ inko-style ContextPackage（预选切片）→ novelist 推镜法则（写作技法）→ onkos store→extract→record（自动后处理）

## 空白地带

1. **无实时风格锁定验证**：生成过程中没有 skill 能实时检测"这一段是否偏离了锁定风格"
2. **无多版本草稿管理**：没有 skill 支持为同一章保留多个版本文本并比较
3. **无增量生成**：没有 skill 支持"先生成大纲骨架→再填充对话→再添加环境描写"的逐层生成
4. **无生成温度动态调节**：没有 skill 根据章节类型（爆发章/过渡章）自动调节 temperature
