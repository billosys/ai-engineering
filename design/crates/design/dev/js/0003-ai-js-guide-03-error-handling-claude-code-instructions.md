# ai-js Guide 03: Error Handling — Claude Code Instructions

## Context

We're building `ai-js`, a repo of curated JavaScript guides that Claude
Code reads via a SKILL.md entry point to produce consistently high-quality
JS code. This is modeled on our `ai-rust` repo.

Guides 01 (Core Idioms) and 02 (API Design) are complete. Now we're
writing Guide 03: Error Handling.

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

**Error fundamentals**:
- `exploring-js/error-class.md`
- `exploring-js/error-subclasses.md`
- `exploring-js/error-chaining.md`
- `exploring-js/throw-statement.md`
- `exploring-js/try-catch-finally.md`
- `exploring-js/finally-clause.md`
- `exploring-js/stack-trace.md`
- `exploring-js/omitting-catch-binding.md`
- `deep-js/promise-exception-handling.md`
- `js-definitive-guide/throw-statement.md`
- `js-definitive-guide/try-catch-finally.md`
- `js-definitive-guide/error-classes.md`
- `eloquent-js/exception.md`
- `eloquent-js/selective-catching.md`
- `eloquent-js/error-propagation.md`
- `eloquent-js/stack-trace.md`

**Custom errors**:
- `exploring-js/error-subclasses.md`
- `exploring-js/error-chaining.md`
- `exploring-js/aggregate-error.md`
- `js-definitive-guide/error-classes.md`

**Promise error handling**:
- `exploring-js/promise.md`
- `exploring-js/promise-states.md`
- `exploring-js/promise-error-handling.md`
- `exploring-js/promise-catch.md`
- `exploring-js/promise-finally.md`
- `exploring-js/promise-chaining.md`
- `exploring-js/promise-chaining-mistakes.md`
- `exploring-js/promise-all.md`
- `exploring-js/promise-all-settled.md`
- `exploring-js/promise-any.md`
- `exploring-js/promise-race.md`
- `exploring-js/promise-combinator-functions.md`
- `exploring-js/promise-short-circuiting.md`
- `exploring-js/promise-try.md`
- `deep-js/promise.md`
- `deep-js/promise-state.md`
- `deep-js/promise-chaining.md`
- `deep-js/promise-exception-handling.md`
- `deep-js/promise-flattening.md`
- `deep-js/promise-reaction-passthrough.md`
- `deep-js/rejection-value.md`
- `deep-js/rejection-reaction.md`
- `deep-js/fulfillment-reaction.md`
- `deep-js/catch-method.md`
- `deep-js/then-method.md`
- `deep-js/revealing-constructor-pattern.md`
- `js-definitive-guide/promise-object.md`
- `js-definitive-guide/promise-states.md`
- `js-definitive-guide/promise-chaining.md`
- `js-definitive-guide/promise-catch.md`
- `js-definitive-guide/promise-all.md`
- `js-definitive-guide/promise-all-settled.md`
- `js-definitive-guide/promise-race.md`
- `js-definitive-guide/promise-resolve-reject.md`
- `eloquent-js/promise.md`
- `eloquent-js/reject.md`
- `eloquent-js/resolve.md`
- `eloquent-js/then-method.md`
- `eloquent-js/catch-method.md`
- `eloquent-js/promise-constructor.md`

**Async/await error handling**:
- `exploring-js/async-function.md`
- `exploring-js/async-function-error-handling.md`
- `exploring-js/async-function-return-semantics.md`
- `exploring-js/awaiting-is-shallow.md`
- `exploring-js/return-await.md`
- `exploring-js/fire-and-forget.md`
- `js-definitive-guide/async-functions.md`
- `js-definitive-guide/await-expressions.md`
- `js-definitive-guide/async-error-handling.md`
- `js-definitive-guide/sequential-vs-parallel-await.md`
- `eloquent-js/async-function.md`
- `eloquent-js/await-keyword.md`
- `eloquent-js/error-handling-in-async.md`
- `eloquent-js/asynchronous-bugs.md`

**Type coercion and silent failures**:
- `exploring-js/silent-failures.md`
- `exploring-js/type-coercion.md`
- `exploring-js/undefined-value.md`
- `exploring-js/null-value.md`
- `exploring-js/checking-for-undefined-or-null.md`
- `deep-js/type-coercion.md`
- `deep-js/to-number.md`
- `deep-js/to-string.md`
- `deep-js/to-boolean.md`

