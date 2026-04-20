# ai-js Guide 01: Core JavaScript Idioms — Claude Code Instructions

## Context

We're building `ai-js`, a collection of curated JavaScript guides that Claude
Code reads via a SKILL.md entry point to produce consistently high-quality
JS code. This is modeled on our `ai-rust` repo which has dramatically
improved Rust code quality.

The target environment is:
- **Deno** (not Node.js — no `require()`, no `node_modules`, no npm scripts)
- **Biome** for linting and formatting (not ESLint, not Prettier)
- **ESM-only** (`import`/`export`, no CommonJS)
- **No TypeScript** (plain JS with JSDoc where needed)
- This is the JS used in the **lykn** project (s-expression syntax for JS)

## Reference material

You have a concept card library with 1,569 cards across seven sources.
These are your authoritative references — the guide must be grounded
in what the cards say, not in general knowledge.

The cards live in the `ai-js` repo under `concept-cards/`:

| Directory | Source | Cards |
|-----------|--------|-------|
| `concept-cards/exploring-js/` | Exploring JavaScript (ES2025) — Rauschmayer | 476 |
| `concept-cards/js-definitive-guide/` | JavaScript: The Definitive Guide 7e — Flanagan | 341 |
| `concept-cards/eloquent-js/` | Eloquent JavaScript 4e — Haverbeke | 330 |
| `concept-cards/deep-js/` | Deep JavaScript — Rauschmayer | 248 |
| `concept-cards/deno/` | Deno documentation | 65 |
| `concept-cards/eslint/` | ESLint documentation | 62 |
| `concept-cards/biome/` | Biome documentation | 54 |

## Structural template

Read `workbench/guides/01-core-idioms.md` copied from the `ai-rust` repo. This is the
structural template. The JS guide should follow the same format:

- Numbered IDs: `ID-01`, `ID-02`, etc.
- Strength levels: **MUST**, **SHOULD**, **CONSIDER**
- Each idiom has: Summary, code examples (good and bad), Rationale
- Code examples use `// Good` / `// Bad` labels
- Cross-references to other guides using `See also:`
- A quick reference table at the end
- Related guidelines section pointing to other guide numbers

## Task

Build `guides/js/01-core-idioms.md`.

### Step 1: Read concept cards

Read the following concept cards to gather authoritative content. Don't
skip this step — the guide must be derived from the cards.

**Declarations and scoping** (read all of these):
- `exploring-js/const-vs-let.md`
- `exploring-js/const-immutability.md`
- `exploring-js/const-and-loops.md`
- `exploring-js/let-declaration.md`
- `exploring-js/var-declaration.md`
- `exploring-js/block-scoping.md`
- `exploring-js/temporal-dead-zone.md`
- `exploring-js/hoisting.md`
- `exploring-js/variable-scope.md`
- `exploring-js/declarations-scope-activation.md`
- `deep-js/lexical-scope.md`
- `deep-js/scope-chain.md`
- `eloquent-js/let-declaration.md`
- `eloquent-js/const-declaration.md`
- `eloquent-js/var-declaration.md`
- `js-definitive-guide/block-scope.md`
- `js-definitive-guide/var-declarations.md`
- `js-definitive-guide/hoisting.md`

**Equality and comparison**:
- `exploring-js/strict-equality-operator.md`
- `exploring-js/strict-equality.md`
- `exploring-js/loose-equality-operator.md`
- `exploring-js/truthy-and-falsy-values.md`
- `exploring-js/truthiness-based-existence-checks.md`
- `exploring-js/checking-for-undefined-or-null.md`
- `exploring-js/nullish-coalescing-operator.md`
- `exploring-js/optional-chaining.md`
- `deep-js/strict-equality-comparison.md`
- `deep-js/abstract-equality-comparison.md`
- `deep-js/type-coercion.md`
- `eloquent-js/strict-equality.md`
- `eloquent-js/type-coercion.md`
- `js-definitive-guide/strict-equality-operator.md`
- `js-definitive-guide/strict-vs-loose-equality.md`
- `js-definitive-guide/boolean-truthy-falsy.md`
- `js-definitive-guide/nullish-coalescing.md`
- `js-definitive-guide/optional-chaining.md`

