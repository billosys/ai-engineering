---
# === CORE IDENTIFICATION ===
concept: Function Call
slug: function-call

# === CLASSIFICATION ===
category: functions-pattern-matching
subcategory: function-calls
tier: foundational

# === PROVENANCE ===
source: "Erlang Reference Manual"
source_slug: otp-reference-manual
authors: "Ericsson AB"
chapter: "Expressions"
chapter_number: null
pdf_page: null
section: "Function Calls"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "local function call"
  - "implicitly qualified function call"
  - "function application"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - function-declaration
  - function-arity
extends: []
related:
  - qualified-function-call
  - fun-expressions
  - auto-imported-bifs
contrasts_with:
  - qualified-function-call

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I call a local function in Erlang?"
  - "What is an implicitly qualified function call?"
  - "What happens when a local function has the same name as a BIF?"
  - "Can I call a fun value using function call syntax?"
---

# Quick Definition

A local function call has the form `ExprF(Expr1,...,ExprN)` where `ExprF` is an atom naming a local or imported function, or an expression evaluating to a fun. This is the implicitly qualified function call form.

# Core Definition

In the function call form `ExprF(Expr1,...,ExprN)`, `ExprF` must be an atom or evaluate to a fun. If `ExprF` is an atom, the function is called using the implicitly qualified function name. Resolution order: if `ExprF` is locally defined, it is called; if explicitly imported from module `M`, then `M:ExprF(...)` is called; otherwise `ExprF` must be an automatically imported BIF. If `ExprF` evaluates to a fun, the fun is applied to the arguments. When calling a local function by name, there is a difference from fully qualified calls: local calls always refer to the current version of the module, while fully qualified calls refer to the latest loaded version (Erlang Reference Manual, "Function Calls" section).

# Prerequisites

- **function-declaration** — Must understand how functions are defined to call them.
- **function-arity** — Function identity is determined by name and arity.

# Key Properties

1. `ExprF(Expr1,...,ExprN)` — the implicitly qualified function call form.
2. `ExprF` must be an atom (function name) or evaluate to a fun.
3. Local functions take precedence over auto-imported BIFs (since R14A).
4. Explicitly imported functions are resolved before auto-imported BIFs.
5. Local calls refer to the current module version; qualified calls refer to the latest version.
6. If `ExprF` is a fun, the fun is applied to the arguments.

# Construction / Recognition

## To Construct:
```erlang
handle(Msg, State)
spawn(m, init, [])
```

Calling a fun:
```erlang
Fun1 = fun(X) -> X+1 end,
Fun1(3)
```

## To Recognize:
1. Look for `Name(Args)` where there is no `Module:` prefix.
2. `Name` is an atom or a variable/expression holding a fun.

# Context & Application

Local function calls are the most common form of function invocation in Erlang. Understanding the resolution order (local > imported > auto-imported BIF) is important when defining functions that share names with BIFs. The distinction between local and qualified calls matters for hot code loading, where local calls stay on the current module version while qualified calls upgrade to the new version.

# Examples

**Example 1** (Function Calls section): Local function calls:

```erlang
handle(Msg, State)
spawn(m, init, [])
```

**Example 2** (Function Calls section): Calling a fun:

```erlang
1> Fun1 = fun(X) -> X+1 end,
Fun1(3).
4
```

**Example 3** (Function Calls section): Avoiding BIF name clash with compiler directive:

```erlang
-compile({no_auto_import,[length/1]}).

length([]) -> 0;
length([H|T]) -> 1 + length(T). %% Calls the local function length/1
```

# Relationships

## Builds Upon
- **function-declaration** — The function being called must be declared.
- **function-arity** — Identity of the function depends on name/arity.

## Enables
- **fun-expressions** — Funs can be called using function call syntax.

## Related
- **qualified-function-call** — The explicit `Module:Function(Args)` form.
- **auto-imported-bifs** — BIFs are called via implicit qualification.

## Contrasts With
- **qualified-function-call** — Local calls stay on current module version; qualified calls use the latest version.

# Common Errors

- **Error**: Defining a local function with the same name as a pre-R14A auto-imported BIF without the `no_auto_import` directive.
  **Correction**: Use `-compile({no_auto_import,[F/A]})` or use fully qualified calls to the BIF.

- **Error**: Calling an undefined function, resulting in an `undef` error.
  **Correction**: Ensure the function is defined locally, imported, or is an auto-imported BIF.

# Common Confusions

- **Confusion**: Expecting a local call to pick up a newly loaded module version during hot code upgrade.
  **Clarification**: Local calls always use the current module version. Use a fully qualified call (`?MODULE:F(Args)`) to switch to the latest version.

# Source Reference

Erlang Reference Manual, "Expressions" chapter, "Function Calls" section.

# Verification Notes

- Definition source: Direct from source text
- Confidence rationale: High — clear resolution rules and examples from source
- Uncertainties: None
- Cross-reference status: Contrast with qualified-function-call verified in source
