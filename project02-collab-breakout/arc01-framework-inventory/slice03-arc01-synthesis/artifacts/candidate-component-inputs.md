# Candidate Component Inputs

```yaml
project: project02-collab-breakout
arc: arc01-framework-inventory
slice: slice03-arc01-synthesis
status: proposed-done
architecture-decisions: none
labels: non-final
```

## Evidence Basis

Slice 01 is verified-closed with `Rows: 7` and `Done: 7`. Slice 02 is
verified-closed with `Rows: 8` and `Done: 8`. This file classifies the Slice 01
and Slice 02 candidate labels for Arc 02 analysis. It does not select final
component boundaries.

## Classification Legend

- candidate component: a plausible standalone or composed component for Arc 02
  analysis.
- support asset: examples, templates, provenance, or secondary guidance that
  should likely travel with another component.
- dependency edge: a relation Arc 02 must preserve between candidate
  components.
- adapter: an entrypoint, agent-surface translation, or reader-facing router.
- constraint: a rule that governs component contracts but is not itself a
  user-facing component.
- package/release gate: a source/package validation or release-surface check
  that any future component plan must satisfy.

## Label Classification Matrix

| Candidate label | Classification for Arc 02 | Evidence basis | Arc 02 use |
|-----------------|---------------------------|----------------|------------|
| `repository-orientation-and-distribution` | adapter; package/release gate | Slice01 inventory `README.md`; Slice02 PSM-02 and PSM-11 | Decide how README-oriented source discovery and component discovery remain coherent after breakout. |
| `protocol-distribution-guidance` | support asset; constraint | Slice01 concept map CCDP row; Slice02 matrix | Keep CCDP as a contrast case for package boundaries; avoid improper merge with skill components. |
| `framework-entrypoint-and-routing` | adapter; candidate component as top-level composer | Slice01 `SKILL.md` entry; Slice02 PSM-02 and PSM-16 | Decide whether the top-level collaboration-framework remains a composition router over smaller components. |
| `agent-adapter-and-routing` | adapter; possible dependency edge | Slice01 concept map `SKILL.md` notes row; Slice02 PSM-09 | Decide whether Codex/Claude surface translation is centralized or repeated in each guide. |
| `collaborative-posture-and-ethics` | candidate component | Slice01 Constitution entry; Slice02 PSM-08; PSF-02 | Evaluate as a standalone posture component and as a dependency of methodology/process work. |
| `engineering-methodology-and-process` | candidate component; improper merge risk | Slice01 methodology entry; Slice02 PSM-01, PSM-03, PSM-05 | Test whether substrate, SDLC/process, verification, audit, and coverage are one component or several. |
| `verification-methodology` | dependency edge; possible candidate component | Slice01 concept map methodology verification row; Slice02 PSM-07 and PSM-09 | Decide whether evidence-strength and reviewer/doer separation are owned by methodology, ledger, or a shared verification layer. |
| `project-management-wayfinder` | adapter for project-management component | Slice01 PM wayfinder entry; Slice02 PSM-10 | Preserve required PM routing without making the wayfinder a standalone ontology by itself. |
| `project-management-scale-model` | candidate component inside PM family | Slice01 `docs/pm/01` entry; Slice02 PSM-04 | Evaluate whether project/arc/slice vocabulary is inseparable from PM mechanics. |
| `planning-worktree-and-layout` | candidate component inside PM family; constraint | Slice01 `docs/pm/02` entry; Slice02 PSM-10 | Preserve planning/source separation, canonical filenames, and artifact home rules. |
| `planning-open-set-mechanics` | candidate component inside PM family | Slice01 `docs/pm/03` entry; Slice02 PSM-04 and PSM-10 | Keep open-set planning dependent on ledger rows and close mechanics. |
| `slice-close-and-bubble-up` | candidate component inside PM family; dependency edge to ledger | Slice01 `docs/pm/04` entry; PSF-01 | Decide whether PM owns lifecycle close while ledger owns evidence semantics. |
| `arc-project-composition-close` | candidate component inside PM family; dependency edge to ledger | Slice01 `docs/pm/05` entry; Slice02 matrix | Preserve recomposition and remediation-not-iteration at parent scales. |
| `planning-confirmation-protocol` | support asset; possible narrow candidate component | Slice01 `docs/pm/06` entry; Slice02 PSM-10 | Decide whether wrong-path prevention is standalone enough or part of PM layout. |
| `planning-anti-patterns-and-repair` | support asset for PM component | Slice01 `docs/pm/07` entry; PSF-09 | Keep corrective guidance near the PM rules it enforces. |
| `framework-maintenance-discipline` | constraint; support asset | Slice01 `docs/pm/08` entry; PSM-15 | Turn into a component-maintenance contract if Arc 02 accepts multiple components. |
| `project-management-examples` | support asset | Slice01 `docs/pm/09` entry; PSF-09 | Keep examples with the PM component unless Arc 02 defines a separate examples package policy. |
| `project-management-provenance` | support asset | Slice01 `docs/pm/version-history` entry; PSF-09 | Preserve history with the owning PM component rather than treating provenance as user-facing. |
| `ledger-verification-protocol` | candidate component; dependency edge to PM close | Slice01 ledger entry; Slice02 PSM-06, PSM-07; PSF-01 | Strong standalone candidate, but must specify PM close dependency direction. |
| `code-audit-discipline` | candidate component | Slice01 code audit entry; Slice02 PSM-12; PSF-05 | Analyze as a standalone audit discipline with a scoped output-location rule. |
| `evidence-backed-modernization` | support asset or dependency edge under code audit | Slice01 concept map audit-modernization row; Slice02 PSM-03 and matrix | Likely travels under audit rather than as a separate component. |
| `coverage-hardening-discipline` | candidate component; mislabel risk | Slice01 coverage entry; Slice02 PSM-12; PSF-04 | Decide whether the coverage guide needs renaming or language-neutral extraction. |
| `delegation-policy` | candidate component | Slice01 delegation entry; Slice02 PSM-13; PSF-08 | Low-risk standalone operational component candidate with a top-level summary dependency. |
| `contribution-style-and-voice` | candidate component paired with support asset | Slice01 contribution style entry; Slice02 PSM-14; PSF-07 | Analyze as a guide paired with the ticket template, not necessarily separate packages. |
| `contribution-ticket-template` | support asset for contribution component | Slice01 ticket template entry; Slice02 PSM-14; PSF-07 | Decide whether templates can stand alone or only travel with their guide. |
| `path-contract-constraints` | constraint; package/release gate; not a component | Slice01 path-contract notes; Slice02 PSM-11; PSF-06 | Attach as acceptance gates to every future component contract. |

