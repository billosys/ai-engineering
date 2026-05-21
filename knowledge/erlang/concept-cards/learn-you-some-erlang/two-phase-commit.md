---
concept: Two-Phase Commit (FSM)
slug: two-phase-commit
category: otp-behaviours
subcategory: state-machines
tier: advanced
source: "Learn You Some Erlang for Great Good!"
source_slug: learn-you-some-erlang
authors: "Fred Hébert"
chapter: "Rage Against the Finite-State Machines"
chapter_number: 15
pdf_page: null
section: "Defining the State Diagrams and Transitions"
extraction_confidence: medium
aliases:
  - two-phase commit
  - "2PC"
  - commit protocol
prerequisites:
  - finite-state-machine
  - fsm-deadlock-avoidance
extends: []
related:
  - gen-fsm
  - fsm-deadlock-avoidance
contrasts_with: []
answers_questions:
  - "How do I implement a stateful process?"
---

# Two-Phase Commit (FSM)

## Quick Definition

A two-phase commit is a protocol for finalising a transaction between two parties: first both confirm readiness, then both commit — used in the trading FSM's `ready` state.

## Core Definition

The book implements "a bastardized version of a *two-phase commit* to make sure things go right when making the trade official" (Ch. 15, "Defining the State Diagrams and Transitions"). In the `ready` state, the two FSMs confirm the transaction synchronously: one asks `ask_commit`, the other replies `ready_commit`, then `do_commit` triggers the actual commit.

## Prerequisites

- **Finite-state machine** — The commit happens within an FSM state.
- **FSM deadlock avoidance** — Two-phase commit needs synchronous calls, which would deadlock without an elected leader.

## Key Properties

1. It synchronises two parties so a transaction is committed by both or neither.
2. The book's version is simplified — a true commit needs a third-party judge and atomic database writes.
3. Two-phase commit requires *synchronous* communication, so the two FSMs cannot both initiate it.
4. The deadlock is broken by *electing a leader*: pids can be compared, so `priority/2` picks one FSM to drive the commit while the other waits for orders.
5. The whole `try ... catch` wrapping the commit aborts the transaction if a synchronous call crashes (peer death or cancellation).

## Construction / Recognition

## To Implement the Commit

1. Enter a dedicated state (`ready`) where ordinary events no longer matter.
2. Elect a leader by comparing pids (`priority(self(), Other)`).
3. The leader synchronously sends `ask_commit`, expects `ready_commit`, then sends `do_commit`.
4. Both FSMs run their `commit` action; wrap leader calls in `try ... catch` to abort on failure.

## Context & Application

The book stresses this is illustrative, not production-grade: "It's generally not possible to do a true safe commit with only two participants; a third party is usually required." The leader-election trick (comparing pids) is presented as a clever, deadlock-free way to coordinate two symmetric FSMs.

## Examples

**Example 1** (Ch. 15): `priority(OwnPid, OtherPid) when OwnPid > OtherPid -> true;` elects the FSM with the greater pid as commit leader.

**Example 2** (Ch. 15): `ready(ack, S)` — the leader runs `ready_commit = ask_commit(...)`, `ok = do_commit(...)`, `commit(S)`, all inside a `try ... catch` that aborts on failure.

## Relationships

## Builds Upon

- **Finite-state machine** — The commit is the `ready` state's logic.

## Related

- **fsm-deadlock-avoidance** — Leader election is what makes the synchronous commit deadlock-free.
- **gen-fsm** — The commit uses `sync_send_event` between the two FSMs.

## Common Errors

- **Error**: Letting both FSMs initiate the synchronous commit.
  **Correction**: Elect one leader (e.g. by pid comparison); the other waits for orders.

## Common Confusions

- **Confusion**: Thinking the book's two-phase commit is a correct, production-ready protocol.
  **Clarification**: It is explicitly a "bastardized version"; a real two-phase commit needs a coordinator and atomic, durable writes.

## Source Reference

Chapter 15: "Rage Against the Finite-State Machines," sections "Defining the State Diagrams and Transitions" and "The gen_fsm Callbacks" (the `ready` state).

## Verification Notes

- Definition: Direct quotes from the chapter.
- Key Properties: Synthesised from the `ready`-state code and the leader-election discussion.
- Confidence: MEDIUM — the source presents a deliberately simplified version and points elsewhere for a correct protocol.
