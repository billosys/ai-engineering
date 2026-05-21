---
# === CORE IDENTIFICATION ===
concept: Supervisor Flags
slug: supervisor-flags

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
section: "Supervisor Flags"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "sup_flags()"
  - "SupFlags"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - supervisor-behaviour
extends: []
related:
  - restart-strategy
  - maximum-restart-intensity
  - automatic-shutdown
  - child-specification
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I define a supervisor with child specifications?"
  - "What must I know before designing a supervision tree?"
---

# Quick Definition

Supervisor flags are a map returned from `init/1` that configures the supervisor's restart strategy, maximum restart intensity, and automatic shutdown behavior.

# Core Definition

The supervisor flags are a map (`sup_flags()`) with the following optional keys: `strategy` (default `one_for_one`) specifies the restart strategy; `intensity` (default `1`) and `period` (default `5`) specify the maximum restart intensity (maximum number of restarts in a time window); and `auto_shutdown` (default `never`) specifies whether and when a supervisor should automatically shut itself down. All keys are optional and have defaults. (Source: sup_princ.md, "Supervisor Flags")

# Prerequisites

- **[Supervisor Behaviour](/concept-cards/otp-design-principles/supervisor-behaviour.md)** -- Supervisor flags are the configuration mechanism for supervisor behaviour.

# Key Properties

1. **`strategy`** (optional, default `one_for_one`): One of `one_for_all`, `one_for_one`, `rest_for_one`, or `simple_one_for_one`.
2. **`intensity`** (optional, default `1`): Maximum number of restarts (`MaxR`) allowed in the `period`.
3. **`period`** (optional, default `5`): Time window in seconds (`MaxT`) for counting restarts.
4. **`auto_shutdown`** (optional, default `never`): One of `never`, `any_significant`, or `all_significant`.
5. **All keys optional**: An empty map `#{}` is valid and uses all defaults.

# Construction / Recognition

## To Construct/Create:
1. Build a map with the desired keys. For example: `#{strategy => one_for_one, intensity => 1, period => 5}`.
2. Return it as the first element of the tuple in `init/1`: `{ok, {SupFlags, ChildSpecs}}`.
3. Omit any keys to use their defaults.

## To Identify/Recognize:
1. Look for the `SupFlags` variable in the `init/1` return value.
2. It is always a map (in modern OTP) with keys from `{strategy, intensity, period, auto_shutdown}`.

# Context & Application

Supervisor flags are set once during supervisor initialization and govern the supervisor's overall behavior policy. The strategy determines how sibling failures are handled, while intensity and period create a safety valve against cascading restarts. The auto_shutdown flag enables cooperative work-unit semantics where a supervisor shuts down when its significant children finish.

# Examples

**Example 1** (sup_princ.md, "Example"): Full supervisor flags:

```erlang
SupFlags = #{strategy => one_for_one, intensity => 1, period => 5}
```

**Example 2** (sup_princ.md, "Supervisor Flags"): Type definition:

```erlang
sup_flags() = #{strategy => strategy(),           % optional
                intensity => non_neg_integer(),   % optional
                period => pos_integer(),          % optional
                auto_shutdown => auto_shutdown()} % optional
```

# Relationships

## Builds Upon
- **[Supervisor Behaviour](/concept-cards/otp-design-principles/supervisor-behaviour.md)** -- Flags configure the supervisor behaviour.

## Enables
- **[Restart Strategy](/concept-cards/otp-design-principles/restart-strategy.md)** -- The `strategy` key selects the restart strategy.
- **[Maximum Restart Intensity](/concept-cards/otp-design-principles/maximum-restart-intensity.md)** -- The `intensity` and `period` keys configure it.
- **[Automatic Shutdown](/concept-cards/otp-design-principles/automatic-shutdown.md)** -- The `auto_shutdown` key enables it.

## Related
- **[Child Specification](/concept-cards/otp-design-principles/child-specification.md)** -- SupFlags and ChildSpecs are returned together from `init/1`.

## Contrasts With
- None directly.

# Common Errors

- **Error**: Using a tuple or proplist instead of a map for supervisor flags (legacy format).
  **Correction**: Modern OTP uses maps for supervisor flags. Use `#{strategy => ..., intensity => ..., period => ...}`.

# Common Confusions

- **Confusion**: All supervisor flag keys are mandatory.
  **Clarification**: All keys are optional with sensible defaults: `strategy` defaults to `one_for_one`, `intensity` to `1`, `period` to `5`, and `auto_shutdown` to `never`. An empty map `#{}` is valid.

# Source Reference

sup_princ.md, "Supervisor Flags" section with type definition.

# Verification Notes

- Definition source: Directly from sup_princ.md, "Supervisor Flags" section.
- Confidence rationale: High -- explicitly defined with full type specification.
- Uncertainties: None.
- Cross-reference status: References restart-strategy, maximum-restart-intensity, automatic-shutdown.
