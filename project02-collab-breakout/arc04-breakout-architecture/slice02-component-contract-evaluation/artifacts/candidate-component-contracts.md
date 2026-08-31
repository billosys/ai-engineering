# Candidate Component Contracts

```yaml
project: project02-collab-breakout
arc: arc04-breakout-architecture
slice: slice02-component-contract-evaluation
status: proposed-done
contract-status: evaluated-candidates
architecture-decisions: none
```

## Input Contract

These contracts apply the verified Slice01 component-contract schema to the
main candidate components and component families. They consume the Slice01
architecture decision instrument, especially the `component-contract schema`,
`candidate architecture worklist`, and `operator decision and risk register`,
plus closed Arc02 conceptual evidence and closed Arc03 functional evidence.

Every package path below is non-final. Slice03 owns target composition and
package architecture. Slice04 owns operator acceptance. Arc05 later owns
implementation-plan source edits, README updates, `SKILL.md` entrypoints,
packaging changes, validation gates, migration notes, and review concerns.

## Shared Contract Requirements

All accepted or adjusted contracts inherit these fields from the Slice01
schema:

- component name, classification, purpose, owned problem, boundary,
  reason-to-load, dependency edges, wayfinding behavior, support assets and
  templates, adapter notes, source paths, package paths, package-local links,
  zip root assumptions, release gates and validation commands, maintenance
  owner, version history responsibility, risk disposition, go / adjust /
  defer, operator acceptance, and Arc05 implementation-plan fields.
- Project01 and `project01-harmonise-paths` source/package constraints:
  source/package vocabulary, package-local links, generated zip root behavior,
  README and `SKILL.md` release surface updates, Makefile package lists, CCDP
  separation, and `make check-package-paths`.

## `CAW-01` Collaborative Posture And Ethics

- component name: `collaborative-posture-and-ethics`; compatibility source:
  `docs/AI-CONSTITUTION-SUPPLEMENT.md`; possible compact summary in the
  top-level composer.
- classification: candidate component and dependency edge.
- purpose: establish the peer frame, structural-pull awareness, calibrated
  uncertainty, failure recovery, and anti-sycophancy floor for collaborative
  work.
- owned problem: posture owns behavioral and ethical collaboration risk;
  methodology should not own this wholesale because methodology is the craft
  process that depends on the posture.
- boundary: in: collaborative rights, structural pulls, honesty, care,
  humility, failure recovery, and non-enforcement caveats; out: project
  lifecycle mechanics, ledger rows, audit procedure, coverage procedure, and
  packaging rules.
- reason-to-load: session start, disputed judgment, sycophancy risk,
  high-stakes planning, or any task where role posture affects correctness;
  minimum useful load is smaller than the current full composer but must name
  its methodology dependency.
- direct-load classification: plausible direct load with required dependency
  edge.
- dependency edges: prerequisite to `engineering-methodology-and-process`;
  supports contribution voice; composer should include only a compact summary.
- wayfinding behavior: top-level composer and README route to it; methodology
  cites it as a prerequisite; direct-load component links back to methodology
  for process.
- support assets and templates: none required as separate durable assets in
  current evidence.
- adapter notes: role-language notes must explain Codex/Claude and CC/CDC
  mapping when loaded outside the composer.
- source paths: `SKILL.md`, `docs/AI-CONSTITUTION-SUPPLEMENT.md`,
  `docs/AI-ENGINEERING-METHODOLOGY.md`.
- package paths: non-final; candidate package entrypoint may be
  `collaborative-posture-and-ethics/SKILL.md` if accepted.
- package-local links: must resolve to methodology, contribution guidance,
  and any adapter note it cites.
- zip root assumptions: one component-named root if packaged separately; the
  top-level `collaboration-framework/` root remains a composer package.
- release gates and validation commands: `make check-skills` for entrypoint
  metadata changes and `make check-package-paths` after package-local links.
- maintenance owner: posture component owner, with top-level composer owning
  only its summary.
- version history responsibility: `docs/AI-CONSTITUTION-SUPPLEMENT.md` if the
  source remains versioned there; otherwise the accepted component `SKILL.md`
  or enclosing framework `SKILL.md`.
