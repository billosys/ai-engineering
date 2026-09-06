---
name: testing
description: |
  Component framework/operational skill for testing discipline, coverage
  hardening, and validation gates. Use when tests, coverage, lint/format
  pressure, or repository validation must prove real behavior rather than
  satisfy a metric cosmetically.
version: 1.1.1
license: MIT
metadata:
  hermes:
    tags: [ai-engineering, testing, coverage, validation]
    category: meta-skills
---

# Testing

Use this component when the work is about testing discipline, coverage
hardening, validation pressure, or coverage-driven repair. It routes to focused
guides for fixing causes rather than hiding failures.

Read only the guide needed for the work:

- [Testing Discipline](./guides/01-testing-discipline.md) - general testing
  quality floor, behavior-focused tests, and failure triage.
- [Coverage Hardening](./guides/02-coverage-hardening.md) - hard 95%+
  coverage work, systematic gap closure, and anti-patterns.
- [Validation Gates](./guides/03-validation-gates.md) - repository-native test,
  lint, format, package, CI, release, and generated-artifact gates.

This is a component entrypoint for the collaboration framework. It is included
inside `collaboration-framework.zip` as routed dependency material and also
ships as the standalone `testing.zip` package.

Component history lives in [version-history.md](./version-history.md).
