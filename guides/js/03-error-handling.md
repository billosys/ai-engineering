# Error Handling

Essential patterns for throwing, catching, and propagating errors in JavaScript. Covers synchronous exceptions, Promise rejections, async/await error flows, custom error types, and validation discipline — grounded in *Exploring JavaScript* (Rauschmayer), *Deep JavaScript* (Rauschmayer), *JavaScript: The Definitive Guide* (Flanagan), and *Eloquent JavaScript* (Haverbeke).

Target environment: **Deno**, **ESM-only**, **Biome** for linting/formatting, **no TypeScript** (JSDoc where needed).

---

## ID-01: Always Throw `Error` Objects, Never Strings or Plain Values

**Strength**: MUST

**Summary**: Only `Error` instances carry `.stack`, `.message`, `.name`, and `.cause` — throw anything else and you lose all of them.

```js
// Good
throw new Error("Connection refused");
throw new TypeError("Expected a number, got string");
throw new RangeError(`Index ${i} out of bounds [0, ${max})`);

// Bad — no stack trace, no .cause support, no .name
throw "Connection refused";
throw 404;
throw { code: "ERR_TIMEOUT", message: "Timed out" };
```

**Rationale**: Stack traces are captured at `new Error()` creation time. Throwing a string or plain object loses the call stack, making debugging a guessing game. All four sources explicitly recommend throwing only `Error` instances (Exploring JS Ch. 26; Eloquent JS Ch. 8; JS Definitive Guide, §5.5.6).

---

## ID-02: Use `throw` for Exceptional Conditions, Not Control Flow

**Strength**: MUST

**Summary**: Throw when something unexpected and unrecoverable at the current level has happened. Do not use exceptions for expected outcomes like "user not found."

```js
// Good — exceptional: file system error, invalid argument
function parseConfig(path) {
  const raw = Deno.readTextFileSync(path);
  const config = JSON.parse(raw); // throws SyntaxError on bad JSON — correct
  if (!config.version) {
    throw new Error(`Config at ${path} missing required "version" field`);
  }
  return config;
}

// Bad — using throw for expected "not found" flow
function findUser(id) {
  const user = users.get(id);
  if (!user) throw new Error("User not found"); // expected case, not exceptional
  return user;
}

// Good — return undefined for expected absence
function findUser(id) {
  return users.get(id); // undefined if not present
}
```

**Rationale**: Exceptions unwind the call stack and disrupt normal control flow. Using them for expected outcomes forces callers into try/catch for routine logic and obscures genuine errors (Eloquent JS Ch. 8; Exploring JS Ch. 26).

**See also**: `02-api-design.md` ID-23, ID-24

---

## ID-03: Include Context in Error Messages

**Strength**: MUST

**Summary**: Error messages must say what failed and why. Include the relevant values.

```js
// Good — says what, why, and includes the offending value
throw new TypeError(`Expected port to be a number, got ${typeof port}: ${port}`);
throw new RangeError(`Retry count ${retries} exceeds maximum (${MAX_RETRIES})`);
throw new Error(`Failed to fetch ${url}: ${response.status} ${response.statusText}`);

// Bad — says nothing useful
throw new Error("Invalid argument");
throw new Error("Something went wrong");
throw new TypeError("Wrong type");
```

**Rationale**: When an error surfaces in logs or a stack trace, the message is often the only context. "Invalid argument" forces a developer to read the source and reproduce the issue. A message with the value and constraint makes the fix obvious.

---

## ID-04: Use `Error.cause` for Error Chaining

**Strength**: SHOULD

**Summary**: When catching and rethrowing, pass the original error as `{ cause }` to preserve the full chain.

```js
// Good — chain preserves the original error and its stack trace
async function loadConfig(path) {
  try {
    const raw = await Deno.readTextFile(path);
    return JSON.parse(raw);
  } catch (err) {
    throw new Error(`Failed to load config from ${path}`, { cause: err });
  }
}

// Bad — original error discarded, stack trace lost
async function loadConfig(path) {
  try {
    const raw = await Deno.readTextFile(path);
    return JSON.parse(raw);
  } catch (err) {
    throw new Error(`Failed to load config from ${path}`); // cause gone
  }
}
```