- risk disposition: D-01/OQ-01 remain operator-pending; avoid overclaim per
  BNF-11 and preserve dependency edge to methodology.
- go / adjust / defer: go as dependency, adjust package/composer placement.
- operator acceptance: required and pending.
- Arc05 implementation-plan fields: source edits to `SKILL.md` and
  `docs/AI-CONSTITUTION-SUPPLEMENT.md`; README route; possible new
  `SKILL.md`; package list update; `make check-package-paths`; migration note
  for current composer summary; review concern: over-thin standalone load.

## `CAW-02` Engineering Methodology And Process

- component name: `engineering-methodology-and-process`; compatibility source:
  `docs/AI-ENGINEERING-METHODOLOGY.md`.
- classification: candidate component and router.
- purpose: define the craft substrate, the 9-point SDLC, anti-degradation
  disciplines, and the routing layer into specialized framework components.
- owned problem: methodology owns how sustained work is structured; PM owns
  lifecycle documents, ledger owns evidence semantics, and operational guides
  own their direct workflows.
- boundary: in: knowledge substrate, collaborative posture as prerequisite,
  process rigour, SDLC, anti-degradation, and routing; out: full PM mechanics,
  ledger protocol details, audit prompt body, coverage instructions,
  delegation policy body, contribution ticket template, and package release
  checks.
- reason-to-load: designing or running sustained research, planning, or
  implementation work where the user needs process architecture but not a full
  operational guide.
- direct-load classification: plausible direct load after routing adjustment.
- dependency edges: depends on posture; routes to PM, ledger, audit, coverage,
  delegation, contribution, and domain skills.
- wayfinding behavior: composer points here for the craft layer; README
  explains that methodology is not the operational guide set.
- support assets and templates: none primary; may cite concept-card or
  methodology examples only as support.
- adapter notes: include short role-language mapping and "how to choose the
  next component" guidance.
- source paths: `SKILL.md`, `docs/AI-ENGINEERING-METHODOLOGY.md`,
  `docs/PROJECT-MANAGEMENT.md`, `templates/LEDGER-DISCIPLINE.md`,
  `docs/CODE-AUDIT.md`, `docs/CLAUDE-CODE-COVERAGE.md`,
  `docs/SUBAGENT-DELEGATION-POLICY.md`, `docs/CONTRIBUTION-STYLE.md`.
- package paths: non-final; candidate package may be
  `engineering-methodology-and-process/SKILL.md` plus focused guides.
- package-local links: must route to component package roots without assuming
  source checkout paths.
- zip root assumptions: one component root if packaged; links remain relative
  inside that root.
- release gates and validation commands: `make check-skills`,
  `make check-package-paths`, and package list review.
- maintenance owner: methodology component owner; routed components own their
  full mechanics.
- version history responsibility: `docs/AI-ENGINEERING-METHODOLOGY.md` or the
  accepted component entrypoint, with composer version updated for route
  changes.
- risk disposition: D-02/OQ-02 pending; mitigate BNF-04 and ARG-01 by removing
  duplicated operational detail from the methodology contract.
- go / adjust / defer: adjust.
- operator acceptance: required and pending.
- Arc05 implementation-plan fields: source split or staging edits,
  README/`SKILL.md` route updates, package list changes, validation gates, and
  review concern that a router can silently become the monolith again.

## `CAW-03` Ledger Verification Protocol

- component name: `ledger-verification-protocol`; compatibility source:
  `templates/LEDGER-DISCIPLINE.md`.
- classification: candidate component.
- purpose: define row closure, evidence strength, independent verification,
  deferral/no-op discipline, iteration limits, and silent-drop prevention at
  slice, arc, and project scale.
- owned problem: ledger owns evidence semantics; PM uses ledger in lifecycle
  close but should not duplicate or redefine evidence strength.
- boundary: in: ledger format, evidence strength, done/deferred/no-op rules,
  closer/verifier separation, slice/arc/project adaptation, and composition
  rows; out: planning layout, artifact directory naming beyond the cited
  contract, code audit workflow, and coverage target execution.
- reason-to-load: closing or verifying a ledgered unit, writing acceptance
  rows, checking evidence quality, or auditing silent drops.
