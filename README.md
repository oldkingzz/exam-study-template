# exam-study-template

Reusable AI-assisted exam study framework for Claude Code, plus the skills that grew out of using it.

## What is here

| Path | What it is |
|---|---|
| `AI_Study_Framework.md` | The 6-phase study framework (materials → per-chapter guides → cheat sheet → mock tests). Validated on ESE 650 midterm, Spring 2026. |
| `CLAUDE.md.template` | Copy to a course folder as `CLAUDE.md` and fill in: exam format, key topics, materials, rules. |
| `raw/`, `study/` | Where raw materials and AI-generated study material go in a course folder. |
| `skills/teaching-lectures/` | ★ A Claude Code skill that turns lecture slides + a homework into one interactive HTML study guide. |

## `skills/teaching-lectures`

Given lecture slides (PDF) and a homework set, the skill produces a single self-contained `.html`:

- **Lesson half** — every concept the slides cover, one *card* each, in an order that meets the homework's concepts in the order the homework asks them. Each 记/推 card has an interactive widget (sliders, draggable points, live-computed checks) or an inline SVG/table, a boxed statement, and three tabs: worked example · where it is used today · self-check.
- **Solutions half** — every homework question fully worked in the submission language (English), each answer linking back to the card that taught it; multiple-choice items get a verdict per option.
- **Tags** decide depth: 记 *memorize* (a starting-point definition or formula), 推 *derive* (follows in ≤5 lines from 记 items, so the derivation is shown once and the self-check asks for it again), 了解 *awareness* (two lines, no example). The rule is written in `SKILL.md`.
- **A gate** (`scripts/check_guide.py`) checks the structural contract — every card tagged, every 记/推 card has a visual + example + application + self-check, every solution links back to a card and has a boxed answer, no lesson-language characters inside the solutions, visible-text budget per card — and prints `OK` or a list of fixes.

Files, one level deep from `SKILL.md`:

```
skills/teaching-lectures/
├── SKILL.md                 # workflow (8 steps with completion criteria), tag rule, language rule
├── pedagogy.md              # card anatomy, HTML-native rules, the evidence behind them, pitfalls
├── html-guide-template.md   # page skeleton, CSS classes the gate reads, tab/widget conventions
└── scripts/check_guide.py   # the gate
```

### Install

```bash
# Claude Code (user-level)
ln -s "$(pwd)/skills/teaching-lectures" ~/.claude/skills/teaching-lectures
```

Then, in a course folder with the slides downloaded, ask for a study guide for the module / homework; the skill's description triggers it, or invoke `/teaching-lectures`.

### Design notes

The skill follows Anthropic's skill-authoring guidance (third-person description with triggers, body under 500 lines, references one level deep, a checklist workflow, a script-backed feedback loop) and was built by iterating against real output: the first guide it produced read like a markdown file wearing HTML clothes, and the second iteration added the HTML-native rules and the gate checks that now enforce them.

Sample output is not committed: the guide it was validated on contains solutions to a live course's homework. Run it on your own slides.

## License

MIT.
