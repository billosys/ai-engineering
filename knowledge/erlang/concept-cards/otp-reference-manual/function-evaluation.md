---
# === CORE IDENTIFICATION ===
concept: Function Evaluation
slug: function-evaluation

# === CLASSIFICATION ===
category: functions-pattern-matching
subcategory: function-declarations
tier: foundational

# === PROVENANCE ===
source: "Erlang Reference Manual"
source_slug: otp-reference-manual
authors: "Ericsson AB"
chapter: "Functions"
chapter_number: null
pdf_page: null
section: "Function Evaluation"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "clause selection"
  - "function dispatch"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - function-declaration
  - function-clause
  - pattern-matching
extends: []
related:
  - function-arity
  - function-calls
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How does Erlang evaluate a function call?"
  - "What happens when no function clause matches?"
  - "In what order are function clauses tried?"
---

# Quick Definition

When a function `M:F/N` is called, the runtime locates the function, then scans clauses sequentially until one is found whose patterns match the arguments and whose guard sequence is true. The matching clause's body is evaluated and the last expression's value is returned.

# Core Definition

The Erlang Reference Manual describes function evaluation: "When a function `M:F/N` is called, first the code for the function is located. If the function cannot be found, an `undef` runtime error occurs. Notice that the function must be exported to be visible outside the module it is defined in." Then: "the function clauses are scanned sequentially until a clause is found that fulfills both of the following two conditions: 1. The patterns in the clause head can be successfully matched against the given arguments. 2. The guard sequence, if any, is true." If no clause matches: "a `function_clause` runtime error occurs." If a clause matches: "the corresponding clause body is evaluated. That is, the expressions in the body are evaluated sequentially and the value of the last expression is returned." (Erlang Reference Manual, "Functions", "Function Evaluation").

# Prerequisites

- **function-declaration** -- Must understand function structure to understand evaluation
- **function-clause** -- Evaluation works by scanning clauses
- **pattern-matching** -- Clause selection depends on pattern matching against arguments

# Key Properties

1. Function code is located first; if not found, `undef` runtime error occurs
2. Functions must be exported to be called from outside their module
3. Clauses are scanned sequentially (top to bottom)
4. A clause matches when: (a) all patterns match the arguments AND (b) the guard sequence is true
5. If no clause matches, a `function_clause` runtime error occurs
6. The body of the matching clause is evaluated sequentially
7. The return value is the value of the last expression in the body

# Construction / Recognition

## To Identify/Recognize:
1. A `function_clause` error indicates no clause matched the call arguments
2. An `undef` error indicates the function could not be found (missing export or wrong module)
3. The order of clauses matters -- the first matching clause wins

# Context & Application

Understanding evaluation order is crucial for writing correct multi-clause functions. The sequential scan means more specific clauses should appear before more general ones. The two-step process (pattern match, then guard check) means guards only run after patterns succeed.

# Examples

**Example 1** (Function Evaluation section): Evaluating `mod:fact(1)`:
```erlang
-module(mod).
-export([fact/1]).

fact(N) when N > 0 ->
    N * fact(N - 1);
fact(0) ->
    1.
```

"Evaluation starts at the first clause. The pattern `N` is matched against argument 1. The matching succeeds and the guard (`N > 0`) is true, thus `N` is bound to 1, and the corresponding body is evaluated: `N * fact(N-1)` => `1 * fact(0)`."

**Example 2** (Function Evaluation section): "Now, `fact(0)` is called, and the function clauses are scanned sequentially again. First, the pattern `N` is matched against 0. The matching succeeds, but the guard (`N > 0`) is false. Second, the pattern `0` is matched against the argument `0`. The matching succeeds and the body is evaluated."

**Example 3** (Function Evaluation section): "If `mod:fact/1` is called with a negative number as argument, no clause head matches. A `function_clause` runtime error occurs."

# Relationships

## Builds Upon
- **function-declaration** -- Evaluation operates on declared functions
- **function-clause** -- Evaluation scans clauses sequentially
- **pattern-matching** -- Pattern matching determines clause selection

## Enables
- **tail-recursion** -- Understanding evaluation enables understanding of tail call optimization

## Related
- **function-calls** -- Calls trigger evaluation

# Common Errors

- **Error**: Placing a general catch-all clause before more specific clauses
  **Correction**: Put specific clauses first; the first matching clause wins due to sequential scanning

- **Error**: Forgetting to export a function that needs to be called from another module
  **Correction**: Add the function to the `-export` attribute; unexported functions cause `undef` errors when called externally

# Common Confusions

- **Confusion**: Thinking all matching clauses are evaluated
  **Clarification**: Only the first matching clause is evaluated; once a clause matches, the remaining clauses are ignored

# Source Reference

"Functions" chapter, section "Function Evaluation", including the detailed `fact(1)` walkthrough.

# Verification Notes

- Definition source: Direct quotes from source with step-by-step evaluation example
- Confidence rationale: HIGH -- explicit description with worked example in source
- Uncertainties: None
- Cross-reference status: Verified against planned slugs
