---
# === CORE IDENTIFICATION ===
concept: Shutdown Specification
slug: shutdown-specification

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
section: "Child Specification / shutdown"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "shutdown"
  - "shutdown()"
  - "shutdown strategy"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - child-specification
  - supervisor-behaviour
extends: []
related:
  - automatic-shutdown
  - child-restart-type
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a child specification?"
  - "How do workers and supervisors relate in a supervision tree?"
---

# Quick Definition

The shutdown specification defines how a supervisor terminates a child process -- either by unconditional kill (`brutal_kill`), by a graceful timeout, or by waiting indefinitely (`infinity`).

# Core Definition

The `shutdown` key in a child specification defines how a child process is to be terminated. `brutal_kill` means the child is unconditionally terminated using `exit_signal(Child, kill)`. An integer time-out value means the supervisor sends `exit_signal(Child, shutdown)` and waits for an exit signal back; if none is received within the specified time, the child is unconditionally killed. `infinity` gives the child unlimited time to shut down, which should be used for child supervisors and may be used for workers. The default is `5000` (milliseconds) for workers and `infinity` for supervisors. (Source: sup_princ.md, "Child Specification / shutdown")

# Prerequisites

- **[Child Specification](/concept-cards/otp-design-principles/child-specification.md)** -- Shutdown is a key in the child specification map.
- **[Supervisor Behaviour](/concept-cards/otp-design-principles/supervisor-behaviour.md)** -- Supervisors use the shutdown spec during termination.

# Key Properties

1. **`brutal_kill`**: Unconditionally terminates the child using `exit_signal(Child, kill)`. No cleanup time.
2. **Integer timeout**: Sends `exit_signal(Child, shutdown)`, waits for the specified milliseconds, then kills unconditionally if no response.
3. **`infinity`**: Waits indefinitely. Required for child supervisors to allow subtree shutdown. Allowed for workers but requires safe cleanup implementation.
4. **Default for workers**: `5000` milliseconds.
5. **Default for supervisors**: `infinity`.
6. **Reverse order**: During supervisor shutdown, children are terminated in reverse start order.

# Construction / Recognition

## To Construct/Create:
1. Set `shutdown` in the child specification:

```erlang
#{id => ch3, start => {ch3, start_link, []}, shutdown => brutal_kill}
#{id => ch4, start => {ch4, start_link, []}, shutdown => 10000}
#{id => sub_sup, start => {sub_sup, start_link, []}, type => supervisor}  % defaults to infinity
```

## To Identify/Recognize:
1. Look for the `shutdown` key in child specification maps.
2. If absent, check the `type` key to determine the default (`5000` for worker, `infinity` for supervisor).

# Context & Application

The shutdown specification controls the graceful termination behavior of child processes. It is critical for ensuring data integrity during shutdowns. Workers that need no cleanup can use `brutal_kill` for instant termination. Workers with cleanup needs should use a timeout or `infinity`. Child supervisors should always use `infinity` to prevent race conditions where a supervisor unlinks its children but fails to terminate them before being killed.

# Examples

**Example 1** (sup_princ.md, "Child Specification"): The source explains that `ch3` does not need cleaning up before termination, so `brutal_kill` is sufficient. `error_man` (an event manager) may need time for event handlers to clean up, so the default timeout of 5000 ms is used.

**Example 2** (sup_princ.md, "Child Specification"): Child supervisor using default infinity:

```erlang
#{id => sup,
  start => {sup, start_link, []},
  restart => transient,
  type => supervisor} % will cause default shutdown=>infinity
```

# Relationships

## Builds Upon
- **[Child Specification](/concept-cards/otp-design-principles/child-specification.md)** -- Shutdown is a child spec key.
- **[Supervisor Behaviour](/concept-cards/otp-design-principles/supervisor-behaviour.md)** -- Supervisors execute the shutdown procedure.

## Enables
- Graceful termination of supervision trees.
- Data integrity during process shutdown.

## Related
- **[Automatic Shutdown](/concept-cards/otp-design-principles/automatic-shutdown.md)** -- During automatic shutdown, remaining children are terminated per their shutdown specs.

## Contrasts With
- The three modes contrast with each other: `brutal_kill` vs timeout vs `infinity`.

# Common Errors

- **Error**: Setting shutdown to a finite timeout for a child supervisor.
  **Correction**: This can cause a race condition where the child supervisor unlinks its own children but fails to terminate them before being killed. Use `infinity` for child supervisors.

- **Error**: Setting shutdown to `infinity` for a worker without ensuring the worker always returns from its cleanup procedure.
  **Correction**: When using `infinity`, the entire supervision tree termination depends on this child. The cleanup must be safe and always return.

# Common Confusions

- **Confusion**: `brutal_kill` sends a `shutdown` signal.
  **Clarification**: `brutal_kill` sends a `kill` signal via `exit_signal(Child, kill)`, which cannot be trapped. A timeout sends `shutdown` first, then `kill` on timeout.

# Source Reference

sup_princ.md, "Child Specification / shutdown" section including warnings.

# Verification Notes

- Definition source: Directly from sup_princ.md, "Child Specification / shutdown" section.
- Confidence rationale: High -- explicitly defined with three modes and defaults.
- Uncertainties: None.
- Cross-reference status: References child-specification, supervisor-behaviour, automatic-shutdown.
