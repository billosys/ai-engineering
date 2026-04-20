#!/usr/bin/env python3
"""Split exploring-js book.md into individual chapter files."""

import re
import unicodedata

BOOK_PATH = "sources-md/exploring-js/book.md"
OUTPUT_DIR = "sources-md/exploring-js"


def slugify(text, max_len=50):
    """Convert title text to a filename-safe slug."""
    # Remove markdown formatting and special markers
    text = re.sub(r'`([^`]*)`', r'\1', text)  # backtick code
    text = re.sub(r'\(bonus\)', 'bonus', text)
    text = re.sub(r'\(advanced\)', 'advanced', text)
    text = re.sub(r'\^ES\w+\^', '', text)  # ^ES6^, ^ES2017^, etc.
    text = re.sub(r'\{[^}]*\}', '', text)  # {#anchor} attributes
    text = text.lower().strip()
    text = unicodedata.normalize('NFKD', text).encode('ascii', 'ignore').decode('ascii')
    text = re.sub(r'[^a-z0-9\s-]', '', text)
    text = re.sub(r'[\s]+', '-', text).strip('-')
    text = re.sub(r'-+', '-', text)
    return text[:max_len].rstrip('-')


# Read book
with open(BOOK_PATH, "r") as f:
    lines = f.readlines()

# Find chapter headings: lines matching "## N Title" or "## A Title" (appendix)
# Note: book uses \u2003 (em space) between number and title
chapter_pattern = re.compile(r'^## (\d+|[A-Z])\s+(.+?)(?:\s*\{[^}]*\})?\s*$')

# Also find Part headings: "# I/II/III/... Title"
part_pattern = re.compile(r'^# ([IVXL]+)\s+(.+?)(?:\s*\{[^}]*\})?\s*$')

chapters = []
parts = []

for i, line in enumerate(lines):
    m = chapter_pattern.match(line.rstrip())
    if m:
        ch_num = m.group(1)
        title = m.group(2).strip()
        # Clean title of remaining attributes
        title = re.sub(r'\s*\{[^}]*\}', '', title).strip()
        chapters.append({
            'number': ch_num,
            'title': title,
            'line': i + 1,  # 1-indexed
            'line_idx': i,  # 0-indexed
        })
    pm = part_pattern.match(line.rstrip())
    if pm:
        parts.append({
            'numeral': pm.group(1),
            'title': pm.group(2).strip(),
            'line': i + 1,
            'line_idx': i,
        })

print(f"Detected {len(chapters)} chapters and {len(parts)} parts\n")
print("Parts:")
for p in parts:
    print(f"  Part {p['numeral']}: {p['title']} (line {p['line']})")

print("\nChapters:")
for ch in chapters:
    print(f"  Ch {ch['number']}: {ch['title']} (line {ch['line']})")

# For each chapter, find if there's a Part heading that should be included.
# A Part heading belongs to a chapter if it appears between the previous chapter
# and this chapter, with no other chapter in between.
# We'll set the actual start of each chapter's content to include any preceding
# Part heading (and its anchor lines).

chapter_starts = []
for idx, ch in enumerate(chapters):
    # Look for a Part heading between previous chapter end and this chapter
    prev_end = chapters[idx - 1]['line_idx'] if idx > 0 else 0
    start = ch['line_idx']

    # Check if any Part heading is between prev_end and this chapter
    for p in parts:
        if prev_end <= p['line_idx'] < start:
            # Include from the Part anchor (usually 2 lines before Part heading)
            # Find the first non-blank line before the Part heading
            part_start = p['line_idx']
            # Look back for anchor lines like []{#pt_xxx.xhtml}
            while part_start > prev_end and lines[part_start - 1].strip() == '':
                part_start -= 1
            if part_start > prev_end and lines[part_start - 1].strip().startswith('[]{#pt_'):
                part_start -= 1
            # Also skip blank line before anchor
            while part_start > prev_end and lines[part_start - 1].strip() == '':
                part_start -= 1
            start = part_start
            break

    chapter_starts.append(start)

# Extract frontmatter (everything before first chapter's actual start)
frontmatter_end = chapter_starts[0]
frontmatter_lines = lines[:frontmatter_end]

fm_path = f"{OUTPUT_DIR}/00-frontmatter.md"
with open(fm_path, "w") as f:
    f.write("---\n")
    f.write("title: Frontmatter\n")
    f.write("source_format: epub\n")
    f.write("---\n\n")
    f.writelines(frontmatter_lines)

fm_count = len(frontmatter_lines)
print(f"\n  00-frontmatter.md ({fm_count} lines)")

# Extract each chapter
for idx, ch in enumerate(chapters):
    start = chapter_starts[idx]
    end = chapter_starts[idx + 1] if idx + 1 < len(chapters) else len(lines)
    chapter_lines = lines[start:end]

    slug = slugify(ch['title'])
    # Format number: zero-pad integers, keep letter for appendix
    if ch['number'].isdigit():
        num_str = f"{int(ch['number']):02d}"
    else:
        num_str = ch['number']

    filename = f"{num_str}-{slug}.md"
    filepath = f"{OUTPUT_DIR}/{filename}"

    with open(filepath, "w") as f:
        f.write("---\n")
        f.write(f"title: \"{ch['title']}\"\n")
        if ch['number'].isdigit():
            f.write(f"chapter_number: {ch['number']}\n")
        else:
            f.write(f"chapter_number: \"{ch['number']}\"\n")
        f.write(f"book_md_line: {ch['line']}\n")
        f.write("source_format: epub\n")
        f.write("---\n\n")
        f.writelines(chapter_lines)

    line_count = len(chapter_lines)
    print(f"  {filename} ({line_count} lines)")

print(f"\nTotal: 1 frontmatter + {len(chapters)} chapter files = {len(chapters) + 1} files created")
