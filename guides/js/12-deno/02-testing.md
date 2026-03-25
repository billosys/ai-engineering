# Deno Testing

Everything you need to write, organize, and run tests in Deno: `Deno.test()`, assertions, async patterns, test organization, mocking, snapshots, documentation tests, coverage, and practical patterns. This is the comprehensive testing reference — test file naming is in Guide 10 (ID-07, ID-20), test naming as documentation is in Guide 11 (ID-18). Grounded in Deno documentation concept cards and *Exploring JavaScript* (Rauschmayer).

Target environment: **Deno**, **ESM-only**, **no TypeScript** (plain JS with JSDoc where needed). No Jest, Mocha, or Vitest.

---

## ID-01: `Deno.test()` — The Built-In Test Runner

**Strength**: MUST

**Summary**: Deno has a built-in test runner. No framework installation, no configuration — just write `Deno.test()` and run `deno test`.

```js
import { assertEquals } from "@std/assert";

// Simple test — name + function
Deno.test("parseConfig returns default timeout", () => {
  const config = parseConfig("{}");
  assertEquals(config.timeout, 5000);
});

// Async test — return a Promise or use async
Deno.test("fetchUser returns user data", async () => {
  const user = await fetchUser("alice");
  assertEquals(user.name, "Alice");
});
```

```sh
# Run all tests
deno test

# Run specific file
deno test auth_test.js

# Run specific directory
deno test auth/
```

**Rationale**: `deno test` discovers files matching `{*_,*.,}test.{js,mjs,jsx,ts,tsx,mts}` and runs all `Deno.test()` calls. No `package.json` scripts, no test runner config files. Async tests pass when the returned Promise resolves and fail when it rejects (Deno test runner docs; Exploring JS Ch. 8).

**See also**: `10-project-structure.md` ID-07 (file naming), `11-documentation.md` ID-18 (test naming)

---

## ID-02: Test Options Object — Permissions, Ignore, Only

**Strength**: SHOULD

**Summary**: The options object form gives access to permissions, skip/focus, and sanitizer control.

```js
// Options object form
Deno.test({
  name: "writes output file",
  permissions: { write: true, read: true },
  fn: async () => {
    await Deno.writeTextFile("/tmp/test.txt", "hello");
    const content = await Deno.readTextFile("/tmp/test.txt");
    assertEquals(content, "hello");
  },
});

// Skip a test — options form
Deno.test({ name: "flaky on CI", ignore: true, fn: () => { /* ... */ } });

// Skip — static method form (verify availability in your Deno version)
Deno.test.ignore("flaky on CI", () => { /* ... */ });

// Focus during development (suite ALWAYS fails when any only is present)
Deno.test({ name: "debugging this", only: true, fn: () => { /* ... */ } });
```

**Key options**: `name`, `fn`, `permissions`, `ignore`, `only`, `sanitizeResources`, `sanitizeOps`, `sanitizeExit`.

**Note**: The `{ ignore: true }` and `{ only: true }` options object form is supported in all Deno versions. The `Deno.test.ignore()` and `Deno.test.only()` static method forms were added later — verify availability in your Deno version. When in doubt, use the options form.

**Rationale**: The options form is required for permission-restricted tests and for controlling sanitizers. `only: true` is a debugging aid — the suite intentionally fails when any `only` is active, preventing accidental commit of focused tests (Deno test runner docs).

---

## ID-03: Test Permissions — Restrict, Never Grant

**Strength**: SHOULD

**Summary**: The `permissions` option **restricts** permissions already granted at the CLI. It cannot grant new ones.

```js
// Good — test that verifies graceful degradation without read access
Deno.test({
  name: "returns fallback when file is unreadable",
  permissions: { read: false },
  fn: async () => {
    const result = await loadConfigSafe("./config.json");
    assertEquals(result, DEFAULT_CONFIG);
  },
});

// Good — test with minimal permissions
Deno.test({
  name: "parses JSON without I/O",
  permissions: { read: false, write: false, net: false },
  fn: () => {
    const config = parseJSON('{"port": 8080}');
    assertEquals(config.port, 8080);
  },
});
```

