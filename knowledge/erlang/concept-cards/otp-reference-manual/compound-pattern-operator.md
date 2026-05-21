---
# === CORE IDENTIFICATION ===
concept: Compound Pattern Operator
slug: compound-pattern-operator

# === CLASSIFICATION ===
category: functions-pattern-matching
subcategory: expressions
tier: intermediate

# === PROVENANCE ===
source: "Erlang Reference Manual"
source_slug: otp-reference-manual
authors: "Ericsson AB"
chapter: "Expressions"
chapter_number: null
pdf_page: null
section: "The Compound Pattern Operator"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "compound pattern"
  - "double pattern"
  - "alias pattern"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - patterns-in-expressions
  - pattern-matching
extends:
  - patterns-in-expressions
related:
  - match-operator
contrasts_with:
  - match-operator

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a compound pattern in Erlang?"
  - "How do I match a term against two patterns simultaneously?"
  - "How do I avoid reconstructing terms in pattern matching?"
---

# Quick Definition

The compound pattern operator (`=`) combines two patterns so that both are matched against the same term simultaneously. This avoids reconstructing terms by allowing both a destructured and an aliased view of the same value.

# Core Definition

The Erlang Reference Manual states: "If `Pattern1` and `Pattern2` are valid patterns, the following is also a valid pattern: `Pattern1 = Pattern2`. When matched against a term, both `Pattern1` and `Pattern2` are matched against the term. The idea behind this feature is to avoid reconstruction of terms." Additionally: "The compound pattern operator does not imply that its operands are matched in any particular order. That means that it is not legal to bind a variable in `Pattern1` and use it in `Pattern2`, or vice versa." (Erlang Reference Manual, "Expressions", "The Compound Pattern Operator").

# Prerequisites

- **patterns-in-expressions** -- Must understand what patterns are
- **pattern-matching** -- Must understand how matching works

# Key Properties

1. Syntax: `Pattern1 = Pattern2` when used in a pattern context
2. Both patterns are matched against the same term
3. The operands are matched simultaneously, not sequentially
4. Variables bound in one sub-pattern CANNOT be used in the other
5. Primary use: avoid reconstructing terms (capture both the whole and parts)
6. The `=` character serves as both this operator and the match operator, depending on context

# Construction / Recognition

## To Construct/Create:
1. Write the destructuring pattern on one side of `=`
2. Write a variable (or other pattern) on the other side
3. Place in any pattern context (clause head, case, receive, match)

## To Identify/Recognize:
1. `=` appearing within a pattern context (not as an expression-level match)
2. Often seen as `{...} = Variable` or `Variable = {...}` in clause heads

# Context & Application

Compound patterns are used when you need both the whole term and some of its parts. Without compound patterns, you would need to match the parts and then reconstruct the whole, which is wasteful and error-prone.

# Examples

**Example 1** (Compound Pattern Operator section): Without compound patterns (wasteful reconstruction):
```erlang
f({connect,From,To,Number,Options}, To) ->
    Signal = {connect,From,To,Number,Options},
    ...;
```

Rewritten with compound pattern (avoids reconstruction):
```erlang
f({connect,_,To,_,_} = Signal, To) ->
    ...;
f(Signal, To) ->
    ignore.
```

**Example 2** (Match Operator and Compound Pattern section): Compound patterns in fun expressions:
```erlang
2> F = fun({A, B} = E) -> {E, A + B} end, F({1,2}).
{{1,2},3}
```

# Relationships

## Builds Upon
- **patterns-in-expressions** -- Compound patterns extend basic patterns
- **pattern-matching** -- Compound patterns use the matching mechanism

## Related
- **match-operator** -- Uses the same `=` character but is an expression-level operator

## Contrasts With
- **match-operator** -- The compound pattern operator matches simultaneously (no order); the match operator evaluates right-to-left

# Common Errors

- **Error**: Binding a variable in one sub-pattern and using it in the other:
  ```erlang
  fun(#{Key := Value} = #{key := Key}) -> Value end.
  %% ERROR: Key is unbound in the left sub-pattern
  ```
  **Correction**: Sub-patterns in a compound pattern are matched simultaneously; variables cannot flow between them. Use the match operator (expression level) instead for sequential matching.

# Common Confusions

- **Confusion**: Confusing the compound pattern operator with the match operator
  **Clarification**: When `=` appears in a pattern context, it is the compound pattern operator (simultaneous matching). When `=` appears in an expression context, it is the match operator (right-to-left evaluation). The distinction is determined by context.

# Source Reference

"Expressions" chapter, sections "The Compound Pattern Operator" and "The Match Operator and the Compound Pattern Operator."

# Verification Notes

- Definition source: Direct quotes from source text
- Confidence rationale: HIGH -- explicit definition with examples and contrast to match operator
- Uncertainties: None
- Cross-reference status: Verified against planned slugs
