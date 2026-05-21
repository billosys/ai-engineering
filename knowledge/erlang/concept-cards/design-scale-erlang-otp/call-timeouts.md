---
# === CORE IDENTIFICATION ===
concept: Call Timeouts
slug: call-timeouts

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
section: "Call Timeouts"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "gen_server:call/3"
  - default timeout
  - 5-second timeout
  - infinity timeout

# === TYPED RELATIONSHIPS ===
prerequisites:
  - synchronous-message-passing
extends: []
related:
  - gen-server-deadlocks
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What timeout does gen_server:call use?"
  - "How do I set a custom call timeout?"
  - "What happens when a gen_server call times out?"
---

# Quick Definition

`gen_server:call` has a built-in 5-second timeout; if no reply arrives, the client process raises an exception. `gen_server:call/3` lets you supply a custom timeout in milliseconds or the atom `infinity`.

# Core Definition

"OTP behaviors have a built-in timeout of 5 seconds in their synchronous `gen_server:call` APIs. ... If you are sending a synchronous request using OTP behaviors and have not received a response within 5 seconds, the client process will raise an exception" (Cesarini & Vinoski, p. 91). A custom timeout is set with `gen_server:call(Server, Message, TimeOut)`, "where TimeOut is either the desired value in milliseconds or the atom infinity" (pp. 92-93). The book warns: "Use the value infinity with extreme care, avoiding it altogether unless there's no other alternative."

# Prerequisites

- **Synchronous message passing** — Call timeouts apply specifically to `gen_server:call`.

# Key Properties

1. `gen_server:call/2` has a built-in 5-second (5,000 ms) timeout.
2. On timeout, the client process raises an exception.
3. `gen_server:call/3` accepts a custom `TimeOut` in milliseconds or `infinity`.
4. A late reply (server alive but slow) still arrives after the timeout and must be handled.
5. An unhandled late reply litters the client mailbox, slowing the process.
6. A timeout exception caught outside a `try-catch` crashes the client process.
7. `infinity` should be avoided unless unavoidable.

# Construction / Recognition

## To Construct:
1. Use `gen_server:call/2` to accept the 5-second default.
2. Use `gen_server:call(Server, Message, TimeOut)` for a custom timeout.
3. If catching timeout exceptions, also handle the possible late reply.

## To Recognize:
1. A `gen_server:call/3` invocation, or a `{timeout, {gen_server, call, ...}}` exception.

# Context & Application

- **Typical contexts**: Calls to busy servers or servers depending on slow external resources.
- **Common applications**: Setting a 30-second timeout when an external client contract requires it.
- **Historical/stylistic notes**: Letting a non-responsive call crash the client and letting a supervisor restart it is usually the best approach.

# Examples

**Example 1** (p. 92): A call exceeding the default timeout raises an exception:

```erlang
3> catch gen_server:call(timeout, {sleep, 5001}).
{'EXIT',{timeout,{gen_server,call,[timeout,{sleep,5001}]}}}
5> gen_server:call(timeout, {sleep, 5001}).
** exception exit: {timeout,{gen_server,call,[timeout,{sleep,5001}]}}
```

**Example 2** (p. 93): The custom-timeout form:

```erlang
gen_server:call(Server, Message, TimeOut) -> Reply
```

# Relationships

## Builds Upon
- **Synchronous message passing** — Timeouts bound `gen_server:call`.

## Enables
- *(none specific in scope)*

## Related
- **Gen_server deadlocks** — Timeouts are the mechanism that resolves deadlocks.

## Contrasts With
- *(none)*

# Common Errors

- **Error**: Catching a timeout exception but ignoring the server's eventual late reply.
  **Correction**: Handle the late reply too; otherwise it litters the mailbox and degrades performance.
- **Error**: Using `infinity` casually.
  **Correction**: Avoid `infinity` unless there is no alternative; prefer a measured finite timeout.

# Common Confusions

- **Confusion**: Thinking a timeout means the server is dead.
  **Clarification**: A timed-out server may simply be slow and will still send its reply, which must be accounted for.

# Source Reference

Chapter 3: Generic Servers, Section "Call Timeouts," pages 91-94. See Figure 4-7 (server timeouts).

# Verification Notes

- Definition source: Direct quotes from pp. 91-93.
- Confidence rationale: HIGH — explicit treatment with shell examples.
- Uncertainties: None.
- Cross-reference status: Verified against planned cards.
- Re-extraction notes: Fresh extraction — no pre-existing card for this source.
</content>
</invoke>
