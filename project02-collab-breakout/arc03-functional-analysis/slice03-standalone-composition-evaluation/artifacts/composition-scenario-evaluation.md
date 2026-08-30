# Composition Scenario Evaluation

```yaml
project: project02-collab-breakout
arc: arc03-functional-analysis
slice: slice03-standalone-composition-evaluation
status: proposed-done
architecture-decisions: none
evaluation-status: analytical, non-final, not accepted architecture
```

## Input Contract

This artifact consumes the verified Slice01 scenario matrix and
functional-analysis method, the Slice02 current-workflow evaluation,
load-path friction, functional-deficiency, and source/package role-language
baseline, plus the Arc02 conceptual model, boundary and naming findings, and
operator decision register as candidate-boundary evidence.

The composed component rows below are non-final. They test load behavior and
dependency order; they do not accept final architecture.

## Scenario Rows

| Scenario ID | Actor | Entrypoint | Trigger | Inputs | Expected outcome | Load set | Dependencies | Friction signals | Evidence collected | Downstream owner |
|-------------|-------|------------|---------|--------|------------------|----------|--------------|------------------|--------------------|------------------|
| S-12 PM and ledger composed component | CC/CDC | PM close plus ledger discipline | Ledgered planning or close | PM wayfinder, PM close guides, ledger discipline, slice plan, ledger, close report, artifacts | Actor distinguishes lifecycle routing from evidence semantics and closes without inherited-composition or silent-drop errors. | project-management family plus ledger-verification-protocol. | PM wayfinder before focused PM docs; ledger-verification before row evidence; slice close before arc/project composition. | Medium-high context cost remains, but composition is correct. Over-thin risk appears if ledger terms are summarized inside PM without loading the ledger owner. | Slice01 S-12; Slice02 LPF-03, LPF-04, LPF-11, FD-07; source PM close files and `templates/LEDGER-DISCIPLINE.md`. | Slice04 synthesis; Arc04 dependency direction; Arc05 package-local links between PM and ledger. |
| S-13 top-level composer combination | Human or LLM | top-level composer / framework-entrypoint | Task needs several disciplines | Arc02 conceptual model, current `SKILL.md` routing table, Slice02 current-workflow baseline | Composer routes to the minimum useful load set without restoring monolith load cost. | framework-entrypoint plus selected components: posture, methodology, PM, ledger, audit, coverage, delegation, or contribution as triggered. | Composer must preserve a small posture/process floor, then route; it must not own every component's full mechanics. | Main risk is duplicate summaries or missing adapter notes. Too rich recreates FD-01; too thin loses role-language and dependency order. | Slice01 S-13; Slice02 LPF-01, LPF-02, LPF-09, FD-01, FD-02; source `SKILL.md` routing table. | Slice04 synthesis; Arc04 top-level composer contract; Arc05 README/SKILL packaging plan. |
| S-14 agent-adapter role-language | CC, CDC, Claude, Codex, fresh context | Agent-adapter plus local component notes | Component loaded outside composer | Role-language text in SKILL, methodology, PM, ledger, audit, coverage, delegation, and AGENTS | Actor understands CDC, CC, Claude, Codex, verifier, reviewer, and operator language in standalone and composed modes. | agent-adapter plus short local notes in components that mention role terms. | Central adapter should define canonical translations; local notes should point to or summarize only what standalone use requires. | Central-only adapter is over-thin for direct component loading; repeated full adapter text risks drift. Audit is the weakest current surface. | Slice01 S-14; Slice02 LPF-09, FD-11, RLF-01 through RLF-08; source notes in methodology, PM, ledger, coverage, delegation, and audit. | Slice04 synthesis; Arc04 adapter ownership; Arc05 drift-control checks. |

## Additional Composed Flows

| Flow | Composed component | Minimum useful load | Dependency order | Result | Baseline |
|------|--------------------|---------------------|------------------|--------|----------|
| Posture/methodology | collaborative posture plus engineering methodology | `docs/AI-CONSTITUTION-SUPPLEMENT.md` and `docs/AI-ENGINEERING-METHODOLOGY.md` | Posture before methodology; methodology routes to operational guides. | Go/adjust. The combination is foundational for substantial work, but methodology should not absorb specialized mechanics. | FD-01, BNF-04, D-01, D-02 |
| Contribution style plus ticket template | contribution guidance plus template support asset | `docs/CONTRIBUTION-STYLE.md` and `templates/CONTRIBUTION-TICKET.md` | Style before template. | Go. This is a real composed flow; the template travels with the style component. | LPF-05, FD-06, D-09 |
| Audit plus domain skills plus evidence language | code-audit discipline plus domain skills and ledger evidence semantics | `docs/CODE-AUDIT.md`, project README/instructions, detected domain skills, ledger terms when reporting evidence | Audit map before findings; domain skills before language audit; diagnosis before fixes. | Adjust. Strong workflow, but output-location adapter must respect slice-local artifacts when audit happens inside planning. | LPF-06, FD-05, FD-11 |
| Coverage plus repo tooling | coverage-hardening plus repo-specific commands and language idioms | coverage guide, Makefile/CI/test tooling, domain test skill where relevant | Repository tooling before example commands; warnings and failures before coverage target closure. | Adjust. Real workflow, but source-neutral naming and examples are needed. | LPF-10, FD-08, D-07 |
| PM/ledger with planning instructions | PM family plus ledger plus AGENTS source/planning split | `docs/PROJECT-MANAGEMENT.md`, selected `docs/pm/`, `templates/LEDGER-DISCIPLINE.md`, relevant AGENTS | Planning worktree and artifact home before writing; ledger before row close; source checkout scope before source inspection. | Go. This composed component preserves the current close discipline if dependency links remain explicit. | LPF-03, LPF-04, RLF-02, RLF-03 |

## Composition Findings

- PM+ledger composition is necessary and should be expressed as a dependency
  edge, not by copying ledger semantics into PM. This protects evidence terms
  and keeps close mechanics discoverable.
- The top-level composer should remain useful as a first entrypoint, but its
  minimum role is routing plus a compact posture/process floor. A rich
  monolith would preserve the current over-rich load path.
- Role-language adaptation is a cross-cutting composed behavior. The strongest
  current pattern is central adapter guidance plus short local notes wherever
  a standalone component can be loaded without the composer.
- Contribution style plus ticket template is a composed workflow with clear
  support-asset ownership; splitting the template into its own component would
  weaken the functional outcome.
- Audit and coverage share quality-floor language, but their workflows differ:
  audit is diagnosis-only, while coverage hardening edits tests/code to reach
  a threshold. Current evidence supports sibling operational components more
  than a broad quality-family merge.
- Package and release gates compose with every accepted component contract;
  they should not be treated as optional implementation cleanup.

All composition results are analytical. Final component composition belongs to
Arc04 after Arc03 closes and the operator accepts an architecture direction.
