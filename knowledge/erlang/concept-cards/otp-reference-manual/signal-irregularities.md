---
# === CORE IDENTIFICATION ===
concept: Signal Irregularities
slug: signal-irregularities

# === CLASSIFICATION ===
category: processes-concurrency
subcategory: null
tier: advanced

# === PROVENANCE ===
source: "Erlang Reference Manual"
source_slug: otp-reference-manual
authors: "Ericsson AB"
chapter: "Processes"
chapter_number: null
pdf_page: null
section: "Irregularities"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - erlang-signals
  - signal-delivery
  - exit-signals
  - links
extends: []
related:
  - message-sending
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What are the known irregularities in Erlang's signal system?"
  - "When can signals behave unexpectedly?"
---

# Quick Definition
Erlang's signal system has several historical irregularities that cannot be fixed without breaking existing code. These include synchronous error checking for some send operations, inconsistent behavior of exit signals with reason `kill` depending on the link flag, and potential blocking when sending over distribution channels.

# Core Definition
The Erlang Reference Manual identifies three irregularities in the signal system (Processes chapter, "Irregularities" subsection):

1. **Synchronous Error Checking**: The send operator `!`, `erlang:send/2,3`, `erlang:link/1`, and `erlang:group_leader/2` perform synchronous error checking when the receiver is identified by a registered name on the local node and the name is not registered.

2. **Unexpected Behaviours of Exit Signals**: When an exit signal with reason `kill` is received, the behavior differs based on the `link` flag. An explicit `exit_signal(Pid, kill)` cannot be trapped, but an exit signal with reason `kill` sent due to a link CAN be trapped.

3. **Blocking Signaling Over Distribution**: Sending signals over a distribution channel may suspend the sender if the output buffer reaches the distribution buffer busy limit, despite signals being nominally asynchronous.

# Prerequisites
- **erlang-signals** -- Must understand the signal system
- **signal-delivery** -- Must understand delivery guarantees
- **exit-signals** -- Must understand exit signal behavior
- **links** -- Must understand how links relate to exit signals

# Key Properties
1. The send operator performs synchronous error checking for locally registered names (raises `badarg`)
2. `erlang:link/1` performs synchronous error checking (raises `noproc`)
3. Exit signal with reason `kill` via `exit_signal/2` is unconditionally fatal
4. Exit signal with reason `kill` via a link CAN be trapped -- and the reason is not converted to `killed`
5. Distribution channel blocking can cause the sender to suspend when the buffer is full
6. Fully asynchronous distributed signaling can be enabled per-process via `process_flag(async_dist, Bool)`
7. These irregularities are permanent -- "they have been part of Erlang too long and it would break a lot of existing code"

# Construction / Recognition
## To Construct/Create:
Not applicable -- irregularities are inherent properties of the system.

## To Identify/Recognize:
1. Unexpected `badarg` when sending to an unregistered name locally
2. Unexpected suspension when sending over distribution
3. Different behavior of `kill` exit signals depending on whether they come from links or `exit_signal/2`

# Context & Application
These irregularities are important for writing robust distributed Erlang applications. The blocking over distribution is particularly impactful in high-throughput systems, where distribution buffer backpressure can cause cascading timeouts. The `process_flag(async_dist, Bool)` flag can mitigate this but requires implementing flow control at the application level.

# Examples
**Example 1** (Processes, "Irregularities" section): Synchronous error checking: "The send operator (`!`), `erlang:send/2,3` BIFs and `erlang:send_nosuspend/2,3` BIFs when the receiver is identified by a name that is expected to be registered locally."

**Example 2** (Processes, "Irregularities" section): Exit signal with `kill`: "When sent using the `exit_signal/2` BIF, the signal cannot be trapped, while it can be trapped if the signal was sent due to a link."

**Example 3** (Processes, "Irregularities" section): Distribution blocking: "When sending a signal over a distribution channel, the sending process may be suspended even though the signal is supposed to be sent asynchronously."

# Relationships
## Builds Upon
- **signal-delivery** -- These are exceptions to the normal signal delivery model
- **exit-signals** -- The `kill` irregularity is specific to exit signals

## Enables
No concepts depend on irregularities.

## Related
- **message-sending** -- Synchronous error checking affects message sending
- **links** -- The `kill` exit signal behaves differently based on the link flag

## Contrasts With
No direct contrasts.

# Common Errors
- **Error**: Sending exit signal with reason `kill` via `exit_signal/2` and expecting the receiver to trap it
  **Correction**: An explicit `exit_signal(Pid, kill)` cannot be trapped. Only a `kill` exit signal sent due to a link can be trapped.

# Common Confusions
- **Confusion**: Thinking that message sending is always non-blocking
  **Clarification**: When sending over distribution, the sender may be suspended if the distribution buffer is full. Use `process_flag(async_dist, true)` for fully asynchronous behavior, but you must then implement your own flow control.

# Source Reference
Processes chapter, "Irregularities" subsection.

# Verification Notes
- Definition source: Direct from source with three explicitly listed irregularities
- Confidence rationale: High -- clearly enumerated irregularities with explanations
- Uncertainties: None
- Cross-reference status: All slugs verified against planned extraction
