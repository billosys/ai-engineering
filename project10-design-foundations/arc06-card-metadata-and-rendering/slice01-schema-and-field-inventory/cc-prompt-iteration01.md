# CC Iteration01 — Repair metadata helper write safety

Execute **Arc06/Slice01 Iteration01** in the Two-Contributor Workflow; CDC Sofie
is independent reviewer via Operator relay, Expedited Mode. This prompt is
`cc-prompt-iteration01.md`, predecessor [cc-prompt.md](cc-prompt.md). Issuing
commit is the planning commit introducing I1, predecessor `be623972b71f7be1002ed3932743c16a23dadb95`.
Current main input `fe4e055885983be6d0b4bbbff1ef201485499aac`; helper SHA-256 `72a278c2561d5383e110295cb4530dac511f4b40d5a591ab79ab72ce224f7eca`.
Read [current slice plan](slice-plan.md), [ledger](ledger.md) and
[initial CDC review](cdc-verification.md) before edits.

S01-01/02/03 are independently done. S01-04/05/06 remain open for F01/F02.
The ten cards,233-row inventory, schema3.2 existing-field mapping, body/value
preservation and version/history are already sound. Complete the same correction;
no new census, corpus mutation, schema decision or hosted-source acquisition.

## Exact delta scope

**Main: only `scripts/normalize-design-card-metadata.rb`.** Keep every card,
all eight live Markdown files, skill metadata/history1.0.4, parser/emitter/
transform meanings, sources, packaging lists and other skills unchanged.
The helper is unbundled repository tooling; no new skill version bump is needed.
Only records' private recovery bytes, write-time checks/recovery/diagnostics and
removal of private buffers before JSONL output may change. Do not change current
`--check` JSONL observations, canonical serializer or four sentinel rules.

**Planning: only** this slice's `artifacts/batch-record.md`, `ledger.md`
(evidence/notes only; CDC owns statuses), and `closing-report.md`.
Append labelled I1 evidence/current dispositions and retain earlier receipts.
Inventory, initial/current issued prompts, CDC review, plans, preparation,
Project08 and parent ledgers are protected. Do not add another supporting file.
Tests run in disposable fixtures; no live pilot/bulk card write or publish/push.

## F01 binding repair recipe

The current top-level write loop at source242–244 silently uses stale snapshots;
its outer rescue does not identify partially written targets. Use these shapes:

1. Retain each process record's original raw bytes in a private buffer alongside
   its input hash/output bytes. Never serialize that buffer in `--check` or
   successful `--write` JSONL. Existing public record fields remain exact.
2. Add an internal guard such as `ensure_unchanged!(record)`: verify the target
   remains an allowed regular, non-symlink input under the existing path rules,
   and freshly hash it against the captured `input_sha256`. On mismatch raise a
   path-specific conflict before that target is replaced. Check **all** snapshots
   before the first write and the current target again just before replacement.
   Do not reparse changed content and quietly adopt it as the new baseline.
3. Add a batch write method such as `write_records!(records)`. Use existing
   same-directory `atomic_replace` per file; record completed writes in order.
   On a later conflict/I/O error, stop immediately. In reverse completed order,
   restore captured originals only when each current target is still a regular,
   non-symlink file whose complete bytes equal this command's recorded output.
   Leave externally changed/missing/symlink targets untouched and identify them
   as held. A restore exception becomes an explicit recovery failure; it must
   not hide the original error or prevent accounting for other completed paths.
4. Report written/restored/held/recovery-failed paths and original failure to
   stderr, and exit nonzero even when recovery succeeded. Emit no success-only
   JSONL for an interrupted batch. Clear private byte buffers before normal
   successful output. Preserve prevalidation-before-any-write and no-argument
   nonmutation. No blind restore of external work or promise of all-file atomicity.

Recommended pseudocode (binding order/policy, local names discretionary):

```ruby
records = paths.map { |path| process(path) } # retain private original bytes
written = []
begin
  records.each { |record| ensure_unchanged!(record) }
  records.each do |record|
    ensure_unchanged!(record)
    atomic_replace(target(record), record['output'])
    written << record
  end
rescue StandardError => original_error
  # For every completed record in reverse order:
  # current == own output and still safe regular target -> restore original
  # otherwise -> leave untouched, report held
  # catch each restore error separately; report recovery-failed
  report_interruption(written, restored, held, recovery_failed, original_error)
  raise original_error
end
```

