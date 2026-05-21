---
# === CORE IDENTIFICATION ===
concept: Anonymous Functions
slug: anonymous-functions

# === CLASSIFICATION ===
category: functions-pattern-matching
subcategory: funs
tier: foundational

# === PROVENANCE ===
source: "Designing for Scalability with Erlang/OTP"
source_slug: design-scale-erlang-otp
authors: "Francesco Cesarini & Steve Vinoski"
chapter: "Introducing Erlang"
chapter_number: 1
pdf_page: 40
section: "Fun with Anonymous Functions"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - fun
  - fun expression
  - lambda
  - named fun

# === TYPED RELATIONSHIPS ===
prerequisites:
  - pattern-matching
extends: []
related:
  - higher-order-functions
  - processes-and-message-passing
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is an anonymous function (fun) in Erlang?"
  - "How are functions treated as first-class citizens in Erlang?"
---

# Quick Definition

An anonymous function, or "fun," is a function value that is not named or defined in a module. Funs make functions first-class citizens: they can be bound to variables, stored in data, passed as arguments, and returned from calls.

# Core Definition

"One functional principle is to treat functions as first-class citizens; they can be assigned to variables, be part of complex data structures, be passed as function arguments, or be returned as the results of function calls. We refer to the functional data type as an anonymous function, or fun for short" (Cesarini & Vinoski, p. 25). A fun is created with a `fun ... end` expression. A fun "does not have to be anonymous, and could instead refer to a local or global function definition" via `fun Mod:Name/Arity`. Since Erlang/OTP 17.0, a fun "can be given a name" placed after the `fun` keyword, enabling recursive anonymous functions; that name "is local to the function itself."

# Prerequisites

- **Pattern matching** — Fun clauses, like named-function clauses, select on argument patterns.

# Key Properties

1. A fun is a first-class value: assignable, storable, passable, returnable.
2. Created with `fun(Args) -> Body end`.
3. Can instead reference an existing function: `fun Mod:Name/Arity`.
4. Since OTP 17.0, a fun may be given a name (e.g., `fun Filter(...) -> ... end`) for recursion.
5. A named fun's name is scoped to the fun's own body and cannot be used to call it externally.
6. Funs can be spawned as a process body and passed in messages.

# Construction / Recognition

## To Construct:
1. Write `fun(Args) -> Body end` for an anonymous fun.
2. Or write `fun Module:Function/Arity` to wrap an existing function.
3. For recursion, name the fun: `fun Name(Args) -> ... Name(...) ... end`.

## To Recognize:
1. Look for the `fun` keyword followed by clauses and a closing `end`, or by a `Mod:Name/Arity`.

# Context & Application

- **Typical contexts**: Arguments to higher-order functions; bodies of spawned processes.
- **Common applications**: Predicates passed to `filter`; recursive helpers defined in the shell.
- **Historical/stylistic notes**: Named funs (OTP 17.0+) are "especially handy in the shell as it allows for easy definition of recursive anonymous functions" (p. 27).

# Examples

**Example 1** (p. 26): An anonymous predicate passed to `filter/2`:

```erlang
2> ex3:filter(fun(X) -> X rem 2 == 0 end, [1,2,3,4]).
[2,4]
```

**Example 2** (p. 26): A fun referencing a named function:

```erlang
3> ex3:filter(fun ex3:is_even/1,[1,2,3,4]).
[2,4]
```

**Example 3** (p. 27): A named recursive fun, assigned to shell variable `F`:

```erlang
4> F = fun Filter(_,[]) -> [];
4>         Filter(P,[X|Xs]) -> case P(X) of true -> [X|Filter(P,Xs)];
4>             false -> Filter(P,Xs) end end.
```

# Relationships

## Builds Upon
- *(none — foundational)*

## Enables
- **Higher-order functions** — Funs are the values passed to and returned from higher-order functions.
- **Processes and message passing** — A fun can be spawned as a process body.

## Related
- *(none additional)*

## Contrasts With
- *(none)*

# Common Errors

- **Error**: Trying to call a named fun by its internal name from outside its body (e.g., `Filter(...)`).
  **Correction**: The name is local to the fun; invoke the fun through the variable it was bound to.

# Common Confusions

- **Confusion**: Believing all funs must be anonymous.
  **Clarification**: A fun can wrap a named function (`fun Mod:F/N`) or, since OTP 17.0, carry its own name for recursion.

# Source Reference

Chapter 1: Introducing Erlang, Section "Functional Influence" / "Fun with Anonymous Functions," pages 25-27.

# Verification Notes

- Definition source: Direct quotes from pp. 25-27.
- Confidence rationale: HIGH — explicit definition with multiple shell examples.
- Uncertainties: None.
- Cross-reference status: Verified against planned cards.
- Re-extraction notes: Fresh extraction — no pre-existing card for this source.
</content>
</invoke>
