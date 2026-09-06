# Arc03 Slice03 Closing Report: Evidence, Validation, And Verification

```yaml
project: project05-concept-card-skill
arc: arc03-concept-cards-skill-core
slice: slice03-evidence-validation-verification
status: cc-proposed-done
reported-by: Codex CC
reported-on: 2026-09-06
source-commit: 3fbfcef25145fb47fd2b67d8dd847e9b4cb9d28c
planning-commit: the commit containing this report and the slice ledger
evidence-strength: attested
```

## Outcome

Implemented evidence lifecycle and validation/verification guides, made guides
05/08 live, and cleaned the authorized caller wording in guides 01–04. The
entrypoint now identifies guides 01–05 and 08 as live and 06/07/09/10 as future.
Nested `metadata.version` and sibling history advance to `1.2.0`.

All eight ledger rows are CC proposed-done with attested evidence. Independent
CDC verification is pending. These are source-guidance changes; no validation
or verification against a real corpus was performed.

## Source Scope

Implementation checkout: `/Users/oubiwann/lab/billosys/ai-engineering`, branch
`main`, opening commit `79664fc`, clean before edits. Source commit:
`3fbfcef25145fb47fd2b67d8dd847e9b4cb9d28c`.

Exactly these eight files were staged, inspected and committed explicitly:

```text
knowledge/concept-cards/SKILL.md
knowledge/concept-cards/version-history.md
knowledge/concept-cards/guides/01-load-contract.md
knowledge/concept-cards/guides/02-operator-workflow.md
knowledge/concept-cards/guides/03-extraction.md
knowledge/concept-cards/guides/04-re-extraction-preservation.md
knowledge/concept-cards/guides/05-evidence-lifecycle.md
knowledge/concept-cards/guides/08-validation-verification.md
```

The commit has 463 insertions and 37 deletions, with both required co-author
trailers. Source status is clean after commit and the skill matches HEAD.
No unrelated source work was present or included.

Guides 01–04 changed only in live-route/availability passages: guide 01's footer;
guide 02's introduction, preservation route, result-route paragraph and ending;
guide 03's review/handoff routes; guide 04's handoff routes. Their extraction,
preservation and foundational construct procedures remain otherwise unchanged.
The temporary entrypoint qualification about stale callers was removed.

## Design Evidence

Read the current source AGENTS.md, Project05 project/Arc03/slice plans and
ledgers, predecessor CDC verification and current source guides. Revisited the
accepted conceptual model and its detailed evidence-lifecycle input:

- `artifacts/project03-concept-card-method/arc03-conceptual-model/slice04-model-synthesis/artifacts/v40-conceptual-model.md`;
- `artifacts/project03-concept-card-method/arc03-conceptual-model/slice02-evidence-lifecycle/artifacts/v40-evidence-lifecycle-model.md`.

The accepted synthesis governs the earlier model input. Historical architecture
and source-edit sequence already inspected in this conversation remain evidence;
current Project05 names, layout, source versioning and slice scope govern.

Guide 05 (183 lines) implements a procedure for identifying assertion/revision
and source support, choosing attachment scope, assessing warrant with explicit
rationale, recording extraction confidence independently, retaining insufficient/
partial/conflicting/unassessed/stale evidence, and maintaining separate result
and lifecycle records. It covers card, claim, support relationship, edge, CQ
coverage assertion and extraction-run attachment points. Both operating modes
and handoff limits are explicit.

Guide 08 (203 lines) implements scoped structural validation and semantic
verification procedures. Its actor/evidence model distinguishes same-context
assistant checks, independent CDC/fresh-context review, operator reports,
direct human review, tool/process evidence and unavailable inputs. Each result
records actor, method, target, evidence, scope, outcome, caveats and revision
identity. It describes result/state applicability after changes and explicit
limits on independence, whole-card conclusions and admission.

Review of the authored guidance confirmed:

- Source locator, source span, source support, bibliography/preparation evidence
  and extraction-run provenance are not interchangeable.
- Evidence grade assesses warrant for the actual assertion/use, with rubric
  identity if established and explicit rationale. Extraction confidence
  describes the extraction act and does not determine the grade.
- Partial or conflicting evidence is retained at its actual attachment scope;
  a card/run summary cannot confer a common grade on all contained claims.
- A result is the durable check observation; state summarizes applicable
  results on a particular revision. Old results remain historical evidence
  rather than automatically transferring to revised content.
- Structural conformance does not establish semantic warrant; one supported
  claim does not verify an entire card; extraction success or worker agreement
  does not establish independent verification; validation is not admission.
- Fresh context, CDC title, human participation and tool success are each
  insufficient by themselves to prove independence or a complete verdict.
- Reconciliation and memory admission remain separate, with their detailed
  guides future. No canonical schema, grade enum, runtime or executable
  validator is introduced.

These are source and model-consistency observations, not live-corpus results.

## Validation Results

Commands ran in the implementation checkout unless stated otherwise. All
results are doer-attested, not independently reproduced.

