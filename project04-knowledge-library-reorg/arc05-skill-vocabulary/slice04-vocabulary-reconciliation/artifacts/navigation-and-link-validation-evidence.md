# navigation and link validation evidence

## Source Scope

Validated local links and navigation route references in:

- `README.md`
- `SKILL.md`
- `docs/*.md`

## Local Link Validation

Command:

```sh
python3 - <<'PY'
from pathlib import Path
import re, urllib.parse
root=Path('/Users/oubiwann/lab/billosys/ai-engineering')
files=[root/'README.md', root/'SKILL.md']+sorted((root/'docs').glob('*.md'))
link_re=re.compile(r'!?\[[^\]]*\]\(([^)]+)\)')
missing=[]; checked=0; skipped=0
for path in files:
    text=path.read_text()
    for i,line in enumerate(text.splitlines(),1):
        for m in link_re.finditer(line):
            target=m.group(1).strip()
            if not target or target.startswith(('http://','https://','mailto:','#')):
                skipped+=1; continue
            target=target.split()[0]
            target=target.split('#',1)[0]
            if not target:
                skipped+=1; continue
            decoded=urllib.parse.unquote(target)
            resolved=(path.parent/decoded).resolve()
            checked+=1
            if not resolved.exists():
                missing.append((path.relative_to(root),i,target,resolved))
print(f'files checked: {len(files)}')
print(f'links checked: {checked}')
print(f'skipped external/anchors: {skipped}')
print(f'missing: {len(missing)}')
raise SystemExit(1 if missing else 0)
PY
```

Result:

```text
files checked: 10
links checked: 104
skipped external/anchors: 1
missing: 0
```

Local link validation passed with missing: 0.

## README/docs/SKILL Route Scan

Command:

```sh
rg -n "\[[^\]]+\]\([^\)]+\)|https?://|docs/|knowledge/|protocols/|templates/|Makefile|package" README.md docs SKILL.md
```

Result: passed. The route scan returned expected references to:

- `docs/`
- `knowledge/`
- `protocols/`
- `templates/`
- `Makefile`
- skill package commands and package links
- CCDP package commands and `ccdp.zip`
- top-level `SKILL.md`

No missing local link or stale navigation route was found.