**Critical distinction**: `permissions: { read: false }` revokes read access for this test even if `--allow-read` was passed to `deno test`. It does NOT grant permissions that weren't given at the CLI level. This is the most commonly confused behavior in Deno testing.

**Rationale**: Per-test permissions enable testing fallback paths and error handling when specific capabilities are unavailable. This is a unique Deno feature — no other test runner provides sandboxed permission control per test (Deno test runner docs).

---

## ID-04: Async Tests — `await` Results, `assertRejects` for Failures

**Strength**: MUST

**Summary**: Async tests must `await` their assertions. Use `assertRejects` for async functions that should reject.

```js
import { assertEquals, assertRejects } from "@std/assert";

// Good — await the async operation
Deno.test("fetchUser returns user data", async () => {
  const user = await fetchUser("alice");
  assertEquals(user.name, "Alice");
  assertEquals(user.email, "alice@example.com");
});

// Good — assertRejects for async failures
Deno.test("fetchUser rejects for invalid ID", async () => {
  await assertRejects(
    () => fetchUser(-1),
    RangeError,
    "ID must be positive",
  );
});

// Bad — missing await (test passes even if fetchUser rejects)
Deno.test("broken test", () => {
  fetchUser("alice"); // fire-and-forget — rejection is lost
});
```

**Rationale**: Deno's async operation sanitizer (on by default) catches un-awaited Promises in tests. A test that calls an async function without `await` will be flagged — but only if the sanitizer is enabled. Always `await` explicitly rather than relying on the sanitizer as a safety net (Exploring JS Ch. 42; Deno test runner docs).

**See also**: `03-error-handling.md` ID-20 (fire-and-forget), `07-async-concurrency.md` ID-21 (async map)

---

## ID-05: Sanitizers — Resource, Async Op, Exit

**Strength**: SHOULD

**Summary**: Deno's test sanitizers catch leaked resources, un-awaited operations, and premature exits. All three are on by default.

```js
// Bad — resource sanitizer catches unclosed file handle
Deno.test("leaks a file handle", async () => {
  const file = await Deno.open("data.txt");
  // forgot file.close() — sanitizer flags this
});

// Good — explicit cleanup with high-level API
Deno.test("reads file cleanly", async () => {
  const file = await Deno.open("data.txt");
  try {
    // Read the entire file via the stream
    const content = new TextDecoder().decode(await new Response(file.readable).arrayBuffer());
    assertEquals(content.length > 0, true);
  } finally {
    // file.readable consumption closes the resource, but explicit close is safe
    file.close();
  }
});

// Disable sanitizers when needed (e.g., intentional long-lived resource)
Deno.test({
  name: "background task test",
  sanitizeOps: false,
  sanitizeResources: false,
  fn: async () => { /* ... */ },
});
```

**Three sanitizers**:
- **Resource** (`sanitizeResources`): Flags file handles, network connections opened but not closed
- **Async ops** (`sanitizeOps`): Flags Promises started but not awaited
- **Exit** (`sanitizeExit`): Prevents `Deno.exit()` from silently terminating the process

**Rationale**: Sanitizers enforce cleanup discipline. A leaked file handle in one test can corrupt a subsequent test. An un-awaited Promise can reject after the test "passes." These are real bugs that most test frameworks silently miss (Deno test runner docs).

---

## ID-06: `assertEquals` for Deep Structural Equality

**Strength**: MUST

**Summary**: `assertEquals` compares by deep structural equality. Two different objects with the same content are equal.

```js
import { assertEquals } from "@std/assert";

Deno.test("parseConfig returns expected shape", () => {
  const config = parseConfig('{"port": 8080, "host": "localhost"}');
  assertEquals(config, { port: 8080, host: "localhost" });
});

Deno.test("getActiveUsers filters correctly", () => {
  const users = [
    { name: "Alice", active: true },
    { name: "Bob", active: false },
  ];
  assertEquals(getActiveUsers(users), [{ name: "Alice", active: true }]);
});
```

