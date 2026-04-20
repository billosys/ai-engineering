---
# === CORE IDENTIFICATION ===
concept: Safe Fixes
slug: safe-fixes

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
section: "Safe fixes"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "safe code fixes"
  - "safe code actions"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - lint-rules
extends: []
related:
  - code-fix-configuration
contrasts_with:
  - unsafe-fixes

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a safe fix vs. an unsafe fix?"
  - "What distinguishes safe fixes from unsafe fixes?"
  - "How do I apply safe fixes?"
---

# Quick Definition
Safe fixes are automatic code corrections provided by Biome lint rules that are guaranteed not to change the semantics of the code.

# Core Definition
Safe fixes are code fixes that are guaranteed to not change the semantic of the code. They can be applied without explicit review. Safe fixes can be applied automatically when saving a file in an LSP-compatible editor.

# Prerequisites
- lint-rules (understanding that rules can emit code fixes)

# Key Properties
1. **Semantics-preserving** -- Guaranteed not to change what the code does
2. **Auto-applicable** -- Can be applied without manual review
3. **On-save support** -- Can be applied automatically on file save in editors via `source.fixAll.biome`
4. **CLI application** -- Applied with the `--write` flag

# Construction / Recognition
- Apply safe fixes via CLI: `biome lint --write ./src`
- Apply on save in editor: configure the `source.fixAll.biome` code action
- A rule's fix can be reclassified from safe to unsafe (or vice versa) via the `fix` configuration option

# Context & Application
Safe fixes are the default automatic corrections applied during development. They are suitable for CI pipelines and automated workflows because they preserve code semantics. In editors, they can be configured to run on every save.

# Examples
From linter/index.mdx, "Safe fixes" section:
- "Safe fixes are guaranteed to not change the semantic of your code. They can be applied without explicit review."
- CLI usage: `biome lint --write ./src`

# Relationships
## Builds Upon
- lint-rules

## Enables
- code-fix-configuration (allows reclassifying fix safety)

## Related
- code-fix-configuration

## Contrasts With
- unsafe-fixes -- Unsafe fixes may change semantics and require manual review

# Common Errors
1. Assuming all rules have safe fixes -- many rules have no fix or only an unsafe fix

# Common Confusions
1. **Safe vs. no fix** -- A safe fix is an automatic correction; some rules have no fix at all
2. **Configurable safety** -- The safety classification can be overridden per rule via the `fix` option

# Source Reference
- linter/index.mdx: "Safe fixes" subsection

# Verification Notes
- High confidence: Explicitly defined in its own subsection
- Definition and CLI usage taken directly from source
