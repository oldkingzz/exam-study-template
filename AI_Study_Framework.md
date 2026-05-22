# AI-Assisted Exam Study Framework

A reusable, 6-phase framework for using AI (Claude Code) to prepare for university exams. Validated on ESE 650 (Learning in Robotics) midterm, 2026-03-22.

---

## Prerequisites (开始前必须准备)

| 材料 | 重要性 | 说明 |
|------|--------|------|
| Lecture slides (PDF) | **必须** | AI 从这里提取知识，没有就无法生成教程 |
| 往年考题 / 样题 | **必须** | 定义考试风格、题型、分值分布 |
| Homework / 作业 | 推荐 | 补充细节和应用场景 |
| 考试范围说明 | 推荐 | 明确哪些章节考、哪些不考，避免浪费时间 |

---

## Phase 0: 项目初始化 (~10 min)

### 目标
建立项目结构和 AI 指令文件，让 AI 在整个复习过程中保持一致。

### 操作
1. 创建项目文件夹，将所有原始材料放入
2. 创建 `CLAUDE.md`（AI 指令文件），内容包括：

```markdown
# [课程名] Exam Prep

## Goal
Help prepare for [课程名] [考试类型] on [日期].

## Exam Format
- 时长、开卷/闭卷、cheat sheet 规则
- 题目数量、总分
- 题型（True/False、简答、推导、设计题等）

## Key Topics
- Chapter X (XX pts): [主题列表]
- Chapter Y (YY pts): [主题列表]
- ...

## Available Materials
- Lecture slides: `pdf/01.pdf` to `pdf/XX.pdf`
  - 标注哪些需要重点看、哪些跳过
- Homework: `HW/`
- Past exams: `[文件名]`

## Study Materials (AI 生成，放在 `study/` 文件夹)
1. 各章节 Complete Guide
2. Cheat sheet
3. 练习题
4. 错题分析

## Rules
- [你的学习偏好，如：用中文解释、英文答题]
- [答题格式要求]
- [其他约束]
```

3. 创建 `study/` 子文件夹

### 产出
```
project/
├── CLAUDE.md          # AI 指令
├── pdf/               # 原始课件
├── HW/                # 作业
├── past_exam.md       # 往年考题 (建议转 markdown)
└── study/             # AI 生成的学习材料 (初始为空)
```

---

## Phase 1: 系统性知识构建 (~2-4 hours)

### 目标
将每章课件转化为结构化的学习文档。

### 操作
1. **逐章生成 Complete Guide**
   - 给 AI 看该章 PDF（截图或直接发）
   - 要求生成包含以下内容的教程：
     - 概念发展脉络（为什么需要这个东西）
     - **第一性原理视角（必须）**：讲清这东西的根 / 为什么非它不可 / 从哪个更基本前提长出来，不只罗列公式
     - 核心公式 + 推导
     - 直觉解释（用工程/机器人例子，不要生活类比）
     - 常见易错点
     - 自测题 + 答案

> **第一性原理 + 防暴增（核心原则）**：complete guide 必须带第一性原理视角，用 `> 💡 **First Principles**:` callout 标出。但根问题若需长篇大论，guide 里只“卖关子”（点出结论 + 指向 QA），把深挖放进单独的 QA 文件，保持 guide 精炼、QA 承接深挖。

2. **同步生成 Cheat Sheet**
   - 一页纸，双面
   - 所有公式用 LaTeX
   - 按章节分区，方便查找
   - 每学完一章就更新

### 关键指令示例
```
请根据 pdf/03.pdf 生成 study/03_complete_guide.md，
包括：概念脉络、核心公式、直觉解释、易错点、自测题。
用中文写，公式用 LaTeX。
```

### 产出
```
study/
├── 02_complete_guide.md
├── 03_complete_guide.md
├── 04_complete_guide.md
├── ...
└── cheat_sheet.md
```

### 注意事项
- 用 **Markdown Preview** 看文件（终端无法渲染 LaTeX）
- 不理解的地方立即追问，AI 会追加到文档中
- 如果某一章完全不懂，要求 AI 从零写专项教程

---

## Phase 2: 模拟考试 + 弱点定位 (~1-2 hours)

### 目标
用往年真题做模拟考试，量化薄弱环节。

### 操作
1. **独立做题**（计时，模拟真实考试条件）
2. **提交给 AI 评分**，告诉它每题的得分/失分情况
3. **AI 输出分析报告**：
   - 总分和得分率
   - 按失分排序的弱点列表
   - 每个错题的错因分类（概念不清 / 公式记错 / 答非所问 / 完全不会）

