# HTML skeleton and classes for teaching-lectures

The gate script (`scripts/check_guide.py`) looks for exactly these ids and classes. Keep the names; restyle freely.

## Contents
- Required structure
- Class reference
- Skeleton (copy, then fill)
- Density and theme notes

## Required structure

```
<title>…</title>
<nav id="toc">                 sticky table of contents; one <a href="#card-id"> per card
<main>
  <section id="lesson">        every lecture section, every card
  <section id="solutions">     one .solution per homework question
```

MathJax is loaded from jsDelivr (`tex-mml-chtml.js`); inline math `\( … \)`, display math `\[ … \]`. The file is opened locally in a browser, so the CDN is fine; there is no offline requirement.

## Class reference

| element | class / attribute | rule the gate enforces |
|---|---|---|
| one concept | `<article class="card" id="…" data-tag="memorize|derive|aware">` | tag required; id unique |
| the card's visual | `<div class="widget" data-widget="name">` (interactive), or an `<svg>`, `<canvas>`, or `<table>` inside the card | memorize/derive cards must contain one |
| tab strip | `<div class="tabs"><button class="tab on" data-tab="ex">算一遍</button>…</div>` + panels `<div class="panel on" data-panel="ex">` | — (JS below) |
| lecture overview | `<div class="overview">` at the top of each `section.lecture` | ≥1 per lecture |
| tag chip in the header | `<span class="tag">记 / 推 / 了解</span>` | present |
| homework link in the header | `<a class="hw-badge" href="#sol-q2-1">考点 · HW1 Q2.1</a>` | href must resolve to a `.solution` id |
| hook | `<p class="hook">` | — |
| plain explanation (用人话说) | `<div class="plain">` — before `.top` | required on memorize/derive |
| glossary | `<section id="glossary">` with a table: plain name · English / abbreviation · one-sentence meaning | required; every ALL-CAPS abbreviation used in `#lesson` must appear in it |
| boxed statement | `<div class="statement">` | required on memorize/derive |
| worked example | `<div class="example">` | required on memorize/derive |
| modern application | `<div class="app">` | required on memorize/derive |
| self-check | `<details class="selfcheck"><summary>…</summary>…</details>` | required on memorize/derive |
| per-lecture recap | `<div class="recap">` | ≥1 per lecture section |
| per-lecture pitfalls | `<div class="pitfall">` | ≥1 per lecture section |
| lecture section | `<section class="lecture" id="l1">` | ≥1 |
| one homework answer | `<article class="solution" id="sol-q2-1" data-q="Q2.1">` | must contain ≥1 `<a href="#card-id">` to an existing card and one `.final`; **no CJK characters in `#solutions` outside `.zh` blocks** |
| lesson-language walkthrough inside a solution | `<div class="zh">` — first thing in the solution, labelled "not for submission" | warned if missing; the only place CJK is allowed in `#solutions` |
| boxed final answer | `<div class="final">` | required in every solution |

## Skeleton (copy, then fill)

