---
# === CORE IDENTIFICATION ===
concept: Supervised Event Handlers
slug: supervised-event-handlers

# === CLASSIFICATION ===
category: fault-tolerance
subcategory: event-handling
tier: advanced

# === PROVENANCE ===
source: Designing for Scalability with Erlang/OTP
source_slug: design-scale-erlang-otp
authors: Francesco Cesarini & Steve Vinoski
chapter: "Event Handlers"
chapter_number: 6
pdf_page: 177
section: "Handling Errors and Invalid Return Values"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "add_sup_handler"
  - "gen_event:add_sup_handler"
  - "gen_event_EXIT"
  - supervised handlers

# === TYPED RELATIONSHIPS ===
prerequisites:
  - event-handler
  - notifying-events
extends:
  - event-handler
related:
  - event-manager
contrasts_with:
  - event-handler

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is an event handler (gen_event)?"
  - "How do I monitor a production system and provide preemptive support?"
---

# Quick Definition

A supervised event handler is one added with `gen_event:add_sup_handler/3`, which sets up two-way monitoring so the adding process is notified with a `{gen_event_EXIT, Mod, Reason}` message if the handler fails — instead of failing silently.

# Core Definition

By default, an abnormal termination in any handler callback "result[s] in deletion. The event manager and other handlers are not affected. This differs from other behaviors in that the event handler is silently removed, without any notifications being sent to the event manager's supervisor" (Cesarini & Vinoski, p. 177). The event manager itself traps exits by default, so a handler crash generates an error report but no exit signal — "Sending notifications can fail silently." The fix: "You get around this problem by connecting a handler to the calling process using `gen_event:add_sup_handler/3`. It works in the same way as `add_handler/3`, with the side effect that the calling process is now monitoring the handler, and the calling process is being monitored by the newly added instance of the handler" (p. 178). If a callback raises an exception or returns an incorrect value, a `{gen_event_EXIT, Mod, Reason}` message is sent to the adding process. Monitoring goes both ways: if the adding process terminates, the handler is removed with `{stop, Reason}`.

# Prerequisites

- **Event handler** — Supervised handlers are ordinary handlers added with extra monitoring.
- **Notifying events** — Silent failure occurs during event notification, which this card mitigates.

# Key Properties

1. Added with `gen_event:add_sup_handler/3`, otherwise identical to `add_handler/3`.
2. Sets up *two-way* monitoring between the adding process and the handler.
3. On callback exception or invalid return, the adding process receives `{gen_event_EXIT, Mod, Reason}`.
4. `Reason` is `normal` (callback returned `remove_handler` or `delete_handler/3` used), `shutdown` (manager stopped), `{'EXIT', Term}` (runtime error), a plain `Term` (invalid return value), or `{swapped, NewMod, Pid}`.
5. If the adding process terminates, the handler is removed with `{stop, Reason}`.
6. Two-way monitoring prevents duplicate handler instances when added by a behavior stuck in a cyclic restart.

# Construction / Recognition

## To Add a Supervised Handler:
1. Call `gen_event:add_sup_handler(Manager, Mod, Args)` from the process that should be notified of failures.
2. Pattern match the return value to confirm the handler was added.
3. Have the adding process receive `{gen_event_EXIT, Mod, Reason}` messages and react.

# Context & Application

- **Typical contexts**: High-availability systems where a silently deleted handler is unacceptable.
- **Common applications**: Alarm and monitoring handlers — "You don't want your alarm system to fail without raising any alarms!"
- **Historical/stylistic notes**: The "Fail Loudly!" sidebar urges always checking the return value of `add_handler/3`/`add_sup_handler/3` and wrapping fallible `init/1` code in `try`-`catch` (p. 178).

# Examples

**Example 1** (pp. 177-178): With a plain `add_handler/3`, notifying a crashing handler produces an `=ERROR REPORT=` ("gen_event handler crash_example crashed") but no exit signal — `which_handlers(P)` then shows `[]`, the handler silently gone.

**Example 2** (p. 181-183): `freq_overload:add/2` uses `gen_event:add_sup_handler/3` so another process can monitor the handlers; `freq_overload:start_link/0` itself uses the plain `add/2` wrapper to re-add `counters` and `logger` on restart.

# Relationships

## Builds Upon
- **Event handler** — A supervised handler is an event handler with monitoring added.

## Enables
- *(No downstream concepts in this scope.)*

## Related
- **event-manager** — The handler runs in the manager; monitoring links the manager-resident handler to the adding process.

## Contrasts With
- **Event handler** — A plainly added handler fails silently on a callback crash; a supervised handler notifies its adder with `{gen_event_EXIT, Mod, Reason}`.

# Common Errors

- **Error**: Adding a handler with `add_handler/3` in a fault-tolerant system and ignoring its return value.
  **Correction**: Prefer `add_sup_handler/3`, pattern match on the return value, and handle `{gen_event_EXIT, ...}` messages; wrap fallible `init/1` code in `try`-`catch`.

# Common Confusions

- **Confusion**: Thinking a handler crash will surface through the event manager's supervisor.
  **Clarification**: The manager traps exits and silently deletes a crashed handler; only `add_sup_handler/3` makes the failure visible, via `{gen_event_EXIT, ...}` to the adding process.

# Source Reference

Chapter 6: Event Handlers, Section "Handling Errors and Invalid Return Values," pages 177-179. See Figure 7-7 and the "Fail Loudly!" sidebar.

# Verification Notes

- Definition source: Direct quotes from pp. 177-178.
- Confidence rationale: HIGH — the source explicitly defines `add_sup_handler/3`, the two-way monitoring, and every `Reason` value.
- Uncertainties: None.
- Cross-reference status: Verified against planned cards in this batch.
- Re-extraction notes: Fresh extraction; no pre-existing card for this source.
