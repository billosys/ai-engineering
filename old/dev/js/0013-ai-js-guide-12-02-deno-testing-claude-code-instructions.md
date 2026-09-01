# ai-js Guide 12-02: Deno Testing — Claude Code Instructions

## Context

We're building `ai-js`, a repo of curated JavaScript guides that Claude
Code reads via a SKILL.md entry point to produce consistently high-quality
JS code. This is modeled on our `ai-rust` repo.

Guides 01–11 are complete, and we're working through the Deno sub-guide
series (Guide 12):

| Chapter | Slug | Status |
|---------|------|--------|
| 12-01 | `12-deno/01-runtime-basics.md` | In progress |
| 12-02 | `12-deno/02-testing.md` | **This prompt** |
| 12-03 | `12-deno/03-task-runner.md` | Pending |
| 12-04 | `12-deno/04-publishing.md` | Pending |

This prompt is for **12-02: Testing** — everything a developer needs
to write, organize, and run tests in Deno. Covers `Deno.test()`, the
`@std/assert` assertion library, async test patterns, test organization
(grouping, steps, filtering), mocking and stubbing with `@std/testing`,
BDD-style tests, snapshot testing, `deno test --doc` for documentation
tests, test coverage, and permissions for tests.

Existing guides have already touched on testing tangentially:
- Guide 03 uses `Deno.test()` in error handling examples
- Guide 08 covers `Deno.bench()` for microbenchmarks (not tests)
- Guide 10 covers test file naming (`*_test.js`) and co-location
- Guide 11 covers test naming as documentation and `deno test --doc`

This chapter is the comprehensive testing reference. It should not
re-teach test naming (Guide 11) or file placement (Guide 10), but
should cross-reference them and cover everything else.

The target environment is:
- **Deno** (not Node.js — no Jest, no Mocha, no Vitest)
- **Biome** for linting and formatting (not ESLint, not Prettier)
- **ESM-only** (`import`/`export`, no CommonJS)
- **No TypeScript** (plain JS with JSDoc where needed)
- This is the JS used in the **lykn** project (s-expression syntax for JS)

## The full ai-js guide list

Use these numbers and slugs for all cross-references.

| # | Slug | Title |
|---|------|-------|
| 01 | `01-core-idioms.md` | Core Idioms |
| 02 | `02-api-design.md` | API Design |
| 03 | `03-error-handling.md` | Error Handling |
| 04 | `04-values-references.md` | Values & References |
| 05 | `05-type-discipline.md` | Type Discipline (without TypeScript) |
| 06 | `06-functions-closures.md` | Functions & Closures |
| 07 | `07-async-concurrency.md` | Async & Concurrency |
| 08 | `08-performance.md` | Performance |
| 09 | `09-anti-patterns.md` | Anti-Patterns |
| 10 | `10-project-structure.md` | Project Structure |
| 11 | `11-documentation.md` | Documentation |
| 12 | `12-deno/` | Deno (multi-part sub-guide) |
|    | `12-deno/01-runtime-basics.md` | Runtime Basics |
|    | `12-deno/02-testing.md` | Testing |
|    | `12-deno/03-task-runner.md` | Task Runner |
|    | `12-deno/04-publishing.md` | Publishing |
| 13 | `13-biome/` | Biome (multi-part sub-guide) |
|    | `13-biome/01-setup.md` | Setup |
|    | `13-biome/02-lint-rules.md` | Lint Rules |
|    | `13-biome/03-formatting.md` | Formatting |
| 14 | `14-no-node-boundary.md` | No-Node Boundary |

## Reference material

You have a concept card library under `concept-cards/`. These are your
authoritative references — the guide must be grounded in what the cards
say, not in general knowledge.

### Source priority

For this guide, **Deno concept cards are the primary authority** for
Deno-specific testing features. JS language cards are secondary — use
them for testing patterns that are language-level (async tests, error
assertions, etc.).

1. `concept-cards/deno/` — **PRIMARY**. Deno test runner, standard
   library testing utilities.
2. `concept-cards/exploring-js/` — Secondary. Assertion patterns,
   async test patterns, unit testing philosophy.
3. `concept-cards/js-definitive-guide/` — Secondary. Jest patterns
   are NOT applicable, but the testing concepts (mocking, coverage)
   translate.
4. `concept-cards/eloquent-js/` — Secondary. Testing philosophy.

