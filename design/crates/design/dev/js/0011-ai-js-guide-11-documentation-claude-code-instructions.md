# ai-js Guide 11: Documentation — Claude Code Instructions

## Context

We're building `ai-js`, a repo of curated JavaScript guides that Claude
Code reads via a SKILL.md entry point to produce consistently high-quality
JS code. This is modeled on our `ai-rust` repo.

Guides 01–10 are complete. Now we're writing Guide 11: Documentation.

This guide covers the writing discipline of documentation: when and what
to comment, how to write effective JSDoc descriptions (not the type
annotation mechanics — Guide 05 covers that), module-level and
function-level documentation, README structure, inline comments vs
doc comments, code as documentation, naming as documentation, and
the anti-patterns of both over- and under-documenting.

**This is explicitly NOT about**:
- JSDoc type annotations (`@param`, `@type`, `@typedef`, `@template`)
  — those are in Guide 05 (Type Discipline)
- API naming conventions (`isX`, `toX`, `fromX`) — those are in
  Guide 02 (API Design)
- Project directory structure — that's in Guide 10
- Deno tooling details (`deno doc`, `deno test`) — those go in Guide 12

This guide is about **what to write in comments and documentation**,
**when to write it**, and **when NOT to write it**. The core tension:
comments should explain *why*, not *what*. Code should be clear enough
that *what* it does is self-evident.

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

Read these cards before writing. The concept card coverage for
documentation-as-writing is thinner than for language mechanics —
that's expected. Ground claims in what the cards say where possible,
and in Deno conventions and general professional practice where the
cards are silent.

**Comments**:
- `exploring-js/javascript-comments.md`
- `js-definitive-guide/comments.md`
- `eloquent-js/comment.md`

**Naming conventions and identifiers**:
- `exploring-js/naming-conventions.md`
- `exploring-js/identifiers.md`
- `js-definitive-guide/identifiers.md`
- `deep-js/function-naming-rules.md`
- `deep-js/default-export-naming.md`
- `deep-js/arrow-function-naming.md`
- `deep-js/bound-function-naming.md`
- `deep-js/creation-time-naming.md`
- `deep-js/method-naming.md`
- `deep-js/getter-setter-naming.md`
- `deep-js/naming-rules-for-introspection.md`

**Module system (documentation implications)**:
- `exploring-js/ecmascript-module.md`
- `exploring-js/module-characteristics.md`
- `exploring-js/named-export.md`
- `exploring-js/default-export.md`
- `exploring-js/re-exporting.md`
- `js-definitive-guide/es6-module-system.md`
- `eloquent-js/module-design.md`

**Testing (as documentation)**:
- `exploring-js/unit-testing.md`
- `exploring-js/assertions.md`
- `deno/deno-test-runner.md`
- `eloquent-js/testing.md`

**Error classes (documentation of error contracts)**:
- `exploring-js/error-class.md`
- `js-definitive-guide/error-classes.md`

**Deno documentation tooling**:
- `deno/deno-api-overview.md`
- `deno/jsr-registry.md`

## Structural template

Follow the same format as the existing guides (01–10):

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
- Related Guidelines — use the format introduced in Guide 09:
  list specific ID numbers per guide so readers can navigate directly
  (e.g., "See `05-type-discipline.md` for ID-16, 17, 18 (JSDoc type
  annotations)"). This is more useful than vague cross-references.
- External References

## Proposed idiom list

This is a starting outline — adjust based on what the concept cards
emphasize. Add idioms if the cards reveal important patterns. Remove
or merge if redundant. Aim for 18-25 idioms.

This guide will be shorter than guides 01–09 because documentation
practice has less language-spec depth. The concept cards say relatively
little about how to write comments — they say a lot about what the
language does, which is what guides 01–09 cover. Guide 11 is more
about writing discipline and less about language mechanics.

### When to comment and when not to

1. Comments explain *why*, not *what* — if the code needs a comment
   to explain what it does, refactor the code (MUST)
2. Don't comment obvious code — `i++ // increment i` is noise (MUST)
3. Comment non-obvious intent — workarounds, edge cases, business
   rules, "why not the obvious approach" (SHOULD)
4. TODO/FIXME/HACK comments — use them, but include context (who,
   when, why, ticket number) (SHOULD)

### JSDoc documentation (the writing, not the types)

5. Every exported function gets a JSDoc description (SHOULD)
6. First sentence is the summary — keep it under 15 words, it
   appears in hover/autocomplete (SHOULD)
7. Document parameters with prose, not just types — what are the
   valid values? what happens with edge cases? (SHOULD)
8. Document thrown errors — `@throws` with the condition (SHOULD)
9. Document return values — especially when `null`/`undefined` have
   meaning (SHOULD)
