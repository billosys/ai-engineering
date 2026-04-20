# ai-js Guide 08: Performance — Claude Code Instructions

## Context

We're building `ai-js`, a repo of curated JavaScript guides that Claude
Code reads via a SKILL.md entry point to produce consistently high-quality
JS code. This is modeled on our `ai-rust` repo.

Guides 01–07 are complete. Now we're writing Guide 08: Performance.

This guide covers the performance patterns and anti-patterns that matter
in practice: data structure choices, allocation discipline, lazy
evaluation, caching, iteration efficiency, measurement, and — critically
— what NOT to micro-optimize. The goal is to help Claude Code generate
code that is both readable and efficient, without falling into the trap
of premature optimization that sacrifices clarity for negligible gains.

Guide 07 (Async & Concurrency) already covers async performance topics
like sequential vs parallel `await`, event loop blocking, Workers, and
streams. Guide 04 (Values & References) covers copying mechanics
(`structuredClone`, spread, `Object.freeze`). This guide should NOT
re-teach those. Instead, this guide focuses on the synchronous
performance patterns and the measurement discipline that inform good
performance decisions.

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

**Garbage collection and memory**:
- `exploring-js/garbage-collection.md`
- `js-definitive-guide/garbage-collection.md`
- `exploring-js/weakly-held-keys.md`
- `exploring-js/weakmap-data-structure.md`
- `exploring-js/weakmap-use-cases.md`
- `exploring-js/weakmap-api.md`
- `exploring-js/weakmap-black-box.md`
- `exploring-js/weakset-data-structure.md`
- `exploring-js/weakset-use-cases.md`
- `js-definitive-guide/weak-map.md`
- `js-definitive-guide/weak-set.md`
- `deep-js/closure.md`

**Map, Set, and collection choices**:
- `exploring-js/map-data-structure.md`
- `exploring-js/map-methods.md`
- `exploring-js/map-iteration.md`
- `exploring-js/map-combining.md`
- `exploring-js/set-data-structure.md`
- `exploring-js/set-iteration.md`
- `exploring-js/set-removing-duplicates.md`
- `js-definitive-guide/map-class.md`
- `js-definitive-guide/set-class.md`

**Array performance and sparse arrays**:
- `exploring-js/array-holes.md`
- `exploring-js/array-length.md`
- `exploring-js/array-indices-as-property-keys.md`
- `exploring-js/array-copying.md`
- `exploring-js/array-sort.md`
- `exploring-js/array-push-pop-shift-unshift.md`
- `exploring-js/array-slice.md`
- `exploring-js/array-spreading.md`
- `js-definitive-guide/sparse-arrays.md`
- `js-definitive-guide/array-length.md`
- `js-definitive-guide/array-iteration.md`
- `js-definitive-guide/push-pop-shift-unshift.md`
- `js-definitive-guide/splice-method.md`
- `js-definitive-guide/concat-method.md`
- `js-definitive-guide/slice-method.md`
- `js-definitive-guide/sort-and-reverse.md`

**Array higher-order methods (performance implications)**:
- `exploring-js/array-reduce.md`
- `exploring-js/array-reduce-right.md`
- `exploring-js/array-filter.md`
- `exploring-js/array-finding-elements.md`
- `exploring-js/array-every-some.md`
- `exploring-js/array-flat-map.md`
- `exploring-js/external-vs-internal-iteration.md`
- `js-definitive-guide/foreach-method.md`
- `js-definitive-guide/map-method.md`
- `js-definitive-guide/filter-method.md`
- `js-definitive-guide/reduce-method.md`
- `js-definitive-guide/find-and-findindex.md`
- `js-definitive-guide/every-and-some.md`
- `js-definitive-guide/flat-and-flatmap.md`
- `eloquent-js/array-foreach.md`
- `eloquent-js/array-filter.md`
- `eloquent-js/array-reduce.md`

