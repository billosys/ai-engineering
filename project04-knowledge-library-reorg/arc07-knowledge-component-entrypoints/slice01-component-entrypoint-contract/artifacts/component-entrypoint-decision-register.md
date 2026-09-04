# Component Entrypoint Decision Register

```yaml
project: project04-knowledge-library-reorg
arc: arc07-knowledge-component-entrypoints
slice: slice01-component-entrypoint-contract
status: proposed-done
source_edits: none
```

## Decision Rule

This component entrypoint decision register tests the starting recommendation
instead of blindly repeating it:

- `SKILL.md` is for concise load contracts, trigger guidance, scope, routing,
  and package/loader entrypoints.
- `guides/` is for long-form explanatory, methodological, policy, or
  working-practice material.
- `templates/` is for reusable forms or skeletons that are copied/adapted by a
  user or another skill.
- A long current document should not be renamed to `SKILL.md` merely because
  it is important.
- A component can be independently loadable without being a separate
  installable zip.

## Decisions

| Component | Decision | Guide/template handling | Rationale |
| --- | --- | --- | --- |
| `knowledge/collaboration-framework/` | Make `knowledge/collaboration-framework/SKILL.md` the canonical collaboration-framework source entrypoint by moving root `SKILL.md`. | Move `docs/AI-CONSTITUTION-SUPPLEMENT.md` to `guides/AI-CONSTITUTION-SUPPLEMENT.md`. Remove emptied `docs/` with `rmdir`. | The collaboration framework remains the composite framework/operational package. The package must still expose `collaboration-framework/SKILL.md`, but the source entrypoint belongs with its component substrate. |
| `knowledge/agent-coordination/` | Add concise component-root `SKILL.md`. | Move `docs/SUBAGENT-DELEGATION-POLICY.md` to `guides/SUBAGENT-DELEGATION-POLICY.md`; remove emptied `docs/` with `rmdir`. | The policy is independently loadable as a component contract, but the existing file is long-form policy material, not an entrypoint. |
| `knowledge/code-auditing/` | Add concise component-root `SKILL.md`. | Move `docs/CODE-AUDIT.md` to `guides/CODE-AUDIT.md`; remove emptied `docs/` with `rmdir`. | The audit prompt is a working-practice guide. A root entrypoint should describe when to load it and route to the guide. |
| `knowledge/contribution-style/` | Add concise component-root `SKILL.md`. | Move `docs/CONTRIBUTION-STYLE.md` to `guides/CONTRIBUTION-STYLE.md`; keep `templates/CONTRIBUTION-TICKET.md`. Remove emptied `docs/` with `rmdir`. | Voice/style guidance is guide material; the ticket skeleton is a reusable template and should stay under `templates/`. |
| `knowledge/engineering-methods/` | Add concise component-root `SKILL.md`. | Move `docs/AI-ENGINEERING-METHODOLOGY.md` to `guides/AI-ENGINEERING-METHODOLOGY.md`; remove emptied `docs/` with `rmdir`. | The methodology is long-form guide material. A component entrypoint should state the load reason and route to it. |
| `knowledge/project-management/` | Add concise component-root `SKILL.md`. | Move `docs/PROJECT-MANAGEMENT.md` to `guides/PROJECT-MANAGEMENT.md`; move every file under `docs/pm/` directly to `guides/`; remove emptied `docs/pm/` and `docs/` with `rmdir`. | Project management needs a component entrypoint plus guide set. The prompt explicitly accepts `knowledge/project-management/guides/` as the successor to `docs/pm/`. |
| `knowledge/testing/` | Include in the same entrypoint contract; add concise component-root `SKILL.md`. | Move `docs/CODE-COVERAGE.md` to `guides/CODE-COVERAGE.md`; remove emptied `docs/` with `rmdir`. | `testing` is adjacent but part of `CF_FILES` and has the same stale `docs/` holdover shape. Excluding it would leave inconsistent package/source layout. |
| `knowledge/work-verification/` | Include for component-root `SKILL.md` only. | Keep `templates/LEDGER-DISCIPLINE.md`; do not move it to `guides/` in Arc07 unless a later slice finds package/link evidence that requires it. | The current surface is already under `templates/`, not `docs/`. It is routed as a reusable verification protocol/template surface. |

## Accepted Entrypoint Contract

Later implementation slices should create concise component-root entrypoints:

- `knowledge/agent-coordination/SKILL.md`
- `knowledge/code-auditing/SKILL.md`
- `knowledge/collaboration-framework/SKILL.md`
- `knowledge/contribution-style/SKILL.md`
- `knowledge/engineering-methods/SKILL.md`
- `knowledge/project-management/SKILL.md`
- `knowledge/testing/SKILL.md`
- `knowledge/work-verification/SKILL.md`

These component entrypoints are source/component entrypoints. Slice01 does not
authorize adding them to `SKILL_ZIP_NAMES` as separate installable packages.
They should be included in `collaboration-framework.zip` only as dependency
files routed from the composite framework package unless a later accepted plan
changes package topology.

## Collaboration-Framework Package Entrypoint

`knowledge/collaboration-framework/SKILL.md` should become the canonical source
entrypoint, while generated package output should still expose:

`collaboration-framework/SKILL.md`

That requires Makefile/package staging behavior rather than a naive `cp` that
preserves the source path inside the zip. The implementation should use an
explicit staged destination for the entrypoint and, if needed, extend
`scripts/stage-skill-entrypoint` or equivalent Makefile logic so source-local
links and package-local links both validate.

## Rejected Blind Renames

These existing long documents should not be directly renamed to `SKILL.md`:

- `SUBAGENT-DELEGATION-POLICY.md`
- `CODE-AUDIT.md`
- `AI-CONSTITUTION-SUPPLEMENT.md`
- `CONTRIBUTION-STYLE.md`
- `AI-ENGINEERING-METHODOLOGY.md`
- `PROJECT-MANAGEMENT.md`
- `CODE-COVERAGE.md`
- `LEDGER-DISCIPLINE.md`

They remain guide or template material and should be routed from concise
component entrypoints.

