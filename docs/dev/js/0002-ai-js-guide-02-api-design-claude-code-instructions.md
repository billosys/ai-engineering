# ai-js Guide 02: API Design — Claude Code Instructions

## Context

We're building `ai-js`, a repo of curated JavaScript guides that Claude
Code reads via a SKILL.md entry point to produce consistently high-quality
JS code. This is modeled on our `ai-rust` repo.

Guide 01 (Core Idioms) is complete. Now we're writing Guide 02: API Design.

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

**Function signatures and parameters**:
- `exploring-js/named-parameters.md`
- `exploring-js/parameter-default-values.md`
- `exploring-js/rest-parameters.md`
- `exploring-js/parameters-vs-arguments.md`
- `exploring-js/function-roles.md`
- `exploring-js/specialized-function.md`
- `exploring-js/ordinary-function.md`
- `deep-js/named-parameters-via-destructuring.md`
- `js-definitive-guide/default-parameters.md`
- `js-definitive-guide/rest-parameters.md`

**Object design and property access**:
- `exploring-js/objects-overview.md`
- `exploring-js/object-literal.md`
- `exploring-js/computed-property-keys.md`
- `exploring-js/property-value-shorthand.md`
- `exploring-js/spreading-into-object-literals.md`
- `exploring-js/accessor-property.md`
- `exploring-js/own-property.md`
- `exploring-js/object-keys-values-entries.md`
- `exploring-js/fixed-layout-vs-dictionary-objects.md`
- `deep-js/property-attributes.md`
- `deep-js/property-descriptor.md`
- `deep-js/data-property.md`
- `deep-js/accessor-property.md`
- `deep-js/property-definition.md`
- `deep-js/property-assignment.md`
- `js-definitive-guide/object-literals.md`
- `js-definitive-guide/objects-as-property-collections.md`
- `js-definitive-guide/property-descriptors.md`
- `js-definitive-guide/getters-and-setters.md`
- `js-definitive-guide/shorthand-properties.md`
- `js-definitive-guide/shorthand-methods.md`

**Module interface design**:
- `exploring-js/ecmascript-module.md`
- `exploring-js/module-characteristics.md`
- `exploring-js/named-export.md`
- `exploring-js/default-export.md`
- `exploring-js/re-exporting.md`
- `exploring-js/live-bindings.md`
- `exploring-js/tree-shaking.md`
- `exploring-js/module-specifier.md`
- `exploring-js/dynamic-import.md`
- `js-definitive-guide/es6-module-system.md`
- `js-definitive-guide/import-export-declarations.md`
- `js-definitive-guide/es6-named-exports.md`
- `js-definitive-guide/es6-default-export.md`
- `js-definitive-guide/re-exports.md`
- `js-definitive-guide/commonjs-vs-es-modules.md`
- `eloquent-js/module-design.md`

**Classes and constructors**:
- `exploring-js/class-declaration.md`
- `exploring-js/class-expression.md`
- `exploring-js/constructor-method.md`
- `exploring-js/static-members.md`
- `exploring-js/instance-private-fields.md`
- `exploring-js/private-methods-and-accessors.md`
- `exploring-js/instance-public-fields.md`
- `exploring-js/static-initialization-blocks.md`
- `exploring-js/subclassing.md`
- `exploring-js/static-factory-methods.md`
- `deep-js/static-factory-method.md`
- `deep-js/private-constructor-pattern.md`
- `deep-js/separate-factory-function.md`
- `deep-js/clone-method.md`
- `deep-js/copy-constructor.md`
- `deep-js/async-class-initialization.md`
- `js-definitive-guide/constructor-functions.md`
- `js-definitive-guide/public-class-fields.md`
- `js-definitive-guide/private-fields.md`
- `js-definitive-guide/static-methods.md`
- `js-definitive-guide/static-fields.md`
- `js-definitive-guide/abstract-classes.md`
- `js-definitive-guide/factory-function-pattern.md`
- `js-definitive-guide/delegation-vs-inheritance.md`

**Iteration and protocol design**:
- `exploring-js/iterable-iterator.md`
- `exploring-js/iterable-interface.md`
- `exploring-js/iterator-interface.md`
- `exploring-js/iterator-result.md`
- `exploring-js/symbol-iterator.md`
- `exploring-js/iteration-protocol.md`
- `exploring-js/generator-function.md`
- `exploring-js/generator-as-iterator-implementer.md`
- `exploring-js/one-time-vs-many-times-iterable.md`
- `exploring-js/iterator-helper-methods.md`
- `exploring-js/iterator-class.md`
- `js-definitive-guide/iterable-vs-iterator.md`
- `js-definitive-guide/iterator-protocol.md`
- `js-definitive-guide/custom-iterable-objects.md`
- `js-definitive-guide/generator-functions.md`

