---
# === CORE IDENTIFICATION ===
concept: Custom Behaviour
slug: custom-behaviour

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
section: "Your Own Behaviors"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "user-defined behavior"
  - "your own behavior"
  - "custom OTP behaviour"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - special-process
  - otp-behaviors
extends: []
related:
  - behaviour-callback-specification
  - proc-lib
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is an OTP behavior?"
  - "How does a behavior relate to its callback module?"
  - "What is a callback module?"
---

# Quick Definition

A custom behaviour is a user-defined OTP behavior: code split into a generic module (named after the behavior) and specific callback modules, created when a recurring process pattern cannot be expressed with the standard behaviors.

# Core Definition

You implement your own behavior by splitting the code into generic and specific parts (Cesarini & Vinoski, p. 251). You want to do this when several processes follow a pattern that cannot be expressed using existing OTP behaviors, and when the generic part is substantial enough to make it worthwhile. The rules for creating a behavior are: the name of the generic module must be the same as the behavior name; you must list the callback functions in the behavior module; and your callback module must include the `-behavior(BehaviorName).` directive. Once the generic behavior is compiled, compiling callback modules with the behavior directive produces warnings if any callbacks are omitted. Custom behaviors should follow the design rules of special processes, using the `sys` and `proc_lib` modules (pp. 252-253).

# Prerequisites

- **Special process** — A custom behavior must follow the special-process design rules (`sys`, `proc_lib`).
- **OTP behaviour** — A custom behavior is an OTP behavior; understanding the generic/specific split is required.

# Key Properties

1. Code is split into a generic module and one or more specific callback modules.
2. The generic module's name must equal the behavior name.
3. The behavior module lists the callback functions.
4. Callback modules include `-behavior(BehaviorName).`
5. Omitting a required callback produces a compiler warning.
6. The generic behavior module must be compiled and on the code path before its callback modules.
7. Should be built on `gen` or follow special-process rules (`sys`, `proc_lib`).

# Construction / Recognition

## To Construct/Create:
1. Separate the recurring pattern into generic code and specific callbacks.
2. Put the generic code in a module named after the behavior; follow special-process design rules.
3. List the callback functions (via `-callback` specs or `behavior_info/1`).
4. In each callback module, add `-behavior(YourBehavior).` and export the callbacks.
5. Compile the generic module first, then the callback modules.

## To Identify/Recognize:
1. A generic module that lists callbacks and is referenced by `-behavior` directives.
2. Callback modules implementing those callbacks.

# Context & Application

- **Typical contexts**: Abstracting a recurring concurrency pattern not covered by `gen_server`/`gen_statem`/`gen_event`.
- **Common applications**: A TCP-stream wrapper exposing only received data to callback modules.
- **Historical/stylistic notes**: The book warns against overengineering — most needs are met by standard behaviors; it also notes current OTP behaviors are built on the undocumented `gen` module, which you may use at your own risk (p. 252).

# Examples

**Example 1** (pp. 254-256): `tcp_wrapper` — a custom behavior wrapping TCP streams; the callback module `tcp_print` declares `-behavior(tcp_wrapper).` and implements `init_request/0`, `get_request/2`, `stop_request/2`.

## Worked Example

A callback module of a custom behavior (p. 254):

```erlang
-module(tcp_print).
-export([init_request/0, get_request/2, stop_request/2]).
-behavior(tcp_wrapper).

init_request() ->
    io:format("Receiving Data~n."),
    {ok,[]}.

get_request(Data, Buffer)->
    io:format("."),
    {ok, [Data|Buffer]}.

stop_request(_Reason, Buffer) ->
    io:format("~n"),
    io:format(lists:reverse(Buffer)),
    io:format("~n").
```

# Relationships

## Builds Upon
- *(none)*

## Enables
- *(none)*

## Related
- **Behaviour callback specification** — A custom behavior declares its callbacks via `-callback` specs or `behavior_info/1`.
- **proc_lib** — A custom behavior should follow the special-process rules built on `proc_lib` and `sys`.

## Contrasts With
- *(none)*

# Common Errors

- **Error**: Naming the generic module differently from the behavior.
  **Correction**: The generic module's name must equal the behavior name used in `-behavior(...)`.

- **Error**: Compiling callback modules before the generic behavior module is available.
  **Correction**: Compile and make the generic module available on the code path first, or you get an undefined-behavior warning.

# Common Confusions

- **Confusion**: Thinking you should write a new behavior for every project.
  **Clarification**: Standard behaviors meet most needs; write a custom behavior only when the generic part is substantial and the pattern truly cannot be expressed otherwise.

# Source Reference

Chapter 9: Special Processes and Your Own Behaviors, "Your Own Behaviors," "Rules for Creating Behaviors," and "An Example Handling TCP Streams," pages 251-258.

# Verification Notes

- Definition source: Direct adaptation from pp. 251-253.
- Confidence rationale: HIGH — explicitly defined with the creation rules and the `tcp_wrapper`/`tcp_print` example.
- Uncertainties: None.
- Cross-reference status: Verified against planned card slugs for this source.
- Re-extraction notes: Fresh extraction — no pre-existing card for this source.
</content>
