# CC Assignment — Project12 / Arc01 / Slice01

Execute the initial **evidence-only** baseline and migration inventory for the
CHCD Protocol project. Return proposed-done evidence to Sofie (CDC) through the
Operator. This prompt is preserved once handed off; corrections require a new
numbered sibling prompt.

## Identity, authority and boundaries

- Project: `project12-chcd-protocol`.
- Arc: `arc01-baseline-and-evidence`.
- Slice: `slice01-baseline-and-migration-inventory`.
- Current assignment: this slice's `cc-prompt.md`; predecessor: none.
- Source root: `/Users/oubiwann/lab/billosys/ai-engineering` (read-only).
- Source pin: `dffa504e851b03b8e4746f1941068e4cc850b612`.
- Planning root: `/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning`.
- Slice root: the project/arc/slice path above beneath that planning root.

The Operator opened this arc and slice on 2026-10-09. Execute when the Operator
relays this assignment; a coherent intake does not require another permission
round. Default Two-Contributor Workflow: you are CC, Sofie is CDC. Do not take
over CDC's design or independent acceptance role. No Expedited Mode, commit,
push, deployment or source editing is authorized by this assignment.

Binding project decisions: the name is **CHCD Protocol**, expanded as
**Composable Heterogeneous Cognition Dispatch Protocol**, pronounced Check-Dee
Protocol; `chcdp` is the compact path segment. Preserve the CCDP 0.2 tree,
including iterations through 0.2m, and eventually seed the successor by a
verified copy. In 0.3 retain legacy protocol names, including `org.ccdp.*`,
with deprecation notices announcing removal in 0.4. Archive and web redirects
survive removal of runtime name support. Do not decide successor identifiers,
alias conflict/normalization rules, notice channels or wire-version changes.

Allowed writes are precisely:

1. `artifacts/baseline-files.jsonl`
2. `artifacts/migration-inventory.jsonl`
3. `artifacts/baseline-report.md`
4. `artifacts/execution-notes.md`
5. This slice's `ledger.md` (execution dispositions/evidence, not criteria).
6. This slice's `slice-plan.md` (execution identity and assignment disposition,
   not scope or acceptance changes).
7. This slice's `closing-report.md`, when there is an actual return to report.

All relative write paths above are under this slice root. Create `artifacts/`
when writing evidence. Temporary inspection files may use an OS temporary
directory; keep replayable commands/snippets in execution notes. Leave all
other source/planning files and unrelated dirty work untouched. Do not create
the successor tree, edit either guide, run assembly into the predecessor,
rebuild packages, repair JSON examples, create a reusable validator, write a
CDC verdict or open a later slice. Leave the scoped outputs uncommitted.

## Required-reading manifest and intake

`SOURCE` below means the source root; `PROJECT` means
`<planning-root>/project12-chcd-protocol`; `SLICE` is this slice root.
Read in order before dependent work. Governing instructions are current
working files, including untracked Project12 documents: record their SHA-256
and actual state rather than attributing their content to planning HEAD.
Protocol/build evidence is read at the source pin using Git objects. If a
working file differs, preserve that distinction.

| Order/type | Exact input and extent | Why/when |
|---|---|---|
| 1 Required-full | `SOURCE/AGENTS.md`, `<planning-root>/AGENTS.md`, `PROJECT/AGENTS.md` | Scope, planning/source separation and authority at intake |
| 2 Required-full | `PROJECT/project-plan.md`, `PROJECT/ledger.md`, `PROJECT/arc01-baseline-and-evidence/arc-plan.md`, its sibling `ledger.md` | Parent obligations and boundaries before inventory |
| 3 Required-full | `SLICE/cc-prompt.md`, `slice-plan.md`, `ledger.md` | Active execution contract before any output |
| 4 Required-full | `SOURCE/knowledge/project-management/SKILL.md`, `guides/README.md`, `guides/03-planning-top-down.md`; `SOURCE/knowledge/work-verification/guides/01-ledger-discipline.md` | Open-set, intake/assignment and evidence discipline; these guide paths are under their respective skills |
| 5 Required-section | `SOURCE/knowledge/engineering-methods/guides/07-implementation-prompt-authoring.md`: “Required reading and CC intake”, including all five steps and evidence-strength paragraphs through the next section | Load before evidence production; record full intake and source-cited readback |
| 6 Required-full, pinned | `protocols/ccdp/README.md`, `protocols/ccdp/src/README.md`, `protocols/ccdp/Makefile`, `protocols/ccdp/json/MANIFEST.md`, `protocols/ccdp/src/18-open-questions.md`, `.github/workflows/pages.yml` in the pinned SOURCE tree | Baseline meaning, build/publication distinction, corpus limits and inherited questions |
| 7 Required-section, pinned | `protocols/ccdp/src/02-conventions.md` §2.1; `src/07-message-format.md` §7.3.1 (same source directory); root `Makefile` CCDP variable definitions and targets `ccdp`, `ccdp-package-clean`, `ccdp-package`, `check-ccdp-package`; `scripts/check-ccdp-package` package constants and required/excluded populations | Establish actual version and distribution witnesses; load full named sections/target bodies and definitions they require |
| 8 Required-data, pinned | Complete Git tree; all tracked predecessor objects; whole-tree content/path census and derived integration population described below | Enumerate and inspect complete structured results in lossless partitions; record counts, errors and exclusions |
| 9 Required-section, pinned | `protocols/ccdp/json/FINDINGS.md`: introduction and each finding's complete ID/title (including multiline titles); both guide files' complete decoded differing passages plus containing section | Index every inherited finding without pretending to reverify it; establish actual guide difference |
| 10 Conditional | Complete defining prose/table/block around each distinct migration surface discovered in step 8, with needed definitions; `json/FINDINGS.md` full body of any finding used substantively beyond indexing | Before assigning a semantic classification or making a substantive finding; name loaded extents in execution notes |
| 11 Conditional | `SOURCE/knowledge/project-management/guides/04-closing-slices.md` and `SOURCE/knowledge/work-verification/guides/03-row-closure.md` | Before the proposed-done return and ledger/report updates |
| Reference-only | Other specification sections and external reference targets not needed to classify a surface | Broader semantic/source verification belongs to later slices; do not claim it here |

