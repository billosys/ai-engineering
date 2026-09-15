# Project08 Working Instructions

Planning lives on branch `planning` in `.worktrees/planning`, under
`project08-concept-card-metadata/`. The operator selected this name and the
existing project/arc/slice layout on 2026-09-12. Durable slice-produced artifacts
belong in the owning slice's `artifacts/` directory.

Read `project-plan.md`, then the active arc and slice plans and their ledgers.
Use the source checkout's `knowledge/collaboration-framework/SKILL.md`,
`knowledge/project-management/SKILL.md` and its `guides/README.md`, plus
`knowledge/work-verification/`. These current routes supersede the historical
`docs/PROJECT-MANAGEMENT.md` and `docs/pm/` routes in the planning root instructions.

Source work belongs in the main checkout on `main`; verify worktree and dirty
state before each run. Preserve unrelated work. When committing, enumerate
actual files in the commit command; never commit a whole project directory or
use `git commit -a`. Include both repository-required co-author trailers.

Operator tooling preference (2026-09-12): use Fennel for new scripts and Rust
or LFE for substantial tooling. Do not introduce Ruby scripts or default to
Python. Use established parsers/libraries; a Fennel wrapper around Ruby or
Python does not meet this preference. Existing repository tools retain their
own scope; this does not authorize rewriting unrelated tools.

Slice01 commit hold history (operator, 2026-09-12): the initial hold was released
after the operator's no-Ruby inspection; CC committed the packet as e2ea1e68.
That commit permission does not establish CDC closure. Future scoped commits
follow the explicit-file convention above. No Ruby source, including renamed
or embedded copies, may enter Git history. Retain honest provenance of earlier
results without restoring the removed Ruby helper.

The live concept-cards baseline is 4.8.1. The operator intends this work to ship
in 4.9.x and to remain on 4.x. Re-read `metadata.version` before source edits;
do not reuse historical 1.x labels, reset the sequence, or automatically advance
to 4.10 or 5.x. Investigate compatibility conflicts and make them visible in
planning before implementation. Document-extraction retains its own sequence.

Arc04 permits an uncapped number of bounded slices for real extraction,
comparison, metadata/body refinements, and fresh reruns. Multiple separate CC
extraction sessions are mandatory. A slice's five-iteration limit is a sizing
signal, not an arc-wide research limit or permission to abandon a quality goal.

Treat the original five-arc roadmap and the added Arc06 as a working hypothesis. Add needed slices and revise
plans with finding IDs and dated histories. No scope reduction, premature
closeout, or transfer of failed quality requirements to follow-on work without
an explicit operator decision. Passing package gates cannot close the UAT work.

CC attestations remain proposed-done until independent verification. Operator
acceptance of card quality is a separate project closure requirement. Candidate
retention, semantic verification, and memory admission remain distinct.

## Operator-Approved Semantic Transition (2026-09-14)

Project-level assessment and transition evidence live in `artifacts/`, per
the operator's request. Source and historical evidence remain read-only.
Arc06 is next in dependency order, ahead of the unchanged Arc02-05 identifiers.
Read the project plan and transition register before following historical
Arc01 prompts. Arc01 is closed-with-transfers, not fully delivered; its
original incomplete criteria remain mandatory Arc06 acceptance obligations.

Use semantic families ordered by capability importance, with exact coverage,
shared evidence plus explicit member roles/exceptions, and targeted research.
Retain small iterative packets when needed. The prior effort is a valued
foundation, not discarded work. Expedited Mode resumes, including scoped
CC/CDC commits and the plain project-relative next-prompt path at handoff.

## Schema/Spec Checkpoint (2026-09-14)

Before finalizing the metadata architecture or implementing it as the accepted
contract, discuss the schemas and creation of a specification with the operator.
See project-plan.md and artifacts/schema-and-spec-discussion-agenda.md; P-15 is
the tracked gate. Arc06 research and approved evidence remediation may proceed,
but neither adopts a schema, spec format or future requiredness policy.
