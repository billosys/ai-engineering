---
# === CORE IDENTIFICATION ===
concept: Significant Child
slug: significant-child

# === CLASSIFICATION ===
category: applications-releases
subcategory: supervisors
tier: advanced

# === PROVENANCE ===
source: "OTP Design Principles"
source_slug: otp-design-principles
authors: "Ericsson AB"
chapter: "Supervisor Behaviour"
chapter_number: null
pdf_page: null
section: "Child Specification / significant"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "significant children"
  - "significant flag"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - child-specification
  - automatic-shutdown
  - child-restart-type
extends: []
related:
  - supervisor-flags
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What must I know before designing a supervision tree?"
---

# Quick Definition

A significant child is a child process marked with `significant => true` in its child specification, whose termination can trigger the supervisor's automatic shutdown.

# Core Definition

The `significant` key in a child specification defines whether a child is considered significant for automatic self-shutdown of the supervisor. It is invalid to set this option to `true` for a child with restart type `permanent` or in a supervisor with `auto_shutdown` set to `never`. When a significant child terminates by itself (not due to supervisor-initiated termination), it may trigger the supervisor's automatic shutdown depending on the `auto_shutdown` mode. (Source: sup_princ.md, "Child Specification / significant")

# Prerequisites

- **[Child Specification](/concept-cards/otp-design-principles/child-specification.md)** -- `significant` is a key in the child specification map.
- **[Automatic Shutdown](/concept-cards/otp-design-principles/automatic-shutdown.md)** -- Significant children are meaningful only when automatic shutdown is enabled.
- **[Child Restart Type](/concept-cards/otp-design-principles/child-restart-type.md)** -- Significant children must be `transient` or `temporary`, not `permanent`.

# Key Properties

1. **Boolean flag**: `significant => true` or `significant => false` (default).
2. **Requires non-permanent restart type**: Cannot be `true` for `permanent` children.
3. **Requires auto_shutdown**: Cannot be `true` when `auto_shutdown => never`.
4. **Self-termination only**: Only triggers automatic shutdown when the child terminates by itself, not when terminated by the supervisor.
5. **Triggers shutdown**: Under `any_significant`, any significant child termination triggers shutdown. Under `all_significant`, the last active significant child's termination triggers shutdown.

# Construction / Recognition

## To Construct/Create:
1. Set `significant => true` in the child specification.
2. Ensure the child's restart type is `transient` or `temporary`.
3. Ensure the supervisor's `auto_shutdown` is `any_significant` or `all_significant`.

```erlang
#{id => worker1,
  start => {worker1, start_link, []},
  restart => transient,
  significant => true}
```

## To Identify/Recognize:
1. Look for `significant => true` in child specification maps.

# Context & Application

Significant children are the mechanism through which automatic shutdown is triggered. In a work-unit supervision pattern, some children represent the primary task (significant) while others are supporting infrastructure. When the primary task completes (significant children terminate), the supervisor automatically cleans up the supporting processes.

# Examples

**Example 1** (sup_princ.md, "Child Specification / significant"): A transient significant child -- when it terminates normally, it can trigger automatic shutdown:

```erlang
#{id => primary_worker,
  start => {primary_worker, start_link, []},
  restart => transient,
  significant => true}
```

# Relationships

## Builds Upon
- **[Child Specification](/concept-cards/otp-design-principles/child-specification.md)** -- Significant is a child spec key.
- **[Automatic Shutdown](/concept-cards/otp-design-principles/automatic-shutdown.md)** -- Significant children drive automatic shutdown decisions.

## Enables
- Automatic supervisor self-shutdown when work units complete.

## Related
- **[Child Restart Type](/concept-cards/otp-design-principles/child-restart-type.md)** -- Only `transient` or `temporary` children can be significant.

## Contrasts With
- None directly.

# Common Errors

- **Error**: Marking a `permanent` child as significant.
  **Correction**: Permanent children are always restarted, so they never "finish." Only `transient` or `temporary` children can be significant.

- **Error**: Marking a child as significant in a supervisor with `auto_shutdown => never`.
  **Correction**: The supervisor will refuse to start or reject the dynamic child addition. Set `auto_shutdown` to `any_significant` or `all_significant`.

# Common Confusions

- **Confusion**: Stopping a significant child with `supervisor:terminate_child/2` triggers automatic shutdown.
  **Clarification**: Manual termination via `supervisor:terminate_child/2` does not trigger automatic shutdown. Only self-initiated terminations count.

# Source Reference

sup_princ.md, "Child Specification / significant" and "Automatic Shutdown" sections.

# Verification Notes

- Definition source: Directly from sup_princ.md, "Child Specification" section, `significant` key description.
- Confidence rationale: High -- explicitly defined with clear constraints.
- Uncertainties: None.
- Cross-reference status: References child-specification, automatic-shutdown, child-restart-type.
