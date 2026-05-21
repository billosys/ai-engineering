---
# === CORE IDENTIFICATION ===
concept: Erlang Feature Concept
slug: erlang-feature-concept

# === CLASSIFICATION ===
category: core-idioms
subcategory: language-evolution
tier: intermediate

# === PROVENANCE ===
source: "Erlang Reference Manual"
source_slug: otp-reference-manual
authors: "Ericsson AB"
chapter: "Features"
chapter_number: null
pdf_page: null
section: null

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "selectable features"
  - "Erlang features system"

# === TYPED RELATIONSHIPS ===
prerequisites: []
extends: []
related:
  - feature-lifecycle
  - feature-enablement
  - maybe-expression-feature
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What are selectable features in Erlang?"
  - "When were selectable features introduced?"
  - "What kinds of changes can features introduce?"
---

# Quick Definition
Introduced in OTP 25, Erlang's selectable features system allows language and runtime changes to be individually enabled or disabled. A feature can add new syntax, change existing semantics, or modify runtime behavior, providing a controlled mechanism for language evolution.

# Core Definition
The Erlang Reference Manual states: "Introduced in OTP 25, Erlang has the concept of selectable features. A feature can change, add, or remove behaviour of the language and/or runtime system." (Features). Examples include "Adding new syntactical constructs to the language," "Changing the semantics of an existing construct," and "Changing the behaviour of some runtime aspect." Features start as experimental, allowing users to try them and provide feedback, and can be enabled or disabled through compiler options, module directives, and runtime options.

# Prerequisites
This is a standalone concept with no prerequisites.

# Key Properties
1. Introduced in OTP 25
2. A feature can add, change, or remove language/runtime behavior
3. Features start as experimental, disabled by default
4. Features can be individually enabled or disabled
5. Even non-experimental features can be enabled or disabled to allow gradual adoption
6. Features are controlled via compiler options, directives, and runtime options
7. The system includes preprocessor macros for conditional compilation

# Construction / Recognition
## To Identify a Feature:
1. Use `erlc -list-features` to see all available features
2. Use `erlc -describe-feature <feature>` for details about a specific feature
3. Use the `erl_features` module to query features programmatically
4. Check for `?FEATURE_AVAILABLE(Feature)` and `?FEATURE_ENABLED(Feature)` macros

# Context & Application
The features system allows Erlang to evolve without forcing immediate adoption of changes. Developers can try experimental features, provide feedback, and gradually adopt approved features at their own pace instead of being forced when changing to a new OTP release. This makes the language evolution process more controlled and less disruptive to existing codebases.

# Examples
**Example 1** (Features -- current features):
- `maybe_expr` (approved): The `maybe` expression from EEP 49, approved in OTP 27
- `compr_assign` (experimental): Pattern assignments in comprehensions from EEP 77

# Relationships
## Builds Upon
None -- this is a foundational concept for the features system.

## Enables
- **feature-lifecycle** -- Features follow a defined lifecycle
- **feature-enablement** -- Features can be enabled/disabled
- **maybe-expression-feature** -- The `maybe_expr` feature is a concrete example

## Related
None.

## Contrasts With
None.

# Common Errors
- **Error**: Assuming all new language additions are always available
  **Correction**: Some features start as experimental and must be explicitly enabled before use.

# Common Confusions
- **Confusion**: Thinking features are only for experimental changes
  **Clarification**: Even approved features can be disabled, allowing gradual migration. The features system is about controlled adoption, not just experimentation.

# Source Reference
"Features" chapter, introductory section.

# Verification Notes
- Definition source: Direct from source text
- Confidence rationale: High -- explicit definition with examples
- Uncertainties: None
- Cross-reference status: All slugs verified
