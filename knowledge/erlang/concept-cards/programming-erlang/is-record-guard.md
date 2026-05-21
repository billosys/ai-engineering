---
# === CORE IDENTIFICATION ===
concept: is_record Guard Test
slug: is-record-guard

# === CLASSIFICATION ===
category: functions-pattern-matching
subcategory: guards
tier: intermediate

# === PROVENANCE ===
source: Programming Erlang, Second Edition
source_slug: programming-erlang
authors: Joe Armstrong
chapter: "Records and Maps"
chapter_number: 5
pdf_page: null
section: "Pattern Matching Records in Functions"

# === CONFIDENCE ===
extraction_confidence: medium

# === VARIANTS (authority control) ===
aliases:
  - "is_record/2"
  - record guard

# === TYPED RELATIONSHIPS ===
prerequisites:
  - record
extends: []
related:
  - pattern-matching
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I check that a value is a record of a particular type?"
  - "How do I dispatch a function clause on record type?"
---

# Quick Definition

`is_record(X, Name)` is a guard test that succeeds when `X` is a record of type `Name`, letting a function clause match only that record type.

# Core Definition

To match a record of a particular type in a function definition, the book writes the clause `do_something(X) when is_record(X, todo) -> ...`. "This clause matches when `X` is a record of type `todo`" ("Records and Maps", *Pattern Matching Records in Functions*). `is_record/2` is used as a guard test in the `when` part of a clause; it tests both that the argument is a tuple and that it is tagged as the named record type.

# Prerequisites

- **Record** — `is_record` exists specifically to test record-typed values, so the record concept must be understood first.

# Key Properties

1. Takes two arguments: a term and a record name.
2. Returns `true` when the term is a record of the given type, `false` otherwise.
3. Usable in a guard (`when` clause).
4. Effectively checks the term is a tuple whose first element is the record name with the correct arity.

# Construction / Recognition

## To Construct/Create:
1. Add a guard to a clause: `do_something(X) when is_record(X, todo) -> ...`.

## To Identify/Recognize:
1. An `is_record(Var, Name)` call in a `when` guard signals record-type dispatch.

# Context & Application

- **Typical contexts**: function clauses that should only fire for a specific record type when a bare record pattern is not desired.
- **Common applications**: dispatching generic helper functions across multiple record types.
- **Historical/stylistic notes**: an alternative to writing the explicit record pattern `#todo{} = X` in the head.

# Examples

**Example 1** (*Pattern Matching Records in Functions*): matching a record type with a guard:

```erlang
do_something(X) when is_record(X, todo) ->
    %% ...
```

# Relationships

## Builds Upon
- This is a small utility concept that depends only on records.

## Enables
- This concept does not have downstream cards in scope.

## Related
- **Pattern matching** — `is_record` complements record pattern matching for clause selection.

## Contrasts With
- No directly contrasting concept in scope.

# Common Errors

- **Error**: Passing the record name as a string or variable instead of a literal atom.
  **Correction**: The second argument to `is_record` is the record name atom, e.g. `todo`.

# Common Confusions

- **Confusion**: Thinking `is_record` checks structural field values.
  **Clarification**: It only tests that the term is a tuple tagged as the named record type with the right arity, not field contents.

# Source Reference

Chapter 5: "Records and Maps", section "Pattern Matching Records in Functions".

# Verification Notes

- Definition source: Adapted from the single `do_something/1` example in *Pattern Matching Records in Functions*.
- Confidence rationale: MEDIUM — the source shows the construct briefly with one example but does not give a full specification.
- Uncertainties: The source does not discuss `is_record/3` or the macro-expansion details.
- Cross-reference status: Slug `record` extracted in this chapter; `pattern-matching` assumed canonical.
- Re-extraction notes: Fresh extraction; no prior card content merged.
