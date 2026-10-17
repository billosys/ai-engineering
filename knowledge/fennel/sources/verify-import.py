#!/usr/bin/env python3
"""Check the source import against a full original upstream Fennel clone."""
import argparse
import hashlib
import json
from pathlib import Path
import subprocess

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('upstream', type=Path)
parser.add_argument('repository', type=Path)
args = parser.parse_args()
source = Path(__file__).resolve().parent
manifest = json.loads((source / 'history-verification.json').read_text())
mapping = [line.split('\t') for line in (source / 'commit-map.tsv').read_text().splitlines()[1:]]
paths = [item['upstream_path'] for item in manifest['files']]
prefix = 'knowledge/fennel/sources/md/'


def git(repo, *options):
    return subprocess.check_output(['git', '-C', str(repo), *options])


def require(condition, message):
    if not condition:
        raise SystemExit(message)


reachable = set(git(args.repository, 'rev-list', manifest['filtered_tip']).decode().splitlines())
require({new for old, new in mapping} == reachable, 'Commit map does not cover imported graph')
require(len(mapping) == len(reachable), 'Commit map is not one-to-one')
git(args.repository, 'merge-base', '--is-ancestor', manifest['filtered_tip'], 'HEAD')
# Every non-merge commit touching a selected path must survive filtering.
changed = set(git(args.upstream, 'log', '--full-history', '--no-merges', '--format=%H',
                  manifest['upstream_pin'], '--', *paths).decode().splitlines())
require(changed <= {old for old, new in mapping}, 'A selected-path change is absent from the map')
fmt = '%an%x00%ae%x00%aI%x00%cn%x00%ce%x00%cI%x00%B'
blobs = 0
for old, new in mapping:
    require(git(args.upstream, 'show', '-s', '--format=' + fmt, old)
            == git(args.repository, 'show', '-s', '--format=' + fmt, new),
            'Author, committer, dates or message changed: ' + old)
    original = git(args.upstream, 'ls-tree', '-r', old, '--', *paths).decode().splitlines()
    expected = sorted(meta + '\t' + prefix + name
                      for meta, name in (line.split('\t', 1) for line in original))
    actual = sorted(git(args.repository, 'ls-tree', '-r', new).decode().splitlines())
    require(expected == actual, 'Historical tree differs: ' + old)
    blobs += len(original)
for item in manifest['files']:
    original = git(args.upstream, 'show', manifest['upstream_pin'] + ':' + item['upstream_path'])
    current = (args.repository / item['retained_path']).read_bytes()
    require(original == current, 'Current source bytes differ: ' + item['upstream_path'])
    require(hashlib.sha256(current).hexdigest() == item['sha256'], 'SHA-256 differs')
require(blobs == manifest['historical_blob_comparisons'], 'Historical comparison count differs')
print(f'PASS: {len(mapping)} commits, {len(changed)} selected-path non-merge changes, '
      f'{blobs} historical blobs, {len(paths)} current files')
