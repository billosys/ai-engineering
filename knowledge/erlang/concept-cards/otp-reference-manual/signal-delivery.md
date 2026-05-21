---
# === CORE IDENTIFICATION ===
concept: Signal Delivery
slug: signal-delivery

# === CLASSIFICATION ===
category: processes-concurrency
subcategory: null
tier: intermediate

# === PROVENANCE ===
source: "Erlang Reference Manual"
source_slug: otp-reference-manual
authors: "Ericsson AB"
chapter: "Processes"
chapter_number: null
pdf_page: null
section: "Delivery of Signals"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - signal ordering guarantee
  - signal ordering

# === TYPED RELATIONSHIPS ===
prerequisites:
  - erlang-process
  - erlang-signals
extends:
  - erlang-signals
related:
  - message-queue
  - message-sending
  - signal-irregularities
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What ordering guarantees does Erlang provide for signals?"
  - "Can signals be lost in Erlang?"
---

# Quick Definition
Erlang guarantees that signals sent from one entity to another arrive in the order they were sent. However, the delivery time is unspecified (only guaranteed to be positive), and signals can be lost if the receiver has terminated or if a distribution channel goes down.

# Core Definition
The Erlang Reference Manual states: "The amount of time that passes between the time a signal is sent and the arrival of the signal at the destination is unspecified but positive. If the receiver has terminated, the signal does not arrive, but it can trigger another signal." The ordering guarantee is: "if an entity sends multiple signals to the same destination entity, the order is preserved; that is, if `A` sends a signal `S1` to `B`, and later sends signal `S2` to `B`, `S1` is guaranteed not to arrive after `S2`. Note that `S1` may or may not have been lost." (Processes chapter, "Delivery of Signals" subsection).

# Prerequisites
- **erlang-process** -- Signals are delivered between processes
- **erlang-signals** -- Must understand what signals are

# Key Properties
1. Delivery time is unspecified but positive (never instantaneous)
2. If the receiver has terminated, the signal does not arrive
3. A non-arriving signal can trigger another signal (e.g., link to dead process triggers exit signal)
4. Signals over distribution can be lost if the distribution channel goes down
5. The ordering guarantee: multiple signals from A to B preserve their order
6. The guarantee is per sender-receiver pair only -- no global ordering across different senders
7. A signal may be lost even with the ordering guarantee (S1 lost, but S2 still arrives)

# Construction / Recognition
## To Construct/Create:
Not applicable -- signal delivery is a property of the runtime system, not something constructed.

## To Identify/Recognize:
1. Any reasoning about signal ordering should reference this guarantee
2. The guarantee applies to ALL signal types, not just messages

# Context & Application
The signal ordering guarantee is the fundamental correctness property that Erlang concurrent programs rely on. It enables reasoning about message-based protocols: if process A sends a request and then a cancellation to process B, the cancellation is guaranteed to arrive after the request (if both arrive). However, programmers must account for the possibility that any signal may be lost, especially over distribution.

# Examples
**Example 1** (Processes, "Delivery of Signals" section): "if `A` sends a signal `S1` to `B`, and later sends signal `S2` to `B`, `S1` is guaranteed not to arrive after `S2`. Note that `S1` may or may not have been lost."

**Example 2** (Processes, "Delivery of Signals" section): "If the receiver has terminated, the signal does not arrive, but it can trigger another signal. For example, a `link` signal sent to a non-existing process triggers an `exit` signal, which is sent back to where the `link` signal originated from."

# Relationships
## Builds Upon
- **erlang-signals** -- Delivery guarantees apply to the signal system

## Enables
- **message-queue** -- Queue ordering is a consequence of the signal ordering guarantee

## Related
- **message-sending** -- Messages are signals subject to this guarantee
- **signal-irregularities** -- Exceptions to the normal signal behavior

## Contrasts With
No direct contrasts.

# Common Errors
- **Error**: Assuming signals from different senders arrive in any predictable order
  **Correction**: The ordering guarantee only applies per sender-receiver pair. There is no global ordering across different senders.

# Common Confusions
- **Confusion**: Thinking the ordering guarantee means no signals can be lost
  **Clarification**: Signals can be lost (receiver terminated, distribution channel down). The guarantee is about relative ordering, not reliability. "S1 may or may not have been lost."

# Source Reference
Processes chapter, "Delivery of Signals" subsection.

# Verification Notes
- Definition source: Direct from source with key quote
- Confidence rationale: High -- explicit definition of the ordering guarantee
- Uncertainties: None
- Cross-reference status: All slugs verified against planned extraction
