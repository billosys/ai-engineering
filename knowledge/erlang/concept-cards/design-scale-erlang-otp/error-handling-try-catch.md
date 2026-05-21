---
# === CORE IDENTIFICATION ===
concept: Error Handling with Try-Catch
slug: error-handling-try-catch

# === CLASSIFICATION ===
category: error-handling
subcategory: exceptions
tier: intermediate

# === PROVENANCE ===
source: "Designing for Scalability with Erlang/OTP"
source_slug: design-scale-erlang-otp
authors: "Francesco Cesarini & Steve Vinoski"
chapter: "Introducing Erlang"
chapter_number: 1
pdf_page: 40
section: "Fail Safe!"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - try-catch
  - exception handling
  - let it fail
  - let it crash

# === TYPED RELATIONSHIPS ===
prerequisites:
  - pattern-matching
extends: []
related:
  - links
  - exit-signals
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How does Erlang handle errors in sequential code?"
  - "What is the let-it-fail philosophy?"
  - "What are the kinds of Erlang exceptions?"
---

# Quick Definition

The try-catch construct handles exceptions in sequential Erlang code, letting you match on different exception classes. It supports the "let it fail" philosophy, where code deals only with the correct case.

# Core Definition

"The Erlang design philosophy says 'let it fail!' so that a function, process, or other running entity deals only with the correct case and leaves it to other parts of the system ... to deal with failure" (Cesarini & Vinoski, p. 35). "One way of dealing with failure in sequential code is to use the mechanism for exception handling given by the try-catch construct" (p. 35). "The try-catch construct gives the user the opportunity to match on the different kinds of exceptions in the clauses, handling them individually. ... There are also exit and throw exceptions, the first being the result of a process calling the exit BIF and the latter the result of a user-generated exception using the throw expression" (p. 36). The three exception classes are `error`, `exit`, and `throw`.

# Prerequisites

- **Pattern matching** — `catch` clauses match on `Class:Reason` patterns to select handling.

# Key Properties

1. Three exception classes exist: `error`, `exit`, and `throw`.
2. `catch` clauses pattern-match `Class:Reason` to handle exceptions individually.
3. An `error` exception arises from runtime errors such as a pattern-match or `function_clause` failure.
4. An `exit` exception results from a process calling the `exit` BIF.
5. A `throw` exception results from a user `throw` expression.
6. "Let it fail" means *avoiding* defensive code that mixes correct computation with error handling.

# Construction / Recognition

## To Construct:
1. Wrap the risky expression in `try Expr catch ... end`.
2. Write `catch` clauses, optionally qualified by class, e.g., `error:Reason -> ...` or `exit:Reason -> ...`.

## To Recognize:
1. A `try ... catch ... end` block; `Class:Reason` patterns in the catch clauses.

# Context & Application

- **Typical contexts**: Sequential code that must contain a specific, known failure.
- **Common applications**: Converting an exception into a value the caller can match on.
- **Historical/stylistic notes**: The book argues *against* defensive catch-all clauses; let unexpected failures crash so a supervising part of the system handles them.

# Examples

**Example 1** (p. 36): Catching a `function_clause` error and returning it as a value:

```erlang
3> try ex1:factorial(zero) catch Type:Error -> {Type, Error} end.
{error,function_clause}
```

**Example 2** (p. 36): Matching specific classes — `error` and `exit`:

```erlang
6> try ex1:factorial(-2) catch error:Error3 -> {error, Error3};
6>     exit:Reason -> {exit, Reason} end.
{error,function_clause}
```

**Counter-example** (p. 35): The defensive catch-all clause `factorial(_) -> {error,bad_argument}.` forces every caller to handle improper results — the anti-pattern "let it fail" avoids.

# Relationships

## Builds Upon
- *(none — foundational)*

## Enables
- *(none specific in scope)*

## Related
- **Links** and **Exit signals** — The process-level counterparts of failure handling.

## Contrasts With
- *(none)*

# Common Errors

- **Error**: Writing defensive catch-all clauses to mask all failures.
  **Correction**: Handle only known, recoverable cases; let genuine bugs crash so supervision can react.

# Common Confusions

- **Confusion**: Thinking all Erlang exceptions are the same class.
  **Clarification**: There are three classes — `error`, `exit`, `throw` — and `catch` can match each individually.

# Source Reference

Chapter 1: Introducing Erlang, Section "Fail Safe!", pages 35-36.

# Verification Notes

- Definition source: Direct quotes from pp. 35-36.
- Confidence rationale: HIGH — explicit treatment with shell examples.
- Uncertainties: None.
- Cross-reference status: Verified against planned cards.
- Re-extraction notes: Fresh extraction — no pre-existing card for this source.
</content>
</invoke>
