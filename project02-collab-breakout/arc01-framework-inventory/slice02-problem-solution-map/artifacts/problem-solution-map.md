# Problem-Solution Map

```yaml
project: project02-collab-breakout
arc: arc01-framework-inventory
slice: slice02-problem-solution-map
status: proposed-done
source-basis:
  - ../slice01-source-inventory/cdc-verification.md
  - ../slice01-source-inventory/artifacts/framework-source-inventory.md
  - ../slice01-source-inventory/artifacts/source-to-concept-map.md
  - ../slice01-source-inventory/artifacts/project01-path-contract-notes.md
candidate-labels: non-final, not component decisions
```

## Basis

Slice 01 is verified-closed. CDC verified `Rows: 7`, `Done: 7`,
`Deferred: 0`, and `No-op: 0` in
`../slice01-source-inventory/cdc-verification.md`. This map treats the Slice 01
inventory as the evidence base and uses current source files only as read-only
clarification.

The candidate breakout labels named here are non-final. They are analysis
handles for Slice 03 and Arc 02, not accepted architecture.

## Problem Rows

### PSM-01: Domain Knowledge Evaporation

- Problem class: domain knowledge loss, substrate reset, repeated re-derivation.
- Historical or functional symptom: without explicit domain knowledge, every
  LLM session starts near zero and loses hard-won judgment when the context
  ends.
- Current mechanism: knowledge substrate, domain skill library, source
  provenance, repository orientation, and skill entrypoint routing.
- Source evidence: `README.md:184-192` lists framework docs and operational
  guides; `SKILL.md:217-226` defines knowledge substrate as portable,
  auditable, indexed, and maintained; `docs/AI-ENGINEERING-METHODOLOGY.md:90`
  says substrate prevents every session starting at zero.
- Candidate breakout labels involved: `repository-orientation-and-distribution`,
  `framework-entrypoint-and-routing`, `engineering-methodology-and-process`
  (non-final).
- Fit assessment: strong fit for source-backed reusable knowledge, partial fit
  for standalone use because the current top-level skill still routes through a
  broad monolith.
- Question: For Slice 03, which substrate guidance belongs in the top-level
  composer versus a standalone methodology/substrate component?
- Disposition: Carry forward as a core problem class for Arc 02 ontology work.

### PSM-02: Tooling and Entrypoint Confusion

- Problem class: tooling confusion, entrypoint ambiguity, command drift.
- Historical or functional symptom: humans and LLMs hand-run scripts, miss
  Make-backed targets, or confuse source checkout guidance with installed skill
  guidance.
- Current mechanism: README build/install section, `SKILL.md` runtime routing,
  AGENTS Make-target convention, and Project01 package-path checks.
- Source evidence: `README.md:242-270` names Make-backed package and validation
  targets; `README.md:274-288` distinguishes skill bundles from `ccdp.zip`;
  `AGENTS.md:54-66` says to start with `make help` and use Make targets.
- Candidate breakout labels involved:
  `repository-orientation-and-distribution`,
  `framework-entrypoint-and-routing`, `path-contract-constraints` (non-final).
- Fit assessment: strong fit for source users; partial fit for package users
  because package-specific command affordances remain centralized in README
  prose rather than per-component contracts.
- Question: For Slice 03, should tool routing be a distribution component or
  remain part of the top-level composer?
- Disposition: Preserve as a functional release-surface concern.

### PSM-03: Drift, Duplication, and Orphaned Work

- Problem class: drift, duplication, orphan work, inconsistent application.
- Historical or functional symptom: cross-feature drift, inconsistent
  best-practice adoption, code duplication, and orphaning appear across long
  lived LLM-assisted projects.
- Current mechanism: 9-point SDLC, project/arc/slice planning, multi-scale
  audits, modernization synthesis, PM maintenance/version history.
- Source evidence: `README.md:56` names drift, duplication, and orphaning;
  `SKILL.md:243-259` explains SDLC altitude and bottom-up recomposition;
  `docs/CODE-AUDIT.md:248-258` requires system themes and modernization moves;
  `docs/pm/08-maintenance.md:1-24` covers process-doc maintenance and artifact
  category drift.
