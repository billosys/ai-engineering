---
# === CORE IDENTIFICATION ===
concept: Rest for One Strategy
slug: rest-for-one-strategy

# === CLASSIFICATION ===
category: applications-releases
subcategory: supervision
tier: intermediate

# === PROVENANCE ===
source: "Designing for Scalability with Erlang/OTP"
source_slug: design-scale-erlang-otp
authors: "Francesco Cesarini & Steve Vinoski"
chapter: "Supervisors"
chapter_number: 7
pdf_page: 188
section: "The restart specification"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "rest_for_one"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - restart-strategy
extends:
  - restart-strategy
related:
  - one-for-all-strategy
contrasts_with:
  - one-for-one-strategy
  - one-for-all-strategy
  - simple-one-for-one-strategy

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the difference between the one_for_one and one_for_all restart strategies?"
  - "How do I write a supervisor and define its child specifications?"
---

# Quick Definition

`rest_for_one` is the supervisor restart strategy in which, when a child crashes, all children started *after* it are terminated and restarted along with it. It suits children started in dependency order.

# Core Definition

Under the `rest_for_one` strategy, all processes started *after* the crashed process are terminated and restarted (Cesarini & Vinoski, p. 179). It is used when processes are started in order of dependency. In the `frequency_sup` example, the overload event manager is started first, then the frequency allocator, which sends requests to the overload manager when it runs out of frequencies. If the overload manager crashes and is being restarted, the frequency allocator might send it requests that get lost — so `rest_for_one` terminates the frequency allocator first, then restarts the overload manager and the frequency allocator in that order (pp. 179-180).

# Prerequisites

- **Restart strategy** — `rest_for_one` is one of the four restart strategy values.

# Key Properties

1. When a child crashes, that child and every child started *after* it are terminated and restarted.
2. Children started *before* the crashed one are unaffected.
3. Requires children to be listed in dependency order (earlier children are depended upon by later ones).
4. Specified as the atom `rest_for_one` in the supervisor specification.

# Construction / Recognition

## To Construct/Create:
1. Order the child specification list so that each child depends only on children before it.
2. Set `strategy => rest_for_one` (or the first tuple element) in the supervisor specification.

## To Identify/Recognize:
1. The supervisor specification's strategy is `rest_for_one`.
2. A crash restarts the crashed child plus all children after it, but not those before it.

# Context & Application

- **Typical contexts**: Supervisors whose children form a linear dependency chain.
- **Common applications**: A service that depends on a manager started before it.
- **Historical/stylistic notes**: The book notes that with asynchronous, loss-tolerant requests `one_for_one` could have been used instead — the choice depends on the system's requirements (p. 180).

# Examples

**Example 1** (pp. 175, 179-180): `frequency_sup` uses `rest_for_one`: `freq_overload` is started before `frequency`; if `freq_overload` crashes, `frequency` is terminated and both restart in order.

**Example 2** (p. 191): `bsc_sup` uses `rest_for_one` so that a crash of the frequency allocator or overload handler restarts the phone subtree, but a crash of the phones does not affect the frequency allocator.

## Worked Example

`bsc_sup` using `rest_for_one` (p. 191):

```erlang
init(_) ->
    ChildSpecList = [child(freq_overload, worker),
                     child(frequency, worker),
                     child(simple_phone_sup, supervisor)],
    {ok,{{rest_for_one, 2, 3600}, ChildSpecList}}.
```

A crash of `frequency` restarts `frequency` and `simple_phone_sup`; a crash of `simple_phone_sup` leaves the first two untouched.

# Relationships

## Builds Upon
- **Restart strategy** — `rest_for_one` is one specific restart strategy.

## Enables
- *(none)*

## Related
- **One for all strategy** — Also dependency-aware; `one_for_all` restarts every child rather than only the suffix.

## Contrasts With
- **One for one strategy** — Restarts only the crashed child; `rest_for_one` also restarts children started after it.
- **One for all strategy** — Restarts all children; `rest_for_one` restarts only those started after the crashed one.
- **Simple one for one strategy** — For identical dynamic children; `rest_for_one` is for an ordered static set.

# Common Errors

- **Error**: Using `rest_for_one` while listing children in arbitrary order.
  **Correction**: List children in dependency order so the "rest" that restarts is exactly the set of dependents.

# Common Confusions

- **Confusion**: Thinking `rest_for_one` restarts children *before* the crashed one.
  **Clarification**: Only the crashed child and those started *after* it restart; earlier children are untouched.

# Source Reference

Chapter 7: Supervisors, "The restart specification," pages 179-180. See Figure 8-9 (Rest for one).

# Verification Notes

- Definition source: Direct adaptation from pp. 179-180.
- Confidence rationale: HIGH — explicitly defined and illustrated, with two code examples.
- Uncertainties: None.
- Cross-reference status: Verified against planned card slugs for this source.
- Re-extraction notes: Fresh extraction — no pre-existing card for this source.
</content>
