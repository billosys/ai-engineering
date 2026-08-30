# Problem-Solution Findings

```yaml
project: project02-collab-breakout
arc: arc01-framework-inventory
slice: slice02-problem-solution-map
status: proposed-done
architecture-decisions: none
candidate-labels: non-final
```

## Summary

The current collaboration framework has strong mechanisms for the failure
modes that motivated it: silent drops, deferral, spec-softening, partial
adoption, sycophancy, deference, context overrun, path confusion, package
confusion, audit weakness, and human/LLM role blur. The main risk for the
breakout is not absence of mechanisms; it is ownership ambiguity after the
monolith is split.

These findings are analytical inputs for Slice 03, Arc 02, and operator
discussion. They do not select final component boundaries.

## Findings

### PSF-01: Ledger and Project Management Deliberately Overlap

- Finding type: overlap; possible duplication if split poorly.
- Problem class: silent drop, deferral, artifact placement, slice close,
  bubble-up, spec-softening.
- Evidence: `templates/LEDGER-DISCIPLINE.md:173-214` covers row evidence,
  artifacts, silent-drop, spec-softening, partial adoption, and artifact
  placement; `docs/pm/04-closing-slices.md:17-45` covers per-row close,
  artifact inventory, and bubble-up checks.
- Fit assessment: strong fit today because PM explains lifecycle mechanics and
  ledger explains verification mechanics.
- Risk: if `ledger-verification-protocol` and PM close files become separate
  components without explicit dependency direction, the same close rules may
  drift.
- Slice 03 question: Does ledger own evidence semantics while PM owns lifecycle
  routing, with each component referencing the other?
- Arc 02 operator discussion: Decide whether this overlap is intentional
  reinforcement or unacceptable duplication.

### PSF-02: Posture and Methodology Are Conceptually Entangled

- Finding type: overlap; improper merge candidate; improper split candidate.
- Problem class: sycophancy, deference, generalization failure, human/LLM role
  confusion.
- Evidence: `docs/AI-CONSTITUTION-SUPPLEMENT.md` defines peer posture and
  structural pulls; `docs/AI-ENGINEERING-METHODOLOGY.md:90-108` combines
  substrate, posture, and process rigour; `SKILL.md:217-226` condenses the
  three pillars into the entrypoint.
- Fit assessment: partial fit for breakout. The combined story is coherent, but
  a user may need posture without the full operational process stack.
- Risk: splitting posture away from methodology may make the process feel
  procedural and lose its anti-sycophancy basis; merging them may preserve
  context load that Project02 is trying to reduce.
- Slice 03 question: Which concepts must travel together for correctness, and
  which only travel together because the monolith currently packages them that
  way?
- Arc 02 decision needed: Whether posture is a standalone component, a required
  dependency of methodology, or both.

### PSF-03: Generalization Failure Is Named More Strongly Than It Is Mechanized

- Finding type: underfit; missing solution.
- Problem class: generalization, abstraction, improper conceptual boundaries.
- Evidence: `README.md:58` names failures of abstract reasoning and proper
  generalizations; `README.md:88` says explicit human presence is required for
  abstraction/generalization work; `docs/AI-ENGINEERING-METHODOLOGY.md:176-186`
  supplies broad SDLC controls.
- Fit assessment: partial fit. The framework has review gates and human
  involvement, but no focused abstraction-decision checklist or ontology
  critique mechanism.
- Risk: Project02 could create components that look tidy while failing to check
  whether the conceptual split itself is valid.
- Slice 03 question: Should the Arc01 synthesis explicitly recommend an Arc02
  abstraction-boundary review artifact?
- Arc 02 operator discussion: Decide whether conceptual analysis needs its own
  reusable discipline beyond general methodology.

### PSF-04: `CLAUDE-CODE-COVERAGE.md` Is a Mislabel Candidate

- Finding type: mislabel candidate; overfit risk.
- Problem class: coverage hardening, quality floor, tool-specific workflow.
- Evidence: `docs/CLAUDE-CODE-COVERAGE.md:13-15` tells Codex to adapt commands
  to the repository, while `docs/CLAUDE-CODE-COVERAGE.md:98-114` and
  `docs/CLAUDE-CODE-COVERAGE.md:366-375` use cargo-oriented examples and
  process loops.
- Fit assessment: strong fit for coverage persistence, but partial/overfit for
  a framework component meant to be source- and language-neutral.
- Risk: the title and examples may make the discipline feel specific to Claude
  Code or Rust even though Slice01 classified it as a general coverage
  hardening discipline.
- Slice 03 question: Should this candidate be renamed or treated as a legacy
  artifact feeding a broader `coverage-hardening-discipline` component?
- Arc 02 operator discussion: Decide whether model-surface names belong in
  component filenames or only in adapter sections.

### PSF-05: Code Audit Owns a `workbench/` Convention That Conflicts With Ledgered Slice Defaults

- Finding type: overlap; path/package underfit; possible improper merge.
- Problem class: path confusion, orphan artifacts, audit output placement,
  release surface.
- Evidence: `docs/CODE-AUDIT.md:136-146` writes audit outputs to
  `workbench/<DATE>-audit-*`; `docs/pm/02-canonical-planning-worktree.md:122-146`
  and `templates/LEDGER-DISCIPLINE.md:173-214` put durable slice artifacts under
  the owning slice's `artifacts/` directory by default; Slice01
  `artifacts/project01-path-contract-notes.md:60-69` carries that Project01
  path contract forward.
