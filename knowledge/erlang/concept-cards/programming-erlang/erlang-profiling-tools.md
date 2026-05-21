---
# === CORE IDENTIFICATION ===
concept: Erlang Profiling Tools
slug: erlang-profiling-tools

# === CLASSIFICATION ===
category: performance
subcategory: profiling
tier: intermediate

# === PROVENANCE ===
source: Programming Erlang, Second Edition
source_slug: programming-erlang
authors: Joe Armstrong
chapter: "Profiling, Debugging, and Tracing"
chapter_number: 21
pdf_page: null
section: "Tools for Profiling Erlang Code"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - cprof
  - fprof
  - eprof
  - profiler

# === TYPED RELATIONSHIPS ===
prerequisites: []
extends: []
related:
  - code-coverage-analysis
  - process-tracing
contrasts_with:
  - code-coverage-analysis
  - cross-reference-analysis

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What profiling tools does Erlang provide?"
  - "How do I find performance bottlenecks in an Erlang program?"
  - "What is the difference between cprof, fprof, and eprof?"
---

# Quick Definition

Erlang ships three profiling tools — `cprof`, `fprof`, and `eprof` — used for performance tuning to find where a program spends its time. The approach is: write the program, confirm correctness, then measure.

# Core Definition

"We use profiling for performance tuning to find out where the hot spots in our programs are" (chapter introduction). The best approach is to write programs, confirm they are correct, and finally measure to find where the time goes — guessing at bottlenecks is "almost impossible". The standard Erlang distribution comes with three profiling tools ("Tools for Profiling Erlang Code"):

- `cprof` counts the number of times each function is called; a lightweight profiler that adds 5–10% to system load and is safe on a live system.
- `fprof` displays the time for calling and called functions, with output to a file; suitable for large-system profiling in a lab, but adds significant load.
- `eprof` measures how time is used in Erlang programs; a predecessor of `fprof`, suitable for small-scale profiling.

# Prerequisites

This is a foundational tooling concept within this chapter — it has no prerequisites among the concepts of these chapters.

# Key Properties

1. Three tools ship with the standard distribution: `cprof`, `fprof`, `eprof`.
2. `cprof` is a lightweight call counter; ~5–10% overhead; usable on live systems.
3. `fprof` reports calling/called function times to a file; significant load; for lab profiling.
4. `eprof` measures time usage; predecessor of `fprof`; for small-scale profiling.
5. Recommended workflow: write, verify correctness, then measure.
6. If the program is already fast enough, measurement can be skipped.

# Construction / Recognition

## To Profile with cprof:
1. Start the profiler with `cprof:start()`.
2. Run the application.
3. Pause with `cprof:pause()`.
4. Analyze with `cprof:analyse(Module)` (or `cprof:analyse()` for all collected modules).
5. Stop with `cprof:stop()`.

## To Recognize:
1. Look for `cprof:`, `fprof:`, or `eprof:` calls around an application run.

# Context & Application

Profiling answers "where does the time go?" once a program already works.

- **Typical contexts**: Performance tuning after correctness is established.
- **Common applications**: `cprof` for live systems and quick call counts; `fprof` for detailed lab profiling; `eprof` for small-scale time measurement.
- **Historical/stylistic notes**: `eprof` is the predecessor of `fprof`.

# Examples

**Example 1** ("Tools for Profiling Erlang Code"): Profiling the SHOUTcast server with `cprof`.

```erlang
1> cprof:start().    %% start the profiler
2> shout:start().    %% run the application
3> cprof:pause().    %% pause the profiler
4> cprof:analyse(shout).   %% analyse function calls
5> cprof:stop().     %% stop the profiler
```

The analysis result shows, for example, `{{shout,split,2},73}` — that `shout:split/2` was called 73 times.

# Relationships

## Builds Upon
- (Foundational tooling concept within this chapter.)

## Enables
- (No card depends on this concept.)

## Related
- **Code coverage analysis** — Another measurement technique, focused on which lines run rather than timing.
- **Process tracing** — Tracing observes dynamic behavior; profiling aggregates it for performance.

## Contrasts With
- **Code coverage analysis** — Coverage counts line executions to find untested/dead code; profiling measures call counts and time to find bottlenecks.
- **Cross-reference analysis** — `xref` is static (finds missing/unused functions); profiling is dynamic measurement.

# Common Errors

- **Error**: Guessing where the bottleneck is and optimizing that.
  **Correction**: Measure first — it is almost impossible to guess where the hot spots are.

- **Error**: Running `fprof` on a live production system.
  **Correction**: `fprof` adds significant load; use `cprof` (5–10% overhead) on live systems and reserve `fprof` for the lab.

# Common Confusions

- **Confusion**: Thinking the three tools are interchangeable.
  **Clarification**: `cprof` counts calls (lightweight), `fprof` reports times in detail (heavyweight, lab use), and `eprof` measures time on a small scale.

# Source Reference

Chapter 21: "Profiling, Debugging, and Tracing", chapter introduction and section "Tools for Profiling Erlang Code". See footnotes 27–29 for the online docs.

# Verification Notes

- Definition source: Direct quotes from the chapter introduction and "Tools for Profiling Erlang Code".
- Confidence rationale: HIGH — the three tools and their roles are explicitly enumerated, with a worked `cprof` session.
- Uncertainties: `fprof`/`eprof` are described only briefly ("broadly similar to cprof").
- Cross-reference status: Verified against planned cards.
- Re-extraction notes: Fresh extraction — no pre-existing card.
