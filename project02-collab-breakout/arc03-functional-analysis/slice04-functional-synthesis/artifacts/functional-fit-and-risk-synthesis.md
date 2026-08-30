# Functional Fit And Risk Synthesis

```yaml
project: project02-collab-breakout
arc: arc03-functional-analysis
slice: slice04-functional-synthesis
status: proposed-done
risk-status: analytical, non-final, not accepted architecture
```

## Input Contract

This synthesis consumes verified Arc03 Slice01, Slice02, and Slice03 evidence:
Slice01 CDC verification and scenario matrix; Slice02 CDC verification,
`current-workflow` baseline, `load-path friction` register,
`functional-deficiency` register, and `source/package role-language` notes;
Slice03 CDC verification, `minimum-load` matrix, and `dependency-adapter`
findings. It also consumes closed Arc02 conceptual model, boundary and naming
findings, operator decision register, and closing report.

The findings consolidate Slice02 `LPF-*`, `FD-*`, `SPR-*`, and `RLF-*` rows
with Slice03 standalone and composition results.

## Fit Summary

Arc03 finds a real functional case for breaking the current monolith into a
thin composer plus narrower direct-load and composed paths. The strongest
functional fit appears where the workflow has a clear trigger, a small
minimum useful load, explicit dependencies, and limited role-language adapter
needs. The weakest fit appears where the candidate is really shared ontology,
a support asset, a constraint, or a package/release gate.

The main risk is not "split or do not split." The risk is splitting without
preserving dependency order, source/package behavior, package-local links, zip
root assumptions, release surface guidance, role-language clarity, and
`make check-package-paths` gate behavior from Project01 and
`project01-harmonise-paths`.

## Consolidated Risks

| ID | Risk category | Consolidated finding | Evidence basis | Arc04 posture |
|----|---------------|----------------------|----------------|---------------|
| FR-01 | Over-rich context-load | The current composer is over-rich for narrow workflows. This preserves a reliable floor but raises context cost at session start and simple execution moments. | LPF-01, FD-01, S-01, S-13. | Adjust: retain composer but reduce it. |
| FR-02 | Over-thin direct load | Standalone components can become over-thin when they hide prerequisite semantics, support assets, or adapter notes. | LPF-02, FD-02, S-08 through S-11. | Go only where dependency edge and support asset travel are explicit. |
| FR-03 | Unclear handoff | PM planning and close workflows depend on ledger evidence language. If PM and ledger split without ownership direction, row closure and bubble-up can drift. | LPF-03, LPF-04, FD-07, S-04, S-05, S-12. | Go: ledger owns evidence; PM owns lifecycle. |
| FR-04 | Routing friction | Contribution, audit, coverage, PM, and package guidance currently require readers to know where the route lives. | LPF-05, LPF-07, FD-06, FD-09. | Adjust component entrypoints and support asset links. |
| FR-05 | Missing functional goal | Ontology critique and component-maintenance discipline are important, but Arc03 does not prove them as direct standalone user workflows. | FD-03, FD-04, S-11, Arc02 D-10 and D-12. | Defer component status; require architecture checklist placement. |
| FR-06 | Under-served audit output path | Audit is strong, but older workbench-oriented output rules conflict with the current slice-local `artifacts/` convention. | LPF-06, FD-05, RLF-04. | Adjust audit component before source implementation. |
| FR-07 | Coverage underfit | Coverage has a real functional workflow but language and examples are underfit for a general framework component. | LPF-10, FD-08, BNF-01, BNF-13. | Adjust naming and examples. |
| FR-08 | Source/package risk | Source-clone, generated skill zip, unzipped installed skill, and CCDP package workflows are all valid but different. Breakout can break package-local links and reader expectations. | LPF-08, FD-10, SPR-01, SPR-02, SPR-03, SPR-04, SPR-06, SPR-07. | Go only with per-component source/package and package/release gate fields. |
| FR-09 | Role-language risk | CDC/CC/Codex/Claude/human language is mostly clear at the top level, weaker in audit and older specialized surfaces, and risky after standalone breakout. | LPF-09, FD-11, RLF-01 through RLF-08, S-14. | Go with central adapter plus short local notes. |
| FR-10 | Package/release risk | Component extraction can break README routing, `SKILL.md` routing, Makefile package lists, zip root behavior, package-local links, CCDP separation, and release surface checks. | SPR-03, SPR-04, SPR-05, SPR-06, SPR-07, Project01. | Go with central gate plus component contract fields. |
| FR-11 | Inherited composition failure mode | A closed child slice or loaded child guide does not automatically close parent-scale work; parent closure must recombine evidence. | FD-07, LPF-11, PM close guidance, ledger discipline. | Go: make composition closure explicit in PM and ledger relationship. |

## Deficiency Carry-Forward

The following functional deficiency themes should be carried into Arc04:

- `FD-01` and `LPF-01`: session-start context-load and context cost caused by
  an over-rich composer.
- `FD-02` and `LPF-02`: over-thin direct guide risk when dependencies are only
  discoverable through the monolith.
- `FD-03` and `FD-04`: missing functional goal for ontology critique and
  component-maintenance discipline.
- `FD-05` and `LPF-06`: audit output-location conflict between old workbench
  guidance and slice-local artifacts.
- `FD-06` and `LPF-05`: contribution style and ticket template are too easy
  to separate accidentally.
- `FD-08` and `LPF-10`: coverage underfit for non-Claude and non-Cargo
  workflows.
- `FD-10`, `SPR-01` through `SPR-07`: source/package risk and component
  contract gaps.
- `FD-11`, `RLF-01` through `RLF-08`: role-language risk after direct-load
  component extraction.

## Package And Source Constraints

Project01 and `project01-harmonise-paths` constraints are functional risks,
not just release housekeeping. Arc04 should require every accepted component
contract to name:

- source paths and packaged paths;
- package-local entrypoint links;
- support assets and templates that must travel with the component;
- dependency edges and adapter requirements;
- generated zip root behavior;
- README and `SKILL.md` release surface updates;
- CCDP separation when protocol packaging is nearby but not part of the
  installable skill component;
- `make check-package-paths` and any additional package/release gate commands.

## Risk Verdict

No remediation slice is required on the current CC-attested evidence before
Arc03 formal close, assuming CDC verifies Slice04. The risks are specific
enough for Arc04 architecture design: they identify what to split, what to
compose, what to defer, and what must become component contract or
package/release gate language.
