---
# === CORE IDENTIFICATION ===
concept: Generic Server Termination
slug: gen-server-termination

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
section: "Termination"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - terminate/2
  - stop tuple
  - gen_server stop

# === TYPED RELATIONSHIPS ===
prerequisites:
  - gen-server
extends: []
related:
  - exit-signals
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How does a gen_server terminate?"
  - "What is the terminate/2 callback for?"
  - "When is terminate/2 called on abnormal termination?"
---

# Quick Definition

A `gen_server` terminates when a callback returns a `{stop, Reason, ...}` tuple, which triggers the `terminate/2` callback for cleanup before the process exits.

# Core Definition

"Stopping the server requires the callbacks to return different tuples" (Cesarini & Vinoski, p. 89): `init/1` may return `{stop, Reason}`; `handle_call/3` `{stop, Reason, Reply, LoopData}`; `handle_cast/2` and `handle_info/2` `{stop, Reason, LoopData}`. "These return values terminate with the same behavior as if `exit(Reason)` were called. In the case of calls and casts, before exiting, the callback function `terminate(Reason, LoopData)` is called. It allows the server to clean up after itself before being shut down. Any value returned by terminate/2 is ignored" (pp. 89-90). On abnormal termination, "if the generic server is trapping exits ... terminate/2 will also be called. ... If you are not trapping exits, the process will just terminate without calling terminate/2" (p. 90).

# Prerequisites

- **Gen_server** — Termination is governed by the `gen_server` callback protocol.

# Key Properties

1. A callback triggers termination by returning a `{stop, Reason, ...}` tuple.
2. `init/1` → `{stop, Reason}`; `handle_call/3` → `{stop, Reason, Reply, LoopData}`; `handle_cast/2`/`handle_info/2` → `{stop, Reason, LoopData}`.
3. Stopping behaves as if `exit(Reason)` were called.
4. For calls/casts, `terminate(Reason, LoopData)` runs before exit; its return value is ignored.
5. If `init/1` returns `{stop, Reason}`, `terminate/2` is *not* called, and `start_link` returns `{error, Reason}`.
6. On abnormal termination, `terminate/2` runs only if the server is trapping exits.
7. Use `Reason = normal` for routine shutdowns to avoid SASL error reports overshadowing real crashes.

# Construction / Recognition

## To Construct:
1. Return a `{stop, Reason, ...}` tuple from the appropriate callback.
2. Implement `terminate(Reason, LoopData)` to clean up resources.
3. To run `terminate/2` after abnormal exits, set the `trap_exit` flag.

## To Recognize:
1. Callbacks returning `{stop, ...}` tuples and a `terminate/2` callback.

# Context & Application

- **Typical contexts**: Shutting a server down cleanly; releasing resources on exit.
- **Common applications**: The frequency server's `stop/0` casts `stop`, and `handle_cast(stop, ...)` returns `{stop, normal, LoopData}`.
- **Historical/stylistic notes**: After a runtime error, clean up state with care — recreate state from authoritative sources, not a possibly-corrupt snapshot.

# Examples

**Example 1** (p. 90): The frequency server's termination path:

```erlang
stop() -> gen_server:cast(frequency, stop).
handle_cast(stop, LoopData) ->
    {stop, normal, LoopData}.
terminate(_Reason, _LoopData) ->
    ok.
```

**Example 2** (p. 90): Only the `stop` in the first element of `handle_cast/2`'s returned tuple has special meaning; the *message* atom `stop` is arbitrary (`donald_duck` would work the same).

# Relationships

## Builds Upon
- **Gen_server** — Termination is part of the behavior's callback protocol.

## Enables
- *(none specific in scope)*

## Related
- **Exit signals** — `terminate/2` runs after abnormal exits only when the server traps exits.

## Contrasts With
- *(none)*

# Common Errors

- **Error**: Expecting `terminate/2` to run after a crash without trapping exits.
  **Correction**: Set the `trap_exit` flag if `terminate/2` must run on abnormal termination.
- **Error**: Using a non-`normal` reason for a routine shutdown.
  **Correction**: Use `Reason = normal` so SASL does not log spurious error reports.

# Common Confusions

- **Confusion**: Thinking the `stop` *message* atom is what stops the server.
  **Clarification**: Only the `stop` atom in the *returned tuple* is interpreted by the behavior; the request atom is arbitrary.

# Source Reference

Chapter 3: Generic Servers, Section "Termination," pages 89-91. See Figure 4-6 (abnormal server termination).

# Verification Notes

- Definition source: Direct quotes from pp. 89-90.
- Confidence rationale: HIGH — explicit treatment of stop tuples and terminate semantics.
- Uncertainties: None.
- Cross-reference status: Verified against planned cards.
- Re-extraction notes: Fresh extraction — no pre-existing card for this source.
</content>
</invoke>
