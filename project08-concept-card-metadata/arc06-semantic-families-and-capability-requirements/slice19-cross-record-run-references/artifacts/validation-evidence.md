# Slice19 validation evidence

Status at the first contribution: CC proposed-done. The original direct checks
below document the six-file alternate-assignment packet; Iteration01 results
are recorded in the section at the end. These receipts establish byte identity,
scope, population, address and target-declaration observations; they do not
independently accept semantic meanings.

## Pinned inputs and tools

```text
SOURCE_ROOT=/Users/oubiwann/lab/billosys/ai-engineering
PLANNING_ROOT=/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning
source authority=a5861c4b8e93af932d18cb571415cc570c758240 (clean at opening)
pre-opening planning=5e6310b8 (clean)
current planning before outputs=e60321d801f93614db15cc55fec603da60570d10
Set authority=dee3052c88e0fd9361e74200fd1eea26ade76435
Slice18 candidate=981ef9ff29ef390e186ae782555d0fcb4d9276ed
Slice18 recipe=2ab6679718326fc76ecf2e10d3678f385f086eb0
inventory_sha256=afc1985f1998da0d1df0bdc5800aada9842e77873271fc65f3ae190c0e057b1b
```

Tool readback:

```text
GNU bash, version 5.3.9(1)-release (aarch64-apple-darwin24.6.0)
jq-1.6
ripgrep 15.2.0
shasum 6.02
git version 2.39.5 (Apple Git-154)
```

The inventory was retrieved into a temporary file with:

```bash
git -C "$PLANNING_ROOT" show 5e6310b8:project08-concept-card-metadata/arc01-metadata-research-and-requirements/slice01-metadata-inventory-and-research-questions/artifacts/frontmatter-inventory.json > "$inventory_file"
shasum -a 256 "$inventory_file"
```

Observed digest: `afc1985f1998da0d1df0bdc5800aada9842e77873271fc65f3ae190c0e057b1b`.
The temporary projection files used for bounded readback were
`record-run-refs.json`, `populated-element-projection.json` and
`tuple-frequency.json` under `/private/tmp/slice19-cross-record.C9w5ZX`; the
native input remains the retrieved, hash-checked inventory.

## Exact scope and accounting

The direct derivation command was:

```bash
git -C "$PLANNING_ROOT" show dee3052c88e0fd9361e74200fd1eea26ade76435:project08-concept-card-metadata/arc06-semantic-families-and-capability-requirements/crc-escalation02.md |
  awk '/^~~~json$/{n++;if(n==1){p=1;next} if(n>1){p=1;next}}
       p && /^~~~$/{p=0;next} p' | jq -s '.[2] | {count:length,unique:(unique|length),pairs:.}'
```

It returned `count=19`, `unique=19` and the exact Set C pairs reproduced in
the membership JSON. The membership check was:

```bash
jq -n -e --argjson expected "$scope" \
  --argjson actual "$(jq -c '.scope.assignment' semantic-membership.json)" \
  '$expected|sort == ($actual|sort) and (($expected|unique|length)==19) and (($actual|unique|length)==19)'
```

Exit status: `0`.

The exact-count check was:

```bash
jq -e '(.scope.counts=={"full":555,"accepted":260,"remaining":295,"assigned":19,"outside":276})
  and (.memberships|length==19)
  and ((.memberships|map([.field_path,.record_kind])|unique|length)==19)
  and ((.scope.assignment|map(join("|"))|sort)==(.memberships|map([.field_path,.record_kind]|join("|"))|sort))' semantic-membership.json
```

Exit status: `0`. No accepted pair overlap, duplicate membership or outside
pair was observed. The opening accounting remains assignment-only.

## Native population checks

The population command was the prompt-prescribed direct query, with the eleven
assigned kinds:

```bash
jq --argjson kinds '["claim","competency-question","concept-card","memory-admission","preservation-decision","reconciliation-result","relationship-edge","source-locator","source-support","validation-result","verification-result"]' '
  [.records[]
   | select(.frontmatter == true and .error == null and (.values | type) == "object")
   | select(.record_kind as $kind | $kinds | index($kind))
   | {path, record_kind, root_present:(.values | has("run_refs")), value:.values.run_refs}
  ]' "$inventory_file"
```

