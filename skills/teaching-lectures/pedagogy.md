# Pedagogy reference for teaching-lectures

## Contents
- The five-part card
- Density rules (information per screen)
- What the evidence says (and the sources)
- Pitfalls that make guides fail

## The five-part card

Every 记 / 推 concept is one `.card` with these parts in this order. 了解 concepts use only parts 1–2 collapsed into two lines.

1. **直觉 (hook)** — one concrete situation the student has seen with their own eyes, *before any symbol*. ("Why does a phone photo at night come out smeared?") One to three sentences.
2. **定义 / 公式 (the statement)** — the thing to remember, boxed. Name every symbol on the line where it first appears. For 推 cards this is where the ≤ 5-line derivation lives, each line justified in a few words.
3. **算一遍 (worked example)** — real numbers, every intermediate step written out, ending in a checked result ("substitute back: 1−2+1=0 ✓"). Choose numbers that make the arithmetic visible, not heroic.
4. **现在哪里用 (modern application)** — one named system, product, or paper family where this exact idea is load-bearing today (AprilTag, ARKit plane detection, NeRF, OpenCV `calibrateCamera`, panorama stitching …). One or two sentences; say *which part* of the idea the application relies on.
5. **自测 (self-check)** — one question the student answers from memory, with the answer hidden in `<details>`. For 记 cards ask for the statement; for 推 cards ask for the derivation or a fresh numeric instance. Where possible interleave: reuse a symbol or object from an earlier card.

A card that a homework question depends on also carries a **考点** badge (`.hw-badge`) naming the question, placed in the card header so it is visible while skimming.

## HTML-native rules (the page must not read like markdown)

The first version of a guide failed on exactly this: dense paragraphs that a `.md` file could have carried. The test for every card: *what here could not exist in markdown?* If the answer is "nothing", the card is not done.

- **One visual per 记/推 card, and it comes first.** In order of preference: an **interactive widget** (sliders, draggable points, live-computed numbers — every formula with a knob gets a knob), an **inline SVG diagram** with the symbols of the statement drawn on it, or a **comparison table**. The visual sits in the top row beside the boxed statement.
- **Tabs, not stacking.** The card body below the top row is a tab strip — 算一遍 · 现在哪里用 · 自测 — showing one facet at a time. Visible text per card stays small; the depth is still there one click away.
- **Text budget** (visible at once): hook ≤ 1 line (~40 chars); statement ≤ 5 bullets or 2 display formulas + 3 bullets; each tab ≤ 6 lines. Prose that exceeds the budget is converted to a table, a diagram label, or a widget readout — never wrapped into another paragraph.
- **Overview strip per lecture**: one screen showing the lecture's concepts as nodes with the homework questions they feed (an SVG map or a chip grid), so the student sees the shape before the parts.
- **Live checks in the widget**: where the concept has a verification (substitute back, \(l^Tp=0\), det = 0), the widget prints it. Seeing "✓ 0.000" as you drag beats reading "check: 0 ✓".
- **Answers hidden, questions visible**: self-check answers behind `<details>`; optional depth behind a tab.
- **A sticky table of contents** listing every card, so solutions and cards link both ways.
- **Recap** (`.recap`) per lecture as the exam-night sheet: 记 items as a bare list, 推 items as "from X get Y" one-liners. **Pitfalls** (`.pitfall`): three to six *wrong belief → correction* lines.
- Diagrams are inline SVG or canvas; never a screenshot of the slides. Widgets are vanilla JS, self-contained, no build step.

## What the evidence says

The card anatomy is not taste; each part maps to a strategy with decades of support. The first two carry the strongest evidence; the last two are supportive but weaker.

| card part | strategy | why it is there |
|---|---|---|
| 算一遍 | **worked examples** (Sweller's worked-example effect) | novices learn a procedure faster from a fully worked instance than from solving; that is why every 记/推 card shows a complete instance before asking anything |
| 自测 | **retrieval practice** | recalling beats rereading for retention; the hidden-answer format forces a retrieval attempt |
| 直觉 | **concrete examples** before abstraction | abstract statements attach to memory only through instances |
| statement + example side by side, diagrams | **dual coding** | verbal + visual channels together |
| 现在哪里用, the *why* lines | **elaboration** | linking to existing knowledge; evidence is real but weaker than the two above |
| recap blocks, interleaved self-checks | **spacing / interleaving** | the recap is the spaced re-exposure; interleaving a self-check with an earlier card mixes practice |

Sources (primary write-ups, not summaries): The Learning Scientists, *Six Strategies for Effective Learning* (learningscientists.org/blog/2016/8/18-1); Weinstein, Madan & Sumeracki, *Teaching the science of learning*, Cognitive Research: Principles and Implications (2018), which reviews the evidence strength per strategy; Sweller's worked-example literature for part 3; the expertise-reversal effect for why 了解 items get *no* worked example (examples help novices and cost experts).

## Pitfalls that make guides fail

- **Symbol before meaning.** A formula appears with a symbol defined three cards later. Fix: name symbols on the line they appear.
- **Coverage from memory.** Writing what you know about the topic instead of what the slides cover. Fix: the inventory is the checklist; the slides are the syllabus.
- **Emphasis by volume.** Giving every card the same depth. Fix: 考点 cards get the fullest example and the hardest self-check; 了解 cards get two lines.
- **Solutions that restart the lesson.** Re-explaining the concept inside the answer. Fix: link back to the card; the solution only *applies* it.
- **Multiple-choice answered by listing the right letters.** Fix: every option gets a verdict and a reason; that is where the learning is.
- **Unverified arithmetic.** Fix: Step 4 of the workflow — solve in a script first.
- **Answers visible by default.** Fix: `<details>`; the student must be able to attempt first.
- **Markdown in HTML clothing.** Paragraph after paragraph, a table or two, no interaction — the reader reports "reading this feels like reading a .md". Fix: the HTML-native rules above; cut text until the visual carries the idea.
- **Lesson language leaking into solutions.** Fix: the solutions section is written only in the submission language; the gate rejects CJK characters there (extend the regex if your lesson language is a different script).
