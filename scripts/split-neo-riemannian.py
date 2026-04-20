#!/usr/bin/env python3
"""
Split the Neo-Riemannian Handbook into individual chapter files.

Reference implementation for the PDF-prep prompt
(docs/dev/concept-cards/0005-prompt-prepare-pdf-converted-source-for-indexing-v2.md).

Implements the "Step 3: Split Book into Chapters" workflow:
  - Reads `metadata.json` (Marker TOC) for per-chapter PDF page numbers
    (optional — the script gracefully degrades if metadata.json is absent or
    has no useful TOC; `pdf_page` is set to `null` in that case).
  - Reads `book.md` and locates chapter boundaries.
  - Extracts pre-chapter content to `00-frontmatter.md`.
  - Writes one YAML-frontmatter-tagged file per chapter **directly into the
    source md directory** (no `chapters/` subdirectory).

Handbook-specific note: this book (Oxford Handbook of Neo-Riemannian Music
Theories) uses `## **Abstract and Keywords**` as its reliable chapter marker,
because each contributed chapter opens with an abstract. When adapting this
script for a different source, replace `find_chapter_boundaries` with the
appropriate detection — usually a regex on `# N Title` or a lookup derived
from `metadata.json`'s `table_of_contents` array.

Run from the project root:

    python3 scripts/split-neo-riemannian.py
"""

import json
import re
from pathlib import Path

# Paths — relative to the project root (run this script from there).
SOURCE_DIR = Path("knowledge/music-theory/sources/md/neo-riemannian-handbook")
SOURCE_FILE = SOURCE_DIR / "book.md"
METADATA_FILE = SOURCE_DIR / "metadata.json"
# Chapter files are written directly into SOURCE_DIR (no `chapters/` subdirectory).
OUTPUT_DIR = SOURCE_DIR

SOURCE_FORMAT = "pdf"
MAX_SLUG_LEN = 50


# ---------------------------------------------------------------------------
# Chapter detection (handbook-specific — replace when cloning for a new source)
# ---------------------------------------------------------------------------

def extract_author_before_abstract(lines, abstract_line_num):
    """Extract author name from the lines before Abstract and Keywords."""
    # Look backwards from abstract for author name.
    #   Pattern 1: `#### **Name**` (bolded with heading)
    #   Pattern 2: Plain text name above "The Oxford Handbook" line
    for i in range(abstract_line_num - 1, max(0, abstract_line_num - 20), -1):
        line = lines[i].strip()

        # Pattern 1: #### **Name**
        match = re.match(r'^####\s+\*\*(.+?)\*\*\s*$', line)
        if match:
            return match.group(1).strip()

        # Pattern 2: Plain text name (not empty, not a heading, not "The Oxford")
        if line and not line.startswith('#') and not line.startswith('The Oxford'):
            for j in range(i + 1, min(len(lines), i + 10)):
                if 'The Oxford Handbook' in lines[j]:
                    author = line.strip()
                    ignore_patterns = [
                        'Print Publication', 'Subject:', 'Online Publication', 'DOI:', '**',
                        ' is ', ' teaches ', ' holds ', ' are ', ' was ', ' were ',
                    ]
                    if len(author) < 60 and not any(x in author for x in ignore_patterns):
                        return author
                    break
    return None


def extract_title_after_abstract(lines, abstract_start):
    """Extract chapter title from the lines after Abstract and Keywords."""
    for i in range(abstract_start + 1, min(len(lines), abstract_start + 30)):
        line = lines[i].strip()
        if not line or line.startswith("Keywords:") or line.startswith("**Keywords"):
            continue
        if line.startswith("##"):
            title = re.sub(r'^#+\s*\*?\*?', '', line)
            title = re.sub(r'\*?\*?\s*$', '', title)
            return title[:80]
    return None


def find_chapter_start_line(lines, abstract_line_num):
    """Walk back from an 'Abstract and Keywords' marker to the true chapter start.

    In this handbook each chapter opens with a `#### **Author Name**` heading a
    few lines before its abstract. If we split on the Abstract line itself, the
    author heading + publication metadata for the *next* chapter ends up tacked
    onto the *previous* chapter's file. So we rewind to the nearest `#### ...`
    heading (within a reasonable look-back window) and use that as the real
    chapter start.
    """
    for i in range(abstract_line_num - 1, max(-1, abstract_line_num - 25), -1):
        stripped = lines[i].strip()
        if stripped.startswith('#### '):
            return i
    return abstract_line_num


def find_chapter_boundaries(lines):
    """Find all chapter start positions. Anchored on 'Abstract and Keywords'."""
    chapters = []
    for i, line in enumerate(lines):
        if line.strip() == "## **Abstract and Keywords**":
            chapters.append({
                'start_line': find_chapter_start_line(lines, i),
                'abstract_line': i,
                'author': extract_author_before_abstract(lines, i) or "Unknown",
                'title': extract_title_after_abstract(lines, i) or "Untitled",
            })
    return chapters


# ---------------------------------------------------------------------------
# metadata.json TOC cross-reference (optional — produces pdf_page per chapter)
# ---------------------------------------------------------------------------