- Candidate breakout labels involved: `engineering-methodology-and-process`,
  `project-management-wayfinder`, `code-audit-discipline`,
  `evidence-backed-modernization`, `framework-maintenance-discipline`
  (non-final).
- Fit assessment: strong fit for detection and planning; duplicated in a
  useful way across methodology, PM, and audit guidance, but the duplication is
  a drift risk if split without a clear owner.
- Question: Which future component owns anti-drift vocabulary so the same rule
  is not maintained independently in several places?
- Disposition: Flag as overlap and possible duplication for findings.

### PSM-04: Context-Window Overrun

- Problem class: context sizing, LLM working-memory overload, slice mis-sizing.
- Historical or functional symptom: work that exceeds one coherent model
  context loses the thread, burns iteration budget, or resumes from compressed
  summaries with weakened evidence.
- Current mechanism: project/arc/slice scale model, context-bounded slice
  definition, five-iteration budget, and plan-late/plan-deep rule.
- Source evidence: `docs/pm/01-scales-of-work.md:32-38` defines a slice as one
  context with headroom; `docs/pm/01-scales-of-work.md:76-90` makes context
  window the sizing bottleneck; `templates/LEDGER-DISCIPLINE.md:231-232`
  routes repeated failure to re-scope or fresh context.
- Candidate breakout labels involved: `project-management-scale-model`,
  `planning-open-set-mechanics`, `ledger-verification-protocol` (non-final).
- Fit assessment: strong fit as planning discipline; underfit as automation
  because no current mechanism measures or gates context budget.
- Question: Should Arc 02 treat context sizing as part of project management,
  ledger discipline, or a separate execution-planning component?
- Disposition: Carry forward as an underfit risk.

### PSM-05: Generalization and Abstraction Failure

- Problem class: generalization failure, abstraction risk, human/LLM judgment
  boundary.
- Historical or functional symptom: LLMs fail at abstract reasoning or produce
  improper generalizations, especially around architecture and refactoring.
- Current mechanism: explicit human presence for abstractions, peer frame,
  research/design steps before implementation, self-review/peer-review/audit,
  and code-audit modernization checks.
- Source evidence: `README.md:58` names failures of abstract reasoning and
  proper generalizations; `README.md:88` requires explicit human presence for
  abstractions/generalizations; `docs/AI-ENGINEERING-METHODOLOGY.md:176-186`
  describes the SDLC steps and the altitude of errors they catch.
- Candidate breakout labels involved: `collaborative-posture-and-ethics`,
  `engineering-methodology-and-process`, `verification-methodology`,
  `code-audit-discipline` (non-final).
- Fit assessment: partial fit. The framework names the risk and installs
  review gates, but there is no dedicated abstraction-decision protocol.
- Question: Does Arc 02 need to separate abstraction governance from general
  methodology?
- Disposition: Mark as underfit and possible missing solution area.

### PSM-06: Silent Drop and Arbitrary Deferral

- Problem class: silent drop, arbitrary deferral, incomplete closure.
- Historical or functional symptom: work appears complete while requested
  pieces are omitted, deferred without re-entry, or never checked row by row.
- Current mechanism: ledger rows, evidence strength, per-row close reports,
  CDC verification, slice bubble-up, and silent-drop diff.
- Source evidence: `README.md:59` names silent drops and arbitrary deferrals;
  `README.md:112-114` says ledger discipline eliminates silent drops;
  `templates/LEDGER-DISCIPLINE.md:103-108` names silent drops and verifier
  separation; `docs/pm/04-closing-slices.md:17-33` requires per-row close and
  silent-drop diff.
- Candidate breakout labels involved: `ledger-verification-protocol`,
  `slice-close-and-bubble-up`, `verification-methodology` (non-final).
- Fit assessment: strong fit. This is the cleanest current mechanism-to-problem
  match in the framework.
- Question: Should ledger discipline become its own standalone component with
  PM close files depending on it, or stay packaged only through the top-level
  framework?
- Disposition: Strong candidate for standalone extraction analysis in Arc 02.

### PSM-07: Spec-Softening and Partial Adoption

- Problem class: spec-softening, partial adoption, evidence weaker than claim.
- Historical or functional symptom: the spec quietly moves to match what was
  delivered, or a rule is applied at some call sites and skipped at others.