- direct-load classification: strong direct load.
- dependency edges: used by PM close mechanics, methodology, audit, coverage,
  and contribution evidence language.
- wayfinding behavior: composer and PM wayfinder route here before close or
  verification work; direct-load guide links back to PM lifecycle docs for
  planning flow.
- support assets and templates: ledger template block and examples; PM close
  docs are dependent guides rather than ledger-owned support.
- adapter notes: role labels CC and CDC require central mapping plus local
  note for Codex surfaces.
- source paths: `templates/LEDGER-DISCIPLINE.md`,
  `docs/PROJECT-MANAGEMENT.md`, `docs/pm/04-closing-slices.md`,
  `docs/pm/05-closing-arcs.md`.
- package paths: non-final; candidate package may be
  `ledger-verification-protocol/SKILL.md` with the ledger discipline template
  as guide content.
- package-local links: must resolve from PM family and from the ledger package
  back to PM close documents where lifecycle is referenced.
- zip root assumptions: component-named zip root, not embedded under PM.
- release gates and validation commands: `make check-skills`,
  `make check-package-paths`; PM package tests must catch broken ledger links.
- maintenance owner: ledger component owner.
- version history responsibility: `templates/LEDGER-DISCIPLINE.md` or
  accepted component entrypoint; PM docs update when lifecycle use changes.
- risk disposition: D-04/ARG-03 resolved at Slice02 level as go for evidence
  ownership and PM lifecycle dependency; operator acceptance still pending.
- go / adjust / defer: go.
- operator acceptance: required and pending.
- Arc05 implementation-plan fields: source/staging strategy, README route,
  component entrypoint, package list, package-local PM links,
  `make check-package-paths`, and review concern for duplicated evidence
  vocabulary.

## `CAW-04` Project Management Family

- component name: `project-management`; compatibility source:
  `docs/PROJECT-MANAGEMENT.md` plus `docs/pm/*.md`.
- classification: component family.
- purpose: guide humans and LLMs through project, arc, slice, planning
  worktree, open-set, close, bubble-up, and plan-change lifecycle mechanics.
- owned problem: PM owns the lifecycle and artifact layout; ledger owns
  evidence semantics used by PM close.
- boundary: in: scales of work, canonical planning worktree, planning
  top-down, slice close, arc close, confirmation protocol, anti-patterns,
  maintenance, worked example, and PM version history; out: standalone ledger
  semantics, code audit, coverage, delegation, contribution, and final package
  release gates except where PM uses them.
- reason-to-load: opening or closing planning units, inspecting artifact
  layout, writing slice prompts, or updating plan records.
- direct-load classification: plausible to strong family load.
- dependency edges: uses `ledger-verification-protocol` for close rows and
  evidence strength; routes to methodology for SDLC context.
- wayfinding behavior: one PM wayfinder should route internal guides; top-level
  composer and README route to PM family for planning/closing.
- support assets and templates: PM examples, PM provenance/version history,
  anti-patterns, confirmation protocol, worked example.
- adapter notes: source/package and role-language mapping should appear in the
  family entrypoint and in close guides where CC/CDC roles appear.
- source paths: `docs/PROJECT-MANAGEMENT.md`, `docs/pm/*.md`,
  `templates/LEDGER-DISCIPLINE.md`.
- package paths: non-final; candidate package may be
  `project-management/SKILL.md` plus `guides/` or equivalent internal docs.
- package-local links: must keep all PM internal links and ledger links
  package-local.
- zip root assumptions: one PM package root if accepted as a family; internal
  guides live beneath that root.
- release gates and validation commands: `make check-skills`,
  `make check-package-paths`, package list review, and README route check.
- maintenance owner: PM family owner, with ledger dependency owned externally.
- version history responsibility: `docs/PROJECT-MANAGEMENT.md` and
  `docs/pm/version-history.md`, or accepted PM component entrypoint if moved.
- risk disposition: D-03/OQ-03 pending; mitigate over-splitting by defaulting
  to one family until Slice03 composes package strategy.
