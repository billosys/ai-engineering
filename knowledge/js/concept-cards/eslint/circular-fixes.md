---
# === CORE IDENTIFICATION ===
concept: Circular Fixes
slug: circular-fixes

# === CLASSIFICATION ===
category: maintenance
subcategory: null
tier: intermediate

# === PROVENANCE ===
source: "ESLint Documentation"
source_slug: eslint
authors: "ESLint Contributors"
chapter: "use/troubleshooting/circular-fixes.md"
chapter_number: null
pdf_page: null
section: null

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "ESLintCircularFixesWarning"
  - "conflicting fixes"
  - "fix loop"
  - "conflicting rule fixes"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - eslint
  - rules
extends: []
related:
  - core-rules-policy
  - configuration-files
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What causes ESLint circular fix warnings?"
  - "Why does ESLint report conflicting fixes?"
  - "How do I find which rules are conflicting?"
  - "How does ESLint autofix work in multiple passes?"
---

# Quick Definition
Circular fixes occur when two or more ESLint rules produce conflicting autofixes that undo each other across successive fix passes, causing ESLint to detect and warn about an infinite fix loop.

# Core Definition
ESLint applies autofixes in multiple passes. After each pass, the modified code is re-linted and additional fixes may be applied. A circular fix occurs when a fix applied in one pass is undone by a different rule's fix in a subsequent pass. For example, one rule might remove a trailing comma while another rule adds it back, creating an endless cycle. ESLint detects these cycles and emits a warning: "Circular fixes detected while fixing [path]. It is likely that you have conflicting rules in your configuration."

The resolution is to identify and reconfigure one of the conflicting rules. The identification process involves: opening the file in an editor with individual fix support (e.g., VS Code), finding a fixable rule's lint problem, applying that single fix, and observing which new lint problem appears -- that is the conflicting rule.

# Prerequisites
- eslint: Basic ESLint knowledge
- rules: Understanding that rules can provide autofixes

# Key Properties
1. **Multi-pass fixing** -- ESLint applies fixes iteratively, re-linting after each pass
2. **Cycle detection** -- ESLint automatically detects when fixes undo each other
3. **Warning, not error** -- Circular fixes produce a warning; linting still completes
4. **Configuration conflict** -- The root cause is always conflicting rule configurations

# Construction / Recognition
Warning message pattern:
```plaintext
ESLintCircularFixesWarning: Circular fixes detected while fixing path/to/file. It is likely that you have conflicting rules in your configuration.
```

Diagnosis steps:
1. Open the file in an editor with individual fix actions
2. Find a fixable lint problem and apply its fix
3. Observe what new problem appears -- that is the other conflicting rule
4. Reconfigure or remove one of the two rules

# Context & Application
Circular fixes typically arise when mixing rule sets from different sources (e.g., a style plugin and ESLint core rules) that have overlapping but contradictory opinions. This is a common issue when combining ESLint with formatting-related plugins or when extending multiple shareable configs with conflicting preferences.

# Examples
From use/troubleshooting/circular-fixes.md:
- "ESLint autofixes code in multiple passes, meaning it's possible that a fix in one pass is undone in a subsequent pass. For example, in the first pass a rule removes a trailing comma and in the following pass a different rule adds a trailing comma in the same place."

# Relationships
## Related
- rules
- configuration-files
- core-rules-policy

## Contrasts With
- Normal autofix behavior (fixes converge after a few passes without conflict)

# Common Errors
1. Ignoring the circular fix warning and assuming ESLint will resolve it -- the conflict persists until configuration is changed
2. Disabling both conflicting rules instead of picking which behavior to keep

# Common Confusions
1. **Warning vs. broken lint** -- ESLint still lints the file; the warning indicates the autofix could not fully converge
2. **Rule bugs vs. configuration conflicts** -- Circular fixes are almost always configuration conflicts, not rule bugs

# Source Reference
- use/troubleshooting/circular-fixes.md: Full description of symptom, cause, and resolution

# Verification Notes
- High confidence: Dedicated troubleshooting page with explicit cause and resolution steps
