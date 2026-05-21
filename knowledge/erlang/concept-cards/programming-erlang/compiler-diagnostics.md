---
# === CORE IDENTIFICATION ===
concept: Compiler Diagnostics
slug: compiler-diagnostics

# === CLASSIFICATION ===
category: tooling
subcategory: compilation
tier: foundational

# === PROVENANCE ===
source: Programming Erlang, Second Edition
source_slug: programming-erlang
authors: Joe Armstrong
chapter: "Profiling, Debugging, and Tracing"
chapter_number: 21
pdf_page: null
section: "Compiler Diagnostics"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "compiler error messages"
  - "compiler warnings"
  - "head mismatch"
  - "unbound variable"
  - "unsafe variable"
  - "shadowed variable"

# === TYPED RELATIONSHIPS ===
prerequisites: []
extends: []
related:
  - cross-reference-analysis
  - runtime-stack-trace
contrasts_with:
  - runtime-stack-trace

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What do common Erlang compiler error messages mean?"
  - "What is an unsafe variable error?"
  - "What is a head mismatch error?"
---

# Quick Definition

Compiler diagnostics are the error and warning messages the Erlang compiler emits for syntactically or structurally incorrect source code, each carrying a filename and line number. Common ones include head mismatch, unbound variable, unterminated string, unsafe variable, and shadowed variable.

# Core Definition

"When we compile a program, the compiler provides us with helpful error messages if our source code is syntactically incorrect" ("Compiler Diagnostics"). Most are self-evident — a missing bracket, comma, or keyword produces an error with the filename and line number. The chapter explains several specific diagnostics:

- **Head mismatch** — the clauses of a function definition do not all have the same name and arity (`head mismatch`).
- **Unbound variables** — a variable is used with no value; reported at the first line where the unbound variable occurs (`variable 'X' is unbound`).
- **Unterminated string** — a missing closing quote on a string or atom (`unterminated string starting with "..."`).
- **Unsafe variables** — a variable bound only in some branches of a `case` is used afterward; the compiler reasons the variable might be undefined (`variable 'Y' unsafe in 'case'`).
- **Shadowed variables** — a variable inside a `fun` hides a previously defined variable of the same name (`variable 'X' shadowed in 'fun'`).

# Prerequisites

This is a foundational tooling concept within this chapter — it has no prerequisites among the concepts of these chapters.

# Key Properties

1. Emitted at compile time, before the program runs.
2. Each message includes a filename and line number.
3. Errors prevent the module from compiling; warnings (e.g. unused variable) do not.
4. An unbound-variable error is reported at the first occurrence, which may not be the true source line.
5. An unsafe-variable error arises when a variable is bound only on some `case` branches.
6. A shadowed-variable warning arises when a `fun` reuses an outer variable name.
7. For an unterminated string, inserting a quote near the suspected spot can yield a more precise diagnostic.

# Construction / Recognition

## To Diagnose a Compiler Message:
1. Read the filename and line number in the message.
2. For "head mismatch", check that all clauses of the function share name and arity.
3. For "unbound", find where the variable should have been given a value.
4. For "unsafe in 'case'", ensure the variable is bound on every `case` branch before use.
5. For "shadowed in 'fun'", rename one of the conflicting variables.

## To Recognize:
1. Messages of the form `./file.erl:N: <description>` printed by `c(Module)` or `erlc`.

# Context & Application

Compiler diagnostics are the first line of defense against coding mistakes.

- **Typical contexts**: Every compilation during development.
- **Common applications**: Pinpointing syntax and structural errors via line numbers.
- **Historical/stylistic notes**: Some diagnostics (head mismatch, unsafe variables) are structural rather than purely syntactic.

# Examples

**Example 1** ("Head Mismatch"): Clauses with different arity in `bad.erl`.

```erlang
foo(1,2) ->
    a;
foo(2,3,a) ->
    b.
%% c(bad).  ->  ./bad.erl:3: head mismatch
```

**Example 2** ("Unsafe Variables"): `Y` is bound only on one `case` branch, then used.

```erlang
foo() ->
    case bar() of
        1 -> X = 1, Y = 2;
        2 -> X = 3
    end,
    b(X, Y).
%% c(bad).  ->  ./bad.erl:9: variable 'Y' unsafe in 'case' (line 2)
```

# Relationships

## Builds Upon
- (Foundational tooling concept within this chapter.)

## Enables
- (No card depends on this concept.)

## Related
- **Cross-reference analysis** — Another static check; `xref` works across modules where the compiler works per-module.
- **Runtime stack trace** — Both report errors with line numbers; one at compile time, one at run time.

## Contrasts With
- **Runtime stack trace** — Compiler diagnostics catch errors before the program runs; a stack trace reports failures during execution.

# Common Errors

- **Error**: Assuming an unbound-variable error is on the exact reported line.
  **Correction**: The error is *detected* at the first occurrence; the real mistake may be where the variable should have been bound.

- **Error**: Ignoring an "unsafe in 'case'" error as a false alarm.
  **Correction**: Bind the variable on every `case` branch, or restructure so it is always defined before use.

# Common Confusions

- **Confusion**: Treating warnings and errors the same.
  **Clarification**: A warning (e.g. unused variable) still produces `{ok, Module}`; an error prevents compilation.

# Source Reference

Chapter 21: "Profiling, Debugging, and Tracing", section "Compiler Diagnostics" (subsections "Head Mismatch", "Unbound Variables", "Unterminated String", "Unsafe Variables", "Shadowed Variables").

# Verification Notes

- Definition source: Direct quotes from "Compiler Diagnostics".
- Confidence rationale: HIGH — each diagnostic is explicitly named and demonstrated with code.
- Uncertainties: None.
- Cross-reference status: Verified against planned cards.
- Re-extraction notes: Fresh extraction — no pre-existing card.
