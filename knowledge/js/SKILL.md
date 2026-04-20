---
name: javascript-deno-guidelines
description: |
  JavaScript and Deno best practices, idioms, and anti-patterns for this project.
  Use when: writing new JS code, refactoring existing JS, reviewing JS for issues,
  designing module APIs, handling errors, writing Deno tests, configuring deno.json
  tasks, preparing modules for JSR publishing, converting Node-style or TypeScript-style
  code to project idioms, doing code quality audits, performance reviews, improving
  documentation, making dependency decisions, configuring Biome lint/format, enforcing
  the no-Node boundary, or answering JS design questions.
---

# JavaScript Skill — Project Style Reference

This project writes **plain JavaScript** (no TypeScript) targeting **Deno** with **ESM-only** modules, **Biome** for linting/formatting, and **JSDoc** for type annotations. Every rule below is derived from the project's style guides (01–14). When writing or reviewing JS for this project, follow these conventions.

**Strength indicators** used throughout:

| Indicator | Meaning | Action |
|-----------|---------|--------|
| **MUST** | Required for correctness/compatibility | Always follow |
| **SHOULD** | Strong project convention | Follow unless specific reason not to |
| **CONSIDER** | Context-dependent | Evaluate for situation |
| **AVOID** | Anti-pattern | Do not use |

---

## Document Selection Guide

The inline content below is enough to write correct code. Load the full guide files when you need deeper rationale, edge cases, or comprehensive examples.

Note: document paths in this skill are relative to the project root. (The project root directory is `ai-design` and this `SKILL.md` file is in `ai-design/skills/nodeless-js`, with the guides it points to being in `ai-design/guides/js`.)

| Task | Load These Documents |
|------|---------------------|
| **Any JS code** | `guides/js/09-anti-patterns.md` (always load first) |
| **New module from scratch** | `guides/js/01-core-idioms.md`, `guides/js/10-project-structure.md`, `guides/js/02-api-design.md` |
| **Implementing a new feature** | `guides/js/01-core-idioms.md`, `guides/js/06-functions-closures.md`, `guides/js/09-anti-patterns.md` |
| **API design** | `guides/js/02-api-design.md`, `guides/js/06-functions-closures.md`, `guides/js/05-type-discipline.md` |
| **Error handling** | `guides/js/03-error-handling.md`, `guides/js/07-async-concurrency.md` |
| **Refactoring** | `guides/js/09-anti-patterns.md`, `guides/js/01-core-idioms.md`, `guides/js/04-values-references.md` |
| **Code review / quality audit** | `guides/js/09-anti-patterns.md`, `guides/js/01-core-idioms.md`, `guides/js/08-performance.md` |
| **Writing or improving tests** | `guides/js/12-deno/12-02-testing.md`, `guides/js/03-error-handling.md` |
| **Debugging failing tests** | `guides/js/12-deno/12-02-testing.md`, `guides/js/03-error-handling.md`, `guides/js/07-async-concurrency.md` |
| **Performance review** | `guides/js/08-performance.md`, `guides/js/07-async-concurrency.md` |
| **Documentation** | `guides/js/11-documentation.md`, `guides/js/05-type-discipline.md` |
| **Dependency decisions** | `guides/js/10-project-structure.md`, `guides/js/12-deno/12-01-runtime-basics.md` |
| **Task runner / deno.json** | `guides/js/12-deno/12-03-task-runner.md` |
| **Publishing to JSR** | `guides/js/12-deno/12-04-publishing.md`, `guides/js/11-documentation.md`, `guides/js/05-type-discipline.md` |
| **Converting Node/TS code** | `guides/js/12-deno/12-01-runtime-basics.md`, `guides/js/01-core-idioms.md`, `guides/js/14-no-node-boundary.md` |
| **Enforcing the no-Node boundary** | `guides/js/14-no-node-boundary.md`, `guides/js/12-deno/12-01-runtime-basics.md` |
| **Async & concurrency** | `guides/js/07-async-concurrency.md`, `guides/js/03-error-handling.md` |
| **Values, mutation, copying** | `guides/js/04-values-references.md`, `guides/js/01-core-idioms.md` |
| **Type discipline / JSDoc** | `guides/js/05-type-discipline.md`, `guides/js/11-documentation.md` |
| **Biome lint/format** | `guides/js/13-biome/13-01-setup.md`, `guides/js/13-biome/13-02-lint-rules.md`, `guides/js/13-biome/13-03-formatting.md` |

---

## Workflows

### Writing New Code

1. **Load anti-patterns first**: Read `guides/js/09-anti-patterns.md` — know what to avoid before writing a line
2. **Load core idioms**: Read `guides/js/01-core-idioms.md` for declarations, naming, control flow
3. **Load topic-specific docs**: Based on what you're building (API design, async, etc.)
4. **Structure the module**: `mod.js` entry point, flat-by-feature layout, named exports only
5. **Write code**: Guard clauses at boundaries, `async`/`await`, `Error.cause`, JSDoc on exports
6. **Self-review**: Check against anti-patterns table before finishing