## Candidate Components

These labels look like viable candidate component inputs for Arc 02:

- `collaborative-posture-and-ethics`: strong problem ownership around
  sycophancy, deference, peer frame, structural pulls, and calibrated
  uncertainty.
- `engineering-methodology-and-process`: strong process/substrate ownership,
  but Arc 02 must test whether it improperly merges substrate, SDLC,
  verification, audit, and coverage.
- `project-management-*`: likely a component family rather than nine standalone
  components. Arc 02 should evaluate one PM component with internal sections
  against a split into load-specific subcomponents.
- `ledger-verification-protocol`: strong standalone candidate because it owns
  evidence strength, per-row closure, verifier separation, and silent-drop
  prevention.
- `code-audit-discipline`: distinct load moment and problem class around
  evidence-based diagnosis and modernization.
- `coverage-hardening-discipline`: distinct load moment around coverage and
  test-quality pressure, with naming and generality risks.
- `delegation-policy`: narrow, self-contained operational policy.
- `contribution-style-and-voice`: likely one component with
  `contribution-ticket-template` as a support asset.

## Support Assets

Support assets that should likely travel with an owning component:

- `protocol-distribution-guidance`: useful as package-boundary contrast, not a
  collaboration-framework component on its own.
- `planning-anti-patterns-and-repair`: useful corrective support for PM.
- `project-management-examples`: useful onboarding support for PM.
- `project-management-provenance`: history that should remain near PM, not a
  primary user-facing component.
