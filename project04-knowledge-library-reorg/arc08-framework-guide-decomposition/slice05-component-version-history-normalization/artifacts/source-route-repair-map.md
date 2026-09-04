# Source Route Repair Map

Source commit: `657f156c7ad8048e60727275c2eed0d910de7f45`

## Route Repairs

| Surface | Change | Reason |
|---------|--------|--------|
| `Makefile` `CF_FILES` | Added the five new sibling histories for `work-verification`, `testing`, `code-auditing`, `agent-coordination`, and `contribution-style`. | Ensures generated `collaboration-framework.zip` carries the component histories beside each component `SKILL.md`. |
| `knowledge/work-verification/SKILL.md` | Bumped to `1.0.1` and added a route to `./version-history.md`. | Makes the sibling history discoverable from the component entrypoint. |
| `knowledge/testing/SKILL.md` | Bumped to `1.0.1` and added a route to `./version-history.md`. | Makes the sibling history discoverable from the component entrypoint. |
| `knowledge/code-auditing/SKILL.md` | Bumped to `1.0.1` and added a route to `./version-history.md`. | Makes the sibling history discoverable from the component entrypoint. |
| `knowledge/agent-coordination/SKILL.md` | Bumped to `1.0.1` and added a route to `./version-history.md`. | Makes the sibling history discoverable from the component entrypoint. |
| `knowledge/contribution-style/SKILL.md` | Bumped to `1.0.1` and added a route to `./version-history.md`. | Makes the sibling history discoverable from the component entrypoint. |
| `knowledge/code-auditing/guides/CODE-AUDIT.md` | Replaced embedded `## Version History` with `## Component History` pointer to `../version-history.md`. | Prevents component history from remaining under `guides/`. |
| `knowledge/work-verification/templates/LEDGER-DISCIPLINE.md` | Replaced embedded `## Version History` with `## Component History` pointer to `../version-history.md`. | Prevents component history from remaining under `templates/`. |
| `knowledge/collaboration-framework/SKILL.md` | Bumped to `1.5.2`; no route-table change. | Records that the composer package surface changed by including new component histories. |
| `knowledge/collaboration-framework/version-history.md` | Added `1.5.2` package-history entry. | Records the collaboration-framework package-content update. |

## No-Op / Dispositioned Surfaces

- `README.md`: no live references to the new sibling component history paths required repair.
- `docs/`: existing route references still point to live guide/template payloads and did not need history-path repair.
- `AGENTS.md`: already contains the framework component sibling-history rule from Slice02; no wording change was required.
- `workbench/release-notes/RELEASE-0.5.0.md`: release-note component descriptions were not made stale by the history normalization; Slice06 owns final release reconciliation.
- Package-path exceptions: no exception update was required; the package-path gate passed with zero hard failures.

Slice02 Expedited Mode guardrails and Slice03/Slice04 split guide routes were preserved.
