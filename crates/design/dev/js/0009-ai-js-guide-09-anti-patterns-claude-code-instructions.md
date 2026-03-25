# ai-js Guide 09: Anti-Patterns — Claude Code Instructions

## Context

We're building `ai-js`, a repo of curated JavaScript guides that Claude
Code reads via a SKILL.md entry point to produce consistently high-quality
JS code. This is modeled on our `ai-rust` repo.

Guides 01–08 are complete. Now we're writing Guide 09: Anti-Patterns.

This guide is different from the others. Guides 01–08 teach what TO do
and include inline "Bad" examples as contrast. Guide 09 is a dedicated
catalog of what NOT to do — cross-cutting anti-patterns that either
don't fit neatly into a single guide's scope, or are so common and
damaging (especially in AI-generated code) that they deserve dedicated,
searchable entries with detailed explanations of *why* they're wrong.

**The purpose is threefold**:
1. Catch patterns that fall between the cracks of other guides
2. Provide a concentrated "negative examples" reference that Claude
   Code can consult when reviewing or generating code
3. Address anti-patterns that are disproportionately common in
   AI-generated JavaScript — patterns that LLMs produce frequently
   because they appear often in training data despite being wrong

The existing guides already reference Guide 09 for these categories:
- Common JavaScript API design mistakes (from Guide 02)
- Common error handling mistakes (from Guide 03)
- Common mutation bugs (from Guide 04)
- Coercion traps and type-unsafe patterns (from Guide 05)
- Common closure and `this` bugs (from Guide 06)
- Async anti-patterns (from Guide 07)

Guide 09 must deliver on all of these promises.

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
related cards while reading, use them too. Anti-patterns draw from
almost every domain, so the card list is broad.

**JavaScript quirks and coercion traps**:
- `exploring-js/javascript-quirks.md`
- `exploring-js/type-coercion.md`
- `exploring-js/operator-coercion.md`
- `exploring-js/loose-equality-operator.md`
- `exploring-js/typeof-operator.md`
- `exploring-js/instanceof-operator.md`
- `exploring-js/nan-value.md`
- `exploring-js/number-isnan.md`
- `exploring-js/void-operator.md`
- `exploring-js/wrapper-objects.md`
- `exploring-js/toprimitive.md`
- `exploring-js/symbol-toprimitive.md`
- `exploring-js/explicit-type-conversion.md`
- `exploring-js/falsy-and-truthy-values.md`
- `exploring-js/truthy-and-falsy-values.md`
- `deep-js/type-coercion.md`
- `deep-js/explicit-type-conversion.md`
- `deep-js/addition-operator-coercion.md`
- `deep-js/object-prototype-tostring.md`
- `js-definitive-guide/type-coercion.md`
- `js-definitive-guide/type-conversion-table.md`
- `js-definitive-guide/strict-vs-loose-equality.md`
- `js-definitive-guide/loose-equality-operator.md`
- `js-definitive-guide/typeof-operator.md`
- `js-definitive-guide/instanceof-operator.md`
- `js-definitive-guide/nan-and-infinity.md`
- `js-definitive-guide/null-vs-undefined.md`
- `js-definitive-guide/object-to-primitive-conversion.md`
- `js-definitive-guide/tostring-valueof-tojson.md`
- `eloquent-js/type-coercion.md`
- `eloquent-js/loose-equality.md`

**`this` binding pitfalls**:
- `exploring-js/this-keyword.md`
- `exploring-js/extracting-methods.md`
- `js-definitive-guide/this-keyword-binding.md`
- `js-definitive-guide/invocation-patterns.md`
- `js-definitive-guide/bind-method.md`
- `js-definitive-guide/call-and-apply.md`
- `js-definitive-guide/arrow-function-this-inheritance.md`
- `eloquent-js/this-keyword.md`

**Legacy patterns to avoid**:
- `exploring-js/var-declaration.md`
- `exploring-js/hoisting.md`
- `exploring-js/sloppy-mode.md`
- `exploring-js/strict-mode.md`
- `exploring-js/iife.md`
- `exploring-js/eval-function.md`
- `exploring-js/for-in-loop.md`
- `exploring-js/commonjs-module.md`
- `exploring-js/automatic-semicolon-insertion.md`
- `exploring-js/labeled-statement.md`
- `exploring-js/delete-operator.md`
- `js-definitive-guide/var-declarations.md`
- `js-definitive-guide/hoisting.md`
- `js-definitive-guide/function-hoisting.md`
- `js-definitive-guide/iifes.md`
- `js-definitive-guide/module-pattern-iife.md`
- `js-definitive-guide/eval-function.md`
- `js-definitive-guide/for-in-loop.md`
- `js-definitive-guide/arguments-object.md`
- `js-definitive-guide/automatic-semicolon-insertion.md`
- `js-definitive-guide/strict-mode.md`
- `js-definitive-guide/use-strict.md`
- `js-definitive-guide/commonjs-require.md`
- `js-definitive-guide/commonjs-vs-es-modules.md`
- `js-definitive-guide/delete-operator.md`
- `eloquent-js/var-declaration.md`
- `eloquent-js/hoisting.md`
- `eloquent-js/commonjs-module.md`
- `eloquent-js/delete-operator.md`

