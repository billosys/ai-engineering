---
# === CORE IDENTIFICATION ===
concept: Automatic Shutdown
slug: automatic-shutdown

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
section: "Automatic Shutdown"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "auto_shutdown"
  - "automatic self-shutdown"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - supervisor-behaviour
  - supervisor-flags
  - significant-child
extends: []
related:
  - child-restart-type
  - shutdown-specification
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What must I know before designing a supervision tree?"
  - "How do workers and supervisors relate in a supervision tree?"
---

# Quick Definition

Automatic shutdown is a supervisor feature that causes the supervisor to terminate itself and all remaining children when significant child processes terminate, enabling cooperative work-unit semantics.

# Core Definition

A supervisor can be configured to automatically shut itself down when significant children terminate. This is specified by the `auto_shutdown` key in the supervisor flags map. Three modes exist: `never` (default, disabled), `any_significant` (shuts down when any significant child terminates normally), and `all_significant` (shuts down when all significant children have terminated). The automatic shutdown facility only applies when significant children terminate by themselves -- not when their termination was caused by the supervisor (e.g., as a consequence of a sibling's termination in `one_for_all` or `rest_for_one`, or by manual `supervisor:terminate_child/2`). Introduced in OTP 24.0. (Source: sup_princ.md, "Automatic Shutdown")

# Prerequisites

- **[Supervisor Behaviour](/concept-cards/otp-design-principles/supervisor-behaviour.md)** -- Automatic shutdown is a supervisor feature.
- **[Supervisor Flags](/concept-cards/otp-design-principles/supervisor-flags.md)** -- Configured via the `auto_shutdown` key.
- **[Significant Child](/concept-cards/otp-design-principles/significant-child.md)** -- Requires at least one child marked as significant.

# Key Properties

1. **Three modes**: `never` (default), `any_significant`, `all_significant`.
2. **Cooperative work units**: Useful when a supervisor represents cooperating children that form a work unit.
3. **Self-termination only**: The supervisor shuts itself down by terminating all remaining children in reverse start order, then terminating itself.
4. **Excludes forced terminations**: Only self-initiated terminations of significant children trigger shutdown. Supervisor-caused terminations (strategy cascading, manual terminate_child) do not trigger it.
5. **OTP 24.0+**: Introduced in OTP 24.0; applications using it will compile on older versions but the automatic shutdowns will not occur.

# Construction / Recognition

## To Construct/Create:
1. Set `auto_shutdown` in supervisor flags:

```erlang
SupFlags = #{auto_shutdown => any_significant, ...}
```

2. Mark at least one child as significant in its child specification:

```erlang
#{id => worker1, start => {worker1, start_link, []}, significant => true, restart => transient}
```

## To Identify/Recognize:
1. Look for `auto_shutdown` key in supervisor flags with value `any_significant` or `all_significant`.
2. Look for children with `significant => true` in their child specifications.

# Context & Application

Automatic shutdown is designed for supervisors that represent a "work unit" of cooperating children. When the work unit finishes (i.e., significant children complete), the supervisor cleans up remaining children and exits. This is preferred over having a child process manually stop its supervisor, which leads to deadlocks and coupling issues.

**Important warnings from the source:**
- Top supervisors of applications should NOT be configured for automatic shutdown, because when the top supervisor exits, the application terminates (and if permanent, all other applications and the runtime system too).
- Supervisors with automatic shutdown should NOT be permanent children of their parent, as they would be immediately restarted only to shut down again, exhausting the parent's restart intensity.

# Examples

**Example 1** (sup_princ.md, "Automatic Shutdown"): The `any_significant` mode shuts down when any single significant child terminates normally (transient) or normally/abnormally (temporary).

**Example 2** (sup_princ.md, "Automatic Shutdown"): The `all_significant` mode shuts down when the last active significant child terminates.

# Relationships

## Builds Upon
- **[Supervisor Flags](/concept-cards/otp-design-principles/supervisor-flags.md)** -- Auto-shutdown is a supervisor flag.
- **[Significant Child](/concept-cards/otp-design-principles/significant-child.md)** -- Automatic shutdown depends on significant child terminations.

## Enables
- Clean cooperative work-unit lifecycle management.
- Avoidance of manual supervisor stopping, which causes deadlocks.

## Related
- **[Child Restart Type](/concept-cards/otp-design-principles/child-restart-type.md)** -- Significant children must be `transient` or `temporary`, not `permanent`.
- **[Shutdown Specification](/concept-cards/otp-design-principles/shutdown-specification.md)** -- The shutdown follows standard shutdown specifications for each remaining child.

## Contrasts With
- None directly; this is a unique supervisor feature.

# Common Errors

- **Error**: Configuring automatic shutdown on the top-level application supervisor.
  **Correction**: When the top supervisor exits, the application terminates. If the application is permanent, this terminates all applications and the runtime system.

- **Error**: Making a supervisor with automatic shutdown a `permanent` child of its parent.
  **Correction**: It will be immediately restarted, shut down again, and exhaust the parent's restart intensity. Use `transient` or `temporary` restart type instead.

- **Error**: Expecting `supervisor:terminate_child/2` to trigger automatic shutdown.
  **Correction**: Manual termination does not trigger automatic shutdown. Only self-initiated terminations of significant children trigger it.

# Common Confusions

- **Confusion**: Automatic shutdown is triggered by any child termination in the `one_for_all` or `rest_for_one` cascading.
  **Clarification**: The automatic shutdown facility only applies when significant children terminate by themselves. Termination caused by the supervisor as part of `one_for_all` or `rest_for_one` strategy does not trigger it.

- **Confusion**: Setting `auto_shutdown => never` and marking children as significant is valid.
  **Clarification**: It is not valid. If `auto_shutdown` is `never`, specifying significant children is rejected -- the supervisor will refuse to start.

# Source Reference

sup_princ.md, "Automatic Shutdown" section including `never`, `any_significant`, `all_significant` subsections and warnings.

# Verification Notes

- Definition source: Directly from sup_princ.md, "Automatic Shutdown" section.
- Confidence rationale: High -- explicitly defined with detailed warnings.
- Uncertainties: None.
- Cross-reference status: References significant-child, child-restart-type, shutdown-specification, supervisor-flags.
