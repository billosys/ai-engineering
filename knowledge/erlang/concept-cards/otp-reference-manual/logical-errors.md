---
# === CORE IDENTIFICATION ===
concept: Logical Errors
slug: logical-errors

# === CLASSIFICATION ===
category: error-handling
subcategory: error-types
tier: foundational

# === PROVENANCE ===
source: "Erlang Reference Manual"
source_slug: otp-reference-manual
authors: "Ericsson AB"
chapter: "Errors and Error Handling"
chapter_number: null
pdf_page: null
section: "Terminology"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "logic errors"
  - "semantic errors"
  - "bugs"

# === TYPED RELATIONSHIPS ===
prerequisites: []
extends: []
related:
  - compile-time-errors
  - runtime-errors
contrasts_with:
  - compile-time-errors
  - runtime-errors

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a logical error in Erlang?"
  - "How do logical errors differ from runtime errors?"
  - "Why don't logical errors cause crashes?"
---

# Quick Definition

Logical errors occur when a program does not behave as intended but does not crash. The code is syntactically valid and runs without exceptions, but produces incorrect results or fails to respond.

# Core Definition

Logical errors are one of four error types in Erlang. They occur when a program does not behave as intended but does not crash. An example given is that nothing happens when a button in a graphical user interface is clicked. Logical errors are not detected by the compiler or runtime system; they must be found through testing, debugging, and code review (Erlang Reference Manual, "Errors and Error Handling" chapter, "Terminology" section).

# Prerequisites

None.

# Key Properties

1. The program compiles and runs without crashing.
2. The behavior does not match the programmer's intent.
3. Not detectable by the compiler or runtime system.
4. Must be found through testing and debugging.
5. Cannot be caught with exception handling mechanisms.

# Construction / Recognition

## To Recognize:
1. The program runs but produces wrong results.
2. Expected behavior does not occur (e.g., a handler is missing or a condition is inverted).
3. No error messages or exceptions are raised.

# Context & Application

Logical errors are the most difficult category of errors to detect because the system provides no automatic feedback. They require careful testing, property-based testing, or formal verification to discover. In Erlang's "let it crash" philosophy, logical errors are distinct from crashes — they represent silently wrong behavior.

# Examples

**Example 1** (Terminology section): A GUI button click does nothing because the event handler is not connected:

```erlang
%% Intended: handle button click
%% Actual: handler registered for wrong event
init() ->
    Button = create_button(),
    register_handler(Button, on_hover, fun handle_click/1).
    %% Should be on_click, not on_hover — logical error
```

**Example 2**: Off-by-one error:

```erlang
%% Returns elements at indices 1..N but intended 0..N-1
take(N, List) ->
    lists:sublist(List, 2, N).  %% Should start at 1, not 2
```

# Relationships

## Related
- **compile-time-errors** — Caught by the compiler; logical errors are not.
- **runtime-errors** — Cause crashes; logical errors do not.

## Contrasts With
- **compile-time-errors** — Compile-time errors prevent execution; logical errors allow execution but produce wrong results.
- **runtime-errors** — Runtime errors crash the process; logical errors run silently with incorrect behavior.

# Common Errors

- **Error**: Assuming comprehensive test coverage guarantees no logical errors.
  **Correction**: Logical errors often hide in untested edge cases. Use property-based testing (PropEr) to explore input spaces systematically.

# Common Confusions

- **Confusion**: Thinking all bugs will cause crashes in Erlang.
  **Clarification**: Only runtime errors cause crashes. Logical errors produce silently wrong results.

# Source Reference

Erlang Reference Manual, "Errors and Error Handling" chapter, "Terminology" section.

# Verification Notes

- Definition source: Direct from source text
- Confidence rationale: High — directly defined in source
- Uncertainties: None
- Cross-reference status: Part of four-category error taxonomy in source