**Iterators, generators, and lazy evaluation**:
- `exploring-js/lazy-evaluation-generators.md`
- `exploring-js/generator-function.md`
- `exploring-js/generator-as-iterator-implementer.md`
- `exploring-js/iterable-iterator.md`
- `exploring-js/iteration-protocol.md`
- `exploring-js/iterator-helper-methods.md`
- `exploring-js/iterator-drop-take.md`
- `exploring-js/iterator-from.md`
- `exploring-js/iterator-to-array.md`
- `exploring-js/one-time-vs-many-times-iterable.md`
- `exploring-js/grouping-iterables.md`
- `js-definitive-guide/lazy-evaluation-iterators.md`
- `js-definitive-guide/infinite-sequences.md`
- `js-definitive-guide/generator-functions.md`
- `js-definitive-guide/custom-iterable-objects.md`
- `eloquent-js/generator.md`
- `eloquent-js/iterator-protocol.md`

**TypedArrays and binary data**:
- `exploring-js/typed-arrays.md`
- `exploring-js/typed-array-vs-array.md`
- `exploring-js/typed-array-element-types.md`
- `exploring-js/array-buffer.md`
- `exploring-js/data-view.md`
- `exploring-js/resizable-array-buffers.md`
- `exploring-js/shared-array-buffer.md`
- `js-definitive-guide/typed-arrays.md`
- `js-definitive-guide/array-buffer.md`
- `js-definitive-guide/data-view.md`

**String performance**:
- `exploring-js/string-concatenation.md`
- `exploring-js/string-methods-overview.md`
- `exploring-js/string-comparison.md`
- `exploring-js/template-literal.md`
- `exploring-js/tagged-template.md`
- `exploring-js/tagged-template-use-cases.md`
- `js-definitive-guide/string-methods.md`
- `js-definitive-guide/template-literals.md`
- `js-definitive-guide/tagged-template-literals.md`

**Property access and object performance**:
- `exploring-js/property-value-shorthand.md`
- `exploring-js/computed-property-keys.md`
- `exploring-js/prototype-chain.md`
- `exploring-js/object-keys-values-entries.md`
- `exploring-js/spreading-into-object-literals.md`
- `deep-js/property-descriptor.md`
- `deep-js/property-attributes.md`
- `deep-js/prototype-chain-and-assignment.md`
- `deep-js/object-keys.md`
- `deep-js/object-values.md`
- `deep-js/object-entries.md`
- `deep-js/spreading-objects.md`
- `deep-js/spreading-arrays.md`
- `deep-js/spreading-enumerability.md`
- `js-definitive-guide/property-access-expressions.md`
- `js-definitive-guide/property-enumeration-order.md`
- `js-definitive-guide/objects-as-property-collections.md`

**Immutability and freezing (performance angle)**:
- `deep-js/object-freeze.md`
- `deep-js/shallow-freezing.md`
- `deep-js/deep-freezing.md`
- `deep-js/immutability-for-shared-state.md`
- `deep-js/non-destructive-update.md`
- `deep-js/non-destructive-update-as-defense.md`
- `deep-js/non-destructive-array-update.md`
- `exploring-js/structured-clone.md`

**Memoization and caching**:
- `js-definitive-guide/memoization.md`
- `exploring-js/closure-use-cases.md`
- `exploring-js/closures.md`
- `js-definitive-guide/closures.md`

**Tree shaking and module optimization**:
- `exploring-js/tree-shaking.md`
- `exploring-js/module-characteristics.md`
- `exploring-js/bundlers.md`
- `js-definitive-guide/tree-shaking.md`
- `js-definitive-guide/code-bundlers.md`

**Scope, hoisting, and lookup**:
- `deep-js/scope-chain.md`
- `deep-js/nested-scopes-via-environments.md`
- `deep-js/lexical-scope.md`
- `deep-js/module-scope.md`
- `deep-js/scope-internal-slot.md`
- `exploring-js/variable-scope.md`
- `exploring-js/declarations-scope-activation.md`

**Proxy performance implications**:
- `deep-js/proxy.md`
- `deep-js/proxy-handler.md`
- `deep-js/proxy-target.md`
- `deep-js/proxy-trap.md`
- `deep-js/proxy-invariants.md`
- `deep-js/revocable-proxy.md`
- `js-definitive-guide/proxy-objects.md`

