# Code Audit

Prepare a full code-quality audit of this project. Audit every language
used in the project for which a skill exists under `knowledge/<slug>/`
in the ai-engineering repo. Produce one report per language plus a
top-level index.

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

## Scope

Per language: all source files in the idiomatic locations for that
language — source tree, test modules, and integration tests. No
files excluded from review. Skip only the generated, vendored, and
build-output trees named in Preparation step 3.

Treat the codebase as if you are handing it to a senior reviewer in
that language who will ship it to users next week.

## Output

Write one Markdown report per audited language to:

    workbench/<DATE>-audit-results-<slug>.md

Write a top-level index to:

    workbench/<DATE>-audit-index.md

`<DATE>` is the `YYYY.MM.DD` value captured in preparation. `<slug>`
is the `knowledge/` directory name (e.g. `rust`, `go`, `js`, `deno`,
`biome`, `tailwindcss`).

### Per-language report structure

1. **Executive summary** — 3 to 5 sentences. What is solid? What is
   the dominant cluster of issues? If the architecture doc was missing
   or undiscoverable, note that here.

2. **Findings**, grouped in this order. Categories that do not apply
   to the language may be omitted, but do not invent categories:
   correctness / soundness; API design and invariants; error handling;
   concurrency and runtime safety; testing; performance; idioms and
   style. Within each category, highest severity first.

3. **Per finding**, in this shape:
   - **Severity** — one of Blocker, High, Medium, Low.
     - *Blocker:* ships a bug or unsoundness to users.
     - *High:* correctness risk under realistic conditions.
     - *Medium:* will bite future maintainers or meaningfully degrade
       quality.
     - *Low:* style or minor idiom drift.
   - **Location** — `path/to/file.ext:LINE` (or `:LINE-LINE` for a
     range). Every finding cites at least one specific file:line.
   - **What's wrong** — one or two sentences.
   - **Why it's wrong** — the actual failure mode, not a restatement.
   - **Fix** — concrete, applied at the cited location. Include a
     code snippet if the fix is non-obvious.

4. **Cross-cutting findings**, if any — bugs whose root cause is in
   this language but whose effects also land in another audited
   language (FFI boundaries, IPC protocols, shared schemas). File
   the finding in the report for the language where the root cause
   lives; leave a one-line cross-reference in the other report(s)
   pointing at this finding.

5. **Things I looked for and did not find** — at least five checks
   you ran that came back clean. This disciplines against padding
   the report with filler and makes negative results visible.

### Index file structure

The index at `workbench/<DATE>-audit-index.md` contains:

1. Date and project root.
2. Languages detected, each marked as *audited* (skill found),
   *skipped* (non-language slug), or *no skill available* (detected
   but no matching `knowledge/<slug>/`).
3. For each audited language: finding counts by severity and a
   relative link to the per-language report.
4. Notes on architecture-doc discovery: which doc was used, or a
   statement that none was found and where the reviewer looked.
5. Any cross-cutting findings, with links back to the root-cause
   report.

## Stance

- **Do not soft-pedal.** A real bug reads as "fix this," not
  "consider this" or "nice-to-have." The only exception is genuine
  open design questions where there is a real tradeoff — label those
  explicitly as "open question" and put them at the end of the
  relevant category.

- **The current state of the code is not evidence it is correct.**
  Compilation and passing tests mean only that the compiler and the
  existing tests are satisfied. Look for what the tests do not cover.

- **Do not produce generic advice.** "Prefer early returns over
  nested conditionals" is worthless; "`handler.rs:127` nests three
  conditions where early returns would flatten the function" is
  actionable. Every recommendation must land on a specific line.

- **Severity is a commitment.** Do not use Medium as a hedge. If you
  cannot decide between two levels, write the reasoning in one line
  and pick.

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