10. Include examples in JSDoc with `@example` for non-obvious APIs
    (CONSIDER)

### Module-level documentation

11. Every module gets a top-of-file JSDoc block — one sentence on
    what the module does and when you'd use it (SHOULD)
12. `deno doc` reads JSDoc — write for tooling, not just humans
    (SHOULD)
13. Re-export modules (barrels) get documentation of the public
    surface they expose (CONSIDER)

### Code as documentation

14. Self-documenting code — descriptive names eliminate most comment
    needs (MUST)
15. Named constants over magic values — `MAX_RETRIES` not `3` (SHOULD)
16. Extract complex conditions into named booleans or predicate
    functions (SHOULD)
17. Function names describe the transformation: `parseConfig`,
    `validateInput`, `formatDate` (SHOULD — references 02 ID-16)
18. Tests as documentation — well-named tests describe behavior
    (SHOULD)

### What NOT to document

19. Don't document internal implementation details in the public
    JSDoc — describe the contract, not the mechanism (SHOULD)
20. Don't write essay-length JSDoc — a sentence or two is usually
    sufficient (SHOULD)
21. Don't use JSDoc for private/internal functions unless the logic
    is non-obvious (CONSIDER)

### Documentation maintenance

22. Update comments when code changes — stale comments are worse
    than no comments (MUST)
23. Delete commented-out code — that's what version control is for
    (MUST)

## Boundaries with other guides

**Guide 02 (API Design)** already covers:
- Method naming conventions: verbs, `isX`, `hasX`, `toX`, `fromX`
  (02 ID-16, 17, 18)
- Module interface design (02 ID-06–10)

**Guide 05 (Type Discipline)** already covers:
- JSDoc type annotation syntax: `@param`, `@returns`, `@type`,
  `@typedef`, `@template` (05 ID-16–20)
- `// @ts-check` and `deno check` integration (05 ID-20)

**Guide 10 (Project Structure)** already covers:
- File naming conventions
- README placement and project skeleton

**Guide 12 (Deno)** will cover:
- `deno doc` command and output format
- JSR publishing requirements (which include documentation)

**Do NOT re-teach these.** Cross-reference them. This guide covers
the *writing craft* of documentation — what to say, how to say it,
and when to stay silent. Guide 05 covers the *type syntax* of JSDoc.
Guide 02 covers *naming conventions*. Guide 10 covers *file-level
organization*.

## Output

Save as: `guides/11-documentation.md` in the `ai-js` repo.

## Quality bar

- Ground claims in concept card content where possible. For
  documentation writing practice that the cards don't cover,
  ground recommendations in Deno ecosystem conventions and
  widely accepted professional practice.
- Code examples must show realistic JSDoc blocks on realistic
  functions — not toy `add(a, b)` examples.
- Good/bad comment examples should be drawn from plausible code
  that a developer would actually write.
- The tone should be terse and direct — this is a reference doc,
  not a style guide manifesto. Match the existing guides' density.
- No Node.js patterns in any examples.
- All cross-references must use the correct guide slugs.
- The "comments explain why, not what" principle is the foundation
  of the entire guide. Establish it in ID-01 and reinforce it
  throughout.
- The JSDoc description section (not types) is the core of this
  guide. Guide 05 covers `@param {string} name` syntax. This guide
  covers the prose: *"The user's display name. Falls back to email
  prefix if not set."*
- Show concrete before/after examples of bad documentation improved.
  Don't just say "write good comments" — show what good looks like.
- This guide should be shorter than guides 01–09. Aim for 18–23
  well-grounded idioms rather than padding to 30.
- AI-generated code has a specific documentation anti-pattern:
  verbose, obvious comments on every line that add no information
  (`// Create a new array` before `const arr = []`). This guide
  should explicitly address this — it is arguably the most
  important documentation anti-pattern for Claude Code to learn.

## What NOT to do

- Don't invent idioms not supported by the concept cards or
  professional practice
- Don't include JSDoc type annotation syntax — that's Guide 05
- Don't include API naming conventions — that's Guide 02
- Don't include project-level documentation structure (README
  templates, CHANGELOG format) — that's Guide 10
- Don't include `deno doc` command usage — that's Guide 12
- Don't include TypeScript-specific documentation patterns
- Don't include documentation generation tools (TypeDoc, JSDoc
  generators) — `deno doc` is the only tool in scope
- Don't include license header templates or legal boilerplate
- Don't philosophize about documentation theory — show concrete
  examples of good and bad documentation
- Don't recommend commenting every function — internal helper
  functions with descriptive names and clear types often need
  no documentation at all. The guide should teach judgment about
  *when* to document, not demand blanket coverage.
- Don't include HTML/Markdown formatting of JSDoc (rendering
  details) — focus on the content, not the markup
