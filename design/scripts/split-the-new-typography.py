#!/usr/bin/env python3
"""
Split the-new-typography/book.md into individual chapter files.

Chapter boundaries identified by cross-referencing metadata.json TOC with
book.md headings. Line numbers are 1-indexed (as shown by grep -n).
Many headings have OCR spacing artifacts; exact line numbers are used
instead of fragile regex matching.
"""

import json
import re
from pathlib import Path

SOURCE_FILE = Path("sources-md/the-new-typography/book.md")
METADATA_FILE = Path("sources-md/the-new-typography/metadata.json")
OUTPUT_DIR = Path("sources-md/the-new-typography")

# (chapter_number, title, pdf_page, line_1indexed)
# Derived by cross-referencing metadata.json TOC with grep -n output.
CHAPTER_MAP = [
    ( 1, "Translator's Foreword",                          8,   92),
    ( 2, "Revisions to Die Neue Typographie",              10,  118),
    ( 3, "Introduction to the English-Language Edition",   14,  220),
    ( 4, "Jan Tschichold: The New Typography (Title)",     41,  521),
    ( 5, "Introduction",                                   45,  569),
    ( 6, "The New World-View",                             49,  587),
    ( 7, "The Old Typography (1440–1914)",                 53,  625),
    ( 8, "The New Art",                                    68,  755),
    ( 9, "The History of the New Typography",              90,  955),
    (10, "Typographic Revolution and Free-Expression Orthography", 91, 973),
    (11, "Topography of Typography",                       98, 1037),
    (12, "The Principles of the New Typography",          102, 1092),
    (13, "Photography and Typography",                    125, 1384),
    (14, "New Typography and Standardization",            134, 1460),
    (15, "Principal Typographic Categories",              145, 1800),
    (16, "The Typographic Symbol",                        147, 1802),
    (17, "The Business Letterhead",                       150, 1836),
    (18, "The Half Letterhead",                           165, 2044),
    (19, "Envelopes Without Windows",                     169, 2090),
    (20, "Window Envelopes",                              172, 2145),
    (21, "The Postcard",                                  174, 2173),
    (22, "The Postcard with Flap",                        182, 2263),
    (23, "The Business Card",                             186, 2297),
    (24, "The Visiting-Card",                             188, 2326),
    (25, "Advertising Matter",                            189, 2332),
    (26, "The Typo-Poster",                               215, 2654),
    (27, "The Pictorial Poster",                          222, 2752),
    (28, "Labels, Plates, and Frames",                    233, 2818),
    (29, "Advertisements",                                236, 2931),
    (30, "The Periodical",                                243, 3148),
    (31, "The Newspaper",                                 253, 3244),
    (32, "The Illustrated Paper",                         256, 3276),
    (33, "Tabular Matter",                                258, 3302),
    (34, "The New Book",                                  258, 3316),
    (35, "Bibliography",                                  270, 3543),
    (36, "A Note on the Book and Its Design",             275, 3683),
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
    print(f"Chapters in split map:        {len(CHAPTER_MAP)}\n")

    # Verify a sample of chapter boundaries against actual file content
    print("Chapter boundary verification (first heading word check):")
    for num, title, pdf_page, line_1idx in CHAPTER_MAP[:5]:
        actual = lines[line_1idx - 1].rstrip('\n')[:80]
        print(f"  {num:2d}. line {line_1idx:4d}  {repr(actual)}")

    # --- Frontmatter ---
    first_line = CHAPTER_MAP[0][3] - 1  # 0-indexed
    fm_content = ''.join(lines[:first_line])
    fm_path = OUTPUT_DIR / "00-frontmatter.md"
    with open(fm_path, 'w', encoding='utf-8') as f:
        f.write("---\n")
        f.write('title: "Frontmatter"\n')
        f.write("chapter_number: 0\n")
        f.write("pdf_page: 0\n")
        f.write("book_md_line: 1\n")
        f.write("---\n\n")
        f.write(fm_content)
    print(f"\nExtracted frontmatter → {fm_path.name}  ({first_line} lines)")

    # --- Chapter files ---
    created = []
    for i, (num, title, pdf_page, line_1idx) in enumerate(CHAPTER_MAP):
        start = line_1idx - 1  # 0-indexed

        if i + 1 < len(CHAPTER_MAP):
            end = CHAPTER_MAP[i + 1][3] - 1  # 0-indexed
        else:
            end = total_lines

        chapter_content = ''.join(lines[start:end])
        slug = slugify(title)
        filename = f"{num:02d}-{slug}.md"
        filepath = OUTPUT_DIR / filename

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write("---\n")
            f.write(f'title: "{title}"\n')
            f.write(f"chapter_number: {num}\n")
            f.write(f"pdf_page: {pdf_page}\n")
            f.write(f"book_md_line: {line_1idx}\n")
            f.write("---\n\n")
            f.write(chapter_content)

        line_count = end - start
        created.append((filename, pdf_page, line_count))
        print(f"  Ch {num:2d} → {filename}  pdf_page={pdf_page:>3}  ({line_count} lines)")

    # --- Validation ---
    print(f"\n{'='*58}")
    print(f"VALIDATION REPORT")
    print(f"{'='*58}")
    print(f"TOC entries in metadata.json:  {len(toc)}")
    print(f"Chapter files created:         {len(created)}")
    print(f"Frontmatter file:              00-frontmatter.md ✓")

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
