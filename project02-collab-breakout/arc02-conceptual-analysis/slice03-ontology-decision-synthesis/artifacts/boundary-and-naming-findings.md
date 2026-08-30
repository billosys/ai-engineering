# Boundary And Naming Findings

```yaml
project: project02-collab-breakout
arc: arc02-conceptual-analysis
slice: slice03-ontology-decision-synthesis
status: proposed-done
architecture-decisions: none
findings-status: analytical, non-final, not accepted architecture
```

## Evidence Basis

These findings consume the Slice01 input contract and CDC verification, then
synthesize the verified Slice02 `candidate-boundary evaluation`,
`component relationship map`, and `conceptual risk register`.

Every finding cites a Slice02 evidence basis and routes follow-up to Arc03
functional analysis, Arc04 architecture, or Arc05 implementation planning.
Project01 and `project01-harmonise-paths` source/package rules remain a
cross-cutting constraint: package-local links, zip roots, release surface
guidance, and `make check-package-paths` must remain component contract gates.

## Findings

| ID | Category | Finding | Slice02 evidence basis | Arc03 / Arc04 / Arc05 action |
|----|----------|---------|------------------------|------------------------------|
| BNF-01 | mislabel | `coverage-hardening-discipline` is broader than `CLAUDE-CODE-COVERAGE.md`; the current name and Cargo-shaped examples understate the intended repository-adapted discipline. | Risk register R-01 and R-11; candidate row for `coverage-hardening-discipline`; source grounding in `docs/CLAUDE-CODE-COVERAGE.md`. | Arc03 should test non-Rust usage moments. Arc04 should choose a surface-neutral name or explicitly keep legacy naming. Arc05 should update package-local links and release surface checks if renamed. |
| BNF-02 | mislabel | `agent-adapter-and-routing` exists conceptually but is hidden in notes rather than owned by a named guide. | Risk register R-02; candidate row for `agent-adapter-and-routing`; relationship map adapter edges. | Arc03 should test standalone component usability without the top-level composer. Arc04 should decide central adapter, per-component note, or both. Arc05 should prevent role-language drift. |
| BNF-03 | mislabel | `verification-methodology` is a shared concept, not a proven component; no source file exclusively owns it. | Risk register R-19; candidate row for `verification-methodology`; relationship map evidence/close/audit overlap. | Arc03 should test whether users ever load this separately. Arc04 should likely keep it as ontology/dependency edge unless a direct load moment appears. |
| BNF-04 | improper merge | `engineering-methodology-and-process` currently narrates posture, substrate, SDLC, verification, audit, coverage, and delegation together. This may preserve monolithic load cost. | Risk register R-03; candidate rows for methodology, posture, audit, coverage, delegation, and verification. | Arc03 should test load moments for methodology-only versus specialized operational work. Arc04 should split owned methodology rules from routed components. |
| BNF-05 | improper merge | Distribution guidance can improperly merge reader adapters, CCDP contrast, and hard package/release gates. | Risk register R-04; rows for `repository-orientation-and-distribution`, `protocol-distribution-guidance`, and `path-contract-constraints`. | Arc04 should separate adapter guidance from cross-cutting gates. Arc05 should enforce source/package, package-local, zip, release surface, and `make check-package-paths` behavior. |
| BNF-06 | improper split | Ledger evidence semantics and PM close lifecycle mechanics can drift if `ledger-verification-protocol`, `slice-close-and-bubble-up`, and `arc-project-composition-close` are split without dependency direction. | Risk register R-05; relationship map edges `slice-close-and-bubble-up uses ledger-verification-protocol` and `arc-project-composition-close uses ledger-verification-protocol`. | Arc04 should make ledger the owner of evidence semantics and PM the owner of lifecycle routing. Arc05 should package links so both surfaces remain coherent. |
| BNF-07 | improper split | Contribution style and ticket template are jointly strong but separately weaker. | Risk register R-06 and R-18; rows for `contribution-style-and-voice` and `contribution-ticket-template`. | Arc04 should package the template as a support asset under contribution guidance. Arc05 should verify package-local template links. |
| BNF-08 | improper split | PM family members have distinct load moments, but evidence does not yet support every split file as a top-level component. | Risk register R-20; PM family grouping in component relationship map. | Arc03 should test PM wayfinder and guide load moments. Arc04 should decide one PM component with internal guides versus separately loadable family members. |
| BNF-09 | missing concept | A component-maintenance contract is missing for post-breakout synchronization across components, README/SKILL routing, support assets, templates, version histories, and package checks. | Risk register R-07; row for `framework-maintenance-discipline`; Arc02 question Q-14. | Arc04 should define maintenance owner and required component contract fields. Arc05 should make those fields checkable. |
| BNF-10 | missing concept | A reusable abstraction-boundary or ontology-critique discipline is not yet a framework component, even though abstraction/generalization failure is a named risk. | Risk register R-08; Arc01 synthesis underfit risk; Arc02 question Q-05. | Arc03 should determine whether this is a repeatable user workflow. Arc04 should decide whether to add a component, keep it as Project02-specific analysis, or route to concept-card method work. |
| BNF-11 | overclaimed mechanism | Posture and methodology improve behavior only when loaded and honored; they are not mechanical enforcement. | Risk register R-09; rows for posture and methodology. | Arc04 should avoid claiming automatic behavioral guarantees. Arc05 should retain evidence-grade and operator acceptance language. |
| BNF-12 | overclaimed mechanism | The PM scale model provides judgment rules and a five-iteration budget, not an automated context-budget proof. | Risk register R-10; row for `project-management-scale-model`. | Arc03 should test actual load/cost and context behavior. Arc04 should describe this as human/LLM judgment support, not enforcement. |
| BNF-13 | underfit | Coverage hardening is underfit for general framework use while examples remain surface- and language-shaped. | Risk register R-11; coverage candidate row. | Arc04 should require language-neutral contract text plus repository-specific command adaptation. Arc05 should keep examples as examples, not hidden requirements. |
| BNF-14 | underfit | Per-component package contracts do not exist yet, even though Project01 gates apply to every future component. | Risk register R-12; path-contract row; Project01 carry-forward language. | Arc04 should add contract fields for package behavior, source paths, and gates. Arc05 should make `make check-package-paths` and related checks explicit. |
| BNF-15 | overfit | `planning-confirmation-protocol`, PM examples, and PM provenance are overfit as standalone components on current evidence. | Risk register R-13 and R-14; rows for confirmation, examples, and provenance. | Arc03 can test direct load demand. Arc04 should default them to PM support assets unless evidence changes. |
| BNF-16 | overlap | Evidence discipline, silent-drop prevention, spec-softening, and partial-adoption language overlap across methodology, ledger, PM close, and code audit. | Risk register R-15; relationship map ledger/methodology/audit edges. | Arc04 should assign primary owners and citation edges. Arc05 should avoid duplicate maintained copies of core semantics. |
| BNF-17 | overlap | README orientation, top-level SKILL routing, and agent-adapter notes all route users or agents into the framework. | Risk register R-16; relationship map adapter grouping. | Arc03 should test source clone, package zip, and standalone component entry. Arc04 should decide composer/adapter boundaries. |
| BNF-18 | duplication | Some duplication is acceptable when ownership is explicit: contribution template repeats calibrated honesty, and PM examples/provenance repeat rationale. | Risk register R-17 and R-18. | Arc04 should preserve deliberate reinforcement while preventing separate maintenance tracks. Arc05 should verify support assets travel with owners. |

## Unresolved Relationship Questions

- Does `verification-methodology` stay a non-component concept or become a
  thin shared guide?
- Does project management ship as one component with internal guides, or as a
  PM wayfinder plus separately loadable component family members?
- Do `code-audit-discipline` and `coverage-hardening-discipline` remain
  sibling operational components, or compose into a broader quality-floor
  family?
- Does `agent-adapter-and-routing` live centrally, locally in each component,
  or both?
- Which Project01 package/release gate rules are centralized, repeated in each
  component contract, or enforced only by future package checks?

## Component-Maintenance Concern

The component-maintenance issue is cross-cutting. Once multiple components
exist, a future change may need synchronized updates to source docs, packaged
SKILL entrypoints, README source/package guidance, templates, PM provenance,
and package/release gate checks. Arc04 should define this maintenance owner
before accepting architecture, and Arc05 should make it verifiable.
