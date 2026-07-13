#!/usr/bin/env python3
"""Regenerate wiki/categories.md as a projection of each source page's `category:`
frontmatter. Deterministic, idempotent, no drift — the frontmatter is the source of
truth. Run from the wiki root (the dir containing .pin-llm-wiki.yml), or pass it as argv[1].

  python3 <skill-dir>/scripts/gen_categories.py [wiki_root]

Behavior:
  - Category display order comes from the `categories:` list in .pin-llm-wiki.yml.
  - Every [[slug]] in wiki/index.md is grouped under its page's `category:`.
  - A slug whose category is missing/unknown (not in the config list) goes to
    "Uncategorized" (rendered last) — surfaced in the report for human review.
  - One-line blurbs are pulled from the matching paragraph in wiki/overview.md.
Exit non-zero if the integrity check fails (a slug missing from index, or a source
file that can't be resolved). Prints a short report to stdout.
"""
import os, re, sys, datetime
from collections import defaultdict

root = os.path.abspath(sys.argv[1]) if len(sys.argv) > 1 else os.getcwd()
CFG = os.path.join(root, ".pin-llm-wiki.yml")
INDEX = os.path.join(root, "wiki", "index.md")
SRC = os.path.join(root, "wiki", "sources")
OVERVIEW = os.path.join(root, "wiki", "overview.md")
CATS_MD = os.path.join(root, "wiki", "categories.md")
DOMAIN_DEFAULT = "wiki"

def die(msg):
    print(f"gen_categories: ERROR: {msg}", file=sys.stderr)
    sys.exit(1)

if not os.path.isfile(CFG):
    die(f"no .pin-llm-wiki.yml at {root} (run from the wiki root or pass it as argv[1])")

# --- config: categories list (order) + domain, parsed without PyYAML ---
categories, domain = [], DOMAIN_DEFAULT
with open(CFG, encoding="utf-8") as f:
    in_cats = False
    for line in f:
        m = re.match(r'^domain:\s*"?([^"\n]+?)"?\s*$', line)
        if m:
            domain = m.group(1).strip()
        if re.match(r"^categories:\s*$", line):
            in_cats = True
            continue
        if in_cats:
            m = re.match(r"^\s+-\s+(.*\S)\s*$", line)
            if m:
                categories.append(m.group(1).strip().strip('"'))
            elif line.strip() and not line.startswith((" ", "\t")):
                in_cats = False
if not categories:
    die("no `categories:` list found in .pin-llm-wiki.yml")

# --- index slug order ---
with open(INDEX, encoding="utf-8") as f:
    index_text = f.read()
# only slugs from the Sources table rows (lines starting with '| [[')
index_slugs = []
for line in index_text.splitlines():
    m = re.match(r"\|\s*\[\[([^\]]+)\]\]", line)
    if m:
        index_slugs.append(m.group(1))
if not index_slugs:
    die("no source rows found in wiki/index.md")

def resolve_file(slug):
    for cand in (f"{slug}.md", slug):
        p = os.path.join(SRC, cand)
        if os.path.isfile(p):
            return p
    return None

def read_category(path):
    with open(path, encoding="utf-8") as f:
        lines = f.readlines()
    if not lines or lines[0].strip() != "---":
        return None
    for i in range(1, len(lines)):
        if lines[i].strip() == "---":
            break
        m = re.match(r'^category:\s*"?([^"\n]+?)"?\s*$', lines[i])
        if m:
            return m.group(1).strip()
    return None

# --- one-line blurbs from overview.md ---
# Abbreviations that end in a period but do NOT end a sentence.
ABBREV = {"e.g", "i.e", "vs", "etc", "inc", "ltd", "co", "corp", "no", "dr",
          "mr", "ms", "mrs", "st", "cf", "al", "approx", "fig", "vol", "pp", "est"}

