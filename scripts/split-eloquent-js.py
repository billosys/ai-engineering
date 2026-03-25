#!/usr/bin/env python3
"""Split eloquent-js book.md into individual chapter files.

This book uses unnumbered chapter headings (# Title) rather than # N Title.
Chapter numbers are derived from the EPUB anchor IDs (e.g., []{#01_values.xhtml}).
The chapter structure is:
  - Introduction (anchor 00_intro) -> Chapter 0
  - Chapters 1-21 (anchors 01_values through 21_skillsharing)
  - Exercise Hints (anchor hints) -> Appendix
"""

import re
import unicodedata

BOOK_PATH = "sources-md/eloquent-js/book.md"
OUTPUT_DIR = "sources-md/eloquent-js"


def slugify(text, max_len=50):
    """Convert title text to a filename-safe slug."""
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

# Find chapter boundaries using EPUB anchor IDs followed by <article> and # heading.
# Pattern: []{#NN_name.xhtml} on its own line, then <article>, then # Title
# The anchor ID encodes the chapter number (00-21) or special names like 'hints'.
anchor_pattern = re.compile(r'^\[]\{#(\w+)\.xhtml\}\s*$')
heading_pattern = re.compile(r'^# (.+)$')

chapters = []
i = 0
while i < len(lines):
    m = anchor_pattern.match(lines[i].strip())
    if m:
        anchor_id = m.group(1)
        # Look ahead for <article> then # heading within next 5 lines
        for j in range(i + 1, min(i + 6, len(lines))):
            hm = heading_pattern.match(lines[j].strip())
            if hm:
                title = hm.group(1).strip()
                # Derive chapter number from anchor ID
                num_match = re.match(r'^(\d+)_', anchor_id)
                if num_match:
                    chapter_num = int(num_match.group(1))
                elif anchor_id == 'hints':
                    chapter_num = 22  # appendix after chapter 21
                else:
                    # Skip non-chapter anchors (toc, frontmatter, titlepage)
                    break

                # Find the actual start: the anchor line itself
                chapters.append({
                    'number': chapter_num,
                    'title': title,
                    'anchor_id': anchor_id,
                    'line': i + 1,  # 1-indexed (anchor line)
                    'line_idx': i,  # 0-indexed
                    'heading_line': j + 1,  # 1-indexed
                })
                break
    i += 1

# Sort by line number (should already be in order)
chapters.sort(key=lambda c: c['line_idx'])

print(f"Detected {len(chapters)} chapters\n")
print("Chapter mapping:")
for ch in chapters:
    label = f"Ch {ch['number']:2d}" if ch['number'] <= 21 else "Hints"
    print(f"  {label}: {ch['title']:<45s} (line {ch['heading_line']})")
print()

# Extract frontmatter (everything before first chapter anchor)
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
    if ch['anchor_id'] == 'hints':
        filename = f"22-exercise-hints.md"
    else:
        filename = f"{ch['number']:02d}-{slug}.md"
    filepath = f"{OUTPUT_DIR}/{filename}"

    with open(filepath, "w") as f:
        f.write("---\n")
        f.write(f'title: "{ch["title"]}"\n')
        f.write(f"chapter_number: {ch['number']}\n")
        f.write(f"book_md_line: {ch['heading_line']}\n")
        f.write("source_format: epub\n")
        f.write("---\n\n")
        f.writelines(chapter_lines)

    line_count = len(chapter_lines)
    print(f"  {filename} ({line_count} lines)")

print(f"\nTotal: 1 frontmatter + {len(chapters)} chapter files = {len(chapters) + 1} files created")
