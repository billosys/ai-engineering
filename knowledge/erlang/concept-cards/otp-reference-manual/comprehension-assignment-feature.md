---
# === CORE IDENTIFICATION ===
concept: Comprehension Assignment Feature
slug: comprehension-assignment-feature

# === CLASSIFICATION ===
category: core-idioms
subcategory: language-features
tier: intermediate

# === PROVENANCE ===
source: "Erlang Reference Manual"
source_slug: otp-reference-manual
authors: "Ericsson AB"
chapter: "Features"
chapter_number: null
pdf_page: null
section: "Existing Features"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "compr_assign feature"
  - "comprehension assignments"
  - "EEP 77"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - erlang-feature-concept
  - feature-enablement
extends: []
related:
  - feature-lifecycle
  - maybe-expression-feature
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the compr_assign feature?"
  - "What does EEP 77 propose?"
  - "What experimental features exist in Erlang?"
---

# Quick Definition
The `compr_assign` feature is an experimental feature that implements `Pattern = Expr` assignments in comprehensions, as proposed in EEP 77. As an experimental feature, it is disabled by default and must be explicitly enabled.

# Core Definition
The Erlang Reference Manual states: "`compr_assign` (experimental) - Implementation of `Pattern = Expr` assignments in comprehensions proposed in EEP 77." (Features, "Existing Features"). As an experimental feature, it is disabled by default, configurable, and available. It must be explicitly enabled to use.

# Prerequisites
- **erlang-feature-concept** -- Must understand the selectable features system
- **feature-enablement** -- Must know how to enable experimental features

# Key Properties
1. Feature name: `compr_assign`
2. Status: experimental
3. Proposed in EEP 77
4. Disabled by default
5. Must be explicitly enabled to use
6. Adds `Pattern = Expr` assignment syntax to comprehensions
7. May be approved, made permanent, or rejected in future releases

# Construction / Recognition
## To Enable:
```erlang
-feature(compr_assign, enable).
```
Or via `erlc`:
```
erlc -enable-feature compr_assign my_module.erl
```

# Context & Application
The `compr_assign` feature represents the experimental end of the feature lifecycle. It demonstrates how new language constructs are introduced for community testing before being committed to the language. As an experimental feature, it should be used with the understanding that it may change or be rejected in future releases.

# Examples
**Example 1** (Existing Features):
The `compr_assign` feature is listed as:
```
compr_assign (experimental) - Implementation of Pattern = Expr
                              assignments in comprehensions proposed in EEP 77.
```

# Relationships
## Builds Upon
- **erlang-feature-concept** -- `compr_assign` is a selectable feature
- **feature-enablement** -- Must be explicitly enabled as it is experimental

## Enables
Usage of `Pattern = Expr` assignments within list/binary comprehensions.

## Related
- **feature-lifecycle** -- An example of a feature in the experimental state
- **maybe-expression-feature** -- Another configurable feature, but in the approved state

## Contrasts With
None.

# Common Errors
- **Error**: Using comprehension assignments without enabling the feature
  **Correction**: Add `-feature(compr_assign, enable).` to the module prefix.

- **Error**: Relying on `compr_assign` in production code
  **Correction**: Experimental features may change semantics or be rejected. Use with caution and be prepared for changes.

# Common Confusions
- **Confusion**: Thinking experimental means "broken" or "unstable"
  **Clarification**: Experimental means the feature is available for testing and feedback, but its final form and acceptance are not guaranteed. It is functional but may evolve.

# Source Reference
"Features" chapter, "Existing Features" section.

# Verification Notes
- Definition source: Direct from source text
- Confidence rationale: High -- explicitly listed as an existing feature
- Uncertainties: Detailed semantics of comprehension assignments are in the Expressions chapter, not covered here
- Cross-reference status: All slugs verified
