# Project04 Close-Readiness Report

```yaml
project: project04-knowledge-library-reorg
arc: arc06-validation-release
slice: slice04-release-readiness-operator-acceptance
status: proposed-done
project_close_status: ready-after-cdc-arc06-close-and-operator-decision
```

## Definition of Done Mapping

Project04's definition of done requires a clear, tested, and documented split
between `docs/` as end-user documentation about repository materials and
`knowledge/` as the raw and derived knowledge-library substrate consumed by
skill packages.

Arc06 completes the validation/release-readiness side of that definition by
showing that README/docs links, installable skill packages, temporary install
behavior, CCDP protocol-package behavior, generated artifact handling, and
source/planning cleanliness are reconciled after the final layout.

## P-6 Mapping

Project ledger P-6 requires Arc06 to close with validation, packaging,
installability, CCDP package separation, and operator acceptance reconciled
after the final layout.

Slice04 evidence supports P-6 close-readiness:

- Arc06 Slice01 is verified-closed with validation surface, package/install
  command matrix, CCDP freshness decision map, source-edit authorization, and
  release-risk inventory.
- Arc06 Slice02 is verified-closed with package-path checks, package builds,
  generated installable package inspection, temporary install smoke, and no
  required source repair.
- Arc06 Slice03 is verified-closed with CCDP freshness resolved, `make
  ccdp-package` passing, `make check-ccdp-package` passing, and protocol
  package separation preserved.
- Arc06 Slice04 reconciles those results and re-runs the final validation
  gates.

P-6 should remain open until CDC verifies Slice04 and performs formal Arc06
close with `arc06-validation-release/closing-report.md`.

## P-7 Mapping

Project ledger P-7 requires a project-level acceptance demo showing that a
user can orient from README into docs for explanation and into knowledge for
actual material substrate without path/category or atomic/composite ambiguity.

Slice04 evidence supports P-7 readiness but does not close P-7:

- README links to focused docs for repository overview, skill library,
  collaboration framework, knowledge-library anatomy, building/installing,
  protocols, contributing, and origins.
- README identifies `docs/` as end-user repository documentation.
- README identifies `knowledge/` as skill source and derived knowledge
  substrate.
- README identifies `protocols/` as protocol distributions, including CCDP.
- Focused docs preserve the same route model.
- Public skill language distinguishes kind from topology, and distinguishes
  atomic from composite.
- CCDP remains a protocol package, not an installable skill package.

P-7 should remain open until project close or operator acceptance reproduces
the project-level route demo as acceptance evidence.

## Remaining Close Step

The remaining close step sequence:

1. CDC verifies Arc06 Slice04.
2. CDC closes Arc06 and updates Arc06 ledger row A-4 and A-5.
3. CDC or the operator updates project ledger P-6 based on Arc06 close.
4. Operator acceptance or project-close verification reproduces P-7.
5. Project04 closes if P-6 and P-7 are both satisfied and no acceptance
   prerequisite remains.

## Acceptance Prerequisite

The acceptance prerequisite is an explicit operator acceptance decision or an
equivalent project-close acceptance artifact. This report prepares the
evidence; it does not record final operator acceptance.
