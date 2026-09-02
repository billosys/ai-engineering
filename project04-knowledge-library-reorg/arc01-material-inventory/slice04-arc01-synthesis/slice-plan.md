# Slice 04: Arc01 Synthesis for Directory Contract

```yaml
project: project04-knowledge-library-reorg
arc: arc01-material-inventory
slice: slice04-arc01-synthesis
status: open
opened-on: 2026-09-01
source_checkout: /Users/oubiwann/lab/billosys/ai-engineering
planning_checkout: /Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning
source-files-edited: false
```

## Goal

Synthesize the verified Arc01 evidence into an Arc02-ready packet. This slice
answers: what facts, hypotheses, unresolved decisions, source-edit risks, and
validation obligations must Arc02 use when it defines the target directory
contract for `docs/`, `knowledge/`, `templates/`, `protocols/`, README, skill
entrypoints, and package roots?

This slice is the recomposition pass for Arc01's evidence base. It does not
choose the final directory contract, move files, or write public docs.

## Scope

In scope:

- Consume the verified Slice01 source inventory artifacts and
  `cdc-verification.md`.
- Consume the verified Slice02 imported-architecture integration artifacts and
  `cdc-verification.md`.
- Consume the verified Slice03 skill kind/topology artifacts and
  `cdc-verification.md`.
- Synthesize current source-backed facts separately from imported accepted
  facts, working hypotheses, unresolved decisions, and re-entry conditions.
- Produce an Arc02 readiness packet that states whether Arc02 has enough input
  to open a target directory contract and migration-plan arc.
- Produce a directory-contract requirements list for `docs/`, `knowledge/`,
  framework/operational components, method skills, protocol surfaces, template
  surfaces, README/SKILL wayfinding, package roots, and validation gates.
- Produce a decision/risk register that Arc02 can turn into ledger rows.
- Identify validation obligations and source-edit risks for later arcs without
  executing them.
- Preserve the external ontology rubric as tested input rather than accepted
  public taxonomy.
- Produce durable artifacts under this slice's `artifacts/` directory.

Out of scope:

- Moving, deleting, renaming, or editing source checkout files.
- Editing source `README.md`, source `SKILL.md`, `docs/`, `knowledge/`,
  `templates/`, `protocols/`, `Makefile`, package-path exceptions, validation
  scripts, or generated zips.
- Selecting the final Arc02 directory contract.
- Writing final public documentation or final README/SKILL wording.
- Re-opening Project02 component architecture or Project03 method-skill
  architecture except to record conflicts or re-entry conditions.
- Treating prior implementation proposals as source-edit authorization.
- Closing Arc01. Arc close remains a separate recomposition step after Slice04
  is verified-closed.

## Artifacts

Expected artifact home: `artifacts/`.

Expected artifacts:

- `artifacts/arc02-readiness-packet.md`
- `artifacts/directory-contract-requirements.md`
- `artifacts/arc01-synthesis-decision-register.md`

## Verification Approach

Use planning-tree inspection with targeted `rg` checks. The artifacts should
cite concrete Slice01, Slice02, and Slice03 evidence paths; distinguish
accepted facts from hypotheses and open decisions; carry forward the
docs/knowledge split; preserve current-versus-planned and kind-versus-topology
boundaries; and identify validation obligations without authorizing source
edits.

## Exit Criteria

- The Arc02 readiness packet consumes all three verified prior slices and
  states whether Arc02 is ready to open.
- Accepted facts, working hypotheses, unresolved decisions, risks, validation
  obligations, and re-entry conditions are separated.
- The directory-contract requirements list covers `docs/`, `knowledge/`,
  framework/operational components, method skills, `protocols/ccdp/`,
  `templates/`, README/SKILL wayfinding, package roots, package-local links,
  `Makefile`, package-path exceptions, and compatibility surfaces.
- The decision register gives Arc02 a concrete queue of decisions, options,
  evidence sources, preservation requirements, and validation obligations.
- The synthesis preserves skill kind and topology as independent axes and does
  not convert the external ontology rubric into final public taxonomy.
- Arc01 composition evidence is prepared for formal arc close.
- No source checkout files are edited.

## Version History

### v1.0 - 2026-09-01

Opened Slice04 as the Arc01 synthesis and Arc02 directory-contract readiness
packet for Project04.
