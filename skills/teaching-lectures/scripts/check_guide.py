#!/usr/bin/env python3
"""Gate for teaching-lectures study guides.

Usage: python3 check_guide.py guide.html

Checks the structural contract from html-guide-template.md and prints every
violation with enough detail to fix it. Exit 0 and prints OK when clean.
"""
import re
import sys
from html.parser import HTMLParser

TAGS = {"memorize", "derive", "aware"}
# Visible characters per card before it starts reading like a wall of text
# (roughly hook + statement + one open tab at the pedagogy.md budget).
VISIBLE_BUDGET = 900
CJK = re.compile(r"[぀-ヿ㐀-䶿一-鿿豈-﫿＀-￯]")


class Node:
    def __init__(self, tag, attrs, parent):
        self.tag = tag
        self.attrs = dict(attrs)
        self.parent = parent
        self.children = []
        self.text = []

    def classes(self):
        return set(self.attrs.get("class", "").split())

    def walk(self):
        yield self
        for c in self.children:
            yield from c.walk()

    def find(self, cls):
        return [n for n in self.walk() if cls in n.classes()]

    def has(self, cls):
        return any(cls in n.classes() for n in self.walk() if n is not self)

    def alltext(self):
        out = list(self.text)
        for c in self.children:
            out.append(c.alltext())
        return " ".join(out)


VOID = {"br", "hr", "img", "meta", "link", "input"}


class Tree(HTMLParser):
    def __init__(self):
        super().__init__()
        self.root = Node("root", [], None)
        self.cur = self.root

    def handle_starttag(self, tag, attrs):
        n = Node(tag, attrs, self.cur)
        self.cur.children.append(n)
        if tag not in VOID:
            self.cur = n

    def handle_endtag(self, tag):
        n = self.cur
        while n is not None and n.tag != tag:
            n = n.parent
        if n is not None and n.parent is not None:
            self.cur = n.parent

    def handle_data(self, data):
        self.cur.text.append(data)


def main(path):
    src = open(path, encoding="utf-8").read()
    t = Tree()
    t.feed(src)
    root = t.root
    errors, warns = [], []

    ids = {}
    for n in root.walk():
        i = n.attrs.get("id")
        if i:
            if i in ids:
                errors.append(f"duplicate id #{i}")
            ids[i] = n

    for req in ("toc", "lesson", "solutions"):
        if req not in ids:
            errors.append(f"missing required id #{req}")
    if "<title>" not in src[:8000]:
        errors.append("missing <title> in the first 8KB")
    if "mathjax" not in src.lower():
        errors.append("MathJax script not included")

    cards = root.find("card")
    if not cards:
        errors.append("no .card found")
    for c in cards:
        cid = c.attrs.get("id", "<no id>")
        tag = c.attrs.get("data-tag")
        if tag not in TAGS:
            errors.append(f"card #{cid}: data-tag must be one of {sorted(TAGS)}, got {tag!r}")
            continue
        if not c.has("tag"):
            errors.append(f"card #{cid}: missing .tag chip")
        if tag in ("memorize", "derive"):
            for need in ("statement", "example", "app", "selfcheck"):
                if not c.has(need):
                    errors.append(f"card #{cid} ({tag}): missing .{need}")
            visual = c.has("widget") or any(n.tag in ("svg", "canvas", "table") for n in c.walk())
            if not visual:
                errors.append(f"card #{cid} ({tag}): no visual (.widget, <svg>, <canvas> or <table>) — reads like markdown")
            # visible text budget: everything outside hidden panels / details bodies
            visible = 0
            for n in c.walk():
                p = n
                hidden = False
                while p is not None and p is not c:
                    if "panel" in p.classes() and "on" not in p.classes():
                        hidden = True
                    if p.tag == "details":
                        hidden = True
                    p = p.parent
                if not hidden and n.tag not in ("script", "style"):
                    visible += sum(len(t.strip()) for t in n.text)
            if visible > VISIBLE_BUDGET:
                warns.append(f"card #{cid}: {visible} visible chars > budget {VISIBLE_BUDGET} — cut text or move it behind a tab")
        for a in [n for n in c.walk() if "hw-badge" in n.classes()]:
            href = a.attrs.get("href", "")
            target = href[1:] if href.startswith("#") else None
            if not target or target not in ids or "solution" not in ids[target].classes():
                errors.append(f"card #{cid}: hw-badge href {href!r} does not resolve to a .solution")

    lectures = root.find("lecture")
    if not lectures:
        errors.append("no section.lecture found")
    for L in lectures:
        lid = L.attrs.get("id", "<no id>")
        for need in ("overview", "recap", "pitfall"):
            if not L.has(need):
                errors.append(f"lecture #{lid}: missing .{need} block")
        if not L.find("card"):
            errors.append(f"lecture #{lid}: has no cards")

    sols = root.find("solution")
    if not sols:
        errors.append("no .solution found")
    sol_section = ids.get("solutions")
    if sol_section is not None:
        cjk_hits = [m.group(0) for m in CJK.finditer(sol_section.alltext())]
        if cjk_hits:
            sample = "".join(cjk_hits[:12])
            errors.append(f"#solutions contains {len(cjk_hits)} CJK character(s) — solutions must be English only (e.g. '{sample}')")
    card_ids = {c.attrs.get("id") for c in cards}
    for s in sols:
        sid = s.attrs.get("id", "<no id>")
        if not s.attrs.get("data-q"):
            errors.append(f"solution #{sid}: missing data-q")
        if not s.has("final"):
            errors.append(f"solution #{sid}: missing .final answer box")
        links = [n.attrs.get("href", "") for n in s.walk() if n.tag == "a"]
        back = [h[1:] for h in links if h.startswith("#") and h[1:] in card_ids]
        if not back:
            errors.append(f"solution #{sid}: no link back to an existing card")

    toc = ids.get("toc")
    if toc:
        toc_targets = {n.attrs.get("href", "")[1:] for n in toc.walk() if n.tag == "a"}
        missing = [cid for cid in card_ids if cid not in toc_targets]
        if missing:
            warns.append(f"toc does not list {len(missing)} card(s): {', '.join(sorted(missing))}")
        dangling = [x for x in toc_targets if x not in ids]
        if dangling:
            errors.append(f"toc links to missing ids: {', '.join(sorted(dangling))}")

    # any '#x' anchor anywhere must resolve
    for n in root.walk():
        if n.tag == "a":
            h = n.attrs.get("href", "")
            if h.startswith("#") and h[1:] not in ids:
                errors.append(f"dangling anchor {h}")

    counts = {t: sum(1 for c in cards if c.attrs.get("data-tag") == t) for t in TAGS}
    hw_cards = sum(1 for c in cards if c.has("hw-badge"))
    print(f"cards: {len(cards)} (记 {counts['memorize']}, 推 {counts['derive']}, 了解 {counts['aware']}), "
          f"考点 cards: {hw_cards}, lectures: {len(lectures)}, solutions: {len(sols)}, size: {len(src)//1024}KB")
    for w in warns:
        print("WARN:", w)
    for e in errors:
        print("ERROR:", e)
    if errors:
        print(f"{len(errors)} error(s)")
        return 1
    print("OK")
    return 0


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    sys.exit(main(sys.argv[1]))