Exit status: `0`; result length: `49`. The lossless result is embedded in
`semantic-evidence.md`. A second direct projection inspected every populated
array element and used `has("id")`, `has("path")`, `has("revision")` plus
value-type checks. Exit status: `0`; result length: `26` elements.

Observed census:

```text
claim 1: absent=0 present=1 empty=1
competency-question 2: absent=1 present=1 empty=1
concept-card 31: absent=8 present=23 empty=1 populated=22
memory-admission 2: absent=1 present=1 empty=1
preservation-decision 1: absent=0 present=1 empty=1
reconciliation-result 2: absent=1 present=1 empty=1
relationship-edge 2: absent=1 present=1 empty=1
source-locator 1: absent=0 present=1 empty=1
source-support 5: absent=0 present=5 empty=1 populated=4
validation-result 1: absent=0 present=1 empty=1
verification-result 1: absent=0 present=1 empty=1
total parsed selected=49; populated elements=26
```

The three YAML errors and fifteen no-opening-frontmatter rows were retained as
exclusions by the inventory and were not interpreted as absent fields. The
historical query returned:

```json
{"parsed_records":2054,"root_presence":{"present":0,"absent":2054}}
```

This is a bounded Complete Musician/Erlang comparison, not a universal
historical claim.

## Tuple and target checks

The tuple-frequency query returned:

```json
[
  {"tuple":{"id":"run-arc07-s02-pilot","path":"../extraction-run.md","revision":1},"source_records":8},
  {"tuple":{"id":"run-compcogneuro-rich-rerun-20260912","path":"../README.md","revision":1},"source_records":7},
  {"tuple":{"id":"run-compcogneuro-teaching-rerun-20260912","path":"../README.md","revision":1},"source_records":10},
  {"tuple":{"id":"run-synthetic-field-guide-001","path":"records/run-synthetic-field-guide-001.md","revision":1},"source_records":1}
]
```

Each target was retrieved with a byte-preserving command, not command
substitution:

```bash
target_tmp=$(mktemp /private/tmp/s19-target.XXXXXX)
git -C "$PLANNING_ROOT" show "$target_commit:$target_path" > "$target_tmp"
status=$?
shasum -a 256 "$target_tmp"
sed -n '1,4p' "$target_tmp"
```

Results:

| Case | Git status | Bytes / header | Classification |
| --- | ---: | --- | --- |
| Arc07 pilot | 0 | `01383dc73135ca701dccbb561d479ad88da6324669963defb987e2fa8abf36ea`; opening `record_type: extraction-run`, id `run-arc07-s02-pilot`, revision 1 | exact identity match |
| Rich rerun README | 0 | `4e9a9fe1449f873cd513cd09369fcb975ef0164939008204c10385f2d9a645ec`; first line is `# CompCogNeuro Rich-Profile Rerun` | address resolved, no declared target identity |
| Teaching rerun README | 0 | `e2bedbe19e88992cc0f3969406228a19d837b7c73c88324217a02b10df13898e`; first line is `# CompCogNeuro Teaching-Profile Rerun` | address resolved, no declared target identity |
| Synthetic field guide target | 128 | non-empty Git stderr: `fatal: path 'knowledge/concept-cards/examples/records/run-synthetic-field-guide-001.md' does not exist in 'a5861c4b8e93af932d18cb571415cc570c758240'` | missing target after readable containing-tree control |

For the synthetic case, `git cat-file -e a5861c4b8e93af932d18cb571415cc570c758240:knowledge/concept-cards/examples`
returned status `0`; the specific target returned `128` with non-empty stderr.
This distinguishes a missing target from an invalid source commit or
inaccessible containing tree. No README body text was treated as frontmatter
identity.

## Evidence identity and applicability

The membership registry binds each cited input to root, path/read mode,
authority commit, digest, role, member scope, source range, interpretation and
limit. The principal byte identities are:

