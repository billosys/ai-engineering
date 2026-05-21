---
# === CORE IDENTIFICATION ===
concept: Selective Receive in FSMs
slug: fsm-selective-receive

# === CLASSIFICATION ===
category: otp-behaviours
subcategory: fsm
tier: advanced

# === PROVENANCE ===
source: Designing for Scalability with Erlang/OTP
source_slug: design-scale-erlang-otp
authors: Francesco Cesarini & Steve Vinoski
chapter: "Finite State Machines"
chapter_number: 5
pdf_page: 156
section: "Selective Receives"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - selective receive
  - out-of-sequence events
  - "plain_fsm"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - generic-fsm-behavior
  - fsm-events
extends: []
related:
  - fsm-the-erlang-way
contrasts_with:
  - fsm-events

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a finite state machine behavior (gen_statem)?"
  - "How do I implement a finite state machine with gen_statem?"
---

# Quick Definition

Selective receive — leaving unmatched events in the process mailbox until a state can handle them — is the one thing the OTP `gen_fsm` behavior does not provide; `gen_fsm` handles events strictly FIFO.

# Core Definition

"Selective receives are one thing the OTP `gen_fsm` behavior module does not provide" (Cesarini & Vinoski, p. 156). In complex FSMs running across unreliable distributed networks, events occasionally arrive out of sequence. With a pure-Erlang FSM a selective receive simply leaves such events in the mailbox until matched by a state that can handle them. "This lack of functionality arises from a conscious design decision in behaviors, where messages are handled in the order they arrive, ensuring no memory leaks occur as a result of any message not being matched. Events in the `gen_fsm` behavior are handled on a first-in, first-out (FIFO) basis, and are removed from the receiving process's mailbox when read" (p. 156). The two workarounds are to buffer out-of-sequence events in the loop data (or add an extra state), or to use a selective FSM behavior such as Ulf Wiger's `plain_fsm`.

# Prerequisites

- **Generic FSM behavior** — The limitation is specific to `gen_fsm`'s event handling.
- **FSM events** — You must understand FIFO event handling to see why selective receive is absent.

# Key Properties

1. `gen_fsm` handles events strictly FIFO, removing each from the mailbox when read.
2. It deliberately does *not* support selective receive — a conscious design decision to prevent memory leaks from unmatched messages.
3. Out-of-sequence events therefore cannot simply be left in the mailbox.
4. Workaround 1: buffer out-of-sequence events in the loop data and handle them later.
5. Workaround 2: add an extra state that turns out-of-sequence events into valid ones.
6. Workaround 3: use a selective FSM behavior such as `plain_fsm`, which follows OTP principles and fits in supervision trees.

# Construction / Recognition

## To Handle Out-of-Sequence Events with gen_fsm:
1. Identify which events may arrive early in a given state.
2. In that state's catch-all clause, append the event to a buffer in the loop data.
3. When the FSM reaches a state that can handle it, drain the buffer.
4. Alternatively, adopt `plain_fsm` if true selective-receive semantics are required.

# Context & Application

- **Typical contexts**: Complex FSMs over unreliable distributed networks where events arrive out of order.
- **Common applications**: Protocol handlers that must tolerate reordering or lost messages.
- **Historical/stylistic notes**: The book notes the most commonly used selective FSM implementation at the time of writing is `plain_fsm` by Ulf Wiger, available on GitHub (pp. 156-157).

# Examples

**Example 1** (p. 156): "Imagine receiving a `sunset` event when you are in state *night*!" — an out-of-sequence event a pure-Erlang selective receive would simply leave in the mailbox.

**Example 2** (p. 157): `plain_fsm` by Ulf Wiger is cited as a ready-made selective FSM behavior that follows OTP principles and can be included in supervision trees.

# Relationships

## Builds Upon
- *(No prior concept; this card explains a deliberate gap in `gen_fsm`.)*

## Enables
- *(No downstream concepts in this scope.)*

## Related
- **fsm-the-erlang-way** — Pure-Erlang FSMs *do* get selective receive for free.

## Contrasts With
- **FSM events** — `gen_fsm` events are FIFO with no selective receive; a pure-Erlang `receive` is selective by nature.

# Common Errors

- **Error**: Assuming a `gen_fsm` will leave an unhandled event in the mailbox for a later state.
  **Correction**: `gen_fsm` removes every event when read; buffer out-of-sequence events in loop data, add a state, or use `plain_fsm`.

# Common Confusions

- **Confusion**: Thinking the absence of selective receive in `gen_fsm` is an oversight.
  **Clarification**: It is a deliberate design decision — handling messages in arrival order prevents memory leaks from permanently unmatched messages.

# Source Reference

Chapter 5: Finite State Machines, Section "Selective Receives," pages 156-157.

# Verification Notes

- Definition source: Direct quotes from p. 156.
- Confidence rationale: HIGH — the source explicitly discusses the limitation, its rationale, and workarounds.
- Uncertainties: None.
- Cross-reference status: Verified — `fsm-the-erlang-way` is the slug for the pure-Erlang FSM card.
- Re-extraction notes: Fresh extraction; no pre-existing card for this source.
