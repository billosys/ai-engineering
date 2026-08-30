# Standalone Scenario Evaluation

```yaml
project: project02-collab-breakout
arc: arc03-functional-analysis
slice: slice03-standalone-composition-evaluation
status: proposed-done
architecture-decisions: none
evaluation-status: analytical, non-final, not accepted architecture
```

## Input Contract

This artifact consumes the verified Slice01 and Slice02 inputs:

- Slice01 CDC verification:
  `../slice01-usage-surface-instrument/cdc-verification.md`
- Slice01 functional-analysis method:
  `../slice01-usage-surface-instrument/artifacts/functional-analysis-method.md`
- Slice01 scenario matrix:
  `../slice01-usage-surface-instrument/artifacts/scenario-matrix.md`
- Slice02 CDC verification:
  `../slice02-current-workflow-evaluation/cdc-verification.md`
- Slice02 current-workflow evaluation:
  `../slice02-current-workflow-evaluation/artifacts/current-workflow-evaluation.md`
- Slice02 load-path friction register:
  `../slice02-current-workflow-evaluation/artifacts/load-path-friction-register.md`
- Slice02 functional-deficiency register:
  `../slice02-current-workflow-evaluation/artifacts/functional-deficiency-register.md`
- Slice02 source/package role-language notes:
  `../slice02-current-workflow-evaluation/artifacts/source-package-role-language-notes.md`

It also consumes the Arc02 conceptual model, boundary and naming findings, and
operator decision register as candidate-boundary evidence only:

- `../../arc02-conceptual-analysis/slice03-ontology-decision-synthesis/artifacts/arc02-conceptual-model.md`
- `../../arc02-conceptual-analysis/slice03-ontology-decision-synthesis/artifacts/boundary-and-naming-findings.md`
- `../../arc02-conceptual-analysis/slice03-ontology-decision-synthesis/artifacts/arc04-operator-decision-register.md`

The current source checkout was used read-only as grounding. This evaluation
does not decide final component names, source moves, package paths, or accepted
architecture. Architecture deferred to Arc04 after Arc03 synthesis and operator
acceptance.

## Scenario Rows

| Scenario ID | Actor | Entrypoint | Trigger | Inputs | Expected outcome | Load set | Dependencies | Friction signals | Evidence collected | Downstream owner |
|-------------|-------|------------|---------|--------|------------------|----------|--------------|------------------|--------------------|------------------|
| S-08 coverage standalone component | CC/test actor | `docs/CLAUDE-CODE-COVERAGE.md`, as candidate `coverage-hardening-discipline` | Coverage threshold requested | Repository tooling, tests, coverage tool, language skill when relevant, Slice02 LPF-10 and FD-08 | Actor can adapt coverage, lint, format, and test commands to the repository and drive a hard threshold without hiding failures. | coverage-hardening guide plus repo-specific tooling evidence; optional domain test idioms. | Source/package mode first; repository Makefile or CI commands before examples; language/domain test idioms after repo discovery. | Strong direct load moment, but current name is Claude/Cargo-shaped. Standalone use can be underfit outside Rust unless the adapter note is visible. | Slice01 scenario matrix S-08; Slice02 LPF-10 and FD-08; source `docs/CLAUDE-CODE-COVERAGE.md` notes for Codex, 95% threshold, warning treatment, and command adaptation. | Slice04 synthesis; Arc04 naming and generality decision; Arc05 package entrypoint and verification gates. |
| S-09 delegation standalone component | Active LLM | `docs/SUBAGENT-DELEGATION-POLICY.md`, as candidate `delegation-policy` | Task invites subagents or parallel work | Current task, tool context, loaded project instructions, Slice02 LPF-02 and RLF-06 | Main context keeps thinking/edit/review judgment; lookup work can be parallelized and independently inspected. | delegation-policy only, plus short local Codex/role note when loaded outside composer. | Role-language clarity before applying to Codex/Claude surfaces; project instructions may install the policy persistently. | Low to medium context cost. The policy is narrow and direct, but the title/audience are still Claude-oriented; standalone package needs a local adapter note. | Slice01 scenario matrix S-09; Slice02 source/package role-language notes RLF-06; source `docs/SUBAGENT-DELEGATION-POLICY.md` policy block and Codex section. | Slice04 synthesis; Arc04 adapter ownership; Arc05 compatibility wording. |
| S-10 contribution standalone component | Human or LLM drafter | `docs/CONTRIBUTION-STYLE.md` plus `templates/CONTRIBUTION-TICKET.md`, as candidate `contribution-guidance` | Upstream bug, feature, doc, or question ticket | Issue evidence, source line refs, maintainer context, Slice02 LPF-05 and FD-06 | Ticket is calibrated, specific, respectful of maintainer ownership, and cheap for the maintainer to act on. | contribution-style-and-voice plus contribution-ticket-template support asset. | Style before template; posture/methodology can support calibrated honesty but are not mandatory for a narrow ticket draft if style is loaded. | Standalone style guide works; template-only use is over-thin because it preserves shape while losing voice and calibration. | Slice01 scenario matrix S-10; Slice02 LPF-05 and FD-06; source `docs/CONTRIBUTION-STYLE.md` voice rules and `templates/CONTRIBUTION-TICKET.md` "read style first" dependency. | Slice04 synthesis; Arc04 support-asset packaging; Arc05 package-local template link checks. |
| S-11 posture/methodology composed component | Operator and LLM | `docs/AI-CONSTITUTION-SUPPLEMENT.md` plus `docs/AI-ENGINEERING-METHODOLOGY.md` | Substantial session start, planning, or quality-floor reset | Constitution supplement, methodology, top-level composer, Slice02 FD-01 and Arc02 D-01/D-02 | Actor gets peer frame, structural-pull countermeasures, SDLC/process rigor, and routing to operational disciplines without loading every specialized guide. | posture plus methodology as a minimum composed load; top-level composer can route this combination. | Posture before methodology; methodology routes to PM, ledger, audit, coverage, delegation, and contribution rather than owning full mechanics. | Real functional load path for substantial work. Risk is improper merge if methodology carries all operational detail, or over-thin process if posture is dropped. | Slice01 scenario matrix S-11; Arc02 conceptual model posture/methodology dependency; operator decisions D-01 and D-02; source notes for Codex in both documents. | Slice04 synthesis; Arc04 posture/methodology boundary and composer contract. |

