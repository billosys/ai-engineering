# ai-js Guide 12-04: Deno Publishing — Claude Code Instructions

## Context

We're building `ai-js`, a repo of curated JavaScript guides that Claude
Code reads via a SKILL.md entry point to produce consistently high-quality
JS code. This is modeled on our `ai-rust` repo.

Guides 01–11 are complete, and we're finishing the Deno sub-guide
series (Guide 12):

| Chapter | Slug | Status |
|---------|------|--------|
| 12-01 | `12-deno/01-runtime-basics.md` | Complete |
| 12-02 | `12-deno/02-testing.md` | In progress |
| 12-03 | `12-deno/03-task-runner.md` | In progress |
| 12-04 | `12-deno/04-publishing.md` | **This prompt** |

This prompt is for **12-04: Publishing** — everything a developer
needs to publish a Deno package to JSR (and optionally npm). Covers
`deno.json` package metadata (`name`, `version`, `exports`), the
`deno publish` command, JSR requirements and conventions, version
management, documentation requirements for JSR, cross-publishing to
npm, and the pre-publish checklist.

This is the final chapter of the Deno series. It brings together
concepts from all three prior chapters: runtime basics (12-01) for
the module system and configuration, testing (12-02) for pre-publish
quality gates, and task runner (12-03) for the publish workflow.

The target environment is:
- **Deno** (not Node.js — no `npm publish`, no `package.json`)
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

For this guide, **Deno concept cards are the primary authority**.

1. `concept-cards/deno/` — **PRIMARY**. JSR registry, publishing,
   package metadata, workspaces.
2. `concept-cards/exploring-js/` — Secondary. Module specifiers,
   package concepts.
3. Other sources as needed.

### Concept cards to read for this guide

Read these cards before writing. This is not exhaustive — if you find
related cards while reading, use them too.

**JSR registry**:
- `deno/jsr-registry.md`

**Package configuration**:
- `deno/deno-configuration.md`
- `deno/deno-workspaces.md`

**Module system (publishing implications)**:
- `deno/ecmascript-modules.md`
- `deno/deno-npm-specifiers.md`
- `deno/deno-package-json-support.md`

**Stability and versioning**:
- `deno/deno-stability-and-releases.md`

**Standard library (as a publishing model)**:
- `deno/deno-standard-library.md`

**JS module concepts**:
- `exploring-js/ecmascript-module.md`
- `exploring-js/module-characteristics.md`
- `exploring-js/module-specifier.md`
- `exploring-js/named-export.md`
- `exploring-js/default-export.md`
- `exploring-js/re-exporting.md`
- `exploring-js/tree-shaking.md`
- `exploring-js/javascript-package.md`
- `exploring-js/npm-registry.md`
- `exploring-js/package-managers.md`
- `js-definitive-guide/es6-module-system.md`
- `js-definitive-guide/re-exports.md`
- `js-definitive-guide/tree-shaking.md`
- `eloquent-js/package.md`

## Structural template

Follow the same format as the existing guides (01–11):

Each idiom entry has:
```
## ID-XX: [Title]

**Strength**: MUST | SHOULD | CONSIDER

**Summary**: One sentence.

[Code examples — deno.json config, shell commands, module structures]

**Rationale**: Why this matters. Cite concept card sources.

**See also**: Cross-references to other IDs or guides
```

End with:
- Quick Reference Table
- Related Guidelines — use the format from Guide 09: list specific
  ID numbers per guide for direct navigation.
- External References

## Proposed idiom list

This is a starting outline — adjust based on what the concept cards
emphasize. Add idioms if the cards reveal important patterns. Remove
or merge if redundant. Aim for 18-25 idioms.

### Package metadata in `deno.json`

1. `name` field — scoped format `@scope/package` (MUST)
2. `version` field — semver (MUST)
3. `exports` field — map of entry points for the public API (MUST)
4. Single vs multiple exports — `"exports": "./mod.js"` vs
   `"exports": { ".": "./mod.js", "./utils": "./utils/mod.js" }`
   (SHOULD)
5. `exclude` field — keep tests, benchmarks, and dev files out of
   the published package (SHOULD)
6. `license` field (SHOULD)

### The `exports` map

7. Every published path must be in `exports` — consumers can only
   import what `exports` exposes (MUST)
8. Use `exports` to enforce the public API boundary — internal
   modules not in `exports` are not importable by consumers (SHOULD)
9. Subpath exports for multi-entrypoint packages — e.g.,
   `@scope/pkg/utils` (SHOULD)

### `deno publish` command

10. `deno publish` — authenticate, validate, upload to JSR (MUST)
11. `deno publish --dry-run` — validate without publishing (SHOULD)
12. `--allow-dirty` for publishing with uncommitted changes
    (CONSIDER)
13. What `deno publish` validates: type-checking, `exports`
    resolution, package completeness (SHOULD)

### JSR requirements and conventions

