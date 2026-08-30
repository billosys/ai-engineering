# Mechanism Coverage Matrix

```yaml
project: project02-collab-breakout
arc: arc01-framework-inventory
slice: slice02-problem-solution-map
status: proposed-done
labels: non-final, from verified Slice01 inventory
```

## Legend

- Primary coverage: the candidate label is one of the main mechanisms for the
  problem class.
- Secondary coverage: the candidate label supports or routes to a main
  mechanism.
- Gap/risk: useful caveat for Slice 03 and Arc 02.

## Matrix

| Candidate label | Primary coverage | Secondary coverage | Source evidence | Gap/risk for later analysis |
|-----------------|------------------|--------------------|-----------------|-----------------------------|
| `repository-orientation-and-distribution` | Tooling entrypoint, source/package vocabulary, release surface guidance | Domain knowledge discovery, package path constraints, component discovery | Slice01 inventory `README.md` entry; `README.md:242-288` | Strong source-reader mechanism, but may become overloaded if it must also explain every future component. |
| `protocol-distribution-guidance` | CCDP package/source distinction | General package semantics and release surface examples | Slice01 concept map `README.md` CCDP row; `README.md:330-349` | Relevant to Project02 mainly as a contrast case; avoid improper merge with skill package guidance. |
| `framework-entrypoint-and-routing` | Runtime load routing, top-level composition, monolithic load-cost mitigation | Posture, PM, ledger, audit, coverage, delegation, contribution guide discovery | Slice01 inventory `SKILL.md` entry; `SKILL.md:320-332` | Strong router, but not itself the final component architecture. |
| `agent-adapter-and-routing` | Surface translation for Codex/Claude terms, human/LLM role clarity | Sycophancy/deference counterpressure and delegation boundaries | Slice01 concept map `SKILL.md` notes row; `SKILL.md:74-86` | Possible mislabel candidate if adapter logic remains buried in the top-level skill. |
| `collaborative-posture-and-ethics` | Sycophancy, deference, peer-frame failures, calibrated uncertainty | Generalization risk, human/LLM authority clarity | Slice01 inventory Constitution entry; `README.md:60`, `README.md:116-118` | Strong conceptual component candidate; enforcement depends on load behavior. |
| `engineering-methodology-and-process` | Domain knowledge substrate, 9-point SDLC, drift detection, abstraction risk | Code audit, coverage, ledger, subagent policy | Slice01 inventory methodology entry; `docs/AI-ENGINEERING-METHODOLOGY.md:90-108` | Possible improper merge of substrate, process, verification, and audit concepts. |
| `verification-methodology` | Evidence claims, reviewer/doer separation, audit mindset | Ledger, code audit, contribution calibration | Slice01 concept map methodology verification row; `templates/LEDGER-DISCIPLINE.md:118-136` | Boundary with ledger protocol is unclear. |
| `project-management-wayfinder` | Planning entrypoint, required load routing, artifact home discipline | Scale model, planning worktree, close/bubble-up | Slice01 inventory PM wayfinder entry; `docs/PROJECT-MANAGEMENT.md:35-53` | Router may stay separate from detailed PM component or be folded into it. |
| `project-management-scale-model` | Context sizing, project/arc/slice/step/iteration vocabulary | Ledger cadence, slice scoping, plan-late/plan-deep | Slice01 inventory `docs/pm/01` entry; `docs/pm/01-scales-of-work.md:32-38` | Strong fit, but may be inseparable from planning mechanics in actual use. |
| `planning-worktree-and-layout` | Path confusion, artifact orphaning, planning/source separation | Package/release-source distinction | Slice01 inventory `docs/pm/02` entry; `docs/pm/02-canonical-planning-worktree.md:3-27` | Strong path mechanism; must stay aligned with Project01 path contract. |
| `planning-open-set-mechanics` | Up-front scope and ledger creation, anti-deferral setup | Context sizing, plan-late/plan-deep | Slice01 inventory `docs/pm/03` entry; `docs/pm/03-planning-top-down.md:75-84` | Good component candidate only if close mechanics remain a clear dependency. |
| `slice-close-and-bubble-up` | Silent drop detection, deferral disclosure, arc feedback | Artifact inventory, plan-change trigger | Slice01 inventory `docs/pm/04` entry; `docs/pm/04-closing-slices.md:17-33` | Tight coupling to ledger protocol may make separate packaging awkward. |
| `arc-project-composition-close` | Higher-scale recomposition, inherited-composition prevention | Plan-change discipline, remediation routing | Slice01 inventory `docs/pm/05` entry; `docs/pm/05-closing-arcs.md:1-31` | Could be part of PM close component rather than its own component. |
| `planning-confirmation-protocol` | Wrong-path prevention, operator confirmation before new layout | Artifact-home confirmation, local instruction capture | Slice01 inventory `docs/pm/06` entry; `docs/pm/06-confirmation-protocol.md:17-19` | Narrow and self-contained; decide whether standalone use is worth package cost. |
| `planning-anti-patterns-and-repair` | Planning-path anti-patterns, artifact scattering, stale layout refusal | Maintenance and confirmation protocol | Slice01 inventory `docs/pm/07` entry; `docs/pm/07-anti-patterns.md:11-14` | Corrective guide depends on canonical layout; improper split risk if separated. |
| `framework-maintenance-discipline` | Process-doc drift, version-history synchronization | Package path and routing consistency | Slice01 inventory `docs/pm/08` entry; `docs/pm/08-maintenance.md:1-24` | Underfit for post-breakout component ownership; needs clearer component maintenance contract. |
| `project-management-examples` | Onboarding and concrete planning flow | PM scale/open/close mechanics | Slice01 inventory `docs/pm/09` entry | Useful support, not likely a primary standalone component. |
| `project-management-provenance` | PM rule history and compatibility rationale | Planning worktree transition, artifact home history | Slice01 inventory `docs/pm/version-history` entry; PM version history v2.5 lines | Provenance should follow the PM component; not a user-facing primary mechanism. |
| `ledger-verification-protocol` | Silent drop, arbitrary deferral, spec-softening, partial adoption, evidence ladder | Artifact placement, close reports, CDC verification | Slice01 inventory ledger entry; `templates/LEDGER-DISCIPLINE.md:103-136` | Strong standalone candidate; dependency direction with PM close docs must be explicit. |
| `code-audit-discipline` | Drift, duplication, orphan code, modernization pressure, quality floor | Spec-softening, partial adoption, language-skill routing | Slice01 inventory code audit entry; `docs/CODE-AUDIT.md:8-13`, `docs/CODE-AUDIT.md:278-299` | `workbench/<DATE>-audit-*` convention conflicts with ledgered artifact-home default unless scoped. |
| `evidence-backed-modernization` | Evidence-first modernization, consolidation opportunities | Code audit findings, drift and duplicated abstractions | Slice01 concept map code-audit modernization row; `docs/CODE-AUDIT.md:242-261` | Likely subcomponent of code audit, not a separate package by itself. |
| `coverage-hardening-discipline` | Coverage floor, weak tests, untested error paths, root-cause test repair | Verification methodology and code audit | Slice01 inventory coverage entry; `docs/CLAUDE-CODE-COVERAGE.md:352-375` | Overfit risk: current examples are cargo/Rust-heavy even though the discipline is general. |
| `delegation-policy` | Subagent judgment leakage, context loss, skill loss, integration friction | Human/LLM role clarity, workflow routing | Slice01 inventory delegation entry; `docs/SUBAGENT-DELEGATION-POLICY.md:13-36` | Strong narrow operational component; verify whether it needs a template/quick-reference entrypoint. |
| `contribution-style-and-voice` | Upstream contribution noise, overclaiming, maintainer burden | Evidence calibration and ticket sizing | Slice01 inventory contribution-style entry; `docs/CONTRIBUTION-STYLE.md:18-21`, `docs/CONTRIBUTION-STYLE.md:81-90` | Strong with the ticket template; weak as an isolated package. |
| `contribution-ticket-template` | Ticket body structure, confirmed/unconfirmed issue shapes | Contribution style, evidence blocks, maintainer workflow | Slice01 inventory ticket-template entry; `templates/CONTRIBUTION-TICKET.md:133-155` | Possible improper split if separated from style guide. |
| `path-contract-constraints` | Project01 source/package, package-local links, zip roots, release surface checks | Planning artifact placement and future component packaging | Slice01 path-contract notes; `README.md:242-288`, `README.md:342-349` | Cross-cutting constraint, not a user-facing component. Must gate any future breakout plan. |