- go / adjust / defer: adjust.
- operator acceptance: required and pending.
- Arc05 implementation-plan fields: source/staging edits, README/entrypoint
  updates, package list additions, `make check-package-paths`, migration note
  for `docs/pm/` links, and review concern for PM/ledger drift.

## `CAW-05` Code Audit Discipline

- component name: `code-audit-discipline`; compatibility source:
  `docs/CODE-AUDIT.md`.
- classification: candidate component.
- purpose: run a full evidence-based, multi-scale, diagnosis-only code quality
  audit with severity-graded findings and modernization synthesis.
- owned problem: audit owns diagnosis and finding structure; coverage owns
  test-writing and code-hardening work.
- boundary: in: audit preparation, language detection, knowledge skill
  loading, audit map, scale coverage, severity, findings, and synthesis; out:
  editing code, driving coverage thresholds, closing project ledgers, and
  package release implementation.
- reason-to-load: commissioning a code quality review, whole-repo audit, or
  language-specific standards audit.
- direct-load classification: strong direct load with adjustment.
- dependency edges: uses domain skills and ledger evidence vocabulary; may
  route to contribution style for upstream tickets after findings.
- wayfinding behavior: composer, README, and methodology route here for audit;
  audit routes to domain skills.
- support assets and templates: audit output examples under audit; no source
  examples should live only in ignored `workbench/` if durable planning output
  is intended.
- adapter notes: replace old workbench-only durable-output implication with
  repository-appropriate output home: slice `artifacts/` when the audit is a
  slice deliverable, otherwise an explicitly chosen workbench/report home.
- source paths: `docs/CODE-AUDIT.md`, `knowledge/*/SKILL.md`,
  `knowledge/*/guides/`.
- package paths: non-final; candidate package may be
  `code-audit-discipline/SKILL.md`.
- package-local links: must include domain-skill routes and any output example
  links.
- zip root assumptions: component-named root if packaged separately.
- release gates and validation commands: `make check-skills`,
  `make check-package-paths`; audit-specific checks remain project-adapted.
- maintenance owner: audit component owner.
- version history responsibility: `docs/CODE-AUDIT.md` or accepted audit
  entrypoint; top-level composer if trigger routing changes.
- risk disposition: ARG-04 requires output-home tightening before acceptance;
  D-08/OQ-04 favor sibling relationship with coverage.
- go / adjust / defer: go / adjust.
- operator acceptance: required and pending.
- Arc05 implementation-plan fields: edit audit prompt for artifact-home
  convention, README route, possible `SKILL.md`, package list, path checks, and
  review concern that diagnosis-only scope must remain intact.

## `CAW-06` Coverage Hardening Discipline

- component name: `coverage-hardening-discipline`; compatibility source:
  `docs/CLAUDE-CODE-COVERAGE.md`.
- classification: candidate component.
- purpose: drive a codebase to a hard coverage target by adding or repairing
  tests and fixing root causes rather than hiding failures.
- owned problem: coverage owns coverage closure and test hardening; audit owns
  diagnosis and does not edit code.
- boundary: in: target coverage, warning treatment, lint/format/test loops,
  coverage measurement, error-path tests, and root-cause repair; out:
  language-specific correctness rules except through domain skills, audit
  findings, PM planning, and release packaging.
- reason-to-load: a user asks to raise coverage to a threshold or repair
  tests to meet a gate.
- direct-load classification: plausible direct load after naming/example
  adjustment.
- dependency edges: uses repository-specific tooling, domain test idioms,
  methodology quality floor, and possibly ledger evidence vocabulary.
- wayfinding behavior: composer and README route here for coverage work; audit
  may cite it only when findings become implementation work.
- support assets and templates: coverage progress report shape and examples;
  examples must be language-neutral or clearly project-adapted.
- adapter notes: title is historical; contract must make Codex/Claude and
  Cargo examples explicit adapters, not hidden requirements.
- source paths: `docs/CLAUDE-CODE-COVERAGE.md`, domain skill guides,
  repository Makefiles and CI configs in target projects.
- package paths: non-final; final name may stay
  `coverage-hardening-discipline` or receive a compatibility alias from
  `CLAUDE-CODE-COVERAGE.md`.
