#!/usr/bin/env python3
"""
Build the deno-js-linter skill from Deno lint rule markdown files.

Filters to pure JS/ECMAScript rules only — no React/JSX, Fresh, Deno-specific,
Node.js-specific, or TypeScript type-system rules. Organizes into categories
appropriate for pure JS development.
"""

import re
from pathlib import Path


# --- Exclusion lists ---

EXCLUDE_NAMES = {
    # React / JSX / Fresh
    "jsx-boolean-value",
    "jsx-button-has-type",
    "jsx-curly-braces",
    "jsx-key",
    "jsx-no-children-prop",
    "jsx-no-comment-text-nodes",
    "jsx-no-duplicate-props",
    "jsx-no-unescaped-entities",
    "jsx-no-useless-fragment",
    "jsx-props-no-spread-multi",
    "jsx-void-dom-elements-no-children",
    "react-no-danger",
    "react-no-danger-with-children",
    "react-rules-of-hooks",
    "fresh-handler-export",
    "fresh-server-event-handlers",
    # Deno-specific
    "no-deprecated-deno-api",
    "no-external-import",
    "no-sloppy-imports",
    "no-slow-types",
    "no-unversioned-import",
    "no-import-prefix",
    # Node.js-specific
    "no-node-globals",
    "no-process-global",
    "no-window-prefix",
    "no-window",
    # TypeScript type-system rules
    "adjacent-overload-signatures",
    "ban-ts-comment",
    "ban-types",
    "explicit-function-return-type",
    "explicit-module-boundary-types",
    "no-empty-enum",
    "no-empty-interface",
    "no-explicit-any",
    "no-extra-non-null-assertion",
    "no-implicit-declare-namespace-export",
    "no-inferrable-types",
    "no-misused-new",
    "no-namespace",
    "no-non-null-asserted-optional-chain",
    "no-non-null-assertion",
    "prefer-as-const",
    "prefer-namespace-keyword",
    "verbatim-module-syntax",
    # TypeScript / module-system specific
    "triple-slash-reference",
    "no-invalid-triple-slash-reference",
    "no-import-assertions",
    # Deno-specific tooling
    "ban-unknown-rule-code",
    "ban-untagged-ignore",
    "ban-unused-ignore",
    "ban-untagged-todo",
    # Deno-specific runtime
    "prefer-primordials",
    "no-top-level-await",
}


# --- JS category mapping ---

# Map rule names to JS-focused categories
CATEGORY_MAP = {
    # Bugs & Correctness
    "constructor-super": "bugs",
    "for-direction": "bugs",
    "getter-return": "bugs",
    "no-array-constructor": "bugs",
    "no-async-promise-executor": "bugs",
    "no-case-declarations": "bugs",
    "no-class-assign": "bugs",
    "no-compare-neg-zero": "bugs",
    "no-cond-assign": "bugs",
    "no-const-assign": "bugs",
    "no-constant-condition": "bugs",
    "no-control-regex": "bugs",
    "no-delete-var": "bugs",
    "no-dupe-args": "bugs",
    "no-dupe-class-members": "bugs",
    "no-dupe-else-if": "bugs",
    "no-dupe-keys": "bugs",
    "no-duplicate-case": "bugs",
    "no-empty-character-class": "bugs",
    "no-empty-pattern": "bugs",
    "no-ex-assign": "bugs",
    "no-fallthrough": "bugs",
    "no-func-assign": "bugs",
    "no-global-assign": "bugs",
    "no-import-assign": "bugs",
    "no-inner-declarations": "bugs",
    "no-invalid-regexp": "bugs",
    "no-new-symbol": "bugs",
    "no-obj-calls": "bugs",
    "no-octal": "bugs",
    "no-prototype-builtins": "bugs",
    "no-redeclare": "bugs",
    "no-self-assign": "bugs",
    "no-setter-return": "bugs",
    "no-shadow-restricted-names": "bugs",
    "no-this-before-super": "bugs",
    "no-unreachable": "bugs",
    "no-unsafe-finally": "bugs",
    "no-unsafe-negation": "bugs",
    "use-isnan": "bugs",
    "valid-typeof": "bugs",
    # Pitfalls & Suspicious
    "eqeqeq": "pitfalls",
    "guard-for-in": "pitfalls",
    "no-await-in-loop": "pitfalls",
    "no-await-in-sync-fn": "pitfalls",
    "no-boolean-literal-for-arguments": "pitfalls",
    "no-console": "pitfalls",
    "no-debugger": "pitfalls",
    "no-empty": "pitfalls",
    "no-eval": "pitfalls",
    "no-irregular-whitespace": "pitfalls",
    "no-regex-spaces": "pitfalls",
    "no-self-compare": "pitfalls",
    "no-sparse-arrays": "pitfalls",
    "no-throw-literal": "pitfalls",
    "no-undef": "pitfalls",
    "no-with": "pitfalls",
    "require-await": "pitfalls",
    "require-yield": "pitfalls",
    # Style & Idioms
    "camelcase": "style",
    "default-param-last": "style",
    "no-this-alias": "style",
    "no-unused-labels": "style",
    "no-unused-vars": "style",
    "no-useless-rename": "style",
    "no-var": "style",
    "no-extra-boolean-cast": "style",
    "prefer-ascii": "style",
    "prefer-const": "style",
    "single-var-declarator": "style",
}