These categories do not reduce governing skill-loading obligations. Follow
the current collaboration-framework routing. No Rust/JavaScript implementation
or quality audit is assigned; file census and template decoding do not authorize
code changes. If a new binding dependency appears, load and record it before
affected work. Missing required inputs block that work.

Write intake coverage and a concise contract readback in
`artifacts/execution-notes.md`: current assignment, source/plan state, loaded
text extents, required-data query results, conditional applicability and any
recovered truncation. Explain the implications of read-only preservation,
0.3/0.4 compatibility, corpus-versus-schema distinction and evidence limits.
Hashes prove identity, not that text was read. Do not use sampled headings as
full-document coverage or hide truncated outputs in a log you never inspect.

## Inspection recipe and record shapes

### 1. Establish immutable input and populations

Confirm source/planning worktree identities and capture `git status --short`
at both roots. Verify the pin exists. Enumerate with NUL-safe Git commands:
`git ls-tree -r -z <pin> -- protocols/ccdp/` and a complete source tree listing.
Read blob bytes through `git cat-file blob <oid>` or an equivalent batch read.
Do not walk the live directory and silently include ignored artifacts.

Define population A as all tracked paths under `protocols/ccdp/` at the pin.
Define H as all pinned tracked files whose path contains `ccdp` case-insensitively
or whose text matches `ccdp` or `Composite Cognition Dispatch Protocol`
case-insensitively. Use `git grep -i -l` at the pin for content discovery and
the tree list for filename discovery; retain binary/non-text exclusions.
Define I as H minus A, plus `.github/workflows/pages.yml`, plus any concrete
build/publication dependency needed to explain an inspected route. Record why
each such extra file was admitted. The manifest population is A union I.

Discover ignored/untracked predecessor content separately using scoped Git
status/list commands. Report path groups/counts and why excluded from A;
do not scan or hash cache payloads or unrelated `knowledge/lfe/`. The absence
of an ignored item from A is deliberate, not proof it does not exist.

Compare every selected pinned file against its current tracked/index state.
If HEAD changes only outside this population, record the difference and
continue against the fixed pin. Changed selected inputs, new relevant surfaces,
unmerged entries or index/worktree mismatch affecting the baseline must be
reported to CDC; stop dependent conclusions rather than silently accepting a
new baseline. The inspection must not reset, stash or overwrite dirty work.

### 2. Write the byte/mode manifest

`baseline-files.jsonl` has one UTF-8 JSON object per unique source-relative path,
sorted lexically by `path`, with these required fields:

```text
path: string
population: "archive" | "integration"
revision: full pinned commit ID
mode: Git mode string
object_type: Git object type
object_oid: full Git object ID
byte_length: nonnegative integer
sha256: lowercase 64-character digest of raw blob bytes
selection_reason: string
```

For symlinks, hash the stored link-target blob, not the target file; preserve
mode `120000`. Do not treat submodule commit entries as file blobs: report any
such entry and return the unresolved manifest representation to CDC. Preserve
raw bytes and line endings. Modes and object identity matter alongside SHA-256.
The author observed A = 103 files and the assembled hash recorded in the slice
plan; derive both and explain discrepancies, never force those results.

### 3. Classify migration surfaces without designing the rename

`migration-inventory.jsonl` contains one observation per distinct semantic
surface within a file, sorted by path and locator. Required fields:

```text
id: unique stable identifier, e.g. MIG-001
path: a path in baseline-files.jsonl
category: "wire-field-or-method" | "capability-schema-or-metadata" |
          "security-or-audit" | "build-or-package" | "navigation-or-url" |
          "display-or-guide" | "historical-reference" | "other-unresolved"
legacy_form: exact observed spelling, or null for a dependency with no legacy text
witness: {line_start: integer, line_end: integer, section: string,
          decoded_locator: string or null, excerpt: string}
role: "normative" | "example" | "generated" | "implementation" |
      "publication" | "history" | "unresolved"
observation: source-supported statement
decision_needed: string or null
owner: named downstream slice/arc or CDC
```

