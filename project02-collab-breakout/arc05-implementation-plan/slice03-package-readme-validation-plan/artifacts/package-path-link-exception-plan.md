# Package Path Link Exception Plan

```yaml
project: project02-collab-breakout
arc: arc05-implementation-plan
slice: slice03-package-readme-validation-plan
status: proposed-done
artifact-status: package path link exception plan
source-files-edited: false
```

## Grounding

This plan consumes verified Slice01 release validation, verified Slice02
package/source contract artifacts, Project01 package-path closure evidence,
and the current `scripts/check-package-paths` behavior. It is a release-surface
plan, not a source edit.

## Link Strategy

| Link kind | Policy | Example route wording |
|-----------|--------|-----------------------|
| package-local | Preferred inside every generated package. Links from a component `SKILL.md` or guide should target files under that package root. | Use `guides/01-testing-discipline.md`, `templates/CONTRIBUTION-TICKET.md`, or `version-history.md` when the target ships in the same package. |
| source checkout | Allowed in README and source-only guidance when the target is expected to exist only in the repository. | "In a source checkout, read `protocols/ccdp/README.md`" or "Source provenance remains in the historical migration note." |
| installed-skill | Preferred for cross-component routes after packaging. | "Load `/work-verification` for ledger mechanics" instead of linking from `project-management` into another package root. |
| installed skill | Use plain route wording in README and route tables where a loader command is clearer than a file path. | "Use `/agent-coordination` when coordinating subagents or multiple LLM surfaces." |
| source-only | Classify explicitly when the target is provenance, history, or source-clone-only material. | Old docs paths can be named as migration provenance, not package links. |
| provenance | Preserve historical source origins without forcing generated package inclusion. | "Derived from `docs/CLAUDE-CODE-COVERAGE.md`" is provenance, not a package-local dependency. |

## Exception Policy

- Prefer package-local link repairs over `package-path-exceptions.tsv` rows.
- Add a package-path exception only after the source path is intentionally not
  bundled and the component still needs to name it.
- `package-path-exceptions.tsv` rows must use the existing TSV schema:
  package, document, target, classification, disposition, reason, source, and
  expires.
- Explicit exception recommendations are valid only for classifications the
  checker allows, especially `repo-only/provenance`, `example-project path`, or
  `external URL`.
- Do not add broad wildcard exceptions for new generated package roots unless
  a later implementation slice records the exact reason and expiration.
- Treat an accepted warning as visible debt with a reason and re-entry
  condition, not as suppressed success.

## Accepted Warning Handling

| Finding class | Default action | When an accepted warning is valid |
|---------------|----------------|-----------------------------------|
| `bundled-reference` warning | Fix package-local path if the target ships in the generated package. | Valid only for code-span shorthand where the package checker is intentionally conservative. |
| `source-clone-reference` warning | Prefer README/source reader wording or installed-skill route wording. | Valid when source-only context is explicitly the point. |
| `repo-only/provenance` warning | Convert to provenance text or add explicit exception with rationale. | Valid for historical source paths retained as provenance. |
| `example-project path` warning | Keep as code/example text where appropriate. | Valid when the path is illustrative and not a package asset. |
| `parser false positive` warning | Reword or leave visible with rationale. | Valid when the token is clearly not a path users should open. |

## Generated Package Checks

- Every generated package should have one zip root matching its component root.
- `make check-package-paths` should run against all skill zips in
  `INSTALL_ZIPS` after component packages are implemented.
- Component packages should aim for 0 hard failures and bounded warnings with
  explicit rationale.
- Existing `collaboration-framework.zip` exceptions for domain skill
  placeholders should not be copied into specialist packages unless the same
  source-only/provenance condition recurs.