def load_metadata_toc():
    """Return a list of (title, page_id) from metadata.json, or [] if unavailable."""
    if not METADATA_FILE.exists():
        return []
    try:
        with open(METADATA_FILE, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except (json.JSONDecodeError, OSError) as e:
        print(f"  (metadata.json present but unreadable: {e}; skipping TOC cross-reference)")
        return []
    toc = data.get('table_of_contents') or []
    return [(entry.get('title', ''), entry.get('page_id')) for entry in toc]


def match_chapter_to_toc(chapter, toc_entries):
    """Best-effort match of a chapter's title/author to a TOC entry; return pdf_page or None."""
    needles = [chapter.get('title') or '', chapter.get('author') or '']
    needles = [n for n in needles if n and n not in ('Untitled', 'Unknown')]
    if not needles:
        return None
    for title, page_id in toc_entries:
        if not title:
            continue
        title_lower = title.lower()
        for needle in needles:
            needle_lower = needle.lower()
            if needle_lower in title_lower or title_lower in needle_lower:
                return page_id
    return None


# ---------------------------------------------------------------------------
# Slug + YAML frontmatter helpers
# ---------------------------------------------------------------------------

def slugify(text):
    """Filename-safe slug (lowercase, hyphenated, ASCII-only, <= MAX_SLUG_LEN chars)."""
    text = text.lower()
    text = re.sub(r'[^\w\s-]', '', text)
    text = re.sub(r'[-\s]+', '-', text)
    text = text.strip('-')
    return text[:MAX_SLUG_LEN].rstrip('-')


def yaml_scalar(value):
    """Render a Python value as a YAML scalar. Quotes strings that contain reserved chars."""
    if value is None:
        return "null"
    if isinstance(value, bool):
        return "true" if value else "false"
    if isinstance(value, int):
        return str(value)
    s = str(value)
    # Quote if the value contains YAML-reserved chars, starts with a reserved
    # leading char, or is empty.
    reserved = set(':#{}[],&*!|>%@`"\'')
    leading_reserved = set('-?:[]{}!&*|>%@`"\'')
    needs_quoting = (
        not s
        or any(c in reserved for c in s)
        or (s and s[0] in leading_reserved)
    )
    if needs_quoting:
        escaped = s.replace('\\', '\\\\').replace('"', '\\"')
        return f'"{escaped}"'
    return s


def write_chapter_file(filepath, meta, content):
    """Write `content` prefixed by a YAML frontmatter block built from `meta`."""
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write("---\n")
        for key, value in meta.items():
            f.write(f"{key}: {yaml_scalar(value)}\n")
        f.write("---\n\n")
        f.write(content)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def split_into_chapters():
    print(f"Reading {SOURCE_FILE}...")
    with open(SOURCE_FILE, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    total_lines = len(lines)
    print(f"Total lines: {total_lines}")

    toc_entries = load_metadata_toc()
    if toc_entries:
        print(f"Loaded {len(toc_entries)} TOC entries from metadata.json")
    else:
        print("No metadata.json TOC available - pdf_page will be null for all chapters")

    chapters = find_chapter_boundaries(lines)
    print(f"\nFound {len(chapters)} chapters:")
    for i, chapter in enumerate(chapters):
        print(f"  {i+1:2d}. Line {chapter['start_line']:5d} - {chapter['author']}")

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    # Extract frontmatter (everything before the first chapter)
    if chapters:
        frontmatter_end = chapters[0]['start_line']
        frontmatter_content = ''.join(lines[:frontmatter_end])
        frontmatter_file = OUTPUT_DIR / "00-frontmatter.md"
        write_chapter_file(
            frontmatter_file,
            {
                "title": "Book Frontmatter",
                "chapter_number": 0,
                "pdf_page": None,
                "book_md_line": 0,
                "source_format": SOURCE_FORMAT,
            },
            frontmatter_content,
        )
        print(f"\nExtracted frontmatter to {frontmatter_file}")

    # Extract each chapter
    for i, chapter in enumerate(chapters):
        chapter_num = i + 1
        start = chapter['start_line']
        end = chapters[i + 1]['start_line'] if i + 1 < len(chapters) else total_lines

        chapter_content = ''.join(lines[start:end])

        # Filename slug: per v2 spec, derive from the chapter title; fall back to
        # the author slug if title extraction didn't recover a real title.
        if chapter['title'] and chapter['title'] != 'Untitled':
            base_slug = slugify(chapter['title'])
        else:
            base_slug = slugify(chapter['author'])
        if not base_slug:
            base_slug = f"chapter-{chapter_num}"

        filename = f"{chapter_num:02d}-{base_slug}.md"
        filepath = OUTPUT_DIR / filename

        pdf_page = match_chapter_to_toc(chapter, toc_entries)

        # Metadata header: v2 spec fields (title / chapter_number / pdf_page /
        # book_md_line / source_format) plus `author`, preserved from the
        # handbook-specific detection for downstream concept extraction.
        write_chapter_file(
            filepath,
            {
                "title": chapter['title'],
                "chapter_number": chapter_num,
                "author": chapter['author'],
                "pdf_page": pdf_page,
                "book_md_line": start,
                "source_format": SOURCE_FORMAT,
            },
            chapter_content,
        )

        page_str = f"page {pdf_page}" if pdf_page is not None else "page ?"
        print(f"  Chapter {chapter_num:2d} -> {filename} ({end - start} lines, {page_str})")

    print(f"\nSplit complete: {len(chapters)} chapters + frontmatter written to {OUTPUT_DIR}/")
    print(f"\nNote: image references still point to the source directory.")
    print(f"      Images remain in: {SOURCE_DIR}/images/")


if __name__ == "__main__":
    split_into_chapters()