**Destructuring**:
- `exploring-js/destructuring.md`
- `exploring-js/object-destructuring.md`
- `exploring-js/array-destructuring.md`
- `exploring-js/destructuring-default-values.md`
- `exploring-js/destructuring-parameters.md`
- `exploring-js/nested-destructuring.md`
- `exploring-js/destructuring-swapping-variables.md`
- `exploring-js/rest-parameters.md`
- `exploring-js/rest-elements.md`
- `exploring-js/spread-syntax.md`
- `deep-js/named-parameters-via-destructuring.md`
- `deep-js/nested-destructuring.md`
- `deep-js/rest-element.md`
- `js-definitive-guide/rest-parameters.md`
- `js-definitive-guide/default-parameters.md`

**Template literals**:
- `exploring-js/template-literal.md`
- `exploring-js/string-interpolation.md`
- `exploring-js/multiline-template-literals.md`
- `exploring-js/tagged-template.md`
- `exploring-js/cooked-vs-raw-template-strings.md`
- `js-definitive-guide/template-literals.md`
- `js-definitive-guide/tagged-template-literals.md`

**Naming conventions**:
- `exploring-js/naming-conventions.md`
- `exploring-js/identifiers.md`
- `exploring-js/reserved-words.md`
- `js-definitive-guide/case-sensitivity.md`
- `deep-js/method-naming.md`
- `deep-js/function-naming-rules.md`
- `deep-js/getter-setter-naming.md`

**Modules (ESM)**:
- `exploring-js/ecmascript-module.md`
- `exploring-js/scripts-vs-modules.md`
- `exploring-js/module-specifier.md`
- `exploring-js/module-characteristics.md`
- `exploring-js/named-export.md`
- `exploring-js/named-import.md`
- `exploring-js/default-export.md`
- `exploring-js/default-import.md`
- `exploring-js/re-exporting.md`
- `exploring-js/live-bindings.md`
- `exploring-js/tree-shaking.md`
- `js-definitive-guide/es6-module-system.md`
- `js-definitive-guide/commonjs-vs-es-modules.md`
- `js-definitive-guide/import-export-declarations.md`
- `js-definitive-guide/script-type-module.md`
- `eloquent-js/es-module.md`
- `eloquent-js/named-export.md`
- `eloquent-js/default-export.md`

**Functions — arrow vs function vs lambda**:
- `exploring-js/arrow-function-expressions.md`
- `exploring-js/arrow-function.md`
- `exploring-js/ordinary-function.md`
- `exploring-js/function-declarations.md`
- `exploring-js/function-declaration-vs-expression.md`
- `exploring-js/function-roles.md`
- `exploring-js/specialized-function.md`
- `exploring-js/iife.md`
- `exploring-js/closures.md`
- `exploring-js/this-keyword.md`
- `exploring-js/this-in-various-contexts.md`
- `exploring-js/shadowing-this.md`
- `js-definitive-guide/arrow-functions.md`
- `js-definitive-guide/arrow-function-this-inheritance.md`
- `js-definitive-guide/function-declarations.md`
- `js-definitive-guide/function-expressions.md`
- `js-definitive-guide/this-keyword-binding.md`
- `js-definitive-guide/nested-functions.md`
- `js-definitive-guide/higher-order-functions.md`
- `js-definitive-guide/iifes.md`
- `eloquent-js/arrow-function.md`
- `eloquent-js/function-declaration.md`
- `eloquent-js/function-definition.md`
- `eloquent-js/functions-as-values.md`

**Values, types, and mutation**:
- `exploring-js/primitive-values.md`
- `exploring-js/primitives-are-immutable.md`
- `exploring-js/primitives-compared-by-value.md`
- `exploring-js/objects-are-mutable.md`
- `exploring-js/objects-compared-by-identity.md`
- `exploring-js/objects-passed-by-identity.md`
- `exploring-js/pass-by-identity-vs-pass-by-reference.md`
- `exploring-js/const-immutability.md`
- `exploring-js/javascript-types.md`
- `exploring-js/javascript-type-hierarchy.md`
- `deep-js/shared-mutable-state.md`
- `deep-js/shallow-copy.md`
- `deep-js/deep-copy.md`
- `deep-js/defensive-copying.md`
- `deep-js/non-destructive-update.md`
- `deep-js/immutability-for-shared-state.md`
- `deep-js/three-strategies-for-shared-state.md`
- `js-definitive-guide/primitive-vs-object-types.md`
- `js-definitive-guide/object-freeze.md`

