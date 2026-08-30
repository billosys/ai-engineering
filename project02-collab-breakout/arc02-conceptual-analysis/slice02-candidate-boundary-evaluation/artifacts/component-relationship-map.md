# Component Relationship Map

```yaml
project: project02-collab-breakout
arc: arc02-conceptual-analysis
slice: slice02-candidate-boundary-evaluation
status: proposed-done
architecture-decisions: none
```

## Scope

This relationship map applies the Slice01 conceptual-analysis method and
component-boundary ledger to the 26 evaluated labels. It uses the Slice01
relationship vocabulary: prerequisite, extends, uses, supports, constrains,
contrasts-with, composes-into, and routes-to.

The map is analytical and non-final. It tests the soft layout hypothesis as a
low-weight hypothesis, not accepted architecture. Evidence outranks the sketch;
Arc03 functional analysis, Arc04 architecture work, and operator acceptance
remain required.

## Likely Component Families

Component family: top-level collaboration-framework composer

- Primary adapter: `framework-entrypoint-and-routing`.
- Supporting adapters and gates: `repository-orientation-and-distribution`,
  `agent-adapter-and-routing`, `protocol-distribution-guidance`, and
  `path-contract-constraints`.
- Soft layout hypothesis: `knowledge/collaboration-framework/` is supported as
  a composer location, provided it remains thin and routes to accepted
  components rather than absorbing their full content.

Component family: project management

- Entrypoint adapter: `project-management-wayfinder`.
- Core family members: `project-management-scale-model`,
  `planning-worktree-and-layout`, `planning-open-set-mechanics`,
  `slice-close-and-bubble-up`, `arc-project-composition-close`, and
  `planning-confirmation-protocol`.
- Support assets: `planning-anti-patterns-and-repair`,
  `project-management-examples`, and `project-management-provenance`.
- Soft layout hypothesis: `knowledge/project-management/` is supported as a
  likely family, but individual guides are not all standalone components.

Component family: ledger discipline

- Strong standalone candidate: `ledger-verification-protocol`.
- Shared ontology/dependency edge: `verification-methodology`.
- Dependent PM edges: `slice-close-and-bubble-up` and
  `arc-project-composition-close` use ledger evidence semantics while PM owns
  lifecycle routing.
- Soft layout hypothesis: `knowledge/ledger-discipline/` is supported, with
  the caution that row-closure evidence semantics must not drift from PM close
  guidance.

Component family: specialized operational guides

- Standalone candidates: `code-audit-discipline`,
  `coverage-hardening-discipline`, `delegation-policy`, and
  `contribution-style-and-voice`.
- Support assets: `evidence-backed-modernization` under code audit and
  `contribution-ticket-template` under contribution guidance.
- Unresolved relationship: whether code audit and coverage should be sibling
  components or both members of a broader quality-floor family.

## Typed Edges

