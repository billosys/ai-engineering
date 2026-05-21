---
# === CORE IDENTIFICATION ===
concept: Feature Lifecycle
slug: feature-lifecycle

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
section: "Life cycle of features"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "feature states"
  - "feature lifecycle states"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - erlang-feature-concept
extends: []
related:
  - feature-enablement
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What states can an Erlang feature be in?"
  - "How does a feature progress from experimental to permanent?"
  - "Can a feature be rejected after being experimental?"
  - "What determines if a feature can be enabled or disabled?"
---

# Quick Definition
An Erlang feature progresses through a defined lifecycle: Experimental (disabled by default, configurable), Approved (enabled by default, configurable), Permanent (always enabled, not configurable), or Rejected (removed, not available). State changes only occur in connection with a release.

# Core Definition
The Erlang Reference Manual defines four feature states (Features, "Life cycle of features"): "**Experimental** - The initial state is meant for trying out and collecting feedback. The feature can be enabled but is disabled by default." "**Approved** - The feature has been finalised and is now part of OTP. By default, it is enabled, but can be disabled." "**Permanent** - The feature is now a permanent part of OTP. It can no longer be disabled." "**Rejected** - The feature never reached the approved state and will not be part of OTP. It cannot be enabled." After leaving the experimental state, a feature can enter any of the other three states. If approved, it will eventually become permanent. A feature can change state only in connection with a release, and may be in the approved state for several releases.

# Prerequisites
- **erlang-feature-concept** -- Must understand what features are

# Key Properties
1. Four states: Experimental, Approved, Permanent, Rejected
2. Experimental: disabled by default, configurable, available
3. Approved: enabled by default, configurable, available
4. Permanent: enabled by default, not configurable, available
5. Rejected: disabled by default, not configurable, not available
6. State changes only occur with OTP releases
7. From Experimental, a feature can go to Approved, Permanent, or Rejected
8. A feature may remain Approved for several releases before becoming Permanent
9. Availability can be checked with `?FEATURE_AVAILABLE(Feature)` macro

# Construction / Recognition
## To Determine Feature State:
1. Use `erlc -list-features` to see features and their states
2. Use `erlc -describe-feature <feature>` for detailed status
3. Use `erl_features` module functions programmatically
4. Use `?FEATURE_AVAILABLE(Feature)` macro for conditional compilation

## State Transition Rules:
```
Experimental -> Approved -> Permanent
Experimental -> Permanent  (skip Approved)
Experimental -> Rejected
```

# Context & Application
The lifecycle provides a controlled pathway for language evolution. Experimental features allow the community to try changes and provide feedback before committing. The Approved state allows gradual adoption across codebases. The distinction between configurable and non-configurable states ensures that permanent features cannot be accidentally disabled, while still giving flexibility during the transition period.

# Examples
**Example 1** (Features, "Life cycle of features" -- state table):

| State        | Default  | Configurable | Available |
| ------------ | -------- | ------------ | --------- |
| Experimental | disabled | yes          | yes       |
| Approved     | enabled  | yes          | yes       |
| Permanent    | enabled  | no           | yes       |
| Rejected     | disabled | no           | no        |

**Example 2** (Features, "Existing Features"):
- `maybe_expr`: Started as experimental, approved in OTP 27
- `compr_assign`: Currently experimental

# Relationships
## Builds Upon
- **erlang-feature-concept** -- The lifecycle applies to selectable features

## Enables
- **feature-enablement** -- Configurable states allow enabling/disabling

## Related
None.

## Contrasts With
None.

# Common Errors
- **Error**: Assuming an experimental feature will always become approved
  **Correction**: Experimental features can be rejected and removed entirely. Do not rely on experimental features in production code.

- **Error**: Trying to disable a permanent feature
  **Correction**: Permanent features cannot be disabled. They are a fixed part of OTP.

# Common Confusions
- **Confusion**: Thinking "approved" means "permanent"
  **Clarification**: An approved feature is enabled by default but can still be disabled. It may remain in the approved state for several releases before becoming permanent.

- **Confusion**: Thinking state transitions happen mid-release
  **Clarification**: A feature can change state only in connection with a release.

# Source Reference
"Features" chapter, "Life cycle of features" section.

# Verification Notes
- Definition source: Direct from source text including the state table
- Confidence rationale: High -- explicit state definitions and transition rules
- Uncertainties: None
- Cross-reference status: All slugs verified
