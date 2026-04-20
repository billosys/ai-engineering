---
# === CORE IDENTIFICATION ===
concept: Rule Severity
slug: rule-severity

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
section: "Change rule severity"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "diagnostic severity"
  - "lint severity levels"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - lint-rules
extends: []
related:
  - lint-rule-groups
  - biome-linter
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What severity levels can a Biome lint rule have?"
  - "How do I change the severity of a lint rule?"
  - "How does severity affect the CLI exit code?"
---

# Quick Definition
Rule severity controls the diagnostic level a Biome lint rule emits -- error, warn, or info -- which determines how the violation is reported and whether it affects the CLI exit code.

# Core Definition
Every Biome lint rule ships with a default severity. Users can override severity using `"error"`, `"warn"`, or `"info"` in configuration. The keyword `"on"` enables a rule with its shipped default severity. Severity can also be controlled at the group level, affecting all rules in that group at once.

- **error**: Always causes the CLI to exit with an error code. Useful for blocking CI when a violation occurs.
- **warn**: Similar to errors but does not cause the CLI to exit with an error code, unless the `--error-on-warnings` flag is used. Useful for surfacing issues while allowing CI to pass.
- **info**: Does not affect the exit status code of the CLI, even when `--error-on-warnings` is passed.

# Prerequisites
- lint-rules

# Key Properties
1. **Three levels** -- error, warn, info
2. **CLI exit behavior** -- error always fails; warn fails only with `--error-on-warnings`; info never fails
3. **Per-rule configuration** -- Each rule's severity can be individually overridden
4. **Per-group configuration** -- All rules in a group can be set to the same severity
5. **Default severity** -- Each rule has a built-in default; `"on"` enables it
6. **"off" disables** -- Setting severity to `"off"` disables the rule entirely

# Construction / Recognition
- Enable with default severity: `"noShoutyConstants": "on"`
- Set to error: `"noDebugger": "error"`
- Set to warn: `"useConst": "warn"`
- Set to info: `"noShoutyConstants": "info"`
- Disable: `"noDebugger": "off"`
- Group-level: `"a11y": "off"` or `"style": "warn"`

# Context & Application
Severity configuration is essential for CI integration. Teams typically set critical rules to `"error"` to block merges, use `"warn"` for rules being gradually adopted, and `"info"` for advisory rules. Group-level severity provides coarse-grained control for entire categories.

# Examples
From linter/index.mdx, "Change rule severity" section:
- "Diagnostics with the 'error' always cause the CLI to exit with an error code."
- "warn are similar to errors, but they don't cause the CLI to exit with an error code, unless the --error-on-warnings flag is used."
- "The 'info' severity won't affect the exit status code of the CLI, even when --error-on-warnings is passed."

# Relationships
## Builds Upon
- lint-rules

## Enables
- Fine-grained CI integration strategies

## Related
- lint-rule-groups (group-level severity control)
- biome-linter

## Contrasts With
- None directly

# Common Errors
1. Expecting `"info"` diagnostics to block CI -- info never affects the exit code
2. Forgetting `--error-on-warnings` -- without it, warnings do not block CI

# Common Confusions
1. **"on" vs. "error"** -- `"on"` uses the rule's shipped default severity, which may be warn or info, not necessarily error
2. **warn and --error-on-warnings** -- Warnings only block CI when this flag is explicitly passed

# Source Reference
- linter/index.mdx: "Change rule severity" and "Change group severity" subsections

# Verification Notes
- High confidence: Severity levels and their CLI behavior are explicitly documented
- All three severity descriptions taken from source text
