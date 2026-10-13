# CC — Fix Post-Card Unicode Presentation

Execute Arc02/Slice09 and return to CDC Sofie. Current assignment is this
`cc-prompt.md`, issued by its introducing planning commit, predecessor
`eac665f569d269b6a913e2f9349ef3e73656781e`. Main input is
`c4cc74279ac845003b0c80f55907981241c58a99`. Two contributors; Expedited Mode.
This is a source correction plus its checks and correction of hosted evidence,
not another analysis-only assignment. Arc06/Slice02 stays open.

## Required reading and preflight

Read in order, recording concise coverage and source-cited contract readback in
this slice's sole `artifacts/batch-record.md`; recover required truncated output.

- Required-full: this prompt, [slice plan](slice-plan.md), [four-row ledger](ledger.md),
  current main `knowledge/design/SKILL.md` and sibling `version-history.md`.
- Required-section: [project plan](../../project-plan.md) Scope and definition of
  done, Immediate sequence and working method, Evidence and workload economy,
  Recorded Operator decisions, Operator metadata and rendering addition, Workflow
  and acceptance, Current status. [Arc02 plan](../arc-plan.md) Capability, Accepted
  inputs and preservation, Slice breakdown and sizing, Workflow and current assignment.
  All thirteen project/ten arc ledger criterion rows; other history is reference-only.
