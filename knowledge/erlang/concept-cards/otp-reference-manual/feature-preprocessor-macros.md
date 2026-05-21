---
# === CORE IDENTIFICATION ===
concept: Feature Preprocessor Macros
slug: feature-preprocessor-macros

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
section: "Preprocessor Additions"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "FEATURE_AVAILABLE macro"
  - "FEATURE_ENABLED macro"
  - "feature macros"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - erlang-feature-concept
  - feature-lifecycle
extends: []
related:
  - feature-enablement
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I conditionally compile code based on feature availability?"
  - "What preprocessor macros exist for the features system?"
  - "What is the difference between FEATURE_AVAILABLE and FEATURE_ENABLED?"
---

# Quick Definition
The features system provides two predefined preprocessor macros: `?FEATURE_AVAILABLE(Feature)` to check if a feature exists in the current OTP release, and `?FEATURE_ENABLED(Feature)` to check if a feature is currently enabled. These enable conditional compilation during code transitioning.

# Core Definition
The Erlang Reference Manual states: "To allow for conditional compilation during transitioning of a code base and/or trying out experimental features feature predefined macros `?FEATURE_AVAILABLE(Feature)` and `?FEATURE_ENABLED(Feature)` are available." (Features, "Preprocessor Additions"). `FEATURE_AVAILABLE` checks whether a feature exists in the current release (regardless of whether it is enabled). `FEATURE_ENABLED` checks whether the feature is currently enabled during compilation.

# Prerequisites
- **erlang-feature-concept** -- Must understand what features are
- **feature-lifecycle** -- Must understand availability vs. enablement

# Key Properties
1. `?FEATURE_AVAILABLE(Feature)` -- true if the feature exists in the current OTP release
2. `?FEATURE_ENABLED(Feature)` -- true if the feature is currently enabled
3. Both are predefined macros usable with `-ifdef`/`-ifndef` directives
4. Designed for conditional compilation during code base transitions
5. A feature is "available" if it is not in the Rejected state
6. A feature is "enabled" if it is in a state where it is active (Approved/Permanent, or Experimental when explicitly enabled)

# Construction / Recognition
## Using FEATURE_AVAILABLE:
```erlang
-ifdef(FEATURE_AVAILABLE(maybe_expr)).
  %% Code that can use maybe_expr, or provide feature-aware logic
-endif.
```

## Using FEATURE_ENABLED:
```erlang
-ifdef(FEATURE_ENABLED(maybe_expr)).
  %% Code that uses the maybe expression
-else.
  %% Fallback code for when the feature is not enabled
-endif.
```

# Context & Application
These macros are essential for maintaining codebases that must work across multiple OTP versions or that are gradually adopting new features. They allow the same source file to compile correctly whether or not a feature is available or enabled, without requiring separate source branches.

# Examples
**Example 1** (Preprocessor Additions):
```erlang
-ifdef(FEATURE_AVAILABLE(maybe_expr)).
  -feature(maybe_expr, enable).
  %% Use maybe expression syntax
-else.
  %% Use nested case expressions as fallback
-endif.
```

**Example 2** (Checking feature state programmatically):
The `erl_features` module and `erlc` options also provide feature information:
```
erlc -list-features
erlc -describe-feature maybe_expr
```

# Relationships
## Builds Upon
- **erlang-feature-concept** -- The macros operate on features
- **feature-lifecycle** -- Availability and enablement depend on the feature's state

## Enables
Writing cross-version compatible code that adapts to feature availability.

## Related
- **feature-enablement** -- The macros complement the enablement mechanism

## Contrasts With
None.

# Common Errors
- **Error**: Using `?FEATURE_ENABLED` when `?FEATURE_AVAILABLE` is intended
  **Correction**: `FEATURE_AVAILABLE` checks if the feature exists in the release. `FEATURE_ENABLED` checks if it is currently enabled. Use `AVAILABLE` to detect the OTP version; use `ENABLED` to check if the feature is active.

# Common Confusions
- **Confusion**: Thinking `FEATURE_AVAILABLE` means the feature is enabled
  **Clarification**: A feature can be available but disabled (e.g., an experimental feature that has not been explicitly enabled). `FEATURE_AVAILABLE` only confirms the feature exists in the current OTP release.

# Source Reference
"Features" chapter, "Preprocessor Additions" section.

# Verification Notes
- Definition source: Direct from source text
- Confidence rationale: High -- explicit macro names and purpose described
- Uncertainties: Exact preprocessor syntax for using these macros (whether they work with -ifdef or as boolean expressions) is inferred from standard Erlang preprocessor conventions
- Cross-reference status: All slugs verified
