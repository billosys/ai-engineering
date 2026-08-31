# Migration Compatibility Plan

```yaml
project: project02-collab-breakout
arc: arc05-implementation-plan
slice: slice03-package-readme-validation-plan
status: proposed-done
artifact-status: migration compatibility plan
source-files-edited: false
```

## Grounding

This compatibility plan consumes the verified Slice02 migration plan and
package/source contract register. It preserves provenance while planning
migration from the old monolithic collaboration-framework surface to the
accepted component roots.

## Compatibility Rows

| Surface | compatibility decision | migration action | provenance rule |
|---------|------------------------|------------------|-----------------|
| top-level SKILL.md | Treat as the old source path for the current monolithic framework. | Slice04 should decide whether implementation keeps a temporary shim, moves the file into `collaboration-framework/SKILL.md`, or rewrites README/source route text in the same commit. | Preserve top-level `SKILL.md` history in `collaboration-framework/version-history.md` and do not erase old source path references silently. |
| `docs/AI-CONSTITUTION-SUPPLEMENT.md` | Old source path for composer posture material. | Move/split into `collaboration-framework/guides/` with possible compatibility note. | Preserve supplement version history in component history. |
| `docs/AI-ENGINEERING-METHODOLOGY.md` | Old source path for methodology and gate material. | Move/split into `engineering-methods/guides/`, including component-boundary and source/package/release gates. | Preserve methodology history in `engineering-methods/version-history.md`. |
| `docs/PROJECT-MANAGEMENT.md` and `docs/pm/*` | Old source path for PM family. | Move/split into `project-management/SKILL.md`, `project-management/guides/`, and `project-management/examples/`. | Preserve `docs/pm/version-history.md` in `project-management/version-history.md`. |
| `templates/LEDGER-DISCIPLINE.md` | Old source path and support payload for work verification. | Split into guides and copy/move template under `work-verification/templates/`. | Preserve template/protocol history in `work-verification/version-history.md`. |
| `docs/CLAUDE-CODE-COVERAGE.md` | Old prompt name and old source path for coverage hardening. | Move/split into `testing/guides/`; add compatibility note that coverage hardening is now one guide in `testing`. | Preserve old prompt name in migration notes and `testing/version-history.md`. |
| `docs/SUBAGENT-DELEGATION-POLICY.md` | Old prompt name and old source path for delegation policy. | Move/split into `agent-coordination/guides/01-when-to-delegate.md` plus new context-packet/result-integration prose. | Preserve old prompt name in `agent-coordination/version-history.md`. |
| `docs/CODE-AUDIT.md` | Old prompt name and old source path for audit discipline. | Move/split into `code-auditing/guides/`. | Preserve audit prompt history in `code-auditing/version-history.md`. |
| `docs/CONTRIBUTION-STYLE.md` | Old source path for contribution voice/workflow. | Move/split into `contribution-style/guides/`. | Preserve contribution guide provenance in `contribution-style/version-history.md`. |
| `templates/CONTRIBUTION-TICKET.md` | Old source path for contribution support template. | Move/copy into `contribution-style/templates/CONTRIBUTION-TICKET.md`. | Preserve template provenance in component history. |
| generated package root `collaboration-framework/` | Keep root name for the composer but change payload. | Generated package root remains stable while contents become composer-local. | Record payload change in composer version history. |
| new generated package root set | Add seven component roots. | Implement new package targets and installed routes after Slice04 sequencing. | Record each package root as accepted Project02 architecture, not an ad hoc split. |

## Old Prompt Name Policy

- Old prompt name references stay as migration compatibility notes when they
  help users recognize previous workflows.
- New README and `SKILL.md` route text should prefer accepted component names:
  `testing`, `code-auditing`, `agent-coordination`, and `contribution-style`.
- Old source path references should be marked as historical/provenance when the
  file no longer exists at that path.

## Version-History Handling

- Each component gets sibling `version-history.md`.
- Existing embedded Version History sections should be moved into the relevant
  component history or summarized with enough provenance to preserve lineage.
- The migration should record expansion versus overwrite: broader components
  such as `testing` and `agent-coordination` are expansions from narrower old
  prompt names, not simple renames.

## Compatibility Risks

- Removing top-level `SKILL.md` without a README route update may break source
  checkout readers.
- Changing generated package root contents while keeping the same
  `collaboration-framework.zip` name may surprise offline users unless README
  and version history state the composer-only payload clearly.
- Cross-component relative links can fail in generated packages. Prefer
  package-local links and installed-skill route wording.
- Source provenance can be lost if implementation moves files mechanically
  without carrying version histories forward.
