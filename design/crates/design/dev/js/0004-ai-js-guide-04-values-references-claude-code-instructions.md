# ai-js Guide 04: Values & References — Claude Code Instructions

## Context

We're building `ai-js`, a repo of curated JavaScript guides that Claude
Code reads via a SKILL.md entry point to produce consistently high-quality
JS code. This is modeled on our `ai-rust` repo.

Guides 01 (Core Idioms), 02 (API Design), and 03 (Error Handling) are
complete. Now we're writing Guide 04: Values & References.

This guide is the JS equivalent of the Rust guide on ownership and
borrowing. JS doesn't have Rust's ownership model, but it has its own
discipline around values vs references, mutation, copying, and shared
state that is equally important to get right. This guide should make
a developer *think* about these things the way Rust forces you to.

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

**Primitive vs object fundamentals**:
- `exploring-js/primitive-values.md`
- `exploring-js/primitives-are-immutable.md`
- `exploring-js/primitives-compared-by-value.md`
- `exploring-js/primitives-passed-by-value.md`
- `exploring-js/objects-are-mutable.md`
- `exploring-js/objects-compared-by-identity.md`
- `exploring-js/objects-passed-by-identity.md`
- `exploring-js/pass-by-identity-vs-pass-by-reference.md`
- `exploring-js/javascript-types.md`
- `exploring-js/javascript-type-hierarchy.md`
- `exploring-js/value-identity.md`
- `exploring-js/value-preservation.md`
- `js-definitive-guide/primitive-vs-object-types.md`
- `eloquent-js/object.md`
- `eloquent-js/property.md`

**Const, let, and binding vs value**:
- `exploring-js/const-vs-let.md`
- `exploring-js/const-immutability.md`
- `exploring-js/const-and-loops.md`
- `exploring-js/variable-binding.md`
- `deep-js/variable-pattern.md`

**Shallow copying**:
- `deep-js/shallow-copy.md`
- `deep-js/spreading-arrays.md`
- `deep-js/spreading-objects.md`
- `deep-js/object-assign.md`
- `deep-js/spreading-enumerability.md`
- `deep-js/spreading-for-non-destructive-updates.md`
- `exploring-js/array-copying.md`
- `exploring-js/spreading-into-object-literals.md`
- `exploring-js/array-spreading.md`
- `exploring-js/object-assign.md`
- `js-definitive-guide/object-assign.md`
- `js-definitive-guide/spread-operator-in-object-literals.md`

**Deep copying**:
- `deep-js/deep-copy.md`
- `deep-js/generic-deep-copy.md`
- `deep-js/recursive-deep-copying.md`
- `deep-js/json-deep-copy.md`
- `deep-js/nested-spreading-deep-copy.md`
- `exploring-js/structured-clone.md`
- `exploring-js/normal-comparison-vs-deep-comparison.md`

**Shared mutable state**:
- `deep-js/shared-mutable-state.md`
- `deep-js/three-strategies-for-shared-state.md`
- `deep-js/aliasing.md`
- `deep-js/immutability-for-shared-state.md`
- `deep-js/collection-immutability.md`

**Defensive copying**:
- `deep-js/defensive-copying.md`
- `deep-js/defensive-copying-input.md`
- `deep-js/defensive-copying-output.md`
- `deep-js/non-destructive-update-as-defense.md`

**Non-destructive updates**:
- `deep-js/non-destructive-update.md`
- `deep-js/non-destructive-array-update.md`
- `deep-js/destructive-update.md`
- `deep-js/copying-to-updating-to-state-progression.md`
- `deep-js/manual-deep-update.md`
- `deep-js/generic-deep-update.md`
- `exploring-js/array-destructive-vs-nondestructive.md`
- `exploring-js/array-nondestructive-prepend-append.md`

**Object.freeze and protection levels**:
- `deep-js/object-freeze.md`
- `deep-js/shallow-freezing.md`
- `deep-js/deep-freezing.md`
- `deep-js/object-seal.md`
- `deep-js/object-prevent-extensions.md`
- `deep-js/protection-levels.md`
- `deep-js/object-is-frozen.md`
- `deep-js/object-is-sealed.md`
- `deep-js/object-is-extensible.md`
- `deep-js/extensible-internal-slot.md`
- `js-definitive-guide/object-freeze.md`

**Immutable wrappers and libraries**:
- `deep-js/immutable-wrapper.md`
- `deep-js/immutable-map-wrapper.md`
- `deep-js/proxy-based-immutable-array.md`
- `deep-js/immutable-js-library.md`
- `deep-js/immer-library.md`

**Property descriptors and definition vs assignment**:
- `deep-js/property-attributes.md`
- `deep-js/property-descriptor.md`
- `deep-js/data-property-descriptor.md`
- `deep-js/accessor-property-descriptor.md`
- `deep-js/data-property.md`
- `deep-js/accessor-property.md`
- `deep-js/property-definition.md`
- `deep-js/property-assignment.md`
- `deep-js/define-property-semantics.md`
- `deep-js/assignment-operator-semantics.md`
- `deep-js/assignment-calls-setters.md`
- `deep-js/assignment-creates-all-true-attributes.md`
- `deep-js/descriptor-defaults-on-creation.md`
- `deep-js/constructs-using-definition-vs-assignment.md`
- `deep-js/inherited-read-only-prevents-assignment.md`
- `deep-js/built-in-property-attributes.md`
- `deep-js/configurable-attribute.md`
- `deep-js/writable-attribute.md`
- `deep-js/enumerable-attribute.md`
- `deep-js/value-attribute.md`
- `deep-js/get-attribute.md`
- `deep-js/set-attribute.md`
- `exploring-js/own-property.md`
- `exploring-js/accessor-property.md`
- `js-definitive-guide/property-descriptors.md`
- `js-definitive-guide/property-attributes.md`
- `js-definitive-guide/object-define-property.md`
- `js-definitive-guide/getters-and-setters.md`

