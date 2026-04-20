# ai-js Guide 12-03: Deno Task Runner — Claude Code Instructions

## Context

We're building `ai-js`, a repo of curated JavaScript guides that Claude
Code reads via a SKILL.md entry point to produce consistently high-quality
JS code. This is modeled on our `ai-rust` repo.

Guides 01–11 are complete, and we're working through the Deno sub-guide
series (Guide 12):

| Chapter | Slug | Status |
|---------|------|--------|
| 12-01 | `12-deno/01-runtime-basics.md` | Complete |
| 12-02 | `12-deno/02-testing.md` | In progress |
| 12-03 | `12-deno/03-task-runner.md` | **This prompt** |
| 12-04 | `12-deno/04-publishing.md` | Pending |

This prompt is for **12-03: Task Runner** — the `deno task` system and
the broader set of Deno CLI commands used in day-to-day development
workflows. Covers the `tasks` field in `deno.json`, `deno task` syntax
and shell features, `--watch` mode, common task recipes (dev, test,
lint, fmt, check, build), task composition and chaining, and the Deno
CLI commands that form the developer workflow (`deno fmt`, `deno lint`,
`deno run`, `deno check`, etc.).

This is a practical, recipe-oriented chapter. Where 12-01 covers
*what Deno can do*, this chapter covers *the commands you type every
day and how to wire them together*.

The target environment is:
- **Deno** (not Node.js — no `npm run`, no `npx`, no Makefile)
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

1. `concept-cards/deno/` — **PRIMARY**. `deno task`, CLI commands,
   configuration, workflows.
2. Other sources only as needed for specific interactions.

### Concept cards to read for this guide

Read these cards before writing. This is not exhaustive — if you find
related cards while reading, use them too.

**Task runner**:
- `deno/deno-task.md`
- `deno/deno-configuration.md`

**CLI commands (the workflow tools)**:
- `deno/deno-cli.md`
- `deno/deno-run.md`
- `deno/deno-linter.md`
- `deno/deno-formatter.md`
- `deno/deno-test-runner.md`
- `deno/deno-compile.md`
- `deno/deno-debugging.md`

**CI and Docker**:
- `deno/deno-in-ci.md`
- `deno/deno-in-docker.md`

**Permissions (relevant to task definitions)**:
- `deno/deno-permissions-system.md`
- `deno/deno-security-model.md`

**Workspaces (task inheritance)**:
- `deno/deno-workspaces.md`

## Structural template

Follow the same format as the existing guides (01–11):