- package-local links: route to domain skills and project tooling guidance.
- zip root assumptions: component-named root if packaged.
- release gates and validation commands: `make check-skills`,
  `make check-package-paths`; target-project coverage commands remain
  project-specific.
- maintenance owner: coverage component owner.
- version history responsibility: `docs/CLAUDE-CODE-COVERAGE.md` or accepted
  component entrypoint; composer route if renamed.
- risk disposition: D-07/OQ-05/ARG-05 require naming and generality adjustment.
- go / adjust / defer: adjust.
- operator acceptance: required and pending.
- Arc05 implementation-plan fields: rename/wrap decision, README/entrypoint
  updates, compatibility alias, package list, path checks, and review concern
  for Rust/Cargo overfit.

## `CAW-07` Delegation Policy

- component name: `delegation-policy`; compatibility source:
  `docs/SUBAGENT-DELEGATION-POLICY.md`.
- classification: candidate component.
- purpose: preserve quality by keeping thinking/edit/review judgment in the
  main context while allowing parallel lookup work.
- owned problem: delegation owns the thinking-vs-lookup boundary; methodology
  only routes to it.
- boundary: in: delegation rule, failure modes, install surfaces, verification
  signs, and one-off use; out: broader SDLC, code review judgments, and
  package release gates.
- reason-to-load: deciding whether to use subagents or parallel lookup during
  a sustained task.
- direct-load classification: strong direct load.
- dependency edges: supports methodology, audit, review, planning, and any
  task with subagent tools.
- wayfinding behavior: composer and methodology route here; standalone guide
  states it can be loaded directly.
- support assets and templates: install-note snippets may travel as support.
- adapter notes: Codex, Claude Code, Claude Desktop, and Cowork surface names
  require local role-language mapping.
- source paths: `docs/SUBAGENT-DELEGATION-POLICY.md`, `SKILL.md`.
- package paths: non-final; candidate package may be
  `delegation-policy/SKILL.md`.
- package-local links: minimal; any methodology route must resolve.
- zip root assumptions: component-named root if packaged.
- release gates and validation commands: `make check-skills`,
  `make check-package-paths`.
- maintenance owner: delegation component owner.
- version history responsibility: `docs/SUBAGENT-DELEGATION-POLICY.md` or
  accepted component entrypoint.
- risk disposition: ARG-08 role-language risk mitigated by central adapter plus
  local notes.
- go / adjust / defer: go.
- operator acceptance: required and pending.
- Arc05 implementation-plan fields: component entrypoint, source route,
  README update, package list, path check, and review concern for accidental
  analytical delegation.

## `CAW-08` Contribution Style And Voice

- component name: `contribution-style-and-voice`; compatibility source:
  `docs/CONTRIBUTION-STYLE.md`.
- classification: candidate component with support asset.
- purpose: draft calibrated upstream tickets that are specific, respectful of
  maintainer ownership, evidence-bounded, and easy to act on.
- owned problem: contribution style owns public-ticket voice and discipline;
  the template is a support asset rather than a separate component.
- boundary: in: ticket voice, calibrated honesty, shape, sizing, upstream
  etiquette, and template use; out: code audit itself, project management,
  source packaging, and maintainer-side decisions.
- reason-to-load: drafting an upstream bug, feature, documentation fix, or
  unconfirmed question.
- direct-load classification: strong direct load when shipped with template.
- dependency edges: supported by posture and methodology; may consume audit
  findings as ticket inputs.
- wayfinding behavior: composer, README, and audit can route to contribution
  guide; guide links package-locally to template.
- support assets and templates: `templates/CONTRIBUTION-TICKET.md` must travel
  with the component.
- adapter notes: line-reference and current-HEAD caveats remain source/package
  aware.
- source paths: `docs/CONTRIBUTION-STYLE.md`,
  `templates/CONTRIBUTION-TICKET.md`.
- package paths: non-final; candidate package may be
  `contribution-style-and-voice/SKILL.md` plus template support asset.
- package-local links: template link must resolve inside the package root.
- zip root assumptions: component-named root with template under a predictable
  support/templates path.
- release gates and validation commands: `make check-skills`,
  `make check-package-paths`.
