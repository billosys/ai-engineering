---
# === CORE IDENTIFICATION ===
concept: No Return Type
slug: no-return-type

# === CLASSIFICATION ===
category: functions-pattern-matching
subcategory: type-annotations
tier: intermediate

# === PROVENANCE ===
source: "Erlang Reference Manual"
source_slug: otp-reference-manual
authors: "Ericsson AB"
chapter: "Types and Function Specifications"
chapter_number: null
pdf_page: null
section: "Specifications for Functions"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "no_return()"
  - "never-returning function"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - function-specification
  - none-type
extends: []
related:
  - built-in-type-aliases
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I write a type specification for a function?"
---

# Quick Definition
`no_return()` is the recommended return type for functions that never return normally, such as server loops, exception throwers, or functions calling `exit/1`. It is an alias for `none()`.

# Core Definition
"Some functions in Erlang are not meant to return; either because they define servers or because they are used to throw exceptions." For such functions, "it is recommended to use the special `no_return()` type for their 'return', through a contract of the following form: `-spec my_error(term()) -> no_return().`" (Erlang Reference Manual, "Specifications for Functions").

# Prerequisites
- **function-specification** -- `no_return()` is used in spec return positions
- **none-type** -- `no_return()` is an alias for `none()`

# Key Properties
1. `no_return()` is an alias for `none()` (the bottom type)
2. Used for functions that always throw exceptions, exit, or loop forever
3. Signals to Dialyzer that the function's return value will never be used
4. Common for server loop functions, error throwers, and process terminators

# Construction / Recognition
## To Construct:
1. Write a spec with `no_return()` as the return type
2. Example: `-spec my_error(term()) -> no_return().`

## To Identify/Recognize:
1. `no_return()` in the return position of a `-spec`
2. The function body always throws, exits, or loops

# Context & Application
Using `no_return()` is important for Dialyzer accuracy. When Dialyzer sees a function specified with `no_return()`, it knows that any code after a call to that function is unreachable. Without this annotation, Dialyzer might report false warnings about unreachable code or try to infer a return type from the throw/exit.

# Examples
**Example 1** (Specifications for Functions):
```erlang
my_error(Err) -> throw({error, Err}).
```
Recommended spec:
```text
-spec my_error(term()) -> no_return().
```

# Relationships
## Builds Upon
- **function-specification** -- Used in spec return position
- **none-type** -- `no_return()` is an alias for `none()`

## Enables
Accurate Dialyzer analysis of unreachable code paths.

## Related
- **built-in-type-aliases** -- `no_return()` is listed in the aliases table

## Contrasts With
None within this source.

# Common Errors
- **Error**: Using `no_return()` for a function that sometimes returns normally
  **Correction**: `no_return()` means the function NEVER returns. If it sometimes returns, use a proper return type

# Common Confusions
- **Confusion**: Thinking `no_return()` means "returns nothing" (like `void` in C)
  **Clarification**: `no_return()` means the function never completes normally. For functions that return but produce no useful value, use `ok` as the return type

# Source Reference
"Types and Function Specifications" chapter, section "Specifications for Functions."

# Verification Notes
- Definition source: Direct from source text with example
- Confidence rationale: High -- explicit recommendation with example
- Uncertainties: None
- Cross-reference status: All slugs verified against planned cards
