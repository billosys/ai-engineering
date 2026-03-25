#!/usr/bin/env python3
"""Split deep-js book.md into individual chapter files."""

import re
import unicodedata

BOOK_PATH = "sources-md/deep-js/book.md"
OUTPUT_DIR = "sources-md/deep-js"

def slugify(text, max_len=50):
    """Convert title text to a filename-safe slug."""
    # Remove markdown formatting
    text = re.sub(r'`([^`]*)`', r'\1', text)  # backtick code
    text = re.sub(r'\(bonus\)', 'bonus', text)
    text = text.lower()
    text = unicodedata.normalize('NFKD', text).encode('ascii', 'ignore').decode('ascii')
    text = re.sub(r'[^a-z0-9\s-]', '', text)
    text = re.sub(r'[\s]+', '-', text).strip('-')
    text = re.sub(r'-+', '-', text)
    return text[:max_len].rstrip('-')

# Read book
with open(BOOK_PATH, "r") as f:
    lines = f.readlines()

# Find chapter headings: lines matching "# N Title"
chapter_pattern = re.compile(r'^# (\d+)\s(.+)$')
chapters = []
for i, line in enumerate(lines):
    m = chapter_pattern.match(line.rstrip())
    if m:
        chapters.append({
            'number': int(m.group(1)),
            'title': m.group(2).strip(),
            'line': i + 1,  # 1-indexed
            'line_idx': i,  # 0-indexed
        })

print(f"Detected {len(chapters)} chapters\n")

# Extract frontmatter (everything before first chapter)
frontmatter_end = chapters[0]['line_idx']
frontmatter_lines = lines[:frontmatter_end]

fm_path = f"{OUTPUT_DIR}/00-frontmatter.md"
with open(fm_path, "w") as f:
    f.write("---\n")
    f.write("title: Frontmatter\n")
    f.write("source_format: epub\n")
    f.write("---\n\n")
    f.writelines(frontmatter_lines)

fm_count = len(frontmatter_lines)
print(f"  00-frontmatter.md ({fm_count} lines)")

# Extract each chapter
for idx, ch in enumerate(chapters):
    start = ch['line_idx']
    end = chapters[idx + 1]['line_idx'] if idx + 1 < len(chapters) else len(lines)
    chapter_lines = lines[start:end]

    slug = slugify(ch['title'])
    filename = f"{ch['number']:02d}-{slug}.md"
    filepath = f"{OUTPUT_DIR}/{filename}"

    with open(filepath, "w") as f:
        f.write("---\n")
        f.write(f"title: \"{ch['title']}\"\n")
        f.write(f"chapter_number: {ch['number']}\n")
        f.write(f"book_md_line: {ch['line']}\n")
        f.write("source_format: epub\n")
        f.write("---\n\n")
        f.writelines(chapter_lines)

    line_count = len(chapter_lines)
    print(f"  {filename} ({line_count} lines)")

print(f"\nTotal: 1 frontmatter + {len(chapters)} chapter files = {len(chapters) + 1} files created")
