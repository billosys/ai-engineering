# ai-js Guide 06: Functions & Closures — Claude Code Instructions

## Context

We're building `ai-js`, a repo of curated JavaScript guides that Claude
Code reads via a SKILL.md entry point to produce consistently high-quality
JS code. This is modeled on our `ai-rust` repo.

Guides 01–05 are complete or in progress. Now we're writing Guide 06:
Functions & Closures.

This is the heart of JavaScript composition. Where Rust uses traits as
its composition primitive, JS uses functions. This guide covers function
mechanics, closures, higher-order functions, partial application, and
the patterns that make functional JS work — all grounded in how the
language actually behaves under the hood.

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

**Function forms and roles**:
- `exploring-js/function-roles.md`
- `exploring-js/specialized-function.md`
- `exploring-js/ordinary-function.md`
- `exploring-js/function-declarations.md`
- `exploring-js/function-declaration-vs-expression.md`
- `exploring-js/arrow-function-expressions.md`
- `exploring-js/arrow-function.md`
- `exploring-js/iife.md`
- `exploring-js/callback-function.md`
- `exploring-js/callback-pattern.md`
- `js-definitive-guide/function-declarations.md`
- `js-definitive-guide/function-definition-expressions.md`
- `js-definitive-guide/function-expressions.md`
- `js-definitive-guide/arrow-functions.md`
- `js-definitive-guide/iifes.md`
- `js-definitive-guide/invocation-patterns.md`
- `js-definitive-guide/invocation-expressions.md`
- `js-definitive-guide/function-constructor.md`
- `eloquent-js/function-declaration.md`
- `eloquent-js/function-definition.md`
- `eloquent-js/arrow-function.md`

**Closures and scope**:
- `exploring-js/closures.md`
- `exploring-js/closure-use-cases.md`
- `exploring-js/variable-scope.md`
- `exploring-js/block-scoping.md`
- `exploring-js/declarations-scope-activation.md`
- `exploring-js/temporal-dead-zone.md`
- `exploring-js/hoisting.md`
- `exploring-js/early-activation.md`
- `exploring-js/bound-vs-free-variables.md`
- `exploring-js/shadowing.md`
- `exploring-js/global-scope.md`
- `exploring-js/global-object.md`
- `deep-js/closure.md`
- `deep-js/lexical-scope.md`
- `deep-js/lexical-environment.md`
- `deep-js/scope-chain.md`
- `deep-js/environment.md`
- `deep-js/environment-record.md`
- `deep-js/declarative-environment-record.md`
- `deep-js/object-environment-record.md`
- `deep-js/execution-context.md`
- `deep-js/outer-environment-reference.md`
- `deep-js/recursion-via-environments.md`
- `deep-js/nested-scopes-via-environments.md`
- `deep-js/script-scope.md`
- `deep-js/module-scope.md`
- `deep-js/global-environment.md`
- `deep-js/global-object.md`
- `deep-js/global-this.md`
- `deep-js/global-ecmascript-vs-host-variables.md`
- `deep-js/global-variable-creation.md`
- `deep-js/scope-internal-slot.md`
- `js-definitive-guide/nested-functions.md`
- `js-definitive-guide/block-scope.md`
- `js-definitive-guide/hoisting.md`
- `js-definitive-guide/function-hoisting.md`
- `eloquent-js/local-scope.md`
- `eloquent-js/global-scope.md`
- `eloquent-js/binding.md`

**`this` binding**:
- `exploring-js/this-keyword.md`
- `exploring-js/this-in-various-contexts.md`
- `exploring-js/shadowing-this.md`
- `exploring-js/extracting-methods.md`
- `exploring-js/dispatched-vs-direct-method-calls.md`
- `deep-js/arrow-function-naming.md`
- `js-definitive-guide/this-keyword-binding.md`
- `js-definitive-guide/arrow-function-this-inheritance.md`
- `js-definitive-guide/bind-method.md`
- `js-definitive-guide/call-and-apply.md`
- `js-definitive-guide/method-invocation.md`
- `js-definitive-guide/constructor-invocation.md`

