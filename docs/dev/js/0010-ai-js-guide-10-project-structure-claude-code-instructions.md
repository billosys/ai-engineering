# ai-js Guide 10: Project Structure — Claude Code Instructions

## Context

We're building `ai-js`, a repo of curated JavaScript guides that Claude
Code reads via a SKILL.md entry point to produce consistently high-quality
JS code. This is modeled on our `ai-rust` repo.

Guides 01–09 are complete. Now we're writing Guide 10: Project Structure.

This guide covers how to organize a JavaScript project for clarity,
maintainability, and tooling compatibility: directory layout, file
naming, module dependency flow, entry points, configuration placement,
separation of concerns at the file/directory level, and the conventions
that make a project navigable by both humans and tools.

This is explicitly NOT a guide about module API design (Guide 02
covers that), Deno runtime mechanics (Guide 12), Biome configuration
(Guide 13), or Node.js avoidance (Guide 14). This guide covers the
*structural skeleton* — the decisions you make before writing the first
line of application code.

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

**ESM module system**:
- `exploring-js/ecmascript-module.md`
- `exploring-js/module-characteristics.md`
- `exploring-js/module-specifier.md`
- `exploring-js/scripts-vs-modules.md`
- `exploring-js/named-export.md`
- `exploring-js/named-import.md`
- `exploring-js/default-export.md`
- `exploring-js/default-import.md`
- `exploring-js/namespace-import.md`
- `exploring-js/re-exporting.md`
- `exploring-js/dynamic-import.md`
- `exploring-js/import-meta.md`
- `exploring-js/tree-shaking.md`
- `exploring-js/bundlers.md`
- `js-definitive-guide/es6-module-system.md`
- `js-definitive-guide/es6-import-statement.md`
- `js-definitive-guide/es6-named-exports.md`
- `js-definitive-guide/es6-default-export.md`
- `js-definitive-guide/import-export-declarations.md`
- `js-definitive-guide/renaming-imports-exports.md`
- `js-definitive-guide/re-exports.md`
- `js-definitive-guide/import-meta-url.md`
- `js-definitive-guide/dynamic-import.md`
- `js-definitive-guide/script-type-module.md`
- `js-definitive-guide/commonjs-vs-es-modules.md`
- `js-definitive-guide/tree-shaking.md`
- `js-definitive-guide/code-bundlers.md`
- `eloquent-js/module.md`
- `eloquent-js/module-design.md`
- `eloquent-js/es-module.md`
- `eloquent-js/import-declaration.md`
- `eloquent-js/export-declaration.md`
- `eloquent-js/named-export.md`
- `eloquent-js/default-export.md`
- `eloquent-js/dependency.md`
- `eloquent-js/bundler.md`

**Module scope and isolation**:
- `deep-js/module-scope.md`
- `deep-js/default-export-naming.md`
- `exploring-js/global-object.md`
- `js-definitive-guide/global-object.md`

**Naming conventions**:
- `exploring-js/naming-conventions.md`
- `deep-js/function-naming-rules.md`
- `deep-js/default-export-naming.md`
- `deep-js/arrow-function-naming.md`
- `deep-js/method-naming.md`

**Deno project configuration**:
- `deno/deno-configuration.md`
- `deno/deno-workspaces.md`
- `deno/deno-import-maps.md`
- `deno/deno-task.md`
- `deno/deno-test-runner.md`
- `deno/deno-standard-library.md`
- `deno/deno-permissions-system.md`
- `deno/deno-npm-specifiers.md`
- `deno/deno-package-json-support.md`
- `deno/ecmascript-modules.md`
- `deno/jsr-registry.md`
- `deno/deno-in-ci.md`

**Testing structure**:
- `exploring-js/unit-testing.md`
- `exploring-js/assertions.md`
- `exploring-js/async-tests.md`
- `deno/deno-test-runner.md`
- `eloquent-js/testing.md`