**Accessing the chain**:
```js
try {
  await loadConfig("./config.json");
} catch (err) {
  console.error(err.message);       // "Failed to load config from ./config.json"
  console.error(err.cause.message); // "Unexpected token } in JSON at position 42"
  console.error(err.cause.stack);   // original stack trace preserved
}
```

**Rationale**: `Error.cause` (ES2022) preserves the original error and its stack trace while adding higher-level context. Without it, rethrowing loses the root cause. All built-in error subclasses support `{ cause }` as the second argument to the constructor (Exploring JS Ch. 26).

---

## ID-05: Subclass `Error` for Domain-Specific Error Types

**Strength**: SHOULD

**Summary**: Create custom error classes for errors that callers need to handle differently from generic errors.

```js
// Good — custom error with context properties
class HttpError extends Error {
  constructor(status, statusText, url) {
    super(`${status} ${statusText}: ${url}`);
    this.status = status;
    this.statusText = statusText;
    this.url = url;
  }
  get name() { return "HttpError"; }
}

class ValidationError extends Error {
  constructor(field, reason) {
    super(`Validation failed for "${field}": ${reason}`);
    this.field = field;
    this.reason = reason;
  }
  get name() { return "ValidationError"; }
}

// Usage — selective catch
try {
  await submitForm(data);
} catch (err) {
  if (err instanceof ValidationError) {
    showFieldError(err.field, err.reason);
  } else if (err instanceof HttpError && err.status === 429) {
    await retryAfterDelay();
  } else {
    throw err; // unknown error — propagate
  }
}
```

**Rationale**: Custom error classes enable `instanceof` checks for selective catching, carry domain-specific properties (status codes, field names), and produce descriptive `.name` values in logs. Always call `super(message, options)` and set `.name` — without it, the name defaults to `"Error"` (Exploring JS Ch. 26; JS Definitive Guide, §11.5).

---

## ID-06: Custom Errors Must Set `name`

**Strength**: MUST

**Summary**: Override `.name` in custom error classes so logs and stack traces identify the error type.

```js
// Good — name matches the class
class ConfigError extends Error {
  get name() { return "ConfigError"; }
}

// Bad — name defaults to "Error"
class ConfigError extends Error {
  // .name is inherited as "Error" — misleading in logs
}
```

**Two approaches**: Use a getter (`get name()`) for zero-cost on unused instances, or set `this.name` in the constructor for simplicity. Either works.

**Rationale**: Without a custom `.name`, all subclasses display as `"Error"` in stack traces and `console.error()` output, defeating the purpose of type-specific errors (Exploring JS Ch. 26).

---

## ID-07: Use `AggregateError` for Multiple Simultaneous Failures

**Strength**: CONSIDER

**Summary**: When multiple independent operations can fail and you need all the failure reasons, use `AggregateError`.

```js
// Good — collect all validation errors at once
function validateForm(data) {
  const errors = [];
  if (!data.name) errors.push(new Error("name is required"));
  if (!data.email) errors.push(new Error("email is required"));
  if (data.age !== undefined && data.age < 0) {
    errors.push(new RangeError("age must be non-negative"));
  }
  if (errors.length > 0) {
    throw new AggregateError(errors, "Form validation failed");
  }
  return data;
}

// Handling
try {
  validateForm({});
} catch (err) {
  if (err instanceof AggregateError) {
    for (const e of err.errors) {
      console.error(`- ${e.message}`);
    }
  }
}
```

**Rationale**: `AggregateError` (ES2021) holds an array of errors in `.errors`. It is the rejection value of `Promise.any()` when all inputs reject, and is appropriate for batch validation and multi-source failures where reporting all errors is better than stopping at the first (Exploring JS Ch. 26, Ch. 43).

---

## ID-08: Never Write Empty `catch` Blocks

**Strength**: MUST

**Summary**: An empty `catch` silently discards both expected and unexpected errors. Always log, handle, or rethrow.

```js
// Bad — swallows everything, including programmer errors
try {
  riskyOperation();
} catch (e) {
  // silence
}

// Good — handle known errors, rethrow unknown
try {
  riskyOperation();
} catch (e) {
  if (e instanceof KnownError) {
    recover(e);
  } else {
    throw e;
  }
}

// Good — log if you can't handle
try {
  riskyOperation();
} catch (e) {
  console.error("riskyOperation failed:", e);
  throw e;
}
```

