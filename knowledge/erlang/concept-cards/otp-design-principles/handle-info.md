---
# === CORE IDENTIFICATION ===
concept: "handle_info/2 Callback"
slug: handle-info

# === CLASSIFICATION ===
category: otp-behaviours
subcategory: gen-server-callbacks
tier: intermediate

# === PROVENANCE ===
source: "OTP Design Principles"
source_slug: otp-design-principles
authors: "Ericsson AB"
chapter: "gen_server Behaviour"
chapter_number: null
pdf_page: null
section: "Handling Other Messages"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "handle_info callback"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - gen-server
extends: []
related:
  - gen-server-call
  - gen-server-cast
  - gen-server-terminate
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How does a gen_server handle messages that are not call or cast requests?"
  - "What is handle_info/2 for?"
---

# Quick Definition

`handle_info/2` is the gen_server callback that handles messages received by the gen_server process that are not `call` or `cast` requests, such as exit signals, monitors, and other direct messages.

# Core Definition

According to the gen_server Behaviour chapter: "If the gen_server is to be able to receive other messages than requests, the callback function handle_info(Info, State) must be implemented to handle them. Examples of other messages are exit messages, if the gen_server is linked to other processes than the supervisor and it is trapping exit signals."

# Prerequisites

- **gen_server** — handle_info/2 is a callback of the gen_server behaviour.

# Key Properties

1. Handles all messages that are not gen_server call or cast protocol messages.
2. Receives the raw message and the current state.
3. Returns `{noreply, State1}` (same return format as `handle_cast/2`).
4. Common use case: handling `{'EXIT', Pid, Reason}` messages when trapping exits.
5. Also handles monitor messages, timer messages, and any direct messages sent to the gen_server pid.

# Construction / Recognition

## To Construct/Create:
1. Implement `handle_info(Info, State)` in the callback module.
2. Pattern-match on the expected message types (e.g., `{'EXIT', Pid, Reason}`).
3. Return `{noreply, NewState}`.

## To Identify/Recognize:
1. A function named `handle_info/2` in a gen_server callback module.
2. Handles messages that don't come through `gen_server:call` or `gen_server:cast`.

# Context & Application

While `handle_call/3` and `handle_cast/2` handle structured gen_server protocol messages, a gen_server process may also receive other kinds of messages. Exit signals from linked processes, monitor DOWN messages, timer messages, and messages sent directly to the process pid all arrive as non-protocol messages that `handle_info/2` must handle. This callback is essential when a gen_server participates in process linking or monitoring beyond its supervisor.

# Examples

**Example 1** (gen_server_concepts.md, "Handling Other Messages"): Handling exit messages from linked processes:
```erlang
handle_info({'EXIT', Pid, Reason}, State) ->
    %% Code to handle exits here.
    ...
    {noreply, State1}.
```

# Relationships

## Builds Upon
- **gen_server** — handle_info/2 is a gen_server callback.

## Enables
- No specific downstream concepts.

## Related
- **gen_server:call** — handle_call handles call protocol messages; handle_info handles everything else
- **gen_server:cast** — handle_cast handles cast protocol messages; handle_info handles everything else
- **gen_server:terminate** — exit messages handled by handle_info may affect termination logic

## Contrasts With
- No direct contrasts in source, but implicitly contrasts with handle_call (structured synchronous requests) and handle_cast (structured asynchronous requests).

# Common Errors

- **Error**: Not implementing `handle_info/2` when the gen_server traps exits or uses monitors.
  **Correction**: If the gen_server is linked to processes (other than its supervisor) and traps exits, `handle_info/2` must be implemented to handle `{'EXIT', Pid, Reason}` messages.

# Common Confusions

- **Confusion**: Thinking all messages to a gen_server go through `handle_call` or `handle_cast`.
  **Clarification**: Only messages sent via `gen_server:call/2` and `gen_server:cast/2` go through those callbacks. All other messages (direct sends, exit signals, monitor notifications) go through `handle_info/2`.

# Source Reference

OTP Design Principles, "gen_server Behaviour" chapter, "Handling Other Messages" section (gen_server_concepts.md).

# Verification Notes

- Definition source: Directly quoted from gen_server_concepts.md "Handling Other Messages" section.
- Confidence rationale: High — explicitly described in the source with an example.
- Uncertainties: None.
- Cross-reference status: References gen-server, gen-server-call, gen-server-cast, gen-server-terminate (planned cards).
