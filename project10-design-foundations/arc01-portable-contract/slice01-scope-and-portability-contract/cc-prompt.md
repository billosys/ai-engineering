# CC Assignment — Scope and Portability Contract

Initial assignment, issued 2026-10-09. Project10 / Arc01 / Slice01.
Project-relative path:
`arc01-portable-contract/slice01-scope-and-portability-contract/cc-prompt.md`.

## Outcome and authority

Produce a complete baseline inventory, source-availability assessment and portable
design contract. This is evidence and design-proposal work; **do not edit the
skill, cards, sources or packaging**. CDC is Sofie in the planning chat; you are
CC in the separate context receiving this prompt through the Operator. Return
proposed completion through the Operator. Do not create a CRC role, accept your
own work, or advance the next slice.

Binding decisions: Project10 requires full semantic review of all 233 baseline
cards; remove C&B coupling with Git-only history, no opt-in preset or compatibility
bridge; Markdown sources use `sources/md/`; preserve useful compositional craft.
Slice01 prepares that work. Its metadata inventory is not semantic review.

## Roots, revisions and drift

Locate both checkouts with `git worktree list`. Path labels in this assignment:

- `SOURCE`: implementation checkout on `main`, currently
  `/Users/oubiwann/lab/billosys/ai-engineering`.
- `PLANNING`: its `.worktrees/planning` checkout, branch `planning`.
- `PROJECT`: `PLANNING/project10-design-foundations`.
- `SLICE`: `PROJECT/arc01-portable-contract/slice01-scope-and-portability-contract`.

Use explicit working directories. Source pin:
`dffa504e851b03b8e4746f1941068e4cc850b612`. Shared audit pin: planning `795ac75b`,
`project09-design-audit/artifacts/`. Project decisions before opening were at
`290b21ffa084ed5b892e5b5c5dd295622b77c8bb`; record the actual commit containing
this issued prompt and current plans. The prior planning pin does not contain
this new open set.

Inspect both Git statuses. Untracked `SOURCE/knowledge/lfe/` predates this work
and is excluded. Never reset, clean or stage unrelated work. If HEAD changed,
compare pinned inputs: unrelated changes may coexist if documented and input
bytes still match. Changed design/method inputs, a changed current assignment
or conflicting scope go to CDC before dependent output; do not silently repin.

## Required reading and preflight

Follow standing instructions and collaboration-framework routes. Additional
assignment reads follow; source paths refer to the source pin and planning paths
to the issued revision. Complete required text extents before dependent work.
Recover truncation through bounded contiguous reads. Filenames, hashes, grep
hits and summaries do not substitute for required prose.

| Order | Path | Scope and purpose |
|---|---|---|
| 1 | `PROJECT/project-plan.md`, `PROJECT/ledger.md`, `PROJECT/arc01-portable-contract/arc-plan.md`, its `ledger.md` | Required-full: scope, review dimensions, authority and composition |
| 2 | `SLICE/slice-plan.md`, `SLICE/ledger.md`, this prompt, `SLICE/artifacts/author-reconnaissance.md` | Required-full: assignment, output contract, checks and baseline |
| 3 | `PLANNING/project09-design-audit/artifacts/audit-results-design.md` | Required-full: all DES findings and evidence limits; current project decisions supersede historical options |
| 4 | Project09 `artifacts/audit-modernization-synthesis.md` | Required-section: `The central recommendation` and all of `Proposed 1.5: coherent, portable foundations`; 2.0 is reference-only |
| 5 | `SOURCE/knowledge/design/SKILL.md` | Required-full: defective input to analyze, not authority to impose C&B or universal claims |
| 6 | `SOURCE/knowledge/design/guides/` | Required-data: all-six-file heading/brand/prescriptive-rule scan below; read complete surrounding sections for each change-map decision |
| 7 | `SOURCE/knowledge/concept-cards/SKILL.md` | Required-full: claim/support/verification/reconciliation distinctions; no schema migration |
| 8 | `SOURCE/knowledge/concept-cards/guides/08-validation-verification.md` | Required-section: opening through `Record Review Actors And Evidence Provenance`; `Perform Semantic Verification`; `Prevent False Upgrades` |
| 9 | `SOURCE/knowledge/concept-cards/guides/07-reconciliation.md` | Required-section: `Establish Targets And Conflict Scope`, `Compare Evidence Before Deciding`, `Keep Lifecycle Results Separate` |
| 10 | `SOURCE/knowledge/document-extraction/guides/03-output-contract.md` | Required-section: `Homes And Identity`, `Locator Semantics`, `Readiness By Intended Use` |
| 11 | `SOURCE/knowledge/testing/guides/03-validation-gates.md` | Required-section: `Proportionate Proof`; no reusable validator requested |
| 12 | `SOURCE/knowledge/design/concept-cards/` and `sources/` | Required-data: complete path/byte inventory and all-card source projection below; inspect every projected row in bounded groups |
| 13 | `SOURCE/Makefile` | Required-section: complete `pack_skill` definition and `design` target; distinguish package and corpus populations |

