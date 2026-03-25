#!/usr/bin/env python3
"""Fix image references in deep-js book.md to use relative paths."""

import re

BOOK_PATH = "sources-md/deep-js/book.md"
FULL_PREFIX = "sources-md/deep-js/media/"
RELATIVE_PREFIX = "./media/"

with open(BOOK_PATH, "r") as f:
    content = f.read()

new_content, count = content.replace(FULL_PREFIX, RELATIVE_PREFIX), content.count(FULL_PREFIX)

with open(BOOK_PATH, "w") as f:
    f.write(new_content)

print(f"Updated {count} image references: '{FULL_PREFIX}' -> '{RELATIVE_PREFIX}'")
