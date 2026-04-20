# ai-js Guide 07: Async & Concurrency — Claude Code Instructions

## Context

We're building `ai-js`, a repo of curated JavaScript guides that Claude
Code reads via a SKILL.md entry point to produce consistently high-quality
JS code. This is modeled on our `ai-rust` repo.

Guides 01–06 are complete or in progress. Now we're writing Guide 07:
Async & Concurrency.

This guide covers the full async landscape: the event loop, Promises,
async/await, async iteration, concurrency patterns, cancellation, and
streams. Guide 03 (Error Handling) already covers async error patterns
(try/catch in async, return await, fire-and-forget, Promise.allSettled,
etc.) — this guide should NOT re-teach those. Instead, this guide focuses
on the concurrency and orchestration patterns that make async JS correct
and efficient.

The target environment is:
- **Deno** (not Node.js — no `require()`, no `node_modules`, no npm scripts)
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

When concept cards from different sources conflict or present different
approaches, weight them in this order of importance:

1. `concept-cards/exploring-js/` — **MOST authoritative**. Rauschmayer,
   ES2025 edition. Spec-grounded, most current. Prefer this source's
   framing, terminology, and recommendations over all others.
2. `concept-cards/deep-js/` — Rauschmayer's deep-dive companion. Covers
   the "why" and internal mechanics. Defer to this for spec-level
   explanations of how things work under the hood.
3. `concept-cards/js-definitive-guide/` — Flanagan. Encyclopedic
   reference. Good for completeness and edge cases, but some patterns
   reflect pre-ES2020 conventions.
4. `concept-cards/eloquent-js/` — **LEAST authoritative** for API
   guidance. Haverbeke is pedagogical and excellent for beginners, but
   less precise on edge cases and modern idioms.

Tooling cards (`deno/`, `biome/`, `eslint/`) are authoritative for
their respective domains and don't conflict with the JS language sources.

### Concept cards to read for this guide

Read these cards before writing. This is not exhaustive — if you find
related cards while reading, use them too.

**Event loop and execution model**:
- `exploring-js/event-loop.md`
- `exploring-js/task-queue.md`
- `exploring-js/microtask-queue.md`
- `exploring-js/run-to-completion.md`
- `exploring-js/synchronous-function-execution.md`
- `exploring-js/blocking-the-javascript-process.md`
- `exploring-js/asynchronous-programming-overview.md`
- `deep-js/task-queue.md`
- `deep-js/microtask.md`
- `js-definitive-guide/node-programming-model.md`
- `eloquent-js/asynchronous-programming.md`
- `eloquent-js/synchronous-execution.md`

**Promises — core mechanics**:
- `exploring-js/promise.md`
- `exploring-js/promise-states.md`
- `exploring-js/promise-advantages.md`
- `exploring-js/promise-sync-start-async-settle.md`
- `exploring-js/promise-constructor.md`
- `exploring-js/promise-resolve-reject.md`
- `exploring-js/resolving-vs-fulfilling.md`
- `exploring-js/thenables.md`
- `exploring-js/promise-try.md`
- `exploring-js/promisification.md`
- `deep-js/promise.md`
- `deep-js/promise-state.md`
- `deep-js/promise-based-constructor.md`
- `deep-js/revealing-constructor-pattern.md`
- `deep-js/promise-flattening.md`
- `deep-js/lock-in-state.md`
- `deep-js/fulfillment-value.md`
- `deep-js/fulfillment-reaction.md`
- `deep-js/rejection-value.md`
- `deep-js/rejection-reaction.md`
- `deep-js/promise-reaction-passthrough.md`
- `deep-js/promise-resolution.md`
- `deep-js/thenable.md`
- `deep-js/subclassing-promise-based-constructor.md`
- `js-definitive-guide/promise-object.md`
- `js-definitive-guide/promise-states.md`
- `js-definitive-guide/promise-resolve-reject.md`
- `eloquent-js/promise.md`
- `eloquent-js/promise-constructor.md`
- `eloquent-js/resolve.md`
- `eloquent-js/reject.md`

**Promise chaining and combinators**:
- `exploring-js/promise-chaining.md`
- `exploring-js/promise-chaining-mistakes.md`
- `exploring-js/promise-catch.md`
- `exploring-js/promise-finally.md`
- `exploring-js/promise-all.md`
- `exploring-js/promise-all-settled.md`
- `exploring-js/promise-any.md`
- `exploring-js/promise-race.md`
- `exploring-js/promise-combinator-functions.md`
- `exploring-js/promise-short-circuiting.md`
- `exploring-js/promise-concurrency.md`
- `exploring-js/promise-with-resolvers.md`
- `deep-js/promise-chaining.md`
- `deep-js/then-method.md`
- `deep-js/catch-method.md`
- `deep-js/promise-exception-handling.md`
- `js-definitive-guide/promise-chaining.md`
- `js-definitive-guide/promise-all.md`
- `js-definitive-guide/promise-all-settled.md`
- `js-definitive-guide/promise-race.md`
- `js-definitive-guide/promise-catch.md`
- `eloquent-js/then-method.md`
- `eloquent-js/catch-method.md`

