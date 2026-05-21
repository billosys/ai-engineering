---
# === CORE IDENTIFICATION ===
concept: Macros
slug: macros

# === CLASSIFICATION ===
category: core-idioms
subcategory: preprocessor
tier: foundational

# === PROVENANCE ===
source: "Designing for Scalability with Erlang/OTP"
source_slug: design-scale-erlang-otp
authors: "Francesco Cesarini & Steve Vinoski"
chapter: "Introducing Erlang"
chapter_number: 1
pdf_page: 40
section: "Macros"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "-define directive"
  - preprocessor macro
  - epp

# === TYPED RELATIONSHIPS ===
prerequisites: []
extends: []
related: []
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a macro in Erlang?"
  - "How do I define a parameterized or conditional macro?"
---

# Quick Definition

An Erlang macro is a textual substitution defined with `-define` and processed by the preprocessor (epp) before compilation. Macros can be constants or take parameters, and are invoked with a `?` prefix.

# Core Definition

"Erlang has a macro facility, implemented by the Erlang preprocessor (epp), which is invoked prior to compilation of source code into BEAM code. Macros can be constants ... or take parameters" (Cesarini & Vinoski, p. 44). "The definition can be any legal sequence of Erlang tokens; it doesn't have to be a meaningful expression in its own right" (p. 44). "Macros are invoked by preceding them with a `?` character" (p. 44). It is "conventional (but only conventional) to use uppercase names." Conditional macros can be defined with `-ifdef`/`-else`/`-endif` and controlled by compiler flags such as `{d,debug}`.

# Prerequisites

This is a foundational concept with no prerequisites within this source.

# Key Properties

1. Defined with `-define(Name, Replacement)`.
2. Processed by the preprocessor (epp) before BEAM compilation.
3. Can be constants or parameterized (`-define(TWICE(F,X), F(F(X)))`).
4. Invoked with a `?` prefix, e.g., `?ANSWER`.
5. The replacement may be any legal token sequence, not necessarily a complete expression.
6. Uppercase macro names are conventional, not required.
7. Conditional macros use `-ifdef`/`-else`/`-endif` with compiler flags (`{d,Flag}`, `{u,Flag}`).
8. `??Arg` records the textual form of a macro argument.

# Construction / Recognition

## To Construct:
1. Write `-define(NAME, replacement).` for a constant macro.
2. Write `-define(NAME(Args), replacement).` for a parameterized macro.
3. Invoke with `?NAME` or `?NAME(...)`.
4. For conditional macros, wrap definitions in `-ifdef(flag). ... -else. ... -endif.`

## To Recognize:
1. Look for `-define` directives and `?` macro invocations.

# Context & Application

- **Typical contexts**: Named constants, protocol field values, debug instrumentation.
- **Common applications**: `?TIMEOUT` constants; debug-only diagnostic code switched by a compiler flag.
- **Historical/stylistic notes**: Compiling with the `'P'` flag emits a `.P` file showing the post-expansion source.

# Examples

**Example 1** (p. 44): Constant and parameterized macros:

```erlang
-define(ANSWER,42).
-define(DOUBLE,2*).
-define(TWICE(F,X),F(F(X))).
test() -> ?TWICE(?DOUBLE,?ANSWER).
```

After expansion (p. 45): `test() -> 2 * (2 * 42).`

**Example 2** (p. 45): A conditional macro toggled by the `debug` flag:

```erlang
-ifdef(debug).
    -define(Assign(Var,Exp), Var=Exp,
        io:format("~s = ~s -> ~p~n",[??Var,??Exp,Var]) ).
-else.
    -define(Assign(Var,Exp), Var=Exp).
-endif.
```

# Relationships

## Builds Upon
- *(none — foundational)*

## Enables
- *(none specific in scope)*

## Related
- *(none additional)*

## Contrasts With
- *(none)*

# Common Errors

- **Error**: Forgetting the `?` prefix when invoking a macro.
  **Correction**: Macros are invoked only via `?NAME`; without it the name is treated as an ordinary atom/variable.

# Common Confusions

- **Confusion**: Thinking a macro replacement must be a complete, meaningful expression.
  **Clarification**: It can be any legal token sequence (e.g., `2*`), expanded textually before compilation.

# Source Reference

Chapter 1: Introducing Erlang, Section "Macros," pages 44-46.

# Verification Notes

- Definition source: Direct quotes from pp. 44-45.
- Confidence rationale: HIGH — explicit definition with multiple examples.
- Uncertainties: None.
- Cross-reference status: Verified against planned cards.
- Re-extraction notes: Fresh extraction — no pre-existing card for this source.
</content>
</invoke>
