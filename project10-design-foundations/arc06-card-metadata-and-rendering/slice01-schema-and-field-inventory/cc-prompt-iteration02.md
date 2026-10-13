# CC Iteration02 — Make recovery identity checks byte-exact

Execute **Arc06/Slice01 Iteration02** and return to CDC Sofie via Operator relay,
Two-Contributor Workflow, Expedited Mode. This file is `cc-prompt-iteration02.md`;
predecessor [Iteration01](cc-prompt-iteration01.md), returned for review.
Issuing revision is the planning commit introducing this prompt, parent
`1e7dc84c43f3a9b823b402132971f93d82a0f045`. Main input `d2188c45a451be8b5e82f534f9a9ac067c137b64`;
helper SHA-256 `db068ee4b161bd3e026ab868a9ac46a99eb1df28b17c98f945557587dfbd909b`.
Current [slice plan](slice-plan.md), [ledger](ledger.md) and
[CDC I1 review](cdc-verification.md#iteration01-independent-review--2026-10-13)
govern. S01-01/02/03 remain done; S01-04/05/06 remain open for F03.

## Binding correction and exact scope

**Main: only `scripts/normalize-design-card-metadata.rb`.** In
`recover_written!`, change the initial `current_bytes == record.fetch('output')`
and the subsequent `File.binread(absolute) != record.fetch('output')` to compare
against `record.fetch('output').b`. `File.binread` already returns binary bytes.
This changes comparison semantics only: no transcoding, normalization, mutation
of output, or relaxed identity condition. Keep output serialization UTF-8.
Both sites must change; changing only the first still fails Unicode restoration.

**Planning: only** `artifacts/batch-record.md`, `ledger.md` (evidence/notes only;
CDC owns statuses), and `closing-report.md` in this slice. Append concise I2
intake/checks/current dispositions and preserve historical claims/receipts.
All card bytes, inventory, source index, schema mapping, eight packaged Markdown
files, Makefile, versions/history, parser/emitter/transform, private-buffer
clearing, guards/accounting and all other helper lines remain exact. Do not add
supporting artifacts, new fields, dependencies or a maintained testing framework.

The cause and two-site repair were exercised by CDC in disposable source copies;
see F03 in the linked review. No integrated source repair has been accepted.
Concept-cards guide08's structural/semantic distinction applies: this fixes byte
preservation during failure, not card meaning, source fidelity or schema adoption.

## Required checks

Use the existing durable two-case Python CLI fixture in `cdc-verification.md`,
with the exact candidate helper and pinned original `1489e767` card blobs in
isolated tracked repositories. Run it in the original additive-first order and
**reversed matrix-first order**. The reversed first output contains real Unicode;
it distinguishes equal byte content from encoding-sensitive Ruby equality.

- Both orders: prewrite external edit exits nonzero/zero JSONL, external first
  bytes retained, second input untouched, path-specific conflict/held accounting.
- Both orders: second rename fails after first succeeds; exits nonzero/zero
  JSONL, both final raw files exactly equal originals, first named written and
  restored, held/recovery-failed none, original injected failure still reported.
- Matrix-first ordinary two-file conversion then check: exit0/two public rows,
  body/typed preservation, no private buffers and byte-idempotent second check.
- Matrix-first external edit during failure: retain the actual external bytes,
  report first held, do not overwrite it. Matrix-first restore failure: first
  retains own output, report recovery-failed and original/recovery errors.
- In a disposable helper copy, revert only the second `.b` comparison while
  leaving the first fixed. The matrix-first second-rename witness must fail
  exact-original restoration. Record this negative at the real CLI path.

Use existing I1 hooks for held/recovery-failure cases; change only first/second
path order as needed. Expected raw files come from pinned input blobs plus the
literal injected external edit, independently of the converter's records.
Do not test only diagnostic labels or reimplement recovery as a test model.

Run `ruby -c` and actual candidate `--check` all233 against immutable inventory:
input hash/complete typed metadata/body bytes/hash/public seven-field shape,
exact four sentinel transformations, ten pilot idempotence, 90 remaining
sentinels. No live `--write`. Retain earlier parser/serialization/path/symlink/
duplicate controls after verifying their methods unchanged. Retain Make/package
gates only after all eight design Markdown inputs and Makefile compare exact to
accepted `fe4e0558`; this unbundled two-comparison change needs no rebuilt ZIP.
Check exact committed parents/scopes/trailers, protected bytes, local links,
LF/EOF and `git diff --check`. Report failures/recoveries and unrun hosted work.

## Intake, budget and return

Before edits, required-full: this prompt, current slice plan and ledger, current
helper. Required-section: CDC record's initial durable Python witness and I1
review/F03/current dispositions; I1 prompt's F01 recipe for recovery/guards and
F02 constraint; concept-cards `knowledge/concept-cards/guides/08-validation-verification.md`
introduction and Perform Structural Validation; project plan Workflow and acceptance/Current
status and arc plan Sequencing, composition and workflow. Framework routes resolve in the main checkout.
Required-data: unchanged233 inventory current path/hash/typed/body/pilot fields,
all233 actual check results, and complete source bytes of fixtures executed.
Reuse prior schema/index reads by immutable applicability checks; no repeated
semantic corpus or new source acquisition. Record concise extent coverage and
source-cited contract readback in the existing batch record, recover clipped
required output. Binding material unavailable or conflicting blocks its change.

This is a two-site repair and affected checks within the existing assignment,
not a new investigation. Keep the return compact: exact source/planning parent
and candidate, changed paths, witness results including negative, preserved
inputs/applicable checks, all six row dispositions and limits. CC proposes;
CDC accepts. No slice closure, Slice02 prompt, bulk mutation, push/install or
hosted/release acceptance is authorized. Commit the helper and three planning
outputs separately with both trailers:

```text
Co-authored-by: Codex <noreply@openai.com>
Co-authored-by: Billo AI <ai-engineering@billo.systems>
```