- `evidence-backed-modernization`: likely part of code audit rather than a
  standalone package.
- `contribution-ticket-template`: a concrete asset for the contribution guide.

## Dependency Edges

Dependency edge inputs for Arc 02:

- Posture -> methodology: methodology depends on posture for the peer frame and
  anti-sycophancy basis.
- Methodology -> project management, ledger, audit, coverage, delegation:
  methodology routes the disciplines but does not necessarily own every detail.
- Project management close -> ledger verification: PM owns lifecycle and
  bubble-up routing; ledger owns evidence semantics and row closure.
- Code audit -> language/domain skills: audit execution depends on the relevant
  domain skills while keeping audit judgment in the main context.
- Coverage hardening -> repository tooling and domain test idioms: the guide
  needs repository-specific command adaptation.
- Contribution ticket template -> contribution style: the template depends on
  the style guide to prevent formulaic or overclaimed reports.
- Framework entrypoint -> every extracted component: the top-level skill must
  remain a thin composer or adapter over accepted components.
- Every component -> Project01 path contract: component contracts must preserve
  package-local links, zip roots, reader guidance, and source/package terms.

## Surface Adapters

Adapters are not automatically components. They mediate reader or agent entry:

- `README.md` is the source-clone and release-surface adapter.
- `SKILL.md` is the runtime loading and composition adapter.
- `agent-adapter-and-routing` maps Claude/CDC/CC language into Codex and future
  surface-neutral language.
- Package guidance adapts the source tree to generated zips and unzipped skill
  installs.

Arc 02 should decide whether each adapter is owned by the top-level composer,
by a component, or by release tooling.

## Cross-Cutting Constraints

Cross-cutting constraints from Project01 and Arc 01:

- Source/package vocabulary is a hard constraint: source clone paths, generated
  skill zip roots, unzipped package-local paths, and CCDP package paths must not
  be blurred.
- `path-contract-constraints` is not a component. It is a cross-cutting
  constraint and package/release gate for future component contracts.
- Durable planning analysis belongs under the owning slice's `artifacts/`
  directory unless an operator-recorded override exists.
- Current file boundaries are evidence, not authority.
- Candidate labels remain non-final until Arc 02 selects a conceptual model.
- Component extraction must not regress `make check-package-paths`,
  package-local links, zip roots, package exceptions, or README/SKILL reader
  guidance.
- Source edits remain out of scope for Project02 until the accepted
  implementation plan says otherwise.

## Package/Release Gates

Package/release gate inputs for Arc 02 and later implementation planning:

- Every future package must preserve package-local relative links.
- Every generated skill zip must keep a coherent root name and entrypoint.
- `make check-package-paths` remains the release-surface gate for packaged
  Markdown paths and explicit exceptions.
- `make check-skills` remains required when `SKILL.md` frontmatter or packaged
  skill metadata changes.
- Component README or SKILL routing must distinguish source clone, skill zip,
  unzipped install, and CCDP package workflows.
- CCDP must remain a protocol package contrast case, not be accidentally folded
  into skill-package component rules.

## Boundary Risks

- Mislabel: `CLAUDE-CODE-COVERAGE.md` may carry a general coverage discipline
  behind a surface-specific name.
- Mislabel: `agent-adapter-and-routing` may currently be hidden as a note in
  `SKILL.md`, not named as an owned adapter.
- Improper merge: posture plus methodology may stay merged only because the
  monolith narrates them together.
- Improper merge: Project01 path contract could be mistaken for a component
  instead of a release gate.
- Improper split: ledger evidence semantics and PM close mechanics can drift if
  split without explicit dependency direction.
- Improper split: contribution style and ticket template may be separately weak
  but jointly strong.
- Overlap/duplication: silent drops, deferral, spec-softening, partial adoption,
  and evidence strength are repeated across methodology, ledger, PM close, and
  audit guidance.
- Underfit: abstraction and generalization failure lacks a dedicated
  conceptual-analysis mechanism.
- Missing solution: monolithic load cost remains unresolved until Arc 02 defines
  component contracts.