| Check | Observed result |
| --- | --- |
| `scripts/check-skill-description.sh knowledge/concept-cards/SKILL.md` | Exit 0, no output. |
| `python3 /Users/oubiwann/.codex/skills/.system/skill-creator/scripts/quick_validate.py knowledge/concept-cards` | Exit 0, `Skill is valid!`. |
| `git diff --check` | Exit 0. |
| `make check-skills` | Exit 0, `>> all skill descriptions within limit`. |
| `make check-skill-versions` | Exit 0; source phase: 22 source skills, 0 packages, 0 errors; final phase: 22 source skills, 20 existing packages, 0 errors. |
| Owned-tree inventory/mode checks | Exactly eight non-executable Markdown files: entrypoint, sibling history and guides 01–05/08. No support directories or future guides. |
| Local Markdown links and anchors | Eight files, 48 local links/anchors, zero errors; inline-code future routes excluded. |
| Version/history inspection | Nested string `1.2.0`, matching sibling history; no top-level version or guide-local histories/current-version prose. |
| Whitespace/newlines | All eight files have final newlines and no trailing whitespace. |
| Scope exclusions | No `knowledge/concept-card-method/` or `knowledge/source-preparation/`; no package/support/runtime edits or live-corpus checking. |
| Staged diff | `git diff --cached --check` exits 0; exact eight paths inspected; working contents match staging. |
| Post-commit status / HEAD comparison | Clean source; `git diff --exit-code HEAD -- knowledge/concept-cards` exits 0. |

The version gate rebuilt ignored existing package archives. It does not build
a concept-cards package; that remains Arc05 work. No archive was committed,
and no package surface changed, so package-path checks were not run.

Executable ledger content verifiers returned:

```text
S3-1: exit 0; 10 stdout lines; 0 stderr lines
S3-2: exit 0; 13 stdout lines; 0 stderr lines
S3-3: exit 0; 24 stdout lines; 0 stderr lines
S3-4: exit 0; 32 stdout lines; 0 stderr lines
S3-5: exit 0; 73 stdout lines; 0 stderr lines
S3-6: exit 0; 29 stdout lines; 0 stderr lines
```

S3-8's five component gates passed as listed above; the version gate ran
separately because it writes ignored build output. Direct content and diff
inspection supplements the keyword verifiers. A whole-source future-route
search confirmed that only guides 06/07/09/10 and later support/package work
remain unavailable; historical version-history entries retain their past tense.

Local link reproduction, from the implementation root:

```python
from pathlib import Path
import re

root = Path("knowledge/concept-cards")
count = 0
for path in root.rglob("*.md"):
    text = re.sub(r"`[^`\n]*`", "", path.read_text())
    for dest in re.findall(r"\]\(([^)\s]+)\)", text):
        name, _, anchor = dest.partition("#")
        target = (path.parent / name).resolve() if name else path
        assert target.is_file(), (path, dest)
        if anchor:
            headings = re.findall(r"^#+ (.+)$", target.read_text(), re.M)
            slugs = [re.sub(r"[^a-z0-9 -]", "", h.lower()).replace(" ", "-")
                     for h in headings]
            assert anchor in slugs, (path, dest)
        count += 1
print(count, "local links/anchors; 0 errors")
```

The procedure covers this source tree's relative Markdown links and heading
anchors, not a general Markdown grammar or a shipped concept-card validator.

## Row Walk

| Row | CC proposed status | Evidence |
| --- | --- | --- |
| S3-1 | done | Guides 05 and 08 exist and are linked Live in the entrypoint; their procedures cross-link relevant existing guides. |
| S3-2 | done | Metadata version 1.2.0 and sibling history agree; whole-tree inspection and repository version gate pass. |
| S3-3 | done | All authorized stale caller passages cleaned; entrypoint and guides 01–04 consistently identify 01–05/08 live and 06/07/09/10 future. |
| S3-4 | done | Guide 05 implements warrant/confidence separation, support/span distinctions, all attachment scopes, evidence gaps, lifecycle separation, both modes and handoff. |
| S3-5 | done | Guide 08 implements structural and semantic checks, actor/evidence boundaries, scoped result/state records, false-upgrade prevention, both modes and handoff. |
| S3-6 | done | Only future references to remaining guides, Arc04 support and Arc05 packaging; no schema, executable validator, runtime or live-corpus behavior added. |
| S3-7 | done | Exact eight-file source scope, clean source before/after, no excluded roots or other source edits. |
| S3-8 | done | All five gates exit 0; all 48 local links/anchors resolve across eight files. |

Rows: 8. CC proposed-done: 8. Deferred: 0. No-op: 0.
Independently verified: 0.

## Planning Scope And Artifact Inventory

Planning worktree: `/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning`,
branch `planning`, opening commit `2796082`. Project05 was clean before edits.
Fifteen unrelated untracked Project06 paths were present at opening; their
content hashes were captured as a baseline. Project06 work continued during
this slice and remains excluded. CC did not edit or stage those files.

Only this slice's `ledger.md` and `closing-report.md` are changed. No parent
plan/ledger or `cdc-verification.md` is authored by CC. No separate durable
planning-analysis artifacts were produced, matching the plan. The eight source
files are implementation output; this report and ledger are durable CC evidence.
Temporary drafts/logs and ignored existing package output are not deliverables.

## Bubble-Up To Arc03

The assigned evidence, validation and verification capability is delivered
subject to CDC reproduction. Slice02's bounded caller cleanup is resolved,
including removal of the temporary entrypoint qualification. No additional
arc-plan scope, sequence or capability change is proposed.

Scope as specified matches scope delivered: two new guides, entrypoint/history
update, route-only changes to four existing guides, all eight ledger criteria
and required gates, and explicit support/package/runtime exclusions. No row
was dropped, weakened or deferred. Independent CDC review is the next closure
step; this report does not close Arc03 or Project05 or open another slice.
