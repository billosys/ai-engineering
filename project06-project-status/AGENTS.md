# Project06 worktree routing

Operator override confirmed 2026-09-06. These project-specific routes supersede
the inherited normal direct-to-main implementation route for Project06.

- Planning home: `/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning/project06-project-status/`,
  branch `planning`. Plans, ledgers, prompts and evidence stay here.
- Implementation home: `/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/project-status-feature`,
  branch `feature/project-status`. Read current source skills/guides here; make
  source and packaging changes, run tests and package gates, and generate build
  outputs here. Main has concurrent work and is not this project's write target.
- CC starts in the planning directory but must explicitly set the feature
  worktree as the working directory for implementation commands. Check its
  branch and working state first. If missing or on another branch, report the
  mismatch instead of falling back to main or changing branches automatically.
- Read `project-plan.md`, then the relevant arc and slice plans/ledgers. The
  current project-management route, relative to the feature worktree, is
  `knowledge/project-management/guides/README.md`; inherited `docs/` skill
  routes are historical.
- Routing does not expand slice scope: the current contract-design slice still
  produces planning artifacts. Later implementation slices target the feature
  worktree. Keep independent verification separate from author attestation.
- Preserve unrelated work. When commits are requested, enumerate exact paths,
  commit source in the feature worktree and planning in the planning worktree,
  and include both required repository co-author trailers. Integration into
  main is a separate operation, not implicit in this routing change.

## Expedited Mode — operator decision, 2026-09-10

Expedited Mode is enabled for Project06. Follow the project-management guides
README in the feature worktree. CC commits the exact files enumerated in each
prompt before CDC review; CDC commits scoped updates and reviews, closes when
evidence permits, and opens the next planned unit immediately after closure.
Preserve explicit approval gates and verification requirements. Give the
operator each CC prompt path as plain project-relative text in a code block.
This supersedes earlier instructions to wait for a separate commit request.
