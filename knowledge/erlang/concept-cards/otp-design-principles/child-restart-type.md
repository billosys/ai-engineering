---
# === CORE IDENTIFICATION ===
concept: Child Restart Type
slug: child-restart-type

# === CLASSIFICATION ===
category: applications-releases
subcategory: child-specs
tier: intermediate

# === PROVENANCE ===
source: "OTP Design Principles"
source_slug: otp-design-principles
authors: "Ericsson AB"
chapter: "Supervisor Behaviour"
chapter_number: null
pdf_page: null
section: "Child Specification / restart"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "restart type"
  - "restart()"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - child-specification
  - supervisor-behaviour
extends: []
related:
  - restart-strategy
  - significant-child
  - maximum-restart-intensity
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What distinguishes permanent, transient, and temporary restart types?"
  - "How do restart strategies affect child processes?"
---

# Quick Definition

The child restart type (`permanent`, `transient`, or `temporary`) determines under what conditions a terminated child process will be restarted by its supervisor.

# Core Definition

The `restart` key in a child specification defines when a terminated child process is to be restarted. A `permanent` child process is always restarted. A `temporary` child process is never restarted (not even when the supervisor restart strategy is `rest_for_one` or `one_for_all` and a sibling death causes the temporary process to be terminated). A `transient` child process is restarted only if it terminates abnormally, that is, with an exit reason other than `normal`, `shutdown`, or `{shutdown, Term}`. The `restart` key is optional and defaults to `permanent`. (Source: sup_princ.md, "Child Specification / restart")

# Prerequisites

- **[Child Specification](/concept-cards/otp-design-principles/child-specification.md)** -- The restart type is a key in the child specification.
- **[Supervisor Behaviour](/concept-cards/otp-design-principles/supervisor-behaviour.md)** -- Only supervisors interpret the restart type.

# Key Properties

1. **`permanent`** (default): Always restarted, regardless of exit reason.
2. **`transient`**: Restarted only on abnormal termination (exit reason other than `normal`, `shutdown`, or `{shutdown, Term}`).
3. **`temporary`**: Never restarted, even when strategy-caused termination occurs under `one_for_all` or `rest_for_one`.
4. **Per-child setting**: Each child in a supervisor can have a different restart type.
5. **Interacts with strategy**: Under `one_for_all` and `rest_for_one`, temporary children are terminated but not restarted.

# Construction / Recognition

## To Construct/Create:
1. Set `restart => permanent | transient | temporary` in the child specification.
2. Omit the key to use the default value `permanent`.

```erlang
#{id => my_worker, start => {my_mod, start_link, []}, restart => transient}
```

## To Identify/Recognize:
1. Look for the `restart` key in child specification maps.
2. If absent, the child is `permanent` by default.

# Context & Application

- **permanent**: Use for long-running services that should always be available (e.g., database connection managers, core application servers).
- **transient**: Use for processes that are expected to terminate normally when their task is done, but should be restarted if they crash (e.g., one-shot workers, task processors).
- **temporary**: Use for processes that should never be restarted (e.g., disposable tasks, one-time initialization processes).

# Examples

**Example 1** (sup_princ.md, "Child Specification"): Permanent child (explicit):

```erlang
#{id => ch3,
  start => {ch3, start_link, []},
  restart => permanent,
  shutdown => brutal_kill,
  type => worker,
  modules => [ch3]}
```

**Example 2** (sup_princ.md, "Child Specification"): Transient child supervisor:

```erlang
#{id => sup,
  start => {sup, start_link, []},
  restart => transient,
  type => supervisor}
```

**Example 3** (sup_princ.md, "Child Specification"): The source notes that both the server `ch3` and event manager `error_man` "are registered processes which can be expected to be always accessible. Thus they are specified to be `permanent`."

# Relationships

## Builds Upon
- **[Child Specification](/concept-cards/otp-design-principles/child-specification.md)** -- Restart type is a child spec key.

## Enables
- **[Significant Child](/concept-cards/otp-design-principles/significant-child.md)** -- Only `transient` or `temporary` children can be significant.
- Fine-grained control over which children are restarted.

## Related
- **[Restart Strategy](/concept-cards/otp-design-principles/restart-strategy.md)** -- The supervisor-level strategy determines *which* children are affected; the restart type determines *whether* each is restarted.
- **[Maximum Restart Intensity](/concept-cards/otp-design-principles/maximum-restart-intensity.md)** -- Only actual restarts count toward the intensity limit.

## Contrasts With
- The three types contrast with each other: `permanent` vs `transient` vs `temporary`.

# Common Errors

- **Error**: Expecting a `temporary` child to be restarted under `one_for_all` when a sibling crashes.
  **Correction**: Temporary children are never restarted, even when terminated as part of `one_for_all` or `rest_for_one` cascading.

- **Error**: Using `permanent` for a child that is meant to complete a task and exit normally.
  **Correction**: Use `transient` for children expected to exit normally. A `permanent` child that exits normally will be immediately restarted, which is likely not desired.

# Common Confusions

- **Confusion**: `transient` children are restarted if they exit with reason `shutdown`.
  **Clarification**: `transient` children are only restarted on abnormal termination. The reasons `normal`, `shutdown`, and `{shutdown, Term}` are all considered normal and do not trigger a restart.

- **Confusion**: The restart type and the restart strategy are the same concept.
  **Clarification**: The restart type is per-child and controls *whether* a child is restarted. The restart strategy is per-supervisor and controls *which* children are affected by a failure.

# Source Reference

sup_princ.md, "Child Specification / restart" section.

# Verification Notes

- Definition source: Directly quoted from sup_princ.md.
- Confidence rationale: High -- all three types explicitly defined with clear semantics.
- Uncertainties: None.
- Cross-reference status: References child-specification, restart-strategy, significant-child, maximum-restart-intensity.
