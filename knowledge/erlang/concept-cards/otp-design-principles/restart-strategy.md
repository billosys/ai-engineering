---
# === CORE IDENTIFICATION ===
concept: Restart Strategy
slug: restart-strategy

# === CLASSIFICATION ===
category: applications-releases
subcategory: supervisors
tier: intermediate

# === PROVENANCE ===
source: "OTP Design Principles"
source_slug: otp-design-principles
authors: "Ericsson AB"
chapter: "Supervisor Behaviour"
chapter_number: null
pdf_page: null
section: "Restart Strategy"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "strategy"
  - "supervision strategy"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - supervisor-behaviour
  - supervisor-flags
extends: []
related:
  - one-for-one-strategy
  - one-for-all-strategy
  - rest-for-one-strategy
  - simple-one-for-one-supervisor
  - child-restart-type
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a restart strategy?"
  - "How do restart strategies affect child processes?"
  - "What must I know before designing a supervision tree?"
---

# Quick Definition

A restart strategy determines how a supervisor responds when a child process terminates -- specifically which other children (if any) are also terminated and restarted alongside the failed child.

# Core Definition

The restart strategy is specified by the `strategy` key in the supervisor flags map returned by the callback function `init`. It determines the scope of restart actions when a child process terminates. The four strategies are: `one_for_one` (only the terminated child is restarted), `one_for_all` (all children are terminated and restarted), `rest_for_one` (the terminated child and all children started after it are terminated and restarted), and `simple_one_for_one` (a simplified variant for dynamic homogeneous children). The `strategy` key is optional and defaults to `one_for_one`. (Source: sup_princ.md, "Restart Strategy")

# Prerequisites

- **[Supervisor Behaviour](/concept-cards/otp-design-principles/supervisor-behaviour.md)** -- Restart strategies are a property of supervisors.
- **[Supervisor Flags](/concept-cards/otp-design-principles/supervisor-flags.md)** -- The strategy is set via the `strategy` key in supervisor flags.

# Key Properties

1. **Four variants**: `one_for_one`, `one_for_all`, `rest_for_one`, and `simple_one_for_one`.
2. **Default**: `one_for_one` if not specified.
3. **Scope of impact**: Determines which sibling processes are affected by a child failure.
4. **Interacts with restart type**: The diagrams in the source assume `permanent` restart type for all children. `temporary` children are never restarted even under `one_for_all` or `rest_for_one`.

# Construction / Recognition

## To Construct/Create:
1. Choose the appropriate strategy based on dependency relationships between children.
2. Set it in the supervisor flags map: `#{strategy => one_for_one, ...}`.

## To Identify/Recognize:
1. Look for the `strategy` key in the supervisor flags map.
2. The value is one of the four atoms: `one_for_one`, `one_for_all`, `rest_for_one`, `simple_one_for_one`.

# Context & Application

The choice of restart strategy reflects the dependency structure among child processes. Use `one_for_one` when children are independent. Use `one_for_all` when all children depend on each other and none can function without the others. Use `rest_for_one` when children have a sequential dependency chain. Use `simple_one_for_one` when all children are identical dynamically-added instances.

# Examples

**Example 1** (sup_princ.md, "Example"): Setting a restart strategy:

```erlang
SupFlags = #{strategy => one_for_one, intensity => 1, period => 5}
```

**Example 2** (sup_princ.md, "Restart Strategy"): General pattern:

```erlang
SupFlags = #{strategy => Strategy, ...}
```

# Relationships

## Builds Upon
- **[Supervisor Flags](/concept-cards/otp-design-principles/supervisor-flags.md)** -- The restart strategy is one of the supervisor flags.
- **[Supervisor Behaviour](/concept-cards/otp-design-principles/supervisor-behaviour.md)** -- Strategies are a core supervisor concept.

## Enables
- **[One-for-One Strategy](/concept-cards/otp-design-principles/one-for-one-strategy.md)** -- Specific strategy variant.
- **[One-for-All Strategy](/concept-cards/otp-design-principles/one-for-all-strategy.md)** -- Specific strategy variant.
- **[Rest-for-One Strategy](/concept-cards/otp-design-principles/rest-for-one-strategy.md)** -- Specific strategy variant.
- **[Simple One-for-One Supervisor](/concept-cards/otp-design-principles/simple-one-for-one-supervisor.md)** -- Specific strategy variant.

## Related
- **[Child Restart Type](/concept-cards/otp-design-principles/child-restart-type.md)** -- The per-child restart type interacts with the supervisor-level strategy.

## Contrasts With
- None; this is the umbrella concept for all strategy variants.

# Common Errors

- **Error**: Choosing `one_for_all` when children are independent, causing unnecessary restarts.
  **Correction**: Use `one_for_one` for independent children. Reserve `one_for_all` for tightly coupled children that cannot function without each other.

# Common Confusions

- **Confusion**: The restart strategy and the child restart type are the same thing.
  **Clarification**: The restart strategy (supervisor-level) determines *which* children are restarted when one fails. The child restart type (per-child) determines *whether* a specific child is restarted at all (permanent, transient, or temporary).

# Source Reference

sup_princ.md, "Restart Strategy" section.

# Verification Notes

- Definition source: Directly from sup_princ.md, "Restart Strategy" section.
- Confidence rationale: High -- explicitly defined with all four variants enumerated.
- Uncertainties: None.
- Cross-reference status: References all four strategy-specific cards and child-restart-type.
