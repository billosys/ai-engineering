#!/usr/bin/env python3
"""Fix image references in js-definitive-guide book.md to use relative paths."""

import re

BOOK_PATH = "sources-md/js-definitive-guide/book.md"

with open(BOOK_PATH, "r") as f:
    content = f.read()

# Replace bare image filenames with ./images/ prefix
new_content, count = re.subn(
    r'!\[([^\]]*)\]\((_page_)',
    r'![\1](./images/\2',
    content
)

with open(BOOK_PATH, "w") as f:
    f.write(new_content)

print(f"Updated {count} image references: '(_page_' -> '(./images/_page_'")
