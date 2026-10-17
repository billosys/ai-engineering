# Project14 — Fennel

project: project14-fennel
status: closed
plan-version: 1.2
depends-on: []
blocks: []
related: [knowledge/rust, https://git.sr.ht/~technomancy/fennel-lang.org]

## Definition of done

Deliver a usable Fennel authoring/review skill at `knowledge/fennel/SKILL.md`,
with focused guides patterned after Rust's numbered, strength-labelled rules,
paired examples, summary tables, sources and task routing. Preserve the pertinent
upstream documentation history under `knowledge/fennel/sources/md/`, together
with licensing, pinned provenance and a commit map. Verify the installed formatter,
exercise examples, and wire the skill into Make packaging and the public library.
Source-preserving integration is part of delivery; publication and installation
of this skill into profiles are outside this request.

## Roadmap and first usable increment

One coherent slice, `slice01-fennel-guidelines/`, delivers the complete skill and
package. No arc wrapper: source acquisition, teaching, routing and packaging are
parts of this single useful increment. Inputs are the website's pinned Fennel
submodule and the existing Rust skill/package conventions. Source inspection is
the routine inspection explicitly requested by the Operator, not a new inquiry.

## Workflow and authority

Operator explicitly selected the One-Contributor Workflow on 2026-10-17:
Sofie owns planning, implementation, checks, corrections and completion without
further Operator supervision or approval. The Operator also explicitly authorized
subagents for checking and required a final unbiased audit in a completely fresh
context with full purpose/source prompting. This overrides agent-coordination's
normal lookup-only boundary for this audit. The primary context retains edit and
finding-disposition judgment. No fictional CDC/CC handoffs or CDC verification
files are required; preserve the initial cc-prompt.md as the pre-transition
assignment record. Complete the fresh audit and address its findings before close.

The Operator authorized the seven-part implementation request and confirmed this
planning layout. Preserve unrelated `knowledge/lfe/` work. History import requires
an unrelated-history, non-squashed merge; rewritten upstream commits retain original
authorship, dates and messages, with a map back to original identities. Record the
CC-generated import commit with the standing trailers. No push is requested.

## Status

Slice01 closed. Source baseline: main `4e635bb3`; existing untracked `knowledge/lfe/`
is unrelated. Project ledger is closed: implementation, fresh audit and all corrections are complete. Final source commit: `c9d98a3ec3d0a24c30a18431d7aeaa13f6451872`.

## Source-lineage clarification — 2026-10-17

`git log --follow` shows `api.md` originated in `README.md`. Retain README
as the language overview and API-history ancestor, within the Operator-authorized
useful supplemental docs. All other selected paths have no predecessor rename.

## Version History

- v1.0 — 2026-10-17: Operator requested the Fennel skill and confirmed this planning home.
- v1.1 — 2026-10-17: Operator explicitly selected single-contributor execution,
  authorized checking subagents and required a fresh final audit plus corrections;
  removed the earlier future-CDC/Operator gate in favor of this explicit contract.

- v1.2 — 2026-10-17: Slice01 delivered, fresh audit corrected and rechecked;
  source, package and evidence compose into the project DoD. No successor work.
