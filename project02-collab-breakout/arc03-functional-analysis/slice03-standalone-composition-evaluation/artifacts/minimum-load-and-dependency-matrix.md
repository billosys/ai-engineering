# Minimum Load And Dependency Matrix

```yaml
project: project02-collab-breakout
arc: arc03-functional-analysis
slice: slice03-standalone-composition-evaluation
status: proposed-done
architecture-decisions: none
matrix-status: analytical, non-final, not accepted architecture
```

## Input Contract

This matrix compares candidate load shapes against the verified Slice01
scenario matrix and the verified Slice02 current-workflow baseline, including
the load-path friction register, functional-deficiency register, and
source/package role-language notes. Arc02 conceptual model, boundary and naming
findings, and operator decision rows are used only as candidate-boundary
evidence.

## Comparative Matrix

| Load shape | Minimum useful load | Context cost | Dependency order | Over-rich risk | Over-thin risk | Routing friction | Current-workflow baseline |
|------------|---------------------|--------------|------------------|----------------|----------------|------------------|---------------------------|
| current monolith | Top-level `SKILL.md` plus routed framework file: posture/methodology for substantial session start; PM plus ledger for planning close; audit/coverage/delegation/contribution as needed. | High for narrow triggers; medium for broad session start. | Composer before selected guide; posture before methodology; PM before PM split files; ledger before ledgered close. | High: LPF-01 and FD-01 show `/collaboration-framework` can load more than audit, coverage, delegation, contribution, or PM-only work needs. | Low when composer is used; the monolith carries adapters and source/package language. | Medium: the route is visible, but the actor must know which document owns the workflow. | LPF-01, LPF-03, LPF-08, LPF-09, FD-01, FD-10 |
| standalone component | One focused component entrypoint plus required support assets: ledger alone for row closure; delegation alone plus adapter note; contribution style plus ticket template; coverage plus repo tooling; audit plus domain skills and artifact-home adapter. | Low to medium when the trigger is narrow. | Component-specific. Ledger before PM close evidence; style before ticket template; repo tooling before coverage examples; domain skills before audit findings. | Low if component contract is scoped tightly. | Medium-high: LPF-02 and FD-02 show direct guide loading can miss role-language, package mode, support assets, or evidence semantics. | Low when a direct entrypoint exists; high if the user must know source file names. | LPF-02, LPF-05, LPF-06, LPF-10, FD-02, FD-05, FD-06, FD-08, FD-12 |
| composed component | Small set of components loaded in dependency order: posture+methodology; PM+ledger; contribution style+template; audit+domain skills+ledger terms; coverage+repo tooling; agent-adapter+local notes. | Medium, with better fit than monolith for multi-discipline tasks. | Explicit dependency edges must be visible at entry: posture before methodology; ledger evidence before PM close; style before template; central adapter before local role terms. | Medium if composed bundles become static mini-monoliths. | Medium if composition is just a list without dependency direction. | Medium: better than direct file guessing, but requires component contract links and package-local paths. | LPF-03, LPF-04, LPF-05, LPF-09, FD-06, FD-07, FD-11 |
| top-level composer combination | Thin framework-entrypoint plus selected component routes. Minimum floor: role adapter, posture/process summary, and explicit load-when table; detailed mechanics stay in components. | Low to medium if kept thin; high if it retains current monolith summaries. | Composer identifies trigger, then loads selected components and required support assets in declared order. | High if Arc04 accepts a rich monolith or duplicates component mechanics. | Medium if the composer omits dependency and role-language adapter notes. | Low for discovery, medium for package/link maintenance after breakout. | LPF-01, LPF-02, LPF-08, LPF-09, FD-01, FD-02, FD-10, FD-12 |

## Scenario-Specific Minimum Loads

| Scenario | Candidate minimum useful load | Required dependency order | Context cost | Main risk | Baseline rows |
|----------|-------------------------------|---------------------------|--------------|-----------|---------------|
| S-08 coverage | coverage-hardening component, repository Makefile/CI/test commands, domain test idioms if language-specific | Discover repo tooling before adapting examples; fix failures/warnings before declaring threshold met. | Medium | Underfit examples or Claude/Cargo naming hide general use. | LPF-10, FD-08 |
| S-09 delegation | delegation-policy plus local Codex/Claude role note | Classify thinking versus lookup before any subagent dispatch. | Low | Direct load may miss role-language if title/audience stays Claude-only. | LPF-02, LPF-09, RLF-06 |
| S-10 contribution | contribution-style-and-voice plus contribution-ticket-template | Read style before template; evidence and confidence before public claims. | Medium-low | Template-only use becomes formulaic and over-thin. | LPF-05, FD-06 |
| S-11 posture/methodology | posture plus methodology; top-level composer can route both | Posture before methodology; methodology routes specialized guides. | Medium | Merge recreates monolith; split without dependency makes methodology procedural. | FD-01, BNF-04, D-01, D-02 |
| S-12 PM/ledger | project-management family plus ledger-verification-protocol | PM lifecycle route, then ledger evidence semantics before close disposition. | Medium-high | Duplicated close semantics or inherited composition. | LPF-03, LPF-04, LPF-11, FD-07 |
| S-13 composer | framework-entrypoint plus selected components | Trigger classification before load; support assets travel with selected component. | Low to medium | Duplicate summaries, missing adapter notes, or package path drift. | LPF-01, LPF-08, FD-10, FD-12 |
| S-14 role adapter | agent-adapter plus local component notes | Central translation first; local component note only where terms appear. | Low to medium | Central-only adapter missed in standalone mode; local-only adapter drift. | LPF-09, FD-11, RLF-08 |

## Matrix Conclusion

The current monolith is safe for discovery and broad session start, but
over-rich for focused operational triggers. Standalone components lower
context cost when a direct load moment exists, but they must carry dependency
links, support assets, role-language clarity, and source/package mode
constraints. Composed components are the best fit for PM+ledger,
posture/methodology, and contribution style+template because the workflow
needs more than one owner. A top-level composer remains useful only if it is
thin enough to avoid restoring the current monolith's load cost while still
declaring dependency order and package/release gate expectations.

This comparison is analytical and non-final. It supplies Slice04 and Arc04
inputs; it does not accept architecture.
