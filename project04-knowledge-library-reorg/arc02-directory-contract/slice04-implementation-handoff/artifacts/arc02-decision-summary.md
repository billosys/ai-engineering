# Arc02 Decision Summary

```yaml
project: project04-knowledge-library-reorg
arc: arc02-directory-contract
slice: slice04-implementation-handoff
artifact: arc02-decision-summary
artifact-status: implementation handoff input
created-on: 2026-09-02
source_checkout: /Users/oubiwann/lab/billosys/ai-engineering
source-files-edited: false
```

## Purpose

This summary preserves the accepted contract, operator gate, explicit
exception, and re-entry condition set that Arc03 should consume. It is not
source-edit authorization and not formal arc close.

## Accepted Contract Decisions

- `docs/` is user-facing explanation, not default substrate.
- `knowledge/` is the default substrate root.
- `knowledge/<component>/` is the accepted default Project02 component source
  root family.
- `knowledge/collaboration-framework/` is the target composer source root when
  composer material moves.
- Source roots and package roots remain separate axes.
- `knowledge/biome/` remains a multi-entrypoint source root.
- Selected-file `collaboration-framework` packaging remains an explicit
  transitional exception class until replaced or validated.
- CCDP remains separate under `protocols/ccdp/` and must not be added to
  installable skill packages.
- Atomic/composite topology remains a separate axis from skill kind.
- `README.md`, `SKILL.md`, `AGENTS.md`, and `CLAUDE.md` remain top-level
  compatibility surfaces until an implementation slice changes them with
  validation evidence.

## Operator Gates

- Top-level SKILL.md remains unresolved until Arc03 chooses a validated shim,
  replacement route, or explicit no-shim implementation path.
- Persistent package-path exception rows require operator approval.
- Accepted warning rows that remain after an implementation slice require
  operator approval.
- CCDP package-policy changes require operator approval.
- Public vocabulary decisions before Arc05 require operator approval.
- Broad package-path exceptions covering more than one owner or package root
  require operator approval.

## Explicit Exception Classes

- Top-level `SKILL.md` compatibility while composer source moves.
- Selected-file `collaboration-framework` package assembly during transition.
- Biome multi-entrypoint package behavior from `knowledge/biome/`.
- Cross-cutting support templates that remain in top-level `templates/`.
- CCDP protocol references that remain outside installable skill packages.
- Narrow source-only, provenance, external URL, transitional wrapper, or
  checker false-positive package-path exception rows.

## Re-Entry Conditions

- Re-enter Project02 if implementation cannot preserve accepted component
  roles, daily-driver composer behavior, independent loadability, or package
  validation under `knowledge/<component>/`.
- Re-enter Project03 if `knowledge/concept-card-method/` cannot preserve the
  planned method-skill architecture without claiming live source.
- Re-enter CCDP policy if `protocols/ccdp/` cannot remain separate under
  package validation.
- Re-enter kind/topology classification if entrypoints, generated package
  behavior, source roots, or package roots change load reason or composition
  identity.
- Re-enter package-path exception policy if package-local link repair cannot
  keep exceptions narrow.

## Arc02 Composition Evidence Prepared

This decision summary, together with the readiness packet and source-edit
roadmap, prepares the Arc02 composition row for formal arc close:

- target layout is represented by the accepted contract;
- path contract is represented by the accepted directory and wrapper/migration
  note rules;
- migration plan is represented by the ordered source-edit roadmap;
- compatibility is represented by the validation and compatibility matrix;
- exception policy is represented by the package-path exception policy;
- source root and package root decisions are represented as separate axes;
- atomic and composite remain topology labels independent of skill kind.

This is not arc close. Formal arc close remains separate arc-level work after
CDC verifies Slice04.

## Boundary

Arc03 implementation, Arc04 end-user docs, and Arc05 public vocabulary remain
later-arc responsibilities. The source checkout remains untouched by this
planning only handoff.