**Deno-specific**:
- `deno/deno.md`
- `deno/ecmascript-modules.md`
- `deno/deno-configuration.md`
- `deno/deno-permissions-system.md`
- `deno/deno-linter.md`
- `deno/deno-formatter.md`

**Biome-specific**:
- `biome/biome.md`
- `biome/biome-linter.md`
- `biome/biome-formatter.md`
- `biome/lint-rules.md`
- `biome/rule-pillars.md`
- `biome/opinionated-formatting.md`

### Step 2: Read the Rust template

Read `guides/01-core-idioms.md` from the `ai-rust` repo (if accessible)
for structural reference. If not accessible, use this structure:

Each idiom entry has:
```
## ID-XX: [Title]

**Strength**: MUST | SHOULD | CONSIDER

**Summary**: One sentence.

[Code examples with // Good and // Bad labels]

**Rationale**: Why this matters.

**See also**: Cross-references
```

### Step 3: Write the guide

Create `guides/01-core-idioms.md` with the following idioms. The list
below is a starting outline — adjust based on what the concept cards
emphasize. Add idioms if the cards reveal important patterns I missed.
Remove or merge idioms if they're redundant.

Proposed idiom list (adjust as needed):

1. **`const` by default, `let` when needed, never `var`** (MUST)
2. **Always use `===` and `!==`** (MUST)
3. **Use `??` for nullish defaults, not `||`** (SHOULD)
4. **Use optional chaining `?.` for safe property access** (SHOULD)
5. **Prefer template literals over string concatenation** (SHOULD)
6. **Destructure at the point of use** (SHOULD)
7. **Use named exports, avoid default exports** (SHOULD)
8. **ESM only — no CommonJS, no `require()`** (MUST)
9. **Arrow functions for callbacks, `function` for declarations** (SHOULD)
10. **Avoid `this` unless in classes or methods** (SHOULD)
11. **All magic values must be documented** (MUST) — adapted from Rust
12. **Naming: camelCase for variables/functions, PascalCase for classes** (MUST)
13. **Avoid weasel words in names** (MUST) — adapted from Rust
14. **`const` does not mean immutable** — explain the distinction (MUST)
15. **Prefer `Object.freeze()` for true constant objects** (CONSIDER)
16. **Prefer `Map`/`Set` over plain objects for dynamic collections** (SHOULD)
17. **Use rest parameters instead of `arguments`** (MUST)
18. **Use spread syntax instead of `apply()`** (SHOULD)
19. **Explicit returns in arrow functions — use block body when >1 statement** (SHOULD)
20. **No Node.js — use Deno APIs and Web Platform APIs** (MUST)

In the event of conflicting examples, weight concepts using the following order of importance:

1. concept-cards/exploring-js - MOST important
2. concept-cards/deep-js
3. concept-cards/js-definitive-guide
4. concept-cards/eloquent-js - LEAST important

### Step 4: Add summary table and cross-references

End the guide with:
- A quick reference table (like the Rust guide)
- Related guidelines pointing to the other `ai-js` guide numbers
- External references (Deno docs, Biome docs, MDN)

## Output

Save as: `guides/js/01-core-idioms.md` in the `ai-js` repo.

## Quality bar

- Every idiom must cite specific behavior described in the concept cards.
  Don't make claims the cards don't support.
- Code examples must be runnable under Deno (not Node.js).
- Good/bad examples should be realistic, not toy code.
- The tone should be terse and direct — this is a reference doc, not a
  tutorial. Match the Rust guide's density.
- Aim for 20-30 idioms. More is fine if the cards support it, but don't
  pad.

## What NOT to do

- Don't invent idioms not supported by the concept card content
- Don't include Node.js-specific patterns (no `require`, no `process.env`
  without Deno equivalent, no `__dirname`)
- Don't include React/Vue/framework patterns — this is vanilla JS
- Don't include TypeScript-specific patterns
- Don't duplicate content that belongs in other guides (error handling
  goes in guide 03, async patterns in guide 07, etc.)
- Don't include browser DOM patterns — this is runtime-agnostic JS
  (Deno-first)