**Rationale**: Empty catch blocks are the root cause of "the program does nothing and nobody knows why" bugs. Typos, wrong types, and logic errors become completely invisible. Haverbeke warns that blanket-catching hides bugs and makes debugging nearly impossible (Eloquent JS Ch. 8; Exploring JS Ch. 26).

---

## ID-09: Catch Specific Errors, Not Everything

**Strength**: SHOULD

**Summary**: Use `instanceof` checks inside `catch` to handle only errors you understand. Rethrow everything else.

```js
// Good — selective catching
try {
  const data = JSON.parse(raw);
  return processData(data);
} catch (e) {
  if (e instanceof SyntaxError) {
    return { error: "Invalid JSON", raw };
  }
  throw e; // TypeError, ReferenceError, etc. propagate
}

// Bad — blanket catch hides a typo
try {
  const dir = promtDirection("Where?"); // typo! "promtDirection"
  console.log(dir);
} catch (e) {
  console.log("Not a valid direction."); // typo is silently swallowed
}
```

**Rationale**: JavaScript's single `catch` clause catches all exceptions without discrimination. Without `instanceof` filtering, programmer errors (misspelled variables, wrong property access) are silently swallowed alongside the errors you intended to handle (Eloquent JS Ch. 8; Exploring JS Ch. 26).

---

## ID-10: Re-Throw Unknown Errors

**Strength**: MUST

**Summary**: After handling known error types, always `throw` the error if it's not one you recognize.

```js
// Good
try {
  await fetchResource(url);
} catch (e) {
  if (e instanceof HttpError && e.status === 404) {
    return null; // expected: resource not found
  }
  if (e instanceof HttpError && e.status === 429) {
    await delay(1000);
    return fetchResource(url); // retry once
  }
  throw e; // anything else: network error, TypeError, etc.
}
```

**Rationale**: Catching and not rethrowing converts an error into silent success. Unknown errors are likely programmer bugs or environmental failures that should propagate to a top-level handler where they can be logged and diagnosed.

---

## ID-11: Use `finally` for Cleanup, Not for Return Values

**Strength**: SHOULD

**Summary**: `finally` always runs — use it for cleanup. Never `return` from a `finally` block.

```js
// Good — resource cleanup
const file = await Deno.open("data.txt");
try {
  return await processFile(file);
} finally {
  file.close(); // guaranteed cleanup
}

// Bad — return in finally silently overrides try's return/throw
function dangerous() {
  try {
    throw new Error("something broke");
  } finally {
    return "all good"; // ERROR IS SILENTLY DISCARDED
  }
}
dangerous(); // "all good" — the error vanished
```

**Rationale**: `return`, `throw`, or `break` inside `finally` overrides any pending result from `try` or `catch`. This can silently discard exceptions — one of the most insidious JavaScript bugs. Use `finally` exclusively for cleanup (closing resources, releasing locks), never for producing values (Exploring JS Ch. 26; JS Definitive Guide, §5.5.7).

---

## ID-12: Omit the Catch Binding When You Don't Need It

**Strength**: CONSIDER

**Summary**: When you only need to know that an error occurred, not what it was, use `catch { }` without a parameter.

```js
// Good — parse with fallback, error details irrelevant
function tryParseJSON(s) {
  try {
    return JSON.parse(s);
  } catch {
    return undefined;
  }
}

// Good — boolean "does it throw?" check
function isValidJSON(s) {
  try { JSON.parse(s); return true; } catch { return false; }
}
```

**Rationale**: ES2019 made the catch binding optional. Omitting it signals to readers that the error value is intentionally unused — cleaner than `catch (_e)` or `catch (ignored)`. Not a license for empty catch blocks — the block must still do something meaningful (Exploring JS Ch. 26).

---

## ID-13: Always Handle Promise Rejections

**Strength**: MUST

**Summary**: Every Promise chain must have a rejection handler. Unhandled rejections are silent bugs (or fatal in some runtimes).

