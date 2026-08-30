# Load Path Friction Register

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

This register consumes the Slice01 functional-analysis method,
usage-surface inventory, scenario matrix, Arc03 input register, Slice01 CDC
verification, and Arc02 close evidence as its input contract. It records
friction in Slice01 vocabulary and does not decide final breakout
architecture.

## Friction Rows

| ID | Category | Current load path | Context cost | Dependency order | Friction observed | Evidence basis | Downstream route |
|----|----------|-------------------|--------------|------------------|-------------------|----------------|------------------|
| LPF-01 | routing friction, over-rich | `/collaboration-framework` or top-level `SKILL.md` for session start | high | posture before methodology; routed guide after composer | The top-level skill is a strong current monolith entrypoint, but it carries substantial inline posture, practice, and routing. It can be too over-rich when the trigger is only audit, coverage, delegation, contribution, or PM mechanics. | `SKILL.md:69`, `SKILL.md:90`, `SKILL.md:326`; `docs/AI-ENGINEERING-METHODOLOGY.md:86`. | Slice03 load-set comparison; Arc04 composer contract. |
| LPF-02 | minimum useful load, over-thin risk | Direct operational guide load without top-level composer | medium | local guide may require posture, methodology, or ledger context | Some guides are self-contained enough for direct use, but standalone loading can become over-thin when role-language, evidence semantics, package mode, or support asset ownership is not present. | `SKILL.md:327`, `SKILL.md:328`, `SKILL.md:329`, `SKILL.md:330`, `SKILL.md:331`, `SKILL.md:332`. | Slice03 standalone component evaluation. |
| LPF-03 | dependency-order friction | `docs/PROJECT-MANAGEMENT.md` to `docs/pm/*.md` plus ledger discipline | medium-high | PM wayfinder before focused PM docs; ledger before ledgered close | PM routing is coherent but multi-hop. A fresh actor must know that PM owns lifecycle layout while ledger owns row evidence, then load both for close work. | `docs/PROJECT-MANAGEMENT.md:35`, `docs/PROJECT-MANAGEMENT.md:47`, `docs/pm/04-closing-slices.md:8`, `templates/LEDGER-DISCIPLINE.md:150`. | Slice03 PM family granularity; Slice04 synthesis. |
| LPF-04 | unclear handoff | PM close files and ledger discipline during slice/arc close | high | ledger evidence semantics before PM bubble-up | The handoff is explicit but mentally expensive: `closing-report.md` is PM lifecycle output, while the row statuses and evidence strengths come from ledger discipline. The current monolith depends on readers preserving that split. | `docs/pm/04-closing-slices.md:14`, `docs/pm/04-closing-slices.md:36`, `templates/LEDGER-DISCIPLINE.md:142`, `templates/LEDGER-DISCIPLINE.md:198`. | Slice03 ledger/PM composition; Arc04 dependency direction. |
| LPF-05 | support asset discovery | Contribution style plus ticket template | medium | style before template | The contribution workflow is good when both files are loaded, but the template is a support asset, not a sufficient standalone entrypoint. Template-only use can lose voice, calibration, and maintainer-ownership discipline. | `docs/CONTRIBUTION-STYLE.md:3`, `docs/CONTRIBUTION-STYLE.md:43`, `templates/CONTRIBUTION-TICKET.md:3`, `templates/CONTRIBUTION-TICKET.md:133`. | Slice03 contribution component/support-asset comparison; Arc04 packaging. |
| LPF-06 | support asset discovery, output-location conflict | Code audit prompt default output path | high | audit map before findings; domain skills before audit | The audit prompt has a strong multi-scale contract, but its default `workbench/` output conflicts with slice-local `artifacts/` when an audit is commissioned inside a ledgered slice. Current behavior relies on the prompt or operator override to choose the owning artifact home. | `docs/CODE-AUDIT.md:71`, `docs/CODE-AUDIT.md:134`, `docs/CODE-AUDIT.md:354`; Slice01 inventory US-11. | Slice03 audit standalone test; Arc04/Arc05 artifact contract. |
| LPF-07 | discoverability | README human orientation into framework and package commands | medium | README overview before Makefile/package details | README gives a good source-clone route, but the reader must move from overview to build/install to CCDP contrast to understand all modes. Discoverability is acceptable for humans but still broad. | `README.md:38`, `README.md:150`, `README.md:240`, `README.md:278`, `README.md:329`. | Slice04 source/package synthesis; Arc05 README planning. |
| LPF-08 | source/package ambiguity | README, Makefile, package-path check, CCDP README | medium | Project01 path gates before package claims | The current monolith controls source/package ambiguity with explicit documentation and `make check-package-paths`, but the rules live in several places. Package-local behavior is testable only after reading packaging files and exceptions. | `README.md:342`, `Makefile:216`, `scripts/check-package-paths:421`, `scripts/check-package-paths:451`, `package-path-exceptions.tsv:8`. | Slice04 and Arc05 package/release gate design. |
| LPF-09 | role-language clarity | Top-level SKILL, methodology, PM, ledger, AGENTS, and individual prompts | medium | adapter notes before Claude-era documents | Role-language clarity is strongest when the top-level adapter stack is loaded. Individual source docs are uneven: methodology, constitution, PM, ledger, coverage, and delegation have Codex notes; the audit prompt still names `CLAUDE.md` as its project instruction file. | `SKILL.md:69`, `docs/AI-ENGINEERING-METHODOLOGY.md:17`, `docs/PROJECT-MANAGEMENT.md:19`, `templates/LEDGER-DISCIPLINE.md:48`, `docs/CODE-AUDIT.md:25`, `docs/CLAUDE-CODE-COVERAGE.md:7`. | Slice03 agent-adapter scenario; Arc04 role-language ownership. |
| LPF-10 | underfit current load path | Coverage guide direct load | medium | repo tooling before examples | The coverage guide includes Codex notes that say the title is historical and examples are Rust/Cargo-shaped, but direct discoverability remains underfit for non-Rust or non-Claude workflows until the reader reaches those notes. | `docs/CLAUDE-CODE-COVERAGE.md:7`, `docs/CLAUDE-CODE-COVERAGE.md:10`, `docs/CLAUDE-CODE-COVERAGE.md:12`. | Slice03 coverage standalone evaluation; Arc04 naming. |
| LPF-11 | inherited composition risk | Arc close through child close reports plus arc ledger | high | children closed before composition demonstration | The current monolith names the inherited-composition failure mode and requires reproduced arc/project composition, but this remains a high-attention path because a reviewer must not accept child closure as proof of parent capability. | `templates/LEDGER-DISCIPLINE.md:142`, `templates/LEDGER-DISCIPLINE.md:302`, `templates/LEDGER-DISCIPLINE.md:344`. | Slice04 functional synthesis; Arc04 architecture gate language. |

## Register Summary

The current monolith has high discoverability as a single entrypoint and
reasonable source/package safeguards, but it pays for that with context cost
and cross-document dependency order. The central current-friction pattern is
not absence of guidance; it is that the minimum useful load set is difficult
to predict before the actor already knows which discipline owns the problem.

This register is analytical and non-final. It evaluates the current monolith
only, does not decide component boundaries, and leaves architecture deferred to
Arc04 after operator acceptance.
