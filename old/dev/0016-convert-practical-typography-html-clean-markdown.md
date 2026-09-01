# Convert *Practical Typography* HTML → Clean Markdown

## Context

We have downloaded the complete HTML source of *Butterick's Practical Typography* into `./sources-html/practical-typography/`. These are raw HTML pages from the live website, including site navigation chrome, font-selection toolbars, and chapter navigation links. We need clean Markdown versions suitable for automated knowledge extraction (concept card generation via LLM).

**Goal:** Convert every `.html` file in `./sources-html/practical-typography/` to a corresponding `.md` file in `./sources-md/practical-typography/`, stripping all site chrome and preserving only the book's actual content with its structural formatting intact.

---

## The HTML structure you'll encounter

Butterick's site is built with [Pollen](https://pollenpub.com/) (his custom publishing system in Racket). The HTML is clean and semantic, but each page includes navigation chrome that must be stripped. Here's the consistent pattern across all pages:

### Content you MUST KEEP

- The page title / `<h1>` heading (usually near the top of the body content)
- All body text paragraphs
- The "key rule" summary line that appears near the top of many pages (e.g., "line spacing — 120–145% of the point size") — this is valuable content
- Inline emphasis (`<em>`, `<i>`, `<strong>`, `<b>`)
- Internal cross-reference links (e.g., `[point size](point-size.html)`) — convert these to relative `.md` links
- External links (e.g., to StackOverflow) — preserve as-is
- Code snippets (e.g., CSS property references like `line-height`, `1.3`)
- Lists (bulleted and numbered)
- "by the way" sections — these contain substantive content (tips, caveats)
- "How to set..." instructional sections with per-application guidance (Word, Pages, CSS)
- Block quotations
- Tables

### Navigation chrome you MUST STRIP

Every page ends with a consistent block of navigation chrome. Remove ALL of the following:

1. **Font-selection toolbar** — the block containing:

   ```
   undock
   move
   Heliotrope
   Equity
   Valkyrie
   Century Supra
   Concourse
   Triplicate
   buy font
   close
   ```

2. **Chapter navigation links** — the prev/next/chapter links at the bottom:

   ```
   [← previous page title](previous-page.html)
   [top](/)
   [chapter](section-landing.html)
   [next page title →](next-page.html)
   ```

   These use `←` and `→` arrows and always include `[top](/)`.
3. **Page title in the `<title>` tag duplicate** — the text `"Page Title | Butterick's Practical Typography"` that may appear as a rendered text node at the very top before the actual content heading.
4. **"Reader-supported & ad-free since 2013"** link/text if present.
5. **Mailing list signup block** if present.
6. **The "Also by Matthew Butterick" section** if present (only on index page).
7. **Any `<script>` or `<style>` tags** and their contents.
8. **Image references** (`<img>` tags) — since we didn't download images, these would be broken references. Strip them. If an image has meaningful `alt` text, preserve it as `[Image: {alt text}]`.

### Special content patterns to handle correctly

**Soft hyphens (­ / `&shy;`).** Butterick's site uses extensive soft hyphenation for typographic control (e.g., `ty­pog­ra­phy` → `ty-pog-ra-phy`). These are `&shy;` / `\u00AD` characters. **REMOVE ALL SOFT HYPHENS.** They serve no purpose in Markdown and will corrupt text search and knowledge extraction. `ty­pog­ra­phy` should become `typography`.

**Non-breaking spaces and special whitespace.** Preserve `&nbsp;` where it separates units or symbols. Convert other special whitespace to regular spaces.

**Typographic characters.** PRESERVE all curly quotes (" " ' '), em dashes (—), en dashes (–), ellipses (…), and other Unicode punctuation. These are intentional typographic choices by the author and are part of the content.

**Per-application instruction blocks.** Many pages have sections like:

```
Word — [instructions]
Pages — [instructions]
CSS — [instructions]
```

Preserve these as sub-sections or labeled paragraphs. They contain valuable practical guidance.

---

## Conversion pipeline

### Step 1: Install dependencies

```bash
# Pandoc is the primary conversion engine
sudo apt-get install -y pandoc

# Python for pre/post-processing
pip install beautifulsoup4 --break-system-packages
```

### Step 2: Write a Python conversion script

Create a script `convert_pt_html_to_md.py` that processes each file through a three-stage pipeline:

#### Stage A — HTML pre-processing (BeautifulSoup)

Before passing to Pandoc, clean the HTML:

1. Parse with BeautifulSoup (`html.parser`).
2. Remove `<script>` and `<style>` tags.
3. Remove `<img>` tags (optionally preserving alt text as noted above).
4. **Identify and remove the navigation chrome.** The font toolbar and chapter nav links appear at the end of the body. Strategy:
   - Look for the text "undock" followed by "move" — this signals the start of the font toolbar. Remove everything from that point to the end of the body.
   - Alternatively, look for links matching the pattern `[← ...]` and `[top](/)` and `[... →]` and remove those elements.
   - The font toolbar text ("Heliotrope", "Equity", "Valkyrie", "Century Supra", "Concourse", "Triplicate", "buy font", "close") can be used as markers.