```js
// Good — .catch() at the end of the chain
fetchData(url)
  .then((data) => process(data))
  .then((result) => save(result))
  .catch((err) => console.error("Pipeline failed:", err));

// Good — async/await with try/catch
async function run() {
  try {
    const data = await fetchData(url);
    const result = await process(data);
    await save(result);
  } catch (err) {
    console.error("Pipeline failed:", err);
  }
}

// Bad — dangling Promise, rejection lost
fetchData(url).then((data) => process(data)); // no .catch()
```

**Rationale**: In modern Deno and Node.js, unhandled rejections terminate the process by default. Even where they don't terminate, they produce silent failures. Every Promise chain must end with either `.catch()` or be inside a `try`/`catch` with `await` (Exploring JS Ch. 43; JS Definitive Guide, §13.2.4).

---

## ID-14: Prefer `async`/`await` with `try`/`catch` over `.then().catch()`

**Strength**: SHOULD

**Summary**: Use `async`/`await` for async error handling. It reads linearly, supports loops and conditionals, and uses the same `try`/`catch` as synchronous code.

```js
// Good — linear, readable, standard error handling
async function loadUser(id) {
  try {
    const response = await fetch(`/api/users/${id}`);
    if (!response.ok) throw new HttpError(response.status, response.statusText, response.url);
    return await response.json();
  } catch (err) {
    if (err instanceof HttpError && err.status === 404) return null;
    throw err;
  }
}

// Less preferred — scattered callbacks, harder to follow
function loadUser(id) {
  return fetch(`/api/users/${id}`)
    .then((response) => {
      if (!response.ok) throw new HttpError(response.status, response.statusText, response.url);
      return response.json();
    })
    .catch((err) => {
      if (err instanceof HttpError && err.status === 404) return null;
      throw err;
    });
}
```

**Rationale**: `.then().catch()` chains split logic across callbacks, scatter error handling, and create readability problems at scale. `async`/`await` supports native loops, conditionals, and `try`/`catch` — constructs that are awkward or impossible in Promise chains (Exploring JS Ch. 42; JS Definitive Guide, §13.3).

---

## ID-15: Understand `.catch()` Placement — It Matters

**Strength**: MUST

**Summary**: `.catch()` only handles rejections from earlier in the chain. Placement determines scope.

```js
// Good — terminal .catch() covers the entire chain
fetchData()
  .then((data) => transform(data))
  .then((result) => save(result))
  .catch((err) => handleError(err)); // catches errors from all three steps

// Good — mid-chain .catch() for recovery, then continue
fetchData()
  .then((data) => riskyTransform(data))
  .catch((err) => fallbackValue)        // recovers — chain continues as fulfilled
  .then((result) => save(result))
  .catch((err) => handleSaveError(err)); // catches save errors

// Bad — two-argument .then() misses handler exceptions
promise.then(
  (result) => process(result),  // if this throws...
  (err) => handleError(err),    // ...this won't catch it
);

// Good — .catch() after .then() catches handler exceptions
promise
  .then((result) => process(result))
  .catch((err) => handleError(err)); // catches both rejection AND handler throws
```

**Rationale**: Using `.then(handler, errorHandler)` with both arguments will NOT catch exceptions thrown by `handler` itself — the error handler only covers the Promise, not the fulfillment callback. A separate `.catch()` avoids this gap (JS Definitive Guide, §13.2.4; Exploring JS Ch. 43).

---

## ID-16: Use `Promise.allSettled()` When Some Failures Are Acceptable

**Strength**: SHOULD

**Summary**: When you need all outcomes regardless of individual failures, use `Promise.allSettled()` instead of `Promise.all()`.

```js
// Good — inspect each outcome independently
const results = await Promise.allSettled([
  fetch("/api/users"),
  fetch("/api/posts"),
  fetch("/api/comments"),
]);

for (const result of results) {
  if (result.status === "fulfilled") {
    processResponse(result.value);
  } else {
    console.warn("Request failed:", result.reason);
  }
}

// Bad — Promise.all() aborts on first failure, losing partial results
const responses = await Promise.all([
  fetch("/api/users"),
  fetch("/api/posts"),    // if this fails...
  fetch("/api/comments"), // ...this result is lost
]);
```