### Refactoring

1. **Load anti-patterns**: Identify which anti-patterns exist in the current code
2. **Load core idioms + values/references**: Understand mutation risks
3. **Extract and rename**: Descriptive names, single-responsibility functions, no weasel names
4. **Verify tests pass**: Run `deno test --allow-all` after each change
5. **Check for regressions**: Same return types, same error behavior, no new side effects

### Code Review / Quality Audit

1. **Scan for anti-patterns**: Check every item in the anti-patterns table
2. **Check error handling**: No empty catches, `Error.cause` used, rejections handled
3. **Check API surfaces**: Consistent return types, options objects for 3+ params, JSDoc complete
4. **Check async discipline**: No fire-and-forget, `Promise.all()` for parallel ops, `AbortSignal` on fetch
5. **Check mutation**: No argument mutation, defensive copies at boundaries

### Adding Tests

1. **Load testing guide**: `12-deno/12-02-testing.md`
2. **Use `Deno.test()`**: Descriptive names, `assertEquals`/`assertThrows`/`assertRejects`
3. **Structure with subtests**: `t.step()` for lifecycle scenarios
4. **Test error paths**: Verify error types, messages, and `.cause` chains
5. **Run with sanitizers**: Default sanitizers catch leaked resources and un-awaited ops
6. **Check coverage**: `deno test --coverage=cov/` then `deno coverage --lcov cov/`

### Preparing for Publish

1. **Validate `deno.json`**: `name`, `version`, `exports`, `license`, `exclude` all set
2. **Complete JSDoc**: All exports must have full type annotations (JSR "slow types" rule)
3. **Run full pipeline**: `biome ci && deno check && deno test --doc && deno publish --dry-run`
4. **Version correctly**: `0.x.y` for unstable APIs, semver for stable
5. **Publish**: `deno publish` — versions are immutable once published

---

## Environment & Module System

- **Runtime**: Deno (not Node.js). No `require()`, no `module.exports`, no `node_modules`, no `package.json`. **MUST**
- **Modules**: ESM exclusively. File extensions are **required** on all local imports. **MUST**
- **Config**: `deno.json` is the single config source (imports, tasks, compilerOptions). Biome handles lint/format via `biome.json`.
- **Type checking**: JSDoc annotations checked by `deno check`. Enable `"checkJs": true` in `deno.json`. **SHOULD**
- **Registry**: Prefer `jsr:` specifiers over `npm:`. Use import maps in `deno.json` for bare specifiers. **SHOULD**

```js
// Correct module style
import { join } from "@std/path";
import { login } from "./auth/mod.js"; // extension required

export function greet(name) { return `Hello, ${name}`; }
```

---

## Declarations & Naming

- `const` by default, `let` when reassignment is needed, **never `var`**. **MUST**
- `===` and `!==` always. The one exception: `x == null` to test both `null` and `undefined`. **MUST**
- `??` for defaults (not `||` — it swallows `0`, `""`, `false`). **MUST**
- `?.` for safe property access. **SHOULD**

```js
const timeout = options.timeout ?? 5000; // 0 is preserved
const street = user?.address?.street ?? "(unknown)";
```

**Naming conventions**:

| Element | Convention | Example |
|---------|-----------|---------|
| Variables, functions | camelCase | `getUserName` |
| Classes, constructors | PascalCase | `HttpClient` |
| Module-level constants | UPPER_CASE | `MAX_RETRIES` |
| Filenames | kebab-case | `http-client.js` |
| Test files | `*_test.js` | `login_test.js` |

**AVOID** weasel names: `Manager`, `Service`, `Handler`, `Utils`, `Data`, `process`, `handle`.

---

## Functions

- **`function` declarations** for named, module-level, exported functions (hoisted, named in stack traces). **SHOULD**
- **Arrow functions** for callbacks and inline closures (inherits `this`). **SHOULD**
- **Never use `function` as a callback** inside methods — arrow inherits `this`, plain `function` loses it. **MUST**
- **Method shorthand** in objects and classes: `{ method() {} }`, not `{ method: function() {} }`. **SHOULD**
- Use **rest parameters** (`...args`), never `arguments`. **MUST**

```js
// Module-level: function declaration
export function parseConfig(raw) {
  const lines = raw.split("\n");
  return Object.fromEntries(lines.map(parseLine));
}

// Callback: arrow
const doubled = items.map((x) => x * 2);
```

**Options pattern** (**SHOULD**): Use destructured options objects for 3+ parameters. Positional args for required, options for optional.

```js
function createServer({ port = 8080, host = "localhost", tls = false } = {}) {
  return { port, host, tls };
}
```

---

## Error Handling

