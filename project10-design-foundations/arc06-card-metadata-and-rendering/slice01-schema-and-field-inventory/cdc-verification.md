# Arc06 Slice01 independent CDC verification

## Initial return — 2026-10-12

**Current verdict: S01-01/02/03 done; S01-04/05/06 open. Slice01 remains open.**
CDC Sofie independently reviews separate CC via Operator relay, Two-Contributor
Workflow, Expedited Mode. Issued initial prompt at `e87186057c4795dfc342f15e06dc8e5a031c9ad2`;
source candidate `fe4e055885983be6d0b4bbbff1ef201485499aac`, parent `1489e76730b759f01fb1e839a18b363d8296b610`;
planning candidate `be623972b71f7be1002ed3932743c16a23dadb95`, parent `e87186057c4795dfc342f15e06dc8e5a031c9ad2`.
No CDC source change or parent acceptance. The next CC assignment is
[Iteration01](cc-prompt-iteration01.md), not bulk conversion.

## What worked and independently reproduced evidence

Both parents and exact13 main/four planning path scopes reproduce; both commits
have the separately required trailers. Issued initial plan/prompt/preparation
and all six criterion/verification/significance/origin/status fields remain exact.
SKILL differs only in metadata1.0.3→1.0.4; sibling history appends its corresponding
entry. No other live guide, original source or unassigned card changed.

CDC read the actual helper, complete batch/report, current plans and all13/seven
parent criteria; applied concept-cards' structural-versus-semantic distinction
and the no-fill preservation rule. Historical3.2 definition/index hashes match
the issued pins. Project08 P-15 remains open; no skill-release inference or4.0
adoption. The field-by-field crosswalk covers all19 core fields and all three
observed extensions. Authors remain scalar; populated nested arrays, nulls,
absence, Unicode and source/relationship/CQ values are retained. This is the
accepted existing-field mapping, not full schema conformance or semantic warrant.

CDC replayed the complete233-row inventory from committed bytes with strict
JSON duplicate-key rejection. All233 paths match the accepted baseline index;
all baseline card blobs equal the issuing main input. Every raw header, file
hash, typed original/current value, index record, revision and body hash/length
reproduces. An independent Perl YAML::XS0.82/JSON::PP4.06 decoder read the pinned
raw headers, not CC's typed projection, and agrees on every complete object.
All233 bodies are byte-identical. Ten actual pilots and223 untouched cards form
an exact disjoint233 union; the ten cover all eight raw source-author identities.
There are16 permitted sentinel changes across six pilots; all other values and
223 files remain unchanged. Original106 sentinels across59 cards reproduce:
aliases13/prerequisites14/extends42/contrasts_with37.
The inventory is1,789,888 bytes, SHA-256
`c7306e8a62291fa635e154463553fd990a9b12d91d70cb4403a0259f9e49dd5c`.

Actual helper `--check` passes all233 with matching current input/typed/body
identities; all ten pilots are byte-idempotent. The positive packet and eight
actual serialized loss/null/invention/duplicate/BOM/fenced/body controls reproduce.
Four additional nested-duplicate/alias/merge/custom-tag AST specimens reject.
Isolated tracked-card CLI fixtures confirm no-argument nonmutation and no writes
on out-of-scope-second-input or repeated-path prevalidation failures. These do
not test the later write-time conflict/I/O paths; F01 below does.

## Source and package checks

Fresh CDC main `make help`, `make check-skills`, `make check-package-paths` and
`make design` exit0; the package-path gate includes version checks:24 source
skills/24 packages/zero errors. Zero hard path failures,596 warnings at594
locations, three exceptions and681 skipped external URLs. The soft18-description
notice remains, design360 characters. All eight actual ZIP Markdown members
match committed source individually; cards/helper are unbundled source inputs.
Fresh CDC ZIP SHA-256 `010283b1ee0588fde91b996fba7465f9a87650dded18b5794f9c8b2c4a61bc06`.
Source/planning committed `git diff --check` pass. CC's initial sandbox denial,
Unicode byte-offset correction and other failed/recovered helper/assertion
attempts remain disclosed. Their recovered structural checks are reproduced;
no clean or browser/fidelity result is fabricated.