```text
Set authority crc-escalation02.md: 7fbb27267077eee831673fe688c60ad8f2e0e96975cf301227f65a037afcb592
alternate prompt: 708a1c05509f571b9f5d901c5303e4e1fdf6b4da1330ed1add050a7ccd2cc9db
slice plan: 62ff10acfb293e05f7ab973deddf4ff6b2ef75d07611c65ad17b347a67983b04
slice ledger opening: 7be1b2408eff05110a871e4328f9b88b8aef8ab30745620906f64645cb9613f2
CDC directive02: 2880d840f9437bd4b56711d2a72e706d69a1e26091deac1ecad073df25a8e1a4
Slice18 CRC: 5479e8c56d6bfacc911a5c1ee768a1152d0abd8213a8389c73a61170299aa74b
Slice18 handoff: 4a1e67598d83ab762bd66b7813117a35833c704ce68a7b853275c0101927070f
replay contract: 73f9ee479261c536f3c96fd9f120aaa709358978c5f9922b9ab8cc77065dd70d
worked replay: 5185ac366c3dd2cbb3e7b0559b989beff770328ec7c574705f037580efb514c8
source SKILL.md: a096893e6a908d014b795bcb2e5e38653b6c590982e99951aae3783a9e7c318a
source rich-profile: 31246186479dd275a4e2f7f1d043dd836e9e2769242a021f8eb56f1b39ef0353
```

The eleven template hashes and all required guide/reference hashes were read
from source authority and are recorded in the membership registry's evidence
role; the complete list is retained in the intake command output and source
readback. No inaccessible object, unknown descriptor or out-of-range source
span was used as verified evidence. The inventory projection is structural and
the full witnesses supply body/context limits.

## Required outcome mapping

| Outcome | Direct evidence | Result |
| --- | --- | --- |
| Exact scope | Set authority block 2, sorted membership comparison, accounting query | pass; 19 unique pairs and 555/260/295/19/276 |
| Complete native states | 49-record projection, 26-element projection, 11-kind census | pass; absent/empty/populated states retained |
| Historical boundary | 2,054-record query | pass; 0 present, 2,054 absent |
| Reference resolution | Four byte-preserving target checks | pass; one exact, two path-only, one missing target |
| Evidence identity/applicability | registry digests, source reads, target hashes and bounded ranges | pass for structural identity; semantic acceptance remains CRC's task |
| Kind-specific interpretation | 19 registry meanings, kind-local consequences and owner-tagged unknowns | CC attestation only; CRC independent review pending |
| Contribution boundary at first contribution | six-path diff, JSON/whitespace/status checks | recorded for the preserved alternate-assignment packet; no seventh output was authorized there |

The alternate verification-method revision supersedes the original committed
wrapper, route extraction, mutation suite, same/distinct endpoint modes and
separate recipe commit for Slice19. Those mechanisms are recorded as
**superseded**, not failed or silently unrun required checks. No custom
verifier, helper, parser, Ruby or Python script was added. No package/source
gate is required for this planning-only packet.

## Failures, blocks and unrun work

No in-scope direct check failed or blocked. The combined witness read was
truncated once by the tool output window and was recovered with four separate
bounded reads before interpretation. The synthetic target's Git status 128 is
an expected missing-target outcome after the containing-tree control, not a
failed validation. CRC semantic review, CDC arc composition, P-15 schema/spec
discussion, repeated real extraction, UAT, Operator quality acceptance,
Slice20/21 and the 248-pair complement remain unrun and out of scope.

## Iteration01 required-reading intake and contract readback

Date: 2026-09-24. Active assignment: `cc-prompt-iteration01.md` at planning
HEAD `ba3850436cf79d5220da21279a5046334986faca`. The source worktree is clean
at `a5861c4b8e93af932d18cb571415cc570c758240`; planning was clean before this
artifact edit. Planning advanced from the prompt's `ed9d38b8` contribution
baseline only by the commit issuing this iteration. `git diff
ed9d38b898a021b1d13e77250cf7b3329fcf8e91..ba3850436cf79d5220da21279a5046334986faca`
touches this slice's new prompt, CRC record, ledger and slice plan; required
prior outputs remain at the committed contribution.

### Required-full manifest

