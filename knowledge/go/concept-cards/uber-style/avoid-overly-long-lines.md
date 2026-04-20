---
# === CORE IDENTIFICATION ===
concept: Avoid Overly Long Lines
slug: avoid-overly-long-lines

# === CLASSIFICATION ===
category: style
subcategory: formatting
tier: foundational

# === PROVENANCE ===
source: "Uber Go Style Guide"
source_slug: uber-style
authors: "Prashant Varanasi, Simon Newton (and Uber Go team)"
chapter: "Style"
chapter_number: 4
pdf_page: null
section: "Avoid overly long lines"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "line length limit"
  - "99 character line limit"
  - "soft line limit"

# === TYPED RELATIONSHIPS ===
prerequisites: []
extends: []
related:
  - be-consistent
  - group-similar-declarations
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the recommended line length limit in the Uber Go style?"
  - "Is the 99 character limit a hard or soft limit?"
  - "Why should long lines be avoided?"
---

# Quick Definition

Avoid lines of code that require horizontal scrolling. The Uber style guide recommends a soft line length limit of 99 characters. Authors should aim to wrap lines before hitting this limit, but code is allowed to exceed it.

# Core Definition

Long lines of code reduce readability by requiring readers to scroll horizontally or turn their heads. The Uber Go Style Guide establishes a **soft** line length limit of **99 characters**. This is explicitly not a hard limit -- code is allowed to exceed it when wrapping would reduce clarity. The intent is to guide authors toward more readable line lengths while allowing pragmatic exceptions.

# Prerequisites

No prerequisites. This is a foundational style convention.

# Key Properties

1. **Soft limit, not hard** -- 99 characters is a guideline, not a rule that breaks builds.
2. **Readability motivation** -- The goal is to avoid horizontal scrolling and improve code comprehension.
3. **Author responsibility** -- Authors should aim to wrap lines before 99 characters but may exceed it when appropriate.

# Construction / Recognition

## To Construct/Create:
1. Break long lines at natural boundaries: after commas in argument lists, before operators, or at logical groupings.
2. Use intermediate variables to break complex expressions across multiple lines.
3. Align continuation lines for readability.

## To Identify/Recognize:
1. Lines exceeding 99 characters in Go source files.
2. Lines requiring horizontal scrolling in a typical editor or code review tool.

# Context & Application

- **Typical contexts**: All Go source code in a project following the Uber style guide.
- **Common applications**: Function signatures with many parameters, long string literals, chained method calls, complex conditional expressions.

# Examples

No specific Bad/Good code examples are provided in the source for this section. The guidance is stated as a principle: aim to wrap lines before 99 characters, but it is not a hard limit.

# Relationships

- **Related to** `be-consistent`: Line length conventions should be applied consistently across the codebase.
- **Related to** `group-similar-declarations`: Grouping declarations can help keep individual lines shorter.

# Common Errors

1. **Treating 99 characters as a hard limit** -- Aggressively wrapping lines to stay under 99 characters can sometimes reduce readability. Use judgment.
2. **Ignoring the limit entirely** -- Lines of 150+ characters are difficult to read in most editors and code review tools.

# Common Confusions

1. **Soft vs. hard limit** -- Unlike some style guides that enforce line length via linters, this is advisory. The guide explicitly states "code is allowed to exceed this limit."
2. **99 vs. 80 characters** -- Many older style guides use 80 characters. The Uber Go style uses 99, which accommodates modern wide-screen displays while still encouraging readability.

# Source Reference

- Source: "Uber Go Style Guide"
- Chapter: "Style" (Ch 4)
- Section: "Avoid overly long lines"

# Verification Notes

- Extraction confidence: high -- Explicitly defined section with clear statement of the 99-character soft limit.