- **Throw only `Error` instances** (never strings, numbers, or plain objects). **MUST**
- **`throw` for exceptional conditions**, not expected outcomes. Return `undefined`/`null` for "not found". **MUST**
- **Include context** in messages: what failed, why, the offending value. **MUST**
- **Use `Error.cause`** when rethrowing to preserve the chain. **SHOULD**
- **Never write empty `catch` blocks**. Catch specific errors with `instanceof`, rethrow unknown ones. **MUST**
- **`return await` inside `try`/`catch`** — without `await`, rejection escapes the local `catch`. **MUST**
- **Always handle Promise rejections** — unawaited async calls need `.catch()`. **MUST**

```js
// Error chaining
try {
  const raw = await Deno.readTextFile(path);
  return JSON.parse(raw);
} catch (err) {
  throw new Error(`Failed to load config from ${path}`, { cause: err });
}

// Custom error with name
class HttpError extends Error {
  constructor(status, statusText, url) {
    super(`${status} ${statusText}: ${url}`);
    this.status = status;
  }
  get name() { return "HttpError"; }
}
```

**Validate at boundaries, trust within** (**SHOULD**): guard clauses at public function entry points, not deep inside internals. Fail fast with typed errors.

```js
export function fetchUser(id) {
  if (id == null) throw new TypeError("id is required");
  if (typeof id !== "string") throw new TypeError(`id must be a string, got ${typeof id}`);
  // ...
}
```

---

## Values, References & Mutation

- **Don't mutate function arguments.** Copy first if you need to modify. **MUST**
- **`const` does not mean immutable** — it freezes the binding, not the value. Use `Object.freeze()` for true constant objects. **SHOULD**
- **Spread for shallow copies**: `{...obj}`, `[...arr]`. Nested objects are still shared.
- **`structuredClone()` for deep copies** (not `JSON.parse(JSON.stringify())`). **SHOULD**
- **Non-destructive array methods** (ES2023): `.toSorted()`, `.toReversed()`, `.toSpliced()`, `.with()`. **SHOULD**
- **Defensive copying at module boundaries**: copy incoming params and outgoing return values when mutation risk exists. **SHOULD**

```js
// Non-destructive update
const updated = { ...config, timeout: 5000 };
const sorted = original.toSorted((a, b) => a - b);
```

---

## Type Discipline (JSDoc, No TypeScript)

- **`typeof` for primitives**, `instanceof` for class hierarchies, `Array.isArray()` for arrays. **MUST**
- **`Number.isNaN()`**, `Number.isFinite()`, `Number.isInteger()` — never the global versions. **MUST**
- **Explicit conversion**: `Number()`, `String()`, `Boolean()` without `new`. Never `+x` or `"" + x`. **SHOULD**
- **JSDoc on every exported function**: `@param`, `@returns`, `@throws`. **MUST**
- **`@typedef`** for shared object shapes, `@template` for generics, `@enum` with `Object.freeze()` for constant sets. **SHOULD**
- **`undefined`** = system-level absence; **`null`** = programmer-intentional absence. **SHOULD**

```js
/**
 * Parse a port number from a string.
 * @param {string} input
 * @returns {number}
 * @throws {RangeError} If port is out of range.
 */
export function parsePort(input) {
  const port = Number(input);
  if (!Number.isFinite(port) || port < 0 || port > 65535) {
    throw new RangeError(`Invalid port: ${input}`);
  }
  return port;
}
```

---

## Async & Concurrency

- **`async`/`await` over `.then().catch()`**. Linear flow, unified error handling. **SHOULD**
- **Never block the event loop**: use async APIs (`Deno.readTextFile`, `fetch`), not sync variants. **MUST**
- **`Promise.all()` for parallel independent ops**. Sequential `await` on independent calls is a performance anti-pattern. **SHOULD**
- **`Promise.allSettled()`** when partial failure is acceptable. **CONSIDER**
- **`.map(async fn)` returns `Promise[]`** — always wrap with `Promise.all()`. **MUST**
- **`AbortController`/`AbortSignal`** for cancellation. Every `fetch()` in production should accept a `signal`. **SHOULD**
- **`for await...of`** for consuming async iterables and streams. **SHOULD**
- **Concurrency limiting**: use a worker-pool pattern when processing many items to avoid exhausting resources. **CONSIDER**

```js
// Parallel
const [users, posts] = await Promise.all([fetchUsers(), fetchPosts()]);

// Cancellable fetch
async function fetchData(url, { signal } = {}) {
  const response = await fetch(url, { signal });
  if (!response.ok) throw new HttpError(response.status, response.statusText, url);
  return response.json();
}
```

---

## Classes & API Design

