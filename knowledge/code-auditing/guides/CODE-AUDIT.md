# Code Audit

Prepare a full code-quality audit of this project. Audit every language
used in the project for which a skill exists under `knowledge/<slug>/`
in the ai-engineering repo. Produce one report per language plus a
top-level index.

This is a multi-scale audit, not a context-window sampling pass. The
review must move deliberately from local code details to coherent
project structure: line/function, file/module, logical unit, package or
crate, application or service, full codebase, and workspace/monorepo
where present. Low-level findings matter, but the audit is incomplete
unless it also asks whether neighboring files, packages, crates,
targets, and apps read as parts of the same system with the same
invariants, idioms, error model, naming, test strategy, and operational
goals.

## Preparation

1. Run `date +%Y.%m.%d` and capture the result — use this as the
   `<DATE>` prefix for every output file. Do not hallucinate the date.

2. Read project context, in this order:
   - `README.md` at the project root.
   - `CLAUDE.md` at the project root, if it exists.
   - Any architecture or design document either of the above references
     as current. Prefer the most recent draft.

   If neither file points at an architecture document — or the pointer
   is stale — note this gap in the executive summary of every report
   you produce. Missing or undiscoverable architectural context is
   itself a finding.

3. Detect languages and tools in use. Do both checks; a match in either
   is enough to count the language as present. Ignore `target/`,
   `node_modules/`, `vendor/`, `.venv/`, `dist/`, `build/`, and any
   other generated or vendored trees.
   - **Manifests and config files** at any depth:
     - `Cargo.toml` → `rust`
     - `go.mod` → `go`
     - `package.json` → `js`
     - `deno.json` / `deno.jsonc` → `deno`
     - `biome.json` / `biome.jsonc` → `biome`
     - `tailwind.config.{js,ts,mjs,cjs}` → `tailwindcss`
   - **File extensions**:
     - `.rs` → `rust`
     - `.go` → `go`
     - `.js`, `.mjs`, `.cjs`, `.jsx`, `.ts`, `.tsx` → `js`, plus
       `deno` if a Deno manifest is present
     - `.css` containing Tailwind directives → `tailwindcss`

4. For each detected language, check whether `knowledge/<slug>/` exists
   in the ai-engineering repo. Languages and tools without a matching
   skill directory are **not** audited; list them in the index as
   "detected but no skill available" so the gap is visible.

5. Skip non-language slugs (currently `design/`, `cobalt/`) in the
   auto-audit. They cover qualitatively different reviews and should
   be invoked explicitly by the user.

6. For each language that has a matching skill directory, load the
   full knowledge set before auditing:
   - Every `knowledge/<slug>/SKILL*.md` file. Some slugs have more
     than one (e.g. `biome/SKILL-js-linter.md` and
     `biome/SKILL-web-linter.md`) — read all of them.
   - Every file under `knowledge/<slug>/guides/`.

   The anti-patterns guide, where one exists, is the canonical
   starting point for the per-language hunt list.

7. Build an audit map before writing findings. Use manifests,
   build files, module declarations, package indexes, target lists,
   public entrypoints, and test layouts to identify:
   - Language boundaries and tool boundaries.
   - First-party source, generated source, vendored source, examples,
     tests, fixtures, and build outputs.
   - Packages, crates, libraries, binaries, apps, services, plugins,
     FFI layers, IPC boundaries, schemas, and command-line entrypoints.
   - Ownership boundaries implied by directory layout, manifests,
     namespaces, module trees, build targets, or documentation.
   - Cross-cutting contracts: error types, logging, configuration,
     persistence, serialization, concurrency model, resource ownership,
     async/runtime boundaries, public API shape, and test harnesses.

   Record this map in the index. If the map cannot be reconstructed
   from the repository, that is itself an architecture/coherence
   finding.

## Scope

Per language: all source files in the idiomatic locations for that
language — source tree, test modules, and integration tests. No
files excluded from review. Skip only the generated, vendored, and
build-output trees named in Preparation step 3.

For each audited language, review at these scales:

1. **Line / expression / function** — correctness, soundness,
   lifetimes, ownership, nullability, error propagation, panic/throw
   behavior, input validation, resource management, and local idiom.
2. **File / module** — whether responsibilities are cohesive,
   invariants are explicit, names are consistent, tests exercise the
   right behavior, and private helpers do not leak architectural
   decisions.
3. **Logical unit** — the neighboring files that implement one concept:
   submodule, feature folder, parser phase, CLI surface, protocol
   handler, persistence layer, renderer, or equivalent. Check whether
   they share one vocabulary, one error model, one dependency posture,
   and one level of abstraction.
4. **Package / crate / library / target** — public API design,
   dependency direction, feature flags, build targets, binary/library
   split, test boundaries, integration points, and whether the unit has
   a coherent reason to exist.
5. **Application / service / executable** — startup/shutdown behavior,
   configuration, observability, process contracts, exit/status
   behavior, stdin/stdout/stderr semantics, persistence, upgrades, and
   user-facing failure modes.
