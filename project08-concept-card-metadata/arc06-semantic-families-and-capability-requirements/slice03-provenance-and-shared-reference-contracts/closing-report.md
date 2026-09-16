# CC Proposed-Done: Arc06 Slice03

Status: proposed-done pending independent CDC verification. This is the
reusable evidence/replay mechanics packet only. It accepts zero semantic
pairs, does not adopt a concept-card schema or specification, and does not
open Slice13.

## Pinned state

- Source opening HEAD: `e763c661592ff1097a94bb470db9cf924524579d`; source was
  clean and remains read-only.
- Planning opening HEAD: `ba2dbfd0a30ca4b0fad406d796efc7f54c76e5b6`; planning
  was clean before this packet.
- CC endpoint: pending until the exact five-file planning commit is created;
  the committed replay must use that SHA as `CC_COMMIT`. Later CDC edits are
  not part of the CC endpoint.
- Current accounting remains 180 accepted / 375 remaining / zero assigned to
  Slice03. No membership was added or removed.
- Historical authority case pins Slice02 CC commit
  `753bacb051c041a75d0c4d36595cfbadd5a9b5eb`; current review/coverage state is
  read live and is not substituted into the historical snapshot.

## Row walk

All five opening rows are addressed exactly once and are CC-attested, not
independently closed.

| Row | CC disposition | Evidence |
| --- | --- | --- |
| S3-1 | done (CC-attested): role, path, hash, Git authority, original/copy, live/snapshot status, operation result and interpretation are kept separate. | `artifacts/evidence-replay-contract.md`; `artifacts/worked-replay.md` |
| S3-2 | done (CC-attested): explicit historical Slice02 bytes reproduce their pinned hashes; current live files are purpose-checked separately; wrong digest and invalid Git path produce distinct failures. | `artifacts/worked-replay.md` |
| S3-3 | done (CC-attested): native legacy lookup and current CQ tuple compare structurally; reordered keys pass; wrong question, wrong ID/revision and missing inventory exercise bounded controls. | `artifacts/worked-replay.md` |
| S3-4 | done (CC-attested): one literal route declares tools/cwd, supports pre-commit and committed modes, checks source/protected history, exact five-file scope, JSON outcomes and whitespace. | `artifacts/worked-replay.md` |
| S3-5 | done (CC-attested): handoff retains all original provenance/shared-reference semantics for Slice13, gives a concrete bounded first unit, and names cross-owner/P-15 limits. | `artifacts/handoff.md` |

## Validation and controls

The final route is designed to run in two explicit modes. `CC_PRECOMMIT=1`
unites unstaged tracked changes, staged tracked changes and the five named new
outputs. Committed mode reads the route from `git show CC_COMMIT:path`, checks
the exact five-file diff from the opening planning HEAD, and protects source,
coverage registers and accepted Slice01/02/12 packets.

The committed-authority case uses historical plan/ledger/coverage bytes from
`753bacb0`, then checks current coverage's own purpose and 180/375/0 values.
The native-query case derives both legacy result arrays and the rich-profile CQ
tuple from the frozen inventory. Expected objects are authored separately;
observed objects are constructed from command output. Structural JSON equality
is used rather than key-order-sensitive text comparison. The route preserves
missing `answer_criteria`, null `memory_admission_ref` and empty
`preservation_refs` states.

The route retains actual failure classes: wrong digest comparison status 1;
invalid Git path status 128 with stderr; wrong question successful no-match
status 0; wrong CQ identity/revision comparator status 1; and missing inventory
jq status 2 with stderr. None is promoted to semantic absence or answer
warrant.

## Artifact inventory and exact scope

Exactly five writable files are delivered:

1. `.../slice03-provenance-and-shared-reference-contracts/artifacts/evidence-replay-contract.md`
2. `.../slice03-provenance-and-shared-reference-contracts/artifacts/worked-replay.md`
3. `.../slice03-provenance-and-shared-reference-contracts/artifacts/handoff.md`
4. `.../slice03-provenance-and-shared-reference-contracts/ledger.md`
5. `.../slice03-provenance-and-shared-reference-contracts/closing-report.md`

No `cdc-verification.md` was created. No plan, current coverage register,
workload observation, source file, prior packet, package, install, runtime,
extraction, database, graph or memory file changed.

## Bubble-up to Arc06

Slice03 delivered the arc-plan assignment: a reusable local evidence/replay
contract with two worked native cases, without building a general framework or
accepting semantic pairs. The work confirms rather than changes the current
Arc06 split: operational replay belongs here; provenance/shared-reference
semantics remain with planned Slice13.

The only sizing finding is already represented in the current arc plan: the
former combined workload is too large. The handoff recommends a candidate
Slice13A of actor/actor.id across four record kinds (8 pairs), followed by a
separate actor.mode/actor.role unit if the first census supports it. This is a
future sizing proposal, not an assignment. No new arc-plan change is proposed.

Silent-drop check: specified scope was three artifacts, five ledger rows, one
close report, two worked cases, all listed controls and exact five-file scope;
delivered scope is the same. Provenance semantics, schema/specification,
source truth, operator acceptance and next-slice execution remain explicitly
outside this close.

CDC must independently rerun the committed route, inspect the actual five-file
diff and decide all five rows. Until then this report and ledger remain
CC-attested/proposed-done.