## Problem Class Coverage Summary

| Problem class | Primary candidate labels | Secondary candidate labels | Coverage assessment |
|---------------|--------------------------|----------------------------|---------------------|
| domain knowledge evaporation | `engineering-methodology-and-process` | `repository-orientation-and-distribution`, `framework-entrypoint-and-routing` | Strong substrate concept, partial standalone packaging. |
| tooling and entrypoint confusion | `repository-orientation-and-distribution`, `framework-entrypoint-and-routing` | `path-contract-constraints` | Strong for current monolith, partial for future components. |
| drift, duplication, orphan work | `engineering-methodology-and-process`, `code-audit-discipline` | `framework-maintenance-discipline`, `evidence-backed-modernization` | Strong detection, ownership overlap. |
| context-window overrun | `project-management-scale-model` | `planning-open-set-mechanics`, `ledger-verification-protocol` | Strong discipline, no automated context gate. |
| generalization and abstraction failure | `collaborative-posture-and-ethics`, `engineering-methodology-and-process` | `verification-methodology`, `code-audit-discipline` | Partial; needs explicit abstraction-decision analysis. |
| silent drop and arbitrary deferral | `ledger-verification-protocol` | `slice-close-and-bubble-up`, `verification-methodology` | Strongest current fit. |
| spec-softening and partial adoption | `ledger-verification-protocol`, `code-audit-discipline` | `engineering-methodology-and-process` | Strong but duplicated across guides. |
| sycophancy and deference | `collaborative-posture-and-ethics` | `agent-adapter-and-routing`, `framework-entrypoint-and-routing` | Strong posture, load-dependent enforcement. |
| human/LLM role confusion | `verification-methodology`, `ledger-verification-protocol`, `agent-adapter-and-routing` | `delegation-policy` | Strong but naming remains surface-specific. |
| path and artifact orphaning | `planning-worktree-and-layout`, `planning-confirmation-protocol` | `planning-anti-patterns-and-repair`, `path-contract-constraints` | Strong after Project01. |
| package and release surface confusion | `path-contract-constraints`, `repository-orientation-and-distribution` | `protocol-distribution-guidance` | Strong current contract, missing future per-component contracts. |
| quality-floor drift | `code-audit-discipline`, `coverage-hardening-discipline` | `verification-methodology`, `evidence-backed-modernization` | Strong code-quality support, component placement unresolved. |
| subagent judgment leakage | `delegation-policy` | `agent-adapter-and-routing` | Strong narrow fit. |
| upstream contribution noise | `contribution-style-and-voice`, `contribution-ticket-template` | `verification-methodology` | Strong paired mechanism; possible improper split if separated. |
| framework maintenance drift | `framework-maintenance-discipline`, `project-management-provenance` | `framework-entrypoint-and-routing`, `path-contract-constraints` | Partial; post-breakout maintenance contract missing. |
| monolithic load cost | `framework-entrypoint-and-routing` | all operational labels | Missing solution; Project02 exists to resolve it. |

## Open Questions

- Slice 03: Which candidate labels should survive as component candidates, and
  which should become dependencies, examples, or cross-cutting constraints?
- Slice 03: Which primary/secondary pairings show deliberate reinforcement
  rather than accidental duplication?
- Arc 02 operator discussion: Should `path-contract-constraints` remain a
  cross-cutting acceptance gate rather than become a packaged component?
- Arc 02 decision needed: Should Claude/Codex adapter wording be centralized in
  one agent-adapter component or remain embedded in every operational guide?
