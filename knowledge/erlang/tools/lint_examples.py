#!/usr/bin/env python3
"""
lint_examples.py — enforce the GOOD/BAD contract across Erlang guide chapters.

Every pattern (an `## PREFIX-NN: Title` H2 block) in knowledge/erlang/guides/
MUST contain, within at least one fenced ```erlang block:
  - a GOOD example, marked `%% Good`, `% Good`, or `✅`
  - a BAD example,  marked `%% Bad`,  `% Bad`,  or `❌`

It also checks the required scaffolding fields (**Strength**, **Summary**).

This is the cheap, mechanical layer of the three-layer enforcement described in
workbench/PLAN.md. It answers "does each pattern HAVE both examples?" — not
"are the examples correct?" (that is the semantic review pass).

Usage:
    python3 lint_examples.py [GUIDES_DIR]
    # default GUIDES_DIR = ../guides relative to this file

Exit code 0 = clean, 1 = violations found. Suitable for CI / pre-commit.
Skeleton chapters (containing the `<!-- STATUS: skeleton` marker and no
patterns yet) are reported as SKIPPED, not failed, so the linter is usable
from day one while chapters are still being populated.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

PATTERN_HEADING = re.compile(r"^##\s+([A-Z]{2,4})-(\d+):\s+(.*)$")
FENCE_ERLANG = re.compile(r"```erlang\b(.*?)```", re.DOTALL)
GOOD_MARK = re.compile(r"%+\s*Good\b|✅", re.IGNORECASE)
BAD_MARK = re.compile(r"%+\s*Bad\b|❌", re.IGNORECASE)
STRENGTH = re.compile(r"^\*\*Strength\*\*:\s*(MUST|SHOULD|CONSIDER|AVOID)\b", re.MULTILINE)
SUMMARY = re.compile(r"^\*\*Summary\*\*:", re.MULTILINE)
SKELETON = re.compile(r"<!--\s*STATUS:\s*skeleton")


def split_patterns(text: str):
    """Yield (pattern_id, title, body) for each `## PREFIX-NN: Title` block."""
    lines = text.splitlines(keepends=True)
    blocks, current, header = [], [], None
    for line in lines:
        m = PATTERN_HEADING.match(line.rstrip("\n"))
        if m:
            if header is not None:
                blocks.append((header, "".join(current)))
            header = (f"{m.group(1)}-{m.group(2)}", m.group(3).strip())
            current = []
        elif header is not None:
            current.append(line)
    if header is not None:
        blocks.append((header, "".join(current)))
    for (pid, title), body in blocks:
        yield pid, title, body


def lint_file(path: Path):
    """Return (violations, n_patterns, skipped:bool) for one guide file."""
    text = path.read_text(encoding="utf-8")
    patterns = list(split_patterns(text))
    if not patterns:
        # No patterns yet. A skeleton stub is fine; anything else is suspicious.
        return ([] if SKELETON.search(text) else
                [f"{path.name}: no patterns and no skeleton marker"], 0, True)

    violations = []
    for pid, title, body in patterns:
        fences = FENCE_ERLANG.findall(body)
        joined = "\n".join(fences)
        if not STRENGTH.search(body):
            violations.append(f"{path.name} {pid}: missing or malformed **Strength**")
        if not SUMMARY.search(body):
            violations.append(f"{path.name} {pid}: missing **Summary**")
        if not fences:
            violations.append(f"{path.name} {pid}: no ```erlang code block")
            continue
        if not GOOD_MARK.search(joined):
            violations.append(f"{path.name} {pid} ({title}): no GOOD example (%% Good / ✅)")
        if not BAD_MARK.search(joined):
            violations.append(f"{path.name} {pid} ({title}): no BAD example (%% Bad / ❌)")
    return violations, len(patterns), False


def main(argv):
    guides_dir = Path(argv[1]) if len(argv) > 1 else Path(__file__).resolve().parent.parent / "guides"
    files = sorted(guides_dir.glob("*.md"))
    if not files:
        print(f"No guide files found in {guides_dir}", file=sys.stderr)
        return 1

    all_violations, total_patterns, skipped = [], 0, 0
    for f in files:
        v, n, was_skipped = lint_file(f)
        total_patterns += n
        if was_skipped and not v:
            skipped += 1
            print(f"  SKIP  {f.name} (skeleton, 0 patterns)")
        elif not v:
            print(f"  OK    {f.name} ({n} patterns)")
        else:
            print(f"  FAIL  {f.name} ({n} patterns, {len(v)} issues)")
            all_violations.extend(v)

    print()
    print(f"Checked {len(files)} files · {total_patterns} patterns · {skipped} skeletons skipped")
    if all_violations:
        print(f"\n{len(all_violations)} violation(s):")
        for v in all_violations:
            print(f"  - {v}")
        return 1
    print("All populated patterns satisfy the GOOD/BAD contract.")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
