---
# === CORE IDENTIFICATION ===
concept: Underscore-Prefixed Variables
slug: underscore-prefixed-variables

# === CLASSIFICATION ===
category: functions-pattern-matching
subcategory: expressions
tier: foundational

# === PROVENANCE ===
source: "Erlang Reference Manual"
source_slug: otp-reference-manual
authors: "Ericsson AB"
chapter: "Expressions"
chapter_number: null
pdf_page: null
section: "Variables"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "underscore variables"
  - "warning-suppressed variables"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - variables
  - anonymous-variable
extends:
  - variables
related:
  - pattern-matching
contrasts_with:
  - anonymous-variable

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What does a variable starting with underscore mean in Erlang?"
  - "How do I suppress unused variable warnings?"
  - "Is _X the same as _ in Erlang?"
---

# Quick Definition

Variables starting with underscore followed by a name (e.g., `_Height`) are normal variables that bind values and participate in matching, but the compiler does not generate unused-variable warnings for them.

# Core Definition

The Erlang Reference Manual states: "Variables starting with underscore (`_`), for example, `_Height`, are normal variables, not anonymous. However, they are ignored by the compiler in the sense that they do not generate warnings." The source further demonstrates that "since variables starting with an underscore are not anonymous," multiple occurrences of the same `_Name` must match the same value (Erlang Reference Manual, "Expressions", "Variables").

# Prerequisites

- **variables** -- Underscore-prefixed variables are a variant of regular variables
- **anonymous-variable** -- Must understand the anonymous variable to distinguish from it

# Key Properties

1. Variables like `_Elem`, `_Height` are normal variables with names
2. They bind to values through pattern matching (unlike anonymous `_`)
3. The compiler does not warn if they are unused
4. Multiple occurrences of the same `_Name` must match the same value
5. They are useful for documenting the meaning of ignored positions

# Construction / Recognition

## To Construct/Create:
1. Start the variable name with underscore followed by a descriptive name
2. Example: `_Elem`, `_Height`, `_Reason`

## To Identify/Recognize:
1. A variable starting with `_` followed by one or more characters
2. Distinct from the bare `_` (anonymous variable)

# Context & Application

Underscore-prefixed variables are a documentation technique: they give a meaningful name to a position in a pattern (improving readability) while suppressing compiler warnings when the value is not used. This is preferred over the anonymous variable when the name helps explain the code structure.

# Examples

**Example 1** (Variables section): Improving readability while suppressing warnings:
```erlang
member(_, []) ->    %% anonymous: no hint about what the first arg is
    [].

member(Elem, []) -> %% readable but generates unused variable warning
    [].

member(_Elem, []) -> %% readable AND no warning
    [].
```

**Example 2** (Variables section): Underscore-prefixed variables bind and assert:
```erlang
{_,_} = {1,2}     %% succeeds: each _ is independent
{_N,_N} = {1,2}   %% FAILS: _N binds to 1, then cannot match 2
```

# Relationships

## Builds Upon
- **variables** -- These are regular variables with a naming convention

## Contrasts With
- **anonymous-variable** -- `_` is truly anonymous (never binds); `_Name` binds normally

## Related
- **pattern-matching** -- Underscore-prefixed variables participate fully in pattern matching
- **single-assignment** -- The same `_Name` appearing twice must match the same value

# Common Errors

- **Error**: Using the same `_Name` in multiple positions expecting independent matching (like `_`)
  **Correction**: `{_N, _N} = {1, 2}` fails because `_N` binds to `1` and cannot match `2`. Use different names or bare `_` for independent positions.

# Common Confusions

- **Confusion**: Treating `_Name` as anonymous/non-binding like bare `_`
  **Clarification**: `_Name` is a normal variable that binds; only bare `_` is anonymous. The underscore prefix only suppresses unused-variable warnings.

# Source Reference

"Expressions" chapter, section "Variables", paragraphs on underscore-prefixed variables with the `member/2` and `{_N,_N}` examples.

# Verification Notes

- Definition source: Direct quotes from source text with examples
- Confidence rationale: HIGH -- explicit definition with positive and negative examples
- Uncertainties: None
- Cross-reference status: Verified against planned slugs