**Higher-order functions**:
- `exploring-js/callback-function.md`
- `exploring-js/callback-pattern.md`
- `exploring-js/array-map.md`
- `exploring-js/array-filter.md`
- `exploring-js/array-reduce.md`
- `exploring-js/array-reduce-right.md`
- `exploring-js/array-every-some.md`
- `exploring-js/array-finding-elements.md`
- `exploring-js/array-flat-map.md`
- `exploring-js/external-vs-internal-iteration.md`
- `js-definitive-guide/higher-order-functions.md`
- `js-definitive-guide/map-method.md`
- `js-definitive-guide/every-and-some.md`
- `js-definitive-guide/find-and-findindex.md`
- `js-definitive-guide/foreach-method.md`
- `js-definitive-guide/flat-and-flatmap.md`
- `eloquent-js/higher-order-function.md`
- `eloquent-js/abstracting-repetition.md`
- `eloquent-js/composability.md`
- `eloquent-js/functions-as-values.md`
- `eloquent-js/predicate-function.md`

**Parameters, arguments, defaults, rest**:
- `exploring-js/parameters-vs-arguments.md`
- `exploring-js/parameter-default-values.md`
- `exploring-js/rest-parameters.md`
- `exploring-js/rest-elements.md`
- `exploring-js/spread-syntax.md`
- `exploring-js/spread-into-function-calls.md`
- `exploring-js/named-parameters.md`
- `exploring-js/destructuring-parameters.md`
- `deep-js/named-parameters-via-destructuring.md`
- `deep-js/default-values-in-destructuring.md`
- `js-definitive-guide/default-parameters.md`
- `js-definitive-guide/rest-parameters.md`
- `js-definitive-guide/spread-in-function-calls.md`

**Function naming and identity**:
- `deep-js/function-naming-rules.md`
- `deep-js/function-name-property.md`
- `deep-js/creation-time-naming.md`
- `deep-js/new-function-naming.md`
- `deep-js/anonymous-function-expression.md`
- `deep-js/named-function-expression.md`
- `deep-js/bound-function-naming.md`
- `deep-js/arrow-function-naming.md`
- `deep-js/getter-setter-naming.md`
- `deep-js/configurable-name-property.md`
- `deep-js/symbol-keyed-method-names.md`
- `deep-js/default-export-naming.md`
- `js-definitive-guide/functions-as-values.md`

**Partial application, currying, bind**:
- `deep-js/partial-application.md`
- `deep-js/currying.md`
- `exploring-js/function-bind-method.md`
- `exploring-js/function-apply-method.md`
- `exploring-js/function-call-method.md`
- `js-definitive-guide/bind-method.md`
- `js-definitive-guide/call-and-apply.md`

**Generators** (as a function form):
- `exploring-js/generator-function.md`
- `exploring-js/generator-as-iterator-implementer.md`
- `exploring-js/yield-operator.md`
- `exploring-js/yield-star-operator.md`
- `exploring-js/lazy-evaluation-generators.md`
- `js-definitive-guide/generator-functions.md`
- `js-definitive-guide/yield-keyword.md`
- `js-definitive-guide/yield-star-delegation.md`
- `js-definitive-guide/sending-values-to-generators.md`

**Pure functions and side effects**:
- `eloquent-js/pure-function.md`
- `eloquent-js/side-effect.md`
- `eloquent-js/abstraction.md`
- `eloquent-js/abstracting-repetition.md`

**Closures for encapsulation**:
- `js-definitive-guide/closure-based-private-state.md`
- `js-definitive-guide/module-pattern-iife.md`

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

