# Slice04 CC execution notes

## Assignment identity and state

- Issuing packet: `db77543df9f6785f9b1889112ac12a79383db400`, tree `f96b26190b6edb7082ab5fb024877841be433ce7`, parent `370cfc8f79cbac56055bef49f1472467b85a2569`. Prompt Git blob `84b08d225a33a2ef0e20457d088553671efb2f2e`, SHA-256 `eb2d69a0cdc23e8efe0ecdf338d447e96450d0eca62bd7b2b0bc20f03098ce88`.
- Current planning HEAD at intake: `83b10880d1bb6ce4c686942438c6da512532dc9a`, receipt-only child of the issuing commit. Opening packet and issue blob match; no assignment drift. Working branch is `planning`.
- SOURCE: `/Users/oubiwann/lab/billosys/ai-engineering`, `main`, pinned `dffa504e851b03b8e4746f1941068e4cc850b612`. HEAD and tracked/index state match the pin. Only unrelated untracked `knowledge/lfe/` was present. Planning unrelated untracked `project12-chcd-protocol/` was preserved.
- Exactly seven allowed CC output paths are used. No SOURCE, Project13, prompt, plan, preparation, prior slice, audit, or parent criterion/status was edited.

## Read receipts and recovery

Text was loaded in this context; hashes below establish identity only. Required document content was read; source excerpts listed below were read completely, with no source excerpt clipping. Where the tool output combined chunks and clipped, I recovered with bounded reads. The interface exposed no stable tool-output IDs, so ranges and extents are recorded here.

| Manifest order | Required input / state | Loaded extent and result |
|---|---|---|
| 0 | SOURCE `AGENTS.md`, pin `dffa504e…`; installed `/Users/oubiwann/.agents/skills/collaboration-framework/SKILL.md`; SOURCE PM `SKILL.md`, `guides/README.md` | Full files: 216, 538, 65 and 178 lines. SHA-256: `cf56f5e91c923811c6a620edb125dffcbc44be2980783c7deec5bf2a2ce258cc`, `63a924ef9fb841b01f1013f0e1e73fc13a95d76de2bd4ff8c1f1a024cbdeecae`, `3b60b8bf6b407465da80c9d00ecb2700d2bccca3716b120cbaccb3a1f5822d19`, `5de496704990ba211f31707f2bfaaa467b66e51555d1232c19420284ae6a4280`. Planning `AGENTS.md` and Project10 `AGENTS.md` also read full (137 and 48 lines). |
| 1 | Project10 `project-plan.md`; Arc02 `arc-plan.md` at issue | Both complete, through current version histories and governing gates. |
| 2 | Project10/Arc02 opening ledgers | Project criterion table 13 rows; Arc criterion table eight rows; Arc02 current Slice04 opening section read. Parent statuses/text left unchanged. |
| 3 | Current prompt, slice plan, ledger, preparation | Full prompt 120 lines, slice plan 138, ledger 31, preparation 186. One contract readback below. |
| 4 | SOURCE PM guide “Issuing and executing an iteration”; prompt-authoring guide “Investigation and semantic evidence assignments”, §5, §6, “Required reading and CC intake” plus definitions | PM lines 134–187; prompt guide lines 162–185, 187–259, 260–361. Full named sections and required definitions read. |
| 5 | SOURCE ledger discipline, row closure, independent verification; design SKILL | Full files (112, 70, 103 and 368 lines). Design SKILL hash `57833e7cecd5984bf1cd6c7b26def1194f7cbbdf83e24a4960bd739a6f26ff63`. Current installed `visual-design-system` SKILL full 368 lines; hash equals the assigned SOURCE design SKILL. |
| 6 | Review procedure at `759ce2dd116a4cfe03b72d43fd2791f48486251c` | Complete 83-line historical procedure. |
| 7 | Project09 audit at `795ac75b7d02536e0e95252457ac3282cd17d8d8` | DES-002/005/006/009 complete relevant audit sections inspected; DES-009 retains intrinsic-first, justified adaptation, scoped prose measure and later browser/Arc03 proof. |
| 8 | Three SOURCE windows and primary readings | All W01–W13 loaded, 13 contexts/184 inclusive physical lines. W01 is 78–99 (the pre-issue extension); no line was sampled. Exact full-file hashes/counts match preparation: SKILL 368 lines `578ea…` (full hash above); `layout.md` 990 lines `361ea7887a69870db6db7aa362455b00b5cf718d6c4ae0d49405785fd5c82aec`; monoculture guide 597 lines `76d209306a8ade1da51f62ad86fb7f01f103f0f4d033e7235c3b4b023397b845`. Complete page scopes and limits are in `source-comparison.md`. |
| 9 | Slice03 preparation example subsection; Slice03 CDC Iteration04/closure section | Preparation lines 82–145 read; CDC verification lines 866–960 read. Used for shape/limit only, not as proof for Slice04. |
| Conditional | Media preference definitions | Not triggered: no preference-specific result relies on them. MQ Abstract, screen/print introduction example and §2.3 were read. |
| Reference-only | Project13 protocol/history | The host record and plans state protocol revision 2 at `23c77653…`, T01 checkpoint and T02 registration. Protocol contents and Case01 were not independently opened in this CC turn. No protocol success or control is inferred. |