| Source label | Relationship | Target label | Basis | Slice03 question |
|--------------|--------------|--------------|-------|------------------|
| collaborative-posture-and-ethics | prerequisite | engineering-methodology-and-process | Methodology depends on peer frame and anti-sycophancy posture for its process controls to remain more than ritual. | Is posture both standalone and a mandatory methodology dependency? |
| engineering-methodology-and-process | routes-to | project-management-wayfinder | `SKILL.md` and methodology point detailed planning mechanics to PM. | How thin should the methodology component be after routing? |
| engineering-methodology-and-process | routes-to | ledger-verification-protocol | Methodology names verification/ledger discipline but ledger owns row closure. | Which evidence terms remain in methodology versus ledger? |
| engineering-methodology-and-process | routes-to | code-audit-discipline | Methodology introduces CAP-style audits; code audit owns execution details. | Is audit a sibling component or methodology subcomponent? |
| engineering-methodology-and-process | routes-to | coverage-hardening-discipline | Methodology names quality-floor practice; coverage owns the hard threshold workflow. | Should coverage sit in a quality family? |
| engineering-methodology-and-process | routes-to | delegation-policy | Methodology names subagent hazards; delegation guide owns the rule. | Is delegation standalone or execution governance? |
| framework-entrypoint-and-routing | routes-to | collaborative-posture-and-ethics | Top-level skill loads posture as foundational character layer. | What posture summary remains in composer? |
| framework-entrypoint-and-routing | routes-to | engineering-methodology-and-process | Top-level skill loads craft/process layer. | What is the default bundle? |
| framework-entrypoint-and-routing | routes-to | project-management-wayfinder | Planning and closing require PM wayfinder first. | Must composer make PM loading mandatory? |
| framework-entrypoint-and-routing | routes-to | ledger-verification-protocol | Ledgered units require ledger discipline at start. | Does composer route to ledger directly or through PM? |
| repository-orientation-and-distribution | routes-to | framework-entrypoint-and-routing | README leads humans to the runtime skill entrypoint. | Does README list every component or only the composer? |
| repository-orientation-and-distribution | contrasts-with | protocol-distribution-guidance | Skill zips and CCDP package roots are separate release surfaces. | Where should CCDP contrast live after breakout? |
| protocol-distribution-guidance | constrains | path-contract-constraints | CCDP remains a protocol package, not an installable skill package. | How are protocol-package checks kept outside skill package contracts? |
| agent-adapter-and-routing | supports | framework-entrypoint-and-routing | Surface-neutral interpretation makes the top-level adapter portable. | Central adapter or repeated local notes? |
| agent-adapter-and-routing | constrains | all future standalone components | Standalone components must still explain CC/CDC/Codex/Claude terminology where needed. | What minimum adapter note belongs in each component? |
| project-management-wayfinder | routes-to | project-management-scale-model | PM starts by choosing the correct scale vocabulary. | Should the PM SKILL load scale model first? |
| project-management-wayfinder | routes-to | planning-worktree-and-layout | PM must find/create canonical planning paths before work. | Is layout always required or only for path work? |
| project-management-wayfinder | routes-to | planning-open-set-mechanics | Opening work uses the top-down planning file. | How does PM avoid overloading the wayfinder? |
| project-management-wayfinder | routes-to | slice-close-and-bubble-up | Closing a slice uses the close file and ledger discipline. | Should close routing be separate from open routing? |
| project-management-wayfinder | routes-to | arc-project-composition-close | Closing arcs/projects uses parent-scale composition rules. | How much parent close belongs in the PM entrypoint? |
| project-management-scale-model | prerequisite | planning-open-set-mechanics | Plans depend on distinguishing project, arc, slice, step, and iteration. | Does Slice03 group all PM core mechanics together? |
| planning-worktree-and-layout | prerequisite | planning-open-set-mechanics | Open sets need canonical file paths and artifact homes. | Does layout become a PM core guide? |
| planning-open-set-mechanics | prerequisite | slice-close-and-bubble-up | Close validates the scope opened by the slice plan and ledger. | Can open and close mechanics be separate guides without drift? |
| slice-close-and-bubble-up | uses | ledger-verification-protocol | Slice close walks ledger rows and evidence. | PM owns lifecycle, ledger owns evidence semantics? |
| arc-project-composition-close | uses | ledger-verification-protocol | Arc/project close use parent-scale ledger composition. | Should parent close be a PM guide or ledger guide? |
| planning-confirmation-protocol | supports | planning-worktree-and-layout | Confirmation protects ambiguous layout choices. | Standalone narrow component or PM support guide? |
| planning-anti-patterns-and-repair | supports | planning-worktree-and-layout | Anti-patterns help refuse wrong planning paths and misplaced artifacts. | Keep as corrective support? |
| project-management-examples | supports | project-management-wayfinder | Examples demonstrate how PM mechanics compose in a real run. | How much example material belongs in packaged component? |
| project-management-provenance | supports | framework-maintenance-discipline | Version history preserves why PM rules changed. | Does maintenance own provenance or PM own it? |
| framework-maintenance-discipline | constrains | all future standalone components | Split components need synchronized routing, version histories, and package checks. | Is a component-maintenance contract missing? |
| ledger-verification-protocol | supports | code-audit-discipline | Audits use evidence-grade thinking and independent verification language. | Does audit cite ledger or duplicate evidence rules? |
| code-audit-discipline | supports | evidence-backed-modernization | Modernization follows audit findings, not fashion. | Keep modernization as audit subsection? |
| evidence-backed-modernization | extends | code-audit-discipline | It specializes audit findings into modernization pressure. | Does it ever have a direct load moment? |
| coverage-hardening-discipline | extends | engineering-methodology-and-process | Coverage is a specialized quality-floor loop. | Is it a standalone component after naming cleanup? |
| coverage-hardening-discipline | contrasts-with | code-audit-discipline | Coverage changes tests; audit diagnoses without editing source. | Sibling components or one code-quality family? |
| delegation-policy | supports | engineering-methodology-and-process | Delegation guardrails instantiate methodology's subagent hazard line. | Standalone operational policy? |
| contribution-style-and-voice | uses | contribution-ticket-template | The guide supplies judgment and voice; the template supplies shape. | One contribution component with template asset? |
| contribution-ticket-template | supports | contribution-style-and-voice | Template operationalizes the style guide. | Can templates stand alone? Current evidence says no. |
| path-contract-constraints | constrains | all future standalone components | Project01 source/package gates apply to every component package. | Which gates are central versus repeated per component? |

## Grouping Findings

- Candidate components with strong reason to load: `collaborative-posture-and-ethics`,
  `engineering-methodology-and-process`, `ledger-verification-protocol`,
  `code-audit-discipline`, `coverage-hardening-discipline`,
  `delegation-policy`, and `contribution-style-and-voice`.
- Component family members rather than standalone top-level components:
  `project-management-scale-model`, `planning-worktree-and-layout`,
  `planning-open-set-mechanics`, `slice-close-and-bubble-up`,
  `arc-project-composition-close`, and `planning-confirmation-protocol`.
- Support assets: `protocol-distribution-guidance`,
  `planning-anti-patterns-and-repair`, `project-management-examples`,
  `project-management-provenance`, `evidence-backed-modernization`, and
  `contribution-ticket-template`.
- Adapters: `repository-orientation-and-distribution`,
  `framework-entrypoint-and-routing`, `agent-adapter-and-routing`, and
  `project-management-wayfinder`.
- Constraints and package/release gates: `path-contract-constraints`,
  `protocol-distribution-guidance`, `repository-orientation-and-distribution`,
  `planning-worktree-and-layout`, and `framework-maintenance-discipline`.

## Unresolved Relationship Questions

- Does `verification-methodology` become its own guide, or stay as shared
  ontology in methodology plus ledger discipline?
- Does project management ship as one component with guides, or as a PM
  wayfinder plus separately loadable family members?
- Do code audit and coverage hardening remain sibling operational components,
  or compose into a larger quality-floor family?
- Does `agent-adapter-and-routing` live centrally in the top-level composer, or
  as a short required note in each standalone component?
- Which Project01 package/release gates are centralized in the composer, which
  are repeated in each component contract, and which are enforced only by
  future implementation checks?
