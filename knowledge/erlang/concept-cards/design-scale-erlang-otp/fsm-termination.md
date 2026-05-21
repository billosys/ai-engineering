---
# === CORE IDENTIFICATION ===
concept: FSM Termination
slug: fsm-termination

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
pdf_page: 158
section: "Termination"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "terminate/3"
  - FSM cleanup
  - stopping an FSM

# === TYPED RELATIONSHIPS ===
prerequisites:
  - generic-fsm-behavior
  - fsm-send-all-state-events
extends: []
related:
  - fsm-synchronous-events
  - fsm-loop-data
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I implement a finite state machine with gen_statem?"
  - "What is a finite state machine behavior (gen_statem)?"
---

# Quick Definition

FSM termination is the orderly or abnormal shutdown of a generic FSM; when the FSM traps exits, the `terminate/3` callback runs cleanup code, which can be specialized per state.

# Core Definition

"Our coffee machine can terminate for two reasons. It is either stopped normally, or the process terminates abnormally if the exit BIFs are used or a runtime error occurs" (Cesarini & Vinoski, p. 158). For abnormal termination, "if the FSM is trapping exits as a result of a `process_flag(trap_exit, true)` call, `terminate/3` is invoked in the callback module. If the FSM is not trapping exits, the FSM terminates and its exit signal propagates to other processes linked to it" (p. 158). A normal stop is typically triggered by a `sync_send_all_state_event/2` whose `handle_sync_event/4` clause returns `{stop, normal, LoopData}`. The `terminate(Reason, StateName, LoopData)` callback receives the current state name, so cleanup can be handled individually per state — for example, refunding a customer who was in the *payment* state, which also works after an abnormal termination.

# Prerequisites

- **Generic FSM behavior** — Termination and the `terminate/3` callback are part of the `gen_fsm` contract.
- **FSM send-all-state events** — A normal stop is commonly triggered via `sync_send_all_state_event/2`.

# Key Properties

1. An FSM terminates normally (a `{stop, ...}` control tuple) or abnormally (exit BIF or runtime error).
2. `terminate(Reason, StateName, LoopData)` runs only if the FSM is trapping exits.
3. If not trapping exits, the FSM dies and its exit signal propagates to linked processes.
4. `terminate/3` receives the current state name, enabling per-state cleanup.
5. A normal stop is usually a `{stop, normal, LoopData}` returned from `handle_sync_event/4`.
6. Per-state cleanup in `terminate/3` runs after both normal and abnormal termination (when trapping exits).

# Construction / Recognition

## To Implement FSM Termination:
1. Call `process_flag(trap_exit, true)` in `init/1` if cleanup must run on abnormal exit.
2. Provide a `stop/0` client function calling `gen_fsm:sync_send_all_state_event(?MODULE, stop)`.
3. Implement `handle_sync_event(stop, _From, _State, LoopData) -> {stop, normal, LoopData}`.
4. Implement `terminate/3` clauses, one per state needing cleanup, plus a catch-all.

# Context & Application

- **Typical contexts**: Any FSM holding resources or partial transactions that must be released on shutdown.
- **Common applications**: The coffee machine refunding a customer's payment if it crashes in the *payment* state.
- **Historical/stylistic notes**: By doing cleanup in `terminate/3`, the FSM can refund users even after an abnormal termination — demonstrated by `exit(Pid, crash)` in the *payment* state returning the change (pp. 158-159).

# Examples

**Example 1** (p. 159): Per-state cleanup in `terminate/3`:

```erlang
terminate(_Reason, payment, {_Type,_Price,Paid}) ->
    hw:return_change(Paid);
terminate(_Reason, _StateName, _LoopData) ->
    ok.
```

**Example 2** (p. 159): `exit(Pid, crash)` while the FSM is in *payment* produces an error report ("State machine coffee_fsm terminating ... When State == payment") and triggers the refund `Machine:Returned 100 in change`.

# Relationships

## Builds Upon
- **Generic FSM behavior** — `terminate/3` is part of the `gen_fsm` callback contract.
- **FSM send-all-state events** — A normal stop is triggered via `sync_send_all_state_event/2`.

## Enables
- *(No downstream concepts in this scope.)*

## Related
- **FSM synchronous events** — The stop event is sent synchronously.
- **FSM loop data** — `terminate/3` receives the loop data for cleanup.

## Contrasts With
- *(None.)*

# Common Errors

- **Error**: Expecting `terminate/3` to run on abnormal exit without trapping exits.
  **Correction**: `terminate/3` is invoked on abnormal termination only if the FSM called `process_flag(trap_exit, true)`.

# Common Confusions

- **Confusion**: Thinking the `stop` atom sent via `sync_send_all_state_event/2` is what stops the FSM.
  **Clarification**: That `stop` is just an application term; the FSM stops because `handle_sync_event/4` returns the `{stop, normal, LoopData}` *control tuple*, which the behavior interprets.

# Source Reference

Chapter 5: Finite State Machines, Section "Termination," pages 158-159. See Figure 6-9 and Table 6-2.

# Verification Notes

- Definition source: Direct quotes from p. 158.
- Confidence rationale: HIGH — the source explicitly covers normal and abnormal termination with a worked crash example.
- Uncertainties: None.
- Cross-reference status: Verified against planned cards in this batch.
- Re-extraction notes: Fresh extraction; no pre-existing card for this source.
