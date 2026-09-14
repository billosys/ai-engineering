# Slice09 Validation Evidence

All commands ran from `/Users/oubiwann/lab/billosys/ai-engineering` on
2026-09-13. They are same-context CC checks, not CDC verification.

## Frozen census

```sh
jq '[.records[] | select(.record_kind=="claim" or .record_kind=="concept-card")] | length' \
  .worktrees/planning/project08-concept-card-metadata/arc01-metadata-research-and-requirements/slice01-metadata-inventory-and-research-questions/artifacts/frontmatter-inventory.json
# 32
```

```sh
jq -r 'def fam: if .path|startswith("knowledge/concept-cards/templates/") then "template" elif .path|startswith("knowledge/concept-cards/examples/") then "synthetic" elif .path|startswith(".worktrees/planning/project05") then "Arc07" elif .path|contains("compcogneuro-rich") then "rich" elif .path|contains("compcogneuro-teaching") then "teaching" else "other" end; ["assertion_kind","card_ref","source_refs","source_support_refs","statement","claim_refs","source_snapshot"] as $f | .records[] | select(.record_kind=="claim" or .record_kind=="concept-card") | . as $r | $f[] as $k | [$r.record_kind,($r|fam),$k,(if ($r.keys|index($k)) then ($r.values[$k]|type) else "absent" end)] | @tsv' inventory.json
```

The literal 224-row output records every selected key for all 32 roots without
projecting missing keys to null. It shows the sole claim template's three null
scalars and two empty arrays, no populated standalone claim, card lists that
are absent/empty/populated by family, and scalar `source_snapshot` in the six
expanded Arc07 cards. The three malformed rich originals remain parser limits.

## Body and target inspection

```sh
sed -n '1,180p' .worktrees/planning/project05-concept-card-skill/arc07-real-corpus-uat-and-feedback/slice02-pilot-markdown-preparation-and-card-extraction/artifacts/candidate-cards/{cc-model-data-constraints,support-model-data-constraints}.md
sed -n '1,180p' .worktrees/planning/project05-concept-card-skill/arc07-real-corpus-uat-and-feedback/slice04-expanded-corpus-card-generation/artifacts/candidate-cards/cc-memory-forms.md
sed -n '1,180p' .worktrees/planning/project08-concept-card-metadata/arc01-metadata-research-and-requirements/slice01-metadata-inventory-and-research-questions/artifacts/baseline-snapshots/compcogneuro-{rich,teaching}-rerun-2026-09-12/candidate-cards/cc-model-data-constraints.md
```

The pilot exposes a body-linked embedded claim and a separate support
subject/span; the expanded card exposes only scalar snapshot/body support; the
pinned reruns expose populated structured lists and body maps. Inspection
showed heading text, not declared literal anchors or embedded target revisions.

```sh
sed -n '1,180p' knowledge/concept-cards/{templates/claim.md,templates/concept-card.md,examples/minimal-card.md,examples/claim-backed-card.md,examples/rich-profile-card.md}
sed -n '1,180p' /Users/oubiwann/lab/music-comp/ai-music-theory/concept-cards/complete-musician/accent-types.md
sed -n '1,180p' knowledge/erlang/concept-cards/otp-design-principles/behaviour.md
```

These checks supplied template/fictional-target limits and historical readable
definition/source/review observations; they did not verify source support.

## Membership and evidence checks

```sh
jq -e '(.memberships|length)==21 and ([.memberships[]|[.field_path,.record_kind]|join("\u0000")] | unique | length)==21' artifacts/semantic-membership.json
# true
jq -e '[.evidence|to_entries[]|select(.value.path != null and .value.sha256 != null and .value.section != null and .value.role != null)] | length == (.evidence|length)' artifacts/semantic-membership.json
# true
```

The expected set was transcribed from Slice09's exact-pair table before
registry review. The following replay checks 21 exact unique pairs, 94 accepted
pairs and no overlap:

```sh
jq -n --slurpfile ours artifacts/semantic-membership.json --slurpfile b04 ../slice04-semantic-identity-source-and-graph-families/artifacts/batch01-identity-membership.json --slurpfile s06 ../slice06-record-identity-and-classification/artifacts/semantic-membership.json --slurpfile s07 ../slice07-source-identity-and-locator-semantics/artifacts/semantic-membership.json --slurpfile s08 ../slice08-source-support-subjects-and-spans/artifacts/semantic-membership.json 'def k: [.field_path,.record_kind]|join("\u0000"); def expected: [["assertion_kind","claim"],["card_ref","claim"],["source_refs","claim"],["source_support_refs","claim"],["statement","claim"],["claim_refs","concept-card"],["claim_refs[]","concept-card"],["claim_refs[].id","concept-card"],["claim_refs[].path","concept-card"],["claim_refs[].revision","concept-card"],["source_refs","concept-card"],["source_refs[]","concept-card"],["source_refs[].id","concept-card"],["source_refs[].path","concept-card"],["source_refs[].revision","concept-card"],["source_snapshot","concept-card"],["source_support_refs","concept-card"],["source_support_refs[]","concept-card"],["source_support_refs[].id","concept-card"],["source_support_refs[].path","concept-card"],["source_support_refs[].revision","concept-card"]]|map(join("\u0000")); ($ours[0].memberships|map(k)) as $o | ($b04[0].memberships+$s06[0].memberships+$s07[0].memberships+$s08[0].memberships|map(k)) as $a | {exact:(($o|sort)==(expected|sort)),ours:($o|length),accepted:($a|length),unique:($o|unique|length==21),disjoint:([$o[]|select(. as $x|$a|index($x))]|length==0),accounted:(($a|length)+($o|length)==115)}'
# {"exact":true,"ours":21,"accepted":94,"unique":true,"disjoint":true,"accounted":true}
```

## Identity and preservation

```sh
shasum -a 256 knowledge/concept-cards/templates/{claim,concept-card}.md knowledge/concept-cards/examples/{minimal-card,claim-backed-card,rich-profile-card}.md .worktrees/planning/project05-concept-card-skill/arc07-real-corpus-uat-and-feedback/slice02-pilot-markdown-preparation-and-card-extraction/artifacts/candidate-cards/{cc-model-data-constraints,support-model-data-constraints}.md .worktrees/planning/project05-concept-card-skill/arc07-real-corpus-uat-and-feedback/slice04-expanded-corpus-card-generation/artifacts/candidate-cards/cc-memory-forms.md .worktrees/planning/project08-concept-card-metadata/arc01-metadata-research-and-requirements/slice01-metadata-inventory-and-research-questions/artifacts/baseline-snapshots/compcogneuro-{rich,teaching}-rerun-2026-09-12/candidate-cards/cc-model-data-constraints.md .worktrees/planning/old/dev/concept-cards/0009-howto-concept-card-extraction-with-claude-code-v3.2.md knowledge/erlang/concept-cards/otp-design-principles/behaviour.md /Users/oubiwann/lab/music-comp/ai-music-theory/concept-cards/complete-musician/accent-types.md
```

All values are registered in the membership artifact. `git diff --exit-code
682e4a10 --` on source/corpus/prior-packet paths is the fixed entry comparison;
the new artifact paths necessarily differ. A pre-commit current-state check is
not falsely described as a future fixed-endpoint replay.

```sh
jq empty artifacts/semantic-membership.json
git diff --check
git status --short
```

These passed before staging: valid JSON, no whitespace errors, and only the
six Slice09 delivery paths modified/untracked.
