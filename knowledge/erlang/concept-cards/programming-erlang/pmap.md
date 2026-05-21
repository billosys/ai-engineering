---
# === CORE IDENTIFICATION ===
concept: pmap
slug: pmap

# === CLASSIFICATION ===
category: performance
subcategory: parallel-abstractions
tier: intermediate

# === PROVENANCE ===
source: Programming Erlang, Second Edition
source_slug: programming-erlang
authors: Joe Armstrong
chapter: "Programming Multicore CPUs"
chapter_number: 26
pdf_page: null
section: "Parallelizing Sequential Code"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - parallel map
  - "pmap/2"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - spawn
  - message-passing
extends: []
related:
  - multicore-efficiency-rules
  - mapreduce
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I parallelize a sequential map over a list?"
  - "When should I use pmap instead of map?"
---

# Quick Definition

`pmap` is a parallel version of `lists:map/2` that spawns one process to evaluate the function for each list element, then gathers the results in the original order.

# Core Definition

"A simple strategy for speeding up our sequential programs would replace all calls to `map` with a new version of `map` that I'll call `pmap`, which evaluates all its arguments in parallel." `pmap(F, L)` "creates one parallel process to evaluate each argument in `L`." The spawned processes can complete in any order; "the selective receive in the `gather` function ensures that the order of the arguments in the return value corresponds to the ordering in the original list" ("Parallelizing Sequential Code"). `pmap` applies `(catch F(H))` so it terminates correctly even if a computation raises an exception.

# Prerequisites

- **Spawn** — `pmap` creates one process per element with `spawn`.
- **Message-passing** — Each worker sends its result back; `pmap` collects results via a selective `receive`.

# Key Properties

1. `pmap(F, L)` creates `length(L)` parallel processes — one per element.
2. Workers may finish in any order; a unique `make_ref()` and a selective receive restore list order.
3. It uses `(catch F(H))` so an exception in one element does not break the whole operation.
4. It is *not* semantically identical to `map` for functions with side effects — each `F(H)` runs in its own process, so process-dictionary changes are isolated.
5. It is not a general speedup panacea — granularity and process count matter.

# Construction / Recognition

## To Construct/Create:
1. Capture the parent pid `S = self()` and a unique `Ref = erlang:make_ref()`.
2. `map` over the list, spawning a process per element that computes `(catch F(I))` and sends `{self(), Ref, Result}` to the parent.
3. `gather` the results with a selective receive matched on each worker pid and `Ref`, rebuilding the list in order.

## To Identify/Recognize:
1. A function that spawns one process per list element and gathers results with a `Ref`-tagged selective receive.

# Context & Application

- **Typical contexts**: Replacing `lists:map/2` to exploit multicore CPUs.
- **Common applications**: CPU-bound, side-effect-free per-element computations such as `fib(27)` over a list.
- **Historical/stylistic notes**: Erlang does not provide `pmap` as a built-in; it is built from `spawn`, `send`, and `receive`. Many variants exist (order-insensitive, bounded-process-count, node-distributed).

# Examples

**Example 1** ("Parallelizing Sequential Code" — `lib_misc.erl`): The order-preserving `pmap`:

```erlang
pmap(F, L) ->
    S = self(),
    Ref = erlang:make_ref(),
    Pids = map(fun(I) ->
                spawn(fun() -> do_f(S, Ref, F, I) end)
              end, L),
    gather(Pids, Ref).

do_f(Parent, Ref, F, I) ->
    Parent ! {self(), Ref, (catch F(I))}.

gather([Pid|T], Ref) ->
    receive
        {Pid, Ref, Ret} -> [Ret|gather(T, Ref)]
    end;
gather([], _) ->
    [].
```

**Example 2** ("When Can We Use pmap?"): An order-insensitive variant `pmap1` uses `foreach` to spawn workers and `gather1(length(L), Ref, [])` to count down replies, building the result in arrival order.

# Relationships

## Builds Upon
- This card builds on `spawn` and message passing; it has no elaborating prerequisite card.

## Enables
- A drop-in parallel replacement for `lists:map/2` in CPU-bound code.

## Related
- **Multicore efficiency rules** — `pmap` is a concrete way to "use lots of processes."
- **mapreduce** — Another parallel higher-order abstraction built from the same primitives.

## Contrasts With
- This concept has no direct contrast within the chapter.

# Common Errors

- **Error**: Replacing `map` with `pmap` for functions that have side effects.
  **Correction**: `pmap` runs each `F(H)` in its own process, so side effects (e.g., process-dictionary writes) are isolated; only parallelize side-effect-free code.

- **Error**: Using `pmap` when the per-element work is tiny.
  **Correction**: The overhead of spawning and replying exceeds the benefit for trivial functions like `fun(I) -> 2*I end`; use `pmap` only when each computation is substantial.

# Common Confusions

- **Confusion**: Thinking `pmap` always speeds up a program.
  **Clarification**: It is not a panacea — for fine-grained work or huge lists (too many processes), it can be slower; consider a bounded-process variant.

# Source Reference

Chapter 26: Programming Multicore CPUs, Section "Parallelizing Sequential Code" (including "When Can We Use pmap?"). See the `lib_misc.erl` `pmap` and `pmap1` listings.

# Verification Notes

- Definition source: Direct adaptation from "Parallelizing Sequential Code."
- Confidence rationale: HIGH — the source gives the full `pmap` implementation and discusses its semantics and pitfalls.
- Uncertainties: None.
- Cross-reference status: Verified concept names exist or are planned.
- Re-extraction notes: Fresh extraction; no pre-existing card.