**Null/undefined confusion**:
- `exploring-js/undefined-value.md`
- `exploring-js/null-value.md`
- `exploring-js/history-of-undefined-and-null.md`
- `exploring-js/checking-for-undefined-or-null.md`
- `exploring-js/undefined-null-no-properties.md`
- `exploring-js/null-prototype-objects.md`
- `exploring-js/nullish-coalescing-operator.md`
- `exploring-js/nullish-coalescing-assignment-operator.md`
- `js-definitive-guide/null-vs-undefined.md`
- `js-definitive-guide/nullish-coalescing.md`
- `eloquent-js/null-value.md`
- `eloquent-js/undefined-value.md`
- `eloquent-js/nullish-coalescing-operator.md`

**Mutation and shared state traps**:
- `deep-js/shared-mutable-state.md`
- `deep-js/three-strategies-for-shared-state.md`
- `deep-js/aliasing.md`
- `deep-js/defensive-copying.md`
- `deep-js/defensive-copying-input.md`
- `deep-js/defensive-copying-output.md`
- `deep-js/non-destructive-update.md`
- `deep-js/non-destructive-update-as-defense.md`
- `exploring-js/objects-are-mutable.md`
- `exploring-js/const-immutability.md`
- `eloquent-js/mutability.md`
- `eloquent-js/side-effect.md`
- `eloquent-js/side-effects.md`
- `js-definitive-guide/primitive-immutability-vs-object-mutability.md`

**Scope and closure traps**:
- `deep-js/closure.md`
- `deep-js/scope-chain.md`
- `deep-js/nested-scopes-via-environments.md`
- `deep-js/scope-internal-slot.md`
- `exploring-js/closures.md`
- `exploring-js/closure-use-cases.md`
- `exploring-js/bound-vs-free-variables.md`
- `exploring-js/shadowing.md`
- `exploring-js/temporal-dead-zone.md`
- `exploring-js/declarations-scope-activation.md`
- `exploring-js/global-object.md`
- `js-definitive-guide/closures.md`
- `js-definitive-guide/block-scope.md`
- `js-definitive-guide/global-object.md`
- `eloquent-js/closure.md`
- `eloquent-js/scope.md`
- `eloquent-js/lexical-scoping.md`

**Promise and async traps**:
- `exploring-js/promise-chaining-mistakes.md`
- `exploring-js/awaiting-is-shallow.md`
- `exploring-js/fire-and-forget.md`
- `exploring-js/async-code-infectiousness.md`
- `exploring-js/return-await.md`
- `js-definitive-guide/callback-hell.md`
- `js-definitive-guide/sequential-vs-parallel-await.md`
- `eloquent-js/callback-hell.md`
- `eloquent-js/asynchronous-bugs.md`

**Array and iteration traps**:
- `exploring-js/array-holes.md`
- `exploring-js/array-indices-as-property-keys.md`
- `exploring-js/external-vs-internal-iteration.md`
- `exploring-js/one-time-vs-many-times-iterable.md`
- `exploring-js/destructuring-non-destructurable-values.md`
- `exploring-js/object-destructuring-assignment-pitfall.md`
- `js-definitive-guide/sparse-arrays.md`
- `js-definitive-guide/array-like-objects.md`

**Prototype chain and inheritance traps**:
- `exploring-js/prototype-chain.md`
- `deep-js/prototype-chain-and-assignment.md`
- `js-definitive-guide/prototype-chain.md`
- `js-definitive-guide/constructor-property.md`
- `js-definitive-guide/prototype-based-inheritance.md`
- `eloquent-js/prototype-chain.md`

**Global object pollution**:
- `exploring-js/global-object.md`
- `deep-js/global-object.md`
- `js-definitive-guide/global-object.md`

## Structural template

Follow the same format as the existing guides (01–08), **but with
an inverted framing**: each entry leads with the anti-pattern, then
shows the fix.

Each anti-pattern entry has:
```
## ID-XX: [Anti-Pattern Title — what NOT to do]

**Strength**: MUST-AVOID | SHOULD-AVOID | CONSIDER-AVOIDING

**Summary**: One sentence describing the mistake.

[Code examples with // Anti-pattern and // Fix labels]

**Why it's wrong**: What breaks, what's confusing, what's slow.
Cite concept card sources.

**Fix**: The correct pattern, with cross-reference to the relevant
guide where the positive pattern is taught.

**See also**: Cross-references to other IDs or guides
```

