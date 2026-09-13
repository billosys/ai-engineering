# Slice04 Validation Evidence

Run from the source checkout:

```sh
p=.worktrees/planning/project08-concept-card-metadata/arc01-metadata-research-and-requirements
jq -s '([.[0].memberships[]|[.field_path,.record_kind]|@tsv] + [.[1].memberships[]|[.field_path,.record_kind]|@tsv]) as $u | {assigned:(.[0].memberships|length),remainder:(.[1].memberships|length),unique:($u|unique|length),duplicates:($u|group_by(.)|map(select(length>1))|length)}' "$p/slice04-semantic-identity-source-and-graph-families/artifacts/semantic-membership.json" "$p/slice04-semantic-identity-source-and-graph-families/artifacts/remainder-membership.json"
jq . "$p/slice04-semantic-identity-source-and-graph-families/artifacts/semantic-membership.json" >/dev/null
git -C .worktrees/planning diff --check
```

Expected: assigned 303, remainder 252, unique 555, duplicates 0. This is
structural coverage; semantic review is the separate authored family artifact.
