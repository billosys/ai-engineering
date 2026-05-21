---
# === CORE IDENTIFICATION ===
concept: Let It Crash
slug: let-it-crash

# === CLASSIFICATION ===
category: fault-tolerance
subcategory: error-philosophy
tier: foundational

# === PROVENANCE ===
source: "Erlang and OTP in Action"
source_slug: erlang-otp-action
authors: "Martin Logan, Eric Merritt, Richard Carlsson"
chapter: "The Erlang/OTP platform"
chapter_number: 1
pdf_page: null
section: "1.2.1 How process links work"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - let-it-crash philosophy
  - fail fast

# === TYPED RELATIONSHIPS ===
prerequisites:
  - process-isolation
  - process-termination
extends: []
related:
  - fault-tolerance
  - supervision
  - process-link
  - function-clause-selection
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the let-it-crash philosophy?"
  - "Why does Erlang prefer crashing over defensive error handling?"
  - "How does let-it-crash relate to fault tolerance?"
---

# Quick Definition

"Let it crash" is the Erlang philosophy of dropping everything cleanly and starting over when an unexpected error occurs, rather than trying to patch over a situation you probably cannot fix.

# Core Definition

"Rather than thrashing around desperately to save a situation that you probably won't be able to fix, the Erlang philosophy is 'let it crash' — you drop everything cleanly and start over, logging precisely where things went pear-shaped and how" (Chapter 1, section 1.2.1, "Let it crash" sidebar). The book calls this "a powerful recipe for fault tolerance and for creating systems that are possible to debug despite their complexity." Following the philosophy, a process that hits unpredicted bad data "dies immediately without trying to untangle the mess"; because processes are isolated, no other processes are affected, and a supervisor restores a known-good base state (section 1.2.3).

# Prerequisites

- **Process isolation** — crashing is safe only because a crash cannot corrupt other processes.
- **Process termination** — clean termination is what "crashing" relies on.

# Key Properties

1. On an unexpected error, the process drops everything and dies immediately.
2. It does not try to untangle or repair the broken situation.
3. The crash is logged with precise information about what failed.
4. Process isolation guarantees the crash does not affect other processes.
5. A supervisor restarts the failed subsystem from a known-good state.

# Construction / Recognition

## To Identify/Recognize:
1. Code does not defensively guard against every conceivable error.
2. Unexpected conditions lead straight to a process crash.
3. A supervisor is responsible for restart and recovery.

# Context & Application

- **Typical contexts**: Worker processes handling potentially malformed input.
- **Common applications**: Servers where a single bad request should fail fast without poisoning others.
- **Historical/stylistic notes**: It is reinforced at the language level — e.g., function-clause failures make a process "fail early" so bad data does not propagate (Chapter 2, section 2.5.2).

# Examples

**Example 1** (section 1.2.3): Malformed multimedia data causes a process in worker group A to malfunction; following let-it-crash, that process dies immediately without trying to untangle the mess, and the supervisor restores group A's base state.

**Example 2** (Chapter 2, section 2.5.2): Calling a function with an unexpected value triggers a `function_clause` exception so callers "fail early" and can detect and fix the mistake before bad data spreads.

# Relationships

## Builds Upon
- **Process isolation** — crashing is safe because state is encapsulated.

## Enables
- **Supervision** — restart-from-known-state is the recovery half of let-it-crash.

## Related
- **Fault tolerance** — let-it-crash is a recipe for it.
- **Process link** — links cascade a crash to a process group cleanly.
- **Function clause selection** — failing to match a clause makes a process fail early.

## Contrasts With
- None noted in this source.

# Common Errors

- **Error**: Writing extensive defensive code to handle every possible error in place.
  **Correction**: Let the process crash on the unexpected; let a supervisor restore a known-good state.

# Common Confusions

- **Confusion**: Believing "let it crash" means errors are ignored.
  **Clarification**: Crashes are logged precisely and a supervisor recovers; the error is handled, just not in place.

# Source Reference

Chapter 1: The Erlang/OTP platform, section 1.2.1 "Let it crash" sidebar, and section 1.2.3 "Layering processes for fault tolerance." See also Chapter 2, section 2.5.2.

# Verification Notes

- Definition source: Direct quotation from the "Let it crash" sidebar in section 1.2.1.
- Confidence rationale: HIGH — the philosophy is explicitly stated and named.
- Uncertainties: None.
- Cross-reference status: Verified against planned card slugs.
- Re-extraction notes: Fresh extraction; no prior card.