**Function forms — when to use which**:
1. `function` declarations for named module-level functions (SHOULD)
2. Arrow functions for callbacks and inline closures (SHOULD)
3. Never use `function` as a callback — arrow inherits `this` (MUST)
4. Method shorthand in objects and classes (SHOULD)
5. Generator functions for lazy sequences and iterator impl (SHOULD)

**Closures — mechanics and patterns**:
6. Closures capture variables, not values (MUST)
7. The `let`-in-loop fix — `let` creates fresh binding per iteration (MUST)
8. Closures for encapsulation — private state without classes (SHOULD)
9. Factory functions that return closures (SHOULD)
10. Beware closing over mutable state — stale closures (SHOULD)

**Scope**:
11. Block scope with `const`/`let` — not function scope like `var` (MUST)
12. Temporal Dead Zone — `let`/`const` exist but are uninitialized (MUST)
13. Function declarations hoist completely; expressions do not (SHOULD)
14. Shadowing — inner bindings mask outer ones of the same name (SHOULD)
15. Module scope — each ESM file has its own scope (SHOULD)

**`this` binding rules**:
16. The four `this` rules — call-site determines binding (MUST)
17. Arrow functions inherit `this` — they have no own binding (MUST)
18. Method extraction loses `this` — use `.bind()` or arrow wrappers (MUST)
19. Never use `call`/`apply`/`bind` when an arrow function suffices (SHOULD)

**Higher-order functions**:
20. Prefer `.map()`, `.filter()`, `.reduce()` for transformations (SHOULD)
21. Use `.find()` / `.findIndex()` for single-element search (SHOULD)
22. Use `.some()` / `.every()` for boolean aggregate checks (SHOULD)
23. Use `.flatMap()` for map-then-flatten patterns (SHOULD)
24. When to use `for-of` instead of array methods — side effects and control flow (SHOULD)

**Partial application and composition**:
25. `.bind()` for partial application (CONSIDER)
26. Manual partial application with closures (SHOULD)
27. Function composition — `pipe()` and `compose()` patterns (CONSIDER)

**Pure functions**:
28. Prefer pure functions — same input, same output, no side effects (SHOULD)
29. Isolate side effects at the edges (SHOULD)

**Function naming**:
30. Functions have a `.name` property — understand how it's set (CONSIDER)
31. Named function expressions for better stack traces (SHOULD)

## Output

Save as: `guides/06-functions-closures.md` in the `ai-js` repo.

## Quality bar

- Every idiom must cite specific behavior described in the concept cards.
  Don't make claims the cards don't support.
- Code examples must be runnable under Deno (not Node.js).
- Good/bad examples should be realistic, not toy code.
- The tone should be terse and direct — this is a reference doc, not a
  tutorial. Match Guide 01's density and style.
- No Node.js imports or APIs in any examples.
- All cross-references must use the correct guide slugs from the list.
- The closure mechanics section should be precise about *how* closures
  work (environments, not just "captures variables"). Deep JS has
  excellent concept cards on this — use them.
- The `this` section should be a definitive reference table, not a
  vague explanation. The four rules (default, implicit, explicit, new)
  and arrow's inheritance should be completely clear.

## What NOT to do

- Don't invent idioms not supported by the concept card content
- Don't include Node.js-specific patterns
- Don't include React hooks patterns (useCallback, useMemo, etc.)
- Don't include TypeScript-specific patterns
- Don't duplicate content that belongs in other guides:
  - Options objects / parameter design → `02-api-design.md`
  - Error handling in callbacks → `03-error-handling.md`
  - Mutation discipline → `04-values-references.md`
  - typeof / instanceof → `05-type-discipline.md`
  - Async functions / Promises → `07-async-concurrency.md`
  - Performance of closures → `08-performance.md`
- Don't teach how closures work from scratch — the audience knows
  programming. Focus on JS-specific mechanics, gotchas, and
  disciplined patterns.
- Don't include FP library recommendations (Ramda, lodash/fp) —
  vanilla JS only. The composition patterns should use plain functions.
