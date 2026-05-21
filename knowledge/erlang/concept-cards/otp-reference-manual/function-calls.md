---
# === CORE IDENTIFICATION ===
concept: Function Calls
slug: function-calls

# === CLASSIFICATION ===
category: functions-pattern-matching
subcategory: functions
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

# === VARIANTS (authority control) ===
aliases:
  - "remote function call"
  - "external function call"
  - "local function call"
  - "fully qualified function name"
  - "implicitly qualified function name"

# === TYPED RELATIONSHIPS ===
prerequisites: []
extends: []
related:
  - function-evaluation
  - auto-imported-bifs
  - built-in-functions
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the difference between a local and a remote function call?"
  - "How do I call a function in another module?"
  - "What is a fully qualified function name?"
  - "How is the called function resolved for an implicitly qualified call?"
---

# Quick Definition

A function call evaluates a function with arguments, using either a fully qualified name (`Module:Function(Args)`) or an implicitly qualified name (`Function(Args)`). The first form is a remote call; the second resolves to a local function, an explicitly imported function, or an auto-imported BIF.

# Core Definition

Erlang has two function-call forms (Reference Manual, "Expressions" > "Function Calls"):

1. `ExprM:ExprF(Expr1,...,ExprN)` — the **fully qualified** (a.k.a. _remote_ or _external_) form. Each of `ExprM` and `ExprF` must be an atom or evaluate to an atom.
2. `ExprF(Expr1,...,ExprN)` — the **implicitly qualified** form. `ExprF` must be an atom or evaluate to a fun. If it is an atom: a locally defined function is called if one exists; otherwise an explicitly imported function from module `M` is called as `M:ExprF(...)`; otherwise `ExprF` must be the name of an automatically imported BIF.

A fully qualified call always refers to the *latest* version of the target module, which matters for code loading; an implicitly qualified local call binds to the currently executing version.

# Prerequisites

This is a foundational concept with no prerequisites within this source.

# Key Properties

1. Fully qualified calls use `Module:Function(Args)`; both module and function expressions must evaluate to atoms.
2. Implicitly qualified calls use `Function(Args)`; resolution order is local function → explicit import → auto-imported BIF.
3. A fully qualified call to a local module always dispatches to the latest loaded version of that module (relevant to hot code loading).
4. `ExprF` in the second form may also evaluate to a fun, in which case the fun is applied.
5. Funs can be applied directly (`Fun(Args)`) or via the `fun M:F/A` form.

# Construction / Recognition

## To Construct:
1. For a call into another module, write `Module:Function(Arg1, ..., ArgN)`.
2. For a call to a local, imported, or auto-imported function, write `Function(Arg1, ..., ArgN)`.
3. To apply a fun bound to a variable, write `Fun(Arg1, ..., ArgN)`.

## To Recognize:
1. A colon between two atoms before the argument list (`m:f(...)`) marks a remote call.
2. A bare atom before the argument list marks an implicitly qualified call.

# Context & Application

- **Typical contexts**: every Erlang program; remote calls cross module boundaries, local calls stay within a module.
- **Common applications**: `lists:keyfind(Name, 1, List)` (remote), `handle(Msg, State)` (local), `spawn(m, init, [])`.
- **Hot code loading note**: prefer a fully qualified call when you intentionally want the newest module version (e.g. a loop that should pick up code upgrades).

# Examples

**Example 1** (Reference Manual, "Function Calls"): Remote call — `lists:keyfind(Name, 1, List)`.

**Example 2**: Implicitly qualified calls — `handle(Msg, State)` and `spawn(m, init, [])`.

**Example 3**: Applying funs —

```erlang
1> Fun1 = fun(X) -> X+1 end, Fun1(3).
4
2> fun lists:append/2([1,2], [3,4]).
[1,2,3,4]
```

# Relationships

## Builds Upon
- **function-evaluation** — how a resolved call is actually evaluated

## Enables
- **auto-imported-bifs** — implicitly qualified calls may resolve to an auto-imported BIF

## Related
- **built-in-functions** — BIFs are called using the same syntax
- **function-evaluation** — the evaluation rules behind a call

## Contrasts With
(none)

# Common Errors

- **Error**: Assuming an implicitly qualified call always picks up the latest loaded module version.
  **Correction**: Only fully qualified (`m:f(...)`) calls guarantee the latest version; local calls stay within the running version.

- **Error**: Writing `Module:Function` where `Module` does not evaluate to an atom.
  **Correction**: Both the module and function expressions in a remote call must be (or evaluate to) atoms.

# Common Confusions

- **Confusion**: Believing remote and local calls are interchangeable.
  **Clarification**: They differ in resolution and in which code version is run during code loading.

- **Confusion**: Thinking `ExprF(...)` only ever calls a local function.
  **Clarification**: If no local function exists, it resolves to an explicit import, then to an auto-imported BIF.

# Source Reference

Chapter "Expressions", section "Function Calls" (Erlang Reference Manual). Subsection "Local Function Names Clashing With Auto-Imported BIFs" is treated as the separate concept `bif-name-clash-resolution`.

# Verification Notes

- Definition source: Direct adaptation of the "Function Calls" section.
- Confidence rationale: HIGH — the section defines both call forms explicitly with examples.
- Uncertainties: None.
- Cross-reference status: All referenced slugs verified to exist (`function-evaluation`, `auto-imported-bifs`, `built-in-functions`).
- Re-extraction notes: New card filling a documented cross-reference gap (was referenced by `function-evaluation`, `auto-imported-bifs`, `built-in-functions`).
