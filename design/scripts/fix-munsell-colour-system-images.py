#!/usr/bin/env python3
"""
Update image references in munsell-colour-system/book.md
to point to the ./images/ subdirectory.
"""

import re
from pathlib import Path

BOOK_FILE = Path("sources-md/munsell-colour-system/book.md")


def fix_image_paths(file_path):
    """Fix image paths in book.md."""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    original_count = content.count('![](_page_')

    updated_content = re.sub(
        r'!\[\]\(_page_',
        r'![](./images/_page_',
        content
    )

    if content != updated_content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(updated_content)
        new_count = updated_content.count('![](./images/_page_')
        return True, original_count, new_count

    return False, 0, 0


def main():
    print(f"Processing {BOOK_FILE}")
    updated, original, new = fix_image_paths(BOOK_FILE)
    if updated:
        print(f"✓ Updated {new} image references (was {original} bare references)")
    else:
        print("  No bare image references found — already fixed or none present.")


if __name__ == "__main__":
    main()
