---
# === CORE IDENTIFICATION ===
concept: Annual Release Model
slug: annual-release-features

# === CLASSIFICATION ===
category: language-background
subcategory: evolution
tier: foundational

# === PROVENANCE ===
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "New JavaScript features"
chapter_number: 6
pdf_page: null
section: null

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - yearly ECMAScript releases
  - incremental release model

# === TYPED RELATIONSHIPS ===
prerequisites:
  - tc39-process
  - es6-features
extends: []
related:
  - ecmascript-versions
  - tc39-proposal-stages
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How often are new JavaScript features released?"
---

# Quick Definition

Since ES2016, ECMAScript follows an annual release model where each June a new version is published containing all features that reached stage 4 by the release deadline.

# Core Definition

Starting with ES2016, ECMAScript versions are released annually, each including features that completed the TC39 process (reached stage 4) before the deadline. This replaced the previous model of large infrequent releases. "The shorter release life cycle resulted in fewer new features compared to the large ES6." (Ch. 5, &sect;5.3). Chapter 6 catalogs these annual releases from ES2016 through ES2025.

# Prerequisites

- **tc39-process** -- the process that produces stage 4 features
- **es6-features** -- the last large release before the annual model

# Key Properties

1. Annual releases every June starting with ES2016
2. Each release includes all features at stage 4 by the deadline
3. Smaller, incremental changes compared to ES6
4. Features are field-tested before inclusion
5. ES2016 had only two features: `Array.prototype.includes()` and `**` operator
6. Versions named by year (ES2016, ES2017, etc.)

# Construction / Recognition

Annual releases are referenced as ES2016, ES2017, etc. Feature availability is best checked per-feature rather than per-version.

# Context & Application

The annual model means developers should think in terms of individual features and their stage, not ECMAScript versions. A stage 4 feature is safe to use regardless of whether the next annual release has been published.

# Examples

From the source text (Ch. 6):
- ES2016: `Array.prototype.includes()`, exponentiation operator (`**`)
- ES2017: async/await, `Object.values()`/`Object.entries()`
- ES2020: optional chaining (`?.`), nullish coalescing (`??`), BigInt
- ES2025: iterator helpers, Set methods, `Promise.try()`

# Relationships

## Builds Upon
- **tc39-process** -- annual releases are a product of the process
- **es6-features** -- the last pre-annual release

## Enables
- Adoption of individual features as they reach stage 4

## Related
- **ecmascript-versions** -- the annual version timeline

## Contrasts With
- No direct contrast

# Common Errors

- **Error**: Waiting for the annual release to use a stage 4 feature.
  **Correction**: Stage 4 features can be used as soon as target engines support them.

# Common Confusions

- **Confusion**: Expecting annual releases to be as impactful as ES6.
  **Clarification**: The annual model intentionally produces smaller, incremental releases.

# Source Reference

Chapter 6: New JavaScript features, lines 1-856. Chapter 5: Section 5.3, lines 113-117.

# Verification Notes

- Definition source: synthesized from Ch. 5 and Ch. 6
- Confidence rationale: Structure is explicit across both chapters
- Cross-reference status: verified