def parse_rule(filepath: Path) -> dict | None:
    """Parse a Deno lint rule markdown file."""
    content = filepath.read_text()
    name = filepath.stem

    # Skip excluded rules
    if name in EXCLUDE_NAMES:
        return None

    # Parse tags from frontmatter
    tags_match = re.search(r"tags:\s*\[([^\]]*)\]", content)
    tags = []
    if tags_match:
        raw = tags_match.group(1).strip()
        if raw:
            tags = [t.strip() for t in raw.split(",")]

    # Skip rules with framework tags
    framework_tags = {"react", "jsx", "fresh"}
    if framework_tags & set(tags):
        return None

    recommended = "recommended" in tags

    # Extract description (text between frontmatter and first **Invalid:** or **Valid:**)
    desc_match = re.search(
        r"^---\s*\n.*?\n---\s*\n(.*?)(?=\*\*Invalid:\*\*|\*\*Valid:\*\*|\Z)",
        content,
        re.DOTALL,
    )
    description = ""
    if desc_match:
        raw = desc_match.group(1).strip()
        # Take first paragraph (up to double newline or code block)
        first_para = re.split(r"\n\n|```", raw)[0].strip()
        # Clean markdown links
        first_para = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", first_para)
        first_para = re.sub(r"`([^`]*)`", r"\1", first_para)
        first_para = re.sub(r"\s+", " ", first_para)
        description = first_para

    # Extract first invalid code block
    invalid_section = re.search(
        r"\*\*Invalid:\*\*\s*\n(.*?)(?=\*\*Valid:\*\*|\Z)", content, re.DOTALL
    )
    invalid_code = ""
    if invalid_section:
        code_match = re.search(
            r"```(?:typescript|javascript|ts|js)?\n(.*?)```",
            invalid_section.group(1),
            re.DOTALL,
        )
        if code_match:
            invalid_code = code_match.group(1).strip()

    # Extract first valid code block
    valid_section = re.search(
        r"\*\*Valid:\*\*\s*\n(.*?)(?=\Z)", content, re.DOTALL
    )
    valid_code = ""
    if valid_section:
        code_match = re.search(
            r"```(?:typescript|javascript|ts|js)?\n(.*?)```",
            valid_section.group(1),
            re.DOTALL,
        )
        if code_match:
            valid_code = code_match.group(1).strip()

    if not invalid_code and not valid_code and not description:
        return None

    # Determine category
    category = CATEGORY_MAP.get(name)
    if category is None:
        return None  # Rule not mapped = excluded

    return {
        "name": name,
        "category": category,
        "description": description,
        "recommended": recommended,
        "invalid": invalid_code,
        "valid": valid_code,
    }


# --- Category definitions ---

CATEGORIES = {
    "bugs": {
        "title": "Bugs & Correctness",
        "description": (
            "Rules that catch real bugs — wrong assignments, unreachable code, "
            "broken control flow, incorrect operations."
        ),
    },
    "pitfalls": {
        "title": "Pitfalls & Suspicious Patterns",
        "description": (
            "Patterns that are likely wrong or unintended — dubious comparisons, "
            "misused async, debug leftovers, eval, empty blocks."
        ),
    },
    "style": {
        "title": "Style & Idioms",
        "description": (
            "Code style consistency — const vs let vs var, naming conventions, "
            "cleaner declarations, modern idioms."
        ),
    },
}


def build_reference(title: str, description: str, rules: list[dict]) -> str:
    """Build a reference markdown file for a category."""
    recommended = [r for r in rules if r["recommended"]]
    optional = [r for r in rules if not r["recommended"]]

    lines = [
        f"# {title}",
        "",
        description,
        "",
        f"**{len(recommended)} recommended** | **{len(optional)} optional**",
        "",
    ]

    def write_rule(rule: dict) -> list[str]:
        out = []
        out.append(f"### {rule['name']}")
        out.append("")
        if rule["description"]:
            out.append(rule["description"])
            out.append("")
        if rule["invalid"]:
            out.append("**Don't:**")
            out.append(f"```js\n{rule['invalid']}\n```")
            out.append("")
        if rule["valid"]:
            out.append("**Do:**")
            out.append(f"```js\n{rule['valid']}\n```")
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
    rules_dir = Path("sources-md/deno/lint/rules")
    out_dir = Path("skills/deno-js-linter/references")
    out_dir.mkdir(parents=True, exist_ok=True)

    # Parse all rules
    all_parsed = []
    skipped = 0
    for md_file in sorted(rules_dir.glob("*.md")):
        rule = parse_rule(md_file)
        if rule:
            all_parsed.append(rule)
        else:
            skipped += 1

    print(f"Total rule files: {len(list(rules_dir.glob('*.md')))}")
    print(f"Pure JS rules: {len(all_parsed)}")
    print(f"Skipped: {skipped}")
    print()

    # Group by category
    by_category: dict[str, list[dict]] = {}
    for rule in all_parsed:
        by_category.setdefault(rule["category"], []).append(rule)

    # Write reference files
    for cat_key, cat_info in CATEGORIES.items():
        cat_rules = by_category.get(cat_key, [])
        if not cat_rules:
            continue

        content = build_reference(
            cat_info["title"], cat_info["description"], cat_rules
        )
        out_file = out_dir / f"{cat_key}.md"
        out_file.write_text(content)

        rec = sum(1 for r in cat_rules if r["recommended"])
        print(f"  {cat_key}: {len(cat_rules)} rules ({rec} recommended)")

    print(f"\nTotal JS rules written: {len(all_parsed)}")


if __name__ == "__main__":
    main()