| Input | Source state and loaded extent | Why it governs this repair |
| --- | --- | --- |
| `cc-prompt-iteration01.md` | planning `ba385043`; lines 1-351, complete | Current R1/R2 repair, direct checks, four-path fence and CRC return boundary. |
| `slice-plan.md` | planning `ba385043`; lines 1-266, complete | Assignment history, governing alternate method, scope and iteration readiness. |
| `ledger.md` | planning `ba385043`; lines 1-23, complete | Seven row criteria and prior CRC findings. |
| `crc-verification.md` | planning `ba385043`; lines 1-70, complete | Reproduced results, R1/R2 findings and required changes. |
| `cc-prompt-alt.md` | planning `ed9d38b8`; lines 1-418, complete | Still-governing Set C meanings, Operator-authorized direct method and return boundary. |
| `artifacts/semantic-membership.json` | planning `ed9d38b8`; lines 1-307, complete in bounded reads | Exact repair target, 19 meanings, citations and original registry. |
| `artifacts/validation-evidence.md` | planning `ed9d38b8`; lines 1-218, complete | Existing direct checks and regression record extended here. |
| `closing-report.md` | planning `ed9d38b8`; lines 1-75, complete | Proposed-done claims and prior six-file contribution history to preserve. |
| Slice18 `artifacts/semantic-membership.json` | planning `981ef9ff29ef390e186ae782555d0fcb4d9276ed`; lines 1-562, complete across bounded reads | Atomic evidence-row precedent and its identity/range fields. A large read was truncated; overlapping reads recovered the complete file, including registry lines 525-562. |
| Slice03 `artifacts/evidence-replay-contract.md` | planning `eb7b606baac634f0a3beb3db5d7dcfea26c986e3`; lines 1-93, complete | Separates input identity from supported meaning and preserves operation outcomes and limits. |

### Required-section manifest

| Input section | Source state and loaded extent | Applicable rule |
| --- | --- | --- |
| `artifacts/semantic-evidence.md`: selected-record projection, populated element/child projection, tuple/outcome matrix, rules/observations/inferences/unknowns and kind consequences | planning `ed9d38b8`; lines 59-285, complete | Retain the reproduced semantic observations; repair their durable evidence links without changing meanings. |
| `artifacts/handoff.md` | planning `ed9d38b8`; lines 1-83, complete | Preserve later owners, P-15, UAT, Operator gates and independent review boundaries. |
| source `knowledge/concept-cards/references/semantic-audit-boundaries.md` | source `a5861c4b`; complete 24-line file | A path or structural match cannot establish semantic warrant. |
| source `knowledge/concept-cards/guides/08-validation-verification.md` | source `a5861c4b`; complete 231-line file | Structural identity checks and semantic review are separate; results need target/scope/evidence provenance and limits. |

### Required-data: committed contribution `ed9d38b8`

The following direct queries read the candidate JSON from the contribution
commit, not from the edited worktree. They retain unique declared/cited IDs,
their set difference and duplicates, and lossless member/evidence edges:

```bash
git show ed9d38b898a021b1d13e77250cf7b3329fcf8e91:project08-concept-card-metadata/arc06-semantic-families-and-capability-requirements/slice19-cross-record-run-references/artifacts/semantic-membership.json |
  jq -r '([.evidence_registry[].evidence_id] | unique) as $declared
    | ([.memberships[].evidence_ids[]] | unique) as $cited
    | {declared_unique:$declared,cited_unique:$cited,
       cited_minus_declared:($cited-$declared),
       duplicate_registry_ids:([.evidence_registry[].evidence_id]
         | group_by(.) | map(select(length>1)|.[0])),
       registry_count:(.evidence_registry|length),
       declared_count:($declared|length),cited_count:($cited|length)}'
git show ed9d38b898a021b1d13e77250cf7b3329fcf8e91:project08-concept-card-metadata/arc06-semantic-families-and-capability-requirements/slice19-cross-record-run-references/artifacts/semantic-membership.json |
  jq -r '.evidence_registry[] |
    [.evidence_id,.root,.path,.authority_commit,.sha256,.source_range] | @tsv'
git show ed9d38b898a021b1d13e77250cf7b3329fcf8e91:project08-concept-card-metadata/arc06-semantic-families-and-capability-requirements/slice19-cross-record-run-references/artifacts/semantic-membership.json |
  jq -c '.memberships[] | {meaning_id,field_path,record_kind,evidence_ids}'
```

