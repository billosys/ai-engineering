---
# === CORE IDENTIFICATION ===
concept: Swapping Event Handlers
slug: swapping-event-handlers

# === CLASSIFICATION ===
category: otp-behaviours
subcategory: event-handling
tier: advanced

# === PROVENANCE ===
source: Designing for Scalability with Erlang/OTP
source_slug: design-scale-erlang-otp
authors: Francesco Cesarini & Steve Vinoski
chapter: "Event Handlers"
chapter_number: 6
pdf_page: 179
section: "Swapping Event Handlers"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "swap_handler"
  - "gen_event:swap_handler"
  - "swap_sup_handler"
  - handler swapping

# === TYPED RELATIONSHIPS ===
prerequisites:
  - event-handler
extends: []
related:
  - supervised-event-handlers
  - alarm-handler
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is an event handler (gen_event)?"
  - "How do I perform a release upgrade?"
---

# Quick Definition

Swapping event handlers replaces one handler with another at runtime via `gen_event:swap_handler/3`, passing the old handler's terminating state into the new handler's `init` function so no events are lost.

# Core Definition

"The event manager provides functionality to swap handlers during runtime. It allows a handler to pass its state to a new handler, ensuring that no events are lost in the process" (Cesarini & Vinoski, p. 179). The second parameter of `gen_event:swap_handler/3` is a tuple `{OldMod, Args1}` — the handler to replace plus the arguments for its `terminate` function. The third is `{NewMod, Args2}` — the new handler's callback module plus arguments for its `init` function. "The `terminate` callback function in the old handler is first called. Its return value, `Res`, is passed in a tuple together with the arguments intended for the `init` function of the new handler" — i.e., the new handler's `init` receives `{Args2, Res}` (pp. 179-180). To swap and start supervising the connection, use `gen_event:swap_sup_handler/3`; the handler being swapped need not itself have been supervised.

# Prerequisites

- **Event handler** — Swapping replaces one handler with another; you must understand handlers and their `init`/`terminate` callbacks.

# Key Properties

1. `gen_event:swap_handler(Name, {OldMod, Args1}, {NewMod, Args2})` replaces a handler at runtime.
2. The old handler's `terminate(Args1, LoopData)` is called first, returning `Res`.
3. The new handler's `init` receives `{Args2, Res}` — old state handed over to the successor.
4. No events are lost during the swap.
5. `gen_event:swap_sup_handler/3` swaps *and* sets up supervision of the new handler.
6. The handler being swapped need not have been supervised.

# Construction / Recognition

## To Swap a Handler:
1. Extend the old handler's `terminate/2` to handle the swap reason, returning state `Res`.
2. Extend the new handler's `init/1` to accept `{Args2, Res}` and adopt the handed-over state.
3. Call `gen_event:swap_handler(Name, {OldMod, Args1}, {NewMod, Args2})`.

# Context & Application

- **Typical contexts**: Runtime reconfiguration and handler upgrades without losing events.
- **Common applications**: Flipping the `logger` handler between logging to a file and printing to standard I/O; swapping the SASL `alarm_handler`.
- **Historical/stylistic notes**: The book extends the `logger` so the swapped-from handler does *not* close the file — it lets the successor decide what to do with it (p. 180).

# Examples

**Example 1** (p. 180): The `logger` handler's swap-aware `init/1` and `terminate/2`:

```erlang
init({standard_io, {Fd, Count}}) when is_pid(Fd) ->
    file:close(Fd),
    {ok, {standard_io, Count}};
init({File, {standard_io, Count}}) when is_list(File) ->
    {ok, Fd} = file:open(File, write),
    {ok, {Fd, Count}};
...
terminate(swap, {Type, Count}) ->
    {Type, Count};
```

**Example 2** (p. 184): Swapping the SASL alarm handler:

```erlang
gen_event:swap_handler(alarm_handler,
                       {alarm_handler, swap}, {NewHandler, Args})
```

The new handler's `init` matches `{Args, {alarm_handler, Alarms}}`.

# Relationships

## Builds Upon
- **Event handler** — A swap replaces one event handler with another.

## Enables
- **alarm-handler** — The SASL `alarm_handler` is designed to be replaced via `swap_handler/3`.

## Related
- **supervised-event-handlers** — `swap_sup_handler/3` is the supervised variant of swapping.

## Contrasts With
- *(None.)*

# Common Errors

- **Error**: Closing or freeing a resource in the old handler's `terminate` before the successor has taken over.
  **Correction**: When swapping, hand the resource state to the new handler in `Res` and let *it* decide; e.g., the `logger` does not close the file on `terminate(swap, ...)`.

# Common Confusions

- **Confusion**: Thinking the new handler's `init` receives only `Args2`.
  **Clarification**: During a swap, the new handler's `init` receives the tuple `{Args2, Res}`, where `Res` is the old handler's terminating state.

# Source Reference

Chapter 6: Event Handlers, Section "Swapping Event Handlers," pages 179-181. See Figure 7-8; SASL swap example on page 184.

# Verification Notes

- Definition source: Direct quotes from pp. 179-180.
- Confidence rationale: HIGH — the source explicitly defines `swap_handler/3`, the parameter tuples, and the state hand-over.
- Uncertainties: None.
- Cross-reference status: Verified against planned cards in this batch.
- Re-extraction notes: Fresh extraction; no pre-existing card for this source.
