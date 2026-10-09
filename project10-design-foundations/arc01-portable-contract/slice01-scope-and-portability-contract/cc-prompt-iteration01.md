# CC iteration01 — Correct source membership and evidence receipts

Issued 2026-10-09. Project10 / Arc01 / Slice01. Current assignment:
`arc01-portable-contract/slice01-scope-and-portability-contract/cc-prompt-iteration01.md`.

## Outcome and governing state

Resolve the two findings in [CDC verification](cdc-verification.md). Return
proposed-done through the Operator to Sofie (CDC). The initial prompt remains
binding except for this narrower mutation allowlist. Do not accept or close the
slice, open Slice02, or change source/design decisions.

Locate SOURCE and PLANNING with `git worktree list`; use explicit working
directories. SOURCE remains `/Users/oubiwann/lab/billosys/ai-engineering`, pin
`dffa504e851b03b8e4746f1941068e4cc850b612`. PLANNING is its planning worktree.
PROJECT is `project10-design-foundations`; SLICE is this directory. Reviewed CC
commit is `0e0c1d0a6b9f451a9328036b0af035e5405cafa8`; audit pin remains
`795ac75b7d02536e0e95252457ac3282cd17d8d8`. Record the actual commit containing
this issued iteration. Do not substitute the original assignment commit for it.

Read the current project/arc/slice plans and ledgers, initial prompt, this
iteration, CDC verification, and the three reports being corrected completely.
Follow standing collaboration-framework instructions. Recheck Git status and
pinned input bytes. Untracked SOURCE `knowledge/lfe/` and PLANNING
`project12-chcd-protocol/` are unrelated: leave them untouched. Unrelated HEAD
movement is acceptable only with unchanged required inputs documented; changed
baseline, assignment or contradictory scope goes to CDC before dependent work.

## 1. Make source populations losslessly selectable

In `artifacts/source-readiness.md`, retain the human-readable availability table
but replace the erroneous exact-predicate claim. Add one fenced JSON array with
exactly eight records, one per observed raw source/author pair, using these keys:

- `source_raw`: the actual string in index `source_fields_raw.source[0]`.
- `authors_raw`: the actual string in index `source_fields_raw.authors[0]`.
- `card_count`: its derived integer population.

Generate JSON from the index rather than transcribing normalized display names.
JSON encoding must preserve the raw value after JSON parsing, including YAML
quote characters and literal backslashes. Example for Brown:

```json
{"source_raw":"\"More Meaningful Typography\"","authors_raw":"\"Tim Brown\"","card_count":10}
```

For each parsed group `g`, the exact expression over parsed index row `r` is:

```python
r["source_fields_raw"]["source"][0] == g["source_raw"] and r["source_fields_raw"]["authors"][0] == g["authors_raw"]
```

Associate each raw pair unambiguously with its existing table row. Fix the later
Butterick reference to the old table predicate. This JSON is slice evidence,
not a new card or global source schema. Do not normalize, rewrite or regenerate
the card-source index or baseline manifest.

Execute a direct check that reads the JSON block back from the report and applies
its predicates to all 233 index objects. Require eight distinct pairs, actual
counts equal declared counts, a 233-card union, and exactly one group for every
card. Preserve the observed 112/19/19/37/12/10/13/11 populations by identity, not
table position. Include a negative control: comparison with unquoted display
titles/authors yields zero matches, demonstrating why the old predicate fails.
Do not weaken literal equality or decode YAML escapes to make it pass.

## 2. Complete intake and replay evidence truthfully

Read the complete required Project09 audit, including its final line 187, from
the pinned bytes. Record the new actual read extent and pin in an iteration01
section of `artifacts/execution-notes.md`. Retain the original 1–98/99–186
receipt, explicitly identifying its incomplete recorded coverage. A fresh read
resolves the gap; do not silently rewrite the receipt as if previously observed.

Retain compact executable query text and actual results from the corrective
pass directly in execution notes. Cover the original prompt's population/hash
and literal-field/body comparisons, raw source grouping and corrected membership,
mapped-content searches (including all 37 Butterick section assertions), and
preservation/output-integrity checks. The existing prose algorithms may remain
as explanation. Shell/Python snippets must state working directories, pins,
population and exclusions; retain ambiguous/unmatched locator results rather
than presenting a search hit as semantic verification. No source acquisition,
reusable script suite, browser checks or package build is requested.

Update `closing-report.md` with an attributed iteration01 addendum or clear
retained initial/current sections: exact assignments and commits, two finding
dispositions, actual checks and failed/blocked/unrun attempts, per-row outcomes,
source-gap ownership and bubble-up findings. Preserve the initial proposed-done
history. Update ledger evidence notes to link the corrective sections, leaving
all seven rows open. Do not claim independent acceptance. The contract remains a
proposal and all-card semantic review remains later assigned work.

## Allowlist and validation

Only four paths relative to SLICE may change:

- `artifacts/source-readiness.md`
- `artifacts/execution-notes.md`
- `closing-report.md`
- `ledger.md` (evidence/disposition notes only; preserve criteria/statuses).

Everything else is immutable, including manifest, index, portable contract,
author reconnaissance, plans, both issued prompts, CDC verification, Project09,
source and packages. Stop and report any necessary expansion before mutation.

Run corrected membership checks against the report's actual JSON; replay the
required direct queries; check local links/anchors, final newlines and planning
`git diff --check`; compare immutable slice files with the reviewed CC commit,
source/audit bytes with their pins, and exact changed paths with this allowlist.
Keep source gaps and semantic limits visible. No new acceptance criterion is
introduced: this corrects S01-01/03/07 evidence under the issued contract.

Commit only these four paths with an explicit path list and `git commit --only`,
preserving unrelated staged work and both required trailers:

```text
Co-authored-by: Codex <noreply@openai.com>
Co-authored-by: Billo AI <ai-engineering@billo.systems>
```

Return the planning commit, finding/row dispositions, exact replay counts,
limits and any bubble-up. State proposed-done pending CDC. No parent acceptance,
source repair or next-slice opening is authorized here.