Each idiom entry has:
```
## ID-XX: [Title]

**Strength**: MUST | SHOULD | CONSIDER

**Summary**: One sentence.

[Code examples — deno.json config, shell commands, task definitions]

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

This guide will be shorter than the language guides (01–09) because
it's a practical recipe chapter, not a language-semantics chapter.

### `deno task` fundamentals

1. Define tasks in `deno.json` — replaces `npm run` / `package.json`
   scripts (MUST)
2. `deno task` with no arguments lists available tasks (SHOULD)
3. Task shell syntax — pipes, redirects, env vars, `&&`, `||`,
   sequential with `;` (SHOULD)
4. Cross-platform shell — `deno task` uses a built-in cross-platform
   shell, not the system shell (SHOULD)
5. Passing arguments to tasks — `deno task dev -- --port 3000`
   (SHOULD)

### Common task recipes

6. `dev` task — `deno run --watch` for file-watching development
   (SHOULD)
7. `test` task — `deno test` with appropriate permissions (SHOULD)
8. `check` task — combined lint + fmt check + type check + test
   pipeline (SHOULD)
9. `lint` and `fmt` tasks — Biome integration via tasks (SHOULD)
10. `build` or `compile` task — `deno compile` for production
    binaries (CONSIDER)

### `--watch` mode

11. `--watch` for auto-restart on file changes — `deno run --watch`
    (SHOULD)
12. `--watch` with `--watch-exclude` for ignoring specific paths
    (CONSIDER)
13. `deno test --watch` for continuous testing (SHOULD)

### CLI command reference

14. `deno run` — execute a script with permissions (MUST)
15. `deno fmt` and `deno lint` — built-in formatting and linting
    (SHOULD — note Biome alternative)
16. `deno check` — type-check without executing
    (SHOULD — references 12-01 ID-20)
17. `deno info` — dependency tree inspection (CONSIDER)
18. `deno install` — install scripts as commands (CONSIDER)
19. `deno eval` — evaluate inline code (CONSIDER)

### Task composition

20. Chaining tasks — `&&` for sequential, `&` for parallel (SHOULD)
21. Composing tasks from other tasks — calling `deno task` inside
    a task (CONSIDER)
22. Environment variables in tasks — inline `VAR=value cmd` syntax
    (SHOULD)

### CI and production workflows

23. CI task recipe — fmt check + lint + type check + test in one
    pipeline (SHOULD)
24. `deno task` in CI — reproducible, no install step (SHOULD)

## Boundaries with other chapters and guides

**12-01 (Runtime Basics)** already covers:
- `deno.json` structure and fields (12-01 ID-13)
- Permission flags in detail (12-01 ID-01–04)
- `deno check` purpose and behavior (12-01 ID-20)
- `deno compile` output (12-01 ID-24)

This chapter covers the **practical usage** of these commands in
task definitions and dev workflows. 12-01 says "this is what
`deno check` does"; this chapter says "here's how to wire it into
your `check` task alongside lint and test."

**12-02 (Testing)** covers:
- `Deno.test()` API and assertion library
- Test organization, mocking, coverage

This chapter covers `deno test` as a *command* (flags, filtering,
watch mode) but not the test API itself.

**12-04 (Publishing)** covers:
- JSR publishing workflow

This chapter may include a `publish` task recipe but defers the
publishing details to 12-04.

**Guide 10 (Project Structure)** already covers:
- `deno.json` placement (10 ID-15)
- Task field overview (10 ID-15 shows example tasks)
- Test file naming conventions (10 ID-07)

**Guide 13 (Biome)** will cover:
- `biome.json` configuration
- Biome lint rules and formatting options

This chapter shows how to call Biome from `deno task` but does not
cover Biome configuration — that's Guide 13's job.

**Do NOT re-teach** permission flags (12-01), test API (12-02),
publishing (12-04), or Biome config (Guide 13). Cross-reference them.

## Output

Save as: `guides/12-deno/03-task-runner.md` in the `ai-js` repo.

## Quality bar

- The Deno concept cards are the primary source. Cite them.
- Task definitions must be realistic — show real `deno.json` `tasks`
  fields with practical commands, not toy examples.
- The cross-platform shell section is important — developers coming
  from Node.js expect system shell behavior. Explain what the built-in
  shell supports and what it doesn't.
- The `check` task recipe (combined lint + fmt + type-check + test)
  is the most valuable entry for day-to-day development. Make it
  comprehensive.
- Show Biome integration in task definitions — since the project uses
  Biome for lint/fmt, tasks should call `biome check` or `biome ci`
  rather than `deno fmt` / `deno lint` where appropriate. Show both
  options and note the project's preference.
- `--watch` mode is a critical DX feature. Cover it thoroughly
  including excluded paths and limitations.
- Match the existing guides' terse, direct style.
- This guide should be practical and recipe-oriented — less "why"
  and more "here's the command."

## What NOT to do

- Don't include `Deno.test()` API details — that's 12-02
- Don't include JSR publishing commands — that's 12-04
- Don't include Biome configuration details — that's Guide 13
- Don't include permission flag semantics — that's 12-01
- Don't include Makefile, `npm run`, or other non-Deno task runners
- Don't include Docker or CI pipeline YAML — mention CI-oriented
  tasks but don't include CI/CD platform configuration
- Don't include Deno Deploy commands — that's infrastructure
- Don't include `deno bench` details — benchmarking is covered
  in Guide 08 and 12-01
- Don't over-explain the shell syntax — a reference table of
  supported operators is more useful than a tutorial
- Don't include tasks that call Node.js tools (`npx`, `node`)
