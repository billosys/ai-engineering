# Functional Deficiency Register

```yaml
project: project02-collab-breakout
arc: arc03-functional-analysis
slice: slice02-current-workflow-evaluation
status: proposed-done
architecture-decisions: none
register-status: analytical, non-final, not accepted architecture
scope: current monolith only
```

## Input Contract

This register consumes the verified Slice01 functional-analysis method,
usage-surface inventory, scenario matrix, Arc03 input register, and the Arc02
close evidence as its input contract. It records current-monolith functional
deficiency candidates and routes them forward. It does not decide final
breakout architecture.

## Deficiency Rows

| ID | Deficiency class | Current surface | Functional deficiency or risk | Evidence basis | Downstream route |
|----|------------------|-----------------|-------------------------------|----------------|------------------|
| FD-01 | over-rich load path | Session start through `/collaboration-framework` | The current monolith gives a strong safety floor, but for narrow triggers it loads posture, methodology summary, and routing before the actor can reach a small operational guide. This is a context-cost deficiency to test, not an architecture decision. | `SKILL.md:90`, `SKILL.md:326`; S-02. | Slice03 compares standalone/composed load sets; Arc04 decides composer contract. |
| FD-02 | over-thin load path, hidden dependency | Direct guide loading without composer | A guide loaded directly can be too thin if it omits role-language clarity, source/package mode, evidence semantics, or support asset dependencies. | `SKILL.md:327`, `docs/CONTRIBUTION-STYLE.md:3`, `templates/CONTRIBUTION-TICKET.md:3`; LPF-02. | Slice03 standalone evaluation; Slice04 synthesis. |
| FD-03 | missing entrypoint, missing functional goal | Reusable ontology critique or boundary-review workflow | Arc02 found ontology critique useful, but the current source framework has no user-facing entrypoint for repeatable component-boundary review. This is an under-served current surface and could be overfit if promoted too eagerly. | Arc02 BNF-10 and operator decision D-12; Slice01 AFQ-12. | Slice03 tests demand; Arc04 decides whether to route to Project03, add a component, or keep project-specific. |
| FD-04 | missing functional goal, under-served maintenance | Post-breakout component maintenance | The current monolith has source/package checks, version histories, and package lists, but no component-maintenance contract because components do not exist yet. Future component work needs explicit owner, source paths, package behavior, support assets, dependency links, and gates. | Arc02 BNF-09; operator decision D-10; `Makefile:86`, `Makefile:216`; `package-path-exceptions.tsv:8`. | Slice04 functional synthesis; Arc04 contract; Arc05 implementation plan. |
| FD-05 | output-location conflict | Code audit output defaults | Audit output defaults to `workbench/`, while planning slices now expect durable outputs under slice-local `artifacts/`. The current behavior works only when the slice prompt or operator explicitly overrides audit output placement. | `docs/CODE-AUDIT.md:134`, `docs/CODE-AUDIT.md:220`; PM artifact-home rules; S-07. | Slice03 audit scenario; Arc04/Arc05 output-location contract. |
| FD-06 | hidden dependency | Contribution guide and ticket template | The contribution template depends on the style guide for voice and calibrated honesty. Loaded alone, the template can preserve shape while losing judgment. | `docs/CONTRIBUTION-STYLE.md:33`, `docs/CONTRIBUTION-STYLE.md:43`, `templates/CONTRIBUTION-TICKET.md:3`, `templates/CONTRIBUTION-TICKET.md:133`. | Slice03 contribution scenario; Arc04 support-asset packaging. |
| FD-07 | inherited composition risk | Slice close and arc close | The current close process explicitly forbids inherited composition, but the risk remains functional because it requires reviewer discipline at arc and project scale. A parent close that trusts child closure without demonstration would be a serious failure. | `templates/LEDGER-DISCIPLINE.md:142`, `templates/LEDGER-DISCIPLINE.md:302`; S-06. | Slice04 synthesis; Arc04/Arc05 gate wording. |
| FD-08 | underfit behavior | Coverage hardening | The coverage guide has Codex notes and can be adapted, but its title and worked examples remain Claude Code/Rust/Cargo-shaped. That underfit can reduce discoverability for non-Rust and non-Claude workflows. | `docs/CLAUDE-CODE-COVERAGE.md:1`, `docs/CLAUDE-CODE-COVERAGE.md:7`, `docs/CLAUDE-CODE-COVERAGE.md:12`; Arc02 BNF-01 and BNF-13. | Slice03 coverage standalone scenario; Arc04 naming and generality decision. |
| FD-09 | overfit behavior | PM support files as possible standalone components | PM split files are useful as focused guides, but the current evidence does not show every split file has its own direct load moment. Treating examples, confirmation, or provenance as top-level components may overfit the current file split. | Arc02 BNF-08 and BNF-15; `docs/PROJECT-MANAGEMENT.md:35`; `docs/pm/02-canonical-planning-worktree.md:136`. | Slice03 PM family evaluation; Arc04 granularity decision. |
| FD-10 | source/package contract gap | Future component contracts | Source/package behavior is documented for the current monolith and CCDP, but there is no per-component contract yet for package-local links, zip roots, release surface behavior, or package/release gate obligations. | `README.md:278`, `README.md:342`, `Makefile:216`, `protocols/ccdp/README.md:3`; Arc02 BNF-14. | Slice04 synthesis; Arc04 component contract; Arc05 package validation plan. |
| FD-11 | role-language clarity gap | Audit and older Claude-era surfaces | Role-language adapters exist, but not uniformly. `docs/CODE-AUDIT.md` still points at `CLAUDE.md`; a fresh-context Codex actor loading audit directly may miss AGENTS-era or CDC/CC role translations. | `docs/CODE-AUDIT.md:25`; `docs/AI-ENGINEERING-METHODOLOGY.md:17`; `docs/SUBAGENT-DELEGATION-POLICY.md:76`. | Slice03 agent-adapter scenario; Arc04 adapter ownership. |
| FD-12 | missing entrypoint | Package reader wanting only one operational discipline | Today the installable package is the collaboration-framework monolith. A package reader who wants only ledger, PM, audit, coverage, delegation, or contribution has no accepted standalone package entrypoint yet. This is the functional reason for Slice03 comparison, not proof of the final split. | `README.md:152`, `README.md:287`, `Makefile:80`, `Makefile:86`; project DoD. | Slice03 standalone/composed evaluation; Arc04 architecture. |

## Register Summary

The current monolith is operationally usable. The functional deficiencies are
mostly about load granularity, dependency visibility, adapter consistency, and
future component contract gaps rather than absent core guidance.

The strongest missing functional goals are component maintenance, reusable
ontology critique, and per-component source/package contracts. The strongest
under-served current surfaces are direct audit-as-Codex loading, coverage
outside Rust/Cargo examples, and package-reader use of a single operational
discipline.

This register is analytical and non-final. It evaluates the current monolith
only, does not decide final component boundaries, and leaves architecture
deferred to Arc04 after operator acceptance.
