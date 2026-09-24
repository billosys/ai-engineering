# Slice19 validation evidence

Status: CC proposed-done. Direct checks below are receipts for the six-file
planning packet. They establish byte identity, scope, population, address and
target-declaration observations; they do not independently accept semantic
meanings.

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
| Contribution boundary | final six-path diff, JSON/whitespace/status checks | pending final commit value; no seventh output authorized |

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