```html
<title>CIS 5800 · HW1 讲义</title>
<style>
:root{--bg:#fafaf8;--fg:#1a1a1a;--muted:#5c5c5c;--line:#e2e0da;--card:#ffffff;
  --memo:#b3261e;--derive:#1d5fa8;--aware:#6b6b6b;--hw:#8a5a00;--hwbg:#fff4d6;--accent:#0b6b3a;}
@media (prefers-color-scheme: dark){:root:not([data-theme="light"]){--bg:#141414;--fg:#ececec;--muted:#a3a3a3;--line:#2b2b2b;--card:#1d1d1d;--hwbg:#3a2f12;}}
:root[data-theme="dark"]{--bg:#141414;--fg:#ececec;--muted:#a3a3a3;--line:#2b2b2b;--card:#1d1d1d;--hwbg:#3a2f12;}
body{margin:0;background:var(--bg);color:var(--fg);font:15px/1.6 -apple-system,"PingFang SC","Noto Sans SC",system-ui,sans-serif;}
.wrap{display:grid;grid-template-columns:240px minmax(0,1fr);gap:24px;max-width:1240px;margin:0 auto;padding:16px;}
#toc{position:sticky;top:0;align-self:start;max-height:100vh;overflow:auto;font-size:13px;border-right:1px solid var(--line);padding-right:12px;}
#toc a{display:block;color:var(--muted);text-decoration:none;padding:2px 0;}
#toc a:hover{color:var(--fg);}
#toc .l{margin-top:10px;font-weight:600;color:var(--fg);}
.card{background:var(--card);border:1px solid var(--line);border-left:4px solid var(--aware);border-radius:8px;padding:14px 16px;margin:14px 0;}
.card[data-tag="memorize"]{border-left-color:var(--memo);}
.card[data-tag="derive"]{border-left-color:var(--derive);}
.card h3{margin:0 0 6px;font-size:17px;display:flex;flex-wrap:wrap;gap:8px;align-items:center;}
.tag{font-size:11px;padding:1px 7px;border-radius:10px;color:#fff;background:var(--aware);}
.card[data-tag="memorize"] .tag{background:var(--memo);}
.card[data-tag="derive"] .tag{background:var(--derive);}
.hw-badge{font-size:11px;padding:1px 7px;border-radius:10px;background:var(--hwbg);color:var(--hw);text-decoration:none;font-weight:600;}
.hook{color:var(--muted);margin:4px 0 8px;}
.two{display:grid;grid-template-columns:1fr 1fr;gap:14px;}
@media (max-width:900px){.two{grid-template-columns:1fr;} .wrap{grid-template-columns:1fr;} #toc{position:static;max-height:none;border:0;}}
.statement{border:1px solid var(--line);border-radius:6px;padding:10px 12px;background:color-mix(in srgb,var(--card) 85%,var(--bg));}
.example{border-left:3px solid var(--accent);padding:6px 12px;}
.app{font-size:14px;color:var(--muted);margin-top:8px;}
.selfcheck{margin-top:8px;} .selfcheck summary{cursor:pointer;font-weight:600;}
.recap,.pitfall{border:1px dashed var(--line);border-radius:8px;padding:10px 14px;margin:16px 0;}
.pitfall li b{color:var(--memo);}
.solution{background:var(--card);border:1px solid var(--line);border-radius:8px;padding:14px 16px;margin:14px 0;}
.final{border:2px solid var(--accent);border-radius:6px;padding:8px 12px;margin-top:8px;font-weight:600;}
table{border-collapse:collapse;font-size:14px;} td,th{border:1px solid var(--line);padding:4px 8px;vertical-align:top;}
.tbl{overflow-x:auto;}
code{font-size:13px;}
</style>
<script>MathJax={tex:{inlineMath:[['\\(','\\)']],displayMath:[['\\[','\\]']]}};</script>
<script async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>

<div class="wrap">
<nav id="toc">
  <div class="l">L1 · …</div>
  <a href="#c-…">…</a>
  <div class="l">作业答案</div>
  <a href="#sol-q1-1">Q1.1</a>
</nav>
<main>
<header>… 页头:课程、作业、截止日期、图例(记/推/了解/考点)、阅读路线 …</header>

<section id="lesson">
<section class="lecture" id="l1">
  <h2>Lecture 1 · …</h2>
  <article class="card" id="c-…" data-tag="memorize">
    <h3>标题 <span class="tag">记</span> <a class="hw-badge" href="#sol-q1-1">考点 · HW1 Q1.1</a></h3>
    <p class="hook">…</p>
    <div class="two">
      <div class="statement">…</div>
      <div class="example"><b>算一遍</b> …</div>
    </div>
    <div class="app"><b>现在哪里用</b> …</div>
    <details class="selfcheck"><summary>自测:…</summary><p>…</p></details>
  </article>
  <div class="recap"><b>回头看 · L1</b> …</div>
  <div class="pitfall"><b>常见坑 · L1</b><ul><li><b>错:</b>… → 对:…</li></ul></div>
</section>
</section>

<section id="solutions">
<h2>Homework 1 · 完整解答</h2>
<p>…map paragraph…</p>
<article class="solution" id="sol-q1-1" data-q="Q1.1">
  <h3>Q1.1 …</h3>
  <p>用到:<a href="#c-…">…</a></p>
  … full working …
  <div class="final">答案:…</div>
</article>
</section>
</main>
</div>
```

## Tabs and widgets (vanilla JS, paste once at the end of the page)

```html
<script>
document.querySelectorAll('.tabs').forEach(strip=>{
  strip.querySelectorAll('.tab').forEach(btn=>btn.addEventListener('click',()=>{
    const card=strip.closest('.card');
    card.querySelectorAll('.tab').forEach(b=>b.classList.toggle('on',b===btn));
    card.querySelectorAll('.panel').forEach(p=>p.classList.toggle('on',p.dataset.panel===btn.dataset.tab));
  }));
});
</script>
```

Widget conventions: one `<div class="widget" data-widget="…">` per card; controls are `<input type="range">` with a live `<output>`; draggable points are SVG circles with pointer events; every widget prints its verification line (e.g. `lᵀp = 0.000 ✓`). Keep each widget's JS in a function named after `data-widget` and call it once at the end. Use `Number.toFixed` for readouts; guard division by zero (a point at infinity is a *result*, not an error).

Card layout that satisfies the rules:

```html
<article class="card" id="c-…" data-tag="derive">
  <h3>标题 <span class="tag">推</span> <a class="hw-badge" href="#sol-q2-1">考点 · HW1 Q2.1</a></h3>
  <p class="hook">一句话直觉</p>
  <div class="plain">用人话说:3–6 句,不出现符号;说清它是什么、为什么要管它、名字(含缩写逐字母)是什么意思。</div>
  <div class="top">
    <div class="widget" data-widget="joinmeet">…</div>          <!-- or <svg> / <table> -->
    <div class="statement">…≤5 bullets or 2 formulas + 3 bullets…</div>
  </div>
  <div class="tabs"><button class="tab on" data-tab="ex">算一遍</button><button class="tab" data-tab="app">现在哪里用</button><button class="tab" data-tab="sc">自测</button></div>
  <div class="panel on" data-panel="ex"><div class="example">…</div></div>
  <div class="panel" data-panel="app"><div class="app">…</div></div>
  <div class="panel" data-panel="sc"><details class="selfcheck"><summary>…</summary><p>…</p></details></div>
</article>
```

## Density and theme notes

- Body font 15px, line-height 1.6; cards 14–16px padding. Two-column `.two` grid inside a card; collapses under 900px.
- Light palette on bare `:root`; dark palette under both `prefers-color-scheme` (guarded) and `[data-theme="dark"]`.
- Side gutter never below 16px; only `.tbl` wrappers may scroll horizontally.
- No external images; SVG inline when a figure earns its place.
