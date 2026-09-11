# CC Prompt: Arc07 Slice03 Feedback-Driven Skill Refinement

You are CC working in Expedited Mode on Project05 Arc07 Slice03.

## Required Reading

Read these files before editing:

1. `project05-concept-card-skill/project-plan.md`
2. `project05-concept-card-skill/arc07-real-corpus-uat-and-feedback/arc-plan.md`
3. `project05-concept-card-skill/arc07-real-corpus-uat-and-feedback/ledger.md`
4. `project05-concept-card-skill/arc07-real-corpus-uat-and-feedback/slice03-feedback-driven-skill-refinement/slice-plan.md`
5. `project05-concept-card-skill/arc07-real-corpus-uat-and-feedback/slice03-feedback-driven-skill-refinement/ledger.md`
6. Slice02 close set:
   - `project05-concept-card-skill/arc07-real-corpus-uat-and-feedback/slice02-pilot-markdown-preparation-and-card-extraction/closing-report.md`
   - `project05-concept-card-skill/arc07-real-corpus-uat-and-feedback/slice02-pilot-markdown-preparation-and-card-extraction/cdc-verification.md`
   - `project05-concept-card-skill/arc07-real-corpus-uat-and-feedback/slice02-pilot-markdown-preparation-and-card-extraction/artifacts/friction-log.md`
   - `project05-concept-card-skill/arc07-real-corpus-uat-and-feedback/slice02-pilot-markdown-preparation-and-card-extraction/artifacts/pilot-review-packet.md`
7. The current source skill files for `document-extraction` and `concept-cards`
   that are relevant to each finding. Historical artifacts are evidence, not
   current authority.

## Task

Disposition every Slice02 finding F-1 through F-7 as one of:

- accepted refinement;
- checked no-op; or
- follow-on boundary with re-entry condition.

Make narrow source changes only when the current source skill text does not
already cover the finding. If source changes are made, update the owning skill
version metadata and sibling `version-history.md` according to the repository
skill-version contract.

Write durable Slice03 artifacts under:

```text
project05-concept-card-skill/arc07-real-corpus-uat-and-feedback/slice03-feedback-driven-skill-refinement/artifacts/
```

Required artifacts:

- `finding-disposition.md`
- `source-change-summary.md`, if source files change
- `no-op-and-follow-on-decisions.md`
- `validation-evidence.md`

Then update the Slice03 ledger and write `closing-report.md`.

## Guardrails

- Do not accept, revise, reject, or admit any Slice02 candidate card on the
  operator's behalf.
- Do not perform expanded corpus generation; that is Slice04 unless the
  operator changes the plan.
- Do not implement graph/RAG/MCP, vector storage, memory runtime, retrieval
  evaluation, or memory admission in this slice.
- Do not treat a Slice02 finding as an accepted defect until you compare it
  against the current source guidance.
- Preserve unrelated work in both source and planning worktrees.

## Validation

Run only the gates that match your actual changes, and record them in
`validation-evidence.md`:

- `git diff --check`
- `make check-skills` if any `SKILL.md` metadata or description changes
- `make check-skill-versions` if any skill version or history changes
- `make check-package-paths` if packaged links, support files, or package
  contents change
- targeted Markdown path/link checks for changed Markdown when no broader
  package gate applies
- source and planning `git status --short --untracked-files=all`

## Commit Discipline

Use explicit file names in commit commands. If source and planning both change,
use separate commits for source changes and planning closeout. Include the
required co-author trailers in assistant-authored commits.

Close with a concise report naming source commit(s), planning commit, changed
files, gates run, and any remaining CDC/operator review needs.