Do not emit one row per substring repetition. Group occurrences of the same
surface within a file and retain representative resolvable witnesses. Distinct
uses need separate rows even if spellings agree. Track census hit counts and
path coverage in the report; every H path needs a row or explicit exclusion
with reason. Files in A with no legacy-name hits still belong in the manifest.

Source-grounded example: `protocols/ccdp/src/07-message-format.md` §7.3.1
defines `ccdp_version` as REQUIRED and requires the value `"1.0"` while stating
document/wire versions are independent. Classify this as a normative wire
field with its actual pinned lines and excerpt. Its question is the future
field/alias/version contract owned by Arc02, not permission to replace its
value with `"0.3"`. Record `org.ccdp.*` metadata/capability names separately;
method strings such as `ccdp/...` are another wire surface. A historical release
note mentioning CCDP is not a protocol alias or a mandatory rewrite target.

Represent contexts tied to token scopes, signatures, schema lookup, replay or
audit as security-relevant migration questions where evidence supports that
classification. Do not assert an implemented alias behavior or invent new
canonical spellings. The project compatibility schedule remains settled.

### 4. Explain archive, package and site boundaries

Trace the root Makefile CCDP targets and the package checker's selected and
excluded populations, protocol Makefile output/version behavior, documentation
entrypoints, site navigation and Pages upload path. Record route edges with
source locators in `baseline-report.md`. Distinguish selection-code inspection
from actually building and testing a zip; no build is assigned.

Compare `protocols/ccdp/visual-guide/index.html` with
`site/protocols/ccdp/visual-guide/index.html` as raw bytes and as decoded template
text. Extract the `<script type="__bundler/template">` payload as data and
JSON-decode its string without running embedded JavaScript. Retain the original
HTML hashes and both original/decoded locators. Inspect every changed span and
its containing section. Author reconnaissance found a published introductory
sentence adding “And how much is” with an emphasized phrase; verify the actual
complete difference, not merely that the hashes differ. Record consequences
for a future authoring authority decision; choose neither copy automatically.

### 5. Index inherited gaps and bounded next decisions

In `baseline-report.md`, index each README readiness item, all five sections
of `src/18-open-questions.md`, and every unique finding declaration in
`json/FINDINGS.md` (including suffix IDs such as F-22bis). Preserve original
IDs and locators; for README items use local report IDs. Reconcile duplicates
by cross-reference, not deletion. State that historical findings are reported
by their source and not independently reproduced in this slice. The historical
manifest reports 32 findings; count the declarations and disclose differences.
An ID in a cross-reference is not a second finding declaration.

Assign existing-claim/normative checks to Slice02, model/comparison research to
Slice03, scope/preservation/publishing decisions to Slice04, and detailed wire
compatibility design to Arc02. Include unresolved input/authority questions
with a concrete blocking scope. Preserve source-reported absent schemas and
conformance tests; extracted examples or maximal instances do not fulfill them.

## Verification and return

Record the exact commands and any short inspection snippets in execution
notes so CDC can replay them without a new software package. Perform:

1. **Manifest reconciliation:** freshly enumerate A and I and compare exact
   path sets and all modes/OIDs/byte lengths/hashes. Matching counts alone cannot
   pass; missing/extra/substituted files must be visible. Verify current scoped
   source/index state again at return.
2. **Record integrity:** parse every JSONL line; check required fields, unique
   paths/IDs, allowed categories and that every inventory path resolves to the
   manifest. Check witness ranges against the pinned text and decoded locators
   against the corresponding template. Retain malformed-record failures.
3. **Coverage:** reconcile all H paths and integration dependencies to rows or
   explicit exclusions. Review the normative wire-field example, a namespace,
   a method, a historical mention and a publication/build route as discriminating
   witnesses. Do not classify everything as a textual rename.
4. **Guide and gaps:** reproduce both raw and decoded guide comparison;
   reconcile all gap/finding IDs and downstream owners. No historical finding
   becomes verified merely because it appears in this inventory.
5. **Preservation and scope:** compare source start/end selected-file identities
   and status, report concurrent unrelated changes without claiming authorship,
   and confirm only allowed planning outputs were written. No package or runtime
   result may be claimed from these static checks.

These checks map respectively to S01-02/06, S01-03/06, S01-03, S01-04/05 and
S01-01/06. S01-07 is the complete return. Use actual outcomes, including
failures/blocked steps. No reusable checker or synthetic mutation suite is
required for this one-off inventory; direct set/blob/context comparisons are
the chosen proof method.

Write `closing-report.md` with assignment/source/plan identities, artifact paths,
per-row claims and evidence strength, actual checks, limitations and a
scope-as-promised versus scope-as-delivered comparison. Bubble up findings and
next-owner questions to the arc. Record intake/readback evidence by reference.
Mark completion as proposed-done and awaiting CDC verification, not accepted.
Return the report path through the Operator. Do not commit, publish, close the
arc or issue Slice02. If blocked, preserve completed evidence and report the
exact unresolved input/decision against affected rows; do not invent results.
