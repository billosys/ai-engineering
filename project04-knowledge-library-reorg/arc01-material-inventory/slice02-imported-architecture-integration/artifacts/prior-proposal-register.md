# Prior Proposal Register

```yaml
project: project04-knowledge-library-reorg
arc: arc01-material-inventory
slice: slice02-imported-architecture-integration
artifact: prior-proposal-register
artifact-status: slice integration evidence
created-on: 2026-09-01
source-files-edited: false
```

## Purpose

This register records every Project04 project-level imported artifact with its
Project04 status, concrete relevance, and Arc02 preservation or decision
requirement. Status labels include accepted fact, working hypothesis,
constraint, conflict, and open question.

| Artifact path | Source project or origin | Project04 status | Concrete Project04 relevance | What Arc02 must decide or preserve |
|---------------|--------------------------|------------------|------------------------------|------------------------------------|
| `artifacts/operator-accepted-architecture.md` | Project02 Arc04 accepted architecture | accepted fact; constraint | Records `collaboration-framework` as daily-driver composer and the seven specialist components: `engineering-methods`, `project-management`, `work-verification`, `testing`, `code-auditing`, `agent-coordination`, and `contribution-style`. Also records `engineering-methods` ownership of source/package/release gates, ontology critique placement, component version-history policy, memory admission deferral, and CCDP separation. | Preserve accepted component names and roles. Decide directory contract without erasing the composer, component version histories, source/package/release gate ownership, or CCDP as separate protocol distribution. |
| `artifacts/component-file-layout-plan.md` | Project02 Arc05 Slice02 implementation plan | working hypothesis; conflict; open question | Proposes top-level component roots such as `engineering-methods/` and `project-management/`, while Project04's direction says `docs/` should become user docs and `knowledge/` should hold substrate and skill source. | Decide whether framework component roots stay top-level, move under `knowledge/`, use wrappers, or split source substrate from public docs. Preserve the component map even if paths change. |
| `artifacts/package-target-plan.md` | Project02 Arc05 Slice03 package/release plan | working hypothesis; constraint | Plans `collaboration-framework.zip` plus seven component zips, `COMPONENT_ZIPS`, `INSTALL_ZIPS`, `ALL_SKILL_FILES`, package roots matching component roots, and CCDP outside install behavior. | Decide package root names and source root relationship. Preserve generated package validation, installed route semantics, and CCDP outside skill-install packages. |
| `artifacts/skill-entrypoint-validation-plan.md` | Project02 Arc05 Slice03 validation plan | constraint; working hypothesis | Requires component-local `SKILL.md`, frontmatter, description length guard, sibling `version-history.md`, package-local links, and route-table wording across package boundaries. | Preserve thin, validated entrypoints and component version-history policy. Decide whether Project04 directory contract changes `ALL_SKILL_FILES` paths or validation script assumptions. |
| `artifacts/readme-wayfinding-plan.md` | Project02 Arc05 Slice03 README plan | working hypothesis; compatibility obligation | Plans README reader modes, composed use, standalone component table, migration notes, source checkout routes, generated zip routes, installed skill routes, and CCDP separation. | Decide whether final public docs live in README, `docs/`, or both. Preserve reader-mode distinctions and avoid making the daily-driver composer look deprecated. |
| `artifacts/migration-compatibility-plan.md` | Project02 Arc05 Slice03 compatibility plan | constraint; conflict; open question | Names old source paths, prompt-name compatibility, top-level `SKILL.md` shim risk, provenance preservation, version-history handling, package-root surprise risk, and cross-component relative-link risk. | Decide move, remain, or wrapper-doc treatment for old `docs/` and template paths. Preserve provenance and version histories. Set re-entry conditions for top-level `SKILL.md` compatibility. |
| `artifacts/package-path-link-exception-plan.md` | Project02 Arc05 Slice03 package-link plan | constraint; working hypothesis | Defines package-local link preference, source checkout wording, installed-skill route wording, source-only/provenance classifications, warning handling, and exception policy. | Preserve package-local repair before exceptions. Decide Project04 exception policy after target layout, package roots, and generated zip payloads are known. |
| `artifacts/implementation-sequence-roadmap.md` | Project02 Arc05 Slice04 source-edit roadmap | working hypothesis; constraint | Provides source-edit sequencing, commit boundaries, validation checkpoints, and coverage of all eight accepted components. It also says future source implementation requires explicit operator authorization. | Preserve sequencing discipline as input, but do not treat it as Project04 source-edit authorization. Decide whether Project04 target layout changes the source-edit slice order. |
| `artifacts/external-ontology-rubric-research.md` | Project04 project-level research input | open question; working hypothesis | Provides kind axis and topology axis vocabulary: domain/tooling, framework/operational, method, protocol/package, support/template, source/provenance; atomic, composite, bridge/integration, application/task bundle. It is input, not accepted taxonomy. | Preserve anti-tautology discipline. Arc02 should use it to ask directory-contract questions; Slice03 should test it against current and planned skill surfaces before public taxonomy is accepted. |

## Register Conclusions

- Accepted fact rows constrain Project04 behavior, but they do not decide final
  source root layout.
- Working hypothesis rows are useful prior plans that Arc02 must test against
  Project04's `docs/` and `knowledge/` direction.
- Constraint rows name behavior Project04 should preserve across any layout:
  entrypoint validation, version history, package-local links, generated zip
  checks, reader modes, and CCDP separation.
- Conflict and open question rows are the concrete input packet for Arc02's
  directory contract and for Slice03's kind/topology classification.
