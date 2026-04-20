# Async & Concurrency

Concurrency orchestration in JavaScript: the event loop, Promises, async/await, async iteration, cancellation, streams, workers, and scheduling. This guide focuses on *orchestration and concurrency patterns* — async error handling is covered in Guide 03 and cross-referenced here, not re-taught. Grounded in *Exploring JavaScript* (Rauschmayer), *Deep JavaScript* (Rauschmayer), *JavaScript: The Definitive Guide* (Flanagan), and *Eloquent JavaScript* (Haverbeke).

Target environment: **Deno**, **ESM-only**, **Biome** for linting/formatting, **no TypeScript** (JSDoc where needed).

---

## ID-01: JavaScript Is Single-Threaded — One Call Stack, Run to Completion

**Strength**: MUST

**Summary**: JavaScript executes one task at a time. Each task always finishes before the next begins — no preemptive interruption.

```js
// This runs to completion — no other task can interrupt it
function handleRequest(data) {
  const parsed = JSON.parse(data);     // sync
  const result = transform(parsed);     // sync
  return serialize(result);             // sync — entire function completes as one task
}

// Consequence: no locks or mutexes needed for shared state WITHIN a task
let count = 0;
count++;    // safe — no concurrent modification possible within a task
```

**The event loop model**: `while (true) { const task = taskQueue.dequeue(); task(); }`. Task sources (timers, I/O, user events) enqueue tasks, but only one executes at a time inside the JS thread.

**Rationale**: Run-to-completion eliminates data races within a task — the most common class of concurrency bugs in multi-threaded languages. But it means a blocked task freezes everything: UI, timers, other handlers. This is why async patterns exist (Exploring JS Ch. 42; Deep JS Ch. 19; Eloquent JS Ch. 11).

---

## ID-02: Microtasks Run Before Macrotasks

**Strength**: SHOULD

**Summary**: Promise callbacks (microtasks) drain completely before the event loop picks up the next timer/IO callback (macrotask).

```js
console.log("1: sync");
setTimeout(() => console.log("4: macrotask"), 0);
Promise.resolve().then(() => console.log("2: microtask"));
queueMicrotask(() => console.log("3: microtask"));
// Output: 1: sync → 2: microtask → 3: microtask → 4: macrotask
```

**Two scheduling tiers**:
- **Microtask queue**: `.then()`, `.catch()`, `.finally()`, `await` continuations, `queueMicrotask()`
- **Macrotask queue**: `setTimeout`, `setInterval`, I/O callbacks, user events

After each macrotask completes, the engine drains **all** pending microtasks before picking up the next macrotask.

**Rationale**: Understanding this ordering is essential for debugging async code. `setTimeout(fn, 0)` does NOT run "immediately" — it runs after all pending microtasks. Promise callbacks always execute before the next timer tick (Exploring JS Ch. 42; Deep JS Ch. 19).

---

## ID-03: Never Block the Event Loop

**Strength**: MUST

**Summary**: No synchronous I/O, no busy-wait loops, no long computation on the main thread.

```js
// Bad — blocks for 5 seconds; freezes all handlers, UI, and timers
function sleep(ms) {
  const start = Date.now();
  while (Date.now() - start < ms) { /* busy wait */ }
}

// Good — yields the event loop; only this async function pauses
const sleep = (ms) => new Promise((resolve) => setTimeout(resolve, ms));
await sleep(5000);

// Bad — synchronous file read blocks the event loop
const data = Deno.readTextFileSync("large.csv");

// Good — async file read yields while waiting for I/O
const data = await Deno.readTextFile("large.csv");
```

**Avoidance strategies** (in order of preference):
1. Use async APIs — `fetch()`, `Deno.readTextFile()`, `await`
2. Offload CPU-heavy work to Web Workers (ID-31)
3. Break computation into chunks via `setTimeout(chunk, 0)` (least preferred)

**Rationale**: A blocked event loop freezes the entire process — no other handlers, timers, or I/O callbacks can run. In a server, this means all concurrent requests stall. In a UI, everything freezes (Exploring JS Ch. 42; Eloquent JS Ch. 11).

---

## ID-04: `queueMicrotask()` for Immediate Async Scheduling

**Strength**: CONSIDER

**Summary**: Schedule a callback at microtask priority — after the current synchronous code, before the next macrotask.

```js
// Good — microtask priority
queueMicrotask(() => {
  console.log("runs before any setTimeout, after current sync code");
});

// Bad — setTimeout is macrotask priority (runs later)
setTimeout(() => {
  console.log("runs after all pending microtasks");
}, 0);
```

**Rationale**: `queueMicrotask()` is the correct tool when you need to defer work to the end of the current microtask checkpoint without creating a Promise chain. Use it for framework-level scheduling or when testing Promise ordering. For application code, `await` and Promises are usually more appropriate (Exploring JS Ch. 42; Deep JS Ch. 19).

---

## ID-05: Promises Start Synchronously, Settle Asynchronously

**Strength**: MUST

**Summary**: The `new Promise(executor)` executor runs synchronously. Settlement notifications (`.then()` callbacks) are always delivered asynchronously as microtasks.

```js
console.log("1: before");
const p = new Promise((resolve) => {
  console.log("2: executor (synchronous)");
  resolve("done");
});
p.then((v) => console.log(`4: .then (${v})`));
console.log("3: after");
// Output: 1: before → 2: executor → 3: after → 4: .then (done)
```

