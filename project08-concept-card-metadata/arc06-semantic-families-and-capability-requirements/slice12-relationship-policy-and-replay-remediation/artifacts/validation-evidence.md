# Slice12 Validation Evidence

## Execution Context

This remediation was executed from the declared source cwd
`/Users/oubiwann/lab/billosys/ai-engineering` with the planning checkout at
`.worktrees/planning`. The actual opening source HEAD was
`e763c661592ff1097a94bb470db9cf924524579d`; the actual opening planning HEAD
was `f3cadf33`, and both worktrees were clean at inspection. Model, effort,
settings and compaction are unknown from repository state; this task changed
no settings. The route uses Bash, `jq`, `rg`, `awk`, `sed`, `shasum`, `cmp` and
Git against the frozen structured inventory and registered source paths. No
custom parser, Ruby, Python, corpus edit, source-skill edit or package gate is
in scope.

## R5 Policy-Authority Checks

The cited historical passages were read directly with their surrounding
headings, not inferred from CDC's summary. These checks passed from the source
cwd:

```bash
set -euo pipefail
cd /Users/oubiwann/lab/billosys/ai-engineering
rg -n 'Every non-foundational concept needs prerequisites' .worktrees/planning/old/dev/concept-cards/0010-a-guide-for-parallel-concept-card-re-extraction-v3.2.md
rg -n 'All frontmatter fields populated \(use null/empty array where N/A\)' .worktrees/planning/old/dev/concept-cards/0010-a-guide-for-parallel-concept-card-re-extraction-v3.2.md
rg -n 'prerequisites:.*REQUIRED \(empty array if foundational\)' .worktrees/planning/old/dev/concept-cards/0010-a-guide-for-parallel-concept-card-re-extraction-v3.2.md
rg -n 'Missing frontmatter \(12 fields\).*prerequisites.*extends.*related.*contrasts_with' .worktrees/planning/old/dev/concept-cards/0009-howto-concept-card-extraction-with-claude-code-v3.2.md
jq empty .worktrees/planning/project08-concept-card-metadata/arc06-semantic-families-and-capability-requirements/slice01-relationship-semantics-and-traversal/artifacts/semantic-membership.json
```

The resulting matrix is in `historical-policy-comparison.md`. It records the
explicit prerequisite applicability rule separately from the broader
all-frontmatter/template-conformance guidance; preserves the exact
absent/null/empty/populated states and item counts; and leaves lineage,
applicability, migration and future requiredness unresolved for P-15.

## R6 And Complete Current-Route Invocation

After the Slice12 commit, the complete declared current route is invoked
literally as one filtered extraction of the current-route code blocks in the
repaired Slice01 validation artifact. The committed endpoint used below is
`b3ea7533`:

```bash
set -euo pipefail
cd /Users/oubiwann/lab/billosys/ai-engineering
route=.worktrees/planning/project08-concept-card-metadata/arc06-semantic-families-and-capability-requirements/slice01-relationship-semantics-and-traversal/artifacts/validation-evidence.md
export COMMITTED_REVIEW_HEAD=b3ea7533
replay_log=$(mktemp)
trap 'rm -f "$replay_log"' EXIT
set +e
awk '
  /^## Current Replay \(Slice12-Repaired Route: R5\/R6\)$/ {active=1; next}
  /^## Iteration 01 Replay$/ {active=0}
  active && /^```bash$/ {inside=1; next}
  active && /^```$/ {inside=0; next}
  active && inside {print}
' "$route" | bash >"$replay_log" 2>&1
replay_status=$?
set -e
cat "$replay_log"
test "$replay_status" = 0
```

The current route's observed control transcript was:

```text
lookup-control match status=0 result=match
lookup-control no-match status=0 result=no-match
lookup-control error status=2 result=<empty>
```

The full route also emitted the accepted legacy census, six-family card
census, exact edge projections and four native comparison results. The four
native comparisons returned `true`; the deliberate wrong-endpoint and
wrong-revision controls returned `false` under the expected `! jq -e` guards.
The complete route returned exit status 0. The injected exit-2 path returned
nonzero inside the same lookup/resolution function and was not converted into
the native no-match result. The real synthetic-edge support lookup returned a
successful no-match and retained the bounded `unavailable` result.

The route also rechecked all 27 registered hashes, exact 35-pair accounting,
115 accepted/440 remaining/405 outside, the original/copy mapping, all census
values, JSON, whitespace and the two fixed historical preservation comparisons.
`query-cases.json` remained unchanged; its expected/observed objects were
replayed without edits.

## Preservation And Scope Checks

The current preservation comparison is separate from fixed historical
comparisons:

- fixed `3cf075ff -> 91c7f5f3` and `91db42fa -> a24758b4` checks retain prior
  CDC/CC history;
- current protected-path preservation compares opening planning `f3cadf33`
  to `b3ea7533` for Arc01 inputs, frozen project artifacts and other
  protected paths;
- the committed current scope compares the explicit eight authorized paths
  from `f3cadf33` to `b3ea7533`;
- `query-cases.json`, Slice01's ledger/closing report/CDC review, plans and
  historical prompts remain outside the authorized diff.

The current route's scope tail is:

```text
opening planning HEAD: f3cadf33
committed review HEAD: b3ea7533
authorized changed files: 8
protected paths changed: 0
query-cases.json changed: 0
```

All source and planning status checks were clean after the commit. This
artifact is CC execution evidence and remains proposed-done pending CDC's
independent Slice12 verification and original Slice01 recomposition.