- Current mechanism: ledger evidence reproduction, explicit spec-keeping,
  self-review/peer-review/audit loop, and workspace-wide code-audit greps.
- Source evidence: `README.md:59` names spec-softening and partial adoption;
  `SKILL.md:276-283` requires disclosed deferral, silent-drop detection, and
  visible spec; `templates/LEDGER-DISCIPLINE.md:205-211` tells CDC to watch
  for spec-softening and partial adoption; `docs/CODE-AUDIT.md:278-291` says
  the context window is not scope and coherence must be auditable.
- Candidate breakout labels involved: `ledger-verification-protocol`,
  `code-audit-discipline`, `engineering-methodology-and-process` (non-final).
- Fit assessment: strong fit, with overlap between ledger and audit guidance
  that should be treated as deliberate reinforcement only if ownership is
  clear.
- Question: Which component owns the general rule, and which components merely
  specialize it?
- Disposition: Flag as overlap and potential duplication.

### PSM-08: Sycophancy and Deference

- Problem class: sycophancy, deference, agreement against evidence.
- Historical or functional symptom: an LLM agrees because the user seems to
  want agreement, does not push back, or reports pleasing certainty instead of
  grounded judgment.
- Current mechanism: Constitution supplement, peer frame, collaborative rights,
  calibrated uncertainty, failure naming, and SKILL posture summary.
- Source evidence: `README.md:60` names sycophancy and deference; `README.md:116-118`
  describes the peer-not-sycophant mechanism; `docs/AI-CONSTITUTION-SUPPLEMENT.md:170-177`
  names the user's right to pre-failure signal; `docs/AI-CONSTITUTION-SUPPLEMENT.md:270-282`
  requires clean failure naming and recovery.
- Candidate breakout labels involved: `collaborative-posture-and-ethics`,
  `framework-entrypoint-and-routing`, `agent-adapter-and-routing` (non-final).
- Fit assessment: strong fit for posture, partial fit for enforcement because
  the mechanism depends on the model actually loading and honoring the posture.
- Question: Should the posture component stand alone so it can be loaded without
  the whole process stack?
- Disposition: Carry to Arc 02 as a major conceptual boundary question.

### PSM-09: Human/LLM Role Confusion

- Problem class: human/LLM authority blur, reviewer/doer collapse, accountability
  confusion.
- Historical or functional symptom: the same attention that produces work
  verifies it; CC/CDC roles blur; the user cannot tell whether a claim is
  implemented, attested, reproduced, or reconciled.
- Current mechanism: CC/CDC terminology, ledger evidence ladder, independent
  audits, subagent boundary, and contribution-calibration guidance.
- Source evidence: `SKILL.md:74-86` adapts CDC/CC roles to Codex;
  `templates/LEDGER-DISCIPLINE.md:118-136` defines evidence strength and role
  separation; `docs/AI-ENGINEERING-METHODOLOGY.md:200-210` defines CAP-style
  independent audit properties; `docs/SUBAGENT-DELEGATION-POLICY.md:13-21`
  separates thinking from lookup.
- Candidate breakout labels involved: `agent-adapter-and-routing`,
  `verification-methodology`, `ledger-verification-protocol`,
  `delegation-policy` (non-final).
- Fit assessment: strong fit conceptually, partial fit in naming because some
  source documents still carry Claude-specific or surface-specific names.
- Question: Does Arc 02 need a surface-neutral adapter layer separate from the
  top-level `SKILL.md`?
- Disposition: Mark as mislabel candidate and adapter-boundary question.

### PSM-10: Planning Path and Artifact Orphaning

- Problem class: path confusion, planning artifact orphaning, workbench misuse.
- Historical or functional symptom: durable planning outputs land in root
  `workbench/`, implementation `docs/`, scratch directories, or stale design
  paths instead of the owning slice.
- Current mechanism: canonical planning worktree, confirmation protocol,
  PM anti-patterns, `artifacts/` default, and Project01 path contract.