**Rationale**: `Promise.all()` short-circuits on the first rejection — the remaining results are discarded. `Promise.allSettled()` (ES2020) never rejects; it returns an array of `{ status, value/reason }` objects for every input. Use it for batch operations, health checks, and multi-source fetches where partial success is acceptable (Exploring JS Ch. 43; JS Definitive Guide, §13.2.5).

---

## ID-17: Use `Promise.any()` for First-Success Patterns

**Strength**: CONSIDER

**Summary**: `Promise.any()` fulfills with the first success, ignoring individual rejections. It only rejects when all inputs fail.

```js
// Good — try multiple sources, take the first success
const content = await Promise.any([
  fetch("https://cdn1.example.com/data.json").then((r) => r.text()),
  fetch("https://cdn2.example.com/data.json").then((r) => r.text()),
  fetch("https://cdn3.example.com/data.json").then((r) => r.text()),
]);

// Handle total failure
try {
  const content = await Promise.any(sources);
} catch (err) {
  // err is AggregateError — all sources failed
  console.error("All sources failed:");
  for (const e of err.errors) console.error(`  - ${e.message}`);
}
```

**Rationale**: `Promise.any()` (ES2021) is the inverse of `Promise.all()`: it needs just one success. The rejection value is an `AggregateError` containing all individual rejection reasons. Contrast with `Promise.race()`, which settles on the first result regardless of success or failure (Exploring JS Ch. 43).

---

## ID-18: Never Mix Callbacks and Promises

**Strength**: MUST

**Summary**: A function must be either callback-based or Promise-based, never both. In new code, always use Promises.

```js
// Good — Promise-only API
export async function readConfig(path) {
  const raw = await Deno.readTextFile(path);
  return JSON.parse(raw);
}

// Bad — dual interface
export function readConfig(path, callback) {
  const promise = Deno.readTextFile(path).then((raw) => JSON.parse(raw));
  if (callback) {
    promise.then((data) => callback(null, data)).catch((err) => callback(err));
  }
  return promise;
}
```

**Critical rule**: Promise-based functions must never throw synchronous exceptions. Callers set up `.catch()` handlers, not `try`/`catch` around the call. A synchronous throw escapes the Promise chain entirely (Exploring JS Ch. 43).

**See also**: `02-api-design.md` ID-25

---

## ID-19: `return await` Inside `try` — When It Matters

**Strength**: MUST

**Summary**: Inside a `try`/`catch`, use `return await` to ensure rejections are caught locally.

```js
// Good — return await: rejection is caught by the local catch
async function loadData(url) {
  try {
    return await fetch(url).then((r) => r.json());
  } catch (err) {
    console.error(`Failed to load ${url}:`, err);
    return null;
  }
}

// Bad — return without await: rejection escapes the catch
async function loadData(url) {
  try {
    return fetch(url).then((r) => r.json()); // catch is bypassed!
  } catch (err) {
    console.error(`Failed to load ${url}:`, err); // never executes
    return null;
  }
}
```

**Outside `try`/`catch`**, `return await p` and `return p` are functionally equivalent. The distinction only matters when you need the local `catch` to intercept the rejection (Exploring JS Ch. 42; JS Definitive Guide, §13.3).

---

## ID-20: Beware Fire-and-Forget Async Calls

**Strength**: MUST

**Summary**: Calling an async function without `await` starts it in the background. Any rejection is silently lost.

```js
// Bad — rejection has nowhere to go
async function handleRequest(req) {
  logRequest(req);              // async, unawaited — rejection lost
  const data = await getData();
  return data;
}

// Good — await it if you need the result or error
async function handleRequest(req) {
  await logRequest(req);
  const data = await getData();
  return data;
}

// Good — fire-and-forget with explicit catch
async function handleRequest(req) {
  logRequest(req).catch((err) => console.error("Log failed:", err));
  const data = await getData();
  return data;
}
```

**Rationale**: An unawaited async call creates a floating Promise with no rejection handler. In Deno, unhandled rejections terminate the process. At minimum, attach `.catch()` to any intentionally unawaited async call (Exploring JS Ch. 42).

---

## ID-21: Parallel `await` — Use `Promise.all()`, Not Sequential Awaits