- **Named exports**, not default exports. Export at the declaration site. **MUST**
- **One module, one responsibility**. No `utils.js` kitchen sinks. **SHOULD**
- **No module-level side effects**. Keep computation pure at the top level. **MUST**
- **Factory functions** for simple data objects. Classes when you need `instanceof`, shared prototypes, or `#private` fields. **SHOULD**
- **`#private` fields** for encapsulation (not `_convention`). **SHOULD**
- **Static factory methods** for alternative construction: `Point.fromPolar()`, `DataStore.create()`. **CONSIDER**
- **Async initialization** via static async factory, never an async constructor. **MUST**
- **Return consistent types**: every code path returns the same type. Never mix return types. **MUST**
- **Boolean methods**: `isX()`, `hasX()`, `canX()`, `shouldX()`. Verbs for methods, nouns for properties. **SHOULD**
- **Discriminated unions**: use a `kind`/`type` property + `switch` with a throwing `default` for exhaustive handling. **CONSIDER**

```js
class Buffer {
  #data = [];
  push(item) { this.#data.push(item); }
  get size() { return this.#data.length; }
}
```

---

## Anti-Patterns to AVOID

These are the most common mistakes, especially in AI-generated code. Memorize these.

| Anti-Pattern | Fix |
|---|---|
| `==` instead of `===` | Always `===` (except `== null`) |
| `\|\|` for defaults when `0`/`""`/`false` valid | Use `??` |
| `var` anywhere | `const` or `let` |
| `for...in` on arrays | `for...of` or array methods |
| Sequential `await` on independent ops | `Promise.all()` |
| `.map(async fn)` without `Promise.all()` | `await Promise.all(items.map(...))` |
| Fire-and-forget async (no `await`, no `.catch()`) | `await` it or attach `.catch()` |
| Empty `catch {}` | Log, handle, or rethrow |
| `return` without `await` in `try/catch` | `return await` inside `try` |
| `.sort()` without comparator on numbers | `(a, b) => a - b` or `.toSorted()` |
| Mutating function arguments | Defensive copy at entry |
| `const` assumed immutable | `Object.freeze()` for true immutability |
| Shallow copy surprise (`{...obj}` shares nested refs) | `structuredClone()` for deep copy |
| `typeof null === "object"` trusted | `value === null` for null checks |
| `isNaN()` global | `Number.isNaN()` |
| `new Boolean(false)` is truthy | `Boolean()` without `new` |
| Method extraction loses `this` | `.bind()` or arrow wrapper |
| Regular `function` as callback in methods | Arrow function |
| Arrow function as object method | Method shorthand |
| `parseInt` without radix | `parseInt(s, 10)` |
| Mixed error channels (return null AND throw) | Pick one: throw for errors, return for absence |
| Boolean positional params | Options object with named props |
| `CommonJS` / `require()` | ESM `import`/`export` |
| `eval()` / `new Function()` | Specific alternatives (`obj[key]`, `JSON.parse()`) |
| `fetch()` without `signal` | Pass `AbortSignal` for cancellation |
| Line-by-line narration comments | Comments explain *why*, not *what* |
| Commented-out code | Delete it; that is what git is for |

---

## Performance

- **Measure first, optimize second.** Write clear code, profile with real data, optimize only the bottleneck. **MUST**
- **`Deno.bench()`** for microbenchmarks. `performance.now()` for timing critical sections.
- **`Map` over plain objects** for dynamic key collections. **`Set` over arrays** for membership testing. **SHOULD**
- **`WeakMap`** for object-keyed caches that should not prevent GC. **CONSIDER**
- **Generators** for lazy sequences (avoid materializing large intermediate arrays). **CONSIDER**
- **Short-circuiting methods**: `.find()`, `.some()`, `.every()` over `.filter()[0]`. **SHOULD**
- **Consistent object shapes**: initialize all properties in the same order. **AVOID** `delete` (use `undefined` or destructure-out).
- **`for-of`** when you need `break`/`return`; `.map()`/`.filter()` when expressing transformations. Don't micro-optimize without evidence.

---

## Documentation

- **Comments explain *why*, not *what*.** If code needs narration, refactor it. **MUST**
- **Do not narrate every line** (the most common AI anti-pattern). Ask: "does this tell me something the code doesn't?" **MUST**
- **JSDoc `/** */`** on every exported function: concise summary (first sentence < 15 words), `@param` with constraints, `@returns` with semantics, `@throws` with conditions. **MUST**
- **`@module`** JSDoc block at top of each file. **SHOULD**
- **`@example`** with fenced code blocks for non-obvious APIs. `deno test --doc` runs these as tests. **SHOULD**
- **Self-documenting code**: descriptive names, named constants, extracted predicates. **SHOULD**
- **TODO/FIXME** with owner, ticket number, and context. Never bare `// TODO: fix`. **MUST**
- **Delete stale comments and commented-out code.** **MUST**

---

## Project Structure

