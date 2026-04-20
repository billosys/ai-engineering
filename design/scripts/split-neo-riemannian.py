#!/usr/bin/env python3
"""
Split the Neo-Riemannian Handbook into individual chapter files.
"""

import re
import os
from pathlib import Path

# Paths
SOURCE_FILE = Path("sources-md/neo-riemannian-handbook/book.md")
OUTPUT_DIR = Path("sources-md/neo-riemannian-handbook/chapters")

def extract_author_before_abstract(lines, abstract_line_num):
    """Extract author name from the lines before Abstract and Keywords."""
    # Look backwards from abstract for author name
    # Pattern 1: #### **Name** (bolded with heading)
    # Pattern 2: Plain text name above "The Oxford Handbook" line
    for i in range(abstract_line_num - 1, max(0, abstract_line_num - 20), -1):
        line = lines[i].strip()

        # Pattern 1: #### **Name**
        match = re.match(r'^####\s+\*\*(.+?)\*\*\s*$', line)
        if match:
            author = match.group(1).strip()
            return author

        # Pattern 2: Plain text name (not empty, not a heading, not "The Oxford")
        if line and not line.startswith('#') and not line.startswith('The Oxford'):
            # Check if "The Oxford Handbook" appears within the next few lines
            for j in range(i + 1, min(len(lines), i + 10)):
                if 'The Oxford Handbook' in lines[j]:
                    # This is likely an author name
                    author = line.strip()
                    # Ignore metadata, bios, and overly long lines (bios are usually long)
                    ignore_patterns = ['Print Publication', 'Subject:', 'Online Publication', 'DOI:', '**',
                                     ' is ', ' teaches ', ' holds ', ' are ', ' was ', ' were ']
                    if len(author) < 60 and not any(x in author for x in ignore_patterns):
                        return author
                    break
    return None

def extract_title_after_abstract(lines, abstract_start):
    """Extract chapter title from the lines after Abstract and Keywords."""
    # Look forward for a heading or significant text
    for i in range(abstract_start + 1, min(len(lines), abstract_start + 30)):
        line = lines[i].strip()
        # Skip empty lines and "Keywords:" lines
        if not line or line.startswith("Keywords:") or line.startswith("**Keywords"):
            continue
        # Look for section headings or significant text
        if line.startswith("##") or line.startswith("One day") or line.startswith("In "):
            # Try to extract meaningful title from nearby content
            # For now, return first significant line
            if line.startswith("##"):
                # Clean up markdown heading
                title = re.sub(r'^#+\s*\*?\*?', '', line)
                title = re.sub(r'\*?\*?\s*$', '', title)
                return title[:80]  # Truncate if too long
    return None

def slugify(text):
    """Convert text to filename-safe slug."""
    # Remove special characters, lowercase, replace spaces with hyphens
    text = text.lower()
    text = re.sub(r'[^\w\s-]', '', text)
    text = re.sub(r'[-\s]+', '-', text)
    return text.strip('-')

def find_chapter_boundaries(lines):
    """Find all chapter start positions marked by Abstract and Keywords."""
    chapters = []

    for i, line in enumerate(lines):
        if line.strip() == "## **Abstract and Keywords**":
            # Extract author from preceding lines
            author = extract_author_before_abstract(lines, i)

            # Extract some context for title
            title = extract_title_after_abstract(lines, i)

            chapters.append({
                'start_line': i,
                'author': author or "Unknown",
                'title': title or "Untitled"
            })

    return chapters

def split_into_chapters():
    """Main function to split the book into chapters."""
    print(f"Reading {SOURCE_FILE}...")
    with open(SOURCE_FILE, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    total_lines = len(lines)
    print(f"Total lines: {total_lines}")

    # Find chapter boundaries
    chapters = find_chapter_boundaries(lines)
    print(f"\nFound {len(chapters)} chapters:")

    for i, chapter in enumerate(chapters):
        print(f"  {i+1:2d}. Line {chapter['start_line']:5d} - {chapter['author']}")

    # Create output directory
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    # Extract frontmatter (everything before first chapter)
    if chapters:
        frontmatter_end = chapters[0]['start_line']
        frontmatter_content = ''.join(lines[:frontmatter_end])

        frontmatter_file = OUTPUT_DIR / "00-frontmatter.md"
        with open(frontmatter_file, 'w', encoding='utf-8') as f:
            f.write(frontmatter_content)
        print(f"\nExtracted frontmatter to {frontmatter_file}")

    # Extract each chapter
    for i, chapter in enumerate(chapters):
        chapter_num = i + 1
        start = chapter['start_line']

        # End is either the next chapter or end of file
        if i + 1 < len(chapters):
            end = chapters[i + 1]['start_line']
        else:
            end = total_lines

        # Extract chapter content
        chapter_content = ''.join(lines[start:end])

        # Create filename
        author_slug = slugify(chapter['author'])
        # Limit author slug length
        if len(author_slug) > 30:
            author_slug = author_slug[:30]

        filename = f"{chapter_num:02d}-{author_slug}.md"
        filepath = OUTPUT_DIR / filename

        # Write chapter file
        with open(filepath, 'w', encoding='utf-8') as f:
            # Add metadata header
            f.write(f"# Chapter {chapter_num}: {chapter['author']}\n\n")
            f.write(f"<!-- Original line: {start} -->\n\n")
            f.write(chapter_content)

        print(f"  Chapter {chapter_num:2d} -> {filename} ({end - start} lines)")

    print(f"\n✓ Split complete! {len(chapters)} chapters + frontmatter extracted to {OUTPUT_DIR}/")
    print(f"\nNote: Image references still point to parent directory.")
    print(f"      Images remain in: sources-md/neo-riemannian-handbook/")

if __name__ == "__main__":
    split_into_chapters()