**Enumerability**:
- `deep-js/enumerability.md`
- `deep-js/enumerability-use-cases.md`
- `deep-js/pre-defined-enumerability.md`
- `deep-js/json-stringify-enumerability.md`
- `deep-js/object-assign-enumerability.md`
- `deep-js/spreading-enumerability.md`
- `deep-js/property-listing-operations.md`
- `deep-js/for-in-loop.md`
- `exploring-js/enumerability.md`
- `js-definitive-guide/enumerating-properties.md`

**Prototype chain and property lookup**:
- `deep-js/prototype-internal-slot.md`
- `deep-js/prototype-chain-and-assignment.md`
- `exploring-js/proto-vs-prototype.md`
- `exploring-js/prototype-chain.md`
- `js-definitive-guide/prototype-chain.md`
- `js-definitive-guide/prototype-based-inheritance.md`
- `js-definitive-guide/prototype-objects.md`

**Instance copying**:
- `deep-js/instance-copying-techniques.md`
- `deep-js/clone-method.md`
- `deep-js/copy-constructor.md`
- `deep-js/prototype-borrowing-factory.md`
- `deep-js/property-descriptor-copying.md`

**Equality and comparison**:
- `deep-js/strict-equality-comparison.md`
- `exploring-js/strict-equality.md`
- `exploring-js/object-is.md`
- `exploring-js/normal-comparison-vs-deep-comparison.md`

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

**Primitives vs objects — the fundamental split**:
1. Primitives are immutable values; objects are mutable references (MUST)
2. Primitives compare by value; objects compare by identity (MUST)
3. "Pass by identity" not "pass by reference" — use Rauschmayer's terminology (SHOULD)
4. `typeof` and its quirks — `typeof null === "object"` (MUST)

**Binding vs value**:
5. `const` freezes the binding, not the value (MUST — reinforces 01-core-idioms ID-14)
6. Reassignment vs mutation — know which you're doing (MUST)

**Shallow copying**:
7. Spread for shallow copies of objects and arrays (SHOULD)
8. `Object.assign()` vs spread — when to use which (CONSIDER)
9. Shallow copies share nested references — know the consequences (MUST)

**Deep copying**:
10. `structuredClone()` for deep copies (SHOULD — reinforces 01-core-idioms ID-23)
11. JSON round-trip is NOT a reliable deep copy (MUST)
12. When deep copying is unnecessary — prefer non-destructive updates (SHOULD)

**Mutation discipline**:
13. Don't mutate function arguments — copy first (MUST)
14. Defensive copying at module boundaries — copy input and output (SHOULD)
15. Non-destructive updates — spread to create modified copies (SHOULD)
16. Destructive array methods vs non-destructive alternatives (SHOULD)
17. Prefer `Array.prototype.toSorted()`, `.toReversed()`, `.with()` (SHOULD)

**Object protection**:
18. `Object.freeze()` — shallow protection (SHOULD)
19. `Object.seal()` vs `Object.freeze()` vs `Object.preventExtensions()` (CONSIDER)
20. Deep freeze patterns — recursive freezing (CONSIDER)
21. Frozen objects as lookup tables and configuration (SHOULD)

**Property mechanics**:
22. Definition vs assignment — they are not the same (SHOULD)
23. Property descriptors — `writable`, `enumerable`, `configurable` (CONSIDER)
24. Getters and setters — computed properties with side-effect control (SHOULD)
25. Enumerability matters — what shows up in `for-in`, spread, `Object.keys()` (SHOULD)

**Equality and identity**:
26. `===` compares identity for objects, value for primitives (MUST)
27. `Object.is()` for edge cases — `NaN`, `-0` (CONSIDER)
28. Deep equality requires manual or library implementation (SHOULD)

**Prototype chain awareness**:
29. Own properties vs inherited properties — use `Object.hasOwn()` (SHOULD)
30. Prototype chain affects property lookup but NOT assignment (MUST)

## Output

Save as: `guides/04-values-references.md` in the `ai-js` repo.

## Quality bar

- Every idiom must cite specific behavior described in the concept cards.
  Don't make claims the cards don't support.
- Code examples must be runnable under Deno (not Node.js).
- Good/bad examples should be realistic, not toy code.
- The tone should be terse and direct — this is a reference doc, not a
  tutorial. Match Guide 01's density and style.
- No Node.js imports or APIs in any examples.
- All cross-references must use the correct guide slugs from the list.
- This guide has the heaviest Deep JS card load — lean into
  Rauschmayer's terminology and mental models. His "pass by identity"
  framing and the three strategies for shared state are the conceptual
  backbone of this guide.

## What NOT to do

- Don't invent idioms not supported by the concept card content
- Don't include Node.js-specific patterns
- Don't include React/Vue state management patterns (no `useState`,
  no Redux, no Vuex)
- Don't include TypeScript-specific patterns
- Don't include Immer or Immutable.js recommendations — mention them
  as "libraries exist" but don't advocate for them. This guide is about
  vanilla JS discipline.
- Don't duplicate content that belongs in other guides:
  - Function parameter patterns → `02-api-design.md`
  - Error handling → `03-error-handling.md`
  - Closure captures → `06-functions-closures.md`
  - Performance of copying → `08-performance.md`
  - Common mutation bugs → `09-anti-patterns.md`
- Don't turn this into a tutorial on how objects work. The audience is
  an experienced developer (or an AI writing code for one). Focus on
  decisions and discipline, not fundamentals.
