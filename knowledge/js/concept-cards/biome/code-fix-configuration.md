---
# === CORE IDENTIFICATION ===
concept: Code Fix Configuration
slug: code-fix-configuration

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
section: "Configure the code fix"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "fix option"
  - "code fix option"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - lint-rules
  - safe-fixes
  - unsafe-fixes
extends: []
related:
  - rule-severity
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I configure whether a rule's fix is safe, unsafe, or disabled?"
  - "Can I override the default safety of a code fix?"
---

# Quick Definition
The code fix configuration is a per-rule `fix` option in `biome.json` that controls whether a rule emits no fix, a safe fix, or an unsafe fix, allowing users to override the default classification.

# Core Definition
Biome allows configuring a safe fix to be treated as unsafe and vice versa, or turning the code fix off entirely. Code fixes are configured using the `fix` option on a rule, which accepts one of three values: `none` (no code fix emitted), `safe` (emit a safe fix), or `unsafe` (emit an unsafe fix).

# Prerequisites
- lint-rules
- safe-fixes
- unsafe-fixes

# Key Properties
1. **Three values** -- `none`, `safe`, `unsafe`
2. **Per-rule granularity** -- Each rule's fix behavior can be independently configured
3. **Override capability** -- A rule's default fix classification can be changed
4. **Combined with severity** -- The `fix` option is used alongside `level` in the rule's configuration object

# Construction / Recognition
```json
{
  "linter": {
    "rules": {
      "correctness": {
        "noUnusedVariables": {
          "level": "error",
          "fix": "none"
        }
      },
      "style": {
        "useConst": {
          "level": "warn",
          "fix": "unsafe"
        },
        "useTemplate": {
          "level": "warn",
          "fix": "safe"
        }
      }
    }
  }
}
```

# Context & Application
The `fix` option is useful when a rule's default fix classification does not match team preferences. For example, a team might disable the `noUnusedVariables` fix entirely to avoid the `_` prefix being added during development, or reclassify a fix from unsafe to safe if they have verified it is appropriate for their codebase.

# Examples
From linter/index.mdx, "Configure the code fix" section:
- `"fix": "none"` -- "the rule won't emit a code fix"
- `"fix": "safe"` -- "the rule will emit a safe fix"
- `"fix": "unsafe"` -- "the rule will emit an unsafe fix"
- Example: `noUnusedVariables` with `"fix": "none"` prevents the automatic `_` prefix

# Relationships
## Builds Upon
- safe-fixes
- unsafe-fixes

## Enables
- Custom workflows where fix safety is tuned per project

## Related
- rule-severity

## Contrasts With
- None directly

# Common Errors
1. Confusing `fix` with `level` -- `level` controls severity, `fix` controls the code action behavior
2. Setting `fix` at the group level -- the `fix` option is only available per rule, not per group

# Common Confusions
1. **"none" vs. "off"** -- `"off"` disables the rule entirely (no diagnostics); `"fix": "none"` keeps the rule active but suppresses its code fix

# Source Reference
- linter/index.mdx: "Configure the code fix" subsection

# Verification Notes
- High confidence: The fix option and its three values are explicitly documented
- Configuration example taken directly from source