**Coercion costs**:
- `exploring-js/type-coercion.md`
- `exploring-js/explicit-type-conversion.md`
- `exploring-js/operator-coercion.md`
- `deep-js/type-coercion.md`
- `deep-js/explicit-type-conversion.md`
- `deep-js/addition-operator-coercion.md`

**Deno-specific performance**:
- `deno/deno-test-runner.md`
- `deno/deno-compile.md`

**Debouncing and throttling** (performance through rate-limiting):
- `eloquent-js/debouncing.md`
- `eloquent-js/throttling.md`

## Structural template

Follow the same format as the existing guides (01–07):

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

**Measurement discipline** (lead with this — the most important section):
1. Don't optimize without measuring — profile first, optimize second (MUST)
2. `Deno.bench()` for microbenchmarks (SHOULD)
3. `performance.now()` for timing critical sections (SHOULD)
4. Beware microbenchmark traps — JIT warmup, dead code elimination,
   monomorphic vs megamorphic call sites (SHOULD)

**Data structure choices**:
5. `Map` over plain objects for dynamic key collections (SHOULD)
6. `Set` over arrays for membership testing (SHOULD)
7. `WeakMap` for object-keyed caches that don't prevent GC (SHOULD)
8. `WeakRef` and `FinalizationRegistry` — rarely needed, understand
   the guarantees (CONSIDER)
9. TypedArrays for numeric/binary data — fixed type, contiguous
   memory (CONSIDER)

**Array performance**:
10. Avoid sparse arrays — holes are slower and produce surprising
    iteration behavior (SHOULD)
11. `push`/`pop` are O(1); `shift`/`unshift` are O(n) — choose
    the right end (SHOULD)
12. Pre-allocate when size is known — `new Array(n)` then fill,
    or `Array.from({ length: n })` (CONSIDER)
13. Chain vs intermediate arrays — `arr.filter().map()` allocates
    twice; single `reduce` or `flatMap` can avoid it (CONSIDER)
14. `arr.find()` / `arr.some()` short-circuit; `arr.filter()` does
    not — pick the right method for the job (SHOULD)

**Iteration and lazy evaluation**:
15. Generators for lazy sequences — process items on demand, not
    all at once (SHOULD)
16. Iterator helpers (`.map()`, `.filter()`, `.take()`) for lazy
    pipelines without intermediate arrays (CONSIDER)
17. `for-of` vs `.forEach()` vs `for` — readability wins unless
    profiling shows otherwise (SHOULD)
18. Early exit with `break`/`return` in `for-of` — `.forEach()`
    cannot break (SHOULD)

**Object and property performance**:
19. Keep object shapes consistent — same properties, same order,
    same types (hidden classes / V8 maps) (SHOULD)
20. Avoid `delete` — use `undefined` assignment or destructure-out
    to preserve shape (SHOULD)
21. Property lookup walks the prototype chain — cache deep lookups
    in a local variable (CONSIDER)
22. `Object.keys()` / `Object.entries()` allocate arrays — use
    `for-in` with `hasOwn` for zero-allocation enumeration when
    it matters (CONSIDER)

**String performance**:
23. Template literals vs concatenation — equivalent for most cases;
    avoid building strings in tight loops either way (SHOULD)
24. Avoid repeated string building — collect pieces in an array,
    `.join()` at the end (SHOULD)

**Allocation discipline**:
25. Avoid allocations in hot loops — hoist object/array creation
    out of loops when possible (SHOULD)
26. Object pooling for high-churn short-lived objects (CONSIDER)
27. `structuredClone()` is not free — only deep-copy when you need
    independence (SHOULD — references 04 ID-09)

**Memoization and caching**:
28. Memoize expensive pure functions with closure + `Map` (SHOULD)
29. Bounded caches — LRU or size-limited to prevent memory leaks (SHOULD)
30. `WeakMap` for memoizing per-object computations (SHOULD)

**Tree shaking and dead code**:
31. ESM static structure enables tree shaking — avoid `export default`
    objects, prefer named exports (SHOULD — references 01 ID-07)
32. Side-effect-free modules — don't execute logic at import time (SHOULD)

