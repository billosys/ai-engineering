#!/usr/bin/env python3
"""
Split art-and-visual-perception/book.md into individual chapter files.

Arnheim, "Art and Visual Perception" (1954).

IMPORTANT STRUCTURAL NOTE:
The PDF conversion produced a book.md with significant duplication.
Chapters IV (Growth) and V (Space) each appear THREE times in the file,
with identical text but different image reference page numbers in each copy.
Two copies of Space also lack sections present in the third copy.

Chapter boundaries are hardcoded using explicit line numbers derived by
cross-referencing metadata.json TOC with grep -n output. Lines 2013-4210
(two duplicate copies of Growth+Space) are intentionally skipped.

Strategy:
- IV Growth: use FIRST occurrence (lines 1532-2012) — most accurate image refs
- V Space:   use LAST occurrence  (lines 4211-5006) — most complete content
- All other chapters: unique (no duplication)
"""

import json
import re
from pathlib import Path

SOURCE_FILE = Path("sources-md/art-and-visual-perception/book.md")
METADATA_FILE = Path("sources-md/art-and-visual-perception/metadata.json")
OUTPUT_DIR = Path("sources-md/art-and-visual-perception")

# (chapter_number, title, pdf_page, start_line_1indexed, end_line_1indexed)
# Lines are 1-indexed (as shown by grep -n).
# end_line is inclusive (last line of this chapter).
# Lines 2013-4210 are duplicate Growth+Space and intentionally excluded.
CHAPTER_MAP = [
    ( 1, "Preface to the New Version",   5,   23,   40),
    ( 2, "Introduction",                  6,   41,  102),
    ( 3, "I. Balance",                   11,  103,  429),
    ( 4, "II. Shape",                    31,  430,  971),
    ( 5, "III. Form",                    65,  972, 1531),
    ( 6, "IV. Growth",                  108, 1532, 2012),  # first of 3 occurrences
    ( 7, "V. Space",                    141, 4211, 5006),  # last/complete occurrence
    ( 8, "VI. Light",                   356, 5007, 5235),
    ( 9, "VII. Color",                  371, 5236, 5629),
    (10, "VIII. Movement",              395, 5630, 5961),
    (11, "IX. Dynamics",                416, 5962, 6290),
    (12, "X. Expression",               437, 6291, 6426),
    (13, "Notes",                       448, 6427, 7765),
    (14, "Bibliography",                466, 7766, 8266),
]


def slugify(text):
    text = text.lower()
    text = re.sub(r'[^\w\s-]', '', text)
    text = re.sub(r'[-\s]+', '-', text)
    text = text.strip('-')
    return text[:50].rstrip('-')


def main():
    print(f"Reading {SOURCE_FILE}...")
    with open(SOURCE_FILE, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    total_lines = len(lines)
    print(f"Total lines: {total_lines}")

    with open(METADATA_FILE, 'r', encoding='utf-8') as f:
        metadata = json.load(f)
    toc = metadata.get('table_of_contents', [])
    print(f"TOC entries in metadata.json: {len(toc)}")
    print(f"Chapters in split map:        {len(CHAPTER_MAP)}")
    print()

    print("NOTE: Lines 2013-4210 are duplicate Growth+Space sections and will be skipped.")
    print()

    # Verify chapter boundaries
    print("Chapter boundary verification (first heading word check):")
    for num, title, pdf_page, start, end in CHAPTER_MAP[:6]:
        actual = lines[start - 1].rstrip('\n')[:80]
        print(f"  Ch {num:2d}: line {start:4d}  {repr(actual)}")

    # --- Frontmatter ---
    first_chapter_start = CHAPTER_MAP[0][3] - 1  # 0-indexed
    fm_content = ''.join(lines[:first_chapter_start])
    fm_path = OUTPUT_DIR / "00-frontmatter.md"
    with open(fm_path, 'w', encoding='utf-8') as f:
        f.write("---\n")
        f.write('title: "Frontmatter"\n')
        f.write("chapter_number: 0\n")
        f.write("pdf_page: 1\n")
        f.write("book_md_line: 1\n")
        f.write("---\n\n")
        f.write(fm_content)
    print(f"\nExtracted frontmatter → 00-frontmatter.md  ({first_chapter_start} lines)")

    # --- Chapter files ---
    created = []
    for num, title, pdf_page, start_1idx, end_1idx in CHAPTER_MAP:
        start = start_1idx - 1   # 0-indexed
        end = end_1idx           # 0-indexed exclusive (= end_1idx since end_1idx is inclusive 1-indexed)

        chapter_content = ''.join(lines[start:end])
        slug = slugify(title)
        filename = f"{num:02d}-{slug}.md"
        filepath = OUTPUT_DIR / filename

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write("---\n")
            f.write(f'title: "{title}"\n')
            f.write(f"chapter_number: {num}\n")
            f.write(f"pdf_page: {pdf_page}\n")
            f.write(f"book_md_line: {start_1idx}\n")
            f.write("---\n\n")
            f.write(chapter_content)

        line_count = end - start
        created.append((filename, pdf_page, line_count))
        print(f"  Ch {num:2d} → {filename}  pdf_page={pdf_page:>3}  ({line_count} lines)")

    # --- Validation ---
    print(f"\n{'='*60}")
    print(f"VALIDATION REPORT")
    print(f"{'='*60}")
    print(f"TOC entries in metadata.json:  {len(toc)}")
    print(f"Chapter files created:         {len(created)}")
    print(f"Frontmatter file:              00-frontmatter.md ✓")
    print(f"Duplicate sections skipped:    lines 2013-4210 (Growth×2 + Space×2)")

    lines_covered = sum(end - (start - 1) for _, _, _, start, end in CHAPTER_MAP)
    lines_covered += first_chapter_start  # frontmatter
    skipped = (4210 - 2013 + 1)
    print(f"Total book lines:              {total_lines}")
    print(f"Lines in chapter files:        {lines_covered}")
    print(f"Lines skipped (duplicates):    {skipped}")
    print(f"Lines accounted for:           {lines_covered + skipped}")

    # Sample first chapter
    first_ch_path = OUTPUT_DIR / created[0][0]
    print(f"\nSample — first 25 lines of {created[0][0]}:")
    with open(first_ch_path, 'r', encoding='utf-8') as f:
        sample = f.readlines()
    for l in sample[:25]:
        print("  " + l, end='')

    print(f"\n\nSource is ready for concept extraction or full-text indexing.")


if __name__ == "__main__":
    main()