**The same applies to async functions**: code before the first `await` runs synchronously:

```js
async function f() {
  console.log("2: sync part");
  const x = await Promise.resolve("value");
  console.log(`4: after await (${x})`);
}
console.log("1: before");
f();
console.log("3: after f() call");
// Output: 1 → 2 → 3 → 4
```

**Rationale**: This guarantee eliminates race conditions between Promise creation and settlement observation. Results are never delivered synchronously, even for already-settled Promises (Exploring JS Ch. 43; Deep JS Ch. 19).

---

## ID-06: "Resolving" vs "Fulfilling" — Resolution Can Lock-In to Another Promise

**Strength**: SHOULD

**Summary**: `resolve(value)` fulfills the Promise. `resolve(anotherPromise)` locks-in to that Promise's fate — which may still be pending.

```js
// resolve(nonPromise) → fulfills immediately
const p1 = new Promise((resolve) => resolve(42));
// p1 is fulfilled with 42

// resolve(promise) → locks in; adopts the other's state
const p2 = new Promise((resolve) => resolve(Promise.reject("oops")));
// p2 is REJECTED with "oops" — not fulfilled with a rejected Promise

// resolve(pendingPromise) → p3 is pending until inner settles
const inner = new Promise((resolve) => setTimeout(() => resolve("delayed"), 1000));
const p3 = new Promise((resolve) => resolve(inner));
// p3 is pending for 1 second, then fulfilled with "delayed"
```

**Key implications**:
- `resolve(Promise.reject(err))` produces a **rejected** Promise, not a fulfilled one
- Returning a Promise from `.then()` or `async` flattens automatically — no `Promise<Promise<T>>` nesting
- `reject()` does NOT flatten — it always rejects with the exact argument

**Rationale**: The resolve/fulfill distinction explains Promise flattening, which is why `async` functions never return nested Promises. Understanding this prevents the common misconception that `resolve()` always means success (Exploring JS Ch. 43; Deep JS Ch. 19).

---

## ID-07: `Promise.withResolvers()` for External Settlement Control

**Strength**: SHOULD

**Summary**: ES2024. Breaks `resolve`/`reject` out of the constructor executor so they can be stored and called from anywhere.

```js
// Good — deferred pattern
const { promise, resolve, reject } = Promise.withResolvers();

// resolve/reject can be called from anywhere, not just inside the executor
setTimeout(() => resolve("delayed value"), 1000);

const result = await promise; // "delayed value"

// Good — queue implementation
class AsyncQueue {
  #queue = [];
  #waiters = [];

  enqueue(value) {
    if (this.#waiters.length > 0) {
      this.#waiters.shift().resolve(value);
    } else {
      this.#queue.push(value);
    }
  }

  dequeue() {
    if (this.#queue.length > 0) {
      return Promise.resolve(this.#queue.shift());
    }
    const { promise, resolve } = Promise.withResolvers();
    this.#waiters.push({ resolve });
    return promise;
  }
}
```

**Rationale**: The revealing constructor pattern (`new Promise((resolve, reject) => {...})`) confines `resolve`/`reject` to the executor. `Promise.withResolvers()` is the standard way to expose them for deferred patterns, queues, and event-driven settlement (Exploring JS Ch. 43).

---

## ID-08: `Promise.try()` for Uniform Sync/Async Error Handling

**Strength**: CONSIDER

**Summary**: ES2025. Starts a Promise chain from a callback that may throw synchronously or return a Promise.

```js
// Good — sync throw becomes rejection, async result forwarded
function loadConfig(path) {
  return Promise.try(() => {
    const raw = validatePath(path); // might throw synchronously
    return Deno.readTextFile(raw);   // returns a Promise
  });
}

// Without Promise.try() — sync throw escapes the chain
function loadConfig(path) {
  validatePath(path);               // if this throws, .catch() never sees it
  return Deno.readTextFile(path)
    .then(JSON.parse)
    .catch(handleError);
}
```

**When NOT needed**: Inside `async` functions, both sync throws and async rejections are caught by `try/catch` natively. `Promise.try()` is useful when writing raw Promise chains where the first step might throw synchronously.

**Rationale**: `Promise.try()` calls the callback immediately (same tick) unlike `Promise.resolve().then(cb)` which defers to a microtask. It ensures uniform error handling at the start of a chain (Exploring JS Ch. 43).

**Availability**: `Promise.try()` is ES2025 and very recent. Verify Deno support with `deno eval "Promise.try(() => 42).then(console.log)"` before relying on it. `Promise.withResolvers()` (ID-07, ES2024) and top-level `await` (ID-10, ES2022) have broader runtime support.

---

## ID-09: Wrapping Callback APIs with `new Promise()` — Promisification

**Strength**: SHOULD

**Summary**: Wrap callback-based APIs in `new Promise()` to integrate them into async/await code.

```js
// Good — promisified timer
function delay(ms) {
  return new Promise((resolve) => setTimeout(resolve, ms));
}
await delay(1000);

// Good — promisified event-based API with error handling
function waitForConnection(socket) {
  return new Promise((resolve, reject) => {
    socket.addEventListener("open", resolve, { once: true });
    socket.addEventListener("error", reject, { once: true });
  });
}
await waitForConnection(ws);

// Bad — wrapping an already-async function (anti-pattern)
function bad(url) {
  return new Promise((resolve, reject) => {
    fetch(url).then(resolve).catch(reject); // unnecessary wrapping
  });
}

// Good — just return the Promise directly
function good(url) {
  return fetch(url);
}
```