```
project/
├── deno.json          # imports, tasks, compilerOptions
├── deno.lock          # commit to VCS
├── biome.json         # lint/format config
├── mod.js             # library entry point
├── main.js            # application entry point
├── auth/
│   ├── mod.js         # selective re-exports (barrel)
│   ├── login.js
│   ├── session.js
│   └── auth_test.js
├── shared/
│   ├── http.js
│   ├── constants.js
│   └── types.js       # shared @typedef definitions
└── testing/
    └── helpers.js     # test utilities (not in shared/)
```

**Key rules**:
- **Flat-by-feature**, not nested-by-type. No `controllers/`, `models/`, `services/` directories. **MUST**
- **`mod.js`** for library entry points (Deno convention, not `index.js`). **`main.js`** for applications. **MUST**
- **`*_test.js`** for test files (Deno auto-discovery). **MUST**
- **Selective re-exports** in barrel files. No wildcard `export *`. **SHOULD**
- **Import from `mod.js`**, not internal files (for external consumers). **SHOULD**
- **Dependency direction**: features depend inward on `shared/`, never outward. No circular imports. **MUST**
- **Import maps** for aliases and centralized version management: `"@shared/": "./shared/"`. **SHOULD**
- **Environment variables** for runtime config, not conditional imports. **SHOULD**
- **Separate pure logic from I/O**. Push side effects to the edges. **SHOULD**

---

## Deno Runtime

### Permissions

- **Secure by default**: no access without explicit permission flags. **MUST**
- **Granular permissions**: `--allow-net=host:port`, `--allow-read=./data`, `--allow-env=PORT,DB_URL`. **SHOULD**
- **`-A` / `--allow-all` for development only**, never production. **MUST**
- **Deny flags override allow**: `--allow-net --deny-net=evil.com`.

### Key APIs

```js
// File I/O (async, requires --allow-read/--allow-write)
const text = await Deno.readTextFile("./config.json");
await Deno.writeTextFile("./out.json", JSON.stringify(data, null, 2));

// HTTP server (standard Request/Response)
Deno.serve({ port: 8080 }, (req) => {
  return new Response("Hello", { status: 200 });
});

// Environment variables (requires --allow-env)
const port = Number(Deno.env.get("PORT") ?? "8080");

// Entry-point detection
if (import.meta.main) { main(); }

// Subprocesses (requires --allow-run)
const cmd = new Deno.Command("git", { args: ["status"] });
const { stdout } = await cmd.output();
```

### Web Platform APIs (globally available, no imports)

`fetch`, `Request`, `Response`, `URL`, `URLSearchParams`, `AbortController`, `AbortSignal`, `TextEncoder`, `TextDecoder`, `crypto.subtle`, `structuredClone`, `ReadableStream`, `WritableStream`, `performance.now()`, `setTimeout`, `queueMicrotask`, `WebSocket`, `BroadcastChannel`.

### Module Resolution

- File extensions required on local imports. **MUST**
- `jsr:` and `npm:` specifiers resolve on import (no install step).
- `node:` specifiers available for compat, but prefer Deno/Web APIs. **SHOULD**
- `import.meta.main` replaces `require.main === module`.
- `import.meta.dirname` / `import.meta.filename` replace `__dirname` / `__filename`.

---

## Testing (Deno Built-In)

```js
import { assertEquals, assertThrows, assertRejects } from "@std/assert";

Deno.test("parsePort returns number", () => {
  assertEquals(parsePort("8080"), 8080);
});

Deno.test("parsePort rejects invalid", () => {
  assertThrows(() => parsePort("abc"), RangeError, "Invalid port");
});

Deno.test("async fetch works", async () => {
  const data = await fetchData("/api");
  assertEquals(data.status, "ok");
});

// Subtests
Deno.test("user lifecycle", async (t) => {
  await t.step("create", async () => { /* ... */ });
  await t.step("read", async () => { /* ... */ });
  await t.step("delete", async () => { /* ... */ });
});
```

**Key patterns**:
- `assertEquals` for deep structural equality. `assertStrictEquals` for `===` identity. **MUST**
- `assertThrows` (sync) and `assertRejects` (async, must `await`) for error testing. **MUST**
- `assertObjectMatch` for partial matching. **CONSIDER**
- **Sanitizers** (on by default): catch leaked resources, un-awaited ops, premature exits.
- **Per-test permissions** restrict (never grant): `{ permissions: { read: false } }`. **CONSIDER**
- **Stubs** via `@std/testing/mock`: always restore in `try/finally`. **MUST**
- **`deno test --doc`**: runs fenced code blocks in JSDoc as tests.
- **`deno test --coverage=cov/`**: V8 coverage, export with `deno coverage --lcov`.
- **HTTP handler testing**: construct `Request`, assert `Response` directly (no server startup). **SHOULD**
- **Temp dirs**: `Deno.makeTempDir()`, clean up in `finally`. **MUST**

**Test naming**: descriptive behavior, not "test1" or "it works". Test names are executable specifications. **MUST**

