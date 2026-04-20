---
# === CORE IDENTIFICATION ===
concept: ECMAScript Versions Timeline
slug: ecmascript-versions

# === CLASSIFICATION ===
category: language-background
subcategory: history
tier: foundational

# === PROVENANCE ===
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "History and evolution of JavaScript"
chapter_number: 5
pdf_page: null
section: "5.3 Timeline of ECMAScript versions"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - ES version history
  - ECMAScript timeline

# === TYPED RELATIONSHIPS ===
prerequisites:
  - ecmascript-standard
extends: []
related:
  - tc39-process
  - tc39-committee
  - es6-features
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What are the major ECMAScript versions and what did they introduce?"
---

# Quick Definition

ECMAScript has evolved through major versions from ES1 (1997) through annual releases (ES2016+), with ES3 and ES6 being the most significant milestones.

# Core Definition

The ECMAScript version timeline spans from ES1 (June 1997) to annual releases starting with ES2016. Key milestones: ES3 (1999) added core features like try/catch and regex; ES4 was abandoned for being too ambitious; ES5 (2009) added strict mode; ES6/ES2015 was the landmark release fulfilling ES4's promises with `let`/`const`, classes, modules, and more. Starting with ES2016, releases are annual and incremental. (Ch. 5, &sect;5.3).

# Prerequisites

- **ecmascript-standard** -- understanding what ECMAScript is

# Key Properties

1. ES1 (1997): first version
2. ES3 (1999): regex, try/catch, switch, do-while
3. ES4: abandoned (too ambitious)
4. ES5 (2009): strict mode, minor standard library additions
5. ES6/ES2015 (June 2015): massive update (let/const, classes, modules, arrows, destructuring, etc.)
6. ES2016+: annual releases, smaller incremental changes
7. All versions ratified in June starting from ES2016

# Construction / Recognition

Version numbers appear in documentation as ES5, ES6, ES2015, ES2020, etc. The `^ES6^` notation in the source marks when features were introduced.

# Context & Application

Knowing which version introduced a feature helps determine browser/engine compatibility and whether transpilation is needed.

# Examples

From the source text (Ch. 5, &sect;5.3):
- ES3 (December 1999): "regular expressions, better string handling, new control statements [do-while, switch], try/catch exception handling"
- ES6 (June 2015): "A large update that fulfilled many of the promises of ECMAScript 4"
- ES2016 (June 2016): "First yearly release"

# Relationships

## Builds Upon
- **ecmascript-standard** -- versions of the standard

## Enables
- **es6-features** -- the largest single version
- **backward-compatibility** -- why old versions still matter

## Related
- **tc39-process** -- the process that produces new versions

## Contrasts With
- No direct contrast

# Common Errors

- **Error**: Thinking ES6 and ES2015 are different versions.
  **Correction**: ES6 is the colloquial name for ECMAScript 2015, the same version.

# Common Confusions

- **Confusion**: Expecting each annual release to be as large as ES6.
  **Clarification**: ES6 was exceptionally large; annual releases since ES2016 are intentionally smaller and incremental.

# Source Reference

Chapter 5: History and evolution of JavaScript, Section 5.3, lines 92-117.

# Verification Notes

- Definition source: direct from source
- Confidence rationale: Explicit timeline with dates and descriptions
- Cross-reference status: verified