Record loaded extents, actual query populations, exclusions/errors and recovered
truncation in `artifacts/execution-notes.md`. Give a short source-cited contract
readback: outputs, immutable inputs, inventory versus semantic review, source-gap
handling at slice/project scale, and authority over proposed wording. Reconcile
conflicts before dependent work; otherwise proceed without another approval.
On context recovery, recheck assignment/state and reload governing contracts.

## Ordered execution and exact outputs

### 1. Pin the complete design population

Write `artifacts/baseline-files.tsv`, header `scope\tpath\tsha256\tbytes`
(actual tabs). One row per regular tracked file under `knowledge/design/` at
the source pin, sorted by repository-relative POSIX path. Scope is `card` for
`concept-cards/`, `source` for `sources/`, and `live` for entrypoint/history/guides.
Flag unexpected path classes/non-regular entries rather than dropping them.

Use Git's full tree listing; inspect filesystem additions/deletions; compute
SHA-256 and byte size from actual bytes and compare working files to pinned Git
blobs. No newline normalization, escape decoding or text reserialization. Retain
exact query text/results in execution notes; a short standard-library Python
query suffices. No maintained script suite is requested.

Author expectation: 402 files = 233 cards + 161 sources + eight live files.
Derive actual counts. A mismatch is evidence to investigate, not a target to
force; changed population requires CDC disposition before baseline adoption.

### 2. Preserve every card's asserted source identity

Write `artifacts/card-source-index.jsonl`, UTF-8, one object per card sorted by
path. This is a local evidence projection, not a new concept-card schema:

- `path`, `sha256`, `collection`: repository-relative identity and immediate
  directory below `concept-cards/`, matching the manifest.
- `source_fields_raw`: mapping for exactly `concept`, `slug`, `source`,
  `source_slug`, `authors`, `chapter`, `pdf_page`, `section`. Each maps to a list
  of literal right-hand-side strings from matching top-level frontmatter lines,
  in occurrence order, trimming only surrounding whitespace. Missing key = `[]`;
  explicit YAML null = `["null"]`; repeat keys retain every occurrence and are
  reported as anomalies. Preserve quoting and literal escapes inside strings.
- `source_reference_status`: `present`, `missing` or `ambiguous` for the exact
  level-one heading `# Source Reference`.
- `source_reference_raw`: unchanged body under that heading until the next
  level-one heading, or JSON null when missing/ambiguous. Report anomalies.

Locate frontmatter using exact opening/closing `---` lines. Report malformed or
multiline fields needing fuller interpretation; these scalar projections are
not general YAML parsing. Do not infer source edition or page convention.

Atomic witness: inspect
`concept-cards/munsell-colour-system/munsell-hue-circle.md` at the source pin.
Its file hash is in author reconnaissance. Literal `pdf_page: 4` supports
recording an asserted locator, not claiming physical PDF page 4 was verified.
Read its complete `Source Reference` and `Verification Notes` sections to explain
the distinction. The card is not an original-source witness.

Inspect all 233 projected rows in bounded groups. Group separately by collection
and literal `source` plus `authors`; collection is not source identity. Expected
collection counts: Arnheim 112, Munsell 19, posts 46, Butterick 37, Tschichold 19.
The four posts have counts 12/10/13/11 as named in reconnaissance. Unexpected
values stay visible and require explanation.

### 3. Assess availability without inventing readiness

Write `artifacts/source-readiness.md`. For each distinct asserted source, include
observed title/author; card paths or exact index membership predicate/count;
local source paths; original versus prepared-content status; locator/edition
uncertainty; checks performed; next action and owner.

Inspect the designated `knowledge/design/sources/` tree and each mapped file's
identifying passage. For the multi-file Butterick collection, inspect its index
or conversion report and identifying source text; derive complete membership
from the manifest. Do not claim full fidelity from a sample. Show the eight
source-title groups if actual observations support them, not five inferred from
directories.

Distinguish local prepared text present, original not located in designated tree,
locator interpretation unresolved, and semantic support not assessed. These are
assessment descriptions, not a new global lifecycle vocabulary. For absent
originals, identify title/edition evidence and what CDC/Operator must locate
before dependent review. Do not infer absence everywhere. Do not scan private
storage, download, purchase, convert or write sources. Acquisition/preparation is
later assigned work; gaps do not prevent an accurate Slice01 gap report.

### 4. Produce the portable contract and change map

Write `artifacts/portability-contract.md` with these sections:

1. **Binding decisions and intended behavior.** Cite the project decisions.
   No C&B identity, legacy profile or compatibility obligation. Preserve supplied
   identity and full-corpus review; package and corpus remain distinct.
2. **Reusable method and project inputs.** Define a short profile as a prose/table
   contract: audience/tasks; content/reading conditions; existing identity/assets;
   platforms/viewports/input modes; language/script/direction; accessibility/user
   preferences; typography/colour/spacing/token constraints; density/themes;
   fixed choices; unknowns/evidence. For each state purpose and absent-input
   behavior. Unknowns remain unknown or become explicit justified proposals,
   never a silent house preset. This is not a serialization schema, mandatory
   questionnaire or new tool.