---

## Task Runner (`deno.json`)

```jsonc
{
  "tasks": {
    "dev": "deno run --watch --allow-net --allow-read main.js",
    "test": "deno test --allow-all",
    "test:watch": "deno test --allow-all --watch",
    "check": "biome ci && deno check **/*.js && deno test --allow-all",
    "lint": "biome check ./",
    "fmt": "biome format --write ./",
    "ci": "biome ci && deno check **/*.js && deno test --allow-all --parallel --coverage=cov/"
  }
}
```

- **`deno task <name>`** replaces `npm run`. Cross-platform built-in shell.
- **`&&`** for sequential stop-on-error. **`&`** for parallel. **`;`** for always-continue.
- **`--watch`** for live reload. **`--watch-exclude='*.log,tmp/'`** to prevent restart loops.
- **`deno run` flag ordering**: permission flags BEFORE the script name. **MUST**
- **`deno check`**: type-check without executing (CI gate).
- **`deno compile`**: standalone binary with embedded permissions.

---

## Publishing to JSR

Required `deno.json` fields:
```jsonc
{
  "name": "@scope/package",
  "version": "1.0.0",
  "exports": "./mod.js",
  "license": "MIT",
  "exclude": ["**/*_test.js", "testing/"]
}
```

- `exports` enforces the public API boundary. Internal files cannot be imported by consumers. **MUST**
- JSR requires **complete JSDoc type information** on all exports ("slow types" rule). **MUST**
- `deno publish --dry-run` validates without uploading. Published versions are **immutable**.
- `0.x.y` for unstable APIs (breaking changes allowed at minor bumps). **SHOULD**
- Pre-publish pipeline: `biome ci && deno check && deno test --doc && deno publish --dry-run`. **MUST**

---

## Biome (Linting & Formatting)

Biome replaces ESLint + Prettier with a single Rust-based binary — one tool, one config file, one pass.

### Setup & Config

- **Install standalone** (no npm required): `brew install biome` or the install script. **MUST**
- **`biome.json`** at project root is the single config file. Use `biome init` to scaffold. **MUST**
- **Omit `lint` and `fmt` from `deno.json`** when using Biome — avoids conflicts. **MUST**
- **Division of labor**: Biome handles lint/format. Deno handles type checking (`deno check`), testing (`deno test`), and running. **SHOULD**
- **VS Code**: Install `biomejs.biome` extension, set `"deno.lint": false`, set Biome as default formatter with format-on-save. **SHOULD**
- **VCS integration**: Enable `vcs.enabled`, `vcs.useIgnoreFile`, `vcs.clientKind: "git"` in `biome.json`. **SHOULD**

```jsonc
// biome.json — recommended starter
{
  "$schema": "https://biomejs.dev/schemas/2.0.0/schema.json",
  "vcs": { "enabled": true, "clientKind": "git", "useIgnoreFile": true, "defaultBranch": "main" },
  "formatter": { "indentStyle": "space", "indentWidth": 2, "lineWidth": 100 },
  "javascript": {
    "formatter": { "quoteStyle": "double", "semicolons": "always", "trailingCommas": "all" }
  },
  "linter": { "enabled": true, "rules": { "recommended": true } }
}
```

### CLI Commands

| Command | Purpose |
|---------|---------|
| `biome check` | Lint + format check (report only) |
| `biome check --write` | Lint fix + format (modify files) |
| `biome check --staged` | Check staged files only (pre-commit) |
| `biome check --changed` | Check files changed from default branch |
| `biome ci` | CI mode — errors on all violations, never modifies files |
| `biome format --write` | Format only |
| `biome lint --write` | Lint + safe fixes only |

### Lint Rules

- **`recommended` rules on by default** — stable, sensible baseline across all groups. **MUST**
- **Rule groups**: `correctness` (error), `suspicious` (error), `style` (warn), `complexity` (warn), `performance` (error), `security` (error), `a11y` (error). **SHOULD**
- **Key rules**: `noDoubleEquals` (MUST), `noVar` (MUST), `useConst` (SHOULD), `noUnusedVariables`/`noUnusedImports` (SHOULD).
- **Severity**: `"error"` blocks CI, `"warn"` is advisory, `"off"` disables. **SHOULD**
- **`types` domain**: Enable for type-aware rules (`noFloatingPromises`, `useAwaitThenable`). Requires JSDoc + `checkJs`. **SHOULD**
- **`project` domain**: Enable for cross-file analysis (`noImportCycles`, `noUndeclaredDependencies`). **CONSIDER**
- **Safe fixes** (`--write`): Never change semantics — auto-apply freely. **SHOULD**
- **Unsafe fixes** (`--write --unsafe`): May change semantics — review required. **SHOULD**
- **Suppression**: `// biome-ignore lint/group/rule: reason` — reason is mandatory. **MUST**

### Formatting

