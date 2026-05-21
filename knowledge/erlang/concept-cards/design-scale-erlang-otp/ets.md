---
# === CORE IDENTIFICATION ===
concept: ETS (Erlang Term Storage)
slug: ets

# === CLASSIFICATION ===
category: performance
subcategory: storage
tier: intermediate

# === PROVENANCE ===
source: "Designing for Scalability with Erlang/OTP"
source_slug: design-scale-erlang-otp
authors: "Francesco Cesarini & Steve Vinoski"
chapter: "Introducing Erlang"
chapter_number: 1
pdf_page: 40
section: "ETS: Erlang Term Storage"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - Erlang Term Storage
  - ETS table
  - DETS

# === TYPED RELATIONSHIPS ===
prerequisites:
  - processes-and-message-passing
extends: []
related:
  - records
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is ETS?"
  - "What kinds of ETS tables exist?"
  - "How does ETS access control work?"
---

# Quick Definition

ETS (Erlang Term Storage) provides in-memory tables of Erlang tuples keyed on a tuple position, offering constant-time key lookup. It scales where linearly-traversed lists do not.

# Core Definition

"If you need a key-value store where the lookup time is constant, or the ability to traverse your keys in lexicographical order, Erlang Term Storage (ETS) tables come in handy. An ETS table is a collection of Erlang tuples, keyed on a particular position in the tuple" (Cesarini & Vinoski, p. 47). ETS tables come in four kinds — *set*, *bag*, *duplicate bag*, and *ordered set* — and have one of three access traits — *public*, *private*, or *protected*. "Access time to a particular element is in constant time, except for ordered sets, where access time is proportional to the logarithm of the size of the table (O(log n) time)" (p. 48). "A table is linked to the process that creates it, and is deleted when that process terminates."

# Prerequisites

- **Processes and message passing** — A table is owned by the process that creates it and is deleted when that process terminates; access traits are defined in terms of processes.

# Key Properties

1. An ETS table is a collection of tuples keyed on a chosen tuple position (default position 1).
2. Four kinds: *set* (unique key-value tuple), *bag* (key repeats, tuple unique), *duplicate bag* (tuples may duplicate), *ordered set* (set ordered by key).
3. Access time is constant, except ordered sets at O(log n).
4. Three access traits: *public* (all processes), *private* (owner only), *protected* (all read, owner writes).
5. `{keypos, N}` sets the key position — useful for storing records.
6. Tables can be referenced by an ID or, if named, by name.
7. A table is linked to its creating process and deleted on that process's termination.
8. ETS is in-memory only; DETS provides disk-backed long-lived tables.

# Construction / Recognition

## To Construct:
1. Create a table with `ets:new(Name, Options)` (e.g., `[named_table]`, `public`, `{keypos,N}`).
2. Insert with `ets:insert/2`, look up with `ets:lookup/2`, traverse with `ets:first/1` and `ets:next/2`.
3. Extract bulk data with `ets:match/2` using `'$N'` variables and `'_'` wildcards.

## To Recognize:
1. Look for `ets:` function calls and table options.

# Context & Application

- **Typical contexts**: Constant-time key-value storage shared between processes.
- **Common applications**: The `hlr` module associates MSISDN phone numbers with pids in two named public tables.
- **Historical/stylistic notes**: ETS underpins many OTP facilities that need fast shared lookup.

# Examples

**Example 1** (p. 48): Basic table operations show a `set` table overwriting a duplicate key:

```erlang
1> TabId = ets:new(tab,[named_table]).
tab
2> ets:insert(tab,{haskell, lazy}).
true
4> ets:insert(tab,{haskell, ghci}).
true
5> ets:lookup(tab,haskell).
[{haskell,ghci}]
```

**Example 2** (p. 49): The `hlr` module uses two named public tables, `msisdn2pid` and `pid2msisdn`, created with `ets:new(msisdn2pid, [public, named_table])`.

# Relationships

## Builds Upon
- *(none — foundational)*

## Enables
- *(none specific in scope)*

## Related
- **Records** — `{keypos, N}` lets a record field serve as the table key.

## Contrasts With
- *(none)*

# Common Errors

- **Error**: Relying on key ordering in a `set` table.
  **Correction**: `set` ordering is hash-based; use an `ordered set` if traversal by key order is needed.

# Common Confusions

- **Confusion**: Thinking ETS tables persist after their owner dies or across restarts.
  **Clarification**: An ETS table is linked to its creating process and deleted when that process terminates; for disk persistence use DETS.

# Source Reference

Chapter 1: Introducing Erlang, Section "ETS: Erlang Term Storage," pages 47-50.

# Verification Notes

- Definition source: Direct quotes from pp. 47-48.
- Confidence rationale: HIGH — explicit definition, kinds, traits, and the `hlr` example.
- Uncertainties: None.
- Cross-reference status: Verified against planned cards.
- Re-extraction notes: Fresh extraction — no pre-existing card for this source.
</content>
</invoke>
