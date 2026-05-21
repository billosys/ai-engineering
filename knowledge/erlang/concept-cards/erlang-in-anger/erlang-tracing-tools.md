---
concept: Erlang Tracing Tools
slug: erlang-tracing-tools
category: production-ops
subcategory: tracing
tier: intermediate
source: "Stuff Goes Bad: Erlang in Anger"
source_slug: erlang-in-anger
authors: "Fred Hébert"
chapter: "Tracing"
chapter_number: 9
pdf_page: null
section: "Tracing"
extraction_confidence: high
aliases:
  - "sys"
  - "dbg"
  - "redbug"
  - "recon_trace"
prerequisites:
  - tracing
related:
  - recon-trace
  - tracing-principles
contrasts_with: []
answers_questions:
  - "What tools can I use to trace OTP processes?"
  - "Which tracing tools are safe to use in production?"
---

# Quick Definition

Erlang offers five main tracing tools: `sys` and `dbg` (standard with OTP), the raw tracing BIFs in the `erlang` module, `redbug` (production-safe, part of `eper`), and `recon_trace` (production-safe, dependency-free, function calls only).

# Core Definition

From section "Tracing," the options for tracing Erlang programs are: `sys` — comes standard with OTP, allows custom tracing functions and event logging, fine for development but weaker in production (no IO redirection to remote shells, no rate-limiting); `dbg` — also standard, clunky interface but capable, dangerous because "`dbg` can log absolutely everything on the node and kill one in under two seconds"; *tracing BIFs* — the raw blocks in the `erlang` module, low-level and difficult to use; `redbug` — a production-safe library in the `eper` suite with an internal rate-limiter and usable interface, but requires `eper`'s dependencies; `recon_trace` — recon's tracing, as safe as `redbug` but with no dependencies, a different interface, and able to trace only function calls (not messages).

# Prerequisites

- `tracing` — these are the concrete tools that implement the tracing facility.

# Key Properties

1. `sys` — standard OTP; custom trace functions and event logging; good for development; no remote-shell IO, no rate-limiting.
2. `dbg` — standard OTP; clunky but capable; dangerous — can log everything and kill a node in under two seconds.
3. Tracing BIFs — raw `erlang`-module primitives underlying the other tools; low-level and hard to use.
4. `redbug` — production-safe; internal rate-limiter; usable interface; requires the full `eper` dependency set.
5. `recon_trace` — production-safe; no dependencies; traces function calls only, not messages.
6. `sys`/`dbg`/BIFs make you reason explicitly about the pid ∩ trace-pattern Venn diagram; `redbug` and `recon_trace` abstract it away.

# Construction / Recognition

Choose by environment and need: `sys` for OTP-process development tracing; `dbg` only when you know exactly what you are doing; `redbug` for production tracing if you can take the `eper` dependency; `recon_trace` for production tracing without dependencies and when function calls (not messages) suffice.

# Context & Application

Production tracing should use `redbug` or `recon_trace` because they rate-limit and cannot easily kill the node. `sys` and `dbg` suit development; `dbg` is especially hazardous in production because it has no rate limiting.

# Examples

From section "Tracing": "`dbg` can log absolutely everything on the node and kill one in under two seconds." And `recon_trace` "can also only trace function calls, and not messages."

# Relationships

## Builds Upon
- `tracing` — these tools implement the tracing facility.

## Enables
- `recon-trace` — the specific `recon_trace` interface this chapter focuses on.

## Related
- `tracing-principles` — `sys`/`dbg`/BIFs expose the pid ∩ pattern model directly.

## Contrasts With
Nothing specific within this source.

# Common Errors

- Running `dbg` in production without precise scoping — it can kill a node in seconds.
- Using `sys` for production tracing and finding it has no rate-limiting or remote-shell IO.

# Common Confusions

- `recon_trace` traces function calls only, not inter-process messages; `redbug` and `dbg` are broader.
- `redbug` and `recon_trace` are both production-safe; `redbug` costs the `eper` dependencies, `recon_trace` has none.

# Source Reference

Chapter 9: Tracing, Section "Tracing". (No PDF pages — this source has none.)

# Verification Notes

- Definition source: quoted from section "Tracing."
- Confidence rationale: high — the source enumerates and characterizes each tool.
- Uncertainties: none.
- Cross-reference status: Verified