**Scope, closures, and isolation** (structural implications):
- `deep-js/scope-chain.md`
- `deep-js/nested-scopes-via-environments.md`
- `deep-js/lexical-scope.md`
- `exploring-js/variable-scope.md`
- `exploring-js/declarations-scope-activation.md`

## Structural template

Follow the same format as the existing guides (01–09):

Each idiom entry has:
```
## ID-XX: [Title]

**Strength**: MUST | SHOULD | CONSIDER

**Summary**: One sentence.

[Code examples, directory trees, or configuration snippets with
// Good and // Bad labels]

**Rationale**: Why this matters. Cite concept card sources.

**See also**: Cross-references to other IDs or guides
```

End with:
- Quick Reference Table
- Related Guidelines — use the format introduced in Guide 09:
  list specific ID numbers per guide so readers can navigate directly
  (e.g., "See `02-api-design.md` for ID-06, 07, 08, 09 (module
  interface design)"). This is more useful than vague cross-references.
- External References

## Proposed idiom list

This is a starting outline — adjust based on what the concept cards
emphasize. Add idioms if the cards reveal important patterns. Remove
or merge if redundant. Aim for 20-30 idioms.

This guide is lighter than 01–09 because project structure conventions
are less language-spec-dense and more about practical organization.
The concept cards will have less to say about directory layout than
about, say, Promise semantics — that's expected. Ground claims in the
module system cards where possible, and in Deno tooling cards for
Deno-specific conventions.

### Directory layout

1. Flat-by-feature, not nested-by-type — group by domain, not by
   `controllers/`, `models/`, `utils/` (SHOULD)
2. Keep the root clean — config files at root, source code in `src/`
   or at top level, tests alongside or in `tests/` (SHOULD)
3. Reference directory structure for a Deno project (SHOULD)

### File naming

4. kebab-case for file and directory names (SHOULD)
5. One module, one purpose — each file should have a clear single
   responsibility (SHOULD — amplifies 02 ID-06)
6. Name files after their primary export (SHOULD)
7. Test files: `foo_test.js` or `foo.test.js` — Deno convention
   (SHOULD)

### Entry points and public API

8. Explicit entry point: `mod.js` (Deno convention) or `main.js`
   (SHOULD)
9. Barrel files for public API surfaces — selective re-exports only
   (SHOULD — amplifies 02 ID-08)
10. Avoid deep imports into internal modules — publish a public surface
    (SHOULD)

### Module dependency flow

11. Dependency direction: depend inward, not outward — inner modules
    should not import from outer layers (MUST)
12. No circular imports — they cause subtle initialization bugs in
    ESM (MUST)
13. Limit import depth — if you're importing
    `../../utils/helpers/strings.js`, restructure (SHOULD)
14. Separate pure logic from I/O — keep core logic importable without
    side effects (SHOULD — amplifies 08 ID-31)

### Configuration

15. `deno.json` as the single config source — tasks, imports, lint,
    fmt, test (SHOULD)
16. Import maps for dependency aliases — readable imports, centralized
    versions (SHOULD)
17. Environment-specific config via environment variables, not
    conditional imports (SHOULD)

### Constants, types, and shared definitions

18. Centralize shared constants in a dedicated module (SHOULD)
19. JSDoc type definitions: co-locate with the code that uses them,
    or centralize in `types.js` for shared types (CONSIDER)

### Test structure

20. Co-locate tests with source or mirror the source tree in `tests/`
    — pick one convention, be consistent (SHOULD)
21. Test file naming: `*_test.js` for Deno's test runner auto-discovery
    (SHOULD)
22. Separate test utilities into a `testing/` or `test_utils/` module
    (CONSIDER)

### Dependency management

23. Pin dependency versions — use `deno.lock` for reproducible builds
    (SHOULD)
24. Prefer `jsr:` specifiers over `npm:` where available (CONSIDER)
25. Vendor dependencies for offline builds or CI stability (CONSIDER)

