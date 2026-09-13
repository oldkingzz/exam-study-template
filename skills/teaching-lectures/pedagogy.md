# Pedagogy reference for teaching-lectures

## Contents
- The five-part card
- Density rules (information per screen)
- What the evidence says (and the sources)
- Pitfalls that make guides fail

## Plain language (说人话) — the rule that overrides the others

The reader is a **complete beginner**: assume they know vector addition, the dot product, and matrix multiplication, and nothing else — remind them what a cross product is the first time it appears. A term they cannot decode is not "dense", it is a wall; every unexplained word after it is lost, and every self-check after it fails. The second version of a guide failed exactly here: the text budget was met by compressing explanations into jargon and abbreviations.

- **Every technical term, first time**: plain-language name in the reader's language → one sentence saying what it is in everyday terms → then the English term and its abbreviation, with the abbreviation *spelled out letter by letter* ("BRDF = Bidirectional 双向 · Reflectance 反射 · Distribution 分布 · Function 函数 — a lookup table of 'light comes in from here, I look from there, how bright'"). After that, use whichever name is shorter.
- **Every formula is read aloud first**: one sentence "this equation says …" in words with no symbols, *then* the formula, *then* each symbol explained with an everyday object, never with another term.
- **Abbreviations in application tabs too** (VIO, SLAM, PBR, HDR, CCD …): expand or replace with a plain description ("the positioning system inside a drone"). Name-dropping a system the reader has never heard of teaches nothing.
- **A glossary at the top** (`#glossary`): every term and abbreviation used anywhere in the lesson, three columns — plain name · English / abbreviation · one-sentence meaning. The gate cross-checks abbreviations against it.
- **Self-checks are tiered**: first "say it in your own words" (with a model answer in plain words), then a computation. A self-check that only asks for a computation tests nothing if the words were not understood.
- **The read-through test** (workflow step 8): read as someone who has never seen the topic; any word not explained on this page before its use is a defect, not a style choice.

Plain language and the text budget are not in tension: the budget cuts *restatement and decoration*; explanation in everyday words is the content and stays.

## The five-part card

Every 记 / 推 concept is one `.card` with these parts in this order. 了解 concepts use only parts 1–2 collapsed into a short paragraph that still obeys the plain-language rule.

1. **直觉 (hook)** — one concrete situation the student has seen with their own eyes, *before any symbol*. ("Why does a phone photo at night come out smeared?") One to three sentences.
2. **用人话说 (plain explanation, `.plain`)** — three to six sentences in everyday words that fully explain the idea *without symbols*: what the thing is, why anyone cares, what the name means (abbreviation spelled out). A reader who stops here should already understand the concept; the formula below only makes it precise.
3. **定义 / 公式 (the statement)** — the thing to remember, boxed. Open with the formula read aloud in words. Name every symbol on the line where it first appears, with an everyday referent. For 推 cards this is where the ≤ 5-line derivation lives, each line justified in a few words.
4. **算一遍 (worked example)** — real numbers, every intermediate step written out, ending in a checked result ("substitute back: 1−2+1=0 ✓"). Choose numbers that make the arithmetic visible, not heroic.
5. **现在哪里用 (modern application)** — one system or product the reader has plausibly touched (the phone's night mode, a panorama, a car's surround camera), described in plain words, then the technical name in parentheses. Say *which part* of the idea it relies on.
6. **自测 (self-check)** — two tiers, answers hidden in `<details>`: (a) "用自己的话说一遍" with a model answer in plain words; (b) a computation or derivation. Where possible interleave: reuse a symbol or object from an earlier card.

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
- **Jargon as content.** Cards that are bullets of terms and abbreviations; the reader reports "I can't understand any of it, what is BRDF". Fix: the plain-language rule; the `.plain` block is mandatory and comes before the formula; every abbreviation is in the glossary.
- **Markdown in HTML clothing.** Paragraph after paragraph, a table or two, no interaction — the reader reports "reading this feels like reading a .md". Fix: the HTML-native rules above; cut text until the visual carries the idea.
- **Lesson language leaking into the submittable working.** Fix: the solution's walkthrough lives in a `.zh` block; everything outside it is submission-language only, and the gate rejects CJK characters there (extend the regex if your lesson language is a different script).
- **Solutions that are correct but opaque.** A perfectly worked English answer the student cannot follow teaches nothing. Fix: the `.zh` walkthrough first — what is being asked, in everyday words, with a tiny instance — then the working.
