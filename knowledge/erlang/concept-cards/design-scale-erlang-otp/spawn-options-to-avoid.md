---
# === CORE IDENTIFICATION ===
concept: Spawn Options to Avoid
slug: spawn-options-to-avoid

# === CLASSIFICATION ===
category: anti-patterns
subcategory: process-tuning
tier: advanced

# === PROVENANCE ===
source: Designing for Scalability with Erlang/OTP
source_slug: design-scale-erlang-otp
authors: Francesco Cesarini & Steve Vinoski
chapter: "Controlling OTP Behaviors"
chapter_number: 4
pdf_page: 132
section: "Spawn Options to Avoid"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "{priority, Level}"
  - process priorities
  - disallowed spawn options

# === TYPED RELATIONSHIPS ===
prerequisites:
  - spawn-options
extends: []
related:
  - memory-management-and-garbage-collection
contrasts_with:
  - spawn-options

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What foundational Erlang concepts underpin the OTP behaviors?"
  - "How does the sys module relate to OTP behaviors?"
---

# Quick Definition

Certain `spawn_opt` options — `monitor`, `link`, and especially `{priority, Level}` — should not be used with OTP behaviors because they either fail outright or are considered bad programming practice.

# Core Definition

Some `spawn_opt` options "should be avoided because they either do not work with behaviors or are considered to be bad programming practice" (Cesarini & Vinoski, p. 132). `monitor`, although valid for the `spawn_opt/3` BIF, "is disallowed in generic servers and will result in the process terminating with a `badarg`." `link` is allowed, but starting behaviors with `start_link` is preferred. Process priorities "should never be set using the `{priority, Level}` option" (`Level` being `low`, `normal`, or `high`); changing priorities is "even more dangerous than meddling with memory and garbage collection," upsetting the VM's scheduler balance, causing starvation, and harming the system's soft real-time properties. These problems typically surface only under heavy load in production, never in testing (pp. 132-133).

# Prerequisites

- **Behavior spawn options** — You must understand how spawn options are passed before knowing which to avoid.

# Key Properties

1. `monitor` — disallowed in generic servers; passing it causes termination with `badarg`.
2. `link` — allowed, but `start_link` is the preferred way to link a behavior to its parent.
3. `{priority, Level}` (`low` / `normal` / `high`) — should never be used; it disrupts the VM's scheduler.
4. Higher-priority processes can starve, and lower-priority processes can cause the runtime to run out of memory under heavy load.
5. Priority-related faults appear only under heavy production load, not during testing.

# Construction / Recognition

## To Avoid These Options:
1. Never pass `monitor` to a generic server's spawn options.
2. Prefer `start_link` over passing `link` as a spawn option.
3. Never pass `{priority, Level}` — let the runtime system schedule on your behalf.

## To Recognize the Anti-Pattern:
1. Scan behavior start calls for `{spawn_opt, [...]}` lists containing `monitor` or `priority`.

# Context & Application

- **Typical contexts**: Reviewing or auditing behavior start code for unsafe tuning.
- **Common applications**: Code review checklists; production stability audits.
- **Historical/stylistic notes**: The authors close with "You have been warned!" — priority misuse is one of the hardest-to-diagnose production faults (p. 133).

# Examples

**Example 1** (p. 132): Passing `monitor` to a generic server's spawn options results in the process terminating with `badarg`.

**Example 2** (pp. 132-133): Using `{priority, high}` has been known to *starve* the high-priority process when the ratio between high- and low-priority processes crosses certain limits — counterintuitive and only visible under load.

# Relationships

## Builds Upon
- *(No prior concept; this card warns against misuse of spawn options.)*

## Enables
- *(No downstream concepts.)*

## Related
- **BEAM memory management and garbage collection** — The book frames priority misuse as "even more dangerous than meddling with memory and garbage collection."

## Contrasts With
- **Behavior spawn options** — Spawn options describes the *safe* memory tuning; this card flags the *unsafe* options to leave alone.

# Common Errors

- **Error**: Passing `{priority, high}` to make a behavior "more responsive."
  **Correction**: Never set priorities; let the VM's schedulers balance load — especially with hundreds of thousands of processes.

- **Error**: Passing `monitor` in a generic server's spawn options.
  **Correction**: It is disallowed and crashes the process with `badarg`; use monitors from application code instead.

# Common Confusions

- **Confusion**: Thinking a higher process priority always makes a process run sooner and faster.
  **Clarification**: Raising priority can *starve* the very process you boosted and destabilize the scheduler; the effect is unpredictable and load-dependent.

# Source Reference

Chapter 4: Controlling OTP Behaviors, Section "Spawn Options to Avoid," pages 132-133.

# Verification Notes

- Definition source: Direct quotes from pp. 132-133.
- Confidence rationale: HIGH — the source explicitly names each option to avoid and explains the consequences.
- Uncertainties: None.
- Cross-reference status: Verified against planned cards in this batch.
- Re-extraction notes: Fresh extraction; no pre-existing card for this source.