14. JSR requires JSDoc on all exported symbols — the "slow types"
    rule for plain JS (MUST)
15. JSR auto-generates documentation from JSDoc — write for the
    registry page (SHOULD — references 11 ID-12)
16. Scoped packages — create a scope on jsr.io, then publish into
    it (MUST)
17. Immutable versions — once published, a version cannot be
    changed or deleted (SHOULD)

### Version management

18. Semantic versioning — major.minor.patch with the standard
    contract (MUST)
19. Pre-release versions — `1.0.0-alpha.1`, `1.0.0-rc.1` (CONSIDER)
20. `0.x.y` versions — breaking changes allowed at minor bumps
    per semver (SHOULD)

### Documentation for publishing

21. Module-level JSDoc is required for good JSR pages
    (SHOULD — references 11 ID-11)
22. `@example` blocks in JSDoc render on JSR and are testable
    with `deno test --doc` (SHOULD — references 11 ID-10)

### Pre-publish checklist

23. The pre-publish pipeline: fmt check → lint → type-check →
    test → dry-run → publish (SHOULD)
24. A `publish` task in `deno.json` that runs the full pipeline
    (SHOULD — references 12-03)

### Workspace publishing

25. Publishing workspace members — each member publishes
    independently with its own `name` and `version` (CONSIDER)

## Boundaries with other chapters and guides

**12-01 (Runtime Basics)** already covers:
- `deno.json` structure and fields overview (12-01 ID-13)
- `jsr:` and `npm:` specifiers (12-01 ID-17)
- `@std/` standard library (12-01 ID-25)

**12-02 (Testing)** covers:
- `Deno.test()` and assertion library
- `deno test --doc` for documentation tests

**12-03 (Task Runner)** covers:
- `deno task` definitions and recipes
- CI pipelines

**Guide 02 (API Design)** already covers:
- Named exports over default (02 ID-07)
- Re-exports / barrel files (02 ID-08)
- Module interface design (02 ID-06, 09)

**Guide 10 (Project Structure)** already covers:
- `mod.js` entry point convention (10 ID-08)
- Barrel file patterns (10 ID-09)
- Workspaces (10 ID-25)
- `deno.lock` (10 ID-22)

**Guide 11 (Documentation)** already covers:
- JSDoc prose for exported functions (11 ID-05–09)
- Module-level JSDoc (11 ID-11)
- `@example` blocks (11 ID-10)
- Writing for tooling / JSR (11 ID-12)

**Do NOT re-teach** module design (Guide 02), project layout
(Guide 10), JSDoc writing (Guide 11), test mechanics (12-02), or
task definitions (12-03). Cross-reference them. This chapter covers
the **publishing-specific concerns**: package metadata, the `exports`
map, `deno publish` mechanics, JSR requirements, versioning, and the
pre-publish checklist.

## Output

Save as: `guides/12-deno/04-publishing.md` in the `ai-js` repo.

## Quality bar

- The Deno and JSR concept cards are the primary sources. Cite them.
- `deno.json` examples must show realistic package metadata — not
  toy packages.
- The `exports` map section is the most important part of this
  chapter. It's the mechanism that enforces the public API boundary
  — consumers can only import paths listed in `exports`. Show
  single-export and multi-export patterns with clear examples.
- The JSR "slow types" requirement for plain JS is critical.
  Since this project uses plain JS (no TypeScript), the guide must
  explain what JSR requires for type information on exports —
  comprehensive JSDoc with `@param` and `@returns` on all exported
  symbols. Link to Guide 05 and Guide 11 for the details.
- The pre-publish checklist should be a concrete, copy-pasteable
  pipeline — not abstract advice.
- `deno publish --dry-run` is the most useful command for iterating
  on publishing issues. Emphasize it.
- Workspace publishing (members publishing independently) is a
  CONSIDER-level feature but important for the lykn project
  structure.
- Match the existing guides' terse, direct style.
- This is the capstone of the Deno series — it should tie together
  threads from all three prior chapters and from Guides 02, 10,
  and 11 via cross-references.

## What NOT to do

- Don't include `npm publish` or `package.json` publishing workflows
- Don't include GitHub Packages, GitLab registry, or other non-JSR
  registries
- Don't include CI/CD pipeline YAML for automated publishing —
  mention the `publish` task but not platform-specific CI config
- Don't include Deno Deploy — that's hosting, not package publishing
- Don't include changelog generation tools or release automation
  — just the publishing mechanics
- Don't re-teach JSDoc syntax (Guide 05), documentation writing
  (Guide 11), module design (Guide 02), or project layout (Guide 10)
- Don't include npm-specific publishing concerns (`npmignore`,
  `prepublishOnly`, `files` field) — those are Node.js patterns
- Don't include React/Vue component publishing patterns
- Don't over-explain semver — one entry with the standard contract
  is sufficient; link to semver.org for details
- Don't include cross-publishing to npm unless the concept cards
  explicitly cover it — the primary target is JSR
