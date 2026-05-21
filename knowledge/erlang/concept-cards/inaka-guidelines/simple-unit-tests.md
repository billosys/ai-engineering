---
concept: Simple Unit Tests
slug: simple-unit-tests
category: testing
subcategory: source-code-layout
tier: foundational
source: "Erlang Coding Standards & Guidelines"
source_slug: inaka-guidelines
authors: Inaka
chapter: "Source Code Layout"
chapter_number: null
pdf_page: null
section: "Simple unit tests"
extraction_confidence: high
aliases:
  - "small unit tests"
  - "one assert per test"
  - "single responsibility for tests"
prerequisites: []
extends: []
related:
  - keep-functions-small
  - no-god-modules
contrasts_with: []
answers_questions:
  - "How many assertions should a unit test have?"
  - "How should I structure unit tests?"
---

# Quick Definition

Keep unit tests short — no more than one or two assertions per test — so each test checks a single thing.

# Core Definition

"Single responsibility applies to tests as well. When writing **unit** tests, keep them short and don't put more than 1 or 2 asserts per test" (Inaka, "Simple unit tests"). Each unit test exercises one scenario; multiple scenarios become multiple tests.

# Prerequisites

This is a foundational concept with no prerequisites within this source.

# Key Properties

1. A unit test contains at most 1–2 assertions.
2. Each distinct scenario gets its own test function.
3. The single-responsibility principle applies to tests, not just production code.
4. It is a PR-rejection rule under Source Code Layout.

# Construction / Recognition

## To Apply

1. Identify the distinct cases under test (e.g., zero, positive, negative input).
2. Write one test function per case, each with a single assert.

## To Recognize a Violation

1. One test function asserts several unrelated expectations in sequence.

# Context & Application

A PR-blocking convention; applies to **unit** tests specifically (not integration tests).

- **Typical contexts**: EUnit and Common Test suites.
- **Common applications**: splitting one `bad/1` test into `good1/1`, `good2/1`, `good3/1`.

# Examples

**Example 1** — bad: a single `bad/1` Common Test case asserts the result for input 0, a positive input, and a negative input.

**Example 2** — good: `good1`, `good2`, `good3` each assert exactly one of those cases.

# Relationships

## Related

- **Keep functions small** — the same single-responsibility principle for functions.
- **No God modules** — single responsibility at the module level.

# Common Errors

- **Error**: Packing every expectation into one mega-test.
  **Correction**: One scenario per test; a failing run then pinpoints every broken case at once.

# Common Confusions

- **Confusion**: Thinking the rule applies to integration tests.
  **Clarification**: The source scopes it explicitly to **unit** tests.

# Source Reference

"Erlang Coding Standards & Guidelines" — Inaka. Section "Source Code Layout", guideline "Simple unit tests".

# Verification Notes

- Definition source: Direct quote from the guideline.
- Confidence rationale: HIGH — explicit rule with bad/good Common Test examples.
- Uncertainties: None.
- Cross-reference status: all referenced slugs are planned cards in this extraction.
