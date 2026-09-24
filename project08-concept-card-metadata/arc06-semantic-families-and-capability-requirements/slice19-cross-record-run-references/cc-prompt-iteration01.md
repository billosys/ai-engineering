# Project08 Arc06 Slice19 Iteration01: Repair Evidence Registration

Execute this first corrective pass for Project08 Arc06 Slice19 in the canonical
`.worktrees/planning` checkout. You are CC in the Operator-selected
Three-Contributor Workflow. CRC independently reviewed the alternate-assignment
contribution `ed9d38b898a021b1d13e77250cf7b3329fcf8e91` and returned two
bounded findings. Repair them and return the packet to CRC. Do not accept the
slice, update coverage, perform CDC composition or open Slice20.

This prompt is `cc-prompt-iteration01.md`. Its predecessor is
`cc-prompt-alt.md`; the original `cc-prompt.md` and alternate prompt remain
preserved. The alternate prompt's Operator-authorized direct-verification
method still governs. Do not reintroduce its superseded wrapper, mutation
battery, same/distinct recipe endpoint or standalone verifier.

## Baseline And Authority

At prompt authoring:

- source HEAD and authority:
  `a5861c4b8e93af932d18cb571415cc570c758240`, clean;
- planning HEAD and first contribution:
  `ed9d38b898a021b1d13e77250cf7b3329fcf8e91`, clean;
- frozen inventory authority: planning `5e6310b8`, SHA-256
  `afc1985f1998da0d1df0bdc5800aada9842e77873271fc65f3ae190c0e057b1b`;
- exact Set C authority:
  `dee3052c88e0fd9361e74200fd1eea26ade76435`.

Recheck both worktrees and relevant pinned bytes. Stop on material drift. An
unrelated global HEAD advance is not itself failure when every affected input
remains byte-identical and the difference is recorded. Preserve unrelated work.

## What CRC Accepted As Reproduced

Do not reopen or rewrite these results unless actual pinned evidence now
contradicts them:

- exact 19-pair Set C and 555/260/295/19/276 opening accounting;
- 49 selected parsed records across eleven kinds;
- 26 populated references: 22 concept-card and four source-support elements;
- four tuple frequencies: 8, 7, 10 and 1;
- three YAML errors and fifteen no-frontmatter exclusions;
- 2,054 parsed Complete Musician/Erlang records with zero `run_refs` roots;
- one exact extraction-run target, two path-only README targets and one missing
  synthetic target after a readable containing-tree control;
- all 19 bounded, kind-local meanings and the no-authority-inheritance rule;
- Slice20/21, 248-pair complement, P-15, real extraction, UAT and Operator
  ownership boundaries.

Fresh regression checks must prove these remained unchanged. Earlier success
receipts are context, not evidence that this iteration ran.

## Required Reading And CC Intake

Record the completed manifest and a source-cited contract readback in the
iteration section of `artifacts/validation-evidence.md` before editing the
registry.

### Required-full

Read these files completely from the current planning state:

1. `cc-prompt-iteration01.md` -- current assignment;
2. `slice-plan.md` and `ledger.md` -- current assignment history and open rows;
3. `crc-verification.md` -- R1/R2 evidence and required correction;
4. `cc-prompt-alt.md` -- still-governing scope, direct-check method and return
   boundary;
5. `artifacts/semantic-membership.json` -- exact repair target;
6. `artifacts/validation-evidence.md` -- existing direct checks to extend;
7. `closing-report.md` -- current proposed-done report to revise;
8. Slice18 `artifacts/semantic-membership.json` -- atomic evidence-row shape;
9. Slice03 `artifacts/evidence-replay-contract.md` -- evidence identity and
   applicability boundaries.

Recover every truncated read with contiguous bounded reads. A successful file
existence/hash command is not a complete text read.

### Required-section

Read the following current sections completely:

- `artifacts/semantic-evidence.md`: complete selected-record projection,
  populated reference projection, documented rules/observations/inferences and
  kind-specific consequences. These are retained semantic evidence.
- `artifacts/handoff.md`: bounded findings, later ownership and review boundary.
- source `knowledge/concept-cards/references/semantic-audit-boundaries.md` at
  `a5861c4b`: evidence limits and structural-versus-semantic distinctions.
- source `knowledge/concept-cards/guides/08-validation-verification.md` at
  `a5861c4b`: validation/verification authority boundaries.

### Required-data

From committed contribution `ed9d38b8`, derive:

1. the unique evidence IDs cited by all 19 memberships;
2. the unique evidence IDs declared by the registry;
3. cited-minus-declared and duplicate-ID sets;
4. every registry row's root, exact path, authority, digest and range;
5. all membership/evidence edges grouped by field path and record kind.

Retain complete outputs or lossless partitions. The current expected defect is
17 cited-but-undeclared IDs; derive it rather than forcing it. Report any
discrepancy before dependent edits.

## CRC Findings To Repair

