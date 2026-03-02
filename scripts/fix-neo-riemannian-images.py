#!/usr/bin/env python3
"""
Update image references in Neo-Riemannian Handbook markdown files
to point to ./images/ subdirectory.
"""

import re
from pathlib import Path

# Directory containing markdown files
MD_DIR = Path("sources-md/neo-riemannian-handbook")

def fix_image_paths(file_path):
    """Fix image paths in a markdown file."""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Count replacements
    original_count = content.count('![](_page_')

    # Replace ![](_page_X with ![](./images/_page_X
    updated_content = re.sub(
        r'!\[\]\(_page_',
        r'![](./images/_page_',
        content
    )

    # Write back if changes were made
    if content != updated_content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(updated_content)

        new_count = updated_content.count('![](./images/_page_')
        return True, new_count

    return False, 0

def main():
    """Process all markdown files."""
    md_files = sorted(MD_DIR.glob("*.md"))

    print(f"Found {len(md_files)} markdown files in {MD_DIR}/")
    print()

    total_updated = 0
    total_images = 0

    for md_file in md_files:
        updated, count = fix_image_paths(md_file)
        if updated:
            print(f"✓ {md_file.name:40s} - {count:3d} images updated")
            total_updated += 1
            total_images += count
        else:
            print(f"  {md_file.name:40s} - no images")

    print()
    print(f"Summary: Updated {total_images} image references in {total_updated} files")

if __name__ == "__main__":
    main()
