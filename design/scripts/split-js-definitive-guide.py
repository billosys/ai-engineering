#!/usr/bin/env python3
"""Split js-definitive-guide book.md into individual chapter files."""

import json
import re
import unicodedata

BOOK_PATH = "sources-md/js-definitive-guide/book.md"
META_PATH = "sources-md/js-definitive-guide/metadata.json"
OUTPUT_DIR = "sources-md/js-definitive-guide"


def slugify(text, max_len=50):
    """Convert title text to a filename-safe slug."""
    text = re.sub(r'\*+', '', text)  # remove bold/italic markers
    text = re.sub(r'<[^>]+>', '', text)  # remove HTML tags
    text = text.lower()
    text = unicodedata.normalize('NFKD', text).encode('ascii', 'ignore').decode('ascii')
    text = re.sub(r'[^a-z0-9\s-]', '', text)
    text = re.sub(r'[\s]+', '-', text).strip('-')
    text = re.sub(r'-+', '-', text)
    return text[:max_len].rstrip('-')


# Read metadata for PDF page numbers
with open(META_PATH, "r") as f:
    metadata = json.load(f)

toc = metadata.get("table_of_contents", [])

# Build a lookup of title -> pdf page from TOC
toc_pages = {}
for entry in toc:
    title = entry.get("title", "").replace("\n", " ").strip()
    page = entry.get("page_id", 0)
    # Normalize for matching
    key = re.sub(r'\s+', ' ', title).strip().lower()
    if key not in toc_pages:
        toc_pages[key] = page

# Read book
with open(BOOK_PATH, "r") as f:
    lines = f.readlines()

# Define chapter structure manually based on analysis
# Format: (chapter_number, title, pdf_page, heading_pattern)
# chapter_number=0 means preface, None means frontmatter/backmatter
chapters_def = [
    (None, "Preface", 14, "Preface"),
    (1, "Introduction to JavaScript", 18, "Introduction to JavaScript"),
    (2, "Lexical Structure", 32, "Lexical Structure"),
    (3, "Types, Values, and Variables", 40, "Types, Values, and Variables"),
    (4, "Expressions and Operators", 78, "Expressions and Operators"),
    (5, "Statements", 114, "Statements"),
    (6, "Objects", 146, "Objects"),
    (7, "Arrays", 172, "Arrays"),
    (8, "Functions", 198, "Functions"),
    (9, "Classes", 238, "Classes"),
    (10, "Modules", 266, "Modules"),
    (11, "The JavaScript Standard Library", 284, "The JavaScript Standard Library"),
    (12, "Iterators and Generators", 344, "Iterators and Generators"),
    (13, "Asynchronous JavaScript", 358, "Asynchronous JavaScript"),
    (14, "Metaprogramming", 396, "Metaprogramming"),
    (15, "JavaScript in Web Browsers", 426, "JavaScript in Web Browsers"),
    (16, "Server-Side JavaScript with Node", 594, "Server-Side JavaScript with Node"),
    (17, "JavaScript Tools and Extensions", 652, "JavaScript Tools and Extensions"),
    (None, "Index", None, "Index"),
]

# Find line numbers for each chapter heading in book.md
# Chapters use ## headings with optional bold/span formatting
chapter_lines = []
for ch_num, title, pdf_page, pattern in chapters_def:
    # Search for the heading line
    found_line = None
    # Escape special regex chars in pattern
    escaped = re.escape(pattern)
    # Build regex that matches ## with optional bold/span formatting
    # Spans may appear as self-closing anchors before the title
    heading_re = re.compile(
        r'^##\s+(?:<span[^>]*></span>\s*)?(?:\*\*)?'
        + escaped
        + r'(?:\*\*)?(?:\s*</span>)?\s*$'
    )
    for i, line in enumerate(lines):
        if heading_re.match(line.strip()):
            # For chapters that appear multiple times (like "Modules"),
            # find the one that's a standalone chapter heading (not a subsection)
            # by checking it doesn't have a number prefix like "10.3"
            # and comes after the previous chapter
            min_line = chapter_lines[-1]['line_idx'] if chapter_lines else 0
            if i > min_line:
                found_line = i
                break

    if found_line is not None:
        chapter_lines.append({
            'number': ch_num,
            'title': title,
            'pdf_page': pdf_page,
            'line': found_line + 1,  # 1-indexed
            'line_idx': found_line,  # 0-indexed
        })
    else:
        print(f"WARNING: Could not find heading for '{title}'")

print(f"Detected {len(chapter_lines)} sections\n")

# Extract frontmatter (everything before first detected section)
frontmatter_end = chapter_lines[0]['line_idx']
frontmatter_lines = lines[:frontmatter_end]

fm_path = f"{OUTPUT_DIR}/00-frontmatter.md"
with open(fm_path, "w") as f:
    f.write("---\n")
    f.write("title: Frontmatter\n")
    f.write("pdf_page: 0\n")
    f.write("book_md_line: 1\n")
    f.write("---\n\n")
    f.writelines(frontmatter_lines)

fm_count = len(frontmatter_lines)
print(f"  00-frontmatter.md (pdf page 0, {fm_count} lines)")

# Extract each chapter/section
for idx, ch in enumerate(chapter_lines):
    start = ch['line_idx']
    end = chapter_lines[idx + 1]['line_idx'] if idx + 1 < len(chapter_lines) else len(lines)
    chapter_content = lines[start:end]

    slug = slugify(ch['title'])

    if ch['number'] is not None:
        filename = f"{ch['number']:02d}-{slug}.md"
    elif ch['title'] == "Preface":
        filename = "00-preface.md"
    elif ch['title'] == "Index":
        filename = "18-index.md"
    else:
        filename = f"00-{slug}.md"

    filepath = f"{OUTPUT_DIR}/{filename}"

    with open(filepath, "w") as f:
        f.write("---\n")
        f.write(f'title: "{ch["title"]}"\n')
        if ch['number'] is not None:
            f.write(f"chapter_number: {ch['number']}\n")
        if ch['pdf_page'] is not None:
            f.write(f"pdf_page: {ch['pdf_page']}\n")
        f.write(f"book_md_line: {ch['line']}\n")
        f.write("---\n\n")
        f.writelines(chapter_content)

    line_count = len(chapter_content)
    page_str = f"pdf page {ch['pdf_page']}" if ch['pdf_page'] is not None else "no pdf page"
    print(f"  {filename} ({page_str}, {line_count} lines)")

print(f"\nTotal: 1 frontmatter + {len(chapter_lines)} section files = {len(chapter_lines) + 1} files created")