**Strength levels for anti-patterns** (inverted from the positive guides):
- **MUST-AVOID**: This will cause bugs, security issues, or silent
  data corruption. Never do this.
- **SHOULD-AVOID**: This will cause maintenance problems, confusion,
  or subtle incorrectness. Avoid unless you have a documented reason.
- **CONSIDER-AVOIDING**: This is a code smell or outdated pattern.
  Prefer the modern alternative.

End with:
- Quick Reference Table
- Related Guidelines (using correct guide slugs from the list above)
- External References

## Proposed anti-pattern list

This is a starting outline — adjust based on what the concept cards
emphasize. Add entries if the cards reveal important anti-patterns.
Remove or merge if redundant with inline "Bad" examples in other
guides (but only if the other guide's coverage is thorough enough).
Aim for 25-35 entries.

**The key question for each entry**: Does this anti-pattern need
its own dedicated entry here, or is the inline "Bad" example in
another guide sufficient? Include it here if:
- It's a cross-cutting mistake that spans multiple guides
- It's disproportionately common in AI-generated code
- The "why it's wrong" explanation needs more depth than an inline
  example can provide
- It involves a subtle interaction between language features

### Coercion and type traps

1. Using `==` instead of `===` (except `== null`) (MUST-AVOID —
   amplifies 01 ID-02 with the full coercion cascade table)
2. Trusting `typeof` for all type checks — `typeof null === "object"`,
   `typeof NaN === "number"`, `typeof [] === "object"` (SHOULD-AVOID)
3. Using `||` for defaults when `0`, `""`, or `false` are valid
   values — use `??` instead (MUST-AVOID — amplifies 01 ID-03)
4. Global `isNaN()` vs `Number.isNaN()` — global coerces first
   (SHOULD-AVOID — amplifies 05 ID-22)
5. Using `parseInt` without a radix, or for non-integer parsing
   (SHOULD-AVOID)
6. Constructor wrappers: `new String()`, `new Number()`, `new Boolean()`
   create objects, not primitives (SHOULD-AVOID)

### `this` binding traps

7. Extracting methods loses `this` — `const fn = obj.method; fn()`
   (MUST-AVOID)
8. Using regular functions as callbacks when `this` matters — use
   arrow functions or `.bind()` (SHOULD-AVOID)
9. Arrow functions as object methods — they inherit `this` from the
   enclosing scope, not the object (SHOULD-AVOID)

### Scope and closure traps

10. `var` in loops with closures — all closures share the same binding
    (MUST-AVOID — amplifies 06 ID-07)
11. Accidental globals — forgetting `const`/`let` in sloppy mode
    creates global properties (MUST-AVOID)
12. Shadowing outer variables — confusing, error-prone (SHOULD-AVOID)
13. Relying on hoisting for variable access before declaration
    (SHOULD-AVOID)

### Mutation traps

14. Mutating function arguments — caller's data changes unexpectedly
    (MUST-AVOID — amplifies 04 ID-11)
15. `const` doesn't mean immutable — it freezes the binding, not
    the value (SHOULD-AVOID — amplifies 04 ID-04)
16. Shallow copy surprise — spread/`Object.assign` don't copy nested
    objects (SHOULD-AVOID — amplifies 04 ID-06, 04 ID-08)
17. `Array.prototype.sort()` mutates in place — use `.toSorted()`
    (SHOULD-AVOID)

### Async anti-patterns

18. Sequential `await` on independent operations — use `Promise.all()`
    (MUST-AVOID — amplifies 03 ID-21, 07 ID-13)
19. `.map(async fn)` without `Promise.all()` — returns `Promise[]`
    not values (MUST-AVOID — amplifies 07 ID-21)
20. Fire-and-forget Promises — unhandled rejections crash Deno
    (MUST-AVOID — amplifies 03 ID-20)
21. Mixing callbacks and Promises — pick one model, promisify the
    other (SHOULD-AVOID — amplifies 03 ID-18)
22. The `.then()` nesting anti-pattern — chaining defeats callback
    hell; nesting recreates it (SHOULD-AVOID)
23. `fetch()` without `signal` — uncancellable requests waste
    resources (SHOULD-AVOID — amplifies 07 ID-24)

### API design anti-patterns

24. Functions that both return AND throw for expected cases — pick
    one error channel (MUST-AVOID — amplifies 03 ID-02)
25. Boolean parameters — `render(true, false)` is unreadable; use
    options objects (SHOULD-AVOID — amplifies 02 ID-05)
26. `return obj` from constructor — confusing, breaks `instanceof`
    (SHOULD-AVOID)
27. Overloaded functions that change behavior based on argument
    count or type — hard to reason about (SHOULD-AVOID)

### Legacy patterns in modern code

28. `var` in any new code (MUST-AVOID — amplifies 01 ID-01)
29. `for...in` for array iteration — iterates inherited properties,
    non-numeric keys (MUST-AVOID)
30. `arguments` object — use rest parameters (`...args`) instead
    (SHOULD-AVOID)
31. `eval()` and `new Function()` — security and performance
    (MUST-AVOID)
32. IIFEs for scope isolation — use block scope or modules instead
    (CONSIDER-AVOIDING)
33. CommonJS `require()` in ESM context (MUST-AVOID)

### Miscellaneous traps

34. `delete` on array elements — creates holes, doesn't update
    `.length` (SHOULD-AVOID)
35. `JSON.parse(JSON.stringify(obj))` for deep copy — use
    `structuredClone()` (SHOULD-AVOID — amplifies 04 ID-10)
36. Catching errors and only logging — swallowed errors hide bugs
    (SHOULD-AVOID — amplifies 03 ID-04)

## Relationship to other guides — the "amplify, don't duplicate" rule

Many anti-patterns are the inverse of a positive idiom in another guide.
The rule:

- If the other guide's inline "Bad" example is sufficient (simple,
  well-explained), then Guide 09 should **briefly reference** it with
  a one-liner and a cross-reference. Don't rewrite the same content.
