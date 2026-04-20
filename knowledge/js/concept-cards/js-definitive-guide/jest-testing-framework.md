---
concept: Jest Testing Framework
slug: jest-testing-framework
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
  - Jest
  - unit testing
  - describe/test/expect
prerequisites: []
extends: []
related:
  - jest-matchers
  - jest-mocking
  - jest-async-testing
  - jest-code-coverage
contrasts_with: []
answers_questions:
  - "How do I write and run unit tests with Jest?"
---

# Quick Definition

Jest is a popular all-in-one JavaScript testing framework providing `describe()` for test suites, `test()` for individual tests, `expect()` for assertions, built-in mocking with `jest.mock()`, and code coverage reporting with `--coverage`.

# Core Definition

Jest is a popular framework that includes everything needed for JavaScript unit testing in a single package: a test runner, assertion library, and mocking tools. Tests are organized with `describe()` blocks and individual `test()` functions. Assertions use `expect(value).toBe(expected)` and other matchers. Jest supports async testing naturally -- async test functions can use `await`. Mock functions track how they were called, and `jest.mock()` replaces entire modules. Code coverage is available via `--coverage` (Flanagan, Ch. 17, pp. 655-658).

# Prerequisites

This is a foundational tooling concept with no prerequisites within this source.

# Key Properties

1. `describe(name, fn)` groups related tests.
2. `test(name, fn)` defines an individual test.
3. `expect(value)` creates an assertion with chainable matchers.
4. `jest.mock(module)` replaces a module with a mock.
5. `--coverage` flag reports code coverage.
6. Async tests: test functions can be `async` and use `await`.

# Construction / Recognition

```javascript
describe("getTemperature()", () => {
  test("Invokes the correct API", async () => {
    let t = await getTemperature("Vancouver");
    expect(getJSON).toHaveBeenCalledWith(expectedURL);
  });
  test("Converts C to F correctly", async () => {
    expect(await getTemperature("x")).toBe(32);
  });
});
```

# Context & Application

The standard testing tool for many JavaScript projects. Used in development, CI/CD pipelines, and as part of the development workflow.

# Examples

From the source (p. 655-658): Testing a `getTemperature()` function that fetches data from a web service. The test mocks the HTTP dependency, verifies the correct URL is called, and checks the temperature conversion formula.

# Relationships

## Builds Upon
- (None - foundational tooling concept)

## Enables
- **jest-matchers** — Assertion methods
- **jest-mocking** — Module mocking
- **jest-async-testing** — Async test support
- **jest-code-coverage** — Coverage reporting

## Related
- (None)

## Contrasts With
- (None)

# Common Errors

- **Error**: Forgetting to `await` in async tests, causing the test to pass before the assertion runs.
  **Correction**: Always `await` async operations inside test functions, or return the Promise.

# Common Confusions

- **Confusion**: Jest is only for React projects.
  **Clarification**: Jest works with any JavaScript project, not just React.

# Source Reference

Chapter 17: JavaScript Tools and Extensions, Section 17.3, pages 655-658.

# Verification Notes

- Definition source: Direct from source text
- Confidence rationale: Complete example showing describe/test/expect/mock/coverage
- Uncertainties: None
- Cross-reference status: Verified
