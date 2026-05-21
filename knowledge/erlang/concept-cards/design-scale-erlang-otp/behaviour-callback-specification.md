---
# === CORE IDENTIFICATION ===
concept: Behaviour Callback Specification
slug: behaviour-callback-specification

# === CLASSIFICATION ===
category: otp-behaviours
subcategory: custom-behaviours
tier: advanced

# === PROVENANCE ===
source: "Designing for Scalability with Erlang/OTP"
source_slug: design-scale-erlang-otp
authors: "Francesco Cesarini & Steve Vinoski"
chapter: "Special Processes and Your Own Behaviors"
chapter_number: 9
pdf_page: 260
section: "An Example Handling TCP Streams"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "callback specification"
  - "-callback attribute"
  - "behavior_info/1"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - custom-behaviour
extends: []
related:
  - otp-behaviors
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How does a behavior relate to its callback module?"
  - "What is a callback module?"
---

# Quick Definition

A behaviour callback specification lists the callback functions a custom behavior's callback modules must export. It is written with `-callback` attributes (R15B+) or, in older releases, the `behavior_info(callbacks)` function.

# Core Definition

The callback specification lists the callback functions that need to be exported in the callback module, following the directives set out in the Erlang type and function specifications (Cesarini & Vinoski, p. 257). Callback specifications are mapped to the `behavior_info(callbacks)` function, which returns a list of `{Function, Arity}` tuples. You can bypass `-callback` specifications and directly implement and export `behavior_info/1` in the generic behavior module — this is how behaviors were required to be implemented prior to R15B. The advantage of `-callback` specifications over `behavior_info/1` is that the *dialyzer* tool will find discrepancies between callback modules and the specs (pp. 257-258).

# Prerequisites

- **Custom behaviour** — A callback specification is part of defining a custom behavior.

# Key Properties

1. Declares the callback functions a callback module must export.
2. Two forms: `-callback` attributes (R15B+) or the `behavior_info(callbacks)` function (older).
3. `behavior_info(callbacks)` returns a list of `{Function, Arity}` tuples.
4. `-callback` specs follow Erlang type and function specification syntax.
5. `-callback` specs enable *dialyzer* to detect discrepancies between callback modules and the behavior.
6. The dialyzer enables behavior callback warnings by default.

# Construction / Recognition

## To Construct/Create:
1. In the generic behavior module, write a `-callback` attribute for each callback function with its argument and return types.
2. Or, for older releases, export and define `behavior_info(callbacks) -> [{Function, Arity}, ...]`.

## To Identify/Recognize:
1. `-callback` attributes in the generic behavior module.
2. Or a `behavior_info/1` function returning `{Function, Arity}` tuples.

# Context & Application

- **Typical contexts**: The generic module of every user-defined behavior.
- **Common applications**: Telling the compiler and dialyzer which callbacks a callback module owes.
- **Historical/stylistic notes**: Before R15B, behaviors *had* to be defined with `behavior_info/1`; `-callback` specs are the modern, dialyzer-checkable replacement (p. 257).

# Examples

**Example 1** (p. 256): `tcp_wrapper` declares `-callback init_request() -> {'ok', Reply :: term()}.` and `-callback` specs for `get_request/2` and `stop_request/2`.

**Example 2** (p. 257): The older form — `behavior_info(callbacks) -> [{init_request, 0}, {get_request, 2}, {stop_request, 2}].`

## Worked Example

Both forms of the callback specification for `tcp_wrapper` (pp. 256-257):

```erlang
%% Modern form: -callback attributes (R15B+), dialyzer-checkable
-callback init_request() -> {'ok', Reply :: term()}.
-callback get_request(Data :: term(), LoopData :: term()) ->
    {'ok', Reply :: term()} |
    {'stop', Reason :: atom(), LoopData :: term()}.
-callback stop_request(Reason :: term(), LoopData :: term()) -> term().

%% Legacy form: behavior_info/1
behavior_info(callbacks) ->
    [{init_request, 0}, {get_request, 2}, {stop_request, 2}].
```

# Relationships

## Builds Upon
- *(none)*

## Enables
- *(none)*

## Related
- **OTP behaviour** — The callback specification is the contract between a behavior and its callback modules.

## Contrasts With
- *(none)*

# Common Errors

- **Error**: A callback module exporting callbacks whose arities do not match the specification.
  **Correction**: Match the `{Function, Arity}` pairs exactly; mismatches produce compiler warnings, and `-callback` specs let dialyzer catch type discrepancies.

# Common Confusions

- **Confusion**: Thinking `-callback` attributes and `behavior_info/1` do different things.
  **Clarification**: They serve the same purpose; `-callback` specs are the modern form and add dialyzer checking, while `behavior_info/1` is the pre-R15B equivalent.

# Source Reference

Chapter 9: Special Processes and Your Own Behaviors, "An Example Handling TCP Streams," pages 256-258.

# Verification Notes

- Definition source: Direct adaptation from p. 257.
- Confidence rationale: HIGH — explicitly defined with both the `-callback` and `behavior_info/1` forms shown.
- Uncertainties: None.
- Cross-reference status: Verified against planned card slugs for this source.
- Re-extraction notes: Fresh extraction — no pre-existing card for this source.
</content>
