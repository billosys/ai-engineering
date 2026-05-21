---
# === CORE IDENTIFICATION ===
concept: gen_server Callback Functions
slug: gen-server-callbacks

# === CLASSIFICATION ===
category: otp-behaviours
subcategory: gen-server
tier: intermediate

# === PROVENANCE ===
source: Programming Erlang, Second Edition
source_slug: programming-erlang
authors: Joe Armstrong
chapter: "Introducing OTP"
chapter_number: 22
pdf_page: null
section: "The gen_server Callback Structure"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "gen_server callbacks"
  - "init/1, handle_call/3, handle_cast/2, handle_info/2, terminate/2, code_change/3"
  - "the six callback functions"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - gen-server
  - callback-module
  - pattern-matching
extends: []
related:
  - gen-server-call
  - gen-server-cast
  - handle-info
  - hot-code-swapping
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What are the gen_server callback functions?"
  - "How do I write a gen_server callback module?"
  - "What does each gen_server callback return?"
---

# Quick Definition

A `gen_server` callback module must export six functions: `init/1`, `handle_call/3`, `handle_cast/2`, `handle_info/2`, `terminate/2`, and `code_change/3`. Each is invoked by the `gen_server` behaviour at a defined moment in the server's life.

# Core Definition

"Our callback module must export six callback routines: `init/1`, `handle_call/3`, `handle_cast/2`, `handle_info/2`, `terminate/2`, and `code_change/3`" (Programming Erlang, "Step 3: Write the Callback Routines"). Each callback has a defined role and a fixed set of return tuples:

- `init(Args)` — initializes the server; normally returns `{ok, State}` (also `{ok, State, Timeout}`, `ignore`, `{stop, Reason}`).
- `handle_call(Request, From, State)` — handles synchronous calls; returns `{reply, Reply, State}`, `{noreply, State}`, `{stop, Reason, Reply, State}`, etc.
- `handle_cast(Msg, State)` — handles asynchronous casts; returns `{noreply, State}` or `{stop, Reason, State}`.
- `handle_info(Info, State)` — handles spontaneous (non-call/cast) messages; same returns as `handle_cast`.
- `terminate(Reason, State)` — called whenever the server is about to terminate; should undo `init/1`; return value is ignored.
- `code_change(OldVsn, State, Extra)` — converts process state during a software upgrade; returns `{ok, NewState}`.

# Prerequisites

- **gen_server** — these functions are the callbacks of the gen_server behaviour.
- **Callback module** — the six functions live in the callback module.
- **Pattern matching** — `handle_call` clauses dispatch on the shape of the request term.

# Key Properties

1. Exactly six functions, all exported from the callback module.
2. `init/1` runs first, when `gen_server:start_link` is called, and seeds `State`.
3. `handle_call/3` is "the most important bit" — one clause per request term defined in the interface.
4. `State` is the global server state, threaded as the last argument and the last (or second-last) return element.
5. `terminate/2` cannot return a new state — the server has already stopped — but knowing the final state is useful for restart logic.
6. The Emacs gen_server template supplies a comment-rich skeleton for all six.

# Construction / Recognition

## To Construct the Callbacks:
1. `init([]) -> {ok, State}.` — build and return the initial state.
2. Write one `handle_call({Tag, ...}, _From, State)` clause per request, returning `{reply, Reply, State1}`.
3. Provide default `handle_cast(_Msg, State) -> {noreply, State}.` and `handle_info(_Info, State) -> {noreply, State}.` if unused.
4. `terminate(_Reason, _State) -> ok.` for cleanup.
5. `code_change(_OldVsn, State, _Extra) -> {ok, State}.` for upgrades.

## To Recognize:
1. A module exporting `init/1, handle_call/3, handle_cast/2, handle_info/2, terminate/2, code_change/3` is a gen_server callback module.

# Context & Application

- **Typical contexts**: Every gen_server callback module.
- **Common applications**: `my_bank` fills in `handle_call/3` with `{new, Who}`, `{add, Who, X}`, `{remove, Who, X}`, and `stop` clauses.
- **Historical/stylistic notes**: `code_change/3` is exercised by the release-handling subsystem during a live software upgrade.

# Examples

**Example 1** ("Filling in the gen_server Template"): `my_bank`'s `handle_call` for stopping the server returns `{stop, normal, stopped, Tab}` — `normal` becomes the first argument to `terminate/2`, `stopped` becomes the return value of `my_bank:stop()`.

**Example 2** ("Step 3: Write the Callback Routines"): The mini-template defaults:

```erlang
init([]) -> {ok, State}.
handle_call(_Request, _From, State) -> {reply, Reply, State}.
handle_cast(_Msg, State) -> {noreply, State}.
handle_info(_Info, State) -> {noreply, State}.
terminate(_Reason, _State) -> ok.
code_change(_OldVsn, State, Extra) -> {ok, State}.
```

# Relationships

## Builds Upon
- **gen_server** — the callbacks are the contract the behaviour enforces.

## Enables
- **gen_server:call** — `handle_call/3` is the callback `call` triggers.
- **gen_server:cast** — `handle_cast/2` is the callback `cast` triggers.
- **handle_info** — the callback for spontaneous messages.

## Related
- **Hot code swapping** — `code_change/3` is the production equivalent of swapping a callback module.

## Contrasts With
- (No direct contrast within this chapter.)

# Common Errors

- **Error**: Returning a bare value from `handle_call` instead of a `{reply, ...}` tuple.
  **Correction**: `handle_call/3` must return one of the documented tuples (`{reply, Reply, State}`, `{noreply, State}`, `{stop, ...}`).

- **Error**: Trying to return new state from `terminate/2`.
  **Correction**: `terminate/2` cannot return state — the server has stopped; its return value is ignored.

# Common Confusions

- **Confusion**: Thinking `init/1` may return just `State`.
  **Clarification**: `init/1` must return `{ok, State}` (or `ignore`/`{stop, Reason}`); a bare `State` is wrong.

- **Confusion**: Believing `handle_info/2` is for cast messages.
  **Clarification**: `handle_info/2` handles only *spontaneous* messages — anything not sent via `gen_server:call` or `gen_server:cast`.

# Source Reference

Chapter 22: Introducing OTP, sections "Step 3: Write the Callback Routines", "The gen_server Callback Structure", "Filling in the gen_server Template". No page numbers (EPUB-origin source).

# Verification Notes

- Definition source: Direct quotes and template code from "The gen_server Callback Structure".
- Confidence rationale: HIGH — each callback's contract and return values are explicitly listed in the source templates.
- Uncertainties: None.
- Cross-reference status: Verified against planned cards in this batch.
- Re-extraction notes: Fresh extraction; no pre-existing card.
