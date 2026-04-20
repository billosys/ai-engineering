#!/usr/bin/env python3
"""
Split munsell-colour-system/book.md into individual chapter files
using the metadata.json TOC for PDF page numbers.
"""

import json
import re
from pathlib import Path

SOURCE_FILE = Path("sources-md/munsell-colour-system/book.md")
METADATA_FILE = Path("sources-md/munsell-colour-system/metadata.json")
OUTPUT_DIR = Path("sources-md/munsell-colour-system")

# Chapter mapping: heading pattern → (chapter_number, toc_title, pdf_page)
# Derived by cross-referencing metadata.json TOC with book.md headings.
CHAPTER_MAP = [
    # (regex to match heading line, chapter_number, title, pdf_page)
    (r'### \*\*FOREWORD\*\*',            1,  "FOREWORD",                          2),
    (r"#### EDITOR'S NOTE",              2,  "EDITOR'S NOTE",                     3),
    (r'#### By T\. M\. CLELAND',         3,  "By T. M. Cleland",                  4),
    (r'#### I\. HUE',                    4,  "I. Hue",                            4),
    (r'#### II\. VALUE',                 5,  "II. Value",                         6),
    (r'#### III\. CHROMA',               6,  "III. Chroma",                       7),
    (r'#### OPPOSITE OR COMPLEMENTARY',  7,  "Opposite or Complementary Colors",  10),
    (r'#### BALANCE',                    8,  "Balance",                           11),
    (r'#### COLOR COMBINATIONS',         9,  "Color Combinations",                15),
    (r'#### APPENDIX',                  10,  "Appendix",                          18),
    (r'#### SUMMARY',                   11,  "Summary",                           18),
]


def slugify(text):
    """Convert text to filename-safe slug (max 50 chars)."""
    text = text.lower()
    text = re.sub(r'[^\w\s-]', '', text)
    text = re.sub(r'[-\s]+', '-', text)
    text = text.strip('-')
    return text[:50].rstrip('-')


def find_chapter_starts(lines):
    """Return list of (line_index, chapter_info) matching CHAPTER_MAP."""
    results = []
    for i, line in enumerate(lines):
        stripped = line.rstrip('\n')
        for pattern, num, title, pdf_page in CHAPTER_MAP:
            if re.match(pattern, stripped):
                results.append((i, num, title, pdf_page))
                break
    return results


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

    # Find chapter boundaries
    chapters = find_chapter_starts(lines)
    print(f"\nChapter mapping (heading → PDF page → line):")
    for line_idx, num, title, pdf_page in chapters:
        print(f"  {num:2d}. line {line_idx+1:4d}  pdf_page={pdf_page:2d}  {title}")

    if not chapters:
        print("ERROR: No chapters found. Check heading patterns.")
        return

    # --- Frontmatter ---
    frontmatter_end = chapters[0][0]
    frontmatter_content = ''.join(lines[:frontmatter_end])
    fm_path = OUTPUT_DIR / "00-frontmatter.md"
    with open(fm_path, 'w', encoding='utf-8') as f:
        f.write("---\n")
        f.write('title: "Frontmatter"\n')
        f.write("chapter_number: 0\n")
        f.write("pdf_page: 0\n")
        f.write("book_md_line: 1\n")
        f.write("---\n\n")
        f.write(frontmatter_content)
    print(f"\nExtracted frontmatter → {fm_path.name}  ({frontmatter_end} lines)")

    # --- Chapter files ---
    created = []
    for i, (line_idx, num, title, pdf_page) in enumerate(chapters):
        # End is next chapter start or EOF
        if i + 1 < len(chapters):
            end_idx = chapters[i + 1][0]
        else:
            end_idx = total_lines

        chapter_content = ''.join(lines[line_idx:end_idx])
        slug = slugify(title)
        filename = f"{num:02d}-{slug}.md"
        filepath = OUTPUT_DIR / filename

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write("---\n")
            f.write(f'title: "{title}"\n')
            f.write(f"chapter_number: {num}\n")
            f.write(f"pdf_page: {pdf_page}\n")
            f.write(f"book_md_line: {line_idx + 1}\n")
            f.write("---\n\n")
            f.write(chapter_content)

        line_count = end_idx - line_idx
        created.append((filename, pdf_page, line_count))
        print(f"  Chapter {num:2d} → {filename}  pdf_page={pdf_page}  ({line_count} lines)")

    # --- Validation report ---
    print(f"\n{'='*55}")
    print(f"VALIDATION REPORT")
    print(f"{'='*55}")
    print(f"TOC entries in metadata.json:  {len(toc)}")
    print(f"Chapter files created:         {len(created)}")
    print(f"Frontmatter file:              00-frontmatter.md")

    # Show first 25 lines of first chapter
    first_chapter_path = OUTPUT_DIR / created[0][0]
    print(f"\nSample — first 25 lines of {created[0][0]}:")
    with open(first_chapter_path, 'r', encoding='utf-8') as f:
        sample_lines = f.readlines()
    for l in sample_lines[:25]:
        print("  " + l, end='')

    print(f"\n\nSource is ready for concept extraction or full-text indexing.")


if __name__ == "__main__":
    main()
