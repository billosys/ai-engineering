---
# === CORE IDENTIFICATION ===
concept: Cross-Reference Analysis
slug: cross-reference-analysis

# === CLASSIFICATION ===
category: tooling
subcategory: static-analysis
tier: intermediate

# === PROVENANCE ===
source: Programming Erlang, Second Edition
source_slug: programming-erlang
authors: Joe Armstrong
chapter: "Profiling, Debugging, and Tracing"
chapter_number: 21
pdf_page: null
section: "Generating Cross-References"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - xref
  - "cross-referencing"
  - "xref:d"

# === TYPED RELATIONSHIPS ===
prerequisites: []
extends: []
related:
  - compiler-diagnostics
contrasts_with:
  - erlang-profiling-tools

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is cross-reference analysis?"
  - "How do I find missing or unused functions in an Erlang project?"
  - "What does the xref tool do?"
---

# Quick Definition

Cross-reference analysis statically inspects compiled code to find missing, deprecated, and unused functions. The `xref` module performs it; it works only on code compiled with the `debug_info` flag.

# Core Definition

"We can use cross-referencing to find out whether we have any missing code and to find out who calls what. If we try to call a function that does not exist, then the cross-reference analysis will detect this. This is mostly useful for large programs with dozens of modules" (chapter introduction). Cross-references are generated with the `xref` module, which "works only if your code has been compiled with the `debug_info` flag set". `xref:d('.')` "performs a cross-reference analysis of all the code in the current directory that has been compiled with the debug flag. It produces lists of deprecated, undefined, and unused functions." Running it before running a program lets you discover missing functions ahead of time.

# Prerequisites

This is a foundational tooling concept within this chapter — it has no prerequisites among the concepts of these chapters.

# Key Properties

1. Performed by the `xref` module.
2. Works only on code compiled with the `debug_info` flag.
3. Detects calls to functions that do not exist.
4. `xref:d('.')` analyzes all debug-compiled code in a directory.
5. Produces three lists: deprecated, undefined, and unused functions.
6. Most useful for large programs with many modules.
7. `xref` has many options; the manual is needed for advanced use.

# Construction / Recognition

## To Run a Cross-Reference Check:
1. Remove stale `.beam` files (`rm *.beam`).
2. Recompile with debug info: `erlc +debug_info *.erl`.
3. Start Erlang and call `xref:d('.')`.
4. Inspect the returned `deprecated`, `undefined`, and `unused` lists.

## To Recognize:
1. Look for `xref:d/1` (or other `xref:` calls) and code compiled with `+debug_info`.

# Context & Application

Cross-reference analysis catches "who calls what" problems before runtime.

- **Typical contexts**: Periodic checks during development of a large multi-module program.
- **Common applications**: Finding calls to functions that do not exist, and spotting unused functions.
- **Historical/stylistic notes**: The book runs `xref` on a hobby graphics project `vsg` because the completed book code has no missing functions.

# Examples

**Example 1** ("Generating Cross-References"): Analyzing a directory of debug-compiled modules.

```erlang
$ rm *.beam
$ erlc +debug_info *.erl
$ erl
1> xref:d('.').
[{deprecated,[]},
 {undefined,[{{new,win1,0},{wish_manager,on_destroy,2}}, ...]},
 {unused,[{vsg,new_tag,0}, {vsg_indicator_box,theValue,1}]}]
```

The `undefined` list shows `{{vsg,call,1},{wish,cmd,1}}` — `vsg:call/1` calls `wish:cmd/1`, which does not exist.

# Relationships

## Builds Upon
- (Foundational tooling concept within this chapter.)

## Enables
- (No card depends on this concept.)

## Related
- **Compiler diagnostics** — Both catch errors statically; the compiler works per-module, `xref` works across modules.

## Contrasts With
- **Erlang profiling tools** — `xref` is static analysis of compiled code; profiling is dynamic measurement of a running program.

# Common Errors

- **Error**: Running `xref` on code compiled without `debug_info`.
  **Correction**: `xref` works only on debug-compiled code; recompile with `+debug_info` first.

- **Error**: Leaving stale `.beam` files in the directory.
  **Correction**: Remove old `.beam` files before recompiling, so the analysis reflects current source.

# Common Confusions

- **Confusion**: Thinking `xref` detects runtime errors.
  **Clarification**: `xref` is a static check; it finds undefined/deprecated/unused functions by analyzing compiled code, before the program runs.

# Source Reference

Chapter 21: "Profiling, Debugging, and Tracing", chapter introduction and section "Generating Cross-References".

# Verification Notes

- Definition source: Direct quotes from the chapter introduction and "Generating Cross-References".
- Confidence rationale: HIGH — `xref:d/1`, the `debug_info` requirement, and the three result lists are explicitly described with a worked example.
- Uncertainties: The book notes `xref` has many options not covered.
- Cross-reference status: Verified against planned cards.
- Re-extraction notes: Fresh extraction — no pre-existing card.
