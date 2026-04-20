---
concept: Deno Test Runner
slug: deno-test-runner
category: toolchain
subcategory: testing
tier: foundational
source: "Deno Documentation"
source_slug: deno
authors: "Deno Contributors"
chapter: "runtime/fundamentals/testing.md"
chapter_number: null
pdf_page: null
section: "Testing"
extraction_confidence: high
aliases:
  - "deno test"
  - "Deno.test"
  - "Deno testing"
prerequisites:
  - deno-configuration
extends: []
related:
  - deno-linter
  - deno-formatter
contrasts_with: []
answers_questions:
  - "What is the Deno test runner?"
  - "How do I run tests in Deno?"
  - "How do I write tests in Deno?"
---

# Quick Definition

Deno includes a built-in test runner accessed via `deno test` that uses the `Deno.test()` function for defining tests, with built-in assertions, test filtering, sanitizers, coverage, hooks, and per-test permission control — requiring no external dependencies.

# Core Definition

The Deno test runner is a zero-dependency testing framework built into the Deno runtime. Tests are defined using `Deno.test()`, which accepts a name and a function (sync or async). The `deno test` subcommand automatically discovers and executes test files matching the glob `{*_,*.,}test.{ts, tsx, mts, js, mjs, jsx}`.

Key capabilities include:

- **Assertions**: The standard library provides `assertEquals`, `expect` (Jest-like), and other assertion utilities via `jsr:@std/assert` and `jsr:@std/expect`.
- **Test steps**: `t.step()` allows breaking tests into sub-steps for setup/teardown within a test.
- **Test hooks**: `Deno.test.beforeAll()`, `Deno.test.beforeEach()`, `Deno.test.afterEach()`, `Deno.test.afterAll()` for lifecycle management. Before hooks run FIFO; after hooks run LIFO.
- **Filtering**: `--filter` accepts string or regex patterns to run specific tests.
- **Test selection**: `Deno.test.only()` to focus on specific tests, `Deno.test.ignore()` to skip tests.
- **Sanitizers**: Resource sanitizer (detects unclosed I/O), async operation sanitizer (detects un-awaited promises), and exit sanitizer (prevents `Deno.exit()` false positives). All enabled by default, disablable per-test.
- **Coverage**: `--coverage` flag collects V8 coverage data, processable to `lcov` via `deno coverage`.
- **Reporters**: `pretty` (default), `dot`, and `junit` output formats.
- **Permissions**: Per-test permission configuration to deny specific permissions for testing fallback behavior.
- **Parallel execution**: `--parallel` flag runs test modules concurrently.
- **Documentation tests**: `--doc` extracts and runs code examples from JSDoc and markdown.
- **BDD style**: `describe`/`it` syntax available via `@std/testing/bdd`.

# Prerequisites

- `deno-configuration` — test include/exclude paths can be configured in `deno.json`

# Key Properties

1. **Zero configuration**: Tests run out of the box with `deno test` — no setup files or configuration needed.
2. **Permission-aware**: Tests can specify `permissions` to deny specific permissions, enabling testing of permission-denied fallback paths.
3. **Sanitizers prevent leaks**: Resource, async operation, and exit sanitizers catch common testing pitfalls by default.
4. **Doc testing**: Code blocks in JSDoc comments and markdown can be extracted and run as tests with `--doc`.
5. **Hooks**: Full lifecycle hooks (`beforeAll`, `beforeEach`, `afterEach`, `afterAll`) with deterministic execution order.
6. **Fail fast**: `--fail-fast` stops on the first test failure.

# Construction / Recognition

Basic test definition:

```ts
import { assertEquals } from "jsr:@std/assert";

Deno.test("simple test", () => {
  const x = 1 + 2;
  assertEquals(x, 3);
});
```

Test with steps:

```ts
Deno.test("database operations", async (t) => {
  using db = await openDatabase();
  await t.step("insert user", async () => { /* ... */ });
  await t.step("insert book", async () => { /* ... */ });
});
```

Test with permission restrictions:

```ts
Deno.test({
  name: "falls back without permission",
  permissions: { read: false },
  fn: async () => {
    const result = await getFileText();
    assertEquals(result, "oops don't have permission");
  },
});
```

# Context & Application

The built-in test runner eliminates the need for external test frameworks like Jest or Mocha (though those are also supported). It integrates tightly with Deno's permission system, allowing tests to verify security-conscious behavior. The sanitizers are particularly valuable for catching resource leaks and unawaited async operations that would silently pass in other test runners.

# Examples

**Running tests** (from `runtime/fundamentals/testing.md`):
```sh
deno test                          # All tests in current directory
deno test util/                    # Tests in specific directory
deno test my_test.ts               # Single file
deno test --parallel               # Parallel execution
deno test --filter "my" tests/     # Filter by name
deno test --coverage               # With coverage collection
deno test --reporter=junit         # JUnit output
deno test --doc example.ts         # Run doc tests
```

**BDD style** (from `runtime/fundamentals/testing.md`):
```ts
import { describe, it } from "jsr:@std/testing/bdd";
import { expect } from "jsr:@std/expect";

describe("add function", () => {
  it("adds two numbers correctly", () => {
    expect(add(2, 3)).toBe(5);
  });
});
```

# Relationships

- **Related**: `deno-linter` — linting and testing are complementary quality tools
- **Related**: `deno-formatter` — consistent code style supports testable code
- **Related**: `deno-configuration` — test include/exclude configured in `deno.json`

# Common Errors

1. **Not awaiting async operations**: The async operation sanitizer will flag un-awaited promises. Always `await` async calls in tests.
2. **Unclosed resources**: Opening files or connections without closing them triggers the resource sanitizer. Use `using` declarations or explicit `.close()`.
3. **Short-lived scripts with `--inspect`**: When debugging tests, use `--inspect-wait` or `--inspect-brk` since `--inspect` may finish before the debugger connects.

# Common Confusions

- **`permissions` in tests deny, not grant**: The `permissions` property in `Deno.test()` can only restrict permissions already granted at the command line; it cannot grant new permissions.
- **`Deno.test.only` always fails the suite**: Using `only` is a debugging aid — the overall test run will always fail when any test has `only: true`.

# Source Reference

Source: "Deno Documentation", file `runtime/fundamentals/testing.md`, all sections.

# Verification Notes

All features described are explicitly documented in the source file. Extraction confidence is high.
