---
# === CORE IDENTIFICATION ===
concept: Variable Scope
slug: variable-scope

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
  - "scoping rules"
  - "variable visibility"
  - "unsafe variables"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - variables
  - single-assignment
extends: []
related:
  - if-expression
  - case-expression
  - maybe-expression
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the scope of a variable in Erlang?"
  - "What are unsafe variables?"
  - "Can I use a variable bound in a case branch outside the case expression?"
---

# Quick Definition

The scope of a variable is its function clause. Variables bound in branches of `if`, `case`, or `receive` expressions must be bound in all branches to be safely used outside the expression; otherwise they are considered unsafe.

# Core Definition

The Erlang Reference Manual states: "The scope for a variable is its function clause. Variables bound in a branch of an `if`, `case`, or `receive` expression must be bound in all branches to have a value outside the expression. Otherwise they are regarded as unsafe outside the expression." Additionally: "For the `try` expression, variable scoping is limited so that variables bound in the expression are always unsafe outside the expression." (Erlang Reference Manual, "Expressions", "Variables").

# Prerequisites

- **variables** -- Must understand what variables are
- **single-assignment** -- Scoping interacts with single assignment

# Key Properties

1. Variable scope is the enclosing function clause
2. Variables bound in `if`/`case`/`receive` branches must be bound in ALL branches to be safe outside
3. Variables only bound in some branches are "unsafe" outside the expression
4. Variables bound in `try` expressions are ALWAYS unsafe outside the expression
5. Variables bound in a `maybe` block must not be used after the block
6. Variables bound in `else` clauses of `maybe` must not be used after the block

# Construction / Recognition

## To Identify/Recognize:
1. A compiler warning about "unsafe variable" indicates a variable bound in only some branches
2. Variables used after a `try` expression that were bound inside it will trigger warnings
3. Safe usage requires all branches to bind the same variable name

# Context & Application

Variable safety rules prevent use of potentially unbound variables. In languages with mutable variables, a variable might hold a default value even if a branch did not set it. In Erlang, since variables must be bound through pattern matching, using a variable that might not be bound is a compile-time error. This rule encourages extracting values through consistent branching patterns.

# Examples

**Example 1** (Variables section): Safe vs. unsafe binding in case branches:
```erlang
%% Safe: X is bound in all branches
case Input of
    a -> X = 1;
    b -> X = 2
end,
X   %% safe to use here

%% Unsafe: Y is only bound in one branch
case Input of
    a -> Y = 1;
    b -> ok
end,
Y   %% UNSAFE: Y might not be bound
```

**Example 2** (Variables section): Variables in `try` are always unsafe outside:
```erlang
try
    Z = compute()
catch _:_ -> error
end,
Z   %% ALWAYS unsafe, even though Z is bound in the try body
```

# Relationships

## Builds Upon
- **variables** -- Scope rules apply to variables
- **single-assignment** -- Scope interacts with the single-assignment model

## Related
- **if-expression** -- Variables bound in `if` branches must be bound in all branches
- **case-expression** -- Variables bound in `case` branches must be bound in all branches
- **maybe-expression** -- Variables bound in `maybe` blocks must not be used outside

# Common Errors

- **Error**: Using a variable outside a `case` expression when it is only bound in some branches
  **Correction**: Either bind the variable in all branches, or restructure to use the variable only within the branch

# Common Confusions

- **Confusion**: Thinking `try`-bound variables are safe if the try succeeds
  **Clarification**: Variables bound inside `try` are ALWAYS unsafe outside, regardless of success or failure. This is a deliberate safety restriction.

# Source Reference

"Expressions" chapter, section "Variables", paragraphs on scope and unsafe variables.

# Verification Notes

- Definition source: Direct quotes from source text
- Confidence rationale: HIGH -- explicit scoping rules stated in source
- Uncertainties: None
- Cross-reference status: Verified against planned slugs
