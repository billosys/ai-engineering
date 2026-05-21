---
# === CORE IDENTIFICATION ===
concept: Hot Code Swapping
slug: hot-code-swapping

# === CLASSIFICATION ===
category: otp-behaviours
subcategory: server-abstraction
tier: advanced

# === PROVENANCE ===
source: Programming Erlang, Second Edition
source_slug: programming-erlang
authors: Joe Armstrong
chapter: "Introducing OTP"
chapter_number: 22
pdf_page: null
section: "Server 3: A Server with Hot Code Swapping"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "hot code swap"
  - "dynamic code upgrade"
  - "dynamic code change"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - generic-server
  - message-passing
extends: []
related:
  - gen-server
  - gen-server-callbacks
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is hot code swapping?"
  - "How can a server change its behaviour without being stopped?"
---

# Quick Definition

Hot code swapping is changing the code a running server executes without stopping it: you send the server a message containing a new callback module, and it continues with the new code and the old session data.

# Core Definition

"Most servers execute a fixed program, and if you want to modify the behavior of the server, you have to stop the server and then restart it with the modified code. When we want to change the behavior of our server, we don't stop it; we just send it a message containing the new code, and it picks up the new code and continues with the new code and the old session data. This process is called *hot code swapping*" (Programming Erlang, "Server 3: A Server with Hot Code Swapping"). In the book's `server3`, a `{swap_code, NewCallbackMod}` message causes the server loop to recurse with the new callback module while keeping the old state. The book calls this "dynamic code upgrade, in action before your eyes, with no black magic."

# Prerequisites

- **The generic server** — hot code swapping is added to the generic server abstraction.
- **Message passing** — the new code is delivered to the running server as a message.

# Key Properties

1. The server is never stopped; its session data (state) is preserved across the swap.
2. The new code arrives as a message, not via a separate deployment step.
3. In `server3` the swap is triggered by a `{swap_code, NewCallBackMod}` message handled before ordinary requests.
4. Used in products that are "never taken out of service for software maintenance upgrades."
5. Powerful but hard to debug: after many dynamic changes, diagnosing a later crash is difficult.

# Construction / Recognition

## To Construct (server3 style):
1. Add a `swap_code(Name, Mod)` interface that does `rpc(Name, {swap_code, Mod})`.
2. In the server loop, match `{From, {swap_code, NewCallBackMod}}` before the generic request clause.
3. Acknowledge the swap and recurse: `loop(Name, NewCallBackMod, OldState)`.

## To Recognize:
1. A server loop clause that pattern-matches a `swap_code` message and recurses with a new module argument performs hot code swapping.

# Context & Application

- **Typical contexts**: Long-running production servers that must not be taken offline for upgrades.
- **Common applications**: Adding a new API function (`all_names`) to a running name server by swapping in `new_name_server`.
- **Historical/stylistic notes**: The book warns this technique "is almost too powerful"; for industrial-scale projects with many programmers, too much dynamism complicates debugging. In the real `gen_server`, the equivalent mechanism is the `code_change/3` callback driven by the release-handling subsystem.

# Examples

**Example 1** ("Server 3: A Server with Hot Code Swapping"): The swap clause in `server3`'s loop:

```erlang
{From, {swap_code, NewCallBackMod}} ->
    From ! {Name, ack},
    loop(Name, NewCallBackMod, OldState);
```

**Example 2** ("Server 3"): After `server3:swap_code(name_server, new_name_server)`, the new `all_names()` function works against state collected by the *old* callback — "we changed the callback module on the fly."

# Relationships

## Builds Upon
- **The generic server** — hot code swapping extends the basic generic server.

## Enables
- **gen_server callbacks** — `code_change/3` is the gen_server callback that handles software upgrades.

## Related
- **gen_server** — the production behaviour where code change is handled by the release subsystem.

## Contrasts With
- (No direct contrast within this chapter.)

# Common Errors

- **Error**: Placing the `swap_code` clause after the generic request clause in the loop.
  **Correction**: A generic `{From, Request}` clause would match the swap message first; put the `swap_code` clause earlier.

- **Error**: Relying heavily on dynamic code changes in large multi-programmer projects.
  **Correction**: The book cautions that excessive dynamism makes later crashes very hard to debug; balance power against maintainability.

# Common Confusions

- **Confusion**: Thinking hot code swapping discards the server's state.
  **Clarification**: The server "continues with the new code and the old session data" — state is preserved.

- **Confusion**: Believing the swap requires recompiling the whole system.
  **Clarification**: You compile only the new callback module and send a message; nothing else stops.

# Source Reference

Chapter 22: Introducing OTP, sections "Server 3: A Server with Hot Code Swapping" and "Server 4: Transactions and Hot Code Swapping". No page numbers (EPUB-origin source).

# Verification Notes

- Definition source: Direct quote from "Server 3: A Server with Hot Code Swapping".
- Confidence rationale: HIGH — explicitly named and demonstrated in the source.
- Uncertainties: None.
- Cross-reference status: Verified against planned cards in this batch.
- Re-extraction notes: Fresh extraction; no pre-existing card.