- **Opinionated formatter** — minimal options by design. Configure once, never discuss formatting in review.
- **Project settings**: spaces, indent 2, line width 100, double quotes, always semicolons, trailing commas all.
- **JS-specific options** go under `javascript.formatter`, not top-level `formatter`. **MUST**
- **97%+ Prettier compatible** — migration produces minimal diffs.
- **Format suppression**: `// biome-ignore format: reason` — for alignment tables, matrix data, generated code. **SHOULD**

### Integration with `deno task`

```jsonc
{
  "tasks": {
    "lint": "biome check",
    "lint:fix": "biome check --write",
    "fmt": "biome format --write",
    "check": "biome ci && deno check **/*.js && deno test --allow-all",
    "ci": "biome ci && deno check **/*.js && deno test --allow-all --parallel"
  }
}
```

---

## No-Node Boundary

This project avoids Node.js patterns entirely. Every Node.js API has a Deno or Web Platform replacement. When encountering Node.js code (or about to emit it), consult this boundary.

### MUST-AVOID (Hard Boundary)

| Node.js Pattern | Deno Replacement |
|----------------|-----------------|
| `require()` | ESM `import` with explicit `.js` extension |
| `module.exports` / `exports` | ESM `export` |
| Extensionless imports | Explicit `.js` extension on all local imports |
| `package.json` | `deno.json` (imports, tasks, compilerOptions) |
| `node_modules` | Global cache via `jsr:` and `npm:` specifiers |
| `npm install` / `npm run` | `deno add` / `deno task` |
| `.eslintrc` / `.prettierrc` | `biome.json` |
| `tsconfig.json` | `compilerOptions` in `deno.json` |
| Error-first callbacks `(err, result)` | `async`/`await` |
| Jest / Mocha / Vitest | `Deno.test()` + `@std/assert` |
| ESLint / Prettier | Biome |

### SHOULD-AVOID (Prefer Deno/Web APIs)

| Node.js Pattern | Deno Replacement |
|----------------|-----------------|
| `process.env.X` | `Deno.env.get("X")` |
| `process.argv.slice(2)` | `Deno.args` |
| `__dirname` / `__filename` | `import.meta.dirname` / `import.meta.filename` |
| `Buffer` | `Uint8Array` + `TextEncoder`/`TextDecoder` |
| `fs.readFile` / `fs.writeFile` | `Deno.readTextFile` / `Deno.writeTextFile` |
| `http.createServer` | `Deno.serve()` |
| `child_process.exec` | `Deno.Command` |
| Node streams (`Readable`/`Writable`) | Web Streams (`ReadableStream`/`WritableStream`) |
| `EventEmitter` | `EventTarget` + `CustomEvent` |
| `process.nextTick` | `queueMicrotask()` |
| `index.js` convention | `mod.js` |
| `npx tool` | `deno run npm:tool` |

### CONSIDER-AVOIDING (Acceptable Escape Hatches)

- **`npm:` specifiers**: Acceptable when no JSR equivalent exists. Prefer `jsr:` when available. **CONSIDER**
- **`node:` built-in specifiers**: Available for compat. Prefer Deno/Web APIs for new code. Acceptable inside npm dependencies. **CONSIDER**
- **`nodeModulesDir: "auto"`**: Last resort for frameworks (Vite, Next.js) or native addons that require local `node_modules`. **CONSIDER**

---

## Worked Examples

### Task: "Write a module that fetches and caches API responses"

1. **Load**: `guides/js/09-anti-patterns.md`, `guides/js/01-core-idioms.md`, `guides/js/07-async-concurrency.md`, `guides/js/03-error-handling.md`
2. **Apply**:
   - Named exports, `function` declarations for public API
   - `async`/`await` with `AbortSignal` on all `fetch()` calls
   - `Error.cause` when rethrowing network errors
   - `Map` for the cache (dynamic keys — not a plain object)
   - Guard clauses at entry: validate URL, check signal not aborted
   - JSDoc on all exports with `@param`, `@returns`, `@throws`
   - `export function fetchCached(url, { signal, ttl } = {})` — options pattern for optional params

### Task: "Design a config loader API"

1. **Load**: `guides/js/02-api-design.md`, `guides/js/06-functions-closures.md`, `guides/js/03-error-handling.md`, `guides/js/05-type-discipline.md`
2. **Apply**:
   - `loadConfig(path)` returns parsed config or throws with `Error.cause` wrapping `SyntaxError`/`Deno.errors.NotFound`
   - Return `undefined` (not throw) if config file is optional and absent
   - Custom `ConfigError extends Error` with `get name()` and context properties
   - `@typedef` for the config shape, `@param`/`@returns`/`@throws` on the function
   - Validate required fields at boundary, trust within

### Task: "Add tests for an HTTP handler"

