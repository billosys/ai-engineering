---
# === CORE IDENTIFICATION ===
concept: Client-Server Design Pattern
slug: client-server-design-pattern

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
section: "Design Patterns"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - client-server architecture
  - receive-evaluate loop

# === TYPED RELATIONSHIPS ===
prerequisites:
  - process-skeleton
extends: []
related:
  - generic-vs-specific-code
  - client-functions
  - the-server-loop
  - gen-server
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the client-server design pattern in Erlang?"
  - "How are clients and servers represented in Erlang?"
---

# Quick Definition

In the client-server design pattern, clients and a server are Erlang processes that exchange requests and replies as messages. The server iterates in a receive-evaluate loop, handling one request at a time.

# Core Definition

"Clients and servers are represented as Erlang processes, with their requests and replies sent as messages" (Cesarini & Vinoski, p. 56). The server is started by spawning a process that runs an `init/1` function, which initializes the *loop data* — "a variable that stores process data between calls" — and enters the loop. "Server processes iterate in a receive-evaluate loop. They wait for client requests, handle them, return a result, and loop again, waiting for the next message to arrive. With every iteration, they may update their process state and might generate side effects" (p. 64). The pattern divides cleanly into generic code (reusable across servers) and specific code (the server's business logic).

# Prerequisites

- **Process skeleton** — The client-server pattern is the process skeleton specialized to request/reply over messages.

# Key Properties

1. Clients and the server are separate Erlang processes.
2. Requests and replies are passed as messages.
3. The server is spawned, runs `init/1` to build loop data, then enters its loop.
4. The server loop receives one request, handles it, replies, and loops with updated state.
5. *Loop data* (process state) is threaded through each loop iteration.
6. Each iteration may update state and produce side effects.
7. The code separates into generic parts and server-specific parts.

# Construction / Recognition

## To Construct:
1. Define client API functions that send request messages and await replies.
2. Spawn a server process running `init/1`, which initializes loop data and calls `loop/1`.
3. Implement `loop/1` as a receive-evaluate loop that handles requests and recurses.
4. Provide a stop path that terminates the server.

## To Recognize:
1. A process with an `init`/`loop` structure, a request/reply message protocol, and a client API.

# Context & Application

- **Typical contexts**: Servers that own a resource or state — key-value stores, window managers, frequency allocators.
- **Common applications**: The frequency-allocation server used throughout Chapters 2-3.
- **Historical/stylistic notes**: This pattern is the basis for the `gen_server` behavior.

# Examples

**Example 1** (pp. 59-67): The `frequency` module — a frequency allocator for cell phones. Clients call `allocate/0` and `deallocate/1`; the server loops handling `allocate`, `{deallocate, Freq}`, and `stop` messages.

**Example 2** (p. 60): A trial run — `frequency:start()`, allocate six frequencies, fail the seventh, `deallocate(11)`, allocate again, then `frequency:stop()`.

# Relationships

## Builds Upon
- *(none — foundational)*

## Enables
- **Gen_server** — The OTP behavior that packages this pattern's generic parts.

## Related
- **Generic vs. specific code** — The pattern is analyzed by separating these.
- **Client functions** and **The server loop** — The two halves of a client-server implementation.

## Contrasts With
- *(none)*

# Common Errors

- **Error**: Exposing message passing directly to callers instead of behind a client API.
  **Correction**: Hide the protocol in client functions so it can change without affecting callers.

# Common Confusions

- **Confusion**: Thinking each new server must be written entirely from scratch.
  **Clarification**: Most of a client-server implementation is generic and reusable; only the business logic is specific.

# Source Reference

Chapter 2: Behaviors, Section "Design Patterns" and "Extracting Generic Behaviors," pages 56-67.

# Verification Notes

- Definition source: Direct quotes from pp. 56 and 64.
- Confidence rationale: HIGH — explicit treatment with the frequency-server running example.
- Uncertainties: None.
- Cross-reference status: Verified against planned cards.
- Re-extraction notes: Fresh extraction — no pre-existing card for this source.
</content>
</invoke>