**Rationale**: `assertEquals` is the workhorse assertion — use it for comparing objects, arrays, primitives, and nested structures. It performs recursive deep comparison, not reference equality. For reference/identity equality, use `assertStrictEquals` (Exploring JS Ch. 8; Deno @std/assert docs).

---

## ID-07: `assertStrictEquals` for Identity/Reference Equality

**Strength**: SHOULD

**Summary**: `assertStrictEquals` uses `===`. Use it for primitives and when you need to verify two variables point to the same object.

```js
import { assertStrictEquals } from "@std/assert";

Deno.test("getDefault returns the singleton", () => {
  const a = getDefault();
  const b = getDefault();
  assertStrictEquals(a, b); // same object reference
});

Deno.test("parsePort returns a number", () => {
  assertStrictEquals(parsePort("8080"), 8080);
  assertStrictEquals(typeof parsePort("8080"), "number");
});
```

**Rationale**: `assertEquals({ a: 1 }, { a: 1 })` passes (deep equality). `assertStrictEquals({ a: 1 }, { a: 1 })` fails (different objects). Use `assertStrictEquals` when identity matters — singleton patterns, caching, or verifying exact primitive values (Exploring JS Ch. 8).

---

## ID-08: `assertThrows` and `assertRejects` for Error Testing

**Strength**: MUST

**Summary**: `assertThrows` for synchronous errors. `assertRejects` for async errors. Both accept optional error class and message pattern.

```js
import { assertThrows, assertRejects } from "@std/assert";

// Synchronous throw
Deno.test("parsePort throws on invalid input", () => {
  assertThrows(
    () => parsePort("not-a-number"),
    RangeError,
    "Invalid port",
  );
});

// Async rejection
Deno.test("connect rejects on bad host", async () => {
  await assertRejects(
    () => connect("invalid://host"),
    TypeError,
    "Invalid URL",
  );
});

// Bad — wrapping in try/catch manually (verbose, error-prone)
Deno.test("manual catch — avoid this", () => {
  try {
    parsePort("bad");
    fail("should have thrown"); // easy to forget this line
  } catch (e) {
    assertInstanceOf(e, RangeError);
  }
});
```

**Rationale**: `assertThrows` and `assertRejects` are cleaner than manual `try/catch` because they fail automatically if no error is thrown — no `fail()` sentinel needed. `assertRejects` must be `await`ed (Exploring JS Ch. 8; Deno @std/assert docs).

**See also**: `03-error-handling.md` ID-05 (custom error types)

---

## ID-09: Targeted Assertions — `assertObjectMatch`, `assertStringIncludes`, `assertMatch`

**Strength**: SHOULD

**Summary**: Use targeted assertions for partial matching, substring checks, and regex matching.

```js
import {
  assertObjectMatch,
  assertStringIncludes,
  assertArrayIncludes,
  assertMatch,
} from "@std/assert";

// Partial object match — extra properties on actual are OK
Deno.test("response contains user fields", async () => {
  const response = await fetchUser("alice");
  assertObjectMatch(response, { name: "Alice", role: "admin" });
  // response may have many other fields — only name and role are checked
});

// Substring check
Deno.test("error message includes the filename", () => {
  const err = getLastError();
  assertStringIncludes(err.message, "config.json");
});

// Array includes (subset, order-independent)
Deno.test("getTags returns expected tags", () => {
  assertArrayIncludes(getTags(), ["javascript", "deno"]);
});

// Regex match
Deno.test("version string matches semver", () => {
  assertMatch(getVersion(), /^\d+\.\d+\.\d+$/);
});
```

**Rationale**: `assertObjectMatch` is particularly valuable for API response testing where the full object has many fields but you only care about a subset. These assertions produce clearer failure messages than `assertEquals` with manual extraction (Deno @std/assert docs).

---

## ID-10: `unreachable()` and `fail()` for Dead Code Paths

**Strength**: SHOULD

**Summary**: Use `unreachable()` for code paths that should never execute. Use `fail()` when you need a manual assertion failure.

