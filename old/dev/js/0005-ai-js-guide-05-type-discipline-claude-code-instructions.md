# ai-js Guide 05: Type Discipline — Claude Code Instructions

## Context

We're building `ai-js`, a repo of curated JavaScript guides that Claude
Code reads via a SKILL.md entry point to produce consistently high-quality
JS code. This is modeled on our `ai-rust` repo.

Guides 01–04 are complete. Now we're writing Guide 05: Type Discipline.

This is the guide about writing type-safe JavaScript *without TypeScript*.
The lykn project does not use TypeScript. Instead, we rely on JSDoc
annotations, runtime validation at boundaries, disciplined use of
JavaScript's type system, and Biome lint rules to catch type errors.
This guide should make a developer confident that their plain JS is
well-typed in practice, not just in theory.

The target environment is:
- **Deno** (not Node.js — no `require()`, no `node_modules`, no npm scripts)
- **Biome** for linting and formatting (not ESLint, not Prettier)
- **ESM-only** (`import`/`export`, no CommonJS)
- **No TypeScript** — plain JS with JSDoc annotations for tooling support
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

**JavaScript type system fundamentals**:
- `exploring-js/javascript-types.md`
- `exploring-js/javascript-type-hierarchy.md`
- `exploring-js/primitive-values.md`
- `exploring-js/dynamic-language.md`
- `exploring-js/multi-paradigm-language.md`
- `exploring-js/static-vs-dynamic.md`
- `exploring-js/static-checking.md`
- `exploring-js/typescript-static-typing.md`
- `js-definitive-guide/type-system-overview.md`
- `js-definitive-guide/primitive-vs-object-types.md`

**typeof and type checking**:
- `exploring-js/typeof-operator.md`
- `exploring-js/instanceof-operator.md`
- `exploring-js/javascript-quirks.md`
- `exploring-js/wrapper-objects.md`
- `exploring-js/primitive-constructor-functions.md`
- `js-definitive-guide/typeof-operator.md`
- `js-definitive-guide/instanceof-operator.md`
- `eloquent-js/type-coercion.md`

**Type coercion mechanics**:
- `exploring-js/type-coercion.md`
- `exploring-js/operator-coercion.md`
- `exploring-js/plus-operator.md`
- `exploring-js/converting-to-number.md`
- `exploring-js/converting-to-string.md`
- `exploring-js/converting-to-boolean.md`
- `exploring-js/explicit-type-conversion.md`
- `exploring-js/silent-failures.md`
- `deep-js/type-coercion.md`
- `deep-js/to-number.md`
- `deep-js/to-string.md`
- `deep-js/to-boolean.md`
- `deep-js/to-primitive.md`
- `deep-js/toprimitive.md`
- `deep-js/abstract-equality-comparison.md`
- `deep-js/addition-operator-coercion.md`
- `deep-js/explicit-type-conversion.md`
- `deep-js/type-casting.md`
- `js-definitive-guide/type-conversion-table.md`
- `js-definitive-guide/object-to-primitive-conversion.md`
- `js-definitive-guide/addition-operator.md`

**Symbols and well-known protocols**:
- `exploring-js/symbol-type.md`
- `exploring-js/symbols-as-property-keys.md`
- `exploring-js/symbols-as-constants.md`
- `exploring-js/converting-symbols.md`
- `exploring-js/publicly-known-symbols.md`
- `exploring-js/symbol-descriptions.md`
- `js-definitive-guide/well-known-symbols.md`
- `js-definitive-guide/symbol-to-string-tag.md`
- `js-definitive-guide/symbol-has-instance.md`

**Null, undefined, and absence**:
- `exploring-js/undefined-value.md`
- `exploring-js/null-value.md`
- `exploring-js/history-of-undefined-and-null.md`
- `exploring-js/checking-for-undefined-or-null.md`
- `exploring-js/undefined-null-no-properties.md`
- `exploring-js/nullish-coalescing-operator.md`
- `exploring-js/optional-chaining.md`
- `js-definitive-guide/null-vs-undefined.md`
- `js-definitive-guide/nullish-coalescing.md`
- `js-definitive-guide/optional-chaining.md`

