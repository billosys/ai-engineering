from pathlib import Path
import hashlib,json,shutil,subprocess,zipfile
repo=Path('/Users/oubiwann/lab/billosys/ai-engineering')
s=repo/'.worktrees/planning/project13-collab-refinements/slice01-autonomous-mode-reliability'
a=s/'artifacts'
changed=subprocess.check_output(['git','diff','--name-only'],cwd=repo,text=True).splitlines()
records=[]
for path in changed:
    f=repo/path
    records.append({'path':path,'source_sha256':hashlib.sha256(f.read_bytes()).hexdigest(),'baseline_blob':subprocess.check_output(['git','rev-parse','f2b1137a:'+path],cwd=repo,text=True).strip()})
(a/'source-inventory.json').write_text(json.dumps({'baseline':'f2b1137a3f3d77b0d34d789c2233b48f4dcb15ff','branch':'codex/autonomous-mode-reliability','changed_count':len(records),'changed':records},indent=2)+'\n')
# Preserve only affected native package outputs; unrelated language bundles stay in target/.
packages=['collaboration-framework','engineering-methods','project-management','agent-coordination','work-verification','testing','methodology-stewardship']
(a/'packages').mkdir(exist_ok=True)
outputs=[]
for package in packages:
    source=repo/'target/skills'/f'{package}.zip'
    dest=a/'packages'/source.name;shutil.copy2(source,dest)
    with zipfile.ZipFile(dest) as z:
        contents=[{'path':i.filename,'size':i.file_size,'sha256':hashlib.sha256(z.read(i)).hexdigest()} for i in z.infolist() if not i.is_dir()]
    outputs.append({'package':package,'artifact':'packages/'+dest.name,'bytes':dest.stat().st_size,'sha256':hashlib.sha256(dest.read_bytes()).hexdigest(),'entries':contents})
(a/'package-inventory.json').write_text(json.dumps(outputs,indent=2)+'\n')
# Read only this session's configuration metadata; retain no conversation payload.
f=Path('/Users/oubiwann/Library/Application Support/ChatGPT-Profiles/work/codex-home/sessions/2026/10/19/rollout-2026-10-19T08-39-37-01a15463-a123-72a3-8c37-9c015f33b511.jsonl')
latest=None;provider=None
for line in f.open():
    r=json.loads(line);p=r.get('payload',{})
    if r.get('type')=='session_meta':provider=p.get('model_provider')
    if r.get('type')=='turn_context':latest={'timestamp':r.get('timestamp'),'model':p.get('model'),'reasoning_effort':p.get('effort')}
(a/'execution-configuration.json').write_text(json.dumps({'actual_role':'implementer; self-checks only','mode':'standard implementation; Operator supplies future PR reviewers','session':'01a15463-a123-72a3-8c37-9c015f33b511','reported_provider':provider,'latest_reported_context':latest,'requested_model':'not separately selected for this standard implementation assignment','model_overrides_or_subagents':'none dispatched','per_slice_spend_or_token_usage':'unavailable; no attribution baseline captured','identity_limit':'session-reported model/configuration; no assertion about unreported backend weights'},indent=2)+'\n')
print(f'Retained {len(records)} changed-source identities and {len(outputs)} actual native bundles; model metadata:',latest)
