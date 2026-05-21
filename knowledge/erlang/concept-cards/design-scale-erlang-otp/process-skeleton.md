---
# === CORE IDENTIFICATION ===
concept: Process Skeleton
slug: process-skeleton

# === CLASSIFICATION ===
category: otp-behaviours
subcategory: process-design
tier: intermediate

# === PROVENANCE ===
source: "Designing for Scalability with Erlang/OTP"
source_slug: design-scale-erlang-otp
authors: "Francesco Cesarini & Steve Vinoski"
chapter: "Behaviors"
chapter_number: 2
pdf_page: 72
section: "Process Skeletons"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - process lifecycle
  - process loop pattern

# === TYPED RELATIONSHIPS ===
prerequisites:
  - processes-and-message-passing
  - tail-recursion
extends: []
related:
  - otp-behaviors
  - client-server-design-pattern
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a process skeleton?"
  - "What lifecycle do all Erlang processes share?"
---

# Quick Definition

A process skeleton is the common lifecycle shared by all Erlang processes: spawn and initialize, repeatedly receive and handle messages, then terminate. It is "the pattern behind all patterns."

# Core Definition

Although processes solving radically different tasks "might at first glance appear very different ... both processes will share a common lifecycle. Both will: Be spawned and initialized; Repeatedly receive messages, handle them, and send replies; Be terminated (normally or abnormally)" (Cesarini & Vinoski, p. 53). The typical loop "must be started, must handle events, and is finally terminated." This skeleton "is in fact the pattern behind all patterns. It is so common that even code written without the OTP behavior libraries tends to use the same function names" — `init/1` to initialize state, `loop/1` to receive, `handle/2` to handle individual messages, and `terminate/1` to clean up (p. 55).

# Prerequisites

- **Processes and message passing** — The skeleton describes a process's life and its message loop.
- **Tail recursion** — The `loop/1` function recurses tail-recursively to run in constant memory.

# Key Properties

1. Every process is spawned, then initializes process-specific state.
2. Once initialized, a process repeatedly receives and handles messages.
3. Each iteration may update state and send replies.
4. A process terminates normally (no more code) or abnormally (exception/exit signal).
5. Where possible, abnormal termination should still run the normal cleanup code.
6. Conventional function names — `init`, `loop`, `handle`, `terminate` — make the skeleton recognizable.

# Construction / Recognition

## To Construct:
1. Write a `start/N` that spawns the process running `init/N`.
2. Write `init/N` to build state and call `loop/1`.
3. Write `loop/1` as a tail-recursive `receive` dispatching to `handle/2`.
4. Write `terminate/1` for cleanup on a `stop` message.

## To Recognize:
1. Look for the `init`/`loop`/`handle`/`terminate` function quartet.

# Context & Application

- **Typical contexts**: Any long-lived Erlang process — key-value stores, GUI window managers, servers.
- **Common applications**: Client-server processes, where the skeleton becomes a receive-evaluate loop.
- **Historical/stylistic notes**: Recognizing this shared structure motivates OTP behaviors, which formalize it.

# Examples

**Example 1** (p. 54): The typical process loop:

```erlang
start(Args) ->                              % Start the server.
    spawn(server, init, [Args]).
init(Args) ->                               % Initialize the internal process state.
    State = initialize_state(Args),
    loop(State).
loop(State) ->                              % Receive and handle messages.
    receive
        {handle, Msg} ->
            NewState = handle(Msg, State),
            loop(NewState);
        stop ->
            terminate(State)                % Stop the process.
    end.
terminate(State) ->                         % Clean up prior to termination.
    clean_up(State).
```

**Example 2** (p. 53, Figure 3-1): The process flow diagram outlining spawn-init, the message loop, and termination.

# Relationships

## Builds Upon
- *(none — foundational pair of prerequisites)*

## Enables
- **OTP behaviors** — Behaviors formalize the process skeleton into reusable library modules.
- **Client-server design pattern** — The skeleton specializes into the client-server receive-evaluate loop.

## Related
- *(none additional)*

## Contrasts With
- *(none)*

# Common Errors

- **Error**: Not running cleanup code on abnormal termination.
  **Correction**: Trap exits or use try-catch so abnormal exits still invoke the `terminate` cleanup where possible.

# Common Confusions

- **Confusion**: Believing different process types have nothing structurally in common.
  **Clarification**: Regardless of task, processes share the same spawn-init / loop / terminate skeleton.

# Source Reference

Chapter 2: Behaviors, Section "Process Skeletons," pages 53-55. See Figure 3-1 (the process skeleton).

# Verification Notes

- Definition source: Direct quotes and paraphrase from pp. 53-55.
- Confidence rationale: HIGH — explicit lifecycle enumeration and code skeleton.
- Uncertainties: None.
- Cross-reference status: Verified against planned cards.
- Re-extraction notes: Fresh extraction — no pre-existing card for this source.
</content>
</invoke>
