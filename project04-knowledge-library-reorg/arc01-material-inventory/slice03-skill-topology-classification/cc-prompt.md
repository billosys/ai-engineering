# CC Prompt: Slice 03 Skill Kind and Topology Classification

You are working in the planning worktree for:

`/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning/project04-knowledge-library-reorg`

Open and complete:

`arc01-material-inventory/slice03-skill-topology-classification/`

## Required Reading

Before writing artifacts, read:

1. `/Users/oubiwann/.codex/skills/collaboration-framework/SKILL.md`
2. `/Users/oubiwann/.codex/skills/collaboration-framework/docs/PROJECT-MANAGEMENT.md`
3. `/Users/oubiwann/.codex/skills/collaboration-framework/docs/pm/01-scales-of-work.md`
4. `/Users/oubiwann/.codex/skills/collaboration-framework/docs/pm/02-canonical-planning-worktree.md`
5. `/Users/oubiwann/.codex/skills/collaboration-framework/docs/pm/03-planning-top-down.md`
6. `/Users/oubiwann/.codex/skills/collaboration-framework/templates/LEDGER-DISCIPLINE.md`
7. `project-plan.md`
8. `ledger.md`
9. `artifacts/external-ontology-rubric-research.md`
10. `arc01-material-inventory/arc-plan.md`
11. `arc01-material-inventory/ledger.md`
12. `arc01-material-inventory/slice03-skill-topology-classification/slice-plan.md`
13. `arc01-material-inventory/slice03-skill-topology-classification/ledger.md`
14. `arc01-material-inventory/slice01-source-surface-inventory/cdc-verification.md`
15. The three Slice01 artifacts under `arc01-material-inventory/slice01-source-surface-inventory/artifacts/`
16. `arc01-material-inventory/slice02-imported-architecture-integration/cdc-verification.md`
17. The three Slice02 artifacts under `arc01-material-inventory/slice02-imported-architecture-integration/artifacts/`

Inspect the source checkout at `/Users/oubiwann/lab/billosys/ai-engineering`
as needed for current skill surfaces, especially:

- `README.md`
- `SKILL.md`
- `knowledge/*/SKILL*.md`
- `knowledge/*/`
- `templates/`
- `protocols/ccdp/`
- `Makefile`
- `package-path-exceptions.tsv`

Do not edit source checkout files.

## Mission

Define a practical Project04 classification instrument for skill kind and
composition topology, then apply it to the repository's current and planned
skill/support surfaces.

The important trap to avoid: do not collapse the axes. A domain/tooling skill
is not automatically atomic. A framework/operational skill is not
automatically composite. A method skill may be atomic or composite depending
on evidence.

## Produce

Create the slice artifact home if needed:

`arc01-material-inventory/slice03-skill-topology-classification/artifacts/`

Then create:

- `artifacts/skill-kind-topology-decision-instrument.md`
- `artifacts/skill-kind-topology-classification-matrix.md`
- `artifacts/public-language-implications.md`

### `skill-kind-topology-decision-instrument.md`

Include:

- Purpose and scope.
- Source inputs used.
- Kind-axis definitions: domain/tooling, framework/operational, method,
  protocol/package, support/template, source/provenance, and any adjustment
  required by repository evidence.
- Topology-axis definitions: atomic, composite, bridge/integration layer, and
  application/task bundle.
- Evidence questions for each axis.
- Classification rules that prevent shortcut reasoning such as
  "atomic equals domain" or "composite equals framework."
- Borderline and re-entry conditions: what evidence would change a
  classification.
- A note that `external-ontology-rubric-research.md` is tested input, not
  accepted taxonomy.

### `skill-kind-topology-classification-matrix.md`

Classify, at minimum:

- Current packaged source surfaces:
  - `knowledge/rust/`
  - `knowledge/go/`
  - `knowledge/cpp/`
  - `knowledge/js/`
  - `knowledge/erlang/`
  - `knowledge/cobalt/`
  - `knowledge/design/`
  - `knowledge/tailwindcss/`
  - `knowledge/deno/`
  - `knowledge/biome/`
  - top-level `SKILL.md` / current `collaboration-framework`
- Planned Project02 framework components:
  - `collaboration-framework`
  - `engineering-methods`
  - `project-management`
  - `work-verification`
  - `testing`
  - `code-auditing`
  - `agent-coordination`
  - `contribution-style`
- Planned Project03 method skill:
  - `concept-card-method`
- Protocol/support surfaces:
  - CCDP
  - `templates/GUIDE.md`
  - `templates/LEDGER-DISCIPLINE.md`
  - `templates/CONTRIBUTION-TICKET.md`

For each row, record:

- surface path or planned surface name;
- current/planned status;
- kind classification;
- topology classification;
- evidence;
- confidence;
- caveats or re-entry conditions;
- implication for Arc02 source-root or package-root decisions.

### `public-language-implications.md`

Include:

- Vocabulary to use in README/docs/skill wayfinding.
- Vocabulary to avoid because it collapses kind/topology or overclaims source
  state.
- How to talk about atomic skills, composite skills, bridges, task bundles,
  protocol packages, and support templates.
- What Arc02 must decide for the target directory contract.
- What Arc05 should reserve for final public wording.
- Risks if public docs imply `concept-card-method` is already implemented, if
  CCDP becomes a skill package accidentally, or if `collaboration-framework`
  sounds deprecated.

## Ledger Work

Update `ledger.md` as you work. For each row you complete, set `Status` to
`done` and fill `Evidence` with `attested:` evidence pointing to the artifact
and command result. Leave no open rows when you hand back.

Run every ledger Verify command from:

`arc01-material-inventory/slice03-skill-topology-classification/`

Also run:

```sh
git -C /Users/oubiwann/lab/billosys/ai-engineering status --short
git -C /Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning diff --check
```

## Closing Report

Create `closing-report.md` only after all ledger rows are final. The closing
report must include:

- Summary.
- Ledger Walk with all 7 rows.
- Artifact Inventory.
- Verification Run.
- Bubble-up to the Arc:
  - whether Slice03 delivered its assigned Arc01 piece;
  - findings for Arc01 and whether they require an `arc-plan.md` update before
    Slice04;
  - silent-drop diff comparing scope as specified to scope as delivered.
- What Worked.
- Closure statement with row counts.

Expected final status is `proposed-done`; CDC will verify independently.

## Constraints

- Do not edit source checkout files.
- Do not create final public docs.
- Do not decide Arc02's final directory contract.
- Do not treat planned surfaces as current source surfaces.
- Do not treat the external ontology rubric as accepted taxonomy without
  repository evidence.
