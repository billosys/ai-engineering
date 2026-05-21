---
# === CORE IDENTIFICATION ===
concept: Error Return Tuple
slug: error-return-tuple

# === CLASSIFICATION ===
category: error-handling
subcategory: error-conventions
tier: intermediate

# === PROVENANCE ===
source: Programming Erlang, Second Edition
source_slug: programming-erlang
authors: Joe Armstrong
chapter: "Error Handling in Sequential Programs"
chapter_number: 6
pdf_page: null
section: "Programming Style with Exceptions"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "{ok, Value}"
  - "{error, Reason}"
  - tagged return value

# === TYPED RELATIONSHIPS ===
prerequisites:
  - exception
  - pattern-matching
related:
  - try-catch
  - let-it-crash
contrasts_with:
  - exception
  - let-it-crash

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "When should a function return {ok, Value} or {error, Reason}?"
  - "How do I decide between returning an error value and raising an exception?"
---

# Quick Definition

An error return tuple — `{ok, Value}` or `{error, Reason}` — is a convention for functions that have no "common case," forcing every caller to handle both outcomes explicitly.

# Core Definition

If a function does not really have a "common case," it should probably return something like `{ok, Value}` or `{error, Reason}`, but this forces all callers to do *something* with the return value. The caller then chooses between two alternatives: a `case` expression handling both `{ok, Val}` and `{error, Why}` branches, or a direct match `{ok, Val} = f(X)` that raises an exception if `f(X)` returns `{error, ...}`. By contrast, when errors are possible but rare, code is typically written to *expect* to handle them, using `try...catch` against matching `throw`s ("Error Handling in Sequential Programs," *Programming Style with Exceptions* — *Code Where Error Returns Are Common* and *Code Where Errors Are Possible but Rare*).

# Prerequisites

- **Exception** — The error-return convention is one of the two main alternatives to raising exceptions.
- **Pattern matching** — Callers consume error tuples by pattern matching, often in a `case`.

# Key Properties

1. Used when a function has no clear "common case" (success and failure are both expected).
2. Success is signaled as `{ok, Value}`; failure as `{error, Reason}`.
3. Forces every caller to handle the return value — it cannot be ignored.
4. A caller may handle both cases with a `case`, or match `{ok, Val} = f(X)` to turn `{error, ...}` into an exception.
5. For rare-but-possible errors, prefer `try...catch` with matching `throw`s instead.

# Construction / Recognition

## To Construct/Create:
1. Return `{ok, Value}` on success and `{error, Reason}` on failure.
2. In callers, either `case f(X) of {ok, Val} -> ...; {error, Why} -> ... end`, or match `{ok, Val} = f(X)` to crash on error.

## To Identify/Recognize:
1. A function whose contract documents both `{ok, _}` and `{error, _}` outcomes uses this convention.

# Context & Application

- **Typical contexts**: I/O and lookups where failure is a normal, expected outcome.
- **Common applications**: `file:read_file(File)` returns `{ok, Bin}` or `{error, Why}`.
- **Historical/stylistic notes**: Matching `{ok, Val} = f(X)` converts an unexpected `{error, ...}` into a crash, blending the two styles.

# Examples

**Example 1** (*Code Where Error Returns Are Common*): Handling both outcomes with a `case`.

```erlang
case f(X) of
    {ok, Val} ->
        do_some_thing_with(Val);
    {error, Why} ->
        %% ... do something with the error ...
end
```

**Example 2** (*Code Where Error Returns Are Common*): A direct match that raises an exception on error.

```erlang
{ok, Val} = f(X),
do_some_thing_with(Val)
```

**Example 3** (Exercise, *Fail Fast and Noisily, Fail Politely*): `file:read_file(File)` returns `{ok, Bin}` or `{error, Why}`.

# Relationships

## Builds Upon
- **Pattern matching** — Callers destructure error tuples by matching.

## Enables
- Explicit caller-side error handling for expected failures.

## Related
- **try...catch** — The preferred style when errors are possible but rare.
- **Let it crash** — Matching `{ok, Val} = f(X)` lets an unexpected error crash.

## Contrasts With
- **Exception** — Error tuples make failure a return value; exceptions make it a non-local jump.
- **Let it crash** — "Let it crash" suits invalid input; error tuples suit functions with no common case.

# Common Errors

- **Error**: Returning `{ok, Value}`/`{error, Reason}` for a function that has a clear common case.
  **Correction**: If there is a common case, return the value directly and raise an exception for the rare failure.

- **Error**: Ignoring the return value of an error-tuple function.
  **Correction**: The convention exists precisely to force the caller to handle both outcomes.

# Common Confusions

- **Confusion**: Thinking error tuples and exceptions are mutually exclusive.
  **Clarification**: They compose — matching `{ok, Val} = f(X)` deliberately turns an `{error, ...}` return into a raised exception.

# Source Reference

Chapter 6: Error Handling in Sequential Programs, section "Programming Style with Exceptions," subsections "Code Where Error Returns Are Common" and "Code Where Errors Are Possible but Rare." EPUB-origin source — no page numbers.

# Verification Notes

- Definition source: Direct adaptation of the "Code Where Error Returns Are Common" discussion.
- Confidence rationale: HIGH — the source explicitly describes the `{ok,...}`/`{error,...}` convention and its trade-offs.
- Uncertainties: None.
- Cross-reference status: Verified against planned cards.
- Re-extraction notes: Fresh extraction — no pre-existing card for this source.
