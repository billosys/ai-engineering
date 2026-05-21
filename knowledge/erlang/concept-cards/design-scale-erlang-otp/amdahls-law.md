---
# === CORE IDENTIFICATION ===
concept: Amdahl's Law
slug: amdahls-law

# === CLASSIFICATION ===
category: performance
subcategory: scaling
tier: advanced

# === PROVENANCE ===
source: "Designing for Scalability with Erlang/OTP"
source_slug: design-scale-erlang-otp
authors: "Francesco Cesarini & Steve Vinoski"
chapter: "Scaling Out"
chapter_number: 14
pdf_page: 424
section: "Horizontal and Vertical Scaling — Amdahl's Law"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - Amdahl's law

# === TYPED RELATIONSHIPS ===
prerequisites:
  - scalability
extends: []
related:
  - vertical-scaling
  - horizontal-scaling
  - littles-law
contrasts_with:
  - littles-law

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is Amdahl's Law?"
  - "Why does adding cores stop improving performance?"
---

# Quick Definition

Amdahl's Law predicts the maximum speedup of a parallel program as cores are added: a program can be no faster than its slowest (sequential) component.

# Core Definition

"Amdahl's Law is used to predict the maximum speedup of your parallel program when adding cores. In simple terms, it tells us that a program will be as fast as its slowest component ... Amdahl's Law states that S(N) = 1/((1-P) + P/N), where S(N) is the speedup the system can achieve when executing with N cores, and P is the proportion of the program that can be made parallel. As N approaches infinity, the maximum speedup becomes S(N) = 1/1-P" (Cesarini & Vinoski, p. 425).

# Prerequisites

- **Scalability** — Amdahl's Law explains a limit on scalability; understand scalability first.

# Key Properties

1. Predicts the maximum speedup of a parallel program when adding cores.
2. Formula: S(N) = 1/((1-P) + P/N), with N cores and parallel proportion P.
3. As N approaches infinity, maximum speedup becomes S(N) = 1/(1-P).
4. A program is as fast as its slowest (sequential) component.
5. Demonstrates the law of diminishing returns — beyond a limit, adding cores improves performance only marginally.
6. Applies not only to your Erlang program but to the sequential code in the Erlang VM itself.

# Construction / Recognition

## To Construct/Create:
This is a law to apply, not an artifact. To apply it:
1. Estimate P, the proportion of the program that can be made parallel.
2. Compute S(N) = 1/((1-P) + P/N) for the available core count.
3. Use S(N) = 1/(1-P) for the theoretical maximum speedup.

## To Identify/Recognize:
1. Recognize Amdahl's Law's effect when adding cores yields progressively smaller speedups.

# Context & Application

- **Typical contexts**: Deciding whether to scale up (more cores) or out (more nodes).
- **Common applications**: Explaining why, past a limit, partitioning the data set across distributed nodes makes more sense than adding cores.
- **Historical/stylistic notes**: Because the law applies to the Erlang VM's own sequential code, fully using many-core hardware requires running multiple distributed VMs (p. 426).

# Examples

**Example 1** (p. 425): If 5% of your code base is sequential, your maximum speedup is 20 times; if 50% is sequential, your maximum speedup is 2 times.

**Example 2** (p. 425): If your sequential code takes 100 ms to run, no matter how fast your parallel code runs, you cannot run faster than 100 ms.

# Relationships

## Builds Upon
- **Scalability** — Amdahl's Law explains a fundamental limit on scaling

## Enables
- Amdahl's Law informs the choice between vertical and horizontal scaling.

## Related
- **Vertical scaling** — Amdahl's Law caps the benefit of adding cores when scaling up
- **Horizontal scaling** — Amdahl's Law motivates partitioning across nodes

## Contrasts With
- **Littles law** — Both are quantitative laws in the chapter; Amdahl's Law concerns parallel speedup, Little's Law concerns queue length and response time

# Common Errors

- **Error**: Expecting linear speedup from adding cores
  **Correction**: Speedup is bounded by the sequential proportion; past a limit, more cores improve performance only marginally.

# Common Confusions

- **Confusion**: Amdahl's Law applies only to your application code.
  **Clarification**: It applies to the sequential code in the Erlang VM too, which is why many-core hardware needs multiple distributed VMs.

# Source Reference

Chapter 14: Scaling Out, "Horizontal and Vertical Scaling — Amdahl's Law," pages 425-426. See Figure 15-1.

# Verification Notes

- Definition source: Direct quote from p. 425.
- Confidence rationale: HIGH — the source states the law, the formula, and worked examples explicitly.
- Uncertainties: None.
- Cross-reference status: Verified against planned cards.
- Re-extraction notes: Fresh extraction — no pre-existing card for this concept.