Observed first-query result: registry rows `19`, unique declared IDs `19`,
unique cited IDs `24`, duplicate declared IDs `[]`, and 17 cited-but-undeclared
IDs: `guidance-admission`, `guidance-evidence`, `guidance-extraction`,
`guidance-graph`, `guidance-preservation`, `guidance-reconciliation`,
`guidance-validation`, `guidance-verification`, `pilot-resolution`,
`rich-card`, `rich-readme`, `rich-rerun-card`, `rich-resolution`,
`synthetic-resolution`, `teaching-readme`, `teaching-rerun-card`, and
`teaching-resolution`. The complete second-query registry projection and
third-query member/evidence projection were read from tool output in full;
their row-level values are recorded in the checked-in JSON at this same
authority and are being replaced by atomic rows and citations in this
iteration. The known mismatch is `run_refs[].id` / `source-support` citing
`rich-profile`, a concept-card witness.

### Source-cited contract readback

- **Scope and authority:** retain all 19 Set C pairs and their observed
  meanings. Do not transfer an assignment into accepted coverage, reopen the
  population or alter schema/requiredness/migration decisions. The active
  prompt's “CRC Findings To Repair,” “Permitted Changes” and “Ledger And Return
  Contract” sections bind this repair; the slice plan's “Authority And
  Assignment,” “Verification Method Decision” and “Binding Boundaries” retain
  `cc-prompt-alt.md` as the semantic/data contract. The project plan's
  “Current Direction” and “Contributor Workflow” sections and Arc06 “Current
  Review” keep the three-contributor workflow, 260/295/19/276 accounting, P-15
  and the unopened successor boundaries in force.
- **Evidence object contract:** Slice03's “Contract boundary” and “Failure
  distinctions” require identity and semantic interpretation to stay
  separate. The current prompt's R1 section requires one retrievable Git-tree
  object per row, with one root, literal path, real authority commit, single
  SHA-256, member scope, source range, interpretation and limit. Therefore
  grouped paths/hashes must split into per-file rows, and temporary projections
  belong in recorded command output, not the registry. The source validation
  guide's “Perform Structural Validation” and “Prevent False Upgrades” sections
  confirm that matching bytes, query success and resolvable targets establish
  structural properties only.
- **Citation applicability:** the prompt's R2 section requires every one of
  the 19 membership-to-evidence edges to apply to that exact field path and
  record kind. The source-support `run_refs[].id` row cannot rely on
  `rich-profile-card.md`, which is a concept-card example. It must instead cite
  the complete inventory projection and the applicable Arc07 source-support
  records and extraction-run target. Shared guidance rows must name the exact
  bounded rule and members to which they apply.
- **Acceptance and preservation:** rows S19-1/S19-3/S19-5/S19-7 remain fresh
  regressions; S19-2/S19-4/S19-6 need new evidence. The same predicates must
  reject dangling/duplicate IDs, bad path/digest/range and the wrong-kind
  witness. Only the four files named in “Permitted Changes” may change. A
  CC-authored ledger walk and closing report remain proposed-done; the separate
  CRC record is required for acceptance, and this context cannot accept its
  own repair.

The specific failure that would invalidate an otherwise plausible repair is
to make the evidence IDs resolve while retaining a witness whose exact
record-kind scope cannot support the member, or to make a digest pass by
binding it to a pseudo-path/multi-object row. Referential closure alone is not
replayability or semantic applicability.

## Iteration01 direct execution and results

Executed 2026-09-24 in the canonical planning worktree. Source remained at
`a5861c4b8e93af932d18cb571415cc570c758240`; planning started at the issued
iteration commit `ba3850436cf79d5220da21279a5046334986faca`, whose parent is the
first contribution `ed9d38b898a021b1d13e77250cf7b3329fcf8e91`. Both source and
planning inputs relevant to this assignment matched their pinned Git blobs.
Tool versions are those recorded above: Bash 5.3.9, jq 1.6, Git 2.39.5 and
shasum 6.02. Temporary inventory/target files were removed after each check;
no helper or script was created.

### Baseline defect reproduced from the contribution commit

The three direct commands above were run against the committed `ed9d38b8`
JSON. They returned registry rows `19`, unique declared IDs `19`, unique
cited IDs `24`, duplicate registry IDs `[]`, and this exact cited-minus-
declared set (17):