**Error-first callbacks** (for understanding the pattern we're replacing):
- `js-definitive-guide/error-first-callbacks.md`
- `js-definitive-guide/callback-hell.md`
- `js-definitive-guide/callback-pattern.md`
- `eloquent-js/callback.md`

**Assertions and validation**:
- `exploring-js/assertions.md`
- `exploring-js/assert-equal.md`
- `exploring-js/assert-deep-equal.md`
- `exploring-js/assert-throws.md`
- `exploring-js/assert-fail.md`

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
or merge if redundant. Aim for 20-30 idioms.

**Throw discipline**:
1. Always throw `Error` objects, never strings or plain values (MUST)
2. Use `throw` for exceptional conditions, not control flow (MUST)
3. Include context in error messages — what failed and why (MUST)
4. Use `Error.cause` for error chaining (SHOULD)

**Custom errors**:
5. Subclass `Error` for domain-specific error types (SHOULD)
6. Custom errors must set `name` to match the class name (MUST)
7. Use `AggregateError` for multiple simultaneous failures (CONSIDER)

**Catch discipline**:
8. Never write empty `catch` blocks — log, rethrow, or handle (MUST)
9. Catch specific errors, not everything — selective catching (SHOULD)
10. Re-throw unknown errors after catching known ones (MUST)
11. Use `finally` for cleanup, not for return values (SHOULD)
12. Omit the catch binding when you don't need it: `catch { }` (CONSIDER)

**Promise error handling**:
13. Always handle Promise rejections — no dangling Promises (MUST)
14. Prefer `async`/`await` with `try`/`catch` over `.then().catch()` chains (SHOULD)
15. Understand `.catch()` placement — it matters for chaining (MUST)
16. Use `Promise.allSettled()` when some failures are acceptable (SHOULD)
17. Use `Promise.any()` with `AggregateError` for first-success patterns (CONSIDER)
18. Never mix callbacks and Promises in the same API (MUST)

**Async/await error patterns**:
19. `return await` inside `try` — when it matters and when it doesn't (MUST)
20. Beware fire-and-forget async calls — rejections are silently lost (MUST)
21. Parallel `await` — use `Promise.all()`, not sequential awaits (SHOULD)
22. Awaiting is shallow — nested Promises need explicit handling (SHOULD)

**Validation and defensive patterns**:
23. Validate at boundaries, trust within (SHOULD)
24. Fail fast — detect and throw on invalid input immediately (MUST)
25. Prefer returning `undefined` or `null` over throwing for "not found" (SHOULD)
26. Use assertions in tests, not in production code (SHOULD)

**Anti-patterns to flag**:
27. Never swallow errors silently (MUST)
28. Never use `try`/`catch` around synchronous code that can't throw (anti-pattern)
29. Never use exceptions for expected control flow (like "user not found") (SHOULD)
30. Avoid `Promise.reject()` in `async` functions — just `throw` (SHOULD)

## Output

Save as: `guides/03-error-handling.md` in the `ai-js` repo.

## Quality bar

- Every idiom must cite specific behavior described in the concept cards.
  Don't make claims the cards don't support.
- Code examples must be runnable under Deno (not Node.js).
- Good/bad examples should be realistic, not toy code.
- The tone should be terse and direct — this is a reference doc, not a
  tutorial. Match Guide 01's density and style.
- No Node.js imports or APIs in any examples.
- All cross-references must use the correct guide slugs from the list.
- Error handling in JS is a topic where many developers have strong
  opinions. Ground the guide in what the authoritative sources say,
  not in popular blog post advice.

## What NOT to do

- Don't invent idioms not supported by the concept card content
- Don't include Node.js-specific patterns (no `process.on('uncaughtException')`,
  no `util.callbackify`, no `EventEmitter` error patterns)
- Don't include React/Vue error boundary patterns
- Don't include TypeScript-specific patterns
- Don't duplicate content that belongs in other guides:
  - API return conventions → `02-api-design.md`
  - Mutation/copying discipline → `04-values-references.md`
  - Async concurrency patterns → `07-async-concurrency.md`
  - Common error handling mistakes → `09-anti-patterns.md`
- Don't include browser-specific error handling (window.onerror, etc.)
- Don't recommend Result/Either monads from functional programming
  unless the concept cards specifically support them — JS doesn't have
  native Result types, and bolting them on adds complexity without
  compiler support