- If the anti-pattern needs **deeper explanation** than the inline
  example provides (e.g., the full `==` coercion table, or why
  `typeof null === "object"` is a historical accident), then Guide 09
  should **amplify** — provide the extended treatment here and
  cross-reference the other guide for the positive pattern.
- If the anti-pattern is **cross-cutting** (spans multiple guides),
  it belongs here primarily, with cross-references outward.

The "amplifies" annotations in the proposed list indicate which
entries extend coverage from another guide. Entries without
"amplifies" are unique to this guide.

## Output

Save as: `guides/09-anti-patterns.md` in the `ai-js` repo.

## Quality bar

- Every anti-pattern must cite specific behavior described in the
  concept cards. Don't make claims the cards don't support.
- Code examples must be runnable under Deno (not Node.js).
- Anti-pattern examples should be realistic — patterns that actually
  appear in code, not contrived strawmen.
- The tone should be terse and direct. This is a reference doc, not
  a lecture. Match the existing guides' density and style.
- No Node.js imports or APIs in any examples.
- All cross-references must use the correct guide slugs from the list.
- **Every entry must have a "Fix" that points to the positive pattern.**
  This guide should never leave the reader knowing what's wrong without
  knowing what's right.
- The coercion/type section should be thorough — `typeof`, `==`,
  `NaN`, `parseInt`, wrapper objects. These are the traps that catch
  even experienced developers and are disproportionately present in
  AI-generated code.
- The `this` section should be practical and example-driven. Abstract
  explanations of `this` binding rules are in Guide 06. This guide
  shows the bugs that happen when you get it wrong.
- The async section should be concise — Guides 03 and 07 cover async
  in depth. This guide catalogs the specific mistakes, with
  cross-references for the full treatment.
- Anti-patterns that Biome catches automatically should note this —
  e.g., "Biome's `noDoubleEquals` rule catches this" — so the reader
  knows which anti-patterns have automated safety nets.

## What NOT to do

- Don't invent anti-patterns not supported by the concept card content
- Don't include Node.js-specific anti-patterns (no `require()` pitfalls
  beyond "don't use it", no `Buffer` misuse, no `process.on` patterns)
- Don't include React/Vue anti-patterns (no stale closure in `useEffect`)
- Don't include TypeScript-specific anti-patterns (no `any` abuse)
- Don't duplicate the full explanation from another guide — amplify
  with additional depth or cross-reference with a one-liner
- Don't moralize. State what breaks and why. The reader is a
  professional who wants facts, not a lecture on best practices.
- Don't include patterns that are merely "not the best way" — every
  entry should describe something that causes actual bugs, confusion,
  or maintenance burden. Aesthetic preferences are not anti-patterns.
- Don't include patterns that only matter in browsers with DOM access
  (no `document.write()`, no `innerHTML` XSS, no global event
  listener leaks) — the target environment is Deno server-side code
- Don't turn this into a JavaScript history lesson — mention legacy
  context only when it explains why the anti-pattern exists (e.g.,
  `typeof null === "object"` is a spec bug from 1995)
- Don't recommend linter rules as the primary fix — the fix should
  be a code pattern. Biome rules are supplementary, not the answer.