3. **Principle disposition.** Map all seven current principles to retain/correct/
   replace proposals with exact source witnesses and DES IDs. Use the synthesis's
   seven-principle proposal as the candidate and explain substantive deviations.
   Distinguish mathematical identity, empirical claim, contextual heuristic,
   project convention and analogy. Do not invent scientific proof. Final new
   wording/example configurations remain proposals for CDC/Operator adoption.
4. **Eight-file change map.** Every live file gets source locations, required
   removals/corrections/preservation, portable replacement behavior and observable
   later checks. History is preservation/version-governance work, not erasure of
   past C&B history. Scan all six guides for headings, C&B/domains, named fonts,
   palette/axis values and default prescriptions; read full surrounding sections
   for each decision. Explain why removing brand words alone is insufficient.
5. **Finding ownership.** Map DES-001–016 individually to existing arc(s), required
   outcome, verification and outstanding source/decision needs. This proposes
   downstream treatment; it does not close findings.
6. **Worked contract cases.** Apply all five cases below as input → expected
   decision behavior, citing contract clauses. These are analytical checks of
   the proposal, not model-performance experiments.
7. **Unresolved decisions and handoff.** Separate proposed wording/configuration
   from settled scope. Name source/method work for Slice02 and adoption/composition
   work for Slice03. No unresolved requirement disappears.

Case expectations, derived from the approved portable scope:

- Generic literary page without identity: ask only consequential missing questions
  or state provisional choices; no inherited C&B names/palette/fonts.
- Existing interface with supplied semantic tokens/typeface: preserve identity;
  explain task-justified corrections rather than unsolicited rebranding.
- User independently chooses brown and Fraunces: preserve appropriate choices.
  Removing C&B coupling is not a blanket ban on those values.
- Dense interface needs a breakpoint and optical adjustment: allow reasoned
  contextual choices; no universal no-media-query/geometric-only veto.
- Source/card conflict or unavailable original: preserve disagreements, evidence
  limits and next actions. Do not promote a convenient claim to verified fact or
  treat quarantine as completion of full-corpus review.

## Validation and failure handling

Use direct checks, retaining exact queries/results in execution notes. No
reusable validator, experiment harness, source build or installation is requested.

| Ledger | Check and expected observation | Failure rejected / limit |
|---|---|---|
| S01-01 | Compare loaded text/query extents and readback with actual contracts | Missing prose concealed by receipts; intake remains attestation |
| S01-02 | Independently enumerate the exact manifest path set; every size/hash matches pinned blobs and working bytes; JSONL identity set equals exactly all 233 card rows | Duplicate+omission with correct count; stale digests; index omissions |
| S01-02/03 | Parse every JSONL line and compare literals/body spans directly to each card; inspect title/author groups and anomalous rows | Posts collapsed to one source; null/missing/quoted values conflated |
| S01-03 | Check availability against existing paths and identifying passages or documented designated-tree absence | Card citations mistaken for originals; presence mistaken for fidelity |
| S01-04 | Apply all five cases to explicit contract clauses; inspect seven principle dispositions | Blanket value bans, new universal preset, proposals mislabeled approved |
| S01-05 | Eight live paths and DES-001–016 each have one primary map entry, cross-referenced for shared work | Omitted file/finding hidden by summary |
| S01-06 | Recheck source bytes, audit hashes, Git statuses, planning diff and all new local links | Unauthorized edits; compare per-path when unrelated concurrent work exists |
| S01-07 | Closing report walks every row and records actual checks, gaps, proposals and owners | Inventory/proposal mislabeled repair or semantic acceptance |

Run planning `git diff --check`. Source metadata/package gates are not triggered
by this evidence-only assignment. Do not report the old audit's build as a fresh
run or claim browser/usability validation. Parsing/population/identity conflicts
go to CDC with observations retained. Unexpected source absence is a finding;
fabricated support is a failure.

## Allowlist, commit and return

CC may create/change only these paths relative to `SLICE`:

- `artifacts/baseline-files.tsv`
- `artifacts/card-source-index.jsonl`
- `artifacts/source-readiness.md`
- `artifacts/portability-contract.md`
- `artifacts/execution-notes.md`
- `ledger.md` (evidence and CC disposition notes; no weakened criteria)
- `closing-report.md` (only when actual execution evidence exists)

Preserve author reconnaissance, all plans, this prompt, Project09 and all source
files. Do not create `cdc-verification.md`, close parent rows, open slices, migrate
schemas or repair source. Additional paths or substantive changes require CDC
disposition before mutation; continue unaffected work.

After self-checks, stage only the named output files that exist and commit with
an explicit path list and `git commit --only`. Do not stage whole directories
or include others' staged work. Include both trailers:

```text
Co-authored-by: Codex <noreply@openai.com>
Co-authored-by: Billo AI <ai-engineering@billo.systems>
```

Return planning commit, exact assignment/source/audit revisions, actual counts
and discrepancies, outputs, per-row outcomes, failed/blocked/unrun checks,
proposed decisions, source gaps and bubble-up findings. State proposed-done
pending CDC; do not call the corpus verified or the skill repaired. Link the
execution-notes intake/readback from the closing report. No publishing or source
commit is authorized.
