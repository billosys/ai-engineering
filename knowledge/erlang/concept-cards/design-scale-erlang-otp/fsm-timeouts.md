---
# === CORE IDENTIFICATION ===
concept: FSM Timeouts
slug: fsm-timeouts

# === CLASSIFICATION ===
category: otp-behaviours
subcategory: fsm
tier: intermediate

# === PROVENANCE ===
source: Designing for Scalability with Erlang/OTP
source_slug: design-scale-erlang-otp
authors: Francesco Cesarini & Steve Vinoski
chapter: "Finite State Machines"
chapter_number: 5
pdf_page: 154
section: "Timeouts"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - state timeout
  - FSM timeout
  - timeout event

# === TYPED RELATIONSHIPS ===
prerequisites:
  - fsm-states-and-state-functions
  - fsm-state-transitions
extends: []
related:
  - fsm-events
contrasts_with:
  - init-timeout

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I implement a finite state machine with gen_statem?"
  - "What is a finite state machine behavior (gen_statem)?"
---

# Quick Definition

An FSM timeout is a millisecond value (or `infinity`) returned alongside a state transition; if no event arrives within that time, a `timeout` event is delivered to the FSM's current state.

# Core Definition

"Timeouts can be specified within the FSM as an integer in milliseconds or as the atom `infinity`. We can include them in the `init/1` and `State` callback functions. When a timeout is triggered, the event is sent to the state the FSM is currently in" (Cesarini & Vinoski, p. 154). The timeout is the optional fourth element of a `{next_state, NextState, NewLoopData, Timeout}` tuple. When it fires, the FSM's state callback receives a `timeout` event, which is handled like any other event — e.g., `State(timeout, LoopData)`. In place of a timeout value, the callback may return `hibernate` to reduce the FSM's memory footprint, though hibernation should be used only when events are not expected for a while and benchmarks show memory issues (p. 155).

# Prerequisites

- **FSM states and state functions** — A timeout is handled by a state callback receiving a `timeout` event.
- **FSM state transitions** — The timeout is attached to a `next_state` transition tuple.

# Key Properties

1. Specified as an integer of milliseconds or the atom `infinity`.
2. Set as the fourth element of `{next_state, NextState, NewLoopData, Timeout}`.
3. Can be set from `init/1` and from any state callback.
4. If no event arrives within `Timeout`, a `timeout` event is sent to the current state.
5. The `timeout` event is handled by an ordinary state callback clause, e.g., `State(timeout, LoopData)`.
6. `hibernate` can be returned in the timeout's place to reduce memory footprint.

# Construction / Recognition

## To Add a Timeout to a State:
1. Define a timeout constant, e.g., `-define(TIMEOUT, 10000).`.
2. Return `{next_state, NextState, NewLoopData, ?TIMEOUT}` from the transitions into that state.
3. Add a `State(timeout, LoopData)` clause to handle expiry.

# Context & Application

- **Typical contexts**: States that must not wait indefinitely for the next event.
- **Common applications**: The coffee machine's *payment* state — if a customer takes longer than 10 seconds between coin insertions, the selection is canceled and money returned.
- **Historical/stylistic notes**: The book humorously frames the payment timeout as "punishment and revenge" against slow customers (p. 154).

# Examples

**Example 1** (p. 155): Refactoring the *payment* state with a 10-second timeout:

```erlang
-define(TIMEOUT, 10000).
...
payment({pay, Coin}, {Type,Price,Paid}) when Coin+Paid < Price ->
    ...
    {next_state, payment, {Type, Price, NewPaid}, ?TIMEOUT};
payment(timeout, {Type, Price, Paid}) ->
    hw:display("Make Your Selection", []),
    hw:return_change(Paid),
    {next_state, selection, []};
```

# Relationships

## Builds Upon
- **FSM states and state functions** — A timeout is delivered as an event to a state callback.
- **FSM state transitions** — The timeout rides on a `next_state` transition tuple.

## Enables
- *(No downstream concepts in this scope.)*

## Related
- **FSM events** — A timeout becomes a `timeout` event handled like any other.

## Contrasts With
- **Behavior init timeout** — The `{timeout, Timeout}` *start option* bounds the `init` callback once; an FSM state timeout is set per transition and fires repeatedly in a running FSM.

# Common Errors

- **Error**: Setting a state timeout but forgetting to add a `State(timeout, LoopData)` clause.
  **Correction**: Always handle the `timeout` event explicitly in any state that sets a timeout, or it falls through to the catch-all and is silently ignored.

# Common Confusions

- **Confusion**: Confusing the FSM state timeout with the `{timeout, Timeout}` start option.
  **Clarification**: The start option limits `init/1`; the state timeout limits how long the FSM waits for the next event while running.

# Source Reference

Chapter 5: Finite State Machines, Section "Timeouts," pages 154-156.

# Verification Notes

- Definition source: Direct quote from p. 154.
- Confidence rationale: HIGH — the source explicitly defines timeouts and gives a worked refactoring example.
- Uncertainties: None.
- Cross-reference status: Verified against planned cards in this batch.
- Re-extraction notes: Fresh extraction; no pre-existing card for this source.
