---
# === CORE IDENTIFICATION ===
concept: Clause Selection and Pattern Matching Compilation
slug: clause-selection

# === CLASSIFICATION ===
category: performance
subcategory: caveats
tier: intermediate

# === PROVENANCE ===
source: "Erlang and OTP in Action"
source_slug: erlang-otp-action
authors: "Martin Logan, Eric Merritt, Richard Carlsson"
chapter: "Optimization and performance"
chapter_number: 14
pdf_page: null
section: "14.3.3. Clause selection"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "clause selection"
  - "pattern matching compilation"
  - "clause reordering"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - function-performance
extends: []
related:
  - bif-performance
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is pattern matching compilation?"
  - "When can the compiler reorder clauses?"
  - "How can a clause with a variable guard hurt clause selection?"
---

# Quick Definition

Pattern matching compilation is the compiler's algorithm for minimizing the tests needed to choose a function clause; it can reorder clauses only when doing so cannot change the outcome.

# Core Definition

When a function or fun, or a `case`/`if`/`try`/`receive` expression, has multiple clauses, the compiler minimizes the number of tests needed to decide which clause applies, using an algorithm called *pattern matching compilation* that groups and sorts clauses into nested if/then/else tests. It can change the order of tests only as long as that has no visible effect on the outcome. Mutually exclusive alternatives (e.g. atom `true` vs `false`, empty vs nonempty list) can be tested in any order, but overlapping alternatives must keep their written order. A clause with a variable or runtime-determined pattern in the middle of otherwise straightforward clauses introduces uncertainty that prevents grouping; moving such a clause below the others (when you know it is safe) restores grouping and is also more readable (Chapter 14, Section 14.3.3).

# Prerequisites

- **Function call performance** — Clause selection is part of the same discussion of efficient function use.

# Key Properties

1. Pattern matching compilation groups and sorts clauses into nested tests.
2. The compiler may reorder tests only when it cannot affect the outcome.
3. Mutually exclusive patterns (true/false, empty/nonempty) can be reordered freely.
4. Overlapping patterns (e.g. ordered numeric guards) must keep their written order.
5. A clause with a runtime variable pattern blocks reordering of clauses around it.
6. Manually moving such an uncertain clause below straightforward ones lets the compiler group them.
7. The optimization matters mainly with many clauses and complicated patterns; it also improves readability.

# Construction / Recognition

## To Identify/Recognize:
1. Spot a clause with a guard like `when Msg =:= SomeVariable` sitting between literal-pattern clauses.
2. If you know that variable can never equal the surrounding literals, move the clause below them.

# Context & Application

- **Typical contexts**: Functions or `case` expressions with many clauses in hot code paths.
- **Common applications**: Reordering a `Special`-variable clause so the literal-atom clauses can be grouped.
- **Historical/stylistic notes**: The book stresses the reordering also makes intent clearer, not just faster.

# Examples

**Example 1** (Section 14.3.3): `coffee_size/1` uses ordered `when N < ...` guards — swapping the first two clauses would change results, so the compiler must keep their order.

**Example 2** (Section 14.3.3): In `handle_message`, a middle clause `when Msg =:= Special` prevents grouping the `stop`/`go`/`report`/`calc` literal clauses, because `Special` could be `report` or `calc`.

# Relationships

## Related
- **BIF and operator performance** — Both are caveats in the same efficiency section.

# Common Errors

- **Error**: Placing a clause with a runtime variable pattern in the middle of literal-pattern clauses.
  **Correction**: If safe, move it below the literal clauses so the compiler can group their tests.

# Common Confusions

- **Confusion**: Thinking the compiler always reorders clauses for speed.
  **Clarification**: It reorders only when the outcome cannot change; overlapping or uncertain clauses are left as written.

# Source Reference

Chapter 14: Optimization and performance, Section 14.3.3 "Clause selection."

# Verification Notes

- Definition source: Direct adaptation of Section 14.3.3.
- Confidence rationale: HIGH — the mechanism and examples are explicit.
- Uncertainties: None.
- Cross-reference status: All cross-references are Agent 5-owned slugs.
- Re-extraction notes: Fresh extraction; no prior card.
</content>
