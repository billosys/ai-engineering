#!/usr/bin/env python3
"""Run every authored Fennel rule example; retain explicit compile-negative cases."""
from pathlib import Path
import hashlib
import json
import re
import subprocess
import tempfile
import sys

# Run from the implementation checkout.
repo = Path(subprocess.check_output(['git', 'rev-parse', '--show-toplevel'], text=True).strip())
root = repo / 'knowledge/fennel/guides'
records = []
fix_format = '--format' in sys.argv
with tempfile.TemporaryDirectory(prefix='fennel-guide-examples-') as work:
    work = Path(work)
    for path in sorted(root.glob('*.md')):
        text = path.read_text()
        substitutions = []
        for index, match in enumerate(re.finditer(r'```fennel\n(.*?)\n```', text, re.S)):
            code = match.group(1) + '\n'
            heading = list(re.finditer(r'^## ([A-Z]+-\d+):', text[:match.start()], re.M))[-1].group(1)
            kind = 'good' if code.startswith(';; GOOD:') else 'bad'
            name = heading + '-' + kind
            file = work / (name + '.fnl')
            file.write_text(code)
            expected_diagnostics = {
                'ID-05-bad': 'tried to reference a special form',
                'FN-05-bad': 'Must be in tail position',
                'PM-04-bad': 'unknown identifier: b',
                'MC-03-bad': 'without gensym',
                'MC-04-bad': 'unknown identifier: helper',
                'MC-05-bad': 'unknown identifier: numeric',
                'MC-06-bad': 'attempt to index a number value',
                'TL-02-bad': 'unknown identifier: misspelled-processor',
            }
            negative = code.startswith(';; BAD: compile error:') or code.startswith(';; BAD: compile-only counterexample:')
            compile_result = subprocess.run(['fennel', '--globals', '', '--compile', str(file)], text=True, capture_output=True)
            record = {'id': name, 'guide': path.name, 'line': text[:match.start()].count('\n') + 1,
                      'expected': 'compile-error' if negative else 'run-success',
                      'compile_exit': compile_result.returncode}
            if negative:
                record['pass'] = (compile_result.returncode != 0
                                  and expected_diagnostics[name] in compile_result.stderr)
                record['diagnostic'] = compile_result.stderr
            elif compile_result.returncode:
                record['pass'] = False
                record['diagnostic'] = compile_result.stderr
            else:
                lua_file = file.with_suffix('.lua')
                lua_file.write_text(compile_result.stdout)
                runs = []
                for command in [['fennel', str(file)], ['lua', str(lua_file)]]:
                    result = subprocess.run(command, text=True, capture_output=True)
                    runs.append({'command': command[0], 'exit': result.returncode,
                                 'stdout': result.stdout, 'stderr': result.stderr})
                record['runs'] = runs
                record['pass'] = all(item['exit'] == 0 for item in runs)
            # A deliberately ugly ST-01 bad example remains ugly to teach layout.
            if not negative and not (heading == 'ST-01' and kind == 'bad'):
                formatted = subprocess.run(['fnlfmt', str(file)], text=True, capture_output=True)
                if formatted.returncode == 0 and fix_format:
                    code = formatted.stdout
                    substitutions.append((match.start(1), match.end(1), code.rstrip('\n')))
                    file.write_text(code)
                checked = subprocess.run(['fnlfmt', '--check', str(file)], text=True, capture_output=True)
                record['format_exit'] = checked.returncode
                record['pass'] = record['pass'] and checked.returncode == 0
            record['sha256'] = hashlib.sha256(code.encode()).hexdigest()
            records.append(record)
        if substitutions:
            for start, end, replacement in reversed(substitutions):
                text = text[:start] + replacement + text[end:]
            path.write_text(text)
report = {'examples': len(records), 'pass': sum(r['pass'] for r in records),
          'fail': sum(not r['pass'] for r in records), 'records': records}
output = Path(__file__).with_name('example-results.json')
output.write_text(json.dumps(report, indent=2) + '\n')
print(f"{report['pass']}/{report['examples']} passed; {report['fail']} failed")
for row in records:
    if not row['pass']:
        print(row['id'], row.get('diagnostic', row.get('runs', 'format failure')))
sys.exit(bool(report['fail']))
