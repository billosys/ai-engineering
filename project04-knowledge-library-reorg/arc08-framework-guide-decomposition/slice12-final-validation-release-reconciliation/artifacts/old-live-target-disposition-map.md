# Old Live-Load Target Disposition Map

## Scan

Command:

```sh
rg -n "AI-CONSTITUTION-SUPPLEMENT\.md|AI-ENGINEERING-METHODOLOGY\.md|CODE-AUDIT\.md|CODE-COVERAGE\.md|SUBAGENT-DELEGATION-POLICY\.md|CONTRIBUTION-STYLE\.md|guides/09-worked-example-odm\.md|guides/version-history\.md" README.md AGENTS.md Makefile docs knowledge/collaboration-framework knowledge/engineering-methods knowledge/project-management knowledge/work-verification knowledge/testing knowledge/code-auditing knowledge/agent-coordination knowledge/contribution-style assets/packaging/path-exceptions.tsv protocols/ccdp/README.md protocols/ccdp/src/README.md workbench/release-notes/RELEASE-0.5.0.md
```

Result: hits found only in historical, provenance, or explicit disposition
contexts. No stale live route target remained.

## Disposition

| Target | Remaining Context | Disposition |
|--------|-------------------|-------------|
| `AI-CONSTITUTION-SUPPLEMENT.md` | `collaboration-framework` guide provenance and version-history lineage | Historical/provenance text only; not a live route. |
| `AI-ENGINEERING-METHODOLOGY.md` | `collaboration-framework/version-history.md` older history entries | Historical text only; not a live route. |
| `CODE-AUDIT.md` | `AGENTS.md`, release notes, and version-history disposition | Explicitly says old path is not live; no defect. |
| `CODE-COVERAGE.md` | `AGENTS.md`, testing guide provenance, release notes, and version-history disposition | Explicitly says old path was renamed or is provenance; no live route. |
| `SUBAGENT-DELEGATION-POLICY.md` | `AGENTS.md`, release notes, and version-history disposition | Explicitly says old path is not live; no defect. |
| `CONTRIBUTION-STYLE.md` | release notes and version-history disposition | Explicitly says old path was split or is not live; package-local `CONTRIBUTION-TICKET.md` template remains valid. |
| `guides/09-worked-example-odm.md` | `project-management/version-history.md` | Historical move record to `examples/01-worked-example-odm.md`; not a live route. |
| `guides/version-history.md` | `project-management/version-history.md` | Historical move record to sibling `version-history.md`; not a live route. |

## Verdict

Pass. Old monolith and pre-split guide filename hits are classified as
historical, provenance, disposition, or package-local template text. No stale
live-load target remains.
