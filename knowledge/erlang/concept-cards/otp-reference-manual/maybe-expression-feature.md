---
# === CORE IDENTIFICATION ===
concept: Maybe Expression Feature
slug: maybe-expression-feature

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
  - "maybe_expr feature"
  - "maybe expression"
  - "EEP 49"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - erlang-feature-concept
  - feature-enablement
extends: []
related:
  - feature-lifecycle
  - comprehension-assignment-feature
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the maybe_expr feature?"
  - "When was the maybe expression approved?"
  - "How do I enable the maybe expression?"
---

# Quick Definition
The `maybe_expr` feature implements the `maybe` expression proposed in EEP 49. It was approved in Erlang/OTP 27 and is enabled by default in that and later releases. It is a concrete example of a feature that progressed through the full lifecycle from experimental to approved.

# Core Definition
The Erlang Reference Manual states: "`maybe_expr` (approved) - Implementation of the `maybe` expression proposed in EEP 49. It was approved in Erlang/OTP 27." (Features, "Existing Features"). The `maybe` expression provides a conditional matching construct that simplifies error handling patterns. As an approved feature, it is enabled by default but can still be disabled.

# Prerequisites
- **erlang-feature-concept** -- Must understand the selectable features system
- **feature-enablement** -- Must know how to enable/disable features

# Key Properties
1. Feature name: `maybe_expr`
2. Status: approved (as of OTP 27)
3. Proposed in EEP 49
4. Enabled by default since OTP 27
5. Can be disabled if needed (it is in the approved state, not permanent)
6. Implements the `maybe ... end` expression syntax

# Construction / Recognition
## To Enable (if using OTP < 27 or if disabled):
```erlang
-feature(maybe_expr, enable).
```

## To Disable (if needed):
```erlang
-feature(maybe_expr, disable).
```

# Context & Application
The `maybe_expr` feature is the most prominent example of the features system in practice. It demonstrates the full lifecycle: introduced as experimental, it allowed the community to try the new syntax and provide feedback, then was approved in OTP 27. The `maybe` expression simplifies code that would otherwise require nested case expressions for error handling, providing a more linear flow for sequences of pattern matches where any step might fail.

# Examples
**Example 1** (Existing Features):
The `maybe_expr` feature is listed as:
```
maybe_expr (approved) - Implementation of the maybe expression proposed in EEP 49.
                        It was approved in Erlang/OTP 27.
```

**Example 2** (Enabling in a module):
```erlang
-module(my_module).
-feature(maybe_expr, enable).

%% The maybe expression is now available
```

# Relationships
## Builds Upon
- **erlang-feature-concept** -- `maybe_expr` is a selectable feature
- **feature-enablement** -- Must be enabled in pre-OTP 27 or if disabled

## Enables
Usage of the `maybe ... end` expression syntax for conditional matching.

## Related
- **feature-lifecycle** -- Demonstrates the experimental-to-approved lifecycle
- **comprehension-assignment-feature** -- Another configurable feature (`compr_assign`)

## Contrasts With
None.

# Common Errors
- **Error**: Using `maybe` syntax without enabling the feature on older OTP versions
  **Correction**: Add `-feature(maybe_expr, enable).` to the module prefix when using OTP versions before 27.

# Common Confusions
- **Confusion**: Thinking `maybe_expr` is permanent and cannot be disabled
  **Clarification**: As of the source, `maybe_expr` is in the approved state, which means it is enabled by default but can still be disabled. It has not yet reached the permanent state.

# Source Reference
"Features" chapter, "Existing Features" section.

# Verification Notes
- Definition source: Direct from source text
- Confidence rationale: High -- explicitly listed as an existing feature
- Uncertainties: The detailed semantics of the maybe expression are in the Expressions chapter, not covered here
- Cross-reference status: All slugs verified