**Strength**: SHOULD

**Summary**: When async operations are independent, run them in parallel with `Promise.all()`.

```js
// Good — parallel execution
const [users, posts] = await Promise.all([
  fetchUsers(),
  fetchPosts(),
]);

// Bad — sequential, doubles total wait time
const users = await fetchUsers();
const posts = await fetchPosts(); // waits for users to finish first
```

**Rationale**: Sequential `await` on independent operations is a performance anti-pattern. `Promise.all()` starts all operations simultaneously. Use sequential `await` only when a later operation depends on the result of an earlier one (JS Definitive Guide, §13.3.3; Exploring JS Ch. 42).

---

## ID-22: Awaiting Is Shallow — Nested Async Needs Explicit Handling

**Strength**: SHOULD

**Summary**: `await` only pauses its immediately enclosing `async` function. Nested async callbacks (e.g., inside `.map()`) require `Promise.all()`.

```js
// Bad — .map(async fn) returns an array of Promises, not resolved values
async function processAll(items) {
  const results = items.map(async (item) => {
    return await transform(item); // pauses inner fn only
  });
  return results; // array of Promises!
}

// Good — await the array of Promises
async function processAll(items) {
  return await Promise.all(
    items.map((item) => transform(item)),
  );
}
```

**Rationale**: `await` cannot reach into a callback's scope. `items.map(async fn)` returns `Promise[]`, not resolved values. You must collect the Promises and `await Promise.all()` to get the results (Exploring JS Ch. 42; Eloquent JS Ch. 11).

---

## ID-23: Validate at Boundaries, Trust Within

**Strength**: SHOULD

**Summary**: Check types and constraints at public API entry points. Inside validated boundaries, trust the data.

```js
// Good — validation at the public boundary
export function createUser({ name, email, age }) {
  if (typeof name !== "string" || name.length === 0) {
    throw new TypeError("name must be a non-empty string");
  }
  if (typeof email !== "string" || !email.includes("@")) {
    throw new TypeError("email must be a valid email address");
  }
  if (age !== undefined && (typeof age !== "number" || age < 0)) {
    throw new RangeError("age must be a non-negative number");
  }
  // Internal functions trust these values
  return { id: generateId(), name, email, age: age ?? null };
}

// Bad — redundant validation deep inside internal functions
function formatUserLine(name) {
  if (typeof name !== "string") throw new TypeError("...");  // already validated at boundary
  return `User: ${name}`;
}
```

**Rationale**: JavaScript's type coercion means wrong-typed inputs produce silent failures (`NaN`, wrong string concatenation) rather than errors. Validate at system boundaries (public functions, API handlers, user input). Redundant validation inside internal code adds noise without safety (Exploring JS Ch. 16; Deep JS Ch. 14).

---

## ID-24: Fail Fast — Detect and Throw on Invalid Input Immediately

**Strength**: MUST

**Summary**: Reject invalid input at the top of a function with guard clauses. Don't let bad data travel.

```js
// Good — guard clauses at the top
async function fetchUser(id) {
  if (id == null) throw new TypeError("id is required");
  if (typeof id !== "string") throw new TypeError(`id must be a string, got ${typeof id}`);

  const response = await fetch(`/api/users/${id}`);
  if (!response.ok) throw new HttpError(response.status, response.statusText, response.url);
  return response.json();
}

// Bad — error surfaces far from the cause
async function fetchUser(id) {
  const response = await fetch(`/api/users/${id}`); // id is undefined → fetches "/api/users/undefined"
  return response.json(); // 404 or garbage response — confusing error
}
```

**Rationale**: JavaScript silently coerces `undefined` and `null` into strings (`"undefined"`, `"null"`) when interpolated into URLs or concatenated. Failing fast at the entry point produces an error with a useful stack trace pointing at the caller, not at some downstream effect (Exploring JS Ch. 16).

**See also**: `01-core-idioms.md` ID-26

---

## ID-25: Prefer Returning `undefined`/`null` over Throwing for "Not Found"

**Strength**: SHOULD

**Summary**: When absence is an expected outcome, return `undefined` or `null`. Reserve `throw` for unexpected failures.

