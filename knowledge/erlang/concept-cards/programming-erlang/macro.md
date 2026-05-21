---
# === CORE IDENTIFICATION ===
concept: Macro
slug: macro

# === CLASSIFICATION ===
category: tooling
subcategory: compilation
tier: intermediate

# === PROVENANCE ===
source: Programming Erlang, Second Edition
source_slug: programming-erlang
authors: Joe Armstrong
chapter: "The Rest of Sequential Erlang"
chapter_number: 8
pdf_page: null
section: "Macros"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "-define"
  - "?MacroName"
  - parameterized macro

# === TYPED RELATIONSHIPS ===
prerequisites:
  - erlang-preprocessor
extends: []
related:
  - conditional-compilation
  - include-files
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is an Erlang macro?"
  - "How do I define and use a macro?"
  - "What predefined macros does Erlang provide?"
---

# Quick Definition

A macro is a compile-time text substitution defined with `-define` and expanded by the preprocessor wherever `?MacroName` appears.

# Core Definition

Erlang macros are written `-define(Constant, Replacement).` or `-define(Func(Var1, ..., Var), Replacement).` ("The Rest of Sequential Erlang", *Macros*). "Macros are expanded by the Erlang preprocessor `epp` when an expression of the form `?MacroName` is encountered. Variables occurring in the macro definition match complete forms in the corresponding site of the macro call." A parameterized macro substitutes its arguments into the replacement text — e.g. `-define(macro1(X, Y), {a, X, Y}).` makes `?macro1(A+10, b)` expand to `{a, A+10, b}`. Three predefined macros give information about the current module: `?FILE` (the filename), `?MODULE` (the module name), and `?LINE` (the current line number).

# Prerequisites

- **Erlang preprocessor** — Macros are expanded by the preprocessor, so that concept comes first.

# Key Properties

1. Defined with `-define(Name, Replacement)` for constants or `-define(Name(Args), Replacement)` for parameterized macros.
2. Invoked with `?MacroName` (or `?MacroName(Args)`).
3. Expanded at compile time by the preprocessor `epp`.
4. Parameters in the definition match complete forms at the call site.
5. Predefined macros: `?FILE`, `?MODULE`, `?LINE`.

# Construction / Recognition

## To Construct/Create:
1. Define a constant macro: `-define(IP_VERSION, 4).`
2. Define a parameterized macro: `-define(macro1(X, Y), {a, X, Y}).`

## To Identify/Recognize:
1. A `?` followed by an uppercase name is a macro invocation.

# Context & Application

- **Typical contexts**: naming constants, abbreviating repeated code or bit-syntax type specifiers.
- **Common applications**: the COFF example defines `-define(DWORD, 32/unsigned-little-integer).` so `?DWORD` expands to that type specifier text.
- **Historical/stylistic notes**: keeping macro names identical to a foreign API's type names minimizes the semantic gap between specification and Erlang code.

# Examples

**Example 1** (*Macros*): a parameterized macro and its expansion:

```erlang
-define(macro1(X, Y), {a, X, Y}).

foo(A) ->
    ?macro1(A+10, b)
```

`foo/1` expands to `foo(A) -> {a,A+10,b}.`

**Example 2** (*Macros*): a debug macro using predefined macros:

```erlang
-define(DEBUG(X), io:format("DEBUG ~p:~p ~p~n",[?MODULE, ?LINE, X])).
```

# Relationships

## Builds Upon
- **Erlang preprocessor** — Macros are a preprocessor feature.

## Enables
- **Conditional compilation** — `-ifdef`/`-ifndef`/`-else`/`-endif` control which macro definitions take effect.

## Related
- **Include files** — Macro definitions are commonly shared via `.hrl` files.

## Contrasts With
- No directly contrasting concept in scope.

# Common Errors

- **Error**: Invoking a macro without the `?` prefix.
  **Correction**: Macro use requires `?MacroName`; without `?` it is just an atom or function name.

- **Error**: Using a parameterized macro with the wrong number of arguments.
  **Correction**: The call must supply exactly the parameters listed in the `-define`.

# Common Confusions

- **Confusion**: Thinking macros are evaluated at runtime.
  **Clarification**: Macros are pure compile-time text substitution performed by the preprocessor.

- **Confusion**: Believing macro parameters match arbitrary text.
  **Clarification**: Parameters match complete syntactic forms at the call site.

# Source Reference

Chapter 8: "The Rest of Sequential Erlang", section "Macros".

# Verification Notes

- Definition source: Direct quotation and adaptation from *Macros*.
- Confidence rationale: HIGH — the source defines the macro syntax, expansion, and predefined macros with examples.
- Uncertainties: None.
- Cross-reference status: Slug `erlang-preprocessor` extracted in this chapter; `conditional-compilation`, `include-files` extracted in this chapter.
- Re-extraction notes: Fresh extraction; no prior card existed for this slug.