**Number edge cases**:
- `exploring-js/number-type.md`
- `exploring-js/nan-value.md`
- `exploring-js/number-isnan.md`
- `exploring-js/number-isfinite.md`
- `exploring-js/number-isinteger.md`
- `exploring-js/safe-integers.md`
- `exploring-js/negative-zero.md`
- `exploring-js/infinity-value.md`
- `exploring-js/ieee-754-floating-point.md`
- `exploring-js/decimal-fraction-precision.md`
- `exploring-js/integer-ranges.md`
- `exploring-js/unary-plus-and-negation.md`
- `exploring-js/number-parseint.md`
- `exploring-js/bigint-type.md`
- `exploring-js/bigint-no-mixing.md`
- `exploring-js/bigint-when-to-use.md`
- `js-definitive-guide/number-type.md`
- `js-definitive-guide/bigint-type.md`

**String and boolean edge cases**:
- `exploring-js/string-type.md`
- `exploring-js/boolean-type.md`
- `exploring-js/truthy-and-falsy-values.md`
- `exploring-js/falsy-and-truthy-values.md`
- `exploring-js/truthiness-based-existence-checks.md`
- `js-definitive-guide/string-type.md`
- `js-definitive-guide/boolean-truthy-falsy.md`

**Array type checking**:
- `exploring-js/array-is-array.md`
- `exploring-js/array-like-objects.md`
- `exploring-js/array-fixed-layout-vs-sequence.md`
- `js-definitive-guide/array-isarray.md`
- `js-definitive-guide/array-like-objects.md`

**Object shape and duck typing**:
- `exploring-js/objects-overview.md`
- `exploring-js/own-property.md`
- `exploring-js/object-has-own.md`
- `exploring-js/in-operator.md`
- `exploring-js/fixed-layout-vs-dictionary-objects.md`
- `exploring-js/computed-property-keys.md`
- `deep-js/property-key.md`
- `deep-js/object-keys.md`
- `deep-js/reflect-own-keys.md`
- `deep-js/introspection.md`
- `js-definitive-guide/property-existence-testing.md`
- `js-definitive-guide/in-operator.md`
- `js-definitive-guide/objects-as-property-collections.md`

**Class-based type identity**:
- `exploring-js/class-declaration.md`
- `exploring-js/classes-evolved-from-functions.md`
- `exploring-js/subclassing.md`
- `exploring-js/mixin-classes.md`
- `exploring-js/static-factory-methods.md`
- `deep-js/private-constructor-pattern.md`
- `js-definitive-guide/abstract-classes.md`
- `js-definitive-guide/delegation-vs-inheritance.md`

**Map, Set, and typed collections**:
- `exploring-js/map-data-structure.md`
- `exploring-js/map-vs-object.md`
- `exploring-js/map-key-equality.md`
- `exploring-js/set-data-structure.md`
- `exploring-js/set-element-equality.md`
- `exploring-js/weakmap-data-structure.md`
- `exploring-js/weakmap-use-cases.md`
- `exploring-js/weakset-data-structure.md`
- `exploring-js/weakset-use-cases.md`
- `js-definitive-guide/map-class.md`
- `js-definitive-guide/weak-map.md`
- `js-definitive-guide/weak-set.md`

**Typed arrays**:
- `exploring-js/typed-arrays.md`
- `exploring-js/typed-array-element-types.md`
- `exploring-js/typed-array-vs-array.md`
- `exploring-js/array-buffer.md`
- `exploring-js/data-view.md`
- `js-definitive-guide/typed-arrays.md`
- `js-definitive-guide/data-view.md`

**Deno and Biome tooling for type safety**:
- `deno/deno-linter.md`
- `deno/deno-typescript-support.md`
- `biome/biome-linter.md`
- `biome/lint-rules.md`
- `biome/rule-pillars.md`
- `biome/types-domain.md`

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

**Runtime type checking**:
1. Use `typeof` correctly — know its quirks (`typeof null === "object"`) (MUST)
2. Use `Array.isArray()` not `typeof` or `instanceof` for arrays (MUST)
3. Use `instanceof` for class hierarchies, not for primitives (SHOULD)
4. Use `Number.isFinite()`, `Number.isNaN()`, `Number.isInteger()` — never the global versions (MUST)
5. Use `Object.hasOwn()` instead of `hasOwnProperty()` (SHOULD)
6. Duck typing — check for properties/methods, not constructor identity (SHOULD)