```js
import { unreachable, fail } from "@std/assert";

Deno.test("switch covers all cases", () => {
  const result = categorize("known-type");
  switch (result.kind) {
    case "a": /* ... */ break;
    case "b": /* ... */ break;
    default: unreachable(); // should never reach here
  }
});

Deno.test("callback is called", async () => {
  let called = false;
  await process({ onComplete: () => { called = true; } });
  if (!called) fail("onComplete callback was never invoked");
});
```

**Rationale**: `unreachable()` throws unconditionally — it marks code paths that should be dead. `fail()` throws an `AssertionError` with a custom message (note: `@std/assert` uses the spelling `AssertionError` — this is the library's actual class name). Both are cleaner than `throw new Error("should not reach here")` because they are semantic and searchable (Deno @std/assert docs).

---

## ID-11: Custom Assertion Messages

**Strength**: SHOULD

**Summary**: Every assertion accepts an optional trailing message parameter. Use it in loops and parameterized tests.

```js
Deno.test("all ports are valid", () => {
  const testCases = [
    { input: "80", expected: 80 },
    { input: "443", expected: 443 },
    { input: "8080", expected: 8080 },
  ];
  for (const { input, expected } of testCases) {
    assertEquals(
      parsePort(input),
      expected,
      `parsePort("${input}") should return ${expected}`,
    );
  }
});
```

**Rationale**: Default failure messages say "Values are not equal" with a diff. In a loop, you need to know *which iteration* failed. Custom messages add that context (Exploring JS Ch. 8).

---

## ID-12: Test Steps — `t.step()` for Subtests

**Strength**: SHOULD

**Summary**: `t.step()` breaks a test into named sub-steps — Deno's answer to nested `describe` blocks.

```js
Deno.test("user lifecycle", async (t) => {
  const user = { name: "Alice", email: "alice@example.com" };
  let userId;

  await t.step("create user", async () => {
    userId = await createUser(user);
    assertExists(userId);
  });

  await t.step("read user back", async () => {
    const found = await getUser(userId);
    assertObjectMatch(found, user);
  });

  await t.step("delete user", async () => {
    await deleteUser(userId);
    assertEquals(await getUser(userId), null);
  });
});
```

**Key behavior**: Steps run sequentially within a test. Each step's name appears in the test output. If a step fails, subsequent steps are skipped. The test context `t` is only available when the test function accepts a parameter.

**Rationale**: Steps provide hierarchy without a BDD framework. They share state within the test (the `userId` variable) while maintaining clear phase separation in output. For teams that prefer `describe`/`it`, see ID-13 (Deno test runner docs).

---

## ID-13: BDD Style — `describe`/`it` from `@std/testing/bdd`

**Strength**: CONSIDER

**Summary**: For teams that prefer Jest/Mocha-style syntax, `@std/testing/bdd` provides `describe`, `it`, and scoped lifecycle hooks.

```js
import { describe, it, beforeEach, afterEach } from "@std/testing/bdd";
import { assertEquals } from "@std/assert";

describe("Calculator", () => {
  let calc;

  beforeEach(() => { calc = new Calculator(); });
  afterEach(() => { calc.reset(); });

  it("adds two numbers", () => {
    assertEquals(calc.add(2, 3), 5);
  });

  it("handles negative numbers", () => {
    assertEquals(calc.add(-1, 1), 0);
  });

  describe("division", () => {
    it("divides correctly", () => {
      assertEquals(calc.divide(10, 2), 5);
    });

    it("throws on division by zero", () => {
      assertThrows(() => calc.divide(1, 0), RangeError);
    });
  });
});
```

**Also available**: `@std/expect` provides Jest-compatible `expect().toBe()`, `.toEqual()`, `.toHaveBeenCalledWith()` for teams migrating from Jest.

**Rationale**: BDD syntax is a wrapper over `Deno.test()` — it compiles down to the same test runner. Use it when the team is more comfortable with `describe`/`it`, or when deeply nested test grouping is needed. `Deno.test()` with `t.step()` is the primary pattern (Deno @std/testing/bdd docs).

---

## ID-14: Filtering and Running Tests

**Strength**: SHOULD

**Summary**: Use `--filter` for name-based selection, path arguments for file-based selection, and flags for execution control.

```sh
# Filter by test name (string or regex)
deno test --filter "parseConfig"
deno test --filter "/database.*integration/"

# Run specific files
deno test auth_test.js users_test.js

# Run a directory
deno test auth/

# Parallel execution (file-level, not test-level)
deno test --parallel

# Stop on first failure
deno test --fail-fast

# JUnit output for CI
deno test --reporter=junit > results.xml

# Combine flags
deno test --parallel --fail-fast --filter "unit"
```

**Rationale**: `--filter` matches against test names (including `t.step` names), enabling surgical test selection without modifying code. `--parallel` runs test modules concurrently for faster suites. `--reporter=junit` integrates with CI dashboards (Deno test runner docs).

---

## ID-15: Setup and Teardown — Plain Functions or `t.step()`

**Strength**: SHOULD

**Summary**: Use plain helper functions or `t.step()` for setup/teardown. Deno's native test API has no magic lifecycle hooks — it's explicit.

```js
// Good — explicit setup/teardown with t.step()
Deno.test("database operations", async (t) => {
  const db = await openTestDatabase();

  await t.step("insert record", async () => {
    await db.insert({ id: 1, name: "Alice" });
    assertEquals(await db.count(), 1);
  });

  await t.step("query record", async () => {
    const record = await db.find(1);
    assertEquals(record.name, "Alice");
  });

  // Teardown — runs even if a step fails (finally block)
  await db.close();
});

// Good — helper function for repeated setup
function createTestContext() {
  const db = new MockDatabase();
  const logger = new MockLogger();
  return { db, logger };
}

Deno.test("process order", () => {
  const { db, logger } = createTestContext();
  processOrder(db, logger, { id: 1 });
  assertEquals(logger.messages.length, 1);
});
```

**Rationale**: Deno's native test API is explicit — no hidden lifecycle hooks. Setup is a function call; teardown is a `finally` block or `afterEach` (with BDD). This makes test execution predictable and debuggable. For teams that need `beforeEach`/`afterEach`, use `@std/testing/bdd` (ID-13) (Deno test runner docs).

---

## ID-16: Mocking with `spy()` — Observe Calls Without Changing Behavior

**Strength**: SHOULD

**Summary**: `spy()` wraps a function to record calls while preserving original behavior.

```js
import { spy, assertSpyCalls, assertSpyCallArgs } from "@std/testing/mock";

Deno.test("processOrder logs the order ID", () => {
  const logSpy = spy(console, "log");
  try {
    processOrder({ id: 42, items: ["widget"] });

    assertSpyCalls(logSpy, 1);
    assertSpyCallArgs(logSpy, 0, ["Processing order: 42"]);
  } finally {
    logSpy.restore();
  }
});

// Standalone spy (not wrapping an existing method)
Deno.test("forEach calls callback for each item", () => {
  const callback = spy();
  ["a", "b", "c"].forEach(callback);
  assertSpyCalls(callback, 3);
  assertSpyCallArgs(callback, 0, ["a", 0, ["a", "b", "c"]]);
});
```

**Rationale**: Spies observe without altering — the original function still runs. Use spies to verify that a dependency was called with the right arguments and the right number of times. Always restore spies in `finally` blocks (Deno @std/testing/mock docs).

---

## ID-17: Stubbing with `stub()` — Replace Behavior

**Strength**: SHOULD

**Summary**: `stub()` replaces a method's implementation while recording calls. Always restore in `finally`.

```js
import { stub, assertSpyCalls, returnsNext } from "@std/testing/mock";

Deno.test("retries on failure then succeeds", async () => {
  const fetchStub = stub(
    globalThis,
    "fetch",
    returnsNext([
      Promise.reject(new Error("network error")),
      Promise.resolve(new Response("ok")),
    ]),
  );
  try {
    const result = await fetchWithRetry("/api/data");
    assertEquals(await result.text(), "ok");
    assertSpyCalls(fetchStub, 2); // called twice: fail then succeed
  } finally {
    fetchStub.restore();
  }
});
```

**Stub return helpers**:
- `returnsNext([v1, v2, ...])` — returns values in sequence, one per call
- `returnsArg(index)` — returns one of its own arguments

**Rationale**: Stubs replace behavior for isolation — test your code without hitting real networks, databases, or file systems. `returnsNext()` is particularly useful for testing retry logic. Always restore: a leaked stub poisons subsequent tests (Deno @std/testing/mock docs).

---

## ID-18: Always Restore Stubs — Use `try/finally`

**Strength**: MUST

**Summary**: Stubs mutate the target object. If a test throws before cleanup, the stub persists and corrupts later tests.

```js
// Good — try/finally guarantees restoration
const s = stub(Deno, "readTextFile", () => Promise.resolve("{}"));
try {
  const config = await loadConfig("./config.json");
  assertEquals(config, {});
} finally {
  s.restore();
}
```

**Note on `using` declarations**: If `@std/testing/mock`'s stub return value implements `Symbol.dispose` (the TC39 Explicit Resource Management protocol), you can use `using s = stub(...)` for automatic cleanup at block exit. Verify this with your version of `@std/testing` before relying on it — if `Symbol.dispose` is not implemented, `using` will silently skip restoration, which is exactly the bug this entry warns against. When in doubt, use `try/finally`.

**Rationale**: A stub on `fetch` or `Deno.readTextFile` that isn't restored will affect every subsequent test in the file. `try/finally` is deterministic and works in all versions (Deno @std/testing/mock docs).

---

## ID-19: Snapshot Testing with `assertSnapshot()`

**Strength**: CONSIDER

**Summary**: Snapshot testing serializes a value and compares it against a stored golden file.

```js
import { assertSnapshot } from "@std/testing/snapshot";

Deno.test("AST output matches snapshot", async (t) => {
  const ast = parse("1 + 2 * 3");
  await assertSnapshot(t, ast);
});

// First run: creates __snapshots__/parser_test.js.snap (matches test file extension)
// Subsequent runs: compares against stored snapshot
```

```sh
# Update snapshots after intentional changes
deno test -- --update
# Note: the -- separator passes --update to the test, not to deno test itself
```

**Rationale**: Snapshots are useful for large, complex outputs (ASTs, rendered HTML, API response shapes) where writing manual assertions is impractical. The test context `t` is required — snapshot identity is tied to the test name. Store snapshot files in version control (Deno @std/testing/snapshot docs).

---

## ID-20: Documentation Tests — `deno test --doc`

**Strength**: SHOULD

**Summary**: `deno test --doc` extracts triple-backtick code blocks from JSDoc comments and runs them as tests.

```js
/**
 * Add two numbers.
 *
 * ```js
 * import { add } from "./math.js";
 * import { assertEquals } from "@std/assert";
 * assertEquals(add(2, 3), 5);
 * ```
 */
export function add(a, b) {
  return a + b;
}
```

```sh
# Run documentation examples as tests
deno test --doc math.js
```

**Key detail**: Deno extracts **fenced code blocks** (triple-backtick) from JSDoc, not `@example` tags specifically. Each code block becomes an independent test module with its own imports.

**Rationale**: Documentation examples that are also tests cannot silently become stale. `--doc` makes documentation a verified artifact — if the example doesn't compile or produces wrong results, CI catches it (Deno test runner docs).

**See also**: `11-documentation.md` ID-10, ID-12

---

## ID-21: Test Coverage — `deno test --coverage`

**Strength**: SHOULD

**Summary**: Collect V8 coverage data during tests and export to lcov for CI integration.

```sh
# Collect coverage
deno test --coverage=cov/

# View summary in terminal
deno coverage cov/

# Export to lcov (for Codecov, Coveralls, etc.)
deno coverage cov/ --lcov --output=coverage.lcov
```

**Rationale**: Coverage measures which code paths were exercised by tests — statement, branch, function, and line metrics. Export to lcov for integration with CI reporting tools. Coverage only measures execution, not assertion quality — 100% coverage does not mean zero bugs (Deno test runner docs; JS Definitive Guide, §17.3).

---

## ID-22: Testing HTTP Handlers — Construct `Request`, Assert `Response`

**Strength**: SHOULD

**Summary**: Deno's `Deno.serve()` handlers accept `Request` and return `Response` — standard Fetch API types that are directly testable.

```js
import { assertEquals } from "@std/assert";

// The handler (exported for testing)
export function handler(req) {
  const url = new URL(req.url);
  if (url.pathname === "/api/health") {
    return new Response(JSON.stringify({ status: "ok" }), {
      status: 200,
      headers: { "content-type": "application/json" },
    });
  }
  return new Response("Not Found", { status: 404 });
}

// The test — no server startup needed
Deno.test("GET /api/health returns 200 with status ok", async () => {
  const req = new Request("http://localhost/api/health");
  const res = handler(req);
  assertEquals(res.status, 200);
  const body = await res.json();
  assertEquals(body.status, "ok");
});

Deno.test("unknown route returns 404", async () => {
  const req = new Request("http://localhost/unknown");
  const res = handler(req);
  assertEquals(res.status, 404);
});
```

**Rationale**: Because `Deno.serve()` handlers use standard Web API types, they can be unit-tested by constructing `Request` objects directly — no HTTP server startup, no port allocation, no `fetch()` in tests. This is faster and more isolated than integration testing with a running server (Deno HTTP server docs).

**See also**: `12-deno/01-runtime-basics.md` ID-06

---

## ID-23: Isolating File System Tests — `Deno.makeTempDir()`

**Strength**: SHOULD

**Summary**: Use temporary directories to prevent file system tests from interfering with each other or with project files.

```js
Deno.test("writeConfig creates valid JSON", async () => {
  const dir = await Deno.makeTempDir();
  try {
    const path = `${dir}/config.json`;
    await writeConfig(path, { port: 8080, debug: true });

    const content = JSON.parse(await Deno.readTextFile(path));
    assertEquals(content.port, 8080);
    assertEquals(content.debug, true);
  } finally {
    await Deno.remove(dir, { recursive: true });
  }
});
```

**Rationale**: `Deno.makeTempDir()` creates a unique directory that won't collide with other tests or project files. Always clean up in `finally` — the resource sanitizer doesn't clean temp directories, but they accumulate on disk. Requires `--allow-read` and `--allow-write` (Deno namespace API docs).

---

## ID-24: Testing with Environment Variables

**Strength**: SHOULD

**Summary**: Set and restore environment variables in tests using `Deno.env.set()` with cleanup.

```js
Deno.test("reads PORT from environment", () => {
  const original = Deno.env.get("PORT");
  try {
    Deno.env.set("PORT", "9090");
    const config = loadConfig();
    assertEquals(config.port, 9090);
  } finally {
    if (original !== undefined) {
      Deno.env.set("PORT", original);
    } else {
      Deno.env.delete("PORT");
    }
  }
});
```

**Rationale**: Environment variable tests must restore the original state — a leaked env var can affect subsequent tests. The `try/finally` pattern ensures cleanup. Requires `--allow-env` (Deno namespace API docs).

---

## Best Practices Summary

### Quick Reference Table

| ID | Pattern | Strength | Key Insight |
|----|---------|----------|-------------|
| 01 | `Deno.test()` — built-in runner | MUST | No framework needed; auto-discovery |
| 02 | Options object form | SHOULD | Permissions, ignore, only, sanitizers |
| 03 | Test permissions restrict, not grant | SHOULD | Most confused Deno testing behavior |
| 04 | Async tests — `await` everything | MUST | `assertRejects` for async failures |
| 05 | Sanitizers catch leaks | SHOULD | Resources, async ops, exit — all on by default |
| 06 | `assertEquals` for deep equality | MUST | Recursive structural comparison |
| 07 | `assertStrictEquals` for identity | SHOULD | `===` comparison; references, not content |
| 08 | `assertThrows` / `assertRejects` | MUST | Cleaner than manual try/catch |
| 09 | Targeted assertions | SHOULD | `assertObjectMatch`, `assertMatch`, subsets |
| 10 | `unreachable()` / `fail()` | SHOULD | Dead code paths and manual failures |
| 11 | Custom assertion messages | SHOULD | Essential in loops and parameterized tests |
| 12 | `t.step()` for subtests | SHOULD | Named phases within a test |
| 13 | BDD `describe`/`it` | CONSIDER | Wrapper over `Deno.test()`; team preference |
| 14 | `--filter`, `--parallel`, `--fail-fast` | SHOULD | Surgical selection; faster CI |
| 15 | Setup/teardown — explicit, no magic | SHOULD | Helper functions or `t.step()` |
| 16 | `spy()` — observe calls | SHOULD | Record without altering behavior |
| 17 | `stub()` — replace behavior | SHOULD | Isolation; `returnsNext()` for sequences |
| 18 | Always restore stubs | MUST | `try/finally` or `using` declaration |
| 19 | Snapshot testing | CONSIDER | Golden-file comparison; `deno test --update` |
| 20 | `deno test --doc` | SHOULD | JSDoc examples as executable tests |
| 21 | `deno test --coverage` | SHOULD | lcov export for CI integration |
| 22 | HTTP handler testing | SHOULD | Construct Request, assert Response — no server |
| 23 | `Deno.makeTempDir()` for isolation | SHOULD | Clean up in `finally` |
| 24 | Env var tests with cleanup | SHOULD | Restore original values in `finally` |

### Jest → Deno Translation

| Jest | Deno |
|------|------|
| `test("name", fn)` | `Deno.test("name", fn)` |
| `describe("name", fn)` | `describe("name", fn)` from `@std/testing/bdd` |
| `it("name", fn)` | `it("name", fn)` from `@std/testing/bdd` |
| `expect(x).toBe(y)` | `assertStrictEquals(x, y)` |
| `expect(x).toEqual(y)` | `assertEquals(x, y)` |
| `expect(fn).toThrow()` | `assertThrows(fn)` |
| `jest.fn()` | `spy()` from `@std/testing/mock` |
| `jest.spyOn(obj, method)` | `stub(obj, method)` from `@std/testing/mock` |
| `toHaveBeenCalledTimes(n)` | `assertSpyCalls(spy, n)` |
| `toHaveBeenCalledWith(...)` | `assertSpyCallArgs(spy, 0, [...])` |
| `mockResolvedValue(x)` | `returnsNext([Promise.resolve(x)])` |
| `--coverage` | `deno test --coverage` + `deno coverage --lcov` |

---

## Related Guidelines

- **Error Handling**: See `03-error-handling.md` for custom error types (ID-05), `assertThrows` patterns (ID-08), fire-and-forget (ID-20)
- **Type Discipline**: See `05-type-discipline.md` for JSDoc annotations on test helpers (ID-16–17)
- **Async & Concurrency**: See `07-async-concurrency.md` for async patterns in tests (ID-13, ID-21), `assertRejects` (ID-04 here)
- **Performance**: See `08-performance.md` for `Deno.bench()` (ID-02) — benchmarks are separate from tests
- **Anti-Patterns**: See `09-anti-patterns.md` for fire-and-forget (ID-20), sequential await (ID-18)
- **Project Structure**: See `10-project-structure.md` for test file naming (ID-07), co-location (ID-20), test utilities (ID-21)
- **Documentation**: See `11-documentation.md` for test naming as docs (ID-18), `deno test --doc` prose (ID-10)
- **Runtime Basics**: See `12-deno/01-runtime-basics.md` for permissions (ID-01–04), `Deno.serve()` (ID-06), `@std/*` (ID-25)

---

## External References

- [Deno — Testing](https://docs.deno.com/runtime/fundamentals/testing/)
- [Deno — @std/assert](https://jsr.io/@std/assert)
- [Deno — @std/testing](https://jsr.io/@std/testing)
- [Deno — Code Coverage](https://docs.deno.com/runtime/fundamentals/testing/#test-coverage)
- *Exploring JavaScript* (ES2025) — Axel Rauschmayer
- *Eloquent JavaScript* (4th ed.) — Marijn Haverbeke