```js
// Good — "not found" is expected, return undefined
function findUser(id) {
  return users.get(id); // undefined if absent — matches Map.get() convention
}

// Good — null for explicit "searched and found nothing"
function getOverride(key) {
  if (!(key in overrides)) return undefined; // key not recognized
  return overrides[key] ?? null;             // key exists, value explicitly empty
}

// Bad — throwing for an expected case
function findUser(id) {
  const user = users.get(id);
  if (!user) throw new Error(`User ${id} not found`); // forces try/catch for normal flow
  return user;
}
```

**Rationale**: Throwing forces callers into try/catch for routine lookups. Returning `undefined`/`null` lets callers use `??`, `?.`, or simple `if` checks. Reserve exceptions for truly exceptional conditions (Exploring JS Ch. 16; JS Definitive Guide, §3.5).

**See also**: `02-api-design.md` ID-23, ID-24

---

## ID-26: Use Assertions in Tests, Not in Production Code

**Strength**: SHOULD

**Summary**: `assert.*` functions throw `AssertionError` and are designed for tests. In production, use explicit guards with typed errors.

```js
// Good — in tests
import { assertEquals, assertThrows } from "@std/assert";

Deno.test("parsePort rejects non-numeric", () => {
  assertThrows(() => parsePort("abc"), TypeError);
});

Deno.test("parsePort returns number", () => {
  assertEquals(parsePort("8080"), 8080);
});

// Good — in production (explicit guard, specific error type)
function parsePort(input) {
  const port = Number(input);
  if (!Number.isFinite(port) || port < 0 || port > 65535) {
    throw new RangeError(`Invalid port: ${input}`);
  }
  return port;
}

// Bad — assertion in production code
import { assert } from "@std/assert";
function parsePort(input) {
  const port = Number(input);
  assert(port >= 0 && port <= 65535); // AssertionError — not informative
  return port;
}
```

**Rationale**: `assert.equal()` uses `===` (identity, not deep equality), `AssertionError` messages are generic, and assertions conflate test infrastructure with application logic. In production, throw domain-appropriate errors with specific messages (Exploring JS Ch. 8).

---

## ID-27: Never Swallow Errors Silently

**Strength**: MUST

**Summary**: If you catch an error, you must do something with it — log, handle, or rethrow. Silent swallowing is always a bug.

```js
// Bad — silent swallow
try { await sync(); } catch (e) { /* TODO */ }

// Bad — catch with only a console.log that could be missed
try { await sync(); } catch (e) { console.log(e); } // easy to miss in noisy output

// Good — explicit handling with structured logging
try {
  await sync();
} catch (e) {
  console.error("[sync] Failed:", e.message, { cause: e.cause });
  throw e; // or handle and continue
}
```

**Rationale**: This is the most important error handling rule. Every silent swallow creates a class of bugs that are invisible to developers. Even during prototyping, at minimum log the error. In production, structured error reporting is essential (Eloquent JS Ch. 8; Exploring JS Ch. 26).

---

## ID-28: Avoid `Promise.reject()` in Async Functions — Just `throw`

**Strength**: SHOULD

**Summary**: Inside an `async` function, `throw` is the natural way to reject. `Promise.reject()` is redundant.

```js
// Good — throw in async function
async function loadData(url) {
  const response = await fetch(url);
  if (!response.ok) {
    throw new HttpError(response.status, response.statusText, url);
  }
  return response.json();
}

// Bad — unnecessary Promise.reject()
async function loadData(url) {
  const response = await fetch(url);
  if (!response.ok) {
    return Promise.reject(new HttpError(response.status, response.statusText, url));
  }
  return response.json();
}
```

**Rationale**: In an `async` function, `throw` automatically becomes a rejected Promise. Using `Promise.reject()` adds verbosity without benefit and may confuse readers about whether the function is truly async (Exploring JS Ch. 42).

---

---

## Best Practices Summary

### Quick Reference Table