**Rationale**: Many legacy APIs use callbacks. Promisification converts them into Promises that work with `await`. Always handle both success and error paths — omitting `reject()` on the error path leaves the Promise pending forever. Never wrap an API that already returns a Promise (Exploring JS Ch. 43; JS Definitive Guide, §13.2.6).

**See also**: `03-error-handling.md` ID-18

---

## ID-10: Top-Level `await` in ESM

**Strength**: SHOULD

**Summary**: ES2022. Use `await` at the top level of a module without wrapping in an async function.

```js
// Good — top-level await for module initialization
const config = JSON.parse(await Deno.readTextFile("./config.json"));
export const db = await connectToDatabase(config.dbUrl);

// Good — dynamic import with fallback
let crypto;
try {
  crypto = await import("./fast-crypto.js");
} catch {
  crypto = await import("./fallback-crypto.js");
}
export { crypto };
```

**Key behavior**: Modules that import from a module with top-level `await` will wait for it to settle before executing. The importing module is not blocked — the event loop remains free.

**Rationale**: Top-level `await` eliminates the `async function main()` wrapper pattern. It is available only in ESM (not scripts). Use it for async initialization that must complete before the module's exports are meaningful (Exploring JS Ch. 42).

---

## ID-11: Async Functions Start Synchronously, Settle Asynchronously

**Strength**: MUST

**Summary**: Code before the first `await` runs synchronously in the caller's task. The returned Promise always settles asynchronously.

```js
async function process(data) {
  validate(data);               // runs synchronously — may throw synchronously
  const result = await transform(data);  // pauses here; caller gets Promise
  return result;
}

// Consequence: validation errors throw synchronously,
// but the caller always receives a Promise
const promise = process(input); // validate() runs NOW; transform() starts NOW
// promise settles later, in a microtask
```

**Rationale**: Understanding the sync-then-async boundary is essential for reasoning about execution order and error behavior. Pre-await validation runs eagerly — this is desirable for fail-fast behavior (Exploring JS Ch. 42; JS Definitive Guide, §13.3).

**See also**: `03-error-handling.md` ID-19

---

## ID-12: Async Infectiousness — Callers Must Handle Promises

**Strength**: SHOULD

**Summary**: An async function returns a Promise. Every caller that needs the result must be async itself or handle the Promise explicitly.

```js
// Async propagates up the call chain
async function getUser(id) { /* ... */ }
async function displayUser(id) {
  const user = await getUser(id); // must be async to await
  render(user);
}
async function main() {
  await displayUser(42); // must be async to await
}
main(); // entry point — or use top-level await

// Non-async caller must use .then()
function startApp() {
  displayUser(42).then(() => console.log("done"));
}
```

**Rationale**: Once any layer introduces async I/O, every layer above it that needs the result must be async. This is intrinsic to the model — "asynchronicity is contagious" (Rauschmayer). Async functions reduce the verbosity cost of this propagation compared to raw callbacks, but do not eliminate it (Exploring JS Ch. 42; Eloquent JS Ch. 11).

---

## ID-13: `Promise.all()` for Parallel Independent Operations

**Strength**: MUST

**Summary**: Start independent async operations concurrently and wait for all to complete.

```js
// Good — parallel: both fetches run concurrently
const [users, posts] = await Promise.all([
  fetch("/api/users").then((r) => r.json()),
  fetch("/api/posts").then((r) => r.json()),
]);

// Bad — sequential: second fetch waits for first to complete
const users = await fetch("/api/users").then((r) => r.json());
const posts = await fetch("/api/posts").then((r) => r.json());
```

**Key behavior**: `Promise.all()` does not *make* operations parallel — it waits for operations that are *already running*. Concurrency is determined by when operations start, not by `Promise.all()`. It short-circuits on the first rejection.

**Rationale**: Sequential `await` on independent operations is a performance anti-pattern — it serializes operations that could overlap. `Promise.all()` is the fork-join primitive (Exploring JS Ch. 43; JS Definitive Guide, §13.2.5).

**See also**: `03-error-handling.md` ID-21 (error behavior of `Promise.all()`)

---

## ID-14: `Promise.allSettled()` for Partial-Success Scenarios

**Strength**: SHOULD

**Summary**: Wait for all operations to complete, regardless of individual failures. Never rejects.

```js
const results = await Promise.allSettled([
  fetch("/api/users"),
  fetch("/api/posts"),
  fetch("/api/comments"),
]);

for (const result of results) {
  if (result.status === "fulfilled") {
    processResponse(result.value);
  } else {
    console.warn("Failed:", result.reason.message);
  }
}
```

For error-handling details (when to use `allSettled` vs `all`, result shape), see `03-error-handling.md` ID-16.

**Rationale**: `Promise.all()` aborts on the first failure, discarding partial results. `Promise.allSettled()` always fulfills with a complete array of outcomes — essential for batch operations, health checks, and multi-source fetches (Exploring JS Ch. 43).

---

## ID-15: `Promise.any()` for First-Success / Redundancy

**Strength**: CONSIDER

