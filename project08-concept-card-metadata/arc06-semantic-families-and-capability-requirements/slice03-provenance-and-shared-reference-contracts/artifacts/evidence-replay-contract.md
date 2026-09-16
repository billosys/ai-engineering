# Evidence and replay contract

Status: CC proposed-done pending independent CDC verification. This is a
planning-evidence convention for Arc06 packets, not a concept-card schema,
specification, validator, parser, runtime, graph service or memory write.
Slice03 accepts zero semantic pairs.

## Contract boundary

Every reusable evidence item has a mechanical identity and an explicitly
bounded meaning. The mechanical identity answers “which bytes or observation
did this route inspect?” The semantic statement answers “what does the
observation support, and what does it not support?” They must remain separate.

| Dimension | Required treatment | What it does not prove |
| --- | --- | --- |
| Root and path | Record `root` (`source`, `planning`, or `absolute`) and the exact `path`. | A path does not establish identity, role or authority. |
| Byte identity | Record `sha256`; for mutable planning authority also record an explicit `authority_commit` and read with `git show COMMIT:path`. | A matching hash proves bytes, not semantic truth or acceptance. |
| Revision | Record the construct's requested/declared revision separately from the Git snapshot used to inspect it. | A parent-card revision does not supply an embedded CQ/reference revision. |
| Original/copy | Record `original` and `copy` paths or an explicit `mapping_id`; compare bytes with `cmp` and hashes. | Equal bytes do not erase lineage or prove the copy was used in a different run. |
| Status | Record opening/endpoint commit, live working-tree status, and whether the read is `snapshot` or `live`. | A clean status is not semantic verification. |
| Role | Record the member role (`rule`, `observation`, `template`, `native-input`, `expected`, `observed`, `control`, or `handoff`) and applicability. | Reference shape or a shared field name does not establish authority. |
| Operation result | Preserve stdout, exit status, stderr presence and a bounded classification (`match`, `successful_no_match`, `tool_error`, `comparison_failure`). | An error status must not be rewritten as absence; a match must not be rewritten as answer adequacy. |
| Interpretation | State the supported claim, scope and limit after recording the raw result. | Query success, byte identity or endpoint resolution does not establish semantic support, verification, admission or operator acceptance. |

## Existing evidence shapes reused

This convention deliberately reuses accepted local planning shapes rather than
introducing a helper or framework:

- Slice02's membership registry uses `root`, `path`, `sha256`, `role`, member
  meanings and evidence IDs. Its evidence IDs remain the reusable register
  pattern, with member-specific roles and exceptions rather than one generic
  authority claim.
- Slice02's case records separate `input`, `path`, `operation`, independently
  authored `expected`, native-derived `observed`, `controls` and `limit`.
  Structural JSON comparison uses parsed values, so object key order is not
  semantic.
- The validation route uses explicit source/planning roots, tool versions,
  `CC_COMMIT`, `git show`, `jq`, `rg`, `shasum`, status checks and exact
  path lists. A committed replay is extracted from the claimed commit, not
  from a later working tree copy.

## Local extensions for this packet

The following names are proposed only for planning evidence and may be reused
by later packets if useful; they are not future profile fields:

```text
evidence_id, root, path, sha256, authority_commit, read_mode,
original_path, copy_path, role, member_scope, operation, stdout,
status, stderr_nonempty, classification, interpretation, limit
```

`authority_commit` is required when a historical plan, ledger or coverage
register is the authority. A live current register instead records its actual
current digest and purpose check; it must not be compared with a stale
historical digest. `read_mode: snapshot` means bytes came from an explicit Git
object; `read_mode: live` means the current worktree was inspected. The
extensions make replay mechanics explicit without assigning authority to a
field shape.

## Pinned inputs for the worked replay

- Source opening HEAD: `e763c661592ff1097a94bb470db9cf924524579d`; source
  status was clean.
- Planning opening HEAD: `ba2dbfd0a30ca4b0fad406d796efc7f54c76e5b6`; planning
  status was clean.
- Historical Slice02 authority commit: `753bacb051c041a75d0c4d36595cfbadd5a9b5eb`.
  Its plan, ledger and current-coverage bytes hash to
  `89ea7c74b6c806471ce4b1bd2243ebb9d502814e9068c34c8c25f2cadd48a151`,
  `31ad0696d41dae69d5e3c9394b91fd9b3799e9e7f2f8dc57ff9c507b7eee9660`, and
  `770b0ea12ff8b260ce10b9cb5fea9a5c63e119993195111176bd6d4889568a03`.
- Frozen native inventory: `project08-concept-card-metadata/arc01-metadata-research-and-requirements/slice01-metadata-inventory-and-research-questions/artifacts/frontmatter-inventory.json`,
  SHA-256 `afc1985f1998da0d1df0bdc5800aada9842e77873271fc65f3ae190c0e057b1b`.
- Current coverage is a live status input, currently 180 accepted / 375
  remaining / zero assigned to Slice03; its live digest is recorded by the
  route, not treated as the historical authority digest.

The historical planning files are deliberately compared with the current
working-tree versions to show review/coverage advancement. The result is a
byte-state observation, not a semantic assertion that either version is true.
The native query case separately demonstrates that an exact lookup can return
a card or a CQ tuple while leaving answer adequacy and support unresolved.

## Failure distinctions

The route retains four different outcomes: a successful match, a successful
no-match from the same operation, a comparator rejection for a wrong expected
identity/revision, and an execution/tool error from a missing input or root.
An incorrect digest is a comparison failure; an invalid Git object/path is a
Git error. Neither is a semantic no-match. Controls must exercise the same
operation as the positive case wherever possible.
