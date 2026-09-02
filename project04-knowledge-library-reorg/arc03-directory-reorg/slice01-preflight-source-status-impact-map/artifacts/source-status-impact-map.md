# Source Status Impact Map

```yaml
project: project04-knowledge-library-reorg
arc: arc03-directory-reorg
slice: slice01-preflight-source-status-impact-map
artifact: source-status-impact-map
created-on: 2026-09-02
source_checkout: /Users/oubiwann/lab/billosys/ai-engineering
planning_checkout: /Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning
source-files-edited: false
boundary: preflight-only
```

## Checkout Identity

| Checkout | Path | Branch | HEAD | Worktree evidence |
|----------|------|--------|------|-------------------|
| main checkout | `/Users/oubiwann/lab/billosys/ai-engineering` | `main` | `5b796c3` | `git -C /Users/oubiwann/lab/billosys/ai-engineering worktree list` reports `/Users/oubiwann/lab/billosys/ai-engineering 5b796c3 [main]`. |
| planning checkout | `/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning` | `planning` | `492dfa8` | `git -C /Users/oubiwann/lab/billosys/ai-engineering worktree list` reports `/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning 492dfa8 [planning]`. |

## Status Baselines

Source status baseline:

- Command: `git -C /Users/oubiwann/lab/billosys/ai-engineering status --short`
- Result: returned no output.
- Interpretation: no existing source dirt was present at preflight capture time.
- Do-not-touch note: this slice does not edit the source checkout. If later
  unrelated source dirt appears, Arc03 source-edit slices must record it
  exactly and avoid modifying it unless explicitly authorized.

Planning status baseline:

- Command: `git -C /Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning status --short`
- Result: returned no output before this slice created its proposed-done
  planning artifacts.
- Interpretation: planning changes in this slice are limited to the Slice01
  artifact set, ledger, and closing report.

## Expected Arc03 Source Surfaces

The following source surfaces are present in the main checkout and are expected
to be reviewed or touched only by later Arc03 source-edit slices with explicit
source authorization:

| Surface | Current baseline | Expected later Arc03 relevance |
|---------|------------------|-------------------------------|
| `README.md` | present | Top-level route map and compatibility review surface; deep end-user docs prose remains Arc04. |
| `SKILL.md` | present | Top-level collaboration-framework compatibility surface; Arc03 must choose a validated shim, replacement route, or no-shim path before composer moves. |
| `docs/` | present | Current framework/project-management source and user-facing explanation surface; Arc04 owns broad docs prose. |
| `knowledge/` | present | Accepted default substrate root for domain/tooling, framework/operational, method, and source/provenance material. |
| `templates/` | present | Top-level cross-cutting support templates; owner-local templates may move later after explicit authorization. |
| `protocols/ccdp` | present | Separate CCDP protocol/package surface; CCDP remains separate from installable skill packages. |
| `Makefile` | present | Package, validation, generated zip, `CF_FILES`, `ALL_SKILL_FILES`, and `INSTALL_ZIPS` surface. |
| `package-path-exceptions.tsv` | present | Repair-before-exception policy surface; persistent package-path exception rows and accepted warnings require operator approval. |
| `generated zips` | present | Generated zips currently include `collaboration-framework.zip`, per-domain skill zips, Biome/Deno zips, and `ccdp.zip`. Later source-edit slices must inspect packages when package content changes. |
| `AGENTS.md` | present | Top-level compatibility route surface. |
| `CLAUDE.md` | present | Top-level compatibility route surface. |
| `package roots` | present | Package roots are Makefile-defined bundle outputs and staged archive roots, including `collaboration-framework`, per-domain skill names, Biome multi-entrypoint packages, and CCDP as a separate protocol package. |
| `source roots` | present | Current source roots include top-level `SKILL.md`/`docs/`/`templates/`, `knowledge/<component>/`, `knowledge/biome/`, and `protocols/ccdp/`; Arc02 accepts source roots and package roots as separate axes. |

## Observed Root Inventory

Top-level expected surfaces all returned `present` for:

- `README.md`
- `SKILL.md`
- `docs/`
- `knowledge/`
- `templates/`
- `protocols/ccdp`
- `Makefile`
- `package-path-exceptions.tsv`
- `AGENTS.md`
- `CLAUDE.md`

Generated zips observed at repository root:

- `biome-js-linter.zip`
- `biome-linter.zip`
- `ccdp.zip`
- `cobalt-guidelines.zip`
- `collaboration-framework.zip`
- `cpp-guidelines.zip`
- `deno-js-linter.zip`
- `erlang-guidelines.zip`
- `go-guidelines.zip`
- `javascript-deno-guidelines.zip`
- `rust-guidelines.zip`
- `tailwindcss.zip`
- `visual-design-system.zip`

Skill entrypoint roots observed under `knowledge/`:

- `knowledge/cobalt/SKILL.md`
- `knowledge/cpp/SKILL.md`
- `knowledge/design/SKILL.md`
- `knowledge/erlang/SKILL.md`
- `knowledge/go/SKILL.md`
- `knowledge/js/SKILL.md`
- `knowledge/rust/SKILL.md`
- `knowledge/tailwindcss/SKILL.md`

The Makefile also declares non-`SKILL.md` entrypoints for
`knowledge/deno/SKILL-js-linter.md`,
`knowledge/biome/SKILL-js-linter.md`, and
`knowledge/biome/SKILL-web-linter.md`; Biome multi-entrypoint behavior remains
explicit and must be preserved.

## Boundary

This artifact is a preflight-only planning artifact. It is not
source-edit authorization. The source checkout remains untouched by this slice,
and later Arc03 source-edit slices must declare their own source scope and
validation evidence before editing source files.