def first_sentence(text):
    # First real sentence end: ., ! or ? followed by space + capital/digit/[, where the
    # token before the period is not a known abbreviation or a single-letter initial,
    # and the sentence is already reasonably long.
    cut = None
    for m in re.finditer(r"([A-Za-z][A-Za-z.]*)([.!?])\s+(?=[A-Z0-9\[])", text):
        word = m.group(1).lower().strip(".")
        if word in ABBREV or len(word) <= 1:
            continue
        if m.end(2) < 40:
            continue
        cut = m.end(2)
        break
    s = (text[:cut] if cut else text).replace("\n", " ").strip()
    if len(s) > 200:
        s = s[:197].rstrip() + "…"
    return s

desc = {}
if os.path.isfile(OVERVIEW):
    ov = open(OVERVIEW, encoding="utf-8").read()
    if ov.startswith("---"):
        parts = ov.split("---", 2)
        ov = parts[2] if len(parts) == 3 else ov
    for para in re.split(r"\n\s*\n", ov):
        para = para.strip()
        m = re.match(r"\[\[([^\]]+)\]\]", para)
        if not m:
            continue
        slug = m.group(1)
        if slug in desc:
            continue
        rest = para[m.end():].lstrip()
        desc[slug] = first_sentence(rest)

# --- group ---
groups = defaultdict(list)
unresolved, uncategorized = [], []
known = set(categories)
for slug in index_slugs:
    p = resolve_file(slug)
    if p is None:
        unresolved.append(slug)
        continue
    cat = read_category(p)
    if cat not in known:
        uncategorized.append(slug)
        groups["Uncategorized"].append(slug)
    else:
        groups[cat].append(slug)

if unresolved:
    die(f"could not resolve source file(s) for: {unresolved}")

order = list(categories) + (["Uncategorized"] if groups["Uncategorized"] else [])

today = datetime.date.today().isoformat()
out = ["---", "type: categories", f'domain: "{domain}"', f"updated: {today}", "---", ""]
out += [f"# {domain} — by category", "", "→ [[index]] | [[overview]] | [[log]]", ""]
out += ["> Grouped, human-navigable view of every source. **Generated** — do not hand-edit;",
        "> the source of truth is each page's `category:` frontmatter. Regenerated on every ingest.", ""]
out += ["## Categories", ""]
for name in order:
    out.append(f"- [[#{name}|{name}]] ({len(groups[name])})")
out.append("")
for name in order:
    out.append(f"## {name}")
    out.append("")
    for slug in sorted(groups[name], key=str.lower):
        d = desc.get(slug)
        out.append(f"- [[{slug}]] — {d}" if d else f"- [[{slug}]]")
    out.append("")
out.append(f"_{len(index_slugs)} sources across {len(categories)} categories._")
out.append("")

with open(CATS_MD, "w", encoding="utf-8") as f:
    f.write("\n".join(out))

# --- ensure index.md nav line links to [[categories]] (idempotent, safe: nav line only) ---
nav_added = False
new_index_lines = []
for line in index_text.splitlines(keepends=True):
    stripped = line.strip()
    if stripped.startswith("→ [[") and "[[categories]]" not in stripped and "[[overview]]" in stripped:
        # insert [[categories]] right after [[overview]]
        line = line.replace("[[overview]]", "[[overview]] | [[categories]]", 1)
        nav_added = True
    new_index_lines.append(line)
if nav_added:
    with open(INDEX, "w", encoding="utf-8") as f:
        f.writelines(new_index_lines)

# --- integrity check ---
placed = [s for name in order for s in groups[name]]
assert sorted(placed) == sorted(index_slugs), "internal: slug set mismatch"
assert len(placed) == len(set(placed)), "internal: duplicate slug"

print(f"gen_categories: wrote wiki/categories.md — {len(index_slugs)} sources, "
      f"{len(categories)} categories; integrity OK.")
if uncategorized:
    print(f"gen_categories: WARN {len(uncategorized)} Uncategorized (review): {uncategorized}")
