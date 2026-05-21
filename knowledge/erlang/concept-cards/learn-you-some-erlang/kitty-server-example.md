---
concept: Kitty Server Example
slug: kitty-server-example
category: otp-behaviours
subcategory: worked-examples
tier: intermediate
source: "Learn You Some Erlang for Great Good!"
source_slug: learn-you-some-erlang
authors: "Fred Hébert"
chapter: "An Introduction to OTP"
chapter_number: 14
pdf_page: null
section: "Introducing the Kitty Server"
extraction_confidence: high
aliases:
  - "kitty server"
  - "kitty_server"
  - "kitty_gen_server"
prerequisites:
  - client-server-pattern
  - gen-server
extends: []
related:
  - the-otp-way
contrasts_with: []
answers_questions:
  - "How does refactoring a server into a gen_server work?"
  - "What does a gen_server callback module look like end to end?"
---

# Kitty Server Example

## Quick Definition

The kitty server is chapter 14's worked example: a tiny cat-store server, written three times — naive, then on a hand-built generic `my_server`, then as a full `gen_server` — to show how OTP separates generic from specific code.

## Core Definition

The kitty server is "a very simple server, allowing us to focus on its essential properties": you describe a cat and get that cat; a returned cat is added to a list and handed out before new orders. The chapter implements it in three stages. (1) `kitty_server` — naive: every synchronous call sets up monitors, timeouts, and `receive` by hand. (2) `kitty_server2` paired with a hand-written generic `my_server` — the repeated machinery (the `call/2` function and the receive loop) is extracted, and the kitty code becomes a callback module implementing `init/1`, `handle_call/3`, `handle_cast/2`. (3) `kitty_gen_server` — the same callback module rewritten against the OTP `gen_server` behaviour, declaring `-behavior(gen_server)` and implementing all six callbacks. Each stage produces the same behavior with progressively less and safer code, demonstrating the OTP generic/specific split concretely (Hébert, ch. 14, "The Basic Server," ".BEAM Me Up, Scotty!").

## Prerequisites

- **Client/server pattern** — The kitty server is an instance of that pattern
- **gen_server** — The final version is a `gen_server` callback module

## Key Properties

1. A minimal server: order a cat (synchronous), return a cat (asynchronous), close shop (synchronous)
2. Implemented three times: naive, on hand-built `my_server`, and on OTP `gen_server`
3. The naive version repeats monitor/timeout/receive code in every call
4. `my_server` extracts the generic `call`/`cast`/loop; the kitty code becomes a callback module
5. The `gen_server` version declares `-behavior(gen_server)` and implements six callbacks
6. Each refactoring keeps identical behavior with shorter, safer code
7. A returned cat is handed out before fulfilling new orders (stock-emptying behavior)

## Construction / Recognition

## To Follow the Kitty Server Refactoring

1. Start with a naive server that hand-codes monitors, timeouts, and the loop
2. Extract the synchronous-call helper and the loop into a generic module
3. Rewrite the server as a callback module implementing `init`/`handle_call`/`handle_cast`
4. Swap the hand-built generic module for OTP's `gen_server`, declaring the behaviour
5. Implement the remaining callbacks (`handle_info`, `terminate`, `code_change`)

## Examples

> **Naive call** (ch. 14): `order_cat/4` sets up `erlang:monitor`, sends, and `receive`s with a 5-second timeout — all by hand.
>
> **gen_server version** (ch. 14): `handle_call({order, ...}, _From, Cats) -> {reply, make_cat(...), Cats}` — "the code is now shorter, thanks to smarter abstractions."

## Relationships

## Builds Upon

- **Client/server pattern** — The kitty server instantiates it
- **gen_server** — The final implementation target

## Related

- **The OTP way** — The kitty server is the chapter's vehicle for demonstrating OTP's philosophy

## Common Errors

- **Error**: Leaving `ok` instead of `exit(normal)` / a `stop` tuple in the terminate path
  **Correction**: The chapter notes you must replace `ok` with `exit(normal)` (or a `stop` tuple) or the server keeps running

## Common Confusions

- **Confusion**: Thinking the three versions behave differently
  **Clarification**: All three produce the same observable behavior; only the amount and safety of code differs

## Source Reference

Chapter 14, "An Introduction to OTP," sections "The Basic Server," "Specific vs. Generic," ".BEAM Me Up, Scotty!".

## Verification Notes

- Three-stage refactoring: directly from ch. 14
- Confidence: HIGH — the chapter is a fully worked example