**Return value conventions**:
- `exploring-js/return-values.md`
- `exploring-js/undefined-value.md`
- `exploring-js/null-value.md`
- `exploring-js/checking-for-undefined-or-null.md`
- `exploring-js/promise.md`
- `exploring-js/promise-states.md`
- `js-definitive-guide/null-vs-undefined.md`
- `js-definitive-guide/promise-object.md`
- `js-definitive-guide/promise-states.md`
- `eloquent-js/return-value.md`

**Naming and conventions**:
- `exploring-js/naming-conventions.md`
- `exploring-js/method-definition.md`
- `deep-js/method-naming.md`
- `deep-js/getter-setter-naming.md`
- `deep-js/function-naming-rules.md`
- `js-definitive-guide/shorthand-methods.md`

**Symbols and protocols**:
- `exploring-js/symbol-type.md`
- `exploring-js/symbols-as-property-keys.md`
- `exploring-js/publicly-known-symbols.md`
- `js-definitive-guide/well-known-symbols.md`
- `js-definitive-guide/symbol-to-string-tag.md`
- `js-definitive-guide/symbol-has-instance.md`
- `js-definitive-guide/symbol-species.md`

**Proxy and metaprogramming** (for advanced API patterns):
- `deep-js/proxy.md`
- `deep-js/proxy-handler.md`
- `deep-js/proxy-target.md`
- `deep-js/proxy-trap.md`
- `deep-js/get-trap.md`
- `deep-js/set-trap.md`
- `deep-js/facade-pattern.md`
- `deep-js/wrapper-pattern.md`
- `deep-js/membrane-pattern.md`
- `deep-js/revocable-proxy.md`
- `js-definitive-guide/reflect-api.md`
- `js-definitive-guide/proxy-invariants.md`

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

**Function signature design**:
1. Options objects for functions with >2-3 parameters (SHOULD)
2. Per-property defaults with `= {}` outer default (SHOULD)
3. Positional args for required params, options for optional (SHOULD)
4. Return consistent types — don't return string-or-null-or-array (MUST)
5. Accept iterables, return arrays (CONSIDER)

**Module interface design**:
6. One module, one responsibility (SHOULD)
7. Export functions, not objects with methods (SHOULD)
8. Re-export for public API surfaces (barrel modules) (CONSIDER)
9. Keep module-level side effects to zero (MUST)
10. Use `export` at declaration, not a bottom-of-file export list (SHOULD)

**Constructor and factory patterns**:
11. Prefer factory functions over classes for simple data (SHOULD)
12. Use `#private` fields, not `_convention` (MUST)
13. Static factory methods for alternative construction (SHOULD)
14. Async initialization — factory function, not async constructor (MUST)
15. Throw in constructors for invalid arguments (MUST)

**Naming and conventions**:
16. Method names are verbs, property names are nouns (SHOULD)
17. Boolean-returning methods start with `is`, `has`, `can`, `should` (SHOULD)
18. Conversion methods: `toX()` creates new, `asX()` is a view (SHOULD)
19. Private methods and fields use `#` prefix (MUST)

**Iteration and protocol design**:
20. Implement `Symbol.iterator` for custom collections (SHOULD)
21. Use generators to simplify iterator implementation (SHOULD)
22. Prefer many-times iterables over one-time (SHOULD)

**Return value and error conventions**:
23. Return `undefined` for "no meaningful value" (SHOULD)
24. Return `null` only when the API explicitly models absence (CONSIDER)
25. Never return different types from the same function (MUST)
26. Async functions always return Promises — no callback alternatives (MUST)

**Advanced patterns** (CONSIDER-level):
27. Use symbols for non-enumerable metadata properties
28. Proxy-based validation at API boundaries
29. Builder pattern for complex object construction

## Output

Save as: `guides/02-api-design.md` in the `ai-js` repo.

## Quality bar

- Every idiom must cite specific behavior described in the concept cards.
  Don't make claims the cards don't support.
- Code examples must be runnable under Deno (not Node.js).
- Good/bad examples should be realistic, not toy code.
- The tone should be terse and direct — this is a reference doc, not a
  tutorial. Match Guide 01's density and style.
- No Node.js imports or APIs in any examples.
- All cross-references must use the correct guide slugs from the list.
- Aim for 20-30 idioms. More is fine if the cards support it, but don't
  pad.

## What NOT to do

- Don't invent idioms not supported by the concept card content
- Don't include Node.js-specific patterns
- Don't include React/Vue/framework patterns — this is vanilla JS
- Don't include TypeScript-specific patterns (use JSDoc instead)
- Don't duplicate content that belongs in other guides:
  - Error handling patterns → `03-error-handling.md`
  - Mutation/copying discipline → `04-values-references.md`
  - Closure patterns → `06-functions-closures.md`
  - Async patterns → `07-async-concurrency.md`
  - Performance concerns → `08-performance.md`
- Don't include browser DOM API design patterns