**Async/await**:
- `exploring-js/async-function.md`
- `exploring-js/async-function-return-semantics.md`
- `exploring-js/async-function-error-handling.md`
- `exploring-js/async-function-vs-asynchronous-function.md`
- `exploring-js/async-callable-entities.md`
- `exploring-js/await-operator.md`
- `exploring-js/await-concurrency.md`
- `exploring-js/awaiting-is-shallow.md`
- `exploring-js/return-await.md`
- `exploring-js/top-level-await.md`
- `exploring-js/fire-and-forget.md`
- `exploring-js/async-function-start-sync-settle-async.md`
- `exploring-js/async-code-infectiousness.md`
- `js-definitive-guide/async-functions.md`
- `js-definitive-guide/await-expressions.md`
- `js-definitive-guide/async-error-handling.md`
- `js-definitive-guide/sequential-vs-parallel-await.md`
- `eloquent-js/async-function.md`
- `eloquent-js/await-keyword.md`
- `eloquent-js/error-handling-in-async.md`
- `eloquent-js/asynchronous-bugs.md`

**Async iteration**:
- `exploring-js/async-iteration-protocol.md`
- `exploring-js/for-await-of.md`
- `exploring-js/for-await-of-loop.md`
- `exploring-js/async-generator.md`
- `exploring-js/async-generator-mapping.md`
- `exploring-js/async-iterable-to-array.md`
- `exploring-js/async-iteration-node-streams.md`
- `exploring-js/async-map-pattern.md`
- `exploring-js/async-tests.md`
- `js-definitive-guide/async-iterators.md`
- `js-definitive-guide/for-await-loop.md`
- `js-definitive-guide/async-generators.md`
- `js-definitive-guide/async-iteration-streams.md`
- `eloquent-js/async-iteration.md`

**Streams**:
- `js-definitive-guide/readable-streams.md`
- `js-definitive-guide/writable-streams.md`
- `js-definitive-guide/duplex-transform-streams.md`
- `js-definitive-guide/stream-backpressure.md`
- `js-definitive-guide/node-streams.md`
- `eloquent-js/stream.md`

**Web Workers and concurrency primitives**:
- `exploring-js/web-workers.md`
- `exploring-js/shared-array-buffer.md`
- `js-definitive-guide/web-workers.md`
- `js-definitive-guide/postmessage.md`
- `js-definitive-guide/sharedarraybuffer-atomics.md`
- `eloquent-js/web-worker.md`

**Timers and scheduling**:
- `exploring-js/set-timeout.md`
- `exploring-js/callback-pattern.md`
- `exploring-js/event-pattern.md`
- `js-definitive-guide/server-sent-events.md`
- `eloquent-js/timer.md`
- `eloquent-js/debouncing.md`
- `eloquent-js/throttling.md`

**Deno-specific async**:
- `deno/deno-http-server.md`
- `deno/deno-serve.md`
- `deno/deno-api-overview.md`
- `deno/deno-web-platform-apis.md`
- `deno/web-platform-apis.md`

## Structural template

Follow the same format as `guides/01-core-idioms.md`:

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
- Related Guidelines (using correct guide slugs from the list above)
- External References

## Proposed idiom list

This is a starting outline — adjust based on what the concept cards
emphasize. Add idioms if the cards reveal important patterns. Remove
or merge if redundant. Aim for 25-35 idioms.

**Event loop mental model**:
1. JavaScript is single-threaded — one call stack, run to completion (MUST)
2. Microtasks (Promises) run before macrotasks (setTimeout) (SHOULD)
3. Never block the event loop — no synchronous I/O, no long computation (MUST)
4. `queueMicrotask()` for immediate async scheduling (CONSIDER)

**Promise fundamentals**:
5. Promises start synchronously, settle asynchronously (MUST)
6. "Resolving" vs "fulfilling" — resolution can lock-in to another Promise (SHOULD)
7. Promise.withResolvers() for external settlement control (SHOULD)
8. Promise.try() for uniform error handling of sync-or-async functions (CONSIDER)
9. Wrapping callback APIs with `new Promise()` — promisification (SHOULD)