### Concept cards to read for this guide

Read these cards before writing. This is not exhaustive — if you find
related cards while reading, use them too.

**Deno test runner**:
- `deno/deno-test-runner.md`
- `deno/deno-standard-library.md`
- `deno/deno-permissions-system.md`

**Assertions (Exploring JS)**:
- `exploring-js/unit-testing.md`
- `exploring-js/assertions.md`
- `exploring-js/assert-equal.md`
- `exploring-js/assert-deep-equal.md`
- `exploring-js/assert-throws.md`
- `exploring-js/assert-fail.md`
- `exploring-js/async-tests.md`

**Testing philosophy**:
- `eloquent-js/testing.md`
- `eloquent-js/assertion.md`

**Jest (for concept translation, not API)**:
- `js-definitive-guide/jest-testing-framework.md`
- `js-definitive-guide/jest-mocking.md`
- `js-definitive-guide/jest-code-coverage.md`

**Async patterns (for async tests)**:
- `exploring-js/async-function.md`
- `exploring-js/await-operator.md`
- `exploring-js/promise-all.md`
- `exploring-js/fire-and-forget.md`

**Error handling (for error assertions)**:
- `exploring-js/error-class.md`
- `exploring-js/async-function-error-handling.md`

## Structural template

Follow the same format as the existing guides (01–11):

Each idiom entry has:
```
## ID-XX: [Title]

**Strength**: MUST | SHOULD | CONSIDER

**Summary**: One sentence.

[Code examples with // Good and // Bad labels]

**Rationale**: Why this matters. Cite concept card sources.

**See also**: Cross-references to other IDs or guides
```

End with:
- Quick Reference Table
- Related Guidelines — use the format from Guide 09: list specific
  ID numbers per guide for direct navigation.
- External References

## Proposed idiom list

This is a starting outline — adjust based on what the concept cards
emphasize. Add idioms if the cards reveal important patterns. Remove
or merge if redundant. Aim for 25-35 idioms.

### `Deno.test()` basics

1. `Deno.test()` — the built-in test runner, no framework needed
   (MUST)
2. Test function signatures — name + fn, or options object (SHOULD)
3. Async tests — return a Promise or use `async fn` (MUST)
4. Test permissions — `permissions` option for sandboxed tests
   (SHOULD)
5. `ignore` and `only` — skip and focus tests during development
   (SHOULD)

### Assertions — `@std/assert`

6. Import from `@std/assert` — `assertEquals`, `assertStrictEquals`,
   `assertThrows`, etc. (MUST)
7. `assertEquals` for deep structural equality (MUST)
8. `assertStrictEquals` for identity/reference equality (SHOULD)
9. `assertThrows` and `assertRejects` for error testing (MUST)
10. `assertExists`, `assertInstanceOf`, `assertStringIncludes`,
    `assertArrayIncludes`, `assertMatch` — targeted assertions
    (SHOULD)
11. `assertObjectMatch` for partial object matching (SHOULD)
12. `unreachable()` / `fail()` for paths that should never execute
    (SHOULD)
13. Custom assertion messages — the optional `msg` parameter (SHOULD)

### Test organization

14. Test steps — `t.step()` for subtests within a test (SHOULD)
15. Test grouping with `describe`/`it` from `@std/testing/bdd`
    (CONSIDER)
16. Filtering tests: `deno test --filter "pattern"` (SHOULD)
17. Running specific test files: `deno test auth_test.js` (SHOULD)

### Setup and teardown

18. Setup/teardown within tests — no magic `beforeEach`; use plain
    functions or `t.step()` (SHOULD)
19. Resource cleanup — `using` declarations and `Deno.close()` in
    tests (SHOULD)
20. `@std/testing/bdd` — `beforeEach`, `afterEach`, `beforeAll`,
    `afterAll` when BDD style is used (CONSIDER)

### Mocking and stubbing

21. `@std/testing/mock` — `spy()` for observing calls (SHOULD)
22. `@std/testing/mock` — `stub()` for replacing behavior (SHOULD)
23. `@std/testing/mock` — `assertSpyCalls`, `assertSpyCallArgs`
    for verification (SHOULD)
24. `@std/testing/mock` — `returnsNext()`, `returnsArg()` for
    stub return values (CONSIDER)
