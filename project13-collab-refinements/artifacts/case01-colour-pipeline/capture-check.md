# Archive capture self-check

CDC Sofie, 2026-10-10. This is a bootstrap integrity receipt, not independent
acceptance of this author's case-study interpretation or a new replay of the
historical numerical/semantic evidence.

The capture used the manifest's pinned Git objects, never the in-flight worktree
files. A second read compared all 50 copies (2,551,564 bytes) to those objects,
including blob identities, SHA-256, byte lengths and line counts: all equal.
All four prompt/notes/JSONL byte and population measures were recounted; each
JSONL line parsed. Assessed-class counts and CDC dispositions are explicitly
report/review-derived, not newly accepted outcomes. Unknown measures stay null.

The nine authored Markdown documents at the final check had 52 local file links,
all present, and LF endings. Historical copies' embedded links were excluded:
repairing them would violate byte preservation. Existing Project10 fragments
were unchanged and not rerun. Both new CLAUDE.md links target AGENTS.md.
Project10's plan retains every prior line except its extended related-project
metadata; the trial and history entry are additive. Its ledger and slice files
were not edited. Planning-only scope requires no source/package/Make validation.

During bootstrap CC committed its separate Iteration04 return as `19dd5385`.
The study remains frozen at review `9a30f480`, with Iteration03 return `6a016960`;
the later work is excluded and remains subject to its normal CDC review.

## Validation exceptions and recovery

Initial staging failed because the sandbox could not create the planning
worktree index lock. The same explicit 63-path staging operation succeeded with
approved Git-metadata access. No alternate checkout or unrelated staging was used.
The full staged `git diff --check` returned 2 for 28 trailing-whitespace lines,
all in the byte-identical historical prepared Oklab source copy. Those bytes are
intentionally retained as archival evidence, not normalized. The check restricted
to the 13 newly authored/host-update paths returned 0. Archive identity validation
still passes; the full diff check is not reported as clean.

## Minimal archive replay

Run from this case-study directory using Python 3 and the shared Git repository.
The command reads evidence only; it does not execute archived prompts or scripts.

```sh
python3 - <<'PY'
from pathlib import Path
import hashlib, json, subprocess
m = json.loads(Path('evidence-manifest.json').read_text())
for e in m['entries']:
    copy = Path(e['copy_path']).read_bytes()
    original = subprocess.check_output([
        'git', 'show', e['revision'] + ':' + e['repository_path']])
    blob = subprocess.check_output([
        'git', 'rev-parse', e['revision'] + ':' + e['repository_path']
    ]).decode().strip()
    assert copy == original, e['copy_path']
    assert blob == e['blob'], e['copy_path']
    assert hashlib.sha256(copy).hexdigest() == e['sha256']
    assert len(copy) == e['bytes']
    assert len(copy.splitlines()) == e['lines']
print(len(m['entries']), 'copies match their pinned Git objects')
PY
```