- Required-section: [Arc06 CDC hosted review](../../arc06-card-metadata-and-rendering/slice02-book-card-metadata/cdc-verification.md#hosted-return-independent-review--2026-10-13)
  complete, and Arc06/Slice02 plan's Frozen existing-field contract, Result bridge
  and hosted boundary, and Hosted review and current handoff. Read its current
  six-row ledger and CC closing report completely, and batch record's complete
  Hosted rendering boundary and Postpublication sections, retaining their chronology.
- Required-section: current repository `knowledge/concept-cards/guides/08-validation-verification.md`
  Define the review, Perform structural validation, Make each result recoverable,
  Prevent false upgrades; `knowledge/work-verification/guides/05-independent-verification.md`
  Evidence during correction review; current project-management README/Expedited
  Mode and engineering-methods guide07 CC intake. Follow current AGENTS.md and
  collaboration-framework routing; no separate schema/domain theory inquiry.
- Required-data: published Arc06/Slice02 bridge at planning `eac665f5`, all233
  path/disposition/revisions/metadata/body/hosted records. Verify pinned hash, exact
  233 roster and46 post paths; resolve every final source hash at `c4cc742`.
  Project these46 bodies' complete escape matches, line contexts and per-token
  frequencies without clipping; inspect code-bearing contexts and Matrix card's
  definition/inverse formulas, feColorMatrix's SVG block, mix-blend-mode's formulas.
  This is representation inspection, not a full-body five-dimension semantic read.
- Conditional: a token outside the whitelist, an intended literal escape example,
  or relevant dirty/source drift requires the exact affected context before editing;
  stop dependent work and return it to CDC. Missing original books/captures do not
  block this known encoding correction. Historical theory/source reports are reference-only.

## Exact source scope and transformation

Use the immutable bridge **from `eac665f5`**, before changing its hosted records:

```python
import hashlib, json, subprocess
p = "project10-design-foundations/arc06-card-metadata-and-rendering/slice02-book-card-metadata/artifacts/batch-results.jsonl"
raw = subprocess.check_output(["git", "-C", ".worktrees/planning", "show", "eac665f569d269b6a913e2f9349ef3e73656781e:" + p])
assert hashlib.sha256(raw).hexdigest() == "3b990a637074cf19dfcecd8709e2712ccaefb394d0e85c44b20ed36e34f9041b"
rows = [json.loads(line) for line in raw.splitlines()]
assert len(rows) == len({r["path"] for r in rows}) == 233
cards = [r["path"] for r in rows if r["path"].startswith("knowledge/design/concept-cards/posts/")]
assert len(cards) == 46
source_paths = cards + ["knowledge/design/SKILL.md", "knowledge/design/version-history.md"]
```

All233 card hashes are `revisions.final.sha256` in those pinned rows. Additional
source pins:

- `knowledge/design/SKILL.md` SHA-256 `d3ca8d883652138b92b1b6d10883695683b3165e63475af715426514b6501401`
- `knowledge/design/version-history.md` SHA-256 `b7bd7f35f4ff60f94c78ffd2e3db0c219feb00e87396df1961a541fd60a44a60`

Only those48 source paths may change. No broad glob commit; keep helper, guides,
sources, unrelated `knowledge/lfe/` and other work untouched. Read actual version
metadata1.0.5 first. Preserve all46 complete header prefixes, through each row's
`body.final.body_start_byte_offset` (including unchanged following newline in
body), and every187 other card whole-byte. Preserve numeric/source/domain claims.

Binding conversion table (1062 occurrences,23 tokens):

| Literal body token | Display character | Expected occurrences at input |
|---|---|---|
| `\u00b0` | ° | 5 |
| `\u00b2` | ² | 10 |
| `\u00b3` | ³ | 2 |
| `\u00b7` | · | 29 |
| `\u00b9` | ¹ | 10 |
| `\u00d7` | × | 53 |
| `\u00e9` | é | 1 |
| `\u00f6` | ö | 13 |
| `\u00f7` | ÷ | 2 |
| `\u03b3` | γ | 5 |
| `\u03c6` | φ | 21 |
| `\u2013` | – | 40 |
| `\u2014` | — | 734 |
| `\u2026` | … | 1 |
| `\u207b` | ⁻ | 10 |
| `\u207f` | ⁿ | 1 |
| `\u2192` | → | 90 |
| `\u2194` | ↔ | 5 |
| `\u2208` | ∈ | 5 |
| `\u2212` | − | 11 |
| `\u221a` | √ | 2 |
| `\u2248` | ≈ | 11 |
| `\u2260` | ≠ | 1 |

Recommended mechanics: split each original committed file at its recorded body
byte offset. Replace only these exact ASCII six-byte tokens in the body with
their UTF-8 characters, then append it to the original prefix. Use a byte regex
for the enumerated tokens or literal replacements; no whole-file/general
`unicode_escape` decoding. No replacement of other escape forms, newline escapes,
HTML entities, Markdown syntax or metadata. The SVG `\u2026` is an illustrative
ellipsis, not a runnable-HTML expansion request. Existing actual Unicode stays
exact. Decode once; a second pass changes no bytes. No reusable helper product.

Useful witnesses: Matrix's definition contains `3×3` and inverse notation `M2⁻¹`
/`M1⁻¹`; mix-blend-mode's `destination × source` and `1−(1−B)÷A` remain legible
formulas; Björn's name and en/em dashes remain their intended characters. This
repair does not accept those formulas' domain meaning or revise their assertions.

Bump only `metadata.version`1.0.5→1.0.6 and append a matching significant correction
entry to the sibling history. Retain prior entries verbatim; version numbers stay
only in the owning metadata/history. Guides/cards/helper remain unbundled as before.

## Checks and compact evidence

Before writes, reconcile all233 hashes/paths/headers against the pinned bridge.
Compare final bytes for each46 to the **original committed prefix plus the exact
specified body replacements**; compare187 other whole files directly to input.
This equality oracle catches any unrelated mutation as well as missing glyphs.
Check every metadata prefix byte, UTF-8 validity, original line counts and all
1062 replacements; the total body byte delta is−3337. Do not compare only counts
or converter-owned hashes. Keep numbers, sections, lists, table/fence/code structure,
references and all metadata exact apart from the explicit entrypoint version.

Use three temporary specimens with that same equality oracle: leave one active
Matrix escape undecoded; modify a header field; modify an unrelated body number.
All three must fail while the exact expected correction passes. No new test or
validator files in source, no broad mutation suite, no repeat helper write-safety
or schema census. Inspect intended glyphs in representative prose, formula/code
and name contexts; global equality covers the full mechanical scope.

From main run `make help`, `make check-skills`, `make check-skill-versions`,
`make check-package-paths`, fresh `make design`, then actual ZIP member/source
comparison for all eight packaged Markdown members. Check the whole owning
version/history contract and source/planning `git diff --check`, links and EOF.
Record actual command outcomes/warnings/failed or recovered attempts and source/
package identity. Gates use the current Makefile, not stale pre-rebase receipts.

Sole new artifact `artifacts/batch-record.md`: concise intake, commands/results,
and a compact46-row table or JSON block giving path, before/after whole-file and
body hashes/sizes, unchanged header/closing-line/body-start offset, replacement
count and source revisions. These fields join the233-row Arc06 input bridge and
serve later revised-body checks; do not duplicate full typed headers/inventory.
Also record preservation of187 and metadata on233, four proposed outcomes,
actual visibility checks versus unrun hosted checks, and downstream owners.

## Correct the existing hosted evidence in this same return

Arc06/Slice02's current bridge/prose falsely classify46 bodies as correct because
they match the source. Correct those published-`c4cc742` assessments to body `fail`
and overall `fail`, retaining metadata `pass`, URLs, raw response evidence and
structural observations. Add the observed escaped token count and concrete
expected-versus-visible example per affected card. Preserve the other187 records;
do not infer their semantic correctness. Preserve every non-hosted field, including
historical final revision/hash/body-preservation claims at `c4cc742`.

Before replacing each affected hosted record, retain its original complete
`eac665f5` hosted observation in a `prior_observations` array under `hosted` with
that planning revision and an explicit superseded reason. Do not nest that array
recursively. This is evidence history, not a new card schema. Add observer/date
and the correction reason; keep original raw fetch identity/provenance distinct
from your current review. Updating prose alone while leaving46 bridge passes is
insufficient. Correct the batch record and closing report explicitly, preserving
initial local/unavailable/CC233-pass proposals as historical. Keep the metadata-only
body preservation result separate from this intentional Arc02 body correction.

Keep all six Arc06 ledger statuses as CDC left them: five done, S02-05 open.
Update evidence/notes only. Point the46 affected observations and prose to this
Slice09 correction record and exact source candidate; do not mark unpublished
repaired bodies hosted-pass. After CDC source acceptance, Operator publication/
access and actual corrected-revision checks re-enter Arc06's remaining gate.
No new push/install/release authority is granted by this assignment.

## Exact planning writes, commits and return

Exactly seven CC planning output paths, relative to Project10:

1. `arc02-theory-and-evidence/slice09-post-card-unicode-presentation/artifacts/batch-record.md`
2. `arc02-theory-and-evidence/slice09-post-card-unicode-presentation/ledger.md` (evidence/notes only)
3. `arc02-theory-and-evidence/slice09-post-card-unicode-presentation/closing-report.md`
4. `arc06-card-metadata-and-rendering/slice02-book-card-metadata/artifacts/batch-record.md`
5. `arc06-card-metadata-and-rendering/slice02-book-card-metadata/artifacts/batch-results.jsonl` (hosted only)
6. `arc06-card-metadata-and-rendering/slice02-book-card-metadata/ledger.md` (evidence/notes only)
7. `arc06-card-metadata-and-rendering/slice02-book-card-metadata/closing-report.md`

Protect all issued prompts/plans, CDC records, parent ledgers, original inventories
and local bridge fields. Commit only the48 explicit source paths, then these seven
planning outputs. Both commit messages include separate trailers:

```text
Co-authored-by: Codex <noreply@openai.com>
Co-authored-by: Billo AI <ai-engineering@billo.systems>
```

Leave all four S09 statuses open for CDC; no self-acceptance. Closing report names
this assignment, source commit, scope/actual checks, sole new artifact, all four
outcomes and Arc02 bubble-up. Record source identity in the same planning return;
no receipt-only child needed. Return for independent review; Arc06's hosted,
all233 five-dimension, originals/fidelity, browser/accessibility and release gates
remain under their existing owners. No renewed readiness research or extra schema work.