- Fit assessment: partial fit. The audit convention may be correct for
  non-ledgered audits, but it is not scoped against ledgered slice work.
- Risk: future audit component packaging could reintroduce root workbench
  outputs as durable planning evidence.
- Slice 03 question: Should the synthesis recommend "audit workbench for
  standalone audits, slice artifacts for ledgered audits" as a compatibility
  rule?
- Arc 02 decision needed: Decide whether code audit owns its output convention
  or inherits artifact placement from project management when used inside a
  slice.

### PSF-06: Project01 Path Contract Is Cross-Cutting, Not a Component

- Finding type: improper merge candidate; missing solution for component
  contracts.
- Problem class: source/package path, package-local links, zip root, release
  surface, package validation.
- Evidence: Slice01 `artifacts/project01-path-contract-notes.md:32-56`
  summarizes the Project01 source/package and package-check constraints;
  `README.md:242-288` documents skill zips and CCDP's separate package.
- Fit assessment: strong as a constraint, weak as a standalone component.
- Risk: treating `path-contract-constraints` as a component would mix acceptance
  policy with user-facing framework guidance.
- Slice 03 question: Should Project01 constraints be represented as acceptance
  gates attached to every future component contract?
- Arc 02 operator discussion: Decide which path and package promises are hard
  compatibility constraints.

### PSF-07: Contribution Style and Ticket Template May Be an Improper Split

- Finding type: improper split; possible duplication.
- Problem class: upstream contribution noise, overclaiming, maintainer burden.
- Evidence: `docs/CONTRIBUTION-STYLE.md:43-76` defines the shape of a ticket;
  `templates/CONTRIBUTION-TICKET.md:14-29` carries the concrete ticket header;
  `templates/CONTRIBUTION-TICKET.md:133-155` repeats calibrated-honesty
  guidance from the style guide in template form.
- Fit assessment: strong as a paired mechanism, partial as separate components.
- Risk: packaging style without template is too abstract; packaging template
  without style invites formulaic tickets without judgment.
- Slice 03 question: Should this pair be represented as one contribution
  component with guide and template, or two files under one component?
- Arc 02 decision needed: Decide whether templates can ever be standalone
  components or only assets of a guide.

### PSF-08: Delegation Policy Is a Clean Standalone Mechanism

- Finding type: strong fit; low duplication.
- Problem class: context loss, skill loss, judgment delegation, integration
  friction.
- Evidence: `docs/SUBAGENT-DELEGATION-POLICY.md:13-21` states the working
  rule; `docs/SUBAGENT-DELEGATION-POLICY.md:29-36` names the failure modes;
  `SKILL.md:296-302` embeds the short version.
- Fit assessment: strong fit. It has a distinct failure mode, narrow policy,
  and clear load moment.
- Risk: if extracted, the top-level framework still needs a compact summary so
  users do not miss the rule before spawning subagents.
- Slice 03 question: Should this be a standalone operational component with a
  short top-level summary dependency?
- Arc 02 operator discussion: Low-risk candidate for standalone analysis.

### PSF-09: Planning Examples and Provenance Are Support Assets, Not Primary Mechanisms

- Finding type: overfit risk; improper split candidate.
- Problem class: onboarding, version-history rationale, process maintenance.
- Evidence: Slice01 inventory records `project-management-examples` and
  `project-management-provenance`; PM version history records the move to
  `.worktrees/planning` and default `artifacts/` homes.
- Fit assessment: useful secondary support, weak as primary standalone
  components.
- Risk: treating examples or provenance as first-class package components would
  inflate the component set without matching a distinct user problem.
- Slice 03 question: Should examples and version history travel inside their
  owning project-management component rather than appear as candidate
  components?
- Arc 02 operator discussion: Decide the threshold for "component" versus
  "supporting asset."

### PSF-10: Monolithic Load Cost Is the Central Missing Solution

- Finding type: missing solution; underfit.
- Problem class: context load, standalone usefulness, package boundary,
  component contract.
- Evidence: `project-plan.md:28-43` defines Project02's done state as coherent,
  standalone, composable components; `SKILL.md:320-332` currently offers a
  routing table rather than component contracts; Slice01 inventory marks all
  candidate breakout labels as non-final.
- Fit assessment: missing solution by design. The current framework knows its
  load moments, but it has not yet accepted component boundaries or package
  contracts.
- Risk: Slice03 could overfit to current file boundaries or candidate labels
  unless it separates problem classes from component contracts.
- Slice 03 question: Which labels are viable component candidates versus
  dependency edges, constraints, examples, or asset groups?
- Arc 02 decision needed: Establish criteria for standalone usefulness before
  selecting target components.

## Cross-Cutting Questions

- Slice 03: Which overlap is desirable redundancy at different load moments,
  and which overlap is duplication likely to drift?
- Slice 03: Which missing solution areas should be named as Arc02 inputs rather
  than prematurely solved in Arc01?
- Slice 03: Which mislabel candidates are naming problems only, and which
  indicate incorrect conceptual ownership?
- Arc 02 operator discussion: Should every component have a short contract
  covering scope, dependency, load moment, package behavior, and maintenance
  owner?
- Arc 02 decision needed: How should future package checks enforce Project01's
  source/package and package-local path contract for each component?
