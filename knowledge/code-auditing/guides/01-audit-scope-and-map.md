# Audit Scope And Map

Use this guide to commission and start a diagnosis-only code audit. It defines
the audit stance, source-discovery pass, language/tool detection, and audit map
that make the rest of the audit evidence-based instead of context-window
sampling.

This guide is independently loadable. For findings and report format, load
[`02-findings-and-severity.md`](./02-findings-and-severity.md). For scale
coverage, load [`03-scale-aware-auditing.md`](./03-scale-aware-auditing.md).
For modernization synthesis, load
[`04-modernization-synthesis.md`](./04-modernization-synthesis.md). For the
handoff from audit to testing or hardening work, load
[`05-audit-to-hardening-handoff.md`](./05-audit-to-hardening-handoff.md).

## Audit Contract

Prepare a full code-quality audit of the project. Audit every language used in
the project for which a skill exists under `knowledge/<slug>/` in the
ai-engineering repo. Produce one report per audited language, a top-level
index, and a modernization synthesis.

The audit is diagnosis-only. Do not stage, commit, or edit source files as part
of the audit. A follow-up hardening round applies fixes.

This is a multi-scale audit, not a context-window sampling pass. Sampling may
help form a hypothesis, but the audit map is the scope. If a package, crate,
target, app, or subsystem is too large for one pass, split the audit into named
passes and make remaining scope explicit.

## Preparation

1. Run `date +%Y.%m.%d` and capture the result. Use this as the `<DATE>` prefix
   for every output file. Do not invent the date.
2. Read project context in this order:
   - `README.md` at the project root.
   - `CLAUDE.md` or `AGENTS.md` at the project root, if present.
   - Any architecture or design document either file references as current.
     Prefer the most recent current draft.
3. If no current architecture document is discoverable, or the pointer is
   stale, note the gap in the executive summary of every report. Missing or
   undiscoverable architecture context is itself a finding.

## Language And Tool Detection

Detect languages and tools in use with both manifest/config checks and
extension/content checks. A match in either is enough to count the language or
tool as present. Ignore generated, vendored, and dependency trees such as
`target/`, `node_modules/`, `vendor/`, `.venv/`, `dist/`, and `build/`.

Manifest and config signals:

- `Cargo.toml` -> `rust`
- `go.mod` -> `go`
- `package.json` -> `js`
- `deno.json` or `deno.jsonc` -> `deno`
- `biome.json` or `biome.jsonc` -> `biome`
- `tailwind.config.{js,ts,mjs,cjs}` -> `tailwindcss`

File and content signals:

- `.rs` -> `rust`
- `.go` -> `go`
- `.js`, `.mjs`, `.cjs`, `.jsx`, `.ts`, `.tsx` -> `js`
- JavaScript/TypeScript plus a Deno manifest -> `deno`
- `.css` containing Tailwind directives -> `tailwindcss`

For each detected language or tool, check whether `knowledge/<slug>/` exists in
the ai-engineering repo. Languages and tools without a matching skill directory
are not audited; list them in the index as "detected but no skill available" so
the gap remains visible.

Skip non-language slugs in automatic audits unless the user explicitly asks for
them. Design, Cobalt, and similar qualitative-review components are invoked by
their own task scope rather than by the code-audit detector.

## Required Skill Loading

For each language or tool that has a matching skill directory, load the full
knowledge set before auditing:

- Every `knowledge/<slug>/SKILL*.md` file.
- Every file under `knowledge/<slug>/guides/`.

Some slugs have more than one skill entrypoint. Read all of them. The
anti-patterns guide, where one exists, is the canonical starting point for the
per-language hunt list.

## Build The Audit Map

Build the audit map before writing findings. Use manifests, build files, module
declarations, package indexes, target lists, public entrypoints, and test
layouts to identify:

- Language and tool boundaries.
- First-party source, generated source, vendored source, examples, tests,
  fixtures, and build outputs.
- Packages, crates, libraries, binaries, apps, services, plugins, FFI layers,
  IPC boundaries, schemas, and command-line entrypoints.
- Ownership boundaries implied by directory layout, manifests, namespaces,
  module trees, build targets, or documentation.
- Cross-cutting contracts: error types, logging, configuration, persistence,
  serialization, concurrency model, resource ownership, async/runtime
  boundaries, public API shape, and test harnesses.

Record this map in the top-level index. If the map cannot be reconstructed from
the repository, that is itself an architecture/coherence finding.

## Output Files

Write one Markdown report per audited language to:

```text
workbench/<DATE>-audit-results-<slug>.md
```

Write the top-level index to:

```text
workbench/<DATE>-audit-index.md
```

Write the modernization synthesis to:

```text
workbench/<DATE>-audit-modernization-synthesis.md
```

`<DATE>` is the `YYYY.MM.DD` value captured during preparation. `<slug>` is the
`knowledge/` directory name, such as `rust`, `go`, `js`, `deno`, `biome`, or
`tailwindcss`.

## Index Contract

The top-level index records:

1. Date and project root.
2. Languages detected, each marked as audited, skipped, or detected but no
   skill available.
3. Audit map: top-level repository shape, workspace/package members,
   first-party versus vendored/generated boundaries, binaries/apps, libraries,
   tests, fixtures, public entrypoints, and cross-language contracts.
4. For each audited language: finding counts by severity and a relative link to
   the per-language report.
5. Scale coverage summary for each language, including any scale that could not
   be assessed because repository structure or documentation was missing.
6. Notes on architecture-doc discovery: which doc was used, or a statement that
   none was found and where the reviewer looked.
7. Cross-cutting findings, with links back to the root-cause report.

## Stance

- Do not soft-pedal. A real bug reads as "fix this," not "consider this" or
  "nice-to-have." Genuine open design questions belong at the end of the
  relevant category and are labelled as open questions.
- The current state of the code is not evidence it is correct. Compilation and
  passing tests mean only that the compiler and existing tests are satisfied.
- Do not produce generic advice. Every recommendation must land on a specific
  file and line.
- The audit map is the scope. The context window is not the scope.

## Component History

The code-auditing component history lives at
[`../version-history.md`](../version-history.md).