5. Remove the duplicate page title if it appears as bare text before the `<h1>`.
6. Remove any "Reader-supported & ad-free" text.
7. **Remove soft hyphens**: do a global string replace of `\u00AD` and `&shy;` with empty string on the final HTML before passing to Pandoc.
8. Extract the cleaned `<body>` content (or the main content container if there's a wrapper `<div>`).

#### Stage B — Pandoc conversion

```bash
pandoc --from=html --to=gfm --wrap=none --strip-comments -o output.md input_cleaned.html
```

Flags explained:

- `--from=html` — input format
- `--to=gfm` — GitHub-Flavored Markdown (fenced code blocks, tables, strikethrough)
- `--wrap=none` — **critical**: prevents Pandoc from hard-wrapping lines at 72 characters
- `--strip-comments` — removes HTML comments

#### Stage C — Markdown post-processing (Python)

After Pandoc conversion, clean up the Markdown:

1. **Remove any remaining soft hyphens** that survived the HTML stage.
2. **Clean up excessive blank lines.** Pandoc sometimes produces 3+ consecutive blank lines. Collapse to a maximum of 2.
3. **Fix internal links.** Convert `.html` extensions to `.md` in internal links:
   - `[point size](point-size.html)` → `[point size](point-size.md)`
4. **Remove any remaining navigation artifacts.** Scan for lines that are just `undock`, `move`, `close`, `buy font`, `top`, or arrow-prefixed navigation links (e.g., lines starting with `←` or ending with `→` that link to other chapters). Remove these lines.
5. **Add YAML front matter** to each file:

   ```yaml
   ---
   title: "Line Spacing"
   source: "Butterick's Practical Typography"
   author: "Matthew Butterick"
   url: "https://practicaltypography.com/line-spacing.html"
   ---
   ```

   Extract the title from the first `#` heading in the Markdown. Derive the URL from the original filename.
6. **Verify the output is not empty or trivially short.** If a converted file has fewer than 50 characters of content (excluding front matter), flag it as suspicious.

### Step 3: Batch process all files

```python
import os
import glob

html_dir = "./sources-html/practical-typography"
md_dir = "./sources-md/practical-typography"
os.makedirs(md_dir, exist_ok=True)

html_files = sorted(glob.glob(os.path.join(html_dir, "*.html")))
for html_file in html_files:
    slug = os.path.splitext(os.path.basename(html_file))[0]
    md_file = os.path.join(md_dir, f"{slug}.md")
    convert(html_file, md_file)  # Your conversion function
```

### Step 4: Verification

After converting all files, generate a report:

1. **Count comparison**: number of `.html` inputs vs. `.md` outputs — should match exactly.
2. **Size check**: flag any `.md` file smaller than 200 bytes (likely failed conversion or empty page).
3. **Soft hyphen audit**: run `grep -rn $'\u00AD' ./sources-md/practical-typography/` to confirm ZERO soft hyphens remain. This is a **hard requirement** — any remaining soft hyphens will break text matching during knowledge extraction.
4. **Chrome residue check**: run `grep -rn "undock\|buy font\|Heliotrope\|Valkyrie\|Century Supra" ./sources-md/practical-typography/` to confirm no font toolbar text leaked through.
5. **Navigation residue check**: run `grep -rn "^\[← \|^\[top\](/\)\|→\]$" ./sources-md/practical-typography/` to confirm no chapter navigation links remain.
6. **Link integrity**: count total internal `.md` links and verify each target file exists.
7. **Sample spot-check**: print the first 20 lines of 3 randomly selected `.md` files so you can visually confirm quality.

Save the report as `./sources-md/practical-typography/_conversion-report.txt`.

---

## Output structure

```
./sources-md/practical-typography/
├── index.md
├── typography-in-ten-minutes.md
├── summary-of-key-rules.md
├── introduction.md
├── ...
├── typography-2024.md
├── mb-lectures-and-articles.md
└── _conversion-report.txt
```

Each `.md` file should look like this (example):

```markdown
---
title: "Line Spacing"
source: "Butterick's Practical Typography"
author: "Matthew Butterick"
url: "https://practicaltypography.com/line-spacing.html"
---

# Line spacing — 120–145% of the point size

Line spacing is the vertical distance between lines of text. Most writers use either
double-spaced lines or single-spaced lines—nothing in between—because those are the
options presented by word processors.

These habits are obsolete [typewriter habits](typewriter-habits.md). Originally, a
typewriter's platen could only move the paper vertically in units of a single line...

## How to set line spacing

**Word** — Right-click in the text and select Paragraph from the menu...

**Pages** — View → Show Toolbar...

**CSS** — Use the `line-height` property, preferably without units...

## By the way

- Recall that different fonts set at the same point size may not appear the same size
  on the page. (See [point size](point-size.md) for why.)...
```

---

## Critical safeguards

1. **ZERO soft hyphens in output.** This is the single most important quality gate. Soft hyphens will silently corrupt search, matching, and extraction. Test aggressively.
2. **Do NOT modify the author's words.** Strip chrome and formatting artifacts only. Never rewrite, summarize, or rephrase content.
3. **Do NOT strip "by the way" sections.** These look like asides but contain critical practical tips.
4. **Do NOT strip per-application instructions** (Word, Pages, CSS blocks). These are valuable implementation guidance.
5. **Do NOT convert internal links to absolute URLs.** Keep them as relative `[text](slug.md)` links for portability.
6. **Do NOT add any content** that isn't in the original HTML. The YAML front matter is the only addition.
7. **Preserve the index page** — convert it too, even though it's mostly a table of contents. It provides structural context.
8. **Handle encoding correctly.** Read HTML as UTF-8, write Markdown as UTF-8 with no BOM.

---

## Success criteria

- [ ] Every `.html` file has a corresponding `.md` file
- [ ] `grep -rP '\xC2\xAD' ./sources-md/practical-typography/` returns ZERO matches (no soft hyphens)
- [ ] No font toolbar text in any `.md` file
- [ ] No chapter navigation links in any `.md` file
- [ ] All `.md` files have YAML front matter with title, source, author, and url
- [ ] All internal links point to `.md` files (not `.html`)
- [ ] No `.md` file is smaller than 200 bytes
- [ ] `_conversion-report.txt` shows all checks passing
