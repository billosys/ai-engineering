---
# === CORE IDENTIFICATION ===
concept: JavaScript Source Deployment
slug: javascript-source-deployment

# === CLASSIFICATION ===
category: language-background
subcategory: design-philosophy
tier: foundational

# === PROVENANCE ===
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "The nature of JavaScript"
chapter_number: 4
pdf_page: null
section: "4.2 The nature of JavaScript"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - source code deployment
  - minification

# === TYPED RELATIONSHIPS ===
prerequisites: []
extends: []
related:
  - javascript-platforms
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How is JavaScript code delivered to users?"
---

# Quick Definition

JavaScript is deployed as source code (not compiled binaries), though the source is often minified to reduce size. This is unique among major programming languages.

# Core Definition

"It is deployed as source code. But that source code is often *minified* (rewritten to require less storage)." (Ch. 4, &sect;4.2). JavaScript is sent to browsers as readable (or minified) source code, which is then compiled just-in-time by the JavaScript engine.

# Prerequisites

Foundational concept with no prerequisites.

# Key Properties

1. Deployed as source code, not compiled binaries
2. Source is often minified for production
3. Minification reduces file size for faster delivery
4. JavaScript engines compile just-in-time (JIT)
5. This makes JavaScript code inspectable in browsers

# Construction / Recognition

Minified code removes whitespace, shortens variable names, and removes comments.

# Context & Application

Source deployment means JavaScript code is visible to users. This has implications for intellectual property, security, and performance optimization.

# Examples

From the source text (Ch. 4, &sect;4.2):
- "deployed as source code"
- "often *minified* (rewritten to require less storage)"

# Relationships

## Builds Upon
- No prerequisites

## Enables
- Browser DevTools inspection
- View-source debugging

## Related
- **javascript-platforms** -- deployment differs by platform

## Contrasts With
- No direct contrast

# Common Errors

- **Error**: Assuming minified code is encrypted or protected.
  **Correction**: Minification reduces size but doesn't protect code; it can be reformatted.

# Common Confusions

- **Confusion**: Thinking JavaScript must be compiled before deployment.
  **Clarification**: JavaScript is deployed as source code; compilation happens at runtime by the engine.

# Source Reference

Chapter 4: The nature of JavaScript, Section 4.2, lines 67-70.

# Verification Notes

- Definition source: direct from source
- Confidence rationale: Briefly stated but explicit
- Cross-reference status: verified
