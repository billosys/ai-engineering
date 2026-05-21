---
# === CORE IDENTIFICATION ===
concept: Error Kernel
slug: error-kernel

# === CLASSIFICATION ===
category: fault-tolerance
subcategory: design-strategy
tier: advanced

# === PROVENANCE ===
source: "Designing for Scalability with Erlang/OTP"
source_slug: design-scale-erlang-otp
authors: "Francesco Cesarini & Steve Vinoski"
chapter: "Supervisors"
chapter_number: 7
pdf_page: 188
section: "Synchronous Starts for Determinism"

# === CONFIDENCE ===
extraction_confidence: medium

# === VARIANTS (authority control) ===
aliases:
  - "simple core"
  - "error-kernel pattern"
  - "fail safe"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - supervision-tree
extends: []
related:
  - supervisor
  - cyclic-restart
  - restart-intensity-and-period
  - otp-application
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the error kernel of a system?"
  - "How do I design a system around the error-kernel pattern?"
---

# Quick Definition

The error kernel is the small, trusted core of a system — built from applications, supervisors, and synchronous startup — that is reliable enough to provide a solid base on which the rest of the system can crash and recover.

# Core Definition

The book describes the error kernel as a "simple core": the combination of applications, supervisors, and the synchronous startup sequence together provide a "'simple core' that guarantees a solid base for the rest of your system" (Cesarini & Vinoski, p. 199). Rather than handling bugs and corrupt data defensively throughout the code, the design isolates failures and lets processes terminate so a trusted, minimal core can restart and recover them — a strategy the book calls *fail safe* (p. 202). Synchronous, ordered startup makes the core deterministic and reproducible, so the system has a known-good base from which to recover.

# Prerequisites

- **Supervision tree** — The error kernel is realized as a trusted supervision structure with the rest of the system arranged around it.

# Key Properties

1. It is the minimal, trusted, reliable core of a system.
2. It is built from applications, supervisors, and synchronous startup.
3. Non-core processes are allowed to crash; the kernel restarts and recovers them.
4. Synchronous, ordered startup makes the core deterministic and its faults reproducible.
5. It embodies the *fail safe* strategy: do not defensively handle bugs — isolate and recover.

# Construction / Recognition

## To Construct/Create:
1. Identify the minimal set of processes that must be reliable for the system to function.
2. Place them in a well-designed supervision tree with carefully chosen restart strategies.
3. Start the core synchronously and in dependency order so it is deterministic.
4. Arrange less-critical, crash-tolerant processes around the core.

## To Identify/Recognize:
1. A small supervision subtree on which the rest of the system depends.
2. Non-core workers are allowed to fail and be restarted by the core.

# Context & Application

- **Typical contexts**: System-level architecture of OTP-based applications.
- **Common applications**: Designing a node so that transient faults are contained and recovered without manual intervention.
- **Historical/stylistic notes**: The book frames the whole supervisors chapter around this idea — "let your process terminate and have someone else deal with the problem" (p. 202).

# Examples

**Example 1** (p. 199): The combination of applications, supervisors, and synchronous startup is presented as the "simple core" providing a solid base for the rest of the system.

**Example 2** (pp. 180-181): Escalation up the supervision tree — when phone FSMs crash from corrupt data, restarting reaches a supervisor high enough to restart the frequency server and clear the fault.

## Worked Example

The book provides no single code listing for the error kernel; it is an architectural pattern. Its realization is the supervision tree built across the chapter, e.g. `bsc_sup` (p. 191) as the trusted core that starts and restarts the frequency, overload, and phone subtrees.

# Relationships

## Builds Upon
- *(none)*

## Enables
- **OTP application** — Applications package the error kernel and the rest of the system into managed units.

## Related
- **Supervisor** — Supervisors are the building blocks of the trusted core.
- **Cyclic restart** — Escalation of cyclic restarts is how the kernel recovers persistent faults.
- **Restart intensity and period** — Thresholds that route unrecoverable faults to a more capable level.

## Contrasts With
- *(none)*

# Common Errors

- **Error**: Spreading defensive error handling throughout the code instead of relying on the kernel.
  **Correction**: Focus on the positive cases; let processes crash and have the trusted core recover them.

- **Error**: Making the "core" large and complex.
  **Correction**: Keep the kernel minimal — the smaller and simpler it is, the more trustworthy the base.

# Common Confusions

- **Confusion**: Equating the error kernel with the Erlang `kernel` application.
  **Clarification**: The error kernel is a design concept — the trusted core of *your* system — not the OTP `kernel` library application.

- **Confusion**: Thinking the error kernel never fails.
  **Clarification**: It is the *most* reliable part, designed to be a solid base; the goal is to make recovery deterministic, not to make failure impossible.

# Source Reference

Chapter 7: Supervisors, "Synchronous Starts for Determinism" and "Summing Up," pages 198-199, 202.

# Verification Notes

- Definition source: Synthesized from pp. 199 ("simple core") and 202 ("fail safe"); the book uses "simple core" and "fail safe" rather than the term "error kernel" verbatim, though the competency questions name it directly.
- Confidence rationale: MEDIUM — the concept is clearly present and central to the chapter, but the source does not give it a single formal definition under the name "error kernel"; the definition is synthesized from the surrounding discussion.
- Uncertainties: The exact term "error kernel" is the competency-question framing; the book's wording is "simple core."
- Cross-reference status: Verified against planned card slugs for this source.
- Re-extraction notes: Fresh extraction — no pre-existing card for this source.
</content>
