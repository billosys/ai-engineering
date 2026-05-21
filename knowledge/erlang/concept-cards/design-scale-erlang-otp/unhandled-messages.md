---
# === CORE IDENTIFICATION ===
concept: Unhandled Messages
slug: unhandled-messages

# === CLASSIFICATION ===
category: otp-behaviours
subcategory: gen-server
tier: intermediate

# === PROVENANCE ===
source: "Designing for Scalability with Erlang/OTP"
source_slug: design-scale-erlang-otp
authors: "Francesco Cesarini & Steve Vinoski"
chapter: "Generic Servers"
chapter_number: 3
pdf_page: 96
section: "Unhandled Messages"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - unknown messages
  - function_clause error
  - mailbox leak

# === TYPED RELATIONSHIPS ===
prerequisites:
  - gen-server
  - selective-receive
extends: []
related:
  - handle-info
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What happens when a gen_server receives an unknown message?"
  - "How does OTP differ from pure Erlang in handling unmatched messages?"
---

# Quick Definition

In a `gen_server`, an unknown `call` or `cast` message that matches no callback clause causes a `function_clause` error and terminates the server — unlike pure Erlang, where unmatched messages silently accumulate in the mailbox.

# Core Definition

"Erlang uses selective receives when retrieving messages from the process mailbox. But allowing us to extract certain messages while leaving others unhandled comes with the risk of memory leakages. ... Using Erlang without OTP, the message queue would get longer and longer" (Cesarini & Vinoski, p. 86). "OTP behaviors take a different approach. Messages are handled in the same order in which they are received." When a `call` or `cast` message matches no `handle_call/3` or `handle_cast/2` clause, "handle_call(foobar, _From, LoopData) doesn't match any of the clauses, causing the function clause error" and the server terminates (p. 87). The advice: "If in doubt, don't be defensive, and instead make your server terminate when receiving unknown messages. Treat these terminations as bugs."

# Prerequisites

- **Gen_server** — Unhandled-message behavior is a property of `gen_server` callbacks.
- **Selective receive** — The mailbox-leak risk stems from selective receive in pure Erlang.

# Key Properties

1. In pure Erlang, unmatched messages accumulate in the mailbox, eventually exhausting memory.
2. In a `gen_server`, every `call`/`cast` message is retrieved and passed to a callback.
3. A message matching no callback clause causes a `function_clause` runtime error.
4. The server then terminates and prints an error report.
5. For `call`/`cast`, all requests should originate from the callback module, so unknown messages indicate bugs.
6. For `handle_info/2`, a catch-all may be appropriate due to ports, sockets, and monitors.

# Construction / Recognition

## To Construct:
1. Implement exactly the `handle_call`/`handle_cast` clauses your protocol defines.
2. Let unknown `call`/`cast` messages crash the server — treat the crash as a bug to fix at the source.
3. In `handle_info/2`, add a catch-all clause (and log unknown messages).

## To Recognize:
1. A `function_clause` error report naming `handle_call`/`handle_cast` indicates an unhandled message.

# Context & Application

- **Typical contexts**: Testing and debugging a `gen_server`'s protocol.
- **Common applications**: Catching protocol mistakes early — sending `foobar` to a server crashes it with a clear report.
- **Historical/stylistic notes**: The book repeatedly warns against defensively handling corner cases that mask bugs.

# Examples

**Example 1** (p. 87): Sending an unknown message crashes the server:

```erlang
2> gen_server:call(frequency, foobar).
=ERROR REPORT==== 29-Nov-2015::18:27:45 ===
** Generic server frequency terminating
** Last message in was foobar
** Reason for termination ==
** {function_clause,[{frequency,handle_call,[foobar, ...]}]}
```

# Relationships

## Builds Upon
- **Gen_server** — The behavior dictates how unhandled messages are treated.

## Enables
- *(none specific in scope)*

## Related
- **Handle_info** — Where a catch-all for forgotten messages is appropriate.

## Contrasts With
- *(none)*

# Common Errors

- **Error**: Adding defensive catch-all clauses to `handle_call`/`handle_cast`.
  **Correction**: Let unknown `call`/`cast` messages crash; fix the bug at its source. If you must ignore them, log them.

# Common Confusions

- **Confusion**: Thinking an unmatched `gen_server` message just sits in the mailbox like in pure Erlang.
  **Clarification**: A `gen_server` always retrieves the message and invokes a callback; a non-matching `call`/`cast` causes a `function_clause` crash.

# Source Reference

Chapter 3: Generic Servers, Section "Unhandled Messages," pages 86-88.

# Verification Notes

- Definition source: Direct quotes from pp. 86-87.
- Confidence rationale: HIGH — explicit treatment with a worked error report.
- Uncertainties: None.
- Cross-reference status: Verified against planned cards.
- Re-extraction notes: Fresh extraction — no pre-existing card for this source.
</content>
</invoke>
