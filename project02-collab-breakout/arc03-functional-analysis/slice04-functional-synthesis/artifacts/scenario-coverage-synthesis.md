# Scenario Coverage Synthesis

```yaml
project: project02-collab-breakout
arc: arc03-functional-analysis
slice: slice04-functional-synthesis
status: proposed-done
coverage-status: analytical, non-final, not accepted architecture
```

## Input Contract

This coverage synthesis consumes Slice01 CDC verification and the Slice01
`scenario matrix`, Slice02 CDC verification and `current-workflow` baseline,
Slice02 `load-path friction`, `functional-deficiency`, and `source/package
role-language` registers, Slice03 CDC verification and the `minimum-load` and
`dependency-adapter` artifacts, plus the closed Arc02 `conceptual model` and
operator decision evidence.

The rows below cover S-01 through S-14 from the Slice01 scenario matrix. S-15
and S-16 remain useful inputs for package contracts and ontology critique, but
the Slice04 exit criteria require scenario coverage for S-01 through S-14.

## Scenario Coverage

| Scenario | Load shape | Coverage finding | Arc04 input |
|----------|------------|------------------|-------------|
| S-01 | Current monolith | Broad `/collaboration-framework` session start is well covered. It gives posture, methodology, PM, ledger, audit, coverage, delegation, and contribution discovery at the cost of high context cost. | Keep a top-level composer, but make it thinner. |
| S-02 | Current monolith | Direct source-clone reading is covered through README, `SKILL.md`, docs, and templates, but source/package orientation is distributed. | Preserve source-clone and package-reader adapter guidance. |
| S-03 | Current monolith | Packaged skill reading is viable because generated zip roots and package-local links are already guarded by Project01 checks, but per-component contracts do not yet exist. | Add package/release gate fields to component contracts. |
| S-04 | Current monolith | Planning work is covered by the PM wayfinder and planning docs, but the user must load PM plus ledger semantics in the right order. | Treat PM as a family and ledger as an explicit dependency edge. |
| S-05 | Current monolith | Slice close and bubble-up are covered, including silent-drop and artifact inventory expectations, but hidden ledger dependencies can make close work over-thin if PM is loaded alone. | Encode PM-close uses-ledger direction. |
| S-06 | Current monolith | Code audit and review are covered as diagnosis-first workflows, with evidence discipline and domain-skill routing. The output-location convention needs update from old workbench language. | Classify audit as strong direct load with adjustment. |
| S-07 | Current monolith | Coverage hardening is covered but examples and naming remain surface-specific and Cargo-shaped. | Adjust naming or add an adapter before accepting a package surface. |
| S-08 | Standalone | Ledger-verification, delegation-policy, contribution-guidance plus support asset, and code-audit show clear standalone value. | Strong direct-load candidates. |
| S-09 | Standalone | Project-management has standalone demand, but its internal files operate as a family rather than independent top-level components. | Decide one PM package with internal guides versus a PM family package model. |
| S-10 | Standalone | Methodology-only and posture-only loading is useful but dependency order matters; methodology without posture can become procedural, and posture alone is not execution guidance. | Keep posture-to-methodology dependency explicit. |
| S-11 | Standalone | Agent-adapter and ontology critique are not proven standalone user workflows. Agent-adapter behavior is required, but as adapter infrastructure; ontology critique remains an unresolved method question. | Use adapter treatment for role language; defer ontology component status. |
| S-12 | Composed | PM and ledger composition is necessary for planning, slice close, arc close, and project close. Composed loading reduces over-thin risk if ledger owns evidence and PM owns lifecycle. | Go for explicit PM/ledger dependency edge. |
| S-13 | Top-level composer | A thin top-level composer is supported as a discovery and session-start route. The current rich composer is too costly for narrow tasks, while a too-thin index would lose the safety floor. | Adjust composer contract: compact posture/process floor plus routes. |
| S-14 | Composed | Role-language adapter composition is required across standalone components, especially where CDC/CC/Codex/Claude terminology appears. Central-only adapter creates direct-load ambiguity; fully repeated adapter text creates drift. | Go with central adapter plus short local notes and drift controls. |

## Load Shape Findings

Current monolith:

- Strong for ambiguous session start, broad human orientation, and discovery.
- Weak for narrow direct-load workflows because it carries high context cost.
- Main risks: over-rich session start, hidden dependency order, and
  distributed source/package or role-language guidance.

Standalone:

- Strong when the trigger is narrow and the minimum useful load is coherent:
  ledger, delegation, contribution with template, and audit.
- Plausible when the workflow is real but naming or examples need adjustment:
  coverage, methodology, posture, and PM family.
- Weak where the concept is shared ontology, adapter behavior, or a support
  asset rather than a user-facing workflow.

Composed:

- Strong where dependency order is real: PM plus ledger, posture plus
  methodology, contribution style plus ticket template, audit plus domain
  skills, and coverage plus repository tooling.
- The composition model must state which component owns semantics, lifecycle,
  support assets, adapters, constraints, and package/release gates.

Top-level composer:

- A top-level composer remains functionally necessary for discovery, session
  start, combination workflow routing, and human orientation.
- It should not remain a rich monolith after breakout.
- It should not become only a list of links; it needs a compact posture and
  process floor plus explicit routes.

## Coverage Verdict

Arc03 has scenario coverage for S-01 through S-14. The evidence is sufficient
for Arc04 architecture work after CDC verifies Slice04, provided Arc04 treats
this synthesis as non-final and keeps component boundary, package path, and
operator decision selection open.