25. Restore stubs — always clean up, use `try/finally` (MUST)

### Snapshot testing

26. `@std/testing/snapshot` — `assertSnapshot()` for golden-file
    testing (CONSIDER)
27. Update snapshots: `deno test -- --update` (CONSIDER)

### Documentation tests

28. `deno test --doc` — extract and test JSDoc code blocks (SHOULD)

### Coverage

29. `deno test --coverage` for line/branch coverage reporting
    (SHOULD)
30. Coverage output formats — lcov for CI integration (CONSIDER)

### Practical patterns

31. Testing async code — `await` results, `assertRejects` for
    failures (MUST)
32. Testing `Deno.serve()` handlers — construct `Request` objects,
    assert on `Response` (SHOULD)
33. Isolating file system tests — use `Deno.makeTempDir()` for
    temp directories (SHOULD)
34. Testing with environment variables — `Deno.env.set()` in tests
    with cleanup (SHOULD)

## Boundaries with other guides and chapters

**Guide 10 (Project Structure)** already covers:
- Test file naming: `*_test.js` (10 ID-07)
- Co-locating tests with source (10 ID-20)
- Test utilities in `testing/` (10 ID-21)

**Guide 11 (Documentation)** already covers:
- Test names as documentation (11 ID-18)
- `deno test --doc` for documentation examples (11 ID-10, 12)

**Guide 08 (Performance)** already covers:
- `Deno.bench()` for benchmarks (08 ID-02)

**12-01 (Runtime Basics)** covers:
- Deno permission model (the basis for test permissions)
- `Deno.serve()` API (the basis for HTTP handler testing)
- `@std/` standard library overview

**Do NOT re-teach** test file naming (Guide 10), test naming as
documentation (Guide 11), or benchmarking (Guide 08). Cross-reference
them. This chapter covers the *mechanics* of writing and running
tests: the API, the assertion library, mocking, organization,
coverage, and practical patterns.

## Output

Save as: `guides/12-deno/02-testing.md` in the `ai-js` repo.

## Quality bar

- The Deno concept cards and `@std/` library are the primary sources.
  Cite them specifically.
- Code examples must use `Deno.test()` and `@std/assert` — not Jest,
  Mocha, Vitest, or any other test framework.
- Every assertion example should show realistic test code, not
  `assertEquals(1 + 1, 2)` toy examples.
- The async testing section is critical — async tests are where most
  testing bugs occur. Show `assertRejects`, proper `await` patterns,
  and the "fire-and-forget in tests" trap.
- The mocking section should use `@std/testing/mock` exclusively —
  no Sinon, no Jest mock syntax.
- The `Deno.test()` permissions option is a unique Deno feature.
  Show how to sandbox tests with minimal permissions (e.g., a test
  that reads files should use `permissions: { read: true }`, not
  run with `--allow-all`).
- `t.step()` for test steps is Deno's answer to nested `describe`
  blocks. Show it as the primary organization tool, with BDD
  (`describe`/`it`) as a CONSIDER alternative.
- The `deno test --doc` entry should clarify exactly what syntax
  Deno extracts and executes (triple-backtick code blocks in JSDoc).
  Guide 11 promised this chapter would cover the details.
- HTTP handler testing (constructing `Request`, asserting `Response`)
  is a common practical need in Deno server code. Include a
  realistic example.
- Match the existing guides' terse, direct style. This is a
  reference, not a testing tutorial.

## What NOT to do

- Don't include Jest, Mocha, Vitest, or any non-Deno test framework
- Don't include `describe`/`it` from libraries other than
  `@std/testing/bdd`
- Don't include React Testing Library, DOM testing, or browser test
  patterns
- Don't include TypeScript-specific test patterns
- Don't re-teach test naming (Guide 11) or test file placement
  (Guide 10) — cross-reference them
- Don't include `Deno.bench()` — that's in Guide 08
- Don't include E2E testing frameworks (Playwright, Puppeteer,
  Cypress)
- Don't include test-driven development methodology or testing
  philosophy beyond what's needed to justify specific patterns
- Don't include Deno Deploy testing or integration testing patterns
  that require external services
- Don't include CI/CD pipeline configuration — that's operational,
  not testing mechanics
- Don't over-emphasize BDD style — `Deno.test()` with `t.step()`
  is the primary pattern; BDD is an alternative for teams that
  prefer it
