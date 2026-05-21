---
# === CORE IDENTIFICATION ===
concept: Function Call Performance
slug: function-performance

# === CLASSIFICATION ===
category: performance
subcategory: caveats
tier: intermediate

# === PROVENANCE ===
source: "Erlang and OTP in Action"
source_slug: erlang-otp-action
authors: "Martin Logan, Eric Merritt, Richard Carlsson"
chapter: "Optimization and performance"
chapter_number: 14
pdf_page: null
section: "14.3.3. Functions"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "function call speed"
  - "meta-call cost"
  - "tail recursion vs body recursion"

# === TYPED RELATIONSHIPS ===
prerequisites: []
extends: []
related:
  - clause-selection
  - bif-performance
  - process-performance
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How fast are the different kinds of function call in Erlang?"
  - "Is a meta-call with apply/3 slower than a direct call?"
  - "Is tail recursion always faster than body recursion?"
---

# Quick Definition

Most Erlang function-call forms are about equally fast; only meta-calls via `apply/3` are significantly slower, and tail vs. body recursion differences are now small enough that you should measure rather than assume.

# Core Definition

Function-invocation times vary by call form (Table 14.2): a local call `foo()` is very fast; a known remote call `bar:foo()` is almost as fast; an unknown remote call `Mod:Func()` is about 3x slower; a fun application `F()` is about 2-3x slower; and a meta-call `apply(Mod,Func,Args)` is about 6-10x slower. Absolute and relative times vary with hardware and compiler releases. In general you need not worry about invocation times unless writing extremely performance-critical code — only meta-calls are significantly slower, and `Mod:Func(...)` is a better choice than `apply/3` when the argument count is fixed. Similarly, tail-recursive solutions used to be faster than body-recursive ones, but compiler and runtime improvements have shrunk the gap; an elegant body-recursive function may be at least as fast — so measure both versions for both small and large inputs (Chapter 14, Section 14.3.3).

# Prerequisites

This is a foundational performance-caveats concept with no prerequisites within this source.

# Key Properties

1. Local call `foo()` — very fast.
2. Known remote call `bar:foo()` — almost as fast as a local call.
3. Unknown remote call `Mod:Func()` — about 3x slower than a local call.
4. Fun application `F()` — about 2-3x slower than a local call.
5. Meta-call `apply(Mod,Func,Args)` — about 6-10x slower than a local call.
6. Only meta-calls are significantly slower; they tend to be rare.
7. `Mod:Func(...)` is preferable to `apply/3` when the argument count is fixed.
8. Tail- vs. body-recursion differences are now small; measure rather than assume.

# Construction / Recognition

## To Identify/Recognize:
1. Reach for a meta-call only when the argument list truly is dynamic.
2. When both a tail- and body-recursive version are feasible, benchmark both — for small and large inputs.

# Context & Application

- **Typical contexts**: Micro-optimizing performance-critical inner loops.
- **Common applications**: Choosing `Mod:Func(...)` over `apply/3` for a known arity.
- **Historical/stylistic notes**: The book notes remote calls were once much slower than local ones, but are now almost equal — relative costs drift with releases.

# Examples

**Example 1** (Table 14.2): The five call forms are ranked from "very fast" (local) to "6-10x slower" (meta-call via `apply/3`).

**Example 2** (Section 14.3.3): For tail vs. body recursion, the book advises not to assume — measure both, since results vary with input size and even hardware cache behaviour.

# Relationships

## Related
- **Clause selection** — Another function-related efficiency consideration from the same section.
- **Process performance** — Continues the efficiency discussion at process granularity.

# Common Errors

- **Error**: Using `apply/3` when the argument count is fixed.
  **Correction**: Use the `Mod:Func(...)` form — it is much faster than a meta-call.

- **Error**: Assuming tail recursion is always faster than body recursion.
  **Correction**: The gap is now small; measure both versions with realistic inputs.

# Common Confusions

- **Confusion**: Believing remote calls are always noticeably slower than local ones.
  **Clarification**: A *known* remote call is almost as fast; only *unknown* `Mod:Func()` and meta-calls are notably slower.

# Source Reference

Chapter 14: Optimization and performance, Section 14.3.3 "Functions," Table 14.2, including "Tail recursion versus body recursion."

# Verification Notes

- Definition source: Direct adaptation of Section 14.3.3 and Table 14.2.
- Confidence rationale: HIGH — call costs are explicitly tabulated.
- Uncertainties: Relative costs are stated to vary with compiler/runtime releases.
- Cross-reference status: All cross-references are Agent 5-owned slugs.
- Re-extraction notes: Fresh extraction; no prior card.
</content>
