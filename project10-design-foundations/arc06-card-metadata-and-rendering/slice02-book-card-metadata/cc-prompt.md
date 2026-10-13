# CC — Arc06 Slice02 all-card metadata normalization and rendering

Execute this **initial Slice02 implementation assignment** in the Two-Contributor
Workflow. Separate CC implements; CDC Sofie independently reviews via Operator
relay. Expedited Mode. Current [slice plan](slice-plan.md) and [six-row ledger](ledger.md)
govern. Parent [arc](../arc-plan.md) and [project](../../project-plan.md) retain
all release/semantic/fidelity gates. Slice01 is closed by its
[CDC I2 acceptance](../slice01-schema-and-field-inventory/cdc-verification.md#iteration02-independent-acceptance-and-slice-close--2026-10-13).
Planning issue is the commit introducing this prompt, parent `9934079aecc5a8c9bc2888c9a1b627fb4f3c55ff`.
Main input `4ccc6f6055743d8e8b53251d7e8852f04d1ed181`. This is source implementation, not another audit packet.

## Exact allowlist and baseline

The immutable Slice01 `artifacts/header-inventory.jsonl` SHA-256 is
`c7306e8a62291fa635e154463553fd990a9b12d91d70cb4403a0259f9e49dd5c`. Its ten pilot bytes and223
remaining bytes match current main. **Exactly223 source card paths** are selected
by the following complete query; it is the explicit path set for this assignment,
not permission to write an entire directory. Run it from planning and use its
returned array for helper writes and exact named-path commits:

```python
from pathlib import Path
import hashlib, json
p = Path('project10-design-foundations/arc06-card-metadata-and-rendering/'
         'slice01-schema-and-field-inventory/artifacts/header-inventory.jsonl')
b = p.read_bytes()
assert hashlib.sha256(b).hexdigest() == 'c7306e8a62291fa635e154463553fd990a9b12d91d70cb4403a0259f9e49dd5c'
rows = [json.loads(line) for line in b.splitlines()]
assert len(rows) == 233 and len({r['current']['path'] for r in rows}) == 233
assert all(type(r['pilot']) is bool for r in rows)
card_paths = sorted(r['current']['path'] for r in rows if not r['pilot'])
pilot_paths = sorted(r['current']['path'] for r in rows if r['pilot'])
assert len(card_paths) == 223 and len(pilot_paths) == 10
assert not set(card_paths) & set(pilot_paths)
source_paths = card_paths + ['knowledge/design/SKILL.md',
                             'knowledge/design/version-history.md']
assert len(source_paths) == 225
```

Only `source_paths` may change on main. Preserve ten pilots whole-byte exactly,
all guides, sources, packaging definitions and all other skills. Helper stays
SHA-256 `8ce4f31322aaa63389283b6a5ce3b41ddc184c73a971f55771997ee343a731ba`. Do not edit it.
Before writes, compare each233 source path/hash/typed/body record with inventory,
check tracked corpus exact union and current skill metadata/history1.0.4.
No silent repin after drift. An unrelated advance may be retained after proving
all relevant input bytes exact and recording its parent; selected design drift
or version conflict returns to CDC before affected writes. Preserve unrelated
worktrees/untracked work and any staged changes; no push/reset/install.

Exactly four CC planning write files in this slice: `artifacts/batch-record.md`,
`artifacts/batch-results.jsonl`, `ledger.md` (evidence/notes only; CDC statuses),
`closing-report.md`. Plans, prompts, Slice01 artifacts, prior reviews, original
manifest/index and other project/arc ledgers are protected.

## Binding recipe

1. Read the frozen contract and verify input coverage. Nonmutating actual helper
   `--check` all233 must show ten byte-idempotent pilots,223 differing outputs,
   90 exact sentinel changes across53 remaining cards and original complete
   metadata/body observations. Derive the observations; report discrepancies.
2. Use existing `ruby scripts/normalize-design-card-metadata.rb --write` with
   **only223 card_paths**, passed as an argument array from main. No glob or
   reimplemented serializer. Exactly `[[]]` in aliases/prerequisites/extends/
   contrasts_with becomes `[]`; other typed values remain exact. Empty versus
   null versus absent, nested populated lists,22 observed root fields/extensions,
   order/types, Unicode, confidence, references and body bytes all survive.
   No new fields/defaults/IDs/dates/schema_version or fact filling. Interruptions
   stop and are accounted written/restored/held/recovery-failed; inspect actual
   bytes before retry and preserve external edits. Do not promise batch atomicity.
3. Independently decode **all233** final headers with installed Perl YAML::XS/
   JSON::PP and compare to frozen inventory metadata with only the accepted
   four transformations. The converter cannot supply its sole oracle. Compare recursive mapping-key
   order using original/final YAML ASTs; decoded Perl hashes alone do not prove
   mapping order (list order remains a typed-value check). Directly
   compare body bytes to pinned main input blobs and immutable body lengths/hashes;
   check original/current paths, slugs, Source Reference bodies and destinations.
   Run actual helper `--check` all233 again: every input/output hash equal,
   zero exact permitted sentinels. Ten pilots remain whole-byte unchanged.
4. Update only owning skill metadata.version1.0.4→1.0.5 and append sibling history
   describing this bulk correction without claiming hosted success not observed.
   Keep all other SKILL prose/history bytes and previous entries. Whole owned-tree
   and fresh package version checks follow AGENTS.md. Cards/helper remain unbundled;
   no packaging-list addition or other skill bump is authorized.
5. Commit exact225 source files with required trailers, then construct the
   all233 result bridge from those committed bytes, recheck parent/diff/scopes,
   and inspect actual hosted rendering where this exact revision is available.
   Source delivery can land while hosted evidence is unavailable; return partial
   and leave S02-05 open. No push/publication permission is supplied by this prompt.

## Checks, compact records and hosted limits

Start `make help`; run `make check-skills`, `make check-skill-versions`,
`make check-package-paths`, fresh `make design`, source/planning `git diff --check`.
Verify each of the eight actual packaged Markdown members against committed
source bytes, ZIP hash, owning version/history/entire tree and scoped commits.
Report accepted warnings accurately; hard failures cannot be hidden by a green
wrapper. Run eight representative parser/preservation controls on real current
card data: extension loss, list member loss, null→empty, invented key, duplicate
key, BOM, fenced frontmatter and changed body. Drive the same actual parser/
independent preservation predicate used for positive data; no diagnostic-only
fixture labels. Reuse existing Slice01 mechanics; no new maintained checker.
Unchanged helper recovery fixtures may be retained with explicit byte applicability.

`artifacts/batch-results.jsonl` is exactly233 unique records as specified in
slice plan Result bridge and hosted boundary: link immutable inventory row/path
and original/current/final revisions/hashes; normalized or protected-pilot
status, current→final sentinel deltas (90 total), complete after typed metadata,
body bytes/hash and exact before/after body offsets/closing-delimiter lines.
Original→final changes also include16 prior pilot corrections; distinguish stages.
Carry the unchanged-body locator shift to Arc02/04. Do not duplicate original
raw/typed census payloads; pinned Git blobs/inventory remain available.

For **every233** card record actual hosted pass/fail/unavailable/unrun plus exact
revision/URL, observer/method/date, checked metadata/Markdown properties and
concrete observation/evidence or blocking reason. Read actual repository file
views at final card commit, including present metadata nesting/nulls/Unicode and
complete body headings/lists/tables/fences/code/link display. Local parse/render,
raw downloads, older views or sample coverage cannot close S02-05/A06-05.
Existing body escapes/rendering defects stay reported and Arc02-owned, with
correctness gates open where needed; body bytes cannot be repaired in this scope.
If hosted revision/access is unavailable, record the exact re-entry condition
and Operator/CDC owner in the same batch record and return checked local changes.
Do not manufacture another source/readiness report or rendering-only slice.

The one prose batch record contains intake/readback, applicable/reproduced
checks, all failures/recoveries/unrun limits, packages, hosted coverage, gaps and
Arc02/04 handoff. Ledger evidence and closing report account for all six IDs,
exact source/planning paths/candidates/parents, artifact inventory and bubble-up.
CC proposes, never accepts or closes. No semantic/fidelity/full-conformance or
parent release claim follows from mechanical preservation.

## Required reading and intake

Before edits, load these complete bounded obligations and record coverage plus
source-cited readback in `artifacts/batch-record.md`; recover clipped tool output.

- Required-full: this prompt, active slice plan and ledger; main helper;
  main `knowledge/design/SKILL.md` and sibling history; applicable standing AGENTS.md.
- Required-section: Slice01 batch Contract readback and drift check (before source
  mutation), including the field crosswalk and F02 correction; CDC I2 acceptance; Project10
  Scope and definition of done, Full-corpus review contract, Evidence and workload economy,
  Workflow and acceptance, Current status; Arc06 Schema decision and preservation,
  Verification and source interaction, Sequencing/composition/workflow; all13
  project/seven arc ledger rows. These distinguish metadata delivery from release.
- Required-section in main: `knowledge/concept-cards/SKILL.md` Ownership And
  Dependencies; `guides/08-validation-verification.md` introduction and Perform
  Structural Validation; work-verification guide05 Evidence During Correction
  Review. Apply structural preservation independently of semantic warrant.
- Required-data: immutable233 inventory full current typed values/raw headers,
  path/hash/body/pilot/delta/index projections; current233 actual check outputs;
  candidate233 independent decoder/body/idempotence observations; all233 hosted
  coverage records. No sample substitutes for these whole-set checks.
- Historical3.2 definition/index/schema selection are frozen accepted input;
  retain applicability by identity rather than reread whole books or redesign
  Project08. Source teaching-body semantic review stays Arc02, not this operation.

Raise binding drift/mapping disagreement before affected mutation; proceed under
existing authority after coherent preflight. Keep a single concise correction
return. Commit exact named arrays separately on main and planning with:

```text
Co-authored-by: Codex <noreply@openai.com>
Co-authored-by: Billo AI <ai-engineering@billo.systems>
```