**Summary**: Fulfills with the first successful result. Only rejects when *all* inputs reject.

```js
// Good — try multiple CDN mirrors, take the first success
const content = await Promise.any([
  fetch("https://cdn1.example.com/data.json").then((r) => r.text()),
  fetch("https://cdn2.example.com/data.json").then((r) => r.text()),
]);
```

For error handling (AggregateError on total failure), see `03-error-handling.md` ID-17.

**Rationale**: `Promise.any()` ignores individual rejections as long as at least one input fulfills — the inverse of `Promise.all()`. Useful for redundant sources and fallback strategies (Exploring JS Ch. 43).

---

## ID-16: `Promise.race()` for First-Settlement Patterns

**Strength**: SHOULD

**Summary**: Settles with the first Promise to settle — fulfillment or rejection. Useful for first-response-wins and legacy timeout patterns.

```js
// Good — first response wins from multiple sources
const fastest = await Promise.race([
  fetch("https://api-east.example.com/data"),
  fetch("https://api-west.example.com/data"),
]);

// Good — legacy timeout pattern (prefer AbortSignal.timeout() for new code — see ID-26)
function withTimeout(ms, promise) {
  return Promise.race([
    promise,
    new Promise((_, reject) =>
      setTimeout(() => reject(new Error(`Timed out after ${ms}ms`)), ms),
    ),
  ]);
}

// Gotcha: Promise.race([]) never settles — always pass at least one input
```

**Key behavior**: The losing Promises continue running — `Promise.race()` has no cancellation mechanism. For timeouts with true cancellation, use `AbortSignal.timeout()` (ID-26) instead.

**Note**: For most timeout use cases, `AbortSignal.timeout()` (ID-26) is the modern replacement — it integrates with `fetch()` and other Web APIs, and actually cancels the operation rather than just ignoring the result.

**Rationale**: `Promise.race()` reacts to the first settlement regardless of type. Contrast with `Promise.any()` which reacts only to fulfillments. Its primary modern use case is first-response-wins patterns; for timeouts, `AbortSignal.timeout()` is preferred (Exploring JS Ch. 43; JS Definitive Guide, §13.2.5).

---

## ID-17: Concurrency Limiting — Process N Items at a Time

**Strength**: SHOULD

**Summary**: When processing many items, limit concurrent operations to avoid overwhelming resources.

```js
/**
 * Process items with at most `limit` operations in flight at once.
 * @template T, R
 * @param {T[]} items
 * @param {number} limit
 * @param {(item: T) => Promise<R>} fn
 * @returns {Promise<R[]>}
 */
async function mapWithLimit(items, limit, fn) {
  const results = new Array(items.length);
  let nextIndex = 0;

  async function worker() {
    while (nextIndex < items.length) {
      const i = nextIndex++;
      results[i] = await fn(items[i]);
    }
  }

  await Promise.all(Array.from({ length: limit }, () => worker()));
  return results;
}

// Good — process 100 URLs, 5 at a time
const responses = await mapWithLimit(urls, 5, async (url) => {
  const res = await fetch(url);
  return res.json();
});

// Bad — all 100 fetch at once (may exhaust connections, trigger rate limits)
const responses = await Promise.all(urls.map((url) => fetch(url)));
```

**Rationale**: `Promise.all(items.map(fn))` starts all operations immediately. For large sets or expensive I/O (network, file system), this can exhaust connections, trigger rate limits, or cause memory pressure. A worker-pool pattern limits concurrency to N simultaneous operations. Note: the shared mutable `nextIndex` is safe because of run-to-completion (ID-01) — `nextIndex++` cannot be interrupted between read and increment within a single task (Exploring JS Ch. 43).

---

## ID-18: Sequential Async — When Order Matters

**Strength**: SHOULD

**Summary**: Use `for-of` with `await` when each operation depends on the previous or order must be preserved.

```js
// Good — sequential: each step depends on the previous
async function migrateDatabase(migrations) {
  for (const migration of migrations) {
    await migration.run(); // must complete before the next starts
    await migration.verify();
  }
}

// Good — sequential with accumulation
async function downloadAll(urls) {
  const results = [];
  for (const url of urls) {
    const res = await fetch(url);
    results.push(await res.json());
  }
  return results;
}
```

**When to use sequential vs parallel**:
- **Sequential**: Each step depends on the previous, or strict ordering is required (migrations, transactions)
- **Parallel**: Operations are independent (ID-13)
- **Limited parallel**: Independent but resource-constrained (ID-17)

**Rationale**: `await` inside `for-of` pauses the loop body until the Promise settles, then continues. This is the correct pattern for ordered, dependent operations (Exploring JS Ch. 42; JS Definitive Guide, §13.3.3).

---

## ID-19: `for await...of` for Consuming Async Iterables

**Strength**: SHOULD

**Summary**: `for await...of` iterates over async iterables, awaiting each value as it arrives.

```js
// Good — consuming an async generator
async function* fetchPages(baseUrl) {
  let page = 1;
  while (true) {
    const res = await fetch(`${baseUrl}?page=${page}`);
    if (!res.ok) break;
    const data = await res.json();
    if (data.items.length === 0) break;
    yield data.items;
    page++;
  }
}

for await (const items of fetchPages("/api/records")) {
  for (const item of items) {
    process(item);
  }
}

// Also works with ReadableStream (Web Streams)
const response = await fetch("/api/stream");
for await (const chunk of response.body) {
  handleChunk(chunk);
}
```

