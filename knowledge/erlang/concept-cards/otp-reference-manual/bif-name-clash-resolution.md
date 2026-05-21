---
# === CORE IDENTIFICATION ===
concept: BIF Name Clash Resolution
slug: bif-name-clash-resolution

# === CLASSIFICATION ===
category: functions-pattern-matching
subcategory: functions
tier: intermediate

# === PROVENANCE ===
source: "Erlang Reference Manual"
source_slug: otp-reference-manual
authors: "Ericsson AB"
chapter: "Expressions"
chapter_number: null
pdf_page: null
section: "Local Function Names Clashing With Auto-Imported BIFs"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "no_auto_import"
  - "local function shadowing a BIF"
  - "overriding an auto-imported BIF"
  - "-compile({no_auto_import, ...})"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - auto-imported-bifs
  - function-calls
extends: []
related:
  - built-in-functions
  - function-evaluation
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What happens when a local function has the same name as an auto-imported BIF?"
  - "How do I prevent a BIF from being auto-imported?"
  - "When is -compile({no_auto_import, [F/A]}) mandatory?"
  - "How did BIF name-clash semantics change in OTP R14A?"
---

# Quick Definition

When a local function has the same name and arity as an auto-imported BIF, implicitly qualified calls go to the *local* function, not the BIF. Use `-compile({no_auto_import, [F/A]})` to suppress the auto-import and remove the ambiguity.

# Core Definition

If a local function shares its name/arity with an auto-imported BIF, the semantics is that implicitly qualified calls (`f(...)`) are directed to the locally defined function, not the BIF (Reference Manual, "Expressions" > "Local Function Names Clashing With Auto-Imported BIFs"). To avoid confusion, the compiler directive `-compile({no_auto_import, [F/A]})` prevents the BIF from being auto-imported; in certain situations this directive is mandatory.

Since Erlang/OTP R14A (ERTS 5.8) the *local* function is called for such clashes. Before R14A, the BIF was always called. To keep pre-R14 code from silently changing behaviour: if you override a BIF that was auto-imported before R14A and call it with an implicitly qualified name, you must either remove the auto-import with the directive or use a fully qualified call (`erlang:f(...)`) — otherwise compilation fails. For BIFs added in R14A or later, overriding is always allowed, but the compiler warns on each implicitly qualified call unless the directive is present.

# Prerequisites

- **auto-imported-bifs** — you must understand which BIFs are callable without the `erlang:` prefix
- **function-calls** — the clash is about how implicitly qualified calls resolve

# Key Properties

1. Local function wins over auto-imported BIF for implicitly qualified calls (R14A+).
2. `-compile({no_auto_import, [F/A]})` removes the BIF from auto-import scope.
3. A fully qualified call (`erlang:length(X)`) always reaches the BIF, and is allowed in guards.
4. Overriding a pre-R14A auto-imported BIF without the directive (and calling it implicitly) is a compile error.
5. Overriding a post-R14A BIF without the directive yields a compiler warning, not an error.
6. The same rules apply to functions explicitly imported from other modules; you cannot both import and locally define the same function.

# Construction / Recognition

## To Apply:
1. Decide whether you intend the local function or the BIF to win.
2. Add `-compile({no_auto_import, [length/1]})` to silence ambiguity (mandatory for pre-R14A BIFs you override and call implicitly).
3. Use `erlang:length(X)` for an explicit BIF call, including inside guards.

## To Recognize:
1. A module defines a function whose name matches a BIF (`length/1`, `size/1`, etc.).
2. A `-compile({no_auto_import, ...})` directive signals an intentional override.

# Context & Application

- **Typical contexts**: utility modules that define functions named like common BIFs; libraries that shadow `length`, `size`, `element`.
- **Common applications**: defining a domain-specific `length/1` while still reaching `erlang:length/1` in guards.

# Examples

**Example 1** (Reference Manual): overriding `length/1` locally —

```erlang
-export([length/1, f/1]).
-compile({no_auto_import,[length/1]}). % erlang:length/1 no longer autoimported

length([]) -> 0;
length([_|T]) -> 1 + length(T).        %% calls the LOCAL length/1

f(X) when erlang:length(X) > 3 ->      %% calls erlang:length/1 (allowed in guards)
    long.
```

**Example 2** (Reference Manual): same logic with an explicit import — it is illegal to both `-import(mod,[length/1])` and define `length/1` locally without `no_auto_import`.

# Relationships

## Builds Upon
- **auto-imported-bifs** — the set of BIFs callable without `erlang:`

## Related
- **function-calls** — implicitly vs fully qualified resolution
- **built-in-functions** — what BIFs are
- **function-evaluation** — how the resolved call is evaluated

## Contrasts With
(none)

# Common Errors

- **Error**: Defining a function named like a pre-R14A BIF and calling it implicitly without `no_auto_import`.
  **Correction**: Add `-compile({no_auto_import,[F/A]})` or use a fully qualified `erlang:F(...)` call.

- **Error**: Expecting `length(X)` in a guard to call your local `length/1`.
  **Correction**: Use `erlang:length/1` in guards; only BIFs (not user functions) are allowed in guards.

# Common Confusions

- **Confusion**: Believing the BIF always wins on a name clash.
  **Clarification**: Since R14A the local function wins for implicitly qualified calls; before R14A the BIF won.

- **Confusion**: Thinking the directive changes runtime behaviour.
  **Clarification**: It only changes *compile-time* name resolution (whether the BIF is auto-imported).

# Source Reference

Chapter "Expressions", section "Function Calls" > subsection "Local Function Names Clashing With Auto-Imported BIFs" (Erlang Reference Manual), including the R14A change note and the two `length/1` examples.

# Verification Notes

- Definition source: Direct adaptation of the subsection, including the OTP R14A behaviour-change note.
- Confidence rationale: HIGH — explicit rules, version history, and two worked examples in source.
- Uncertainties: None.
- Cross-reference status: All referenced slugs verified (`auto-imported-bifs`, `function-calls`, `built-in-functions`, `function-evaluation`).
- Re-extraction notes: New card filling a documented gap (was referenced by `auto-imported-bifs`).
