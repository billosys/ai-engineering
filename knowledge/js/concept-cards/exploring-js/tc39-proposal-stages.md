---
# === CORE IDENTIFICATION ===
concept: TC39 Proposal Stages
slug: tc39-proposal-stages

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
section: "5.5.2 The details of the TC39 process (advanced)"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - proposal maturity stages
  - TC39 stages 0-4

# === TYPED RELATIONSHIPS ===
prerequisites:
  - tc39-process
extends:
  - tc39-process
related:
  - tc39-committee
  - ecmascript-versions
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What are the stages of a TC39 proposal and what do they mean?"
---

# Quick Definition

TC39 proposals progress through six stages: Stage 0 (ideation), Stage 1 (designing), Stage 2 (refining), Stage 2.7 (testing/validation), Stage 3 (implementation experience), and Stage 4 (ready for standard).

# Core Definition

Each ECMAScript proposal progresses through defined stages with entrance criteria (Ch. 5, &sect;5.5.2):
- **Stage 0**: Ideation and exploration; any author can create a draft
- **Stage 1**: Designing a solution; requires champions and a repository
- **Stage 2**: Refining; proposal complete, draft specification
- **Stage 2.7**: Testing and validation; specification complete, approved by reviewers
- **Stage 3**: Gaining implementation experience; tests finished, prototype implementations
- **Stage 4**: Integration; two passing implementations, significant field experience, ready for standard

# Prerequisites

- **tc39-process** -- stages are part of this process

# Key Properties

1. Each stage has specific entrance criteria for proposal, specification, tests, and implementations
2. Stage 2.7 was added in late 2023 (between existing stages 2 and 3)
3. Stage 2.7 uses ".7" because it's closer to stage 3 than stage 2
4. Artifacts: proposal document, Ecmarkup specification, Test262 tests, engine implementations
5. Roles: author, champion (TC39 delegate), reviewer, editor
6. Stage 4 requires two implementations passing tests

# Construction / Recognition

Proposal stages are tracked at github.com/tc39/proposals. Documentation references stages when discussing feature readiness.

# Context & Application

Developers should check a feature's stage before adopting it. Stage 3+ features are generally safe; earlier stages may undergo breaking changes.

# Examples

From the source text (Ch. 5, &sect;5.5.2.3):
- Stage 0: strawperson, no formal requirements
- Stage 1: pick champions, create repository
- Stage 2: proposal finished, specification drafted
- Stage 2.7: specification finished and approved
- Stage 3: tests finished, prototype implementations
- Stage 4: two implementations passing tests, pull request approved by editors

# Relationships

## Builds Upon
- **tc39-process** -- detailed breakdown of the process stages

## Enables
- Understanding feature readiness and stability

## Related
- **tc39-committee** -- manages the stage progression
- **ecmascript-versions** -- stage 4 features are included in annual releases

## Contrasts With
- No direct contrast

# Common Errors

- **Error**: Relying on stage 1 or 2 features in production code.
  **Correction**: Features below stage 3 may change significantly or be abandoned.

# Common Confusions

- **Confusion**: Wondering why stage 2.7 has an unusual number.
  **Clarification**: It was added after stages 0-4 were established; renumbering would make old documents confusing. ".7" reflects proximity to stage 3.

# Source Reference

Chapter 5: History and evolution of JavaScript, Section 5.5.2, lines 180-456.

# Verification Notes

- Definition source: direct from source
- Confidence rationale: Detailed with entrance criteria table and stage descriptions
- Cross-reference status: verified
