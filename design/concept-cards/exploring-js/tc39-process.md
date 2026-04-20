---
# === CORE IDENTIFICATION ===
concept: TC39 Process
slug: tc39-process

# === CLASSIFICATION ===
category: language-background
subcategory: ecosystem
tier: foundational

# === PROVENANCE ===
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "History and evolution of JavaScript"
chapter_number: 5
pdf_page: null
section: "5.5 The TC39 process for proposed ECMAScript features"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - TC39 proposal process
  - ECMAScript proposal stages

# === TYPED RELATIONSHIPS ===
prerequisites:
  - tc39-committee
extends: []
related:
  - tc39-proposal-stages
  - ecmascript-versions
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do new features get added to JavaScript?"
---

# Quick Definition

The TC39 process is the standardized method for evolving JavaScript: features are designed independently, progress through six stages (0-4, including 2.7), require real-world testing, and are released annually.

# Core Definition

The TC39 process was instituted to address problems with the ES6 release cycle (long waits and rushed features). "ECMAScript features are designed independently and go through six stages: a strawperson stage 0 and five 'maturity' stages (1, 2, 2.7, 3, 4). Especially the later stages require prototype implementations and real-world testing, leading to feedback loops between designs and implementations. ECMAScript versions are released once per year and include all features that have reached stage 4 prior to a release deadline." (Ch. 5, &sect;5.5). ES2016 was the first version designed under this process.

# Prerequisites

- **tc39-committee** -- the committee that runs this process

# Key Properties

1. Features designed independently, not bundled into monolithic releases
2. Six stages: 0 (strawperson), 1, 2, 2.7, 3, 4
3. Later stages require prototype implementations and real-world testing
4. Annual releases include all stage-4 features
5. Result: smaller, incremental releases with field-tested features
6. Think in features and stages, not ECMAScript versions (post-ES6 advice)

# Construction / Recognition

Proposals are tracked at github.com/tc39/proposals. Each has a stage number indicating its maturity.

# Context & Application

When evaluating whether to use a new feature, check its stage. Stage 4 means safe to use; stage 3 means likely safe; earlier stages may change.

# Examples

From the source text (Ch. 5, &sect;5.5.1):
- "Starting with ES2016, it's better to think in individual features: once a feature reaches stage 4, we can safely use it"
- ES2016 was the first version designed under the TC39 process

# Relationships

## Builds Upon
- **tc39-committee** -- the committee running the process

## Enables
- **tc39-proposal-stages** -- the detailed stage definitions

## Related
- **ecmascript-versions** -- produced by this process

## Contrasts With
- No direct contrast

# Common Errors

- **Error**: Waiting for an ECMAScript version before using a stage 4 feature.
  **Correction**: Once a feature reaches stage 4, it can be used if the target engine supports it.

# Common Confusions

- **Confusion**: Thinking stages are simply version numbers.
  **Clarification**: Stages represent maturity of individual features, not the language as a whole.

# Source Reference

Chapter 5: History and evolution of JavaScript, Section 5.5, lines 136-167.

# Verification Notes

- Definition source: direct from source
- Confidence rationale: Detailed description with clear structure
- Cross-reference status: verified