**Read-order deviation:** on the first intake pass I read the current prompt, slice plan and ledger before completing manifest orders 0–2. I stopped before dependent batch work, then loaded orders 0–9 and re-read the governing assignment texts. No evidence was produced until after intake and the example replay. This is recorded rather than represented as prescribed-order execution.

**Recovered failed attempts:** the first author-example extraction ran from SOURCE with a planning-relative path and exited nonzero (`FileNotFoundError`); the preparation was not found at that cwd. I corrected to its absolute PLANNING path, extracted the unchanged fenced example to `/tmp`, and ran it from SOURCE. Exit 0: positive 1; invalid records rejected 5; hypothetical glyph counts `[60,120]`; semantic oracle explicitly human. `/tmp` held only the transient example. No repository helper file was added. No source/install/package/browser/AT command was attempted. The first final local-link verifier used an incorrectly escaped heading matcher and falsely reported a missing fragment; after correcting the matcher, all 11 local file/fragment links resolved. The first commit invocation then used abbreviated slice pathspecs and Git rejected them; no commit was created. The corrected full-path invocation is used for the candidate.

## Contract readback

Prompt execution spine and S04-02/S04-04 require a clause-level occurrence inventory across all 13/184 selected window lines before verdicts; these are context bounds, not the claim denominator. S04-03 and the preparation’s primary-reading table separate present technical evidence from unavailable originals and authoring lineage. S04-04 requires five separate results per assigned assertion; S04-05 composes intrinsic-first guidance with justified discrete adaptation and scoped measure; S04-06 binds every proposal to an exact untouched SOURCE subject and later owner. S04-07 requires a checker whose actual predicates reject identity, bounds, omission and join defects while leaving semantic truth to people. S04-08/09 preserve the seven paths and parent gates. Therefore a passing checker, current W3C page, or CC report cannot establish fidelity, browser behavior, WCAG conformance, full DES closure, source readiness or acceptance. CDC review remains required and all nine child rows stay open.

## Population, comparison and observed limits

The 13 inclusive windows sum to 184 physical lines (sum independently recomputed from bounds). Current assigned atomic population is **27** claim records. `occurrence-inventory.jsonl` has one source-verified row for each of the 184 selected lines; every row is assigned to one or more claims or to an explicit context/markup/retained-boundary owner. Other primitive, spacing, color, typography, attribution/analogy and converted-markup assertions remain mapped to Arc03, Arc02 T/source readiness or Arc04 as stated per row; they are not accepted by this slice. Claim-result denominator is 27, not 13 or 184.

Primary page read scopes, versions, dates/status and unknowns appear in `source-comparison.md`. Current evidence supports correcting universal measure/query and correctness-guarantee language while preserving a configurable prose measure, intrinsic Switcher behavior and the composition ethos. The Every Layout page currently demonstrates both axiom language and selector exceptions. That is a present local scope tension, not proof of what edition the guide originally represented. `ch` is glyph-relative and approximate under specified conditions. WCAG distinctions constrain standards claims, but no runtime conformance was assessed.

## Trial, tool and utility observations