### 关键指令示例
```
我的模拟考成绩：P1(2) 全错 -4分，P1(3e) 全错 -4分，
P2(1) 全错 -4分，P4(b) 全错 -8分...
帮我算总分，按失分排序弱点，生成 study/after_mock.md
```

### 产出
```
study/
└── after_mock.md    # 错题分析 + 弱点优先级排序
```

---

## Phase 3: 针对性强化 (~2-3 hours)

### 目标
对 Phase 2 定位的弱点做深度补强。

### 操作（按优先级从高到低）

1. **重灾区（全错 + 高分值）**
   - 要求 AI 把原题翻译成母语，逐步详解
   - 如果是整章不懂，从 lecture slides 生成专项教程
   - 例：`study/nerf_tutorial.md`

2. **半懂区（部分得分）**
   - 追加解释到已有 guide 中
   - 或创建 QA 文件记录概念辨析

3. **粗心区（公式/符号错误）**
   - 更新 cheat sheet，标注易错点
   - 做一两道同类练习题确认

### 关键指令示例
```
我整个 NeRF 一章都没理解，请从 pdf/04.pdf 生成
study/nerf_tutorial.md，从零开始教，用中文。
```

### 注意事项
- **错题驱动**，不要全面复习（ROI 最高的是失分最多的地方）
- 对不懂的符号/记号要求 AI 解释（如 $SE(3)$, $\hat{\omega}$）
- 复习完一个弱点后，让 AI 出 1-2 道类似的题当场验证

---

## Phase 4: 快速测试 (~1-1.5 hours)

### 目标
通过轮询式出题，检验所有章节的掌握程度。

### 操作
1. 让 AI 创建 `study/final_test.md`
2. **规则设定**：
   - 按章节轮流出题（Ch2 → Ch3 → Ch4 → ... → 循环）
   - 一次一道，你在聊天框回答
   - AI 即时评分 + 解析
   - 不会的题展开详细讲解，写入文件
   - 题目特点：概念辨析、tricky True/False、简短推导（无复杂计算、无画图）

3. **做完后 AI 输出总成绩单**：
   - 每题得分
   - 各章节得分率
   - 剩余弱点诊断

### 关键指令示例
```
创建 study/final_test.md，按 Note2-Note5 轮询出题。
一次一道，我在聊天框回答，你评分。
题目要 tricky，不要复杂计算和画图。
不会的题详细解释并写入文件。开始出 Note2 第一题。
```

### 注意事项
- 如果连续几道同类题错，说明 Phase 3 没补到位 → 暂停测试，回去补
- 让 AI 在最后出 3-5 道"你没想到会考的题"（跨章节组合、反向提问等）

---

## Phase 5: 答题模板化 (~30 min)

### 目标
对高分值题型提炼标准化的答题模板。

### 操作
1. 识别高分值题型（通常是设计题、推导题）
2. 让 AI 拆解：
   - 完整的满分答案
   - 得分点分布
   - 常见错误写法及其扣分
   - 答题结构模板

### 关键指令示例
```
请完整给出 P4(b) 的题目、满分答案、得分点拆解。
我想知道这一类设计题应该怎么写。
```

### 通用答题模板

**True/False 题：**
```
[True/False]. [1句解释原因]. [可选：反例或关键公式]
```

**推导题：**
```
1. 写出模型参数 (A, B, C, R, Q 等)
2. 代入公式
3. 化简
```

**设计题（万能4步）：**
```
1. Method: 一句话说方法
2. Training/Setup: 数学目标 (loss function)
3. Output: 怎么从模型得到最终结果
4. Why it works: 为什么能解决题目的问题
```

---

## Phase 6: 考前 30 分钟

### 操作
1. 过一遍 cheat sheet，确认所有公式都在
2. 看 `final_test.md` 中的错题解析（只看错的）
3. 默背 3-5 个最容易忘的知识点

---

## 效率对比

| 传统复习 | AI-Assisted |
|---------|-------------|
| 手动整理笔记 2-3 天 | AI 生成 Complete Guide 2-4 小时 |
| 自己找弱点（凭感觉） | 模拟考 + AI 量化排序 |
| 被动看笔记 | 主动答题 + 即时反馈 |
| Cheat sheet 写完发现缺东西 | 边学边更新，同步维护 |
| 不知道还能怎么考 | AI 出"你没想到的题" |

---

## Checklist (可打印)

- [ ] Phase 0: `CLAUDE.md` + 项目结构
- [ ] Phase 1: 各章 Complete Guide + Cheat Sheet
- [ ] Phase 2: 模拟考 + `after_mock.md`
- [ ] Phase 3: 弱点专项教程
- [ ] Phase 4: `final_test.md` 轮询测试
- [ ] Phase 5: 高分题型答题模板
- [ ] Phase 6: 考前 30 分钟速览
