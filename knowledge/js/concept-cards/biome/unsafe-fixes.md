---
# === CORE IDENTIFICATION ===
concept: Unsafe Fixes
slug: unsafe-fixes

# === CLASSIFICATION ===
category: linter
subcategory: null
tier: intermediate

# === PROVENANCE ===
source: "Biome Documentation"
source_slug: biome
authors: "Biome Contributors"
chapter: "linter/index.mdx"
chapter_number: null
pdf_page: null
section: "Unsafe fixes"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "unsafe code fixes"
  - "unsafe code actions"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - lint-rules
  - safe-fixes
extends: []
related:
  - code-fix-configuration
contrasts_with:
  - safe-fixes

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a safe fix vs. an unsafe fix?"
  - "What distinguishes safe fixes from unsafe fixes?"
  - "How do I apply unsafe fixes?"
---

# Quick Definition
Unsafe fixes are automatic code corrections provided by Biome lint rules that may change the semantics of the program, requiring manual review before acceptance.

# Core Definition
Unsafe fixes may change the semantic of the program. It is advised to manually review the changes before accepting them. Unsafe fixes cannot be automatically applied on save in editors -- this is intentional, as it would be undesirable to change code semantics on save. However, individual unsafe fixes can be reviewed and applied one at a time in an editor.

# Prerequisites
- lint-rules
- safe-fixes (understanding the contrast)

# Key Properties
1. **Semantics-altering** -- May change what the code actually does
2. **Manual review required** -- Should not be applied without inspection
3. **No on-save support** -- Cannot be bulk-applied on file save in editors
4. **CLI requires explicit opt-in** -- Applied only with `--write --unsafe` flags together
5. **Individual review in editors** -- Can be reviewed and applied one fix at a time

# Construction / Recognition
- Apply both safe and unsafe fixes via CLI: `biome lint --write --unsafe ./src`
- In editors, review individual unsafe fixes through the code action tooltip
- A rule's fix can be reclassified from unsafe to safe via the `fix` configuration option

# Context & Application
Unsafe fixes exist because some automatic corrections trade correctness for convenience. The Biome team marks a fix as unsafe for several reasons: the rule or fix is still under development, the fix can change program semantics, or the fix can deteriorate developer experience during typing and saving (e.g., `noUnusedVariables` adds `_` prefixes).

# Examples
From linter/index.mdx, "Unsafe fixes" section:
- "Unsafe fixes may change the semantic of your program. Therefore, it's advised to manually review the changes."
- CLI usage: `biome lint --write --unsafe ./src`

From the FAQ:
- `noUnusedVariables` has an unsafe fix because it adds `_` to variable names, which "can deteriorate the DX of programmers while typing and saving"
- A fix may be unsafe because "the rule fix can change the semantics of a program"

# Relationships
## Builds Upon
- lint-rules

## Enables
- code-fix-configuration

## Related
- code-fix-configuration

## Contrasts With
- safe-fixes -- Safe fixes are guaranteed not to change semantics

# Common Errors
1. Using `--unsafe` without `--write` -- both flags are needed to apply unsafe fixes
2. Applying unsafe fixes in CI without review -- may introduce subtle behavior changes

# Common Confusions
1. **"Unsafe" does not mean "dangerous"** -- It means the fix may change semantics, not that it will break the code
2. **Why is rule X unsafe?** -- A fix is marked unsafe when it is under development, can change semantics, or can worsen developer experience during typing

# Source Reference
- linter/index.mdx: "Unsafe fixes" subsection and FAQ section

# Verification Notes
- High confidence: Explicitly defined in its own subsection
- FAQ reasoning for unsafe classification taken from source