**What NOT to micro-optimize** (critical for AI code generation):
33. Don't hand-unroll loops — the engine does it better (MUST)
34. Don't convert idiomatic code to "faster" unreadable code without
    profiling evidence (MUST)
35. Don't cache `array.length` in `for` loops — engines optimize
    this already (SHOULD)
36. Proxies have overhead — don't use them in hot paths without
    measurement (CONSIDER)

## Boundaries with other guides

**Guide 04 (Values & References)** already covers:
- `structuredClone()` mechanics (04 ID-09)
- Spread for shallow copies (04 ID-06)
- `Object.assign()` vs spread (04 ID-07)
- `Object.freeze()` / `seal()` / `preventExtensions()` (04 ID-16, ID-17)

**Guide 05 (Type Discipline)** already covers:
- TypedArray as a type discipline choice (05 ID-27)
- `Map`/`Set` for typed collections (05 ID-26)

**Guide 06 (Functions & Closures)** already covers:
- Closures for encapsulation (06 ID-08)
- Factory functions with closures (06 ID-09)
- Closure memory considerations (06 ID-10 if present)

**Guide 07 (Async & Concurrency)** already covers:
- Sequential vs parallel `await` (also 03 ID-21)
- Event loop blocking
- Web Workers for CPU-intensive work
- Streams and backpressure
- Debouncing and throttling

**Do NOT re-teach these.** Cross-reference them. This guide covers
the *synchronous performance patterns* and *measurement discipline*
that the other guides don't address.

## Output

Save as: `guides/08-performance.md` in the `ai-js` repo.

## Quality bar

- Every idiom must cite specific behavior described in the concept cards.
  Don't make claims the cards don't support.
- Code examples must be runnable under Deno (not Node.js).
- Good/bad examples should be realistic, not toy code.
- The tone should be terse and direct — this is a reference doc, not a
  tutorial. Match the existing guides' density and style.
- No Node.js imports or APIs in any examples. Use `Deno.bench()`,
  `Deno.readTextFile`, `fetch()`, `performance.now()`, etc.
- All cross-references must use the correct guide slugs from the list.
- The "measurement discipline" section MUST come first. The single
  most damaging performance anti-pattern in AI-generated code is
  premature optimization. Establish "measure first" before presenting
  any optimization technique.
- The "what NOT to micro-optimize" section is critical — it prevents
  Claude Code from generating code that trades readability for
  negligible performance gains. Be specific about what engines already
  optimize.
- For data structure recommendations (Map vs object, Set vs array),
  give concrete guidance on when the crossover point matters and when
  it doesn't. A `Map` with 3 entries is not faster than an object
  with 3 properties.
- The concept cards have limited coverage of engine internals (hidden
  classes, JIT, inline caches). Ground claims in what the cards say
  about observable behavior (sparse arrays, prototype chain lookup,
  coercion steps). Don't speculate about V8 internals beyond what
  the cards support — but you can note that engines optimize common
  patterns and that the takeaway is "write idiomatic code and let the
  engine do its job."

## What NOT to do

- Don't invent idioms not supported by the concept card content
- Don't include Node.js-specific patterns (no `Buffer.allocUnsafe()`,
  no `process.memoryUsage()`, no Node profiling tools)
- Don't include React/Vue patterns (no `useMemo`, no `React.memo`)
- Don't include TypeScript-specific patterns
- Don't re-teach patterns already covered in other guides — just
  cross-reference them (see Boundaries section)
- Don't speculate about V8/SpiderMonkey/JSC internals beyond what
  the concept cards support — stay grounded in observable behavior
- Don't recommend micro-optimizations without evidence they matter —
  the default position should be "write clear code"
- Don't include benchmark framework comparisons or third-party
  profiling tools — stick to built-in Deno and Web Platform APIs
- Don't include WASM patterns — that's a separate domain
- Don't include Web Worker performance patterns — those are in
  Guide 07
- Don't turn this into a "JavaScript engine internals" guide — it's
  a practical performance guide for application developers
- Don't recommend `for` loops over `.map()` / `.filter()` as a
  blanket rule — only when profiling shows it matters for a specific
  hot path. Readability is the default priority.