**Async/await patterns**:
10. Prefer `async`/`await` over raw `.then()` chains (SHOULD — references 03 ID-14)
11. Top-level `await` in ESM — no wrapper needed (SHOULD)
12. `async` functions start synchronously, settle asynchronously (MUST)
13. Async function infectiousness — callers must also be async or handle Promises (SHOULD)

**Concurrency orchestration**:
14. `Promise.all()` for parallel independent operations (MUST)
15. `Promise.allSettled()` for partial-success scenarios (SHOULD — references 03 ID-16)
16. `Promise.any()` for first-success / redundancy (CONSIDER — references 03 ID-17)
17. `Promise.race()` for timeout patterns (SHOULD)
18. Concurrency limiting — process N items at a time, not all at once (SHOULD)
19. Sequential async — when order matters (SHOULD)

**Async iteration**:
20. `for await...of` for consuming async iterables (SHOULD)
21. Async generators for producing async sequences (SHOULD)
22. Async mapping — `Promise.all(items.map(async fn))` pattern (MUST)
23. Converting async iterables to arrays (CONSIDER)

**Cancellation**:
24. `AbortController` / `AbortSignal` for cancellation (SHOULD)
25. Passing `signal` to `fetch()` and other Web APIs (MUST)
26. Checking `signal.aborted` in long-running async loops (SHOULD)
27. `AbortSignal.timeout()` for deadline-based cancellation (SHOULD)

**Streams**:
28. Web Streams API — `ReadableStream`, `WritableStream`, `TransformStream` (SHOULD)
29. `.pipeThrough()` and `.pipeTo()` for stream composition (SHOULD)
30. Backpressure — the stream API handles it automatically (CONSIDER)

**Workers and parallelism**:
31. Web Workers for CPU-intensive work off the main thread (CONSIDER)
32. `postMessage` / `onmessage` for worker communication (CONSIDER)
33. `SharedArrayBuffer` and `Atomics` for shared memory (CONSIDER)

**Timers and scheduling**:
34. `setTimeout` / `setInterval` — understand they are macrotasks (SHOULD)
35. Debouncing and throttling for rate-limited execution (SHOULD)

## Boundary with Guide 03 (Error Handling)

Guide 03 already covers these async error topics in detail:
- `return await` inside `try` (03 ID-19)
- Fire-and-forget rejections (03 ID-20)
- Parallel await with `Promise.all()` error behavior (03 ID-21)
- Awaiting is shallow / `.map(async fn)` returns `Promise[]` (03 ID-22)
- `Promise.allSettled()` for partial success (03 ID-16)
- `Promise.any()` with `AggregateError` (03 ID-17)
- Never mix callbacks and Promises (03 ID-18)
- `throw` vs `Promise.reject()` in async functions (03 ID-28)

**Do NOT re-teach these.** Cross-reference them. This guide should
cover the *concurrency and orchestration* aspects of async, not the
error-handling aspects.

## Output

Save as: `guides/07-async-concurrency.md` in the `ai-js` repo.

## Quality bar

- Every idiom must cite specific behavior described in the concept cards.
  Don't make claims the cards don't support.
- Code examples must be runnable under Deno (not Node.js).
- Good/bad examples should be realistic, not toy code.
- The tone should be terse and direct — this is a reference doc, not a
  tutorial. Match Guide 01's density and style.
- No Node.js imports or APIs in any examples. Use `Deno.readTextFile`,
  `fetch()`, `Deno.serve()`, etc.
- All cross-references must use the correct guide slugs from the list.
- The event loop section must be precise about the microtask/macrotask
  distinction — this is where most async mental models break down.
- The cancellation section (AbortController) is critical for modern
  async JS. The concept cards may not cover it deeply — supplement
  with Deno docs cards if needed. This pattern is essential for
  production code.

## What NOT to do

- Don't invent idioms not supported by the concept card content
- Don't include Node.js-specific patterns (no `EventEmitter`, no
  `process.nextTick()`, no Node streams — use Web Streams)
- Don't include React/Vue patterns (no `useEffect`, no `Suspense`)
- Don't include TypeScript-specific patterns
- Don't re-teach error handling patterns already in Guide 03 — just
  cross-reference them
- Don't duplicate content that belongs in other guides:
  - Async error handling → `03-error-handling.md`
  - Closure captures in async callbacks → `06-functions-closures.md`
  - Performance of async patterns → `08-performance.md`
- Don't include RxJS or other reactive library patterns — vanilla JS only
- Don't include callback-based patterns as recommended approaches —
  they are legacy. Mention promisification as a bridge, not as a
  destination.
- Don't over-emphasize Workers — they are a CONSIDER-level tool for
  most JS applications. The core of this guide is Promises, async/await,
  and async iteration.
