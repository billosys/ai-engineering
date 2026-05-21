---
# === CORE IDENTIFICATION ===
concept: "gen_server terminate/2 Callback"
slug: gen-server-terminate

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
section: "Stopping"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "terminate callback"
  - "gen_server terminate"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - gen-server
  - gen-server-init
extends: []
related:
  - gen-server-cast
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How does a gen_server clean up before stopping?"
  - "When is terminate/2 called?"
  - "How do I stop a gen_server?"
---

# Quick Definition

`terminate/2` is the gen_server callback invoked when the server is about to stop, allowing it to perform cleanup before the process exits.

# Core Definition

The gen_server Behaviour chapter describes two termination scenarios. In a supervision tree: "If it is necessary to clean up before termination, the shutdown strategy must be a time-out value and the gen_server must be set to trap exit signals in function init. When ordered to shut down, the gen_server then calls the callback function terminate(shutdown, State)." For standalone servers, a stop request via `handle_cast` returns `{stop, normal, State1}`, which "causes the gen_server to call terminate(normal, State1) and then it terminates gracefully."

# Prerequisites

- **gen_server** — terminate/2 is a callback of the gen_server behaviour.
- **gen_server:init** — init may set up resources and trap exits that terminate must handle.

# Key Properties

1. Called when the gen_server is about to terminate.
2. Receives the reason for termination and the current state.
3. In a supervision tree with cleanup needs: gen_server must trap exits in `init/1`, and `terminate(shutdown, State)` is called.
4. For standalone gen_servers: returning `{stop, Reason, State}` from a callback triggers `terminate(Reason, State)`.
5. Should be the opposite of `init/1` — release resources, close files, etc.
6. In a supervision tree without cleanup, no stop function or terminate implementation is needed.

# Construction / Recognition

## To Construct/Create:
1. Implement `terminate(Reason, State)` in the callback module.
2. Perform cleanup: close files, release resources, deregister names.
3. Return value is ignored.
4. If in a supervision tree, ensure `process_flag(trap_exit, true)` is set in `init/1`.

## To Identify/Recognize:
1. A function named `terminate/2` in a gen_server callback module.
2. Called with a reason atom (`shutdown`, `normal`, or an error reason) and the current state.

# Context & Application

`terminate/2` provides a hook for orderly shutdown. In supervision trees, the supervisor sends an exit signal to the gen_server; if the gen_server traps exits, `terminate(shutdown, State)` is called before the process stops. For standalone servers, the typical pattern is to handle a `stop` message in `handle_cast`, returning `{stop, normal, State}`, which triggers `terminate(normal, State)`.

# Examples

**Example 1** (gen_server_concepts.md, "Stopping - In a Supervision Tree"): Cleanup in a supervised gen_server:
```erlang
init(Args) ->
    ...,
    process_flag(trap_exit, true),
    ...,
    {ok, State}.

...

terminate(shutdown, State) ->
    %% Code for cleaning up here
    ...
    ok.
```

**Example 2** (gen_server_concepts.md, "Stopping - Standalone Gen_Servers"): Stop via cast for standalone server:
```erlang
stop() ->
    gen_server:cast(ch3, stop).

handle_cast(stop, State) ->
    {stop, normal, State};

...

terminate(normal, State) ->
    ok.
```

# Relationships

## Builds Upon
- **gen_server** — terminate/2 is a gen_server callback
- **gen_server:init** — terminate is the counterpart to init (cleanup vs. setup)

## Enables
- No specific downstream concepts.

## Related
- **gen_server:cast** — cast can trigger termination via `{stop, Reason, State}` return
- **Supervision Tree** — supervisors trigger termination of their children

## Contrasts With
- No direct contrasts in source.

# Common Errors

- **Error**: Expecting `terminate/2` to be called in a supervision tree without trapping exits.
  **Correction**: The source states that "the shutdown strategy must be a time-out value and the gen_server must be set to trap exit signals in function init" for terminate to be called during supervised shutdown.

# Common Confusions

- **Confusion**: Thinking `terminate/2` is always called when a gen_server crashes.
  **Clarification**: `terminate/2` is only reliably called when the gen_server traps exits or when it explicitly returns `{stop, Reason, State}` from a callback. If the gen_server crashes without trapping exits, `terminate/2` may not be called.

# Source Reference

OTP Design Principles, "gen_server Behaviour" chapter, "Stopping" section (gen_server_concepts.md).

# Verification Notes

- Definition source: Directly quoted from gen_server_concepts.md "Stopping" section.
- Confidence rationale: High — explicitly described with two scenarios and code examples.
- Uncertainties: None.
- Cross-reference status: References gen-server, gen-server-init, gen-server-cast, supervision-tree (planned cards).