6. **Whole codebase** — architectural through-line, naming and layout
   coherence, duplicate concepts, scattered policy, inconsistent
   abstractions, test pyramid shape, CI coverage, release posture, and
   modernization pressure.
7. **Workspace / monorepo / system-of-systems**, when present — shared
   crates/packages, internal dependency graph, versioning and feature
   compatibility, shared schemas, repo-wide tooling, ownership
   boundaries, and whether local conventions scale across members.

Every scale does not need the same number of findings, but every scale
must be examined. Do not let whichever files fit in context become the
implicit scope of the audit.

Treat the codebase as if you are handing it to a senior reviewer in
that language who will ship it to users next week.

## Output

Write one Markdown report per audited language to:

    workbench/<DATE>-audit-results-<slug>.md

Write a top-level index to:

    workbench/<DATE>-audit-index.md

Write a modernization synthesis to:

    workbench/<DATE>-audit-modernization-synthesis.md

`<DATE>` is the `YYYY.MM.DD` value captured in preparation. `<slug>`
is the `knowledge/` directory name (e.g. `rust`, `go`, `js`, `deno`,
`biome`, `tailwindcss`).

### Per-language report structure

1. **Executive summary** — 3 to 5 sentences. What is solid? What is
   the dominant cluster of issues? If the architecture doc was missing
   or undiscoverable, note that here.

2. **Audit map for this language** — the packages, crates, modules,
   targets, binaries, entrypoints, test trees, generated/vendored
   exclusions, and cross-language boundaries reviewed. Name any
   boundary that was inferred rather than documented.

3. **Scale coverage** — one short paragraph or checklist covering
   line/function, file/module, logical unit, package/crate/target,
   app/service/executable, whole codebase, and workspace/monorepo
   where present. This is not filler; it is the reviewer showing that
   the audit climbed the ladder.

4. **Findings**, grouped in this order. Categories that do not apply
   to the language may be omitted, but do not invent categories:
   correctness / soundness; architecture and coherence; API design
   and invariants; error handling; concurrency and runtime safety;
   testing; performance; idioms and style; modernization. Within each
   category, highest severity first.

5. **Per finding**, in this shape:
   - **ID** — stable within this report, e.g. `RUST-001`,
     `CPP-004`, or `JS-002`. Use the same ID in cross-references,
     the index, and the modernization synthesis.
   - **Severity** — one of Blocker, High, Medium, Low.
     - *Blocker:* ships a bug or unsoundness to users.
     - *High:* correctness risk under realistic conditions.
     - *Medium:* will bite future maintainers or meaningfully degrade
       quality.
     - *Low:* style or minor idiom drift.
   - **Location** — `path/to/file.ext:LINE` (or `:LINE-LINE` for a
     range). Every finding cites at least one specific file:line.
     For scale findings, cite the boundary-defining file:line
     (manifest, build file, module declaration, public entrypoint,
     schema, or documented contract) plus representative file:line
     evidence.
   - **Scale** — line/function, file/module, logical unit,
     package/crate/target, app/service/executable, whole codebase, or
     workspace/monorepo.
   - **What's wrong** — one or two sentences.
   - **Why it's wrong** — the actual failure mode, not a restatement.
   - **Fix** — concrete, applied at the cited location. Include a
     code snippet if the fix is non-obvious.

6. **Coherence observations** — patterns that are not single defects
   but affect maintainability at scale: mismatched naming systems,
   duplicated concepts, inconsistent layering, multiple competing
   abstractions, divergent testing styles, or different error/logging
   models in neighboring code. Promote any observation with a concrete
   failure mode to a severity-graded finding.

7. **Cross-cutting findings**, if any — bugs whose root cause is in
   this language but whose effects also land in another audited
   language (FFI boundaries, IPC protocols, shared schemas). File
   the finding in the report for the language where the root cause
   lives; leave a one-line cross-reference in the other report(s)
   pointing at this finding.

8. **Things I looked for and did not find** — at least five checks
   you ran that came back clean. This disciplines against padding
   the report with filler and makes negative results visible.

### Index file structure

The index at `workbench/<DATE>-audit-index.md` contains:

1. Date and project root.
2. Languages detected, each marked as *audited* (skill found),
   *skipped* (non-language slug), or *no skill available* (detected
   but no matching `knowledge/<slug>/`).
3. Audit map: top-level repository shape, workspace/package members,
   first-party versus vendored/generated boundaries, binaries/apps,
   libraries, tests, fixtures, public entrypoints, and cross-language
   contracts.
4. For each audited language: finding counts by severity and a
   relative link to the per-language report.
5. Scale coverage summary: which scales were present and audited for
   each language, including any scale that could not be assessed
   because repository structure or documentation was missing.
6. Notes on architecture-doc discovery: which doc was used, or a
   statement that none was found and where the reviewer looked.
7. Any cross-cutting findings, with links back to the root-cause
   report.

