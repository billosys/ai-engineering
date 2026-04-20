---
concept: Code Coverage
slug: jest-code-coverage
category: tooling
subcategory: testing
tier: intermediate
source: "JavaScript: The Definitive Guide, 7th Edition"
source_slug: js-definitive-guide
authors: "David Flanagan"
chapter: "JavaScript Tools and Extensions"
chapter_number: 17
pdf_page: 657
section: "17.3 Unit Testing with Jest"
extraction_confidence: high
aliases:
  - test coverage
  - "--coverage"
prerequisites:
  - jest-testing-framework
extends:
  - jest-testing-framework
related: []
contrasts_with: []
answers_questions:
  - "How do I write and run unit tests with Jest?"
---

# Quick Definition

Jest's `--coverage` flag measures and reports what percentage of statements, branches, functions, and lines in your code are exercised by your tests.

# Core Definition

When invoked with the `--coverage` argument, Jest computes and displays code coverage for the tested modules. Coverage includes four metrics: statement coverage (% Stmts), branch coverage (% Branch), function coverage (% Funcs), and line coverage (% Lines). The report also shows uncovered line numbers, helping developers identify untested code paths (Flanagan, Ch. 17, pp. 657-658).

# Prerequisites

- **jest-testing-framework** — Coverage is a Jest feature.

# Key Properties

1. Enable with `jest --coverage`.
2. Reports: % Statements, % Branches, % Functions, % Lines.
3. Shows uncovered line numbers.
4. 100% coverage of the module under test is the goal; mocked modules show partial coverage.

# Construction / Recognition

```bash
$ jest --coverage getTemperature
File             | % Stmts | % Branch | % Funcs | % Lines |
getTemperature.js|  100    |  100     |  100    |  100    |
```

# Context & Application

Used to identify untested code paths and ensure adequate test coverage before releases.

# Examples

From the source (p. 658): Running `jest --coverage getTemperature` shows 100% coverage for the module under test but only partial coverage for the mocked dependency, which is expected.

# Relationships

## Builds Upon
- **jest-testing-framework** — Coverage is an output of running tests

## Enables
- Identifying untested code paths

## Related
- (None)

## Contrasts With
- (None)

# Common Errors

- **Error**: Chasing 100% coverage on mocked modules.
  **Correction**: Partial coverage on mocked modules is expected and intentional.

# Common Confusions

- **Confusion**: 100% code coverage means zero bugs.
  **Clarification**: Coverage measures which code runs, not whether it produces correct results. Tests need meaningful assertions too.

# Source Reference

Chapter 17: JavaScript Tools and Extensions, Section 17.3, pages 657-658.

# Verification Notes

- Definition source: Direct from source text
- Confidence rationale: Clear output example
- Uncertainties: None
- Cross-reference status: Verified
