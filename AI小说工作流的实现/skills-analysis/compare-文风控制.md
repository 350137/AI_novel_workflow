# 文风控制 — 跨 Skills/项目比对报告

## 覆盖度矩阵

| 分析对象 | 类型 | 覆盖度 | 实现方式 | 亮点 |
|----------|------|--------|---------|------|
| fiction-crafter | skill | ⚡ | 6条创作原则+6条禁忌事项 | 禁忌事项清单明确 |
| novelist | skill | ✅ | 5条强制句法红线（白描/肯定句/短句句号/禁止上帝视角/中文语感）；黑名单硬替换9组；否定转肯定；剥离心理锚点；对话排毒；形容词压缩；逐句自检 | **市面上最强的AI味清除规则** |
| novel-writer-cn | skill | ⚡ | 用户指定情感基调（轻松/虐心/热血） | — |
| story-cog | skill | ⚡ | 通过 prompt 指定语调；6条写作建议 | 强调"情感真实" |
| story-writer | skill | ❌ | 无 | — |
| my-novel-writer | skill | ✅ | `--set-style` 锁定风格；违禁词替换规则；第一人称强制锁定；补全机制（心理独白/环境渲染/动作细节/配角反应） | 风格锁定+违禁词替换双重保障 |
| openclaw-novel-write | skill | ✅ | writing-style + writing-requirements YAML；AI高频词黑名单9组；具象化三原则（时间/人物/数量）；单句成段30-50%；5个 requirements 文件 | 反AI检测规范最完善（v4版本） |
| tomato-novelist | skill | ✅ | 深度润色（去AI味+加番茄味）：去过度修饰/减少抽象/避免四字格律/增加口语化/金句设计；黄金开篇3版本 | 番茄味润色是与通用去AI味不同的层次 |
| onkos | skill | ✅ | style_learner.py + 统计指纹（句长/TTR/高频模式）；analyze-style/compare-style | 量化风格指标（非主观判断） |
| inkos | 项目 | ⚡ | Genre Profile 疲劳词表；Polisher Agent 文笔润色（严格边界：✅可做/❌禁止） | Polisher 职责边界极其严格 |

## 共同模式

1. **违禁词/疲劳词管理是标配**：novelist（黑名单9组）、my-novel-writer（违禁词替换）、openclaw-novel-write（9组禁用词）、onkos（疲劳词检测）、inkos（Genre Profile 疲劳词表）
2. **去AI味是共同目标**：novelist（句法红线）、openclaw-novel-write（反AI检测v4）、tomato-novelist（深度润色）都在解决同一问题
3. **风格锁定机制**：my-novel-writer（--set-style）、onkos（统计指纹）、openclaw-novel-write（writing-style YAML）
4. **对话品质被关注**：novelist（对话排毒：加动作打断+去端水发言）、openclaw-novel-write（对话比例建议≤50%）

## 差异化分析

| 特色做法 | 采用者 | 优劣分析 |
|---------|--------|---------|
| 句法红线（肯定句/禁止否定） | novelist | ✅ 最根本的去AI味方法 ❌ 执行难度高 |
| 统计指纹量化 | onkos | ✅ 可数学对比 ❌ 需要足够样本 |
| 反AI检测v4 | openclaw-novel-write | ✅ 最完善的规则体系 ❌ 200+禁用词可能过度 |
| 番茄味润色 | tomato-novelist | ✅ 平台特化 ❌ 不通用 |
| Polisher 严格边界 | inkos | ✅ 防润色越界 ❌ 边界判断本身需要准确性 |
| 金句设计 | tomato-novelist | ✅ 增加读者互动 ❌ 风格化过强可能不自然 |

## onkos/inkos 工作流视角

- **onkos**：统计指纹是唯一可量化的风格度量——能数学地回答"第50章的文风和第5章一样吗？"而不仅是主观感觉。style_learner 可以从已有章节学习风格特征
- **inkos**：Polisher 的职责边界设计（✅可做/❌禁止）是重要的架构原则——润色只改文笔不改情节。这防止了"润色时顺手改了个情节细节导致连锁矛盾"

## 最佳实践推荐

- **首选方案**：**novelist**（句法红线+黑名单——最深层的AI味清除）+ **onkos**（统计指纹——量化风格一致性）+ **openclaw-novel-write**（反AI检测规范——最全面的规则清单）
- **推荐理由**：novelist 从根本写作方法上解决问题（肯定句/白描），onkos 提供量化验证能力，openclaw 提供最全面的规则参考
- **可组合方案**：onkos style_learner（学习已有风格）→ novelist 句法红线（写作时遵守）→ openclaw 反AI规范（自检时对照）→ onkos compare-style（验证一致性）

## 空白地带

1. **无风格迁移能力**：没有 skill 能"学习作者A的风格，应用到小说B"（onkos style_learner 最近似但不支持迁移）
2. **无读者偏好风格适配**：不能根据目标读者群体（如"18-25岁男性"）自动调整文风复杂度
3. **无多视角风格管理**：第一人称/第三人称切换时，没有 skill 能自动调整叙事距离和描写密度
4. **无情绪色彩自动分析**：没有 skill 能量化"本章的情绪色彩是暖色还是冷色、明快还是沉重"
