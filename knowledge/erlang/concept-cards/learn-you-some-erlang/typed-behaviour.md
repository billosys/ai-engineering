---
concept: Typed Behaviour
slug: typed-behaviour
category: data-types
subcategory: typespecs
tier: advanced
source: "Learn You Some Erlang for Great Good!"
source_slug: learn-you-some-erlang
authors: "Fred Hébert"
chapter: "Type Specifications and Dialyzer"
chapter_number: 30
pdf_page: null
section: "Typed Behaviors"
extraction_confidence: high
aliases:
  - "-callback attribute"
  - "typed behavior"
prerequisites:
  - type-annotation
  - otp-behaviour
related:
  - dialyzer
  - gen-server
contrasts_with: []
answers_questions:
  - "How are OTP behaviour callbacks given types?"
  - "What is the -callback module attribute?"
---

# Typed Behaviour

## Quick Definition

A typed behaviour is an OTP behaviour whose callback functions are declared with `-callback` attributes, giving Dialyzer type information to check callback modules.

## Core Definition

Originally, behaviours were declared with a `behavior_info/1` function listing callback names and arities, which gave Dialyzer no type information about the callbacks. Starting with R15B, the Erlang/OTP compiler handles a new module attribute, `-callback`, with a syntax similar to `-spec`. When callback function types are specified with `-callback`, the `behavior_info/1` function is declared automatically, and the specifications are added to module metadata so Dialyzer can check the types of callback module return values. A module cannot use both the `-callback` form and `behavior_info/1` at once — only one or the other (Chapter 30, "Typed Behaviors").

## Prerequisites

- **Type annotation** — `-callback` has a `-spec`-like syntax and reuses type specifications
- **OTP behaviour** — Typed behaviours are an enhancement of the behaviour mechanism

## Key Properties

1. `-callback` is a module attribute introduced in R15B for declaring callback types
2. Its syntax is similar to `-spec`
3. Using `-callback` automatically declares `behavior_info/1`
4. Callback type specs are added to module metadata, enabling Dialyzer to check callback modules
5. A module uses either `-callback` or `behavior_info/1`, never both
6. Standard OTP behaviours (e.g., `gen_server`) were rewritten with `-callback` declarations starting in R15B
7. Custom behaviours have a pre-R15 / post-R15 rift, since the two declaration styles are mutually exclusive

## Construction / Recognition

## To Type a Behaviour

1. For each callback, write `-callback Name(ArgTypes) -> ReturnTypes.` in the behaviour module
2. Do not also define `behavior_info/1` — it is generated automatically
3. Callback modules using `-behaviour(ModName)` are then checkable by Dialyzer

## Context & Application

Typed behaviours close the gap where Dialyzer could not verify that a callback module's functions returned the right types. The chapter contrasts the old `gen_server` `behavior_info/1` definition with the R15B `-callback` declarations for `init/1`, `handle_call/3`, `handle_cast/2`, `handle_info/2`, `terminate/2`, and `code_change/3`. A noted R15B-only bug: Dialyzer checked callback types only when the callback module used `-behaviour` (British spelling), not `-behavior`; this was later fixed.

## Examples

**Example** (Chapter 30, "Typed Behaviors"): the R15B `gen_server` declares
`-callback init(Args :: term()) -> {ok, State :: term()} | {ok, State :: term(), timeout() | hibernate} | {stop, Reason :: term()} | ignore.` and similar `-callback` lines for the other five callbacks.

## Relationships

## Builds Upon

- **OTP behaviour** — A typed behaviour is a behaviour with callback type declarations
- **Type annotation** — `-callback` reuses the `-spec`-style type syntax

## Related

- **Dialyzer** — Consumes `-callback` types to check callback modules
- **gen_server** — A standard behaviour rewritten with `-callback` declarations in R15B

## Common Errors

- **Error**: Defining both `-callback` attributes and `behavior_info/1` in the same module
  **Correction**: A module must use one or the other, not both

## Common Confusions

- **Confusion**: Assuming `-callback` works in any Erlang version
  **Clarification**: `-callback` was introduced in R15B; custom behaviours have a pre-R15/post-R15 compatibility rift

## Source Reference

Chapter 30: Type Specifications and Dialyzer, section "Typed Behaviors."

## Verification Notes

- Definition: Direct adaptation from "Typed Behaviors"
- Key Properties: All explicit in the chapter
- Confidence: HIGH — explicitly defined with the gen_server `-callback` example
- Cross-references: `otp-behaviour` and `gen-server` are shared slugs from Agent 2