**Key behavior**: Sequential by design — waits for each item before requesting the next. This provides natural backpressure for stream-like sources.

**Rationale**: `for await...of` is the consumption counterpart to async generators. It prefers `Symbol.asyncIterator` if present, falling back to `Symbol.iterator`. Must be inside an `async` function or at module top level (Exploring JS Ch. 44; JS Definitive Guide, §13.4.1).

---

## ID-20: Async Generators for Producing Async Sequences

**Strength**: SHOULD

**Summary**: `async function*` combines `await` (input) with `yield` (output) to create async iterables.

```js
// Good — async generator for paginated API
async function* paginatedFetch(url) {
  let cursor = null;
  do {
    const res = await fetch(cursor ? `${url}?cursor=${cursor}` : url);
    const data = await res.json();
    yield* data.items;
    cursor = data.nextCursor;
  } while (cursor);
}

// Good — async generator for transformation pipeline
async function* filterAsync(source, predicate) {
  for await (const item of source) {
    if (await predicate(item)) yield item;
  }
}

// Good — async generator for rate-limited processing
async function* throttled(source, intervalMs) {
  for await (const item of source) {
    yield item;
    await new Promise((resolve) => setTimeout(resolve, intervalMs));
  }
}
```

**Rationale**: Async generators are the simplest way to implement custom async iterables. They eliminate manual async iterator state management and compose naturally with `for await...of` (Exploring JS Ch. 44; JS Definitive Guide, §13.4.3).

---

## ID-21: Async Mapping — `Promise.all(items.map(async fn))`

**Strength**: MUST

**Summary**: `.map(async fn)` returns `Promise[]`, not resolved values. Wrap with `Promise.all()` to get results.

```js
// Good — concurrent async map
const results = await Promise.all(
  items.map(async (item) => {
    const data = await fetchData(item.id);
    return transform(data);
  }),
);

// Bad — map returns Promises, not values
const results = items.map(async (item) => {
  return await fetchData(item.id);
});
// results is [Promise, Promise, ...] — not the resolved values!

// Bad — await inside map does not make map await
const results = items.map(async (item) => await fetchData(item.id));
console.log(results[0]); // Promise { <pending> }
```

**Rationale**: This is the most common async pitfall — `.map()` does not know about Promises. It returns an array of Promises, which must be explicitly awaited via `Promise.all()`. For sequential processing, use `for-of` (ID-18) (Exploring JS Ch. 42; JS Definitive Guide, §13.3.3).

**See also**: `03-error-handling.md` ID-22

---

## ID-22: Converting Async Iterables to Arrays

**Strength**: CONSIDER

**Summary**: Use `Array.fromAsync()` (ES2024) to collect an async iterable into an array.

```js
// Good — Array.fromAsync() (ES2024, supported in Deno)
const allItems = await Array.fromAsync(paginatedFetch("/api/records"));

// Good — with mapping function (like Array.from's second argument)
const names = await Array.fromAsync(userStream, (user) => user.name);

// Fallback — manual collection (for environments without Array.fromAsync)
async function toArray(asyncIterable) {
  const result = [];
  for await (const item of asyncIterable) {
    result.push(item);
  }
  return result;
}
```

**Rationale**: Spread (`[...asyncIterable]`) and `Array.from()` do not work with async iterables. `Array.fromAsync()` shipped in ES2024 and is supported in Deno — it is the standard approach. It accepts an optional mapping function as a second argument, mirroring `Array.from()` (Exploring JS Ch. 44).

---

## ID-23: `AbortController` / `AbortSignal` for Cancellation

**Strength**: SHOULD

**Summary**: Use `AbortController` to cancel async operations. Pass its `signal` to `fetch()` and other Web APIs.

```js
// Good — cancellable fetch
const controller = new AbortController();

const response = await fetch("/api/data", { signal: controller.signal });

// Cancel from elsewhere (e.g., user navigation, timeout)
controller.abort();
// The fetch rejects with an AbortError

// Good — cleanup pattern
try {
  const data = await fetch(url, { signal: controller.signal });
  return await data.json();
} catch (err) {
  if (err.name === "AbortError") {
    console.log("Request was cancelled");
    return null;
  }
  throw err; // re-throw non-cancellation errors
}
```

**Key facts**:
- `controller.abort()` sets `signal.aborted = true` and fires the `abort` event on the signal
- Multiple operations can share the same signal — aborting cancels all of them
- Once aborted, a signal stays aborted — it cannot be reset
- `AbortError` is distinguishable via `err.name === "AbortError"`

**Rationale**: `AbortController` is the Web Platform standard for cooperative cancellation. Without it, `fetch()` calls and other async operations have no way to be stopped — they run to completion even if the result is no longer needed. This is essential for production code with timeouts, navigation, and cleanup.

---

## ID-24: Pass `signal` to `fetch()` and Other Web APIs

**Strength**: MUST

**Summary**: Every `fetch()` call in production code should accept a signal for cancellation.