### Modernization synthesis structure

The synthesis at `workbench/<DATE>-audit-modernization-synthesis.md`
comes after the per-language reports. It is not a substitute for
evidence and must cite the report finding IDs it relies on.

1. **Executive summary** — what modernization pressure is real, what
   can wait, and what should not be changed until evidence improves.
2. **System themes** — recurring findings across files, packages,
   crates, apps, or languages. Distinguish isolated defects from
   architectural drift.
3. **Consolidation opportunities** — duplicated concepts, overlapping
   utilities, competing abstractions, shared schemas, repeated parser
   or protocol logic, copy-pasted tests, and places where one supported
   implementation should replace several local variants.
4. **Modernization moves** — ordered recommendations such as dependency
   replacement, API redesign, language-edition migration, build-system
   cleanup, test harness changes, error-model unification, or
   workspace restructuring. Each move must cite audit findings and say
   whether it is safe as a local refactor, requires a compatibility
   layer, or needs an explicit behavior change.
5. **Defer / do not touch yet** — areas where modernization would be
   speculative, where public contracts are unclear, or where tests are
   too weak to support safe change.

## Stance

- **Do not soft-pedal.** A real bug reads as "fix this," not
  "consider this" or "nice-to-have." The only exception is genuine
  open design questions where there is a real tradeoff — label those
  explicitly as "open question" and put them at the end of the
  relevant category.

- **The current state of the code is not evidence it is correct.**
  Compilation and passing tests mean only that the compiler and the
  existing tests are satisfied. Look for what the tests do not cover.

- **The context window is not the scope.** Sample only to form a
  hypothesis, then verify it against the audit map. If a package,
  crate, target, or subsystem is too large for one pass, split the
  audit into named passes and make the remaining scope explicit.

- **Do not produce generic advice.** "Prefer early returns over
  nested conditionals" is worthless; "`handler.rs:127` nests three
  conditions where early returns would flatten the function" is
  actionable. Every recommendation must land on a specific line.

- **Severity is a commitment.** Do not use Medium as a hedge. If you
  cannot decide between two levels, write the reasoning in one line
  and pick.

- **Coherence is auditable.** "These files feel inconsistent" is not
  enough. Name the inconsistent idiom, cite representative lines from
  each side, explain the operational or maintenance failure mode, and
  assign severity if it matters.

- **Modernization follows evidence.** Do not start with the newest
  library, edition, framework, or rewrite shape. Start with observed
  defects and structural pressure; then recommend the smallest
  modernization move that resolves the real problem while preserving
  supported behavior.

## What to hunt for

### Cross-language patterns (apply to every language)

- Silently dropped errors — results/exceptions swallowed, `catch`
  blocks that log and continue, missing `?` propagation,
  `.unwrap()` / `.expect()` / non-null assertions on library paths
  a user can reach.
- Panics or exceptions on code paths a library caller can hit that
  should be returned as recoverable errors instead.
- Test doubles (mocks, fakes, stubs) that diverge from production
  code paths and hide integration-level bugs.
- Wildcard or catch-all patterns (`_ =>`, `default:`, broad
  `except:`) that suppress compile-time or lint-time exhaustiveness
  checks.
- Assertions that accept ranges where exact values are computable.
- Shared mutable state accessed without the synchronization the
  language's concurrency model requires (`Send`/`Sync` in Rust,
  goroutine / channel misuse in Go, closures capturing mutable
  bindings in JS, etc.).
- Resource leaks — unclosed handles, listeners not removed, timers
  not cleared, connections not released on error paths.
- Untrusted input reaching trusted code without validation,
  canonicalization, or escaping.
- Implicit assumptions about time, locale, encoding, file-system
  case sensitivity, or line endings.
- Missing or misconfigured CI gates (lint, format, type check,
  test) that would have caught any of the above.
- Inconsistent naming, layering, logging, error handling, configuration,
  serialization, or dependency direction across files that implement
  the same concept.
- Two or more local abstractions solving the same problem without a
  documented reason for coexistence.
- Policy scattered through call sites instead of held in one boundary
  where it can be tested and changed safely.
- Public entrypoints whose behavior is not exercised through the same
  boundary real users or supervised processes use.
- Workspace or monorepo members that silently diverge in toolchain,
  edition, dependency policy, CI gates, release assumptions, or shared
  schema versions.

### Per-language patterns

For each language, derive the hunt list from the skill and guides
loaded in Preparation. The anti-patterns guide, where one exists
(e.g. `knowledge/rust/guides/11-anti-patterns.md`), is the canonical
starting point — work through its items and grep the codebase for
each. Do not fall back to generic knowledge when a guide exists;
the guide is the contract.

## Do not modify code

The audit is diagnosis only. A follow-up round will apply the fixes.
Do not stage, commit, or edit source files as part of this work.

## Component History

The code-auditing component history lives at
[`../version-history.md`](../version-history.md). Current audit guide lineage:
1.1, 2026-08-27.