**Explicit type conversion**:
7. Use `Number()`, `String()`, `Boolean()` for explicit conversion (SHOULD)
8. Never use `new Number()`, `new String()`, `new Boolean()` — they create wrapper objects (MUST)
9. Use `parseInt(s, 10)` / `parseFloat(s)` for string-to-number with parsing semantics (SHOULD)
10. Avoid implicit coercion — no `+x` for number conversion, no `"" + x` for string (SHOULD)
11. Understand the `+` operator's dual nature — addition vs concatenation (MUST)

**Guarding against coercion traps**:
12. `NaN` is not equal to itself — always use `Number.isNaN()` (MUST)
13. `-0` exists and `=== 0` is true — use `Object.is()` when it matters (CONSIDER)
14. Floating point precision — `0.1 + 0.2 !== 0.3` (MUST)
15. `BigInt` cannot be mixed with `Number` in operations (MUST)

**JSDoc for static analysis**:
16. Annotate function parameters and return types with JSDoc (SHOULD)
17. Use `@typedef` for complex object shapes (SHOULD)
18. Use `@enum` for string/number constant sets (CONSIDER)
19. Use `@template` for generic patterns (CONSIDER)
20. JSDoc works with Deno's language server and VS Code — leverage it (SHOULD)

**Null and undefined discipline**:
21. Distinguish "not provided" (`undefined`) from "explicitly empty" (`null`) (SHOULD)
22. Use `??` and `?.` — they understand the null/undefined distinction (MUST)
23. Never check for `undefined` with `typeof x === "undefined"` in modern code (SHOULD)

**Discriminated unions / tagged objects**:
24. Use a `type` or `kind` property to discriminate object variants (SHOULD)
25. Use `switch` on the discriminant for exhaustive handling (SHOULD)

**Collection type safety**:
26. Use `Map<K,V>` and `Set<T>` for homogeneous collections (SHOULD)
27. Use `TypedArray` when you need fixed element types (CONSIDER)
28. Avoid heterogeneous arrays — keep element types consistent (SHOULD)

**Defensive patterns**:
29. Validate at public boundaries with typed guards (SHOULD — links to 03-error-handling)
30. Use `Object.freeze()` for enum-like constant objects (SHOULD — links to 04-values-references)

## Output

Save as: `guides/05-type-discipline.md` in the `ai-js` repo.

## Quality bar

- Every idiom must cite specific behavior described in the concept cards.
  Don't make claims the cards don't support.
- Code examples must be runnable under Deno (not Node.js).
- Good/bad examples should be realistic, not toy code.
- The tone should be terse and direct — this is a reference doc, not a
  tutorial. Match Guide 01's density and style.
- No Node.js imports or APIs in any examples.
- All cross-references must use the correct guide slugs from the list.
- The JSDoc section should show real, useful annotations — not toy
  examples. Show how JSDoc interacts with Deno's LSP and editors.
- This guide must never apologize for not using TypeScript. The position
  is: plain JS with discipline, JSDoc, and runtime validation is a
  legitimate choice. Present it confidently.

## What NOT to do

- Don't invent idioms not supported by the concept card content
- Don't include Node.js-specific patterns
- Don't include TypeScript syntax or recommend switching to TypeScript
- Don't include React/Vue framework patterns
- Don't turn this into a TypeScript tutorial or a JSDoc reference manual —
  focus on the *discipline* of writing type-safe JS
- Don't duplicate content that belongs in other guides:
  - `===` and `==` → `01-core-idioms.md`
  - API parameter validation → `02-api-design.md`
  - Error types and throwing → `03-error-handling.md`
  - Mutation and `Object.freeze()` → `04-values-references.md`
  - Coercion anti-patterns → `09-anti-patterns.md`
- Don't include Flow or other type systems — JSDoc is the only
  annotation system in scope
- Don't recommend third-party validation libraries (Zod, Yup, etc.) —
  mention they exist if relevant, but the guide is about vanilla JS
  discipline