## F01 — Write-time drift and interrupted-batch recovery are missing

At `fe4e055885983be6d0b4bbbff1ef201485499aac`, `scripts/normalize-design-card-metadata.rb:242–252` reads every
input into records, then writes the saved outputs without checking their current
contents. `process` keeps hashes but no original-byte recovery buffer. A later
rename failure prints only the exception and no written/restored/held path list.
The issued recipe explicitly requires rejection of conflicting edits and
honest partial-batch recovery; early validation alone does not supply either.

CDC copied the exact helper and two actual original card blobs into disposable
tracked repositories. A File.binread hook changed the first input after it was
read, while the second input was being prevalidated: the real CLI returned0,
wrote two records and erased the external edit. A File.rename hook failed the
second replacement: exit1, no JSONL output, first card remained converted,
second untouched, stderr only `CDC injected second-target rename failure`.
No main card or helper was modified by these witnesses. This is a reproduced
write-safety defect, not a hypothetical warning about future work.

The executable fixture below pins the old helper by default; a candidate revision
argument permits the same witness against the fix. It copies source bytes and
initializes only temporary repositories. The result must show conflict exit1
with the external first edit retained and second untouched; interruption exit1
with both originals recovered, or an explicit un-restored path and reason if
safe recovery is unavailable. It must never label a failed batch successful.

```python
from pathlib import Path
import subprocess,os,tempfile,json,hashlib,sys
R=Path('/Users/oubiwann/lab/billosys/ai-engineering');baseline='1489e76730b759f01fb1e839a18b363d8296b610';helper_ref=sys.argv[1] if len(sys.argv)>1 else 'fe4e055885983be6d0b4bbbff1ef201485499aac';helper_bytes=subprocess.check_output(['git','show',helper_ref+':scripts/normalize-design-card-metadata.rb'],cwd=R);paths=['knowledge/design/concept-cards/posts/additive-colour-mixing.md','knowledge/design/concept-cards/posts/matrix-transformation-colour.md'];results=[]
for case in ['concurrent-edit','second-rename-fails']:
 with tempfile.TemporaryDirectory(prefix='a06s01-cdc-',dir='/private/tmp') as tmp:
  root=Path(tmp);(root/'scripts').mkdir();(root/'scripts/normalize-design-card-metadata.rb').write_bytes(helper_bytes)
  for p in paths:
   f=root/p;f.parent.mkdir(parents=True,exist_ok=True);f.write_bytes(subprocess.check_output(['git','show',baseline+':'+p],cwd=R))
  subprocess.run(['git','init','-q'],cwd=root,check=True);subprocess.run(['git','add','--',*paths],cwd=root,check=True)
  originals={p:(root/p).read_bytes() for p in paths}
  if case=='concurrent-edit':
   hook='''class << File
  alias_method :cdc_original_binread, :binread
  def binread(path,*args)
    data=cdc_original_binread(path,*args)
    if path==ENV.fetch('CDC_SECOND') && !@cdc_injected
      @cdc_injected=true
      first=ENV.fetch('CDC_FIRST')
      File.binwrite(first,cdc_original_binread(first)+"\\nCDC external edit witness\\n")
    end
    data
  end
end
'''
  else:
   hook='''class << File
  alias_method :cdc_original_rename, :rename
  def rename(from,to)
    raise IOError, 'CDC injected second-target rename failure' if to==ENV.fetch('CDC_SECOND')
    cdc_original_rename(from,to)
  end
end
'''
  hookfile=root/'hook.rb';hookfile.write_text(hook);env=os.environ.copy();env['CDC_FIRST']=str(root/paths[0]);env['CDC_SECOND']=str(root/paths[1])
  run=subprocess.run(['ruby','-r',str(hookfile),'scripts/normalize-design-card-metadata.rb','--write',*paths],cwd=root,env=env,capture_output=True,text=True)
  after={p:(root/p).read_bytes() for p in paths}
  results.append({'case':case,'exit':run.returncode,'stdout_rows':len(run.stdout.splitlines()),'stderr':run.stderr.strip(),'first_changed':after[paths[0]]!=originals[paths[0]],'second_changed':after[paths[1]]!=originals[paths[1]],'external_edit_preserved':b'CDC external edit witness' in after[paths[0]]})
print(json.dumps(results,indent=2))
```

