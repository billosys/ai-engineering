#!/usr/bin/env python3
"""
Extract Biome linter rules from MDX source files into categorized JSON.

Parses each .mdx rule file to extract:
- Rule name, category, description
- First invalid code example (the "don't")
- First valid code example (the "do")
- Whether the rule is recommended
"""

import json
import os
import re
import sys
from pathlib import Path


def extract_rule(filepath: str) -> dict | None:
    """Extract structured rule data from an MDX file."""
    with open(filepath, "r") as f:
        content = f.read()

    # Rule name from frontmatter title
    title_match = re.search(r"^title:\s*(.+)$", content, re.MULTILINE)
    if not title_match:
        return None
    name = title_match.group(1).strip()

    # Category from diagnostic category
    cat_match = re.search(r"lint/(\w+)/", content)
    if not cat_match:
        return None
    category = cat_match.group(1)

    # Recommended?
    recommended = "**recommended**" in content

    # Description — text between "## Description" and "## Examples"
    desc_match = re.search(
        r"## Description\s*\n(.*?)(?=\n## )", content, re.DOTALL
    )
    description = ""
    if desc_match:
        raw = desc_match.group(1).strip()
        # Take first paragraph only (up to double newline or code block)
        first_para = re.split(r"\n\n|```", raw)[0].strip()
        # Clean markdown artifacts
        first_para = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", first_para)
        first_para = re.sub(r"`([^`]+)`", r"\1", first_para)
        # Collapse to single line
        first_para = re.sub(r"\s+", " ", first_para)
        description = first_para

    # Extract code blocks between ### Invalid and ### Valid
    invalid_section = re.search(
        r"### Invalid\s*\n(.*?)(?=### Valid)", content, re.DOTALL
    )
    valid_section = re.search(
        r"### Valid\s*\n(.*?)(?=## (?:Options|Related)|\Z)", content, re.DOTALL
    )

    def first_code_block(section_text: str) -> str:
        """Extract the first fenced code block from a section."""
        match = re.search(
            r"```(?:js|jsx|ts|tsx|css|graphql|html)\n(.*?)```",
            section_text,
            re.DOTALL,
        )
        if match:
            return match.group(1).strip()
        return ""

    invalid_code = ""
    if invalid_section:
        invalid_code = first_code_block(invalid_section.group(1))

    valid_code = ""
    if valid_section:
        valid_code = first_code_block(valid_section.group(1))

    if not invalid_code and not valid_code:
        return None

    return {
        "name": name,
        "category": category,
        "description": description,
        "recommended": recommended,
        "invalid": invalid_code,
        "valid": valid_code,
    }


def main():
    rules_dir = Path(
        os.environ.get(
            "RULES_DIR",
            "sources-md/biome/linter/rules",
        )
    )
    output_path = Path(
        os.environ.get("OUTPUT", "sources-md/biome/extracted-rules.json")
    )

    rules = []
    skipped = 0
    for mdx_file in sorted(rules_dir.glob("*.mdx")):
        rule = extract_rule(str(mdx_file))
        if rule:
            rules.append(rule)
        else:
            skipped += 1

    # Group by category for stats
    categories = {}
    for r in rules:
        cat = r["category"]
        categories.setdefault(cat, []).append(r)

    print(f"Extracted {len(rules)} rules, skipped {skipped}")
    for cat, cat_rules in sorted(
        categories.items(), key=lambda x: -len(x[1])
    ):
        rec = sum(1 for r in cat_rules if r["recommended"])
        print(f"  {cat}: {len(cat_rules)} rules ({rec} recommended)")

    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(
            {"total": len(rules), "categories": categories},
            f,
            indent=2,
        )

    print(f"\nWritten to {output_path}")


if __name__ == "__main__":
    main()