```text
guidance-admission guidance-evidence guidance-extraction guidance-graph
guidance-preservation guidance-reconciliation guidance-validation
guidance-verification pilot-resolution rich-card rich-readme rich-rerun-card
rich-resolution synthetic-resolution teaching-readme teaching-rerun-card
teaching-resolution
```

The immutable contribution commit remains the lossless source for the full
19-row pre-repair registry and edge projections; the corrected commands above
recreate the complete results. Its wrong-kind edge was
`run_refs[].id / source-support -> rich-profile`; this iteration removes it.

### R1 row retrieval, digest, range and negative controls

The complete row projection is `.evidence_registry` in
`semantic-membership.json`; it has 49 rows and 49 unique IDs. Each row was
independently resolved as `authority_commit:path` in its declared source or
planning repository, hashed from `git show` bytes with SHA-256, and checked
for an in-bounds non-reversed line range: **49/49 PASS**. The structured-data
range is the explicit descriptor `complete minified JSON object; 2124
records`; its exact one-line blob digest matched. All other ranges are
numeric. Full per-row outcomes, joined to path/hash/range in the JSON, are:

| Evidence IDs | Retrieval, digest and range |
| --- | --- |
| `current-assignment`, `alternate-assignment`, `crc-review`, `slice-plan`, `slice-ledger`, `project-plan`, `arc-plan`, `directive02`, `set-c-authority` | PASS; exact Git object retrieved, SHA-256 matched, range valid |
| `inventory`, `semantic-evidence-projection`, `prior-validation-evidence`, `slice18-crc`, `slice18-handoff`, `slice18-membership-shape`, `slice03-replay-contract` | PASS; exact Git object retrieved, SHA-256 matched, range or whole-object descriptor valid |
| `template-claim`, `template-competency-question`, `template-concept-card`, `template-memory-admission`, `template-preservation-decision`, `template-reconciliation-result`, `template-relationship-edge`, `template-source-locator`, `template-source-support`, `template-validation-result`, `template-verification-result` | PASS; exact source Git object retrieved, SHA-256 matched, range valid |
| `arc07-run`, `arc07-card-emergent`, `arc07-card-memory`, `arc07-card-model`, `arc07-card-pattern`, `arc07-support-emergent`, `arc07-support-memory`, `arc07-support-model`, `arc07-support-pattern` | PASS; exact planning Git object retrieved, SHA-256 matched, range valid |
| `rich-profile-card`, `rich-rerun-card`, `rich-rerun-readme`, `teaching-rerun-card`, `teaching-rerun-readme` | PASS; exact Git object retrieved, SHA-256 matched, range valid |
| `guide-extraction`, `guide-evidence-lifecycle`, `guide-graph-cq`, `guide-preservation`, `guide-reconciliation`, `guide-validation-verification`, `guide-memory-admission`, `guide-semantic-audit-boundaries` | PASS; exact source Git object retrieved, SHA-256 matched, range valid |

The failed mutations used the same object retrieval/hash/range checks as the
positive rows and were applied only to in-memory values:

| Mutation | Rejection oracle | Result |
| --- | --- | --- |
| Append `.missing` to a registered path | `git cat-file -e authority:path` | rejected, Git status 128 |
| Replace a row digest with 64 zeroes | Retrieved SHA-256 equality | rejected, comparison status 1 |
| Set a numeric range end to `line_count + 1` | Numeric bounds predicate | rejected, predicate status 1 |

The frozen inventory at `5e6310b8ef6d48a45b816822cdbc658a62603ba6` returned
SHA-256 `afc1985f1998da0d1df0bdc5800aada9842e77873271fc65f3ae190c0e057b1b`.
Its complete minified object has one physical line; the explicit descriptor
records its structured interpretation and all 2,124 records. The Arc07 run
blob's verified count is 47 newline-terminated lines (earlier CRC prose called
it 50); the exact pinned digest matches, so this is a line-count correction,
not input drift. Rich rerun card/README blobs contain 146/45 lines; their
registered partial ranges remain within bounds.

### R2 member/evidence applicability audit

This lossless command projects every edge with field path, record kind,
evidence ID, registered scope, exact path and role; the output was inspected
in bounded partitions:

```bash
jq -r '.memberships[] as $m | $m.evidence_ids[] as $id |
  .evidence_registry[] | select(.evidence_id==$id) |
  [$m.field_path,$m.record_kind,$id,.member_scope,.path,.role] | @tsv' \
  artifacts/semantic-membership.json
```

All 19 members were inspected. The complete folded edge matrix is:

| Field path | Record kind | Evidence IDs |
| --- | --- | --- |
| `run_refs` | `claim` | `guide-evidence-lifecycle`, `guide-extraction`, `inventory`, `template-claim` |
| `run_refs` | `competency-question` | `guide-extraction`, `guide-graph-cq`, `inventory`, `template-competency-question` |
| `run_refs` | `concept-card` | `arc07-card-emergent`, `arc07-card-memory`, `arc07-card-model`, `arc07-card-pattern`, `arc07-run`, `guide-extraction`, `inventory`, `rich-profile-card`, `rich-rerun-card`, `teaching-rerun-card`, `template-concept-card` |
| `run_refs` | `memory-admission` | `guide-evidence-lifecycle`, `guide-memory-admission`, `inventory`, `template-memory-admission` |
| `run_refs` | `preservation-decision` | `guide-evidence-lifecycle`, `guide-preservation`, `inventory`, `template-preservation-decision` |
| `run_refs` | `reconciliation-result` | `guide-evidence-lifecycle`, `guide-reconciliation`, `inventory`, `template-reconciliation-result` |
| `run_refs` | `relationship-edge` | `guide-extraction`, `guide-graph-cq`, `inventory`, `template-relationship-edge` |
| `run_refs` | `source-locator` | `guide-evidence-lifecycle`, `guide-extraction`, `inventory`, `template-source-locator` |
| `run_refs` | `source-support` | `arc07-run`, `arc07-support-emergent`, `arc07-support-memory`, `arc07-support-model`, `arc07-support-pattern`, `guide-evidence-lifecycle`, `guide-extraction`, `inventory`, `template-source-support` |
| `run_refs` | `validation-result` | `guide-evidence-lifecycle`, `guide-validation-verification`, `inventory`, `template-validation-result` |
| `run_refs` | `verification-result` | `guide-evidence-lifecycle`, `guide-validation-verification`, `inventory`, `template-verification-result` |
| `run_refs[]` | `concept-card` | `arc07-card-emergent`, `arc07-card-memory`, `arc07-card-model`, `arc07-card-pattern`, `rich-rerun-card`, `semantic-evidence-projection`, `teaching-rerun-card` |
| `run_refs[]` | `source-support` | `arc07-run`, `arc07-support-emergent`, `arc07-support-memory`, `arc07-support-model`, `arc07-support-pattern`, `semantic-evidence-projection` |
| `run_refs[].id` | `concept-card` | `arc07-run`, `rich-profile-card`, `rich-rerun-readme`, `semantic-evidence-projection`, `teaching-rerun-readme` |
| `run_refs[].id` | `source-support` | `inventory`, `arc07-run`, `arc07-support-emergent`, `arc07-support-memory`, `arc07-support-model`, `arc07-support-pattern`, `semantic-evidence-projection` |
| `run_refs[].path` | `concept-card` | `arc07-run`, `rich-profile-card`, `rich-rerun-readme`, `semantic-evidence-projection`, `teaching-rerun-readme` |
| `run_refs[].path` | `source-support` | `arc07-run`, `arc07-support-emergent`, `arc07-support-memory`, `arc07-support-model`, `arc07-support-pattern`, `semantic-evidence-projection` |
| `run_refs[].revision` | `concept-card` | `arc07-run`, `rich-profile-card`, `rich-rerun-readme`, `semantic-evidence-projection`, `teaching-rerun-readme` |
| `run_refs[].revision` | `source-support` | `arc07-run`, `arc07-support-emergent`, `arc07-support-memory`, `arc07-support-model`, `arc07-support-pattern`, `semantic-evidence-projection` |

