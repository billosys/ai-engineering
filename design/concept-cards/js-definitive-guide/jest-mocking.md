---
concept: Mocking with jest.mock()
slug: jest-mocking
category: tooling
subcategory: testing
tier: intermediate
source: "JavaScript: The Definitive Guide, 7th Edition"
source_slug: js-definitive-guide
authors: "David Flanagan"
chapter: "JavaScript Tools and Extensions"
chapter_number: 17
pdf_page: 655
section: "17.3 Unit Testing with Jest"
extraction_confidence: high
aliases:
  - jest.mock
  - mock functions
  - mockResolvedValue
prerequisites:
  - jest-testing-framework
extends:
  - jest-testing-framework
related:
  - jest-matchers
contrasts_with: []
answers_questions:
  - "How do I write and run unit tests with Jest?"
---

# Quick Definition

`jest.mock(modulePath)` replaces a module's exports with mock functions that track calls and can be configured to return specific values, enabling isolated testing without real dependencies.

# Core Definition

Jest's `jest.mock()` function replaces a module's real implementation with a mock. After mocking, `require()` returns the mock instead of the real module. Mock functions remember how they were called (enabling assertions like `toHaveBeenCalledWith()`). `mockResolvedValue(value)` configures a mock to return an already-resolved Promise, useful for testing async code that depends on network requests (Flanagan, Ch. 17, pp. 656-657).

# Prerequisites

- **jest-testing-framework** — Must understand the Jest testing structure.

# Key Properties

1. `jest.mock("./module")` replaces the module with mocks.
2. Mock functions track calls: `toHaveBeenCalledWith()`.
3. `mockResolvedValue(value)` returns a resolved Promise.
4. `mockReturnValue(value)` returns a synchronous value.
5. Mocks isolate the code under test from its dependencies.

# Construction / Recognition

```javascript
jest.mock("./getJSON");
const getJSON = require("./getJSON.js");
getJSON.mockResolvedValue(0);
// ...
expect(getJSON).toHaveBeenCalledWith(expectedURL);
```

# Context & Application

Essential for unit testing functions that depend on external services, APIs, or complex subsystems. Mocking isolates the unit under test.

# Examples

From the source (p. 656): The `getTemperature()` test mocks the `getJSON()` module so no actual network requests are made, then configures it to return specific temperature values.

# Relationships

## Builds Upon
- **jest-testing-framework** — Part of Jest's testing API

## Enables
- Isolated unit testing without real dependencies

## Related
- **jest-matchers** — Used to assert mock call behavior

## Contrasts With
- (None)

# Common Errors

- **Error**: Calling `jest.mock()` after `require()` instead of before.
  **Correction**: `jest.mock()` is hoisted automatically by Jest, but the mock must be declared before the module under test is required.

# Common Confusions

- **Confusion**: Mocking replaces the module for all tests.
  **Clarification**: `jest.mock()` at the top of a test file applies to that file. Use `jest.resetAllMocks()` or `beforeEach` to reset state between tests.

# Source Reference

Chapter 17: JavaScript Tools and Extensions, Section 17.3, pages 655-658.

# Verification Notes

- Definition source: Direct from source text
- Confidence rationale: Clear example with mockResolvedValue and assertion
- Uncertainties: None
- Cross-reference status: Verified