Project13’s register identifies T02 as prospectively registered before issue, not executed, under protocol revision 2. T01’s checkpoint says comparative benefit was inconclusive. This CC turn saw those statements in host planning artifacts but did not read the protocol body, measure a run, or determine causal benefit. No provider/model ID, sampling settings, token counts, elapsed time or independent execution environment were surfaced. The conversation reused one continuing thread; no independent-session claim is made.

The occurrence registry supports full-context omission checks and the handoff supports exact future planning. It adds review volume: 184 line records plus 27 five-dimension assessments and 26 non-overlapping actions (C09/C10 share one coherent replacement). Reviewer minutes, maintenance burden over time, tokens attributable to each artifact and downstream implementation utility are unknown. These artifacts serve the assigned evidence/handoff decision; their existence alone is not a methodology improvement.

## Inline structural checker and discriminating controls

The checker below is intentionally limited to identities, declared bounds, complete selected-line accounting, cross-file joins, required dimension/evidence shapes and non-overlapping virtual edits. It is not a truth oracle for assertion completeness, technical applicability, pair comparability or policy quality; those remain human review. It verifies bounds before slicing and uses the same `check()` predicate for valid and corrupted datasets.

```python
import copy, hashlib, json, subprocess
from pathlib import Path
ROOT = Path('/Users/oubiwann/lab/billosys/ai-engineering')
REV = 'dffa504e851b03b8e4746f1941068e4cc850b612'
WINDOWS = [
 ('knowledge/design/SKILL.md',78,99),('knowledge/design/SKILL.md',206,208),('knowledge/design/SKILL.md',266,273),('knowledge/design/SKILL.md',328,333),
 ('knowledge/design/guides/layout.md',142,154),('knowledge/design/guides/layout.md',271,295),('knowledge/design/guides/layout.md',324,351),('knowledge/design/guides/layout.md',383,412),('knowledge/design/guides/layout.md',598,609),('knowledge/design/guides/layout.md',669,680),('knowledge/design/guides/layout.md',698,702),('knowledge/design/guides/layout.md',966,977),('knowledge/design/guides/breaking-the-layout-monoculture.md',105,112)]
BASE = Path('/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning/project10-design-foundations/arc02-theory-and-evidence/slice04-layout-and-measure-exceptions/artifacts')
EXPECTED = {'source_faithfulness','correctness','scope_attribution','consistency','relationship_cq_coverage'}
def read_jsonl(name):
 out=[]
 for n,line in enumerate((BASE/name).read_text().splitlines(),1):
  obj=json.loads(line)
  if not isinstance(obj,dict): raise ValueError((name,n,'row must be object'))
  out.append(obj)
 return out
def check(inv, claims, actions):
 # Establish every declared bound against actual bytes before any source slicing.
 source={}; expected=set(); hashes={}; window_for={}
 for wi,(path,lo,hi) in enumerate(WINDOWS,1):
  data=subprocess.check_output(['git','-C',str(ROOT),'show',REV+':'+path]); lines=data.decode().splitlines()
  if lo<1 or hi<lo or hi>len(lines): raise ValueError(('window-bounds',path,lo,hi,len(lines)))
  digest=hashlib.sha256(data).hexdigest(); hashes[path]=digest; source[path]=(data,lines)
  for n in range(lo,hi+1):
   key=(path,n,f'W{wi:02}'); expected.add(key); window_for[(path,n)]=f'W{wi:02}'
 if len(expected)!=184: raise ValueError(('declared-line-total',len(expected)))
 got={}
 for row in inv:
  k=(row['path'],row['line'],row['window'])
  if k in got: raise ValueError(('duplicate-occurrence',k))
  if k not in expected: raise ValueError(('unexpected-occurrence',k))
  data,lines=source[row['path']]
  if row['revision']!=REV or row['sha256']!=hashes[row['path']] or row['literal']!=lines[row['line']-1]: raise ValueError(('source-identity',k))
  if not row['owner'] or row['classification'] not in {'assigned-assertion','retained-boundary','context-or-markup'}: raise ValueError(('owner-or-class',k))
  if (row['classification']=='assigned-assertion') != bool(row['claim_ids']): raise ValueError(('line-claim-membership',k))
  got[k]=row
 if set(got)!=expected: raise ValueError(('omitted-lines',sorted(expected-set(got))))
 byid={}
 for r in claims:
  cid=r['claim_id']
  if cid in byid: raise ValueError(('duplicate-claim',cid))
  s=r['subject']; path=s['path']; data,lines=source[path]; lo,hi=s['span']
  if lo<1 or hi<lo or hi>len(lines): raise ValueError(('subject-bounds',cid,lo,hi,len(lines)))
  joined='\n'.join(lines[lo-1:hi]); a,b=s['offsets']
  if a<0 or b<a or b>len(joined): raise ValueError(('subject-offset-bounds',cid,a,b,len(joined)))
  if s['revision']!=REV or s['sha256']!=hashes[path] or joined[a:b]!=s['assertion']: raise ValueError(('subject-identity',cid))
  if not all((path,n,window_for[(path,n)]) in got and cid in got[(path,n,window_for[(path,n)])]['claim_ids'] for n in range(lo,hi+1)):
   raise ValueError(('claim-line-reverse-membership',cid))
  if set(r['dimensions'])!=EXPECTED: raise ValueError(('dimensions',cid))
  evid=r['evidence']; eids=[e['id'] for e in evid]
  if len(eids)!=len(set(eids)): raise ValueError(('duplicate-evidence',cid))
  for e in evid:
   if e.get('snapshot_sha256') is not None: raise ValueError(('invented-capture',cid,e['id']))
  for dim,result in r['dimensions'].items():
   if not isinstance(result.get('reason'),str) or not result['reason'] or not set(result.get('evidence_refs',[]))<=set(eids): raise ValueError(('evidence-join',cid,dim))
  if r['dimensions']['source_faithfulness']['outcome']!='not assessed': raise ValueError(('fidelity-upgrade',cid))
  pair=r['dimensions']['consistency']
  for other in pair.get('paired_subjects',[]):
   if other not in {x['claim_id'] for x in claims} or other==cid: raise ValueError(('invented-pair',cid,other))
   if cid not in next(x for x in claims if x['claim_id']==other)['dimensions']['consistency'].get('paired_subjects',[]): raise ValueError(('nonreciprocal-pair',cid,other))
  if pair.get('outcome')!='not assessed' and not pair.get('paired_subjects'): raise ValueError(('unpaired-consistency',cid))
  if not r['disposition'].get('action_id') or not r['disposition'].get('replacement'): raise ValueError(('missing-disposition',cid))
  byid[cid]=r
 if len(inv)!=184 or len(claims)!=27: raise ValueError(('population',len(inv),len(claims)))
 for row in inv:
  if any(cid not in byid for cid in row['claim_ids']): raise ValueError(('inventory-claim-join',row['path'],row['line'],row['claim_ids']))
 aids={}
 for a in actions:
  if a['action_id'] in aids: raise ValueError(('duplicate-action',a['action_id']))
  ids=a['result_ids']
  if not ids or any(i not in byid for i in ids): raise ValueError(('dangling-action',a['action_id'],ids))
  if set(ids)!=set(a['claim_ids']): raise ValueError(('action-result-join',a['action_id']))
  group=[byid[i] for i in ids]; path=a['path']; data,lines=source[path]
  if any(r['subject']['path']!=path for r in group): raise ValueError(('cross-file-action',a['action_id']))
  spans=[r['subject']['span'] for r in group]; span=[min(x[0] for x in spans),max(x[1] for x in spans)]
  if a['source_revision']!=REV or a['source_sha256']!=hashes[path] or a['span']!=span: raise ValueError(('action-source-span',a['action_id']))
  joined='\n'.join(lines[span[0]-1:span[1]])
  if a['original']!=joined or a['literal_offset_0based']!=[0,len(joined)]: raise ValueError(('action-source-subject',a['action_id']))
  if any(x[0]<span[0] or x[1]>span[1] for x in spans): raise ValueError(('action-omits-result-span',a['action_id']))
  x,y=a['file_byte_offsets']; prefix='\n'.join(lines[:span[0]-1]); expected_start=len(prefix.encode())+(1 if span[0]>1 else 0); expected_end=expected_start+len(joined.encode())
  if [x,y]!=[expected_start,expected_end]: raise ValueError(('action-offset-identity',a['action_id']))
  if x<0 or y<x or y>len(data) or data[x:y].decode()!=a['original']: raise ValueError(('action-byte-bounds-or-subject',a['action_id']))
  if not a.get('replacement') or not a.get('owner'): raise ValueError(('action-owner-or-replacement',a['action_id']))
  if any(byid[i]['disposition']['proposed']!=a['disposition'] for i in ids): raise ValueError(('action-disposition-join',a['action_id']))
  aids[a['action_id']]=a
 if set(aids)!={r['disposition']['action_id'] for r in claims}: raise ValueError('action-reverse-membership')
 for r in claims:
  action=aids[r['disposition']['action_id']]
  if r['claim_id'] not in action['claim_ids']: raise ValueError(('action-claim-reverse-membership',r['claim_id']))
 # Compose each file virtually, with nonoverlapping UTF-8 byte replacements.
 for path,(data,_) in source.items():
  edits=sorted([a for a in actions if a['path']==path],key=lambda q:q['file_byte_offsets'][0])
  previous=0; pieces=[]; untouched=[]
  for a in edits:
   x,y=a['file_byte_offsets']
   if x<previous: raise ValueError(('overlap',path,a['action_id']))
   unchanged=data[previous:x]; pieces.extend((unchanged,a['replacement'].encode())); untouched.append(unchanged); previous=y
  tail=data[previous:]; pieces.append(tail); untouched.append(tail); candidate=b''.join(pieces)
  # Every non-target source segment is carried byte-for-byte around the virtual edits.
  if b''.join(untouched)!=b''.join([data[0:edits[0]['file_byte_offsets'][0]]] + [data[x['file_byte_offsets'][1]:y['file_byte_offsets'][0]] for x,y in zip(edits,edits[1:])] + ([data[edits[-1]['file_byte_offsets'][1]:]] if edits else [data])): raise ValueError(('neighbor-preservation',path))
  if not candidate: raise ValueError(('empty-virtual-file',path))
 return True
inv=read_jsonl('occurrence-inventory.jsonl'); claims=read_jsonl('claim-results.jsonl')
actions=json.loads((BASE/'correction-handoff.md').read_text().split('```json\n',1)[1].split('\n```',1)[0])
check(inv,claims,actions)
controls=[]
def rejected(label,mutate):
 i,c,a=copy.deepcopy(inv),copy.deepcopy(claims),copy.deepcopy(actions); mutate(i,c,a)
 try: check(i,c,a)
 except (ValueError,KeyError,IndexError,TypeError): controls.append(label)
 else: raise AssertionError('negative control passed: '+label)
rejected('omitted selected line',lambda i,c,a:i.pop())
rejected('out-of-file declared subject bound',lambda i,c,a:c[0]['subject'].__setitem__('span',[999999,999999]))
rejected('clipped source qualifier',lambda i,c,a:c[0]['subject'].__setitem__('assertion',c[0]['subject']['assertion'][:-1]))
rejected('replacement presented as original subject',lambda i,c,a:c[0]['subject'].__setitem__('assertion',c[0]['disposition']['replacement']))
rejected('duplicate evidence identifier',lambda i,c,a:c[0]['evidence'].append(copy.deepcopy(c[0]['evidence'][0])))
rejected('dangling action/result join',lambda i,c,a:a[0].__setitem__('result_ids',['MISSING']))
rejected('invented immutable capture',lambda i,c,a:c[0]['evidence'][0].__setitem__('snapshot_sha256','0'*64))
rejected('invented comparable pair',lambda i,c,a:c[0]['dimensions']['consistency'].__setitem__('paired_subjects',['NOT-A-CLAIM']))
print(json.dumps({'valid':'pass','negative_controls_rejected':controls,'semantic_oracle':'human review only'}))
```

## Re-entry and final checks

Required dependent re-entry: exact original/capture/edition/lineage (Operator/P10-11) for fidelity; implemented page samples and browser/user-agent/assistive-technology runs (Arc03/04) for actual behavior and accessibility. No blocked technical comparison prevents the bounded current-source claims above; each gap blocks only its dependent fidelity or runtime claim. No preference claim is pending because none is relied on.