```js
// Good — signal passed to fetch
async function fetchData(url, { signal } = {}) {
  const response = await fetch(url, { signal });
  if (!response.ok) throw new Error(`HTTP ${response.status}`);
  return response.json();
}

// Good — composing signals
async function loadDashboard(signal) {
  const [users, metrics] = await Promise.all([
    fetchData("/api/users", { signal }),
    fetchData("/api/metrics", { signal }),
  ]);
  return { users, metrics };
}

// Caller controls cancellation
const controller = new AbortController();
loadDashboard(controller.signal);
// Later: controller.abort();  // cancels both fetches
```

**Rationale**: A `fetch()` without a signal cannot be cancelled — it continues consuming bandwidth and server resources even after the result is discarded. Threading signals through async functions enables coordinated cancellation across parallel operations.

---

## ID-25: Check `signal.aborted` in Long-Running Async Loops

**Strength**: SHOULD

**Summary**: For long-running async loops, check `signal.aborted` at each iteration to enable cooperative cancellation.

```js
// Good — check signal in loop
async function processAll(items, { signal } = {}) {
  const results = [];
  for (const item of items) {
    if (signal?.aborted) {
      throw new DOMException("Operation cancelled", "AbortError");
    }
    results.push(await processItem(item));
  }
  return results;
}

// Good — listen for abort event for cleanup
async function longOperation(signal) {
  signal?.addEventListener("abort", () => {
    cleanup();
  }, { once: true });

  for await (const chunk of dataSource) {
    if (signal?.aborted) break;
    await processChunk(chunk);
  }
}
```

**Rationale**: `fetch()` checks the signal internally, but custom async loops do not. Without explicit `signal.aborted` checks, a loop continues processing even after cancellation. The check should be at the top of each iteration — cooperative, not preemptive.

---

## ID-26: `AbortSignal.timeout()` for Deadline-Based Cancellation

**Strength**: SHOULD

**Summary**: `AbortSignal.timeout(ms)` creates a signal that auto-aborts after the specified duration — no manual timer needed.

```js
// Good — 5-second timeout on fetch, no manual setTimeout/AbortController
const response = await fetch("/api/slow", {
  signal: AbortSignal.timeout(5000),
});

// Good — compose with other signals using AbortSignal.any()
const controller = new AbortController();
const signal = AbortSignal.any([
  controller.signal,           // manual cancellation
  AbortSignal.timeout(10000),  // 10-second deadline
]);

const data = await fetch("/api/data", { signal });
```

**`AbortSignal.any()`** creates a derived signal that aborts when **any** of its input signals abort. This enables composing multiple cancellation sources — a manual abort button, a timeout, and a navigation event can all feed into one signal that cancels the operation when any trigger fires.

**Rationale**: `AbortSignal.timeout()` replaces the `Promise.race()` + `setTimeout` timeout pattern (ID-16) with a cleaner, more composable API. It works with any API that accepts a signal, not just Promises. Combined with `AbortSignal.any()`, multiple cancellation sources compose into a single signal.

---

## ID-27: Web Streams — `ReadableStream`, `WritableStream`, `TransformStream`

**Strength**: SHOULD

**Summary**: Deno uses the Web Streams API for streaming I/O. Use it for efficient, composable data pipelines.

```js
// Good — streaming HTTP response in Deno
Deno.serve((_req) => {
  let count = 0;
  const body = new ReadableStream({
    pull(controller) {
      if (count >= 5) {
        controller.close();
        return;
      }
      controller.enqueue(`chunk ${count++}\n`);
    },
  });

  return new Response(
    body.pipeThrough(new TextEncoderStream()),
    { headers: { "content-type": "text/plain" } },
  );
});

// Good — consuming a stream with for await
const response = await fetch("/api/stream");
for await (const chunk of response.body) {
  process(chunk);
}
```

**Three stream types**:
- `ReadableStream` — data source (pull or push model)
- `WritableStream` — data sink
- `TransformStream` — readable + writable pair with transformation between them

**Rationale**: Web Streams are the standard streaming API in Deno and browsers. They handle backpressure automatically, compose via `.pipeThrough()` and `.pipeTo()`, and integrate with `for await...of` (JS Definitive Guide, §16.5; Deno docs).

---

## ID-28: `.pipeThrough()` and `.pipeTo()` for Stream Composition

**Strength**: SHOULD

**Summary**: Chain transforms with `.pipeThrough()` and direct output with `.pipeTo()`.

```js
// Good — pipeline: read → decompress → decode → process
const response = await fetch("/api/compressed-data");

const textStream = response.body
  .pipeThrough(new DecompressionStream("gzip"))
  .pipeThrough(new TextDecoderStream());

for await (const text of textStream) {
  process(text);
}

// Good — pipe readable to writable
const source = (await fetch("/api/data")).body;
const file = await Deno.open("output.bin", { write: true, create: true });
await source.pipeTo(file.writable);

// Good — custom transform
const upper = new TransformStream({
  transform(chunk, controller) {
    controller.enqueue(chunk.toUpperCase());
  },
});

const upperStream = textStream.pipeThrough(upper);
```

**Rationale**: `.pipeThrough()` takes a `TransformStream` and returns a new `ReadableStream`, enabling composable pipelines. `.pipeTo()` sends a `ReadableStream` to a `WritableStream` and returns a Promise that settles when the pipe completes. Both handle backpressure automatically (JS Definitive Guide, §16.5).

---

## ID-29: Backpressure — Streams Handle It Automatically

**Strength**: CONSIDER

**Summary**: The Web Streams API manages backpressure internally. The consumer's read speed controls the producer's output rate.