### R1: referentially closed, atomic and durable evidence registry

Every membership `evidence_ids` value must resolve to exactly one registered
`evidence_id`. Every registered input row must describe one independently
retrievable evidence object:

```json
{
  "evidence_id": "unique-stable-id",
  "root": "planning",
  "path": "one/exact/repository/path.md",
  "read_mode": "snapshot",
  "authority_commit": "one-real-git-commit",
  "sha256": "one-64-hex-digest",
  "role": "observation",
  "member_scope": "specific members or bounded shared role",
  "source_range": "one validated range or explicit whole-file descriptor",
  "interpretation": "what this exact object supports",
  "limit": "what it cannot establish"
}
```

Binding decisions:

- Split grouped pseudo-path/multi-hash entries into one row per actual file
  whenever a component is cited as evidence. This applies to prompt/plan
  bundles, Arc07 card/support sets, rerun cards/READMEs, templates, guidance and
  prior-contract bundles.
- Keep one real Git authority per snapshot row. Do not use values such as
  `5e6310b8 inventory`, `5e6310b8 and a5861c4b` or a concatenated authority.
- Keep one SHA-256 per row. A label plus several hashes is not a digest field.
- Remove the three `/private/tmp` projection rows as registered inputs. They are
  non-durable derived receipts. Cite the frozen inventory for the native data
  and the committed `semantic-evidence.md` sections for the durable projection;
  validation may recreate temporary files without registering them as inputs.
- Derived target outcomes are checks, not fabricated source documents. Bind
  member claims to the actual containing record, target file when present,
  source/preserved tree and guidance. Keep the missing-target result in the
  validation/semantic outcome matrix after confirming the real containing tree.
- It is acceptable for a rule/handoff registry row not to be cited by a
  membership when the packet genuinely uses it at assignment scope. Do not
  delete governing evidence merely to make an unused-set count zero. Dangling
  membership citations, duplicate IDs and non-retrievable rows are failures.
- Do not change any effective meaning merely to simplify evidence linkage.

Recommended mapping shape:

- `inventory` supports complete root/element/child observations;
- individual `template-<kind>` rows support that kind's template state;
- individual `arc07-card-<slug>` and `arc07-support-<slug>` rows support the
  respective record kind;
- individual `rerun-rich-card`, `rerun-rich-readme`,
  `rerun-teaching-card`, `rerun-teaching-readme` rows support path-only cases;
- `rich-profile-card` supports only the synthetic concept-card case;
- individual guidance rows support only the meanings to which their named
  sections apply;
- `arc07-run` supports the exact extraction-run declaration/identity target.

Names may differ, but the one-ID/one-object/one-authority/one-digest contract
and member applicability are binding.

### R2: member-specific witness applicability

Audit all 19 membership evidence lists after R1. A cited row must support that
exact field-path/record-kind observation or explicitly supply a bounded shared
rule that applies to it.

The known wrong-kind case is:

```text
field_path: run_refs[].id
record_kind: source-support
current evidence id: rich-profile
```

`rich-profile-card.md` is a concept-card witness. It cannot establish a
source-support child. Replace it with the frozen inventory, Arc07 support
witnesses and Arc07 run target as applicable. Check the other eighteen members
for the same class of mismatch; do not assume an evidence ID is applicable
because its prose mentions a similar child name.

## Implementation Spine

1. Complete intake and contract readback before edits.
2. Derive the current cited/declared ID sets and preserve the defect output.
3. Design the atomic registry IDs and exact member-to-evidence edge list on
   paper or in temporary shell variables; do not create a helper file.
4. Replace the registry rows and membership `evidence_ids` in
   `semantic-membership.json`. Preserve exactly 19 memberships, meanings,
   observed states, consequences, questions and dispositions.
5. Extend `validation-evidence.md` with a dated Iteration01 section containing
   the exact direct commands, tool versions, commits, exits and complete/folded
   outputs used for R1/R2 and regressions.
6. Update `ledger.md` and `closing-report.md` for this iteration. Preserve CRC's
   changes-required history and identify this prompt as the executed assignment.
7. Inspect the exact four-file diff, run whitespace/JSON checks, commit only
   those four files and return the contribution commit to CRC.

## Direct Checks And Oracles

Run these checks against the candidate contribution. Equivalent direct jq/Git/
hash commands are allowed only when they preserve the same or stronger oracle.

### Referential integrity

This predicate must return true and status 0:

```bash
jq -e '
  ([.evidence_registry[].evidence_id]) as $registry
  | ([.memberships[].evidence_ids[]] | unique) as $cited
  | (($registry | length) == ($registry | unique | length))
    and (($cited - ($registry | unique)) == [])
    and ([.memberships[] | select((.evidence_ids | length) == 0)] | length == 0)
' artifacts/semantic-membership.json
```

Run a negative control against an in-memory copy with one membership evidence
ID replaced by `missing-evidence-id`; the same predicate must return status 1.
Run another with one duplicate registry ID; it must return status 1. Do not
modify the committed candidate for controls.

