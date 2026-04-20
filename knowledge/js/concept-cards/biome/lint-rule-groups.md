---
# === CORE IDENTIFICATION ===
concept: Lint Rule Groups
slug: lint-rule-groups

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
section: "Linter Groups"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "linter groups"
  - "rule groups"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - biome-linter
  - lint-rules
extends: []
related:
  - rule-severity
  - nursery-rules
  - linter-domains
contrasts_with:
  - linter-domains

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What are lint rule groups?"
  - "What distinguishes lint rule groups from domains?"
  - "How do I enable or disable a group of rules?"
---

# Quick Definition
Lint rule groups are organizational categories that classify Biome's rules by the type of problem they address, such as accessibility, correctness, or style.

# Core Definition
The Biome linter divides rules into groups. Groups offer a category under which rules fall, helping users choose which rules to enable or disable and helping developers decide where to place new rules. Groups can be configured as a whole -- all rules in a group can be turned on, off, or set to a specific severity level.

# Prerequisites
- biome-linter
- lint-rules

# Key Properties
1. **Accessibility (a11y)** -- Rules focused on preventing accessibility problems
2. **Complexity** -- Rules that inspect complex code that could be simplified
3. **Correctness** -- Rules that detect code guaranteed to be incorrect or useless
4. **Nursery** -- New rules still under development, requiring explicit opt-in
5. **Performance** -- Rules catching code that could run faster or be more efficient
6. **Security** -- Rules that detect potential security flaws
7. **Style** -- Rules enforcing consistent, idiomatic code; generate warnings by default instead of errors
8. **Suspicious** -- Rules that detect code likely to be incorrect or useless

# Construction / Recognition
- Disable an entire group:
```json
{
  "linter": {
    "rules": {
      "a11y": "off"
    }
  }
}
```
- Skip a group via CLI: `biome lint --skip=style`
- Run only a group via CLI: `biome lint --only=a11y`
- Individual rule configuration overrides group-level settings

# Context & Application
Groups provide coarse-grained control over which rules are active. For example, a backend-only project might disable the `a11y` group entirely since accessibility is not a concern. Style rules default to warning severity rather than error, reflecting their advisory nature.

# Examples
From linter/index.mdx, "Linter Groups" section:
- "Rules focused on preventing accessibility problems" (Accessibility)
- "Rules that detect code that is guaranteed to be incorrect or useless" (Correctness)
- "Rules that detect code that is likely to be incorrect or useless" (Suspicious)
- The `noDebugger` rule "is part of the suspicious group"

# Relationships
## Builds Upon
- lint-rules

## Enables
- nursery-rules (nursery is a special group)

## Related
- rule-severity (group-level severity can be set)

## Contrasts With
- linter-domains -- Groups categorize by problem type (correctness, style), while domains categorize by technology (React, Solid, test). A rule belongs to one group but may also belong to a domain.

# Common Errors
1. Confusing groups with domains -- groups classify by problem type, domains by technology
2. Disabling a group but expecting individual rule overrides to still work without re-enabling them

# Common Confusions
1. **Correctness vs. Suspicious** -- Correctness rules detect code "guaranteed" to be incorrect, while suspicious rules detect code "likely" to be incorrect
2. **Style rules default to warnings** -- Unlike other groups, style rules generate warnings by default, not errors

# Source Reference
- linter/index.mdx: "Linter Groups" section and "Change group severity" subsection

# Verification Notes
- High confidence: All eight groups are explicitly listed and described in linter/index.mdx
- Descriptions quoted directly from source