| ID | Pattern | Strength | Key Insight |
|----|---------|----------|-------------|
| 01 | Throw `Error` objects only | MUST | Strings/values have no `.stack`, `.cause`, `.name` |
| 02 | `throw` for exceptional, not expected | MUST | Don't use exceptions for "not found" control flow |
| 03 | Context in error messages | MUST | Include what failed, why, and the offending value |
| 04 | `Error.cause` for chaining | SHOULD | Preserves original error + stack when rethrowing |
| 05 | Custom `Error` subclasses | SHOULD | Enables `instanceof` checks and domain-specific properties |
| 06 | Set `.name` on custom errors | MUST | Without it, all subclasses display as "Error" in logs |
| 07 | `AggregateError` for multiple failures | CONSIDER | `.errors` array for batch validation and `Promise.any()` |
| 08 | No empty `catch` blocks | MUST | Silent swallowing hides bugs completely |
| 09 | Selective catching with `instanceof` | SHOULD | JS has one `catch` clause — filter manually |
| 10 | Re-throw unknown errors | MUST | Don't convert unknown errors into silent success |
| 11 | `finally` for cleanup only | SHOULD | `return` in `finally` silently discards exceptions |
| 12 | Omit catch binding when unused | CONSIDER | `catch { }` signals intentional discard (ES2019) |
| 13 | Always handle rejections | MUST | Unhandled rejections terminate Deno/Node.js |
| 14 | `async`/`await` over `.then().catch()` | SHOULD | Linear flow, native loops/conditionals, unified error handling |
| 15 | `.catch()` placement matters | MUST | Two-arg `.then()` misses handler exceptions |
| 16 | `Promise.allSettled()` for partial success | SHOULD | Never rejects; returns `{status, value/reason}` for all |
| 17 | `Promise.any()` for first-success | CONSIDER | Rejects with `AggregateError` only when all fail |
| 18 | Never mix callbacks and Promises | MUST | Sync throws escape the Promise chain |
| 19 | `return await` inside `try` | MUST | Without `await`, rejection escapes the local `catch` |
| 20 | Handle fire-and-forget rejections | MUST | Unawaited async calls lose rejections silently |
| 21 | Parallel `await` with `Promise.all()` | SHOULD | Sequential await on independent ops wastes time |
| 22 | Awaiting is shallow | SHOULD | `.map(async fn)` returns `Promise[]`, not values |
| 23 | Validate at boundaries | SHOULD | Trust within; validate at public entry points |
| 24 | Fail fast on invalid input | MUST | Guard clauses at function top, not downstream effects |
| 25 | Return `undefined`/`null` for "not found" | SHOULD | Reserve `throw` for unexpected failures |
| 26 | Assertions for tests only | SHOULD | Use typed errors with specific messages in production |
| 27 | Never swallow errors silently | MUST | Log, handle, or rethrow — never ignore |
| 28 | `throw` in async, not `Promise.reject()` | SHOULD | `throw` is the natural rejection mechanism in async |

---

## Related Guidelines

- **Core Idioms**: See `01-core-idioms.md` for `===` (ID-02), `??` (ID-03), `?.` (ID-04), early returns (ID-26)
- **API Design**: See `02-api-design.md` for return value conventions (ID-04, ID-23, ID-24) and consistent types
- **Values & References**: See `04-values-references.md` for mutation discipline (ID-12, ID-13) and defensive copying
- **Type Discipline**: See `05-type-discipline.md` for runtime validation (ID-29) and `typeof` guards (ID-01)
- **Functions & Closures**: See `06-functions-closures.md` for closure capture in async callbacks (ID-06–10)
- **Async & Concurrency**: See `07-async-concurrency.md` for concurrency limits (ID-17), cancellation (ID-23–26), and combinators (ID-13–16) — those idioms cross-reference ID-13–22 here for error behavior
- **Anti-Patterns**: See `09-anti-patterns.md` for ID-18, 19, 20, 21, 22, 24, 36 (error handling anti-patterns)
- **Deno**: See `12-deno/01-runtime-basics.md` for Deno-specific error handling and permissions

---

## External References

- [Deno Manual](https://docs.deno.com/)
- [MDN — Error](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Error)
- [MDN — Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)
- *Exploring JavaScript* (ES2025) — Axel Rauschmayer
- *Deep JavaScript* — Axel Rauschmayer
- *JavaScript: The Definitive Guide* (7th ed.) — David Flanagan
- *Eloquent JavaScript* (4th ed.) — Marijn Haverbeke