```js
// Good — backpressure is automatic with pipeTo/pipeThrough
const response = await fetch("/api/large-file");
const file = await Deno.open("output.bin", { write: true, create: true });
await response.body.pipeTo(file.writable);
// If the file write is slower than the network, the fetch slows down automatically

// Good — pull-based ReadableStream: pull() is only called when consumer is ready
const stream = new ReadableStream({
  pull(controller) {
    // Called only when the consumer requests data
    controller.enqueue(generateNextChunk());
  },
});
```

**Rationale**: Without backpressure, a fast producer overwhelms a slow consumer, causing unbounded memory growth. The Web Streams API's pull model and automatic flow control prevent this. `.pipeTo()` and `.pipeThrough()` handle backpressure correctly without manual intervention (JS Definitive Guide, §16.5).

---

## ID-30: Web Workers for CPU-Intensive Work Off the Main Thread

**Strength**: CONSIDER

**Summary**: Offload CPU-bound computation to Workers. Communicate via `postMessage` — no shared state.

```js
// main.js — spawn a worker
const worker = new Worker(new URL("./worker.js", import.meta.url).href, {
  type: "module",
  deno: { permissions: "inherit" }, // explicit: inherit parent's permissions
});

worker.postMessage({ data: largeDataSet });
worker.addEventListener("message", (event) => {
  console.log("Result:", event.data);
});

// worker.js — isolated environment, no DOM, no shared globals
self.addEventListener("message", async (event) => {
  const result = heavyComputation(event.data);
  self.postMessage(result);
});
```

**Key constraints**:
- Workers run in an isolated environment — no shared variables, no DOM
- Communication via `postMessage` using structured clone (deep copy)
- `Transferable` objects (typed arrays, `MessagePort`) can be zero-copy transferred
- In Deno, Workers must use `type: "module"`. By default, Workers get **no permissions** — you must explicitly grant them via the `deno.permissions` option (`"inherit"` to match parent, or a specific permission object)

**When to use Workers**: Image processing, data parsing, cryptography, any computation >50ms that would freeze the event loop. Not a replacement for async I/O patterns.

**Rationale**: Workers are the only way to run CPU-intensive code without blocking the main thread. Message passing eliminates shared-state bugs at the cost of serialization overhead. For most I/O-bound async work, `await` is sufficient (Exploring JS Ch. 42; JS Definitive Guide, §15.13).

---

## ID-31: `setTimeout` / `setInterval` Are Macrotasks

**Strength**: SHOULD

**Summary**: Timer callbacks are macrotasks. They run after all pending microtasks, with a minimum (not guaranteed) delay.

```js
// setTimeout delay is a minimum, not a guarantee
setTimeout(() => console.log("at least 100ms later"), 100);

// Good — promisified delay for use with await
const delay = (ms) => new Promise((resolve) => setTimeout(resolve, ms));
await delay(1000);

// setInterval — remember to clear it
const id = setInterval(() => { /* ... */ }, 1000);
clearInterval(id); // always clean up

// Common mistake: setTimeout(fn, 0) does NOT run "immediately"
// It runs after all pending microtasks and the current task
```

**Rationale**: Timer callbacks are enqueued as macrotasks. `setTimeout(fn, 0)` does not mean "run now" — it means "run in the next macrotask cycle, after all microtasks drain." Understanding this prevents ordering bugs when mixing timers with Promise chains (Exploring JS Ch. 42; Eloquent JS Ch. 11).

---

## ID-32: Debouncing and Throttling for Rate-Limited Execution

**Strength**: SHOULD

**Summary**: Debounce fires after a pause in events. Throttle fires at regular intervals during events.

```js
// Good — debounce: fire after events stop for `wait` ms
function debounce(fn, wait) {
  let timer;
  return (...args) => {
    clearTimeout(timer);
    timer = setTimeout(() => fn(...args), wait);
  };
}

const search = debounce(async (query) => {
  const results = await fetch(`/api/search?q=${query}`);
  displayResults(await results.json());
}, 300);

input.addEventListener("input", (e) => search(e.target.value));

// Good — throttle: fire at most once every `interval` ms
function throttle(fn, interval) {
  let lastEvent = null;
  let timer = null;
  return (...args) => {
    lastEvent = args;
    if (timer === null) {
      timer = setTimeout(() => {
        fn(...lastEvent);
        timer = null;
      }, interval);
    }
  };
}

const trackMouse = throttle((x, y) => {
  updateCursor(x, y);
}, 100);

document.addEventListener("mousemove", (e) => trackMouse(e.pageX, e.pageY));
```

| Pattern | Fires when | Use case |
|---------|-----------|----------|
| **Debounce** | Events stop for `wait` ms | Search-as-you-type, auto-save, resize handler |
| **Throttle** | At most once per `interval` | Scroll handler, mouse tracking, rate-limited API calls |

**Rationale**: Without rate limiting, rapid events (keystrokes, scroll, resize) trigger expensive operations on every event. Debouncing waits for the burst to end; throttling ensures regular periodic updates. Both use `setTimeout` under the hood (Eloquent JS Ch. 15).

---

## Best Practices Summary

### Quick Reference Table

