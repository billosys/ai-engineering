---
concept: FSM Monitor Integration
slug: fsm-monitor-integration
category: otp-behaviours
subcategory: state-machines
tier: advanced
source: "Learn You Some Erlang for Great Good!"
source_slug: learn-you-some-erlang
authors: "Fred Hébert"
chapter: "Rage Against the Finite-State Machines"
chapter_number: 15
pdf_page: null
section: "The gen_fsm Callbacks"
extraction_confidence: high
aliases:
  - FSM monitors
  - "handle_info DOWN"
  - peer-death handling
prerequisites:
  - gen-fsm
  - finite-state-machine
extends: []
related:
  - fsm-handle-event
  - gen-fsm
contrasts_with: []
answers_questions:
  - "What is a finite-state-machine behaviour (gen_fsm / gen_statem)?"
  - "How do I implement a stateful process?"
---

# FSM Monitor Integration

## Quick Definition

When an FSM depends on a peer process, it sets a monitor on that peer and handles the resulting `'DOWN'` message in `handle_info/3`, terminating cleanly if the peer dies.

## Core Definition

The `trade_fsm` sets up a monitor when it first learns of the other player's pid: `Ref = monitor(process, OtherPid)` in the `idle` state, storing the reference in its state data. "The last event to take care of is when the other FSM goes down. Fortunately, we set a monitor back in the `idle` state. We can match on this and react accordingly" (Ch. 15, "The gen_fsm Callbacks").

## Prerequisites

- **gen_fsm** — The monitor's `'DOWN'` message arrives via `handle_info/3`.
- **finite-state-machine** — The pattern applies to FSMs depending on peers.

## Key Properties

1. The FSM calls `monitor(process, PeerPid)` when it learns of the peer.
2. The monitor reference is stored in the FSM's state data.
3. A peer's death produces a `{'DOWN', Ref, process, Pid, Reason}` message.
4. That message is delivered to the FSM's `handle_info/3` callback.
5. The FSM matches the `Ref`/`Pid` against its stored values and returns `{stop, {other_down, Reason}, S}`.
6. Monitors are chosen over links because they can be set up unilaterally and stacked.

## Construction / Recognition

## To Integrate Monitors into an FSM

1. When the FSM obtains a peer pid, call `monitor(process, PeerPid)`.
2. Store the returned reference in the state data record.
3. Implement `handle_info({'DOWN', Ref, process, Pid, Reason}, _, S)` matching the stored `Ref`/`Pid`.
4. Return `{stop, ...}` so the FSM terminates cleanly when the peer is gone.

## Context & Application

In `trade_fsm`, both `idle/2` and `idle/3` set up the monitor before moving to `idle_wait`: "A monitor is set up to allow us to handle the other dying." The `handle_info/3` clause stops the FSM with `{other_down, Reason}`. The book notes that even if the peer dies mid-commit, "everything should be safe, and the players will still have their own items."

## Examples

**Example 1** (Ch. 15): `idle({ask_negotiate, OtherPid}, S) -> Ref = monitor(process, OtherPid), ... {next_state, idle_wait, S#state{other=OtherPid, monitor=Ref}}.`

**Example 2** (Ch. 15): `handle_info({'DOWN', Ref, process, Pid, Reason}, _, S=#state{other=Pid, monitor=Ref}) -> notice(S, "Other side dead", []), {stop, {other_down, Reason}, S}.`

## Relationships

## Builds Upon

- **gen_fsm** — `'DOWN'` messages arrive through `handle_info/3`.

## Related

- **fsm-handle-event** — Both `handle_info/3` and the global-event callbacks handle cross-state concerns.

## Common Errors

- **Error**: Not storing the monitor reference, so the `'DOWN'` message cannot be matched.
  **Correction**: Save the reference in the state data and match `Ref` in `handle_info/3`.

## Common Confusions

- **Confusion**: Using a link instead of a monitor to watch a peer.
  **Clarification**: Monitors are unidirectional, stackable, and do not propagate exits — better suited for an FSM that needs to *know about* a peer's death without dying automatically.

## Source Reference

Chapter 15: "Rage Against the Finite-State Machines," section "The gen_fsm Callbacks" (the `idle` state and the `handle_info/3` clause).

## Verification Notes

- Definition: Adapted from "The gen_fsm Callbacks."
- Key Properties: Synthesised from the monitor setup and `handle_info/3` code.
- Confidence: HIGH — explicitly shown with code.