The source fix should retain private original bytes, check all snapshots before
writes and each target again immediately before replacement, track completed
writes, and recover only completed targets still equal to this batch's output.
Leave an externally changed/missing target untouched and report it explicitly;
report recovery failures separately. Re-raise/exit nonzero after interruption,
including successfully recovered cases. This is optimistic conflict detection
with per-file replacement; coordinate overlapping writers and do not claim atomic
cross-process compare-and-swap or a multi-file transaction.

CDC exercised a temporary virtual patch using these shapes. The conflict case
now exits1, retains the external edit and changes no second input. The injected
second-rename failure exits1 and restores the first original. An additional
external edit during failure is retained and reported as held rather than
blindly restored. That is author preparation only, not an independently accepted
source repair. No live source code was changed. Exact recipe/checks are in I1.

## F02 — Two sentinel-table entries contradict the real headers

At planning `be623972b71f7be1002ed3932743c16a23dadb95`, batch-record.md's pilot table marks additive-colour-mixing
and colour-gamut `aliases` as exact empty sentinels. Their pinned aliases are
populated nested arrays: respectively `[["additive mixing", "light mixing",
"RGB mixing"]]` and `[["gamut", "color gamut", "sRGB gamut"]]`.
Both are correctly preserved by the actual source diff and inventory; neither
was a permitted value delta. Correct the current evidence without rewriting
history: additive sentinel fields are prerequisites/extends; gamut fields are
prerequisites/extends/contrasts_with. The actual total remains16, not18.
No further card change or flattening is authorized. Record these preserved
non-flat values as a limitation of strict string-list conformance.

## Six-row disposition and bubble-up

| Row | CDC status | Evidence / remaining work |
|---|---|---|
| S01-01 | done | Issued authority/pins, authorized3.2 selection, actual population and no-fill readback reproduce. |
| S01-02 | done | Complete strict233 inventory, pinned raw/typed/index/hash/body data, independent decoder and10/223 union reproduce. |
| S01-03 | done | All22 existing fields/extensions mapped with only four authorized sentinel transformations; no inferred values. Preserve non-flat populated lists as a recorded conformance limitation. |
| S01-04 | open | Parsing/preservation controls pass, but concrete write-time conflict and interrupted-batch behavior fail F01. Hosted observation remains prior attributed CDC evidence, not fresh CC inspection. |
| S01-05 | open | Ten delivered cards and allocation pass; the reusable helper must satisfy F01 before bulk normalization. |
| S01-06 | open | Exact scopes/commits and useful return pass; current return must correct F02 and disclose repaired write paths with actual witnesses. |

Schema mapping and inventory remain accepted at their named bytes. Keep all
six criteria and three accepted rows; I1 updates only helper and the three
existing prose/ledger return files. Preserve all card blobs, version/history,
233-row inventory, initial prompts, source originals and Project08 evidence.
No new supporting artifact, no expanded metadata research or extra analysis
phase. Slice02 remains unissued until this bounded correction is accepted.
Full233 changed-revision GitHub rendering, Arc02 body-escape/substantive/fidelity,
P10-11 readiness and Arc04 final composition/release remain open. Main's unrelated
knowledge/lfe and other planning projects stay untouched. Parent criteria are
not waived or promoted by this partial acceptance.