- Source evidence: `docs/pm/02-canonical-planning-worktree.md:3-27` defines
  the planning branch/worktree; `docs/pm/02-canonical-planning-worktree.md:122-146`
  defines per-slice documents and artifact home; `docs/pm/07-anti-patterns.md:11-14`
  rejects misplaced slice artifacts; Slice01
  `artifacts/project01-path-contract-notes.md:60-69` carries the Project01
  constraint into Project02.
- Candidate breakout labels involved: `planning-worktree-and-layout`,
  `planning-confirmation-protocol`, `planning-anti-patterns-and-repair`,
  `path-contract-constraints` (non-final).
- Fit assessment: strong fit after Project01; duplication across PM and ledger
  is intentional but must stay synchronized.
- Question: Should future component packages include planning-path guidance, or
  should it live only in a project-management component?
- Disposition: Preserve as a release-surface and planning-safety constraint.

### PSM-11: Package and Release Surface Confusion

- Problem class: package path contract, package-local links, zip roots, release
  surface mismatch.
- Historical or functional symptom: generated zips contain broken Markdown
  links, source-only references leak into packages, or readers confuse source
  clone, skill zip, unzipped install, and CCDP package workflows.
- Current mechanism: README package guidance, Makefile package targets,
  `make check-package-paths`, CCDP package checks, and Project01 final contract.
- Source evidence: `README.md:242-288` documents skill zips and separate
  `ccdp.zip`; `README.md:342-349` names package-local CCDP links and excluded
  source-only directories; Slice01 `artifacts/project01-path-contract-notes.md:32-56`
  summarizes source/package constraints and package checks.
- Candidate breakout labels involved: `repository-orientation-and-distribution`,
  `protocol-distribution-guidance`, `path-contract-constraints` (non-final).
- Fit assessment: strong fit for current distribution; underfit for future
  breakout because per-component package contracts do not exist yet.
- Question: For Slice 03, what package-path facts must be passed to Arc 02 as
  hard compatibility promises?
- Disposition: Carry as required Project01 functional constraint.

### PSM-12: Audit and Coverage Quality Floor

- Problem class: quality-floor drift, unverified code quality, inadequate
  coverage, weak tests.
- Historical or functional symptom: passing tests are treated as sufficient,
  code quality is sampled only inside the current context, coverage stalls
  below threshold, and modernization is proposed without evidence.
- Current mechanism: code-audit prompt, coverage prompt, independent audit
  properties, root-cause testing, and quality gates.
- Source evidence: `README.md:119-125` names independent audits, hard coverage
  targets, and subagent guardrails; `docs/CODE-AUDIT.md:8-13` rejects
  context-window sampling; `docs/CODE-AUDIT.md:242-261` defines modernization
  synthesis; `docs/CLAUDE-CODE-COVERAGE.md:352-375` names coverage gates and
  iterative process.
- Candidate breakout labels involved: `code-audit-discipline`,
  `evidence-backed-modernization`, `coverage-hardening-discipline`,
  `verification-methodology` (non-final).
- Fit assessment: strong fit inside code-quality work; overfit risk where the
  coverage prompt is language/tool specific and may not generalize as a
  framework-wide component without adaptation.
- Question: Should coverage hardening be a standalone testing discipline or a
  subordinate guide under code-quality methodology?
- Disposition: Flag overfit and component-placement question.

### PSM-13: Subagent Judgment Leakage

- Problem class: delegation leakage, context loss, LLM-to-LLM telephone.
- Historical or functional symptom: subagents are asked to design, decide,
  write, or judge, losing context and skill instructions while producing a
  summary the main agent still has to re-evaluate.
- Current mechanism: subagent delegation policy and `SKILL.md` routing that
  keeps thinking in the main context and allows parallel lookup.
- Source evidence: `docs/SUBAGENT-DELEGATION-POLICY.md:13-21` states the
  no-delegated-thinking rule; `docs/SUBAGENT-DELEGATION-POLICY.md:29-36` names
  context loss, skill loss, and integration friction; `SKILL.md:296-302`
  embeds the same boundary.
- Candidate breakout labels involved: `delegation-policy`,
  `framework-entrypoint-and-routing`, `agent-adapter-and-routing` (non-final).
- Fit assessment: strong fit. The rule is narrow, self-contained, and has a
  clear load moment.