| ID | Pattern | Strength | Key Insight |
|----|---------|----------|-------------|
| 01 | Single-threaded, run-to-completion | MUST | No preemptive interruption; one task at a time |
| 02 | Microtasks before macrotasks | SHOULD | Promise callbacks drain before next setTimeout |
| 03 | Never block the event loop | MUST | Async I/O; Workers for CPU; no busy-wait |
| 04 | `queueMicrotask()` | CONSIDER | Microtask priority without creating a Promise |
| 05 | Promises: sync start, async settle | MUST | Executor runs now; `.then()` runs in next microtask |
| 06 | Resolving vs fulfilling | SHOULD | `resolve(promise)` locks-in; `resolve(value)` fulfills |
| 07 | `Promise.withResolvers()` | SHOULD | External settlement control (ES2024) |
| 08 | `Promise.try()` | CONSIDER | Uniform sync/async at chain start (ES2025) |
| 09 | Promisification | SHOULD | Wrap callback APIs; never double-wrap async APIs |
| 10 | Top-level `await` | SHOULD | No wrapper needed in ESM (ES2022) |
| 11 | Async start sync, settle async | MUST | Pre-await code runs eagerly in caller's task |
| 12 | Async infectiousness | SHOULD | Callers must be async or handle Promises |
| 13 | `Promise.all()` for parallel | MUST | Fork-join; short-circuits on first rejection |
| 14 | `Promise.allSettled()` | SHOULD | Partial success; never rejects → see 03 ID-16 |
| 15 | `Promise.any()` | CONSIDER | First success; AggregateError on total failure → see 03 ID-17 |
| 16 | `Promise.race()` for first-settlement | SHOULD | First-response-wins; for timeouts prefer ID-26 |
| 17 | Concurrency limiting | SHOULD | N-at-a-time worker pool; don't blast all at once |
| 18 | Sequential async with `for-of` | SHOULD | `await` inside loop pauses between iterations |
| 19 | `for await...of` | SHOULD | Consumes async iterables with natural backpressure |
| 20 | Async generators | SHOULD | `async function*` combines `await` + `yield` |
| 21 | `Promise.all(items.map(async fn))` | MUST | `.map()` returns `Promise[]`; must wrap with `all()` |
| 22 | Async iterable to array | CONSIDER | `Array.fromAsync()` (ES2024, supported in Deno) |
| 23 | `AbortController` / `AbortSignal` | SHOULD | Web Platform cancellation standard |
| 24 | Pass `signal` to `fetch()` | MUST | Every production fetch needs a signal |
| 25 | Check `signal.aborted` in loops | SHOULD | Cooperative cancellation for custom async loops |
| 26 | `AbortSignal.timeout()` | SHOULD | Auto-abort after deadline; composable with `.any()` |
| 27 | Web Streams API | SHOULD | ReadableStream, WritableStream, TransformStream |
| 28 | `.pipeThrough()` / `.pipeTo()` | SHOULD | Composable stream pipelines with auto-backpressure |
| 29 | Backpressure is automatic | CONSIDER | Pull model prevents unbounded memory growth |
| 30 | Web Workers for CPU work | CONSIDER | Isolated thread; message passing; no shared state |
| 31 | setTimeout/setInterval = macrotasks | SHOULD | Run after microtasks; delay is a minimum |
| 32 | Debouncing and throttling | SHOULD | Rate-limit rapid events; debounce vs throttle |

### Promise Combinator Decision Table

| Question | Use |
|----------|-----|
| Need ALL results, fail if any fail | `Promise.all()` |
| Need ALL outcomes, partial failure OK | `Promise.allSettled()` |
| Need FIRST success, ignore individual failures | `Promise.any()` |
| Need FIRST settlement (timeout pattern) | `Promise.race()` |

---

## Related Guidelines

- **Core Idioms**: See `01-core-idioms.md` for `for-of` vs `.forEach()` (ID-25), `??` (ID-03), `?.` (ID-04)
- **API Design**: See `02-api-design.md` for async function return conventions (ID-25), Promise-only APIs (ID-25 here cross-refs ID-25 there)
- **Error Handling**: See `03-error-handling.md` for async error patterns (ID-13–22, ID-27–28 there) — this guide cross-references those by ID at each overlap point
- **Values & References**: See `04-values-references.md` for mutation discipline in async contexts (ID-12–14)
- **Functions & Closures**: See `06-functions-closures.md` for closure capture in callbacks (ID-06–10), generators (ID-05), and `this` binding (ID-16–18)
- **Performance**: See `08-performance.md` for lazy evaluation (ID-14–15) and allocation discipline (ID-24)
- **Anti-Patterns**: See `09-anti-patterns.md` for ID-18, 19, 20, 21, 22, 23 (async anti-patterns)
- **Deno**: See `12-deno/01-runtime-basics.md` for Deno-specific async APIs

---

## External References

- [Deno Manual](https://docs.deno.com/)
- [MDN — AbortController](https://developer.mozilla.org/en-US/docs/Web/API/AbortController)
- [MDN — Streams API](https://developer.mozilla.org/en-US/docs/Web/API/Streams_API)
- [MDN — Web Workers](https://developer.mozilla.org/en-US/docs/Web/API/Web_Workers_API)
- *Exploring JavaScript* (ES2025) — Axel Rauschmayer
- *Deep JavaScript* — Axel Rauschmayer
- *JavaScript: The Definitive Guide* (7th ed.) — David Flanagan
- *Eloquent JavaScript* (4th ed.) — Marijn Haverbeke
