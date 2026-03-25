#!/usr/bin/env python3
"""
Build the biome-linter skill reference files from extracted rules JSON.

Generates one markdown reference file per Biome category, with each rule
distilled to: name, description, don't example, do example.
"""

import json
import os
from pathlib import Path


CATEGORY_TITLES = {
    "correctness": "Correctness",
    "suspicious": "Suspicious Patterns",
    "style": "Style",
    "complexity": "Complexity",
    "a11y": "Accessibility (a11y)",
    "performance": "Performance",
    "security": "Security",
    "nursery": "Nursery (Experimental)",
}

CATEGORY_DESCRIPTIONS = {
    "correctness": "Rules that catch actual bugs — wrong assignments, unreachable code, broken control flow.",
    "suspicious": "Patterns that are likely wrong or unintended — potential typos, dubious comparisons, debug leftovers.",
    "style": "Code style consistency — naming, syntax preferences, idiomatic patterns.",
    "complexity": "Rules that flag unnecessarily complex code and suggest simpler alternatives.",
    "a11y": "Accessibility rules for HTML/JSX — ARIA compliance, semantic elements, keyboard navigation.",
    "performance": "Rules that catch performance pitfalls — O(n^2) patterns, unnecessary re-renders, blocking operations.",
    "security": "Rules that catch security vulnerabilities — eval(), target=_blank, unsafe innerHTML.",
    "nursery": "Experimental rules under evaluation. Not recommended by default — enable individually.",
}


def format_code_block(code: str, lang: str = "js") -> str:
    """Format a code block, detecting language from content."""
    if not code:
        return ""
    # Detect JSX
    if "<" in code and (">" in code or "/>" in code):
        if "role=" in code or "aria-" in code or "tabIndex" in code:
            lang = "jsx"
        elif code.strip().startswith("<"):
            lang = "jsx"
    # Detect CSS
    if any(kw in code for kw in ["@media", "color:", "font-", "display:", ".class"]):
        lang = "css"
    # Detect TypeScript
    if any(kw in code for kw in [": string", ": number", "<T>", "interface ", "type "]):
        lang = "ts"
    return f"```{lang}\n{code}\n```"


def build_reference(category: str, rules: list[dict]) -> str:
    """Build a reference markdown file for a category."""
    title = CATEGORY_TITLES.get(category, category.title())
    desc = CATEGORY_DESCRIPTIONS.get(category, "")

    # Split into recommended and optional
    recommended = [r for r in rules if r["recommended"]]
    optional = [r for r in rules if not r["recommended"]]

    lines = [
        f"# {title}",
        "",
        desc,
        "",
        f"**{len(recommended)} recommended** (enabled by default) | **{len(optional)} optional** (enable individually)",
        "",
    ]

    def write_rule(rule: dict) -> list[str]:
        out = []
        out.append(f"### {rule['name']}")
        out.append("")
        if rule["description"]:
            out.append(f"{rule['description']}")
            out.append("")
        if rule["invalid"]:
            out.append("**Don't:**")
            out.append(format_code_block(rule["invalid"]))
            out.append("")
        if rule["valid"]:
            out.append("**Do:**")
            out.append(format_code_block(rule["valid"]))
            out.append("")
        out.append("---")
        out.append("")
        return out

    if recommended:
        lines.append("## Recommended Rules")
        lines.append("")
        for rule in recommended:
            lines.extend(write_rule(rule))

    if optional:
        lines.append("## Optional Rules")
        lines.append("")
        for rule in optional:
            lines.extend(write_rule(rule))

    return "\n".join(lines)


def main():
    with open("sources-md/biome/extracted-rules.json") as f:
        data = json.load(f)

    out_dir = Path("skills/biome-linter/references")
    out_dir.mkdir(parents=True, exist_ok=True)

    for category, rules in data["categories"].items():
        content = build_reference(category, rules)
        out_file = out_dir / f"{category}.md"
        with open(out_file, "w") as f:
            f.write(content)
        print(f"  {out_file}: {len(rules)} rules")

    print(f"\nGenerated {len(data['categories'])} reference files in {out_dir}")


if __name__ == "__main__":
    main()