The registered scopes and exact paths show why each edge applies. Shared
extraction guidance names claim, competency-question, concept-card,
relationship-edge, source-locator and source-support. Evidence-lifecycle
guidance names its applicable decision/result kinds. Graph/CQ guidance names
competency-question and relationship-edge. Remaining guidance is kind-specific;
templates support only their named record kind. The inventory and complete
semantic-evidence projection provide the shared native-state observations.
Arc07 extraction-run and support witnesses apply to the populated pilot
members. `rich-profile-card` is concept-card scoped; rerun README witnesses
establish path resolution without target identity.

The positive focused source-support child-ID predicate returned `true`, exit
0. It requires `inventory`, `arc07-run`, all four Arc07 support witnesses and
the shared complete projection. Injecting `rich-profile-card` into that member
made the same path/scope predicate return false, exit 1. Referential integrity
returned `true`, exit 0. In-memory negative controls replacing a cited ID with
`missing-evidence-id` and appending a duplicate registry row each returned
false, exit 1.

### Retained regressions and outcomes

| Check | Result |
| --- | --- |
| JSON parse; registry count/unique IDs; membership count/unique meaning IDs | pass; 49/49 registry IDs and 19/19 memberships/meanings |
| Exact Set C at `dee3052c88e0fd9361e74200fd1eea26ade76435`; sorted comparison and counts | pass; 19/19 pairs, 555/260/295/19/276; jq status 0 |
| Frozen selected native records and populated child elements | pass; 49 records over eleven kinds and 26 populated elements |
| Tuple frequency | pass; pilot 8, rich rerun 7, teaching rerun 10, synthetic target 1 |
| Parse and no-frontmatter exclusions | pass; three distinct YAML parse errors and 15 `no-opening-frontmatter` records |
| Historical Complete Musician/Erlang subset | pass; 2,054 parsed records, roots present 0 / absent 2,054 |
| Arc07 pilot target | status 0; exact extraction-run header, id `run-arc07-s02-pilot`, revision 1; SHA-256 `01383dc73135ca701dccbb561d479ad88da6324669963defb987e2fa8abf36ea` |
| Rich/teaching README targets | both status 0; addresses resolve, README bodies have no opening target identity; hashes match the earlier target matrix |
| Synthetic target | containing tree status 0; exact target status 128 at pinned source commit |
| Membership meaning preservation | pass; after removing only evidence registry and membership evidence IDs, all membership meanings, states, consequences, questions and dispositions compare equal to the first contribution |
| Registry object shape | pass; 49 unique IDs, snapshot read mode, allowed roots, literal relative paths, one full authority and digest, and nonempty range/scope/interpretation/limit; jq status 0 |
| Whitespace and JSON | `git diff --check` status 0; `jq empty` status 0; precommit diff lists exactly the four authorized paths; postcommit clean state and trailers are reported with the contribution return |

The root-state census grouped by kind and preserves absent/empty/populated
distinctions: claim 1/0/1/0; competency-question 2/1/1/0; concept-card
31/8/1/22; memory-admission 2/1/1/0; preservation-decision 1/0/1/0;
reconciliation-result 2/1/1/0; relationship-edge 2/1/1/0; source-locator
1/0/1/0; source-support 5/0/1/4; validation-result 1/0/1/0 and
verification-result 1/0/1/0 (total / absent / empty / populated).

### Execution notes and row disposition

During command construction, a few jq drafts had syntax or iterator-context
errors and were corrected before their output was used. One registry-shape jq
draft applied string containment to the row object; the corrected predicate
returned true, exit 0. Two exploratory Git hash commands also used mistyped
paths and returned status 128; corrected
commands retrieved the pinned blobs. These were authoring errors in exploratory
commands, not acceptance-check failures. The 47-line Arc07 witness count and
the rich-rerun card/README lengths (146/45) were confirmed against pinned
hashes; all recorded ranges are in bounds. A tool-truncated read was recovered
with bounded reads as recorded in the intake.

S19-1, S19-3, S19-5 and S19-7 were rerun as regressions. S19-2, S19-4 and
S19-6 now have CC repair evidence for read coverage, atomic rows, all 19 member
edges and direct rejection controls. All seven ledger rows remain open for
independent CRC verification. CDC composition, P-15, repeated real extraction,
UAT, Operator acceptance, Slice20/21 and the 248-pair complement remain unrun
and out of scope.
