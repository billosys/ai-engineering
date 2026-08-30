# Conceptual Risk Register

```yaml
project: project02-collab-breakout
arc: arc02-conceptual-analysis
slice: slice02-candidate-boundary-evaluation
status: proposed-done
architecture-decisions: none
```

## Scope

This register records conceptual risks found while applying the Slice01
conceptual-analysis method to the Slice01 component-boundary ledger. It cites
Arc01 evidence, current source grounding, and the Slice02 evaluation artifacts.
Project03 remains operator-accepted input-only. Project01 and
`project01-harmonise-paths` remain cross-cutting constraint and
package/release gate inputs.

The soft layout hypothesis is a low-weight hypothesis, not accepted
architecture. Evidence outranks the sketch. The register is analytical and
non-final; final architecture remains deferred to Arc03 functional analysis,
Arc04 architecture work, and operator acceptance.

## Risk Rows

| Risk ID | Category | Affected label or labels | Evidence basis | Risk disposition | Follow-up |
|---------|----------|--------------------------|----------------|------------------|-----------|
| R-01 | mislabel | `coverage-hardening-discipline` | Current file is `docs/CLAUDE-CODE-COVERAGE.md`; it contains Codex adaptation notes but remains Claude/Cargo-shaped in title and examples. | Confirmed risk. The concept is broader than its filename and examples. | Slice03 should record a naming critique and ask Arc04 whether a surface-neutral component name is required. |
| R-02 | mislabel | `agent-adapter-and-routing` | Source evidence is mostly notes inside `SKILL.md` and methodology rather than a named adapter file. | Confirmed risk. The adapter exists conceptually but is hidden in current routing prose. | Slice03 should decide whether to recommend a central adapter guide or required per-component notes. |
| R-03 | improper merge | `engineering-methodology-and-process`, `collaborative-posture-and-ethics`, `verification-methodology`, `code-audit-discipline`, `coverage-hardening-discipline`, `delegation-policy` | Methodology narrates posture, substrate, SDLC, verification, audit, coverage, and delegation as one coherent story. | Confirmed risk. The merge may preserve monolithic load cost. | Slice03 should distinguish owned methodology rules from routed specialized components. |
| R-04 | improper merge | `path-contract-constraints`, `repository-orientation-and-distribution`, `protocol-distribution-guidance` | Project01 path/package rules are gates, while README/protocol guidance are reader adapters. | Confirmed risk. Treating all distribution material as one component would mix user-facing guidance with release gates. | Slice03 should keep path-contract constraints as component-contract gates. |
| R-05 | improper split | `ledger-verification-protocol`, `slice-close-and-bubble-up`, `arc-project-composition-close` | PM close docs own lifecycle and bubble-up; ledger owns evidence strength and row closure. | Confirmed risk. Splitting without explicit dependency direction would duplicate or drift close semantics. | Slice03 should state dependency direction: PM close uses ledger discipline. |
| R-06 | improper split | `contribution-style-and-voice`, `contribution-ticket-template` | Style guide supplies judgment and voice; template supplies concrete shape and repeats calibrated-honesty cautions. | Confirmed risk. Either artifact alone is weaker than the pair. | Slice03 should propose one contribution-guidance component with the ticket template as support asset. |
| R-07 | missing concept | component-maintenance contract spanning all accepted components | Current maintenance guidance covers PM/process docs but not a post-breakout multi-component coherence contract. | Confirmed missing concept candidate, not a final component. | Slice03 should add an operator decision about component maintenance owner and Arc04 contract fields. |
| R-08 | missing concept | abstraction-boundary or ontology-critique discipline | Arc01 PSF-03 says abstraction/generalization failure is named more strongly than mechanized. | Confirmed missing-solution area. | Slice03 should decide whether Arc02 needs a reusable boundary-review checklist or only this project-specific analysis. |
| R-09 | overclaimed mechanism | `collaborative-posture-and-ethics`, `engineering-methodology-and-process` | Source names structural pulls and SDLC gates, but enforcement depends on the active model actually loading and honoring them. | Confirmed caveat. Strong conceptual fit, weaker enforcement mechanism. | Slice03 should preserve evidence-grade language and avoid implying posture/process mechanically guarantees behavior. |
| R-10 | overclaimed mechanism | `project-management-scale-model` | Source gives context-sizing judgment and iteration budget but no mechanical context-budget gate. | Confirmed caveat. Good discipline, not an automated sizing proof. | Arc03 should test actual load/use patterns; Arc04 should avoid claiming automatic sizing enforcement. |
| R-11 | underfit | `coverage-hardening-discipline` | Coverage guide requires 95%+ and quality gates but has language/tool-specific examples. | Confirmed underfit for a general framework component. | Slice03 should require language-neutral contract language plus repository-specific command adaptation. |
| R-12 | underfit | `path-contract-constraints` across every future component | Project01 gates are known, but per-component package contracts do not exist yet. | Confirmed underfit by project design. | Arc04/Arc05 must add component contract fields for package behavior and validation gates. |
| R-13 | overfit | `planning-confirmation-protocol` | It has a clear narrow load moment, but is mostly useful as part of PM layout safety. | Possible risk. It may be overfit as a standalone component. | Slice03 should classify it as PM guide/support unless Arc03 finds direct standalone use. |
| R-14 | overfit | `project-management-examples`, `project-management-provenance` | Examples and version history support PM but do not own independent problem classes. | Confirmed risk if elevated to primary components. | Keep them as PM support assets unless operator chooses a separate example/provenance packaging policy. |
| R-15 | overlap | `ledger-verification-protocol`, `verification-methodology`, `code-audit-discipline`, `slice-close-and-bubble-up` | Silent drops, spec-softening, partial adoption, and evidence strength recur across ledger, methodology, PM, and audit. | Confirmed overlap; likely partly deliberate reinforcement. | Slice03 should mark one owner for each general rule and note where other components specialize or cite it. |
| R-16 | overlap | `repository-orientation-and-distribution`, `framework-entrypoint-and-routing`, `agent-adapter-and-routing` | README, SKILL, and adapter notes all route users/agents into framework content. | Confirmed overlap. It is useful but can drift if split inconsistently. | Slice03 should define the composer/adapter relationship before Arc04 architecture. |
| R-17 | duplication | PM examples/provenance versus PM rules | Version history and worked examples repeat rule rationale already present in PM guides. | No harmful duplication confirmed if kept as support assets. | Slice03 should avoid making them separately maintained components. |
| R-18 | duplication | contribution style versus ticket template | The template repeats calibrated-honesty guidance from style guide. | Acceptable duplication when packaged together; risky if separated. | Keep the template dependent on the style guide. |
| R-19 | mislabel | `verification-methodology` | No current file exclusively owns this label; it is a shared concept across methodology and ledger. | Confirmed label risk. It may be a non-component concept, not a component. | Slice03 should preserve it as ontology/dependency edge unless a direct load moment is proved. |
| R-20 | improper split | project-management family members | The soft layout hypothesis splits PM into many guides; evidence supports a family but not necessarily separate components. | Confirmed caution. The layout is plausible as guides under one component, not accepted package architecture. | Slice03 should synthesize PM as a likely component family and defer package granularity to Arc04. |

## Category Coverage

- mislabel: confirmed for coverage, agent adapter, and verification-methodology.
- improper merge: confirmed for methodology/process and distribution/gate
  material.
- improper split: confirmed for ledger/PM close, contribution guide/template,
  and PM family granularity.
- missing concept: confirmed candidates for component-maintenance contract and
  abstraction/ontology critique.
- overclaimed mechanism: confirmed caveats for posture/process enforcement and
  context sizing.
- underfit: confirmed for general coverage component language and future
  per-component package contracts.
- overfit: confirmed or possible for confirmation protocol, examples, and
  provenance as standalone components.
- overlap: confirmed among entrypoint adapters and among evidence/close/audit
  concepts.
- duplication: acceptable only where an owner/dependency is explicit; risky for
  PM support material and contribution style/template if split.

## Follow-Up Summary

Slice03 should synthesize these risks into a non-final ontology, naming
critique, and operator decision set. No risk requires changing Arc02 Slice03's
planned scope: the existing Slice03 scope already includes ontology synthesis,
naming critique, merge/split findings, missing/overclaimed concept findings,
and an operator decision register for Arc04.