### Workspaces and monorepos

26. Deno workspaces for multi-package projects — shared config,
    independent dependencies (CONSIDER)

## Boundaries with other guides

**Guide 02 (API Design)** already covers:
- One module, one responsibility (02 ID-06)
- Named exports over default (02 ID-07)
- Re-exports / barrel files (02 ID-08)
- Module interface design (02 ID-09)

**Guide 08 (Performance)** already covers:
- Named exports for tree shaking (08 ID-30)
- Side-effect-free modules (08 ID-31)

**Guide 12 (Deno)** will cover in detail:
- `deno.json` configuration options
- `Deno.test()` API and runner details
- `deno task` runner
- Publishing to JSR

**Guide 13 (Biome)** will cover:
- `biome.json` setup and rules
- Lint/format configuration

**Guide 14 (No-Node Boundary)** will cover:
- Why no `package.json`, no `node_modules`, no npm scripts
- Migration patterns from Node.js projects

**Do NOT re-teach these.** Cross-reference them. This guide covers the
*structural layout and organizational decisions* — where files go, how
they're named, how dependencies flow between modules, and how to set
up a project skeleton. It should reference the other guides for the
"how" of each specific tool or API.

## Output

Save as: `guides/10-project-structure.md` in the `ai-js` repo.

## Quality bar

- Every idiom must cite specific behavior or recommendation from the
  concept cards where possible. For structural conventions (directory
  layout, file naming) that the concept cards don't cover directly,
  ground the recommendation in Deno ecosystem conventions and the
  Deno tooling cards.
- Directory tree examples should use ASCII art (`├── `, `└── `, etc.)
  and show realistic, non-trivial project structures.
- Code examples must be runnable under Deno (not Node.js).
- The tone should be terse and direct — this is a reference doc, not
  a tutorial. Match the existing guides' density and style.
- No Node.js patterns in any examples (no `package.json`, no
  `node_modules/`, no `src/index.ts`).
- All cross-references must use the correct guide slugs from the list.
- The circular import entry (ID-12) is critical — ESM circular imports
  cause hard-to-debug initialization bugs that the concept cards
  document. Explain the mechanism clearly.
- The flat-by-feature layout recommendation should show both the
  recommended structure and the anti-pattern (nested-by-type) with
  concrete examples of why the anti-pattern causes problems (shotgun
  surgery, scattered imports).
- This guide will be shorter than guides 01–08 because project
  structure has less language-spec depth. That's fine — aim for 20–26
  well-grounded idioms rather than padding to 30+.

## What NOT to do

- Don't invent idioms not supported by the concept cards or Deno
  tooling conventions
- Don't include Node.js project conventions (`package.json` scripts,
  `node_modules`, `src/index.js`, `.eslintrc`, `.prettierrc`)
- Don't include React/Vue/Next.js project structures (no `pages/`,
  no `components/`, no `app/` router)
- Don't include TypeScript-specific patterns (`tsconfig.json`,
  `.d.ts` organization, `paths` mapping)
- Don't duplicate content from Guide 02 (module API design) or
  Guide 12 (Deno runtime details) — cross-reference them
- Don't prescribe a single "correct" directory layout dogmatically
  — present the principles (feature cohesion, dependency direction,
  clean root) and show one or two concrete layouts that embody them
- Don't include monorepo tooling comparisons (no Nx, no Turborepo,
  no Lerna) — Deno workspaces are the only monorepo tool in scope
- Don't include Docker, CI/CD pipeline configuration, or deployment
  structure — those are operational concerns, not project structure
- Don't include patterns that are purely aesthetic preference with
  no functional impact — every recommendation should explain what
  goes wrong if you violate it
- Don't pad the guide with obvious advice ("use meaningful file
  names") — every entry should address a decision point where
  reasonable developers might disagree or get it wrong
