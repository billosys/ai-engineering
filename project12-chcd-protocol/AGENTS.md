# Project12 — CHCD Protocol

Operator-confirmed planning layout (2026-10-09): branch `planning`, worktree
`.worktrees/planning`, project directory `project12-chcd-protocol/`. Use the
repository's canonical project/arc/slice layout; durable slice-produced
artifacts belong in the owning slice's `artifacts/`. Implementation belongs in
the source checkout, not this worktree.

Read `project-plan.md` and `ledger.md` before extending the project. Arc01 and
its Slice01 are open; use the slice's current assignment record and preserved
`cc-prompt.md` for the bounded evidence assignment. Source implementation is
not authorized by that assignment.
Default Two-Contributor Workflow: Sofie handles CDC planning with the Operator;
CC is not yet assigned. No CRC or Expedited Mode is selected.

The public name is **CHCD Protocol**, expanded as **Composable Heterogeneous
Cognition Dispatch Protocol**, pronounced **Check-Dee Protocol**. `chcdp` is
the agreed compact source-directory and URL segment. Do not turn that path
spelling into the normal prose name.

Preserve `protocols/ccdp/` as the historical 0.2 baseline, including the review
iterations through 0.2m. Develop the successor under `protocols/chcdp/` from a
verified copy. Published redirects belong under `site/`, outside the frozen
historical tree.

Operator decision: CHCD 0.3 continues to support legacy CCDP names, including
`org.ccdp.*` and other inventoried protocol identifiers, with deprecation
notices announcing removal in 0.4. The exact successor spellings, alias rules,
and notice mechanism require design; do not silently break 0.3 compatibility
or treat 0.4 removal as permission to delete historical documents or redirects.
