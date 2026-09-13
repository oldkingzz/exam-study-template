---
name: teaching-lectures
description: Builds a self-contained HTML study guide that teaches a course module from lecture slides or notes to a complete beginner, then works the assigned homework in full at the end of the same page. Use when the user asks to be taught lecture material, wants a 讲义 / study guide / 复习 built from slides, or wants homework explained with complete solutions tied back to the lessons.
---

# Teaching lectures → one HTML study guide

Output is **one `.html` file with two halves in one arc**: the *lesson* (every concept the sources cover, beginner-first) and the *solutions* (every homework question, fully worked, each linking back to the card that taught it). The slides decide **coverage**; the homework decides **emphasis**.

Three leading words run through the whole job:

- **inventory** — the exhaustive list of concepts in the sources. Coverage is checked against it, never against memory.
- **card** — the unit of teaching. One concept = one card with the five fixed parts in [pedagogy.md](pedagogy.md).
- **gate** — the machine check that must pass before the file is delivered.

## Workflow

Copy this checklist into your working notes and tick it as you go:

```
Study-guide progress:
- [ ] 1 Sources → text
- [ ] 2 Inventory
- [ ] 3 Homework map
- [ ] 4 Solve first (script)
- [ ] 5 Write the lesson (cards)
- [ ] 6 Write the solutions
- [ ] 7 Gate
- [ ] 8 Read it as the student
```

**Step 1 — Sources → text.** `pdftotext -layout <slides.pdf> <out.txt>` per lecture into the scratchpad. Slides with equations often render as `<latexit>` blobs: recover the equation from the surrounding text and your own knowledge, and mark it in the inventory as *reconstructed*. Done when every source file has a text twin and you have read all of them end to end.

**Step 2 — Inventory.** Write `inventory.md` in the scratchpad: one line per concept, in slide order: `L<n> | concept | tag | HW hit`. Tag with the decision rule below. Done when a second pass over the slide text adds no new line.

**Step 3 — Homework map.** For each homework question list the inventory lines it needs. Every such line gets the `HW hit` column filled with the question id (e.g. `HW1 Q2.1`). Done when every question maps to ≥1 concept and every mapped concept is in the inventory (add it if the homework needs something the slides only imply — mark it *beyond slides*).

**Step 4 — Solve first.** Work every homework question in a script (numpy / sympy) or on paper *before* writing any prose; keep the script in the scratchpad. Symbolic identities get a random-vector numeric check; geometry gets a substitution check. Done when every answer has a printed verification line. Ambiguous multiple-choice items: decide using the slide that the question paraphrases, then record the ambiguity so the solution can state it honestly.

**Step 5 — Write the lesson.** The reader is a **complete beginner**; the **plain-language rule** in [pedagogy.md](pedagogy.md) overrides everything else: every term gets a plain name and an everyday explanation before its English name or abbreviation, every formula is read aloud in words before it is written, every abbreviation is spelled out and listed in the `#glossary` at the top of the page. One card per inventory line, in an order that (a) respects prerequisites and (b) meets the homework's concepts in the order the homework asks them. Follow the card anatomy and the **HTML-native rules** in pedagogy.md; use the skeleton, tab markup and widget conventions in [html-guide-template.md](html-guide-template.md). Every 记/推 card carries a `.plain` block (用人话说) *before* the boxed statement and a **visual** (interactive widget, SVG diagram, or comparison table). Every card carries its tag; every card with an `HW hit` carries a `考点` badge naming the question. Each lecture opens with a one-screen *overview strip* and ends with a *回头看* recap and a *常见坑* pitfalls block. Done when every inventory line has a card, every 记/推 card has a plain block, a visual, a worked example and a two-tier self-check, and the glossary covers every abbreviation the gate finds.

**Step 6 — Write the solutions.** **Solutions are written entirely in English** — headings, working, final answers, no CJK characters anywhere inside `#solutions` — because the student submits them as-is. Open with a one-paragraph map ("you have already met everything you need: Q1 ← cards …"). Then one `.solution` block per question: restate → link the card(s) → work it fully → box the final answer → one line on *why this is what they wanted*. Multiple-choice: give the verdict for **every** option, not only the chosen ones. Done when each solution links to ≥1 existing card id, states a final answer, and the gate's CJK check is clean.

**Step 7 — Gate.** Run `python3 <this skill's directory>/scripts/check_guide.py <file>.html`. Fix every reported error and rerun until it prints `OK`. The gate is a floor, not the bar.

**Step 8 — Read it as the student.** Open the file (browser or screenshot) and read one full lecture section plus one solution as someone who has never seen the topic and does not know what the abbreviations stand for. Any word not explained on this page before its use, any formula not read aloud in words, any self-check that presumes a term the reader could not have understood — each is a defect, fix it. Done when that read-through needs no outside knowledge.

## Tag decision rule (memorize vs derive vs awareness)

Ask: *if the student forgot this in the exam, could they rebuild it from the other tagged items in the same module?*

| answer | tag | card obligation |
|---|---|---|
| no — it is a definition or a starting-point formula | **记** memorize | boxed statement + worked example + self-check that asks for recall |
| yes, in ≤ 5 lines | **推** derive | show the derivation once, then the self-check asks the student to re-derive it |
| it never appears in exams or homework (history, hardware trivia, a named person) | **了解** awareness | one or two lines, no example required |

Examples: the layout of the hat matrix is 记; "line through two points is p₁×p₂" is 推 (from incidence + cross-product orthogonality); Brunelleschi inventing perspective is 了解.

## Language

Lesson prose in the language the user writes in; technical terms in English at first mention with a gloss in that language, then whichever is shorter. **Solutions in the course's submission language** — English for most courses — with no characters from the lesson language leaking in (they get submitted as-is). Formulas in MathJax, never as images. The tag chips and tab labels in the template are Chinese (记 / 推 / 了解, 算一遍 / 现在哪里用 / 自测); swap the visible labels for the user's language, keep the class names the gate reads.

## Files

- [pedagogy.md](pedagogy.md) — card anatomy, density rules, the evidence behind them, pitfalls to avoid.
- [html-guide-template.md](html-guide-template.md) — page skeleton, CSS classes the gate looks for, MathJax include.
- `scripts/check_guide.py` — the gate. Run it; do not paraphrase its checks by hand.