### Atomic row retrieval, digest and range

For every registry row:

- root must select exactly one allowed repository (`planning` or `source`);
- `authority_commit` must resolve in that repository;
- `path` must be one literal Git-tree path, not a glob, brace expression,
  prose bundle, comma/`and` list or absolute temporary path;
- retrieving `authority_commit:path` must succeed;
- SHA-256 of the retrieved bytes must equal the row's single lowercase 64-hex
  digest;
- numeric line ranges must be in bounds and non-reversed; explicit whole-file
  or structured-data descriptors must name their interpretation and remain
  inspectable.

Record the complete row result table. A suggested row projection is:

```bash
jq -r '.evidence_registry[] |
  [.evidence_id,.root,.authority_commit,.path,.sha256,.source_range] | @tsv'
  artifacts/semantic-membership.json
```

Use byte-preserving temporary files for hash comparison. Add direct negative
controls that alter, in memory and one at a time: a path, a digest and a
numeric range. Each must be rejected by the same check used for valid rows.
Do not add a committed verifier or standalone script.

### Kind applicability

Construct a direct member/evidence projection containing field path, record
kind, evidence ID, evidence `member_scope`, exact evidence path and role.
Inspect all 19 members. Add a focused predicate that rejects the known invalid
edge: a source-support membership satisfied only by the concept-card-only
`rich-profile-card` witness. The positive source-support ID member must cite
the inventory plus applicable Arc07 support/run inputs. Record why shared
guidance applies where used.

The wrong-kind negative control must return status 1 when the concept-card-only
witness is injected into that source-support member without an applicable
shared role. A textual ID match alone is not the oracle; use row path/scope and
the member's record kind.

### Retained regressions

Re-run and record:

- JSON parse and exact 19 memberships/19 meaning IDs;
- exact Set C and 555/260/295/19/276 accounting;
- 49-record census, 26 populated elements and 8/7/10/1 tuple frequencies;
- three YAML errors, fifteen no-frontmatter exclusions and 2,054 historical
  records with zero roots;
- all four target outcomes at the pinned authority;
- exact four changed paths for this iteration;
- `git diff --check`, required trailers and clean final worktrees.

The Operator-authorized direct method remains binding. Wrapper/recipe endpoint
and broad mutation machinery are still superseded, not failed or unrun gates.

## Permitted Changes

Change exactly these four files:

```text
project08-concept-card-metadata/arc06-semantic-families-and-capability-requirements/slice19-cross-record-run-references/artifacts/semantic-membership.json
project08-concept-card-metadata/arc06-semantic-families-and-capability-requirements/slice19-cross-record-run-references/artifacts/validation-evidence.md
project08-concept-card-metadata/arc06-semantic-families-and-capability-requirements/slice19-cross-record-run-references/ledger.md
project08-concept-card-metadata/arc06-semantic-families-and-capability-requirements/slice19-cross-record-run-references/closing-report.md
```

Do not edit `semantic-evidence.md`, `handoff.md`, any prompt, `slice-plan.md`,
`crc-verification.md`, parent plan/ledger, coverage register, prior packet,
source file, baseline snapshot, schema, runtime, package, extraction output or
memory surface. If a validated semantic statement itself requires change, stop
and return the contradiction to CRC rather than broadening this repair.

No Ruby or Python. No new helper/script file. Use direct bounded Bash, jq, Git,
hash and text inspection.

## Stop Conditions

Stop and report without reducing scope if:

- a pinned input or reproduced semantic/data result materially differs;
- one registry row cannot be represented as a durable exact input without a
  new evidence artifact or source change;
- a member's meaning lacks applicable evidence after the audit;
- a required fix would change schema, requiredness, migration, target identity
  policy or acceptance criteria;
- any fifth path would need to change;
- context truncation cannot be recovered before dependent edits.

CRC resolves routine review questions. Architecture, scope or acceptance
changes escalate through the Operator to CDC.

## Ledger And Return Contract

Walk all seven S19 rows. S19-1, S19-3, S19-5 and S19-7 are reproduced
regressions, not permission to omit them. S19-2, S19-4 and S19-6 require fresh
repair evidence. CC may mark the iteration proposed-done; only CRC can accept
the slice and transfer coverage.

Commit with explicit full filenames using `git commit --only --` and include
exactly once:

```text
Co-authored-by: Codex <noreply@openai.com>
Co-authored-by: Billo AI <ai-engineering@billo.systems>
```

Return:

- this assignment path and source/planning baseline;
- contribution commit and exact four changed paths;
- intake/readback pointer;
- registry/citation counts and all direct-check outcomes;
- the member/evidence applicability audit result;
- retained regression results;
- per-row attestation, deviations, failures and unrun work;
- clean/dirty final state.

CRC independent verification, CDC composition, P-15, repeated real extraction,
UAT and Operator acceptance remain pending.
