# Scenario Matrix

```yaml
project: project02-collab-breakout
arc: arc03-functional-analysis
slice: slice01-usage-surface-instrument
status: proposed-done
architecture-decisions: none
matrix-status: analytical, non-final, not accepted architecture
```

## Evidence Basis

This matrix consumes Arc02 closed/composed evidence: conceptual model, boundary
and naming findings, operator decision register, and close-readiness. It also
uses current source grounding for README, SKILL, project-management, ledger,
audit, coverage, delegation, contribution, templates, and package/release gate
surfaces.

Scenario rows are work instructions for later Arc03 evaluation slices. They do
not decide architecture; architecture deferred to Arc04 after operator
acceptance.

## Row Fields

| Scenario ID | Actor | Entrypoint | Trigger | Inputs | Expected outcome | Load set | Dependencies | Friction signals | Evidence to collect | Downstream owner |
|-------------|-------|------------|---------|--------|------------------|----------|--------------|------------------|---------------------|------------------|
| S-01 current monolith source/package | Human source reader | `README.md` | direct source-clone reading after clone | README, source tree, Makefile target list | Reader can tell source clone, packaged skill, unzipped install, and CCDP package modes apart. | README sections for use, build/install, repository layout, CCDP | Project01 path gates | source/package ambiguity, package-local link confusion, release surface drift | Compare README guidance to package/release gate language and `make check-package-paths`. | Slice02 current workflow |
| S-02 current monolith LLM skill loading | Active LLM | top-level `SKILL.md` or `/collaboration-framework` | session start | SKILL routing table and required load guidance | LLM gets posture/process floor and routes to PM, ledger, audit, coverage, delegation, or contribution as needed. | top-level composer plus target operational guide | posture before methodology; PM before planning; ledger before ledgered close | high context cost, over-rich composer, hidden dependency order | Walk through a planning and audit trigger from `SKILL.md`. | Slice02 current workflow |
| S-03 planning workflow | CC or CDC | `docs/PROJECT-MANAGEMENT.md` | planning a project/arc/slice | PM wayfinder, PM split files, ledger discipline | Actor can open planning work with canonical files and artifact home. | PM wayfinder, scales, layout, top-down planning, ledger | PM layout before open set; ledger before criteria | routing friction across PM family, support asset overfit | Trace required load set and minimum useful load set. | Slice02 current workflow |
| S-04 execution workflow | CC | slice `cc-prompt.md` | execution requested by operator | slice plan, ledger, source checkout | CC can execute slice without source/planning confusion and reports CC-attested close. | slice prompt, slice plan, ledger, source files as needed | source checkout read/write scope from instructions | role-language clarity, source/package mode ambiguity | Compare prompt instructions to AGENTS.md planning/source split. | Slice02 current workflow |
| S-05 review workflow | CDC or fresh verifier | `closing-report.md` and `ledger.md` | proposed-done slice | artifacts, ledger, diff, close report | Reviewer reproduces rows and writes CDC verification. | ledger discipline, PM close guide, slice artifacts | ledger evidence semantics before close review | attested/reproduced confusion, inherited claim acceptance | Re-run sample Verify commands and row-count checks. | Slice02 current workflow |
| S-06 slice close and arc close composition | CDC and operator | PM close files and arc ledger | slice or final arc slice closes | child close reports, arc ledger, artifacts | Slice close bubbles up to arc; arc close reproduces composition. | PM slice close, PM arc close, ledger discipline | ledger versus PM dependency direction | unclear handoff, remediation versus iteration confusion | Compare slice close output to arc ledger criteria. | Slice02 current workflow |
| S-07 audit standalone component | User and active LLM | `docs/CODE-AUDIT.md` | audit requested | README, project context, domain skills | Audit remains diagnosis-only and writes scoped workbench outputs unless ledgered slice overrides to artifacts. | code-audit discipline plus domain skills | domain skill loading after audit map | output-location conflict, modernization overreach | Apply audit preparation/output rules to a source checkout. | Slice02 current workflow |
| S-08 coverage standalone component | CC/test actor | `docs/CLAUDE-CODE-COVERAGE.md` | coverage threshold requested | repo tooling, tests, coverage tool | Actor adapts commands and drives threshold without hiding failures. | coverage-hardening-discipline plus repo-specific tooling | source/package mode, language test idioms | Claude/Cargo naming, non-Rust underfit, context cost | Test whether guide remains usable outside Rust/Cargo examples. | Slice03 standalone component |
| S-09 delegation standalone component | Active LLM | `docs/SUBAGENT-DELEGATION-POLICY.md` | task invites subagents | current task and tool context | Thinking remains in main context; lookup may be parallelized. | delegation-policy only, optionally methodology summary | role-language clarity | hidden dependency on methodology, policy too narrow | Walk a multi-step task and classify thinking versus lookup. | Slice03 standalone component |
| S-10 contribution standalone component | Human or LLM drafter | contribution style plus ticket template | upstream bug/feature/doc/question | issue evidence, source line refs, template | Ticket is calibrated, specific, respectful, and cheap for maintainer. | contribution-style-and-voice plus contribution-ticket-template | template depends on style | template-only misuse, support asset split | Draft or inspect a mock ticket path and dependency. | Slice03 standalone component |
| S-11 posture/methodology composed component | Operator and LLM | posture and methodology guides | substantial session start or planning | Constitution supplement, methodology, top-level composer | Actor gets peer frame plus SDLC/process without loading all specialized guides. | posture, methodology, routed guide names | posture prerequisite to methodology | posture/methodology merge or split cost | Compare load cost and missing guarantees in standalone versus composed use. | Slice03 standalone component |
| S-12 PM and ledger composed component | CC/CDC | PM close plus ledger discipline | ledgered planning or close | PM wayfinder, PM close guides, ledger discipline | Actor can distinguish lifecycle routing from evidence semantics. | project-management family plus ledger-verification-protocol | ledger versus PM ownership | duplicated close semantics, evidence term drift | Trace one slice close and one arc close through both components. | Slice03 standalone component |
| S-13 top-level composer combination | Human or LLM | top-level composer | task needs several disciplines | Arc02 conceptual model and current SKILL routing | Composer routes to minimum useful load set without restoring monolith load cost. | framework-entrypoint plus selected components | top-level composer contract | duplicate summaries, missing adapter notes, role-language gaps | Walk session start, planning, audit, and contribution triggers. | Slice03 standalone component |
| S-14 agent-adapter role-language | CC, CDC, Claude, Codex, fresh context | adapter notes or local component notes | component loaded outside composer | role-language text in SKILL/methodology/PM/ledger | Actor understands CDC, CC, Claude, Codex, verifier, and operator language. | agent-adapter plus local component notes | central adapter versus local notes | role-language clarity failure, repeated notes drift | Search components for role language and compare adapter coverage. | Slice03 standalone component |
| S-15 component contract source/package | Maintainer or release checker | future component contract | Arc04 architecture or Arc05 implementation planning | Project01 gates, README package guidance, package checks | Component contract names source paths, package behavior, support assets, and gates. | path-contract constraints plus component contract | Project01 package/release gate first | package-local link breakage, zip-root drift | Verify package-local path assumptions and `make check-package-paths` coverage. | Slice04 synthesis and Arc05 |
| S-16 ontology critique functional question | Operator and Arc04 planner | Arc02 boundary method or future ontology guide | architecture boundary disputed | boundary and naming findings, decision register | Team knows whether ontology critique is reusable workflow or project-specific analysis. | ontology critique material plus Arc02 inputs | operator decision register | missing functional goal, overfit new component | Test whether a fresh session can use the method outside Project02. | Slice04 synthesis and Arc04 |

## Current Monolith Questions

- Does the current monolith let each actor reach the right guide without
  overloading context?
- Which current monolith routes hide dependency order or role-language clarity?
- Which current monolith surfaces blur source/package mode?

## Standalone Component Questions

- Can posture, ledger, audit, coverage, delegation, and contribution scenarios
  be completed from standalone component load sets?
- Which support assets are mandatory for standalone use?
- Which standalone component names mislead the actor?

## Composed Component Questions

- Which combinations are common enough to route from the top-level composer?
- Does composed use reduce or increase context cost?
- Which dependency order must be enforced to avoid improper merge or split
  failure?

This scenario matrix is analytical and non-final. It provides functional
question rows for Arc03; it does not accept final architecture.
