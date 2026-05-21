---
# === CORE IDENTIFICATION ===
concept: Pattern Matching
slug: pattern-matching

# === CLASSIFICATION ===
category: functions-pattern-matching
subcategory: core-mechanism
tier: foundational

# === PROVENANCE ===
source: "Programming Erlang, Second Edition"
source_slug: programming-erlang
authors: Joe Armstrong
chapter: "Basic Concepts"
chapter_number: 3
pdf_page: null
section: "Pattern Matching Again"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - matching
  - pattern match

# === TYPED RELATIONSHIPS ===
prerequisites:
  - single-assignment-variable
  - term
extends: []
related:
  - the-match-operator
  - tuple
  - list
  - function-clause
  - anonymous-variable
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is pattern matching?"
  - "How does pattern matching select messages and function clauses?"
---

# Quick Definition

Pattern matching compares a pattern against an Erlang term: if they have the same shape, the match succeeds and the pattern's unbound variables are bound to the corresponding parts of the term; otherwise it fails.

# Core Definition

"Pattern matching is fundamental to Erlang and it's used for lots of different tasks. It's used for extracting values from data structures, and it's also used for flow of control within functions and for selecting which messages are to be processed in a parallel program" (Chapter 3, "Extracting Values from Tuples"). A pattern is matched against a *term* — "just an Erlang data structure." If the pattern and term have the same shape, the match "succeeds" and binds the pattern's unbound variables; if not, it "fails." "If we have a complex tuple, then we can extract values from the tuple by writing a pattern that is the same shape (structure) as the tuple and that contains unbound variables at the places ... where we want to extract values" (Chapter 3, "Extracting Values from Tuples"). A variable that already has a value must match the corresponding part of the term exactly — so `{X,Y,X}` matched against `{{abc,12},42,true}` fails because "X cannot be both `{abc,12}` and `true`" (Chapter 3, "Pattern Matching Again").

# Prerequisites

- **Single-assignment variable** — Matching binds unbound variables and tests bound ones; the success rule depends on these semantics.
- **Term** — A pattern is matched against a term (an Erlang data structure).

# Key Properties

1. A pattern matches a term when they have the same structure (shape).
2. A successful match binds the pattern's unbound variables to corresponding term parts.
3. A bound variable in a pattern must equal the corresponding part of the term.
4. The same variable used twice in one pattern must bind to the same value.
5. The anonymous variable `_` matches anything and never binds.
6. A failed match raises an exception (in `=`) or selects no clause (in functions/`receive`).
7. It serves three roles: data extraction, flow of control, and message selection.

# Construction / Recognition

## To Match and Extract:
1. Write a pattern with the same shape as the term.
2. Place unbound variables where you want to capture values.
3. Place `_` where you do not care about a value.
4. On success, the variables are bound; on failure, an error is raised or no clause matches.

## To Recognize It:
1. A pattern appears on the left of `=`, in a function head, in a `case` clause, or in a `receive` clause.

# Context & Application

- **Typical contexts**: The `=` operator, function-clause heads, `case` expressions, `receive` blocks, list comprehension generators.
- **Common applications**: Unpacking tuples and lists, dispatching on the shape of a message, selecting a function clause.
- **Historical/stylistic notes**: Armstrong calls clause selection by pattern "one of the joys of pattern matching, which will save you lots of work" — no `if-then-else` or `switch` code is needed.

# Examples

**Example 1** (Chapter 3, "Pattern Matching Again" table): `[H|T] = [1,2,3,4,5]` succeeds with `H = 1` and `T = [2,3,4,5]`; `{X,Y} = {333,ghi,"cat"}` fails because "the tuples have different shapes."

**Example 2** (Chapter 3, "Extracting Values from Tuples"): `{_,{_,Who,_},_} = Person` extracts the first name `joe` from `{person,{name,joe,armstrong},{footsize,42}}`, using `_` for the parts not wanted.

# Relationships

## Builds Upon
- **Single-assignment variable** — Pattern matching is the mechanism by which variables become bound.
- **Term** — The data structure a pattern is matched against.

## Enables
- **Function clause** — Clause selection is pattern matching on the call arguments.
- **The match operator** — `=` is the explicit operator form of pattern matching.

## Related
- **Tuple** and **list** — The compound structures most often matched.
- **Anonymous variable** — The `_` placeholder used within patterns.
- **Function clause** — Each clause head is a pattern.

## Contrasts With
- No directly contrasting concept in these chapters.

# Common Errors

- **Error**: Writing a pattern with a different number of elements than the term (e.g., `{X,Y}` vs. a 3-tuple).
  **Correction**: The pattern must have the same shape as the term, or the match fails.

- **Error**: Reusing a variable name in a pattern expecting independent values.
  **Correction**: A repeated variable must match the same value everywhere; use `_` or distinct names for independent positions.

# Common Confusions

- **Confusion**: Thinking pattern matching only happens with the `=` operator.
  **Clarification**: It also drives function-clause selection, `case`, `receive`, and list comprehension generators.

- **Confusion**: Assuming repeated `_` in one pattern must bind to the same value.
  **Clarification**: "Unlike regular variables, several occurrences of `_` in the same pattern don't have to bind to the same value."

# Source Reference

"Programming Erlang, Second Edition," Chapter 3: Basic Concepts, sections "Extracting Values from Tuples" and "Pattern Matching Again"; Chapter 2: A Whirlwind Tour of Erlang, "Pattern matching is used to select the message." EPUB-origin source; no page numbers.

# Verification Notes

- Definition source: Synthesized from Chapter 3, "Extracting Values from Tuples" and "Pattern Matching Again," with direct quotation of the three roles of pattern matching.
- Confidence rationale: HIGH — the mechanism, success/failure rules, and examples are explicit and extensive.
- Uncertainties: None.
- Cross-reference status: Verified against planned cards.
- Re-extraction notes: Fresh extraction; no pre-existing card. Canonical slug `pattern-matching` used.
