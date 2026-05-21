---
# === CORE IDENTIFICATION ===
concept: Fail Fast and Noisily
slug: fail-fast-and-noisily

# === CLASSIFICATION ===
category: error-handling
subcategory: error-philosophy
tier: foundational

# === PROVENANCE ===
source: Programming Erlang, Second Edition
source_slug: programming-erlang
authors: Joe Armstrong
chapter: "Error Handling in Sequential Programs"
chapter_number: 6
pdf_page: null
section: "Fail Fast and Noisily, Fail Politely"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - let it crash
  - fail fast
  - fail politely

# === TYPED RELATIONSHIPS ===
prerequisites: []
extends: []
related:
  - exception
  - throw-exit-error
  - error-logger
contrasts_with:
  - error-return-tuple

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the let it crash philosophy?"
  - "How should I code for errors in Erlang?"
  - "What does fail politely mean?"
---

# Quick Definition

"Fail fast and noisily, fail politely" is Erlang's error-coding philosophy: crash immediately with a meaningful, logged error message rather than continuing in a broken state, while shielding end users from raw error detail.

# Core Definition

The book states two key principles for coding for errors ("Error Handling in Sequential Programs", *Fail Fast and Noisily, Fail Politely*). First, "we should fail as soon as an error occurs, and we should fail noisily" — failing silently and trying to patch up the error "results in code that is a nightmare to debug." When an error is detected, "the correct approach is to crash immediately and generate a meaningful error message. We crash immediately so as not to make matters worse." Second, "fail politely means that only the programmer should see the detailed error messages... A user of the program should never see these messages" but should be alerted that an error occurred and told what they can do. This is the same rule the book elsewhere calls "Let it crash": never return a value when a function is called with an incorrect argument — raise an exception and assume the caller will fix it.

# Prerequisites

This is a foundational philosophy with no prerequisites within this source.

# Key Properties

1. Fail as soon as an error is detected — do not continue.
2. Fail noisily — generate a meaningful, detailed error message.
3. Crash immediately so as not to make matters worse.
4. Detailed error messages go to a permanent log file, not the screen, so they are never lost.
5. Fail politely — end users see only an alert and a remedy, never the raw detail.
6. Never return a value for invalid arguments; raise an exception.

# Construction / Recognition

## To Construct/Create:
1. Describe function behavior only for valid inputs; let invalid inputs raise exceptions automatically.
2. Where an error is detected by program logic, raise an exception rather than patching and continuing.
3. Route detailed error messages to a permanent error log.
4. Present users with a polite message and a suggested action.

## To Identify/Recognize:
1. Code that follows this philosophy has no defensive "fix-up-and-continue" branches; it crashes on bad input.

# Context & Application

- **Typical contexts**: all sequential Erlang code; the foundation extended to concurrent error handling later in the book.
- **Common applications**: pairing crashes with a permanent error log; separating developer detail from user-facing messages.
- **Historical/stylistic notes**: "Error messages are gold dust for programmers. They should never scroll up the screen to vanish forever" — they belong in a log file readable later.

# Examples

**Example 1** (*Handling Errors in Sequential Code*): the runtime fails fast on a missing clause rather than guessing a value:

```erlang
2> shop:cost(socks).
** exception error: no function clause matching
shop:cost(socks) (shop.erl, line 5)
```

There is no sensible value for `cost(socks)`, so the system crashes immediately with a meaningful message instead of returning a bogus value.

**Example 2** (*Fail Fast and Noisily, Fail Politely*, Exercise 2): the book asks the reader to rewrite `try_test.erl` to produce two messages — a polite one for the user and a detailed one for the developer — illustrating "fail politely".

# Relationships

## Builds Upon
- This is a foundational philosophy.

## Enables
- This concept does not have downstream cards in scope within these chapters.

## Related
- **Exception** — Failing fast means raising an exception on detecting an error.
- **throw/exit/error** — The BIFs used to fail noisily with a meaningful reason.
- **Error logger** — Detailed error messages should be written to a permanent log.

## Contrasts With
- **Error return tuple** — Returning `{error, Reason}` is appropriate when errors are common; the fail-fast rule says never return a value for *invalid* arguments — raise an exception instead.

# Common Errors

- **Error**: Catching an error, patching the state, and continuing.
  **Correction**: Crash immediately so as not to make matters worse; let the caller decide what to do.

- **Error**: Printing detailed crash output to the user's screen.
  **Correction**: Send detailed messages to a permanent log; show the user only an alert and a remedy.

# Common Confusions

- **Confusion**: Thinking "let it crash" means error handling is neglected.
  **Clarification**: It means errors are detected and surfaced immediately and loudly, then handled by a caller (or supervisor) — not ignored.

- **Confusion**: Believing "fail noisily" and "fail politely" contradict each other.
  **Clarification**: They address different audiences — noisy detail for the developer's log, polite brevity for the user.

# Source Reference

Chapter 6: "Error Handling in Sequential Programs", sections "Fail Fast and Noisily, Fail Politely" and "Handling Errors in Sequential Code" (the "Let it crash" rule).

# Verification Notes

- Definition source: Direct quotation and adaptation from *Fail Fast and Noisily, Fail Politely*.
- Confidence rationale: HIGH — the source states the two principles explicitly and in detail.
- Uncertainties: None.
- Cross-reference status: Slugs `exception`, `throw-exit-error` extracted in this chapter; `error-logger`, `error-return-tuple` exist.
- Re-extraction notes: Fresh extraction; no prior card content merged.
