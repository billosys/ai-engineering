---
# === CORE IDENTIFICATION ===
concept: mapreduce
slug: mapreduce

# === CLASSIFICATION ===
category: performance
subcategory: parallel-abstractions
tier: advanced

# === PROVENANCE ===
source: Programming Erlang, Second Edition
source_slug: programming-erlang
authors: Joe Armstrong
chapter: "Programming Multicore CPUs"
chapter_number: 26
pdf_page: null
section: "Parallelizing Computations with mapreduce"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - map-reduce
  - parallel higher-order function
  - "mapreduce/4"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - spawn
  - message-passing
  - pmap
extends: []
related:
  - data-partitioning-for-parallelism
  - link
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is mapreduce and how is it implemented in Erlang?"
  - "How do I parallelize a computation over a set of inputs?"
---

# Quick Definition

`mapreduce` is a parallel higher-order function: many mapping processes emit `{Key, Value}` pairs that a single reduce process merges and folds into a final result.

# Core Definition

"`mapreduce` is a parallel higher-order function. Proposed by Jeffrey Dean and Sanjay Ghemawat of Google, it is said to be in daily use on Google clusters." It is "more like a family of algorithms than one particular algorithm." Its spec is `mapreduce(F1, F2, Acc0, L) -> Acc`. `F1(Pid, X)` is the mapping function — it sends a stream of `{Key, Value}` messages to `Pid` and then terminates; `mapreduce` spawns a fresh process for each `X` in `L`. `F2(Key, [Value], Acc0) -> Acc` is the reduction function — once all mapping processes terminate, the reduce process has merged all values per key and folds `F2` over the `{Key, [Value]}` tuples ("Parallelizing Computations with mapreduce").

# Prerequisites

- **Spawn** — `mapreduce` spawns one mapping process per input element.
- **Message-passing** — Mapping processes send `{Key, Value}` messages to the reduce process.
- **pmap** — `mapreduce` is the same family of parallel abstraction as `pmap`, built from the same primitives.

# Key Properties

1. Signature: `mapreduce(F1, F2, Acc0, L) -> Acc`.
2. `F1(Pid, X)` (the mapper) sends `{Key, Value}` messages to `Pid` and then terminates.
3. `mapreduce` spawns one mapper process per element of `L`, using `spawn_link`.
4. The reduce process collects messages, merging values into a dictionary keyed by `Key`.
5. `F2(Key, [Value], Acc0) -> Acc` (the reducer) is folded over the collected `{Key, [Value]}` tuples (`dict:fold/3`).
6. The reduce process traps exits so it can count down terminating mappers even on failure.
7. The `map` of `mapreduce` is unrelated to the `map` function used elsewhere in the book.

# Construction / Recognition

## To Construct/Create:
1. Write `F1(Pid, X)` to emit `{Key, Value}` messages to `Pid` and then return.
2. Write `F2(Key, [Value], Acc) -> Acc` to fold collected values into an accumulator.
3. Call `mapreduce(F1, F2, Acc0, L)`; it spawns a reduce process which `spawn_link`s one mapper per element of `L`.
4. The reduce process collects `N = length(L)` mappers' replies, builds a dictionary, then `dict:fold`s `F2` over it.

## To Identify/Recognize:
1. A reduce process that spawns one linked mapper per input and merges `{Key, Value}` messages into a dictionary.

# Context & Application

- **Typical contexts**: Parallelizing computations over a set of inputs on multicore or clustered hardware.
- **Common applications**: Counting word frequencies across a directory of files — one mapper process per file.
- **Historical/stylistic notes**: Erlang provides no built-in `mapreduce`; it is built from `spawn`, `send`, and `receive`. The chapter's `mapreduce` lives in module `phofs` ("parallel higher-order functions").

# Examples

**Example 1** ("Parallelizing Computations with mapreduce" — `phofs.erl`): The core of `mapreduce`:

```erlang
mapreduce(F1, F2, Acc0, L) ->
    S = self(),
    Pid = spawn(fun() -> reduce(S, F1, F2, Acc0, L) end),
    receive
        {Pid, Result} -> Result
    end.

reduce(Parent, F1, F2, Acc0, L) ->
    process_flag(trap_exit, true),
    ReducePid = self(),
    foreach(fun(X) ->
              spawn_link(fun() -> do_job(ReducePid, F1, X) end)
            end, L),
    N = length(L),
    Dict0 = dict:new(),
    Dict1 = collect_replies(N, Dict0),
    Acc = dict:fold(F2, Acc0, Dict1),
    Parent ! {self(), Acc}.
```

**Example 2** ("Parallelizing Computations with mapreduce" — `test_mapreduce.erl`): A word-frequency counter. `generate_words(Pid, File)` sends `{Word, 1}` for each word; `count_words(Key, Vals, A)` accumulates `[{length(Vals), Key}|A]`. Running it created 102 parallel processes — one per Erlang module in the code directory.

# Relationships

## Builds Upon
- This card builds on `spawn`, `spawn_link`, and message passing; it has no elaborating prerequisite card.

## Enables
- **Data partitioning for parallelism** — The map-reduce architecture is exactly the partition-then-gather idea.

## Related
- **pmap** — Same family of parallel higher-order abstractions.
- **link** — Mappers are created with `spawn_link`; the reducer traps exits.

## Contrasts With
- This concept has no direct contrast within the chapter.

# Common Errors

- **Error**: Confusing the `map` of `mapreduce` with the list function `map`.
  **Correction**: They are unrelated; the source explicitly warns of this.

- **Error**: Writing `F1` to return a value instead of sending `{Key, Value}` messages.
  **Correction**: `F1(Pid, X)` must *send* `{Key, Value}` messages to `Pid` and then terminate.

# Common Confusions

- **Confusion**: Thinking `mapreduce` is one fixed algorithm.
  **Clarification**: It "is actually more like a family of algorithms than one particular algorithm"; many implementations and semantics are possible.

# Source Reference

Chapter 26: Programming Multicore CPUs, Section "Parallelizing Computations with mapreduce." See the `phofs.erl` and `test_mapreduce.erl` listings and the `fig_9.png` figure.

# Verification Notes

- Definition source: Direct quote and adaptation from "Parallelizing Computations with mapreduce."
- Confidence rationale: HIGH — the source gives the full spec, a complete implementation, and a worked word-count example.
- Uncertainties: The implementation uses the now-discouraged `dict` module; the algorithm is unchanged.
- Cross-reference status: Verified concept names exist or are planned.
- Re-extraction notes: Fresh extraction; no pre-existing card.