- Question: Should delegation policy remain a short operational guide, or move
  into a broader execution-governance component?
- Disposition: Candidate standalone operational component for Arc 02 analysis.

### PSM-14: Upstream Contribution Noise

- Problem class: contribution quality, maintainer burden, evidence calibration.
- Historical or functional symptom: tickets are too thin to act on, too long to
  read, overclaim certainty, bundle multiple problems, or impose on maintainer
  ownership.
- Current mechanism: contribution style guide and contribution ticket template.
- Source evidence: `docs/CONTRIBUTION-STYLE.md:18-21` names too-thin and
  too-broad ticket failures; `docs/CONTRIBUTION-STYLE.md:81-90` defines
  calibrated honesty; `templates/CONTRIBUTION-TICKET.md:133-155` names habits
  for useful tickets and unconfirmed questions.
- Candidate breakout labels involved: `contribution-style-and-voice`,
  `contribution-ticket-template` (non-final).
- Fit assessment: strong fit, with improper split possibility because the style
  and template are only independently useful in narrow cases.
- Question: Should contribution guidance be a composed pair, a single component,
  or an optional operational add-on?
- Disposition: Flag possible improper split.

### PSM-15: Framework Maintenance and Version Drift

- Problem class: framework maintenance, guide drift, version-history mismatch.
- Historical or functional symptom: split PM files, top-level routing, package
  guidance, and ledger rules can drift when one file changes and another is not
  updated.
- Current mechanism: PM maintenance guidance, version histories, README/SKILL
  routing, and Project01 path checks.
- Source evidence: `docs/pm/08-maintenance.md:1-24` says to update the
  wayfinder, version history, and synchronized files; `SKILL.md:375-385`
  records versioned routing changes; `AGENTS.md:27-30` requires version-history
  updates when framework docs change.
- Candidate breakout labels involved: `framework-maintenance-discipline`,
  `project-management-provenance`, `framework-entrypoint-and-routing`,
  `path-contract-constraints` (non-final).
- Fit assessment: partial fit. The guidance exists, but there is no explicit
  component-coherence checklist for a post-breakout world.
- Question: Should Arc 02 require a component-maintenance contract before any
  implementation plan is accepted?
- Disposition: Mark as missing solution area for future breakout maintenance.

### PSM-16: Monolithic Load Cost and Component Boundary Ambiguity

- Problem class: context load, package/component ambiguity, standalone
  usefulness gap.
- Historical or functional symptom: a user who needs only ledger discipline,
  contribution tickets, coverage, or delegation must enter through the broad
  collaboration-framework skill and infer which parts are independently useful.
- Current mechanism: top-level `SKILL.md` load-when table, README guide index,
  and Project02 planning itself.
- Source evidence: `SKILL.md:320-332` lists framework files and load moments;
  Slice01 `artifacts/framework-source-inventory.md:52-75` identifies `SKILL.md`
  as a router rather than a full standalone process; `project-plan.md:28-43`
  defines Project02's done state as coherent standalone composable components.
- Candidate breakout labels involved: all current labels remain non-final,
  especially `framework-entrypoint-and-routing`,
  `ledger-verification-protocol`, `code-audit-discipline`,
  `coverage-hardening-discipline`, `delegation-policy`,
  `contribution-style-and-voice`, `contribution-ticket-template` (non-final).
- Fit assessment: missing solution. The current framework has routing hints but
  no accepted component contracts yet.
- Question: Slice 03 must distinguish current load labels from candidate
  component contracts before Arc 02 starts.
- Disposition: Central input for Slice 03 synthesis.

## Open Questions

- Slice 03: Which rows above are true component candidates and which are just
  problem classes covered by shared mechanisms?
- Slice 03: Which overlaps are deliberate reinforcement needed at multiple load
  moments, and which are duplication that will drift if split?
- Slice 03: Which underfit/missing-solution areas should become explicit Arc 02
  questions rather than assumed architecture work?
- Arc 02 operator discussion: Should the final breakout optimize first for
  lower context load, stronger standalone usefulness, package stability, or
  maintenance ownership?
- Arc 02 decision needed: Which Project01 path contract constraints are hard
  compatibility promises for every component package?
