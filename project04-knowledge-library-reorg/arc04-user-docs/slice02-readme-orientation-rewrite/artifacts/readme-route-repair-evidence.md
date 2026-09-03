# README Route Repair Evidence

Source commit: `cebadeb3009386e446b3454f263592d3115efea7`

## Route Repairs

- `docs/dev` references were removed from README. New-domain and contribution
  details are routed to `docs/contributing.md` for Slice03 expansion.
- `docs/design` references were removed from README. Historical design material
  remains provenance, not current user navigation.
- Former framework docs under `docs/` were repaired in `docs/ORIGINS.md`:
  - `./CODE-AUDIT.md` -> `../knowledge/code-auditing/docs/CODE-AUDIT.md`
  - `./AI-ENGINEERING-METHODOLOGY.md` -> `../knowledge/engineering-methods/docs/AI-ENGINEERING-METHODOLOGY.md`
  - `./AI-CONSTITUTION-SUPPLEMENT.md` -> `../knowledge/collaboration-framework/docs/AI-CONSTITUTION-SUPPLEMENT.md`
  - `./PROJECT-MANAGEMENT.md` -> `../knowledge/project-management/docs/PROJECT-MANAGEMENT.md`
  - `./SUBAGENT-DELEGATION-POLICY.md` -> `../knowledge/agent-coordination/docs/SUBAGENT-DELEGATION-POLICY.md`
- Moved template paths were repaired in `docs/ORIGINS.md`:
  - `../templates/LEDGER-DISCIPLINE.md` -> `../knowledge/work-verification/templates/LEDGER-DISCIPLINE.md`
- Current README routes preserve valid `docs/`, `knowledge/`,
  `protocols/ccdp`, and `templates/GUIDE.md` surfaces.

## Targeted Route Check Evidence

Command:

```sh
rg -n "\[[^\]]+\]\([^\)]+\)|https?://|docs/|knowledge/|protocols/|templates/|Makefile|package" README.md docs
```

Result: matched expected current routes in README, seven focused doc stubs,
and repaired `docs/ORIGINS.md` links into `knowledge/`.

Command:

```sh
rg -n "docs/dev|docs/design|CODE-AUDIT|AI-ENGINEERING|PROJECT-MANAGEMENT|SUBAGENT|LEDGER-DISCIPLINE|CONTRIBUTION-TICKET|templates/" README.md docs
```

Result: no stale `docs/dev`, `docs/design`, or `CONTRIBUTION-TICKET` routes.
Remaining matches are:

- `README.md` references to `templates/GUIDE.md`: current valid route.
- `README.md` layout line for `templates/`: current valid top-level directory.
- `docs/ORIGINS.md` filename references such as `CODE-AUDIT.md`,
  `AI-ENGINEERING-METHODOLOGY.md`, `PROJECT-MANAGEMENT.md`,
  `SUBAGENT-DELEGATION-POLICY.md`, and `LEDGER-DISCIPLINE.md`: repaired
  historical/context links now pointing into `knowledge/`.

Verdict: no stale route remains in README/docs for this slice scope.