## Candidate Direct Load Moment Tests

| Direct load moment | Minimum useful load | Functional load path | Standalone result | Support asset / dependency notes | Slice02 baseline |
|--------------------|---------------------|----------------------|-------------------|----------------------------------|------------------|
| coverage-hardening | `docs/CLAUDE-CODE-COVERAGE.md` plus repository tooling and language test idioms | Yes: triggered by an explicit hard coverage threshold. | Adjust. Keep as standalone candidate, but rename or wrap with surface-neutral entry language. | Requires repo-specific commands; examples are not hidden requirements. | LPF-10, FD-08 |
| delegation-policy | `docs/SUBAGENT-DELEGATION-POLICY.md` plus local role adapter | Yes: triggered when a task invites subagents or parallel lookup. | Go. Narrow standalone operational component has a clear reason to load. | Local Codex/Claude/CC/CDC note prevents role-language drift. | LPF-02, RLF-06 |
| contribution-guidance | `docs/CONTRIBUTION-STYLE.md` plus `templates/CONTRIBUTION-TICKET.md` | Yes: triggered by upstream ticket drafting. | Go, with template bundled as support asset. | contribution-ticket-template must not become a standalone component by itself. | LPF-05, FD-06 |
| posture | `docs/AI-CONSTITUTION-SUPPLEMENT.md` | Yes: substantial session start and posture repair. | Go as a standalone candidate or named dependency, pending Arc04. | Methodology depends on posture; top-level composer may summarize but should not hide it. | FD-01, BNF-11 |
| methodology | `docs/AI-ENGINEERING-METHODOLOGY.md` plus posture when not already loaded | Yes: planning how work will be done and quality-floor calibration. | Adjust. Core component should own pillars, SDLC, and routing, not duplicate all operational guides. | Routes to project-management, ledger-verification, code-audit, coverage-hardening, delegation-policy, and contribution-guidance. | LPF-01, FD-01 |
| project-management | `docs/PROJECT-MANAGEMENT.md` plus focused `docs/pm/` guide(s) | Yes: planning or closing project/arc/slice work. | Go as a PM family; defer package granularity. | PM owns lifecycle routing, layout, open/close/bubble-up, and plan-change discipline. | LPF-03, FD-09 |
| ledger-verification | `templates/LEDGER-DISCIPLINE.md` | Yes: any ledgered unit at slice, arc, or project scale. | Go. Strong standalone candidate. | Ledger owns evidence semantics and row closure; PM close guides depend on it. | LPF-04, FD-07 |
| code-audit | `docs/CODE-AUDIT.md` plus README, project instructions, detected domain skills | Yes: whole-repo audit requested. | Adjust. Standalone audit is strong but needs output-location and Codex/AGENTS adapter behavior. | Default workbench outputs conflict with ledgered slice artifacts unless prompt/operator overrides. | LPF-06, FD-05, FD-11 |
| agent-adapter | Central adapter note plus local component notes where role terms appear | Partial: triggered when a component is loaded outside the composer and mentions CDC/CC/Claude/Codex/operator. | Adjust/defer as adapter, not proven standalone component. | Central-only adapter is too easy to miss; local-only notes can drift. | LPF-09, RLF-08 |
| ontology critique | Arc02 boundary method or Project03 concept-card boundary aid | Weak: current repeatable workflow is project-planning evidence, not a source framework entrypoint. | Defer. Treat as missing/under-served workflow, not accepted component. | Could route to Project03 concept-card method or an Arc04 architecture checklist. | FD-03, BNF-10 |

## Standalone Findings

- Strong standalone functional load paths exist for ledger-verification,
  delegation-policy, contribution-guidance with its support asset, coverage
  hardening, project-management as a family, and code-audit with adapters.
- The coverage path is functionally real but naming and examples are underfit;
  Arc04 should correct the surface without erasing provenance.
- PM should not be split by current file boundaries alone. The functional
  evidence supports a project-management family with internal focused guides;
  Arc04 should decide whether any family member also receives its own package
  entrypoint.
- Ledger and PM have opposite ownership responsibilities: ledger-verification
  owns evidence terms and row closure, while project-management owns lifecycle
  routing, artifact homes, and bubble-up.
- Contribution ticket drafting has a direct load moment, but the
  contribution-ticket-template is a support asset. Template-only standalone use
  is over-thin.
- Agent-adapter behavior is functionally required for standalone components,
  but current evidence supports it as an adapter pattern rather than a
  free-standing user workflow.
- Ontology critique remains a weak functional load path. It should be routed
  to Slice04 and Arc04 as an unresolved architecture question, not promoted
  solely because Arc02 used it successfully.

All findings remain analytical and non-final.