CDC exercised this shape in temporary source copies: detected prewrite conflict,
restored first output on second-rename failure, and preserved an external edit
during recovery. That prototype is author preparation, not a supplied accepted
source patch. This is optimistic snapshot conflict detection and per-file atomic
replacement; coordinate overlapping writers and disclose the check-to-rename
interval. No claim of atomic cross-process compare-and-swap or transactional batch.

## F02 and accurate current return

The original batch's sentinel table incorrectly includes aliases for additive-
colour-mixing and colour-gamut. Those aliases are populated nested arrays and
were correctly preserved. Append a current correction citing the pinned headers/
inventory: additive delta fields prerequisites/extends; gamut prerequisites/
extends/contrasts_with. Actual pilot total remains16 across six cards. Label the
old entries as historical discrepancies without flattening or editing any card.
Record preserved non-flat aliases as a strict string-list conformance limitation,
not invented metadata or a newly accepted4.0 profile.

## Discriminating checks and return

Use **isolated tracked repositories** with the exact helper candidate copied to
scripts/ and original `1489e767` additive/matrix card blobs at their real paths.
The reproducible two-case hook fixture is in the CDC review; its revision
argument lets you run it against your candidate. Cover:

| Action | Required observation |
|---|---|
| Ordinary two-file conversion | Exit0; two expected public JSONL records, exact mapping/body preservation and byte-idempotence; no private byte buffers emitted. |
| First input externally edited while second is prevalidated | Nonzero; external first edit retained; neither input normalized; conflict names its target. |
| Second replacement fails after first completed | Nonzero; first original recovered, second original untouched; stderr identifies written/restored paths and original failure. |
| Completed first output externally edited before recovery | Nonzero; external edit retained; held path reported; no false all-originals recovery claim. |
| Recovery itself fails | Nonzero; failed restoration path and original failure both reported; all completed paths accounted for. |
| Late second-target conflict after first write | Nonzero; second external edit retained; first own output safely restored; exact written/restored/held accounting. |
| Invalid second input or duplicate path | Nonzero before writes; first original unchanged. No arguments exit0 without mutation. |

Run `ruby -c` and actual candidate `--check` all233, including ten pilot
idempotence, exact public typed/hash/body observations and preserved233 inventory
applicability. Reuse accepted parser/serialization/eight controls only after a
method-byte/diff applicability check; rerun if affected. Verify no private buffer
appears in public records. Tests must reach actual CLI/write helpers with hooks,
not hand-maintained success/failure models or a new testing framework.

Current fresh CDC Make/package gates are accepted at `fe4e055885983be6d0b4bbbff1ef201485499aac`.
Because only an unbundled helper changes, preserve them after verifying every
one of the eight packaged-source Markdown inputs, version/history and Makefile/
package dependencies remains exact. A new ZIP build is unnecessary for an
unchanged payload; any meaningful package drift needs fresh affected gates.
Run source/planning `git diff --check`, exact committed parent/path/trailer
checks and changed local links/LF/EOF checks.

Required-full: this I1 prompt and CDC review; current helper; slice ledger. Required-section: slice-plan.md Assignment history and I1 author
readiness; initial
recipe step5 and original no-fill/no-loss scope, Project10 Evidence economy/
Workflow, Arc06 current workflow; work-verification correction-retention route
and relevant concept-cards structural-validation boundary. Required-data:
protected233 inventory input hashes/deltas, all233 actual `--check` observations
and complete fixture source bytes for the named write-path cases above. Prior
schema/index/corpus reads may be retained by explicit immutable input comparison;
no repeated full-corpus narrative read. Record concise intake and source-cited
contract readback before mutation in the existing batch record; recover clipped
required output. Held mapping disagreement returns to CDC, not unilateral expansion.

Commit only the named main helper and three planning outputs separately with:

```text
Co-authored-by: Codex <noreply@openai.com>
Co-authored-by: Billo AI <ai-engineering@billo.systems>
```

Return source/planning candidates and parents, exact paths, all witness exits/
written-restored-held outcomes, positive233/ten results, applicability, preserved
card/inventory bytes, failures/unrun checks and all six ledger dispositions.
Accepted S01-01/02/03 stay done; S01-04/05/06 stay open pending CDC review.
No slice closure, Slice02 opening, hosted/fidelity/parent acceptance is claimed.
