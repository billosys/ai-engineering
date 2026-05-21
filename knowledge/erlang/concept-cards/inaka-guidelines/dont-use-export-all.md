---
concept: Don't export_all
slug: dont-use-export-all
category: api-design
subcategory: misc
tier: foundational
source: "Erlang Coding Standards & Guidelines"
source_slug: inaka-guidelines
authors: Inaka
chapter: "Misc"
chapter_number: null
pdf_page: null
section: "Don't export_all"
extraction_confidence: high
aliases:
  - "no export_all"
  - "compile export_all"
prerequisites: []
extends: []
related:
  - dont-use-import
  - encapsulate-otp-apis
  - facade-pattern-for-libraries
contrasts_with: []
answers_questions:
  - "Why shouldn't I use -compile(export_all)?"
---

# Quick Definition

Do not use the `-compile(export_all)` directive.

# Core Definition

"Do not use the `-compile(export_all)` directive" (Inaka, "Don't export_all"). A module explicitly lists only the specific functions that form its documented external API in `-export`.

# Prerequisites

This is a foundational concept with no prerequisites within this source.

# Key Properties

1. `-compile(export_all)` is not used.
2. The `-export` list names exactly the intended public API.
3. A small, deliberate export list encourages good encapsulation.
4. It is a PR-rejection rule under Misc.

# Construction / Recognition

## To Apply

1. Replace `-compile(export_all)` with an explicit `-export([...])` listing only public functions.

## To Recognize a Violation

1. The module contains `-compile(export_all)`.

# Context & Application

A PR-blocking convention under Misc.

- **Typical contexts**: modules where `export_all` was added for quick testing convenience.
- **Common applications**: `-export([real_fun/0, other_fun/0])` instead of exporting everything.

# Examples

**Example 1** — bad: `-compile(export_all)` with a commented-out explicit `-export`.

**Example 2** — good: an explicit `-export([real_fun/0, other_fun/0])`.

# Relationships

## Related

- **Don't import** — companion rule on explicit, visible module boundaries.
- **Encapsulate OTP server APIs** — a small public surface supports encapsulation.
- **Use the facade pattern on libraries** — both keep the exposed API deliberate and minimal.

# Common Errors

- **Error**: Leaving `-compile(export_all)` in place after testing.
  **Correction**: Export only the documented public functions.

# Common Confusions

- **Confusion**: Thinking a wide export surface is harmless.
  **Clarification**: A small, consistent API enables aggressive internal refactoring without breaking callers.

# Source Reference

"Erlang Coding Standards & Guidelines" — Inaka. Section "Misc", guideline "Don't export_all".

# Verification Notes

- Definition source: Direct quote from the guideline.
- Confidence rationale: HIGH — explicit rule with a bad/good example.
- Uncertainties: None.
- Cross-reference status: all referenced slugs are planned cards in this extraction.