- maintenance owner: contribution component owner.
- version history responsibility: `docs/CONTRIBUTION-STYLE.md` or accepted
  component entrypoint; template history if the template becomes versioned.
- risk disposition: D-09/ARG-06 favor guide plus template support asset.
- go / adjust / defer: go.
- operator acceptance: required and pending.
- Arc05 implementation-plan fields: entrypoint, template packaging, README
  route, package list, path check, and review concern for separating voice from
  template.

## Partial Composer And Adapter Contracts For Slice03

### `CAW-09` Framework Entrypoint And Routing

- component name: `framework-entrypoint-and-routing`; compatibility source:
  top-level `SKILL.md`; relationship to `collaboration-framework` package must
  remain explicit.
- classification: top-level composer / adapter.
- purpose: preserve discovery, session start, broad human orientation, and
  composed workflow routing after breakout.
- owned problem: the composer owns how components are found and combined; it
  does not own the full text of every component.
- boundary: in: compact posture/process floor, component routing table,
  dependency order, source/package adapter links; out: full operational guide
  content and final operator acceptance.
- reason-to-load: broad or ambiguous session start, first-time user
  orientation, or combination workflow.
- dependency edges: routes to posture, methodology, PM, ledger, audit,
  coverage, delegation, contribution, repository orientation, and agent
  adapter.
- wayfinding behavior: remains the `/collaboration-framework` load surface.
- support assets and templates: none owned directly except route indexes.
- adapter notes: central place for Codex/Claude role mapping, with local notes
  in standalone components.
- source paths: `SKILL.md`, README collaboration-framework section.
- package paths: non-final; current package is `collaboration-framework.zip`
  with root `collaboration-framework/`.
- package-local links: all component routes must resolve in source and package
  contexts.
- zip root assumptions: current composer package root remains
  `collaboration-framework/` unless operator accepts a new release shape.
- release gates and validation commands: `make collab-framework`,
  `make check-skills`, `make check-package-paths`.
- maintenance owner: top-level composer owner.
- version history responsibility: top-level `SKILL.md`.
- risk disposition: D-05/ARG-01 require thin but not link-only composer.
- go / adjust / defer: adjust.
- operator acceptance: required and pending.
- Arc05 implementation-plan fields: route table, summary trims, README
  changes, package list behavior, path validation, and review concern for
  losing safety floor.

### `CAW-10` Agent Adapter And Routing

- component name: `agent-adapter-and-routing`.
- classification: adapter, with deferred standalone component status.
- purpose: translate CC/CDC/Claude/Codex/operator role language so each
  component is usable when loaded alone.
- owned problem: role-language translation and standalone readability; not the
  substantive workflow of any component.
- boundary: in: role mappings, local-note requirements, drift controls, and
  source/package language; out: methodology, PM, ledger, audit, coverage,
  delegation, and contribution content.
- reason-to-load: standalone components refer to CC, CDC, Codex, Claude, or
  operator roles and the reader is not in the original surface.
- direct-load classification: weak as standalone, necessary as adapter.
- dependency edges: every role-bearing component cites the adapter or embeds a
  short local note.
- wayfinding behavior: composer routes to the central adapter; standalone
  entrypoints include short local adapter notes.
- support assets and templates: short local-note pattern to be defined in
  Slice03/Arc05.
- adapter notes: this is the adapter note owner.
- source paths: `SKILL.md`, framework docs with "Notes for Codex", PM docs,
  ledger template, audit, coverage, delegation, contribution docs.
- package paths: non-final; may be central guide inside composer package or
  shared support package.
- package-local links: every direct-load component must resolve adapter links
  locally.
- zip root assumptions: central package root if accepted; otherwise local
  notes travel with each component.
- release gates and validation commands: `make check-package-paths` and role
  grep checks in Arc05.
- maintenance owner: central adapter owner plus component owners for local
  notes.
- version history responsibility: top-level `SKILL.md` or accepted adapter
  entrypoint.
- risk disposition: D-06/OQ-06/ARG-08 favor central plus local notes.
- go / adjust / defer: adjust as adapter, defer standalone component.
- operator acceptance: required and pending.
- Arc05 implementation-plan fields: central note source, local note placement,
  README route, package links, validation grep, and review concern for drift.