1. **Load**: `guides/js/12-deno/12-02-testing.md`, `guides/js/03-error-handling.md`
2. **Apply**:
   - `Deno.test("handler returns 200 for valid request", async () => { ... })`
   - Construct `new Request("http://localhost/api/users")` directly — no server needed
   - Assert `Response` status, headers, and JSON body with `assertEquals`
   - Test error paths: `assertRejects` for async failures, check error type with `instanceof`
   - Subtests via `t.step()` for request lifecycle (create, read, update, delete)
   - Clean up temp state in `finally`

### Task: "Refactor a Node.js module to project idioms"

1. **Load**: `guides/js/12-deno/12-01-runtime-basics.md`, `guides/js/01-core-idioms.md`, `guides/js/09-anti-patterns.md`
2. **Apply**:
   - Replace `require()` → `import`, `module.exports` → `export`
   - Replace `__dirname` → `import.meta.dirname`, `process.env` → `Deno.env.get()`
   - Replace `fs.readFile` → `Deno.readTextFile`, `http.createServer` → `Deno.serve`
   - Replace `index.js` → `mod.js`, add file extensions to all local imports
   - Replace `package.json` scripts → `deno.json` tasks
   - Replace `||` defaults → `??`, `var` → `const`/`let`, `==` → `===`
   - Add JSDoc, remove TypeScript type annotations (convert to JSDoc `@param`/`@returns`)

### Task: "Set up a new Deno project from scratch"

1. **Load**: `guides/js/10-project-structure.md`, `guides/js/12-deno/12-03-task-runner.md`, `guides/js/01-core-idioms.md`
2. **Apply**:
   - Create `deno.json` with `imports`, `tasks` (dev, test, check, lint, fmt, ci), `compilerOptions`
   - Create `biome.json` for lint/format
   - Create `mod.js` (library) or `main.js` (application) entry point
   - Flat-by-feature directory structure, `*_test.js` co-located with source
   - `shared/` for cross-cutting concerns, `testing/` for test helpers
   - JSR import map entries: `"@std/assert": "jsr:@std/assert@^1"` etc.
   - `if (import.meta.main) { main(); }` guard in application entry point

### Task: "Set up Biome linting and formatting for an existing project"

1. **Load**: `guides/js/13-biome/13-01-setup.md`, `guides/js/13-biome/13-02-lint-rules.md`, `guides/js/13-biome/13-03-formatting.md`
2. **Apply**:
   - Install Biome standalone (`brew install biome`), not via npm
   - Run `biome init` to scaffold `biome.json`
   - Configure: spaces, indent 2, line width 100, double quotes, always semicolons, trailing commas all
   - Enable VCS integration with `useIgnoreFile: true`
   - Remove `lint` and `fmt` fields from `deno.json`
   - Wire into `deno task`: `lint`, `lint:fix`, `fmt`, `check`, `ci`
   - VS Code: install `biomejs.biome`, set `"deno.lint": false`, configure format-on-save
   - Enable `types` domain if project has JSDoc coverage
   - Run `biome ci` to validate — fix all violations before committing

### Task: "Migrate a Node.js codebase to Deno project idioms"

1. **Load**: `guides/js/14-no-node-boundary.md`, `guides/js/12-deno/12-01-runtime-basics.md`, `guides/js/01-core-idioms.md`, `guides/js/09-anti-patterns.md`
2. **Apply**:
   - Replace `package.json` → `deno.json` with `imports`, `tasks`, `compilerOptions`
   - Replace `require()` → `import` with explicit `.js` extensions
   - Replace `module.exports` → ESM `export`
   - Replace `index.js` → `mod.js` entry points
   - Replace `process.env` → `Deno.env.get()`, `__dirname` → `import.meta.dirname`
   - Replace `fs.readFile` → `Deno.readTextFile`, `http.createServer` → `Deno.serve()`
   - Replace `Buffer` → `Uint8Array` + `TextEncoder`/`TextDecoder`
   - Replace Node streams → Web Streams (`ReadableStream`/`WritableStream`)
   - Replace Jest/Mocha → `Deno.test()` + `@std/assert`
   - Replace ESLint + Prettier → Biome (`biome.json`)
   - Use `npm:` specifiers for npm packages with no JSR equivalent
   - Fix `||` → `??`, `var` → `const`/`let`, `==` → `===`

### Task: "Performance review of an async data pipeline"

1. **Load**: `guides/js/08-performance.md`, `guides/js/07-async-concurrency.md`, `guides/js/09-anti-patterns.md`
2. **Apply**:
   - Check for sequential `await` on independent ops → convert to `Promise.all()`
   - Check for `.map(async fn)` without `Promise.all()` wrapping
   - Check for large intermediate arrays → consider generators or streaming
   - Check for `Array.includes()` in hot loops → convert to `Set`
   - Check for plain objects as dynamic maps → convert to `Map`
   - Profile with `Deno.bench()` before and after changes
   - Don't micro-optimize without measurement evidence
