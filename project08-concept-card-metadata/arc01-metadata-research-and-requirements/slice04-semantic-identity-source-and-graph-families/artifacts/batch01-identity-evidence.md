# Batch01 Identity Evidence

## Scope and representation

This is a partial authored replacement for exactly ten mechanical path/kind pairs.
The companion JSON registers every membership with a meaning ID, explicit
disposition, and resolvable evidence IDs. Its meanings and evidence objects
carry shared definitions plus exact path, SHA-256, section, and revision.
Aliases containers and aliases[] members are deliberately distinct. Untyped
evidence is two inspected legacy contexts, not an inferred common schema.

## Inspected inputs and observations

| Context | Exact path, SHA-256, revision | Values and body section |
| --- | --- | --- |
| Current template | knowledge/concept-cards/templates/concept-card.md; 24d88eaa1edeae31ccd4943e8f635e0e3dc11e26e9a1b69ba3374b49d9700fec; source e763c661 | Frontmatter lines 1-25: null id/revision/title/concept_slug and aliases: []; placeholders are not missing values. |
| Current entrypoint | knowledge/concept-cards/SKILL.md; a096893e6a908d014b795bcb2e5e38653b6c590982e99951aae3783a9e7c318a; metadata 4.8.1 | References And Review Surfaces lines 133-146: IDs/revisions preserve identity, paths locate records. |
| Complete Musician | /Users/oubiwann/lab/music-comp/ai-music-theory/concept-cards/complete-musician/accent-types.md; c5af9d16b099430d15d6a6fab2beaa00aea73704021a0c224056a271ffe07fde; corpus 2e23e2635681a17da6083634e142249dccf8ae58 | concept Accent Types, slug accent-types, four aliases; body Quick Definition. |
| design-scale-erlang-otp | knowledge/erlang/concept-cards/design-scale-erlang-otp/application-behaviour.md; ad84fd8277c9fe70dc9e3c0b08ae067b6b9faaf51a9553dc2e2cbf5811c002eb; no record revision | CORE IDENTIFICATION Application Behaviour/application-behaviour; VARIANTS three aliases; body Quick Definition; source_slug separately design-scale-erlang-otp. |
| Arc07 | .worktrees/planning/project05-concept-card-skill/arc07-real-corpus-uat-and-feedback/slice02-pilot-markdown-preparation-and-card-extraction/artifacts/candidate-cards/cc-emergent-explanation.md; a7b5b387434bc82885ad013b36ed65d354cdb7687d4d3fa1daaffcebadbcbead; record revision 1 | cc-emergent-explanation, emergent_explanation, title/aliases; body Concept Boundary. |
| usable rich rerun | workbench/compcogneuro-rich-rerun-2026-09-12/candidate-cards/cc-pattern-completion.md; 822f64b87c31cbea36624f1fc6323e4fd3eb3f8269a72bbfbd3358a53a210ece; record revision 2 | cc-pattern-completion, pattern_completion, title Pattern Completion From Partial Cues, two aliases; body Quick Definition And Core Definition. |
| teaching rerun | workbench/compcogneuro-teaching-rerun-2026-09-12/candidate-cards/cc-pattern-completion.md; 08389f04949c4fe78cafb567d5741195827af13c73f4cf6f59589d8caf682c56; record revision 3 | Same id/concept_slug, title Pattern Completion, one alias; same named body section, different wording. |
| malformed rich | workbench/compcogneuro-rich-rerun-2026-09-12/candidate-cards/cc-memory-forms.md; d9bc411c40684815798d6b9a952c821f1bd8c3ef81be2839ff0fb7fecec17593; revision unavailable | YAML::XS mapping-values error, frontmatter line 4 column 20: invalid YAML, not populated-value evidence. |

Both predecessor prompts and both v3.2 prompts were read in full. v3.1 0007
(8308788db39358a0d28631913b8319e5b4bbf9fd79545b1f16484ea5e47d637c),
Core Identification 86-101 and Variants 145-165, makes slug a lowercase-
hyphenated filename and aliases authority control. v3.1 0008
(7d7c5b53c4d8aa4c6f479d5af453e3cb9ba50c07f2b9ed8cb8ef15acc4520e66),
template 314-344, filename 578-619, requirements 831-840 repeats this.
v3.2 0009 path old/dev/concept-cards/0009-howto-concept-card-extraction-with-claude-code-v3.2.md
has SHA-256 56eb092cfed206edf588748e041df9ed53448f941f1dee43684f96994a898cbd.
v3.2 0010 path old/dev/concept-cards/0010-a-guide-for-parallel-concept-card-re-extraction-v3.2.md
has SHA-256 b942d34237391d7a8d84ad463cd2c25aa72196adbc98797877dabc26a5ba337c;
template 351-382 retains legacy concept/slug/aliases, 613-619 requires
filename equality, and 870-890 requires aliases empty when none. It supports
legacy lookup practice, not current stable-ID equivalence.

## Comparisons and consequences

legacy-slug is filename-coupled legacy lookup; current-id is record identity.
Record-revision is not source edition: rich revision 2 and teaching revision 3
share id/concept_slug. Title-display is not identity because titles differ.
Legacy concept is a display/teaching label; concept_slug is separately named
current lookup. Both legacy and usable current records have aliases, but this
does not prove historic authority curation was retained. Migration must retain
filename lookup, id/revision, display labels, aliases and parse state separately.
Open: corpus-wide slug/id mapping, alias retention and the other 545 pairs.
No source-book claim is inferred from generated-card bodies.

## Executed Validation Record: CDC Replay Correction

CDC corrected this section on 2026-09-12 without changing CC's semantic
analysis or membership registry. The original CC transcript is preserved in
commit `995c86d6`; its relative `artifacts/` paths fail from the claimed
repository-root cwd (independently reproduced: exit 2), and its temporary
checksum file is not a durable replay input. Do not attribute the commands
below to CC's original run.

Run this complete replacement from the source checkout. It uses the committed
evidence registry for all twelve checksum inputs, asserts exact pairs and
both membership-to-meaning and meaning-to-evidence links, and separately checks
the unchanged original full partition and Slice01 evidence.

~~~bash
set -euo pipefail
cd /Users/oubiwann/lab/billosys/ai-engineering
jq -e --slurpfile i '.worktrees/planning/project08-concept-card-metadata/arc01-metadata-research-and-requirements/slice01-metadata-inventory-and-research-questions/artifacts/field-dispositions.json' '. as $root |
([.memberships[]|[.field_path,.record_kind]]|sort) as $actual |
([["aliases","concept-card"],["aliases","untyped"],["aliases[]","concept-card"],["aliases[]","untyped"],["concept","untyped"],["concept_slug","concept-card"],["id","concept-card"],["revision","concept-card"],["slug","untyped"],["title","concept-card"]]|sort) as $expected |
([$i[0].field_paths[]|.field_path as $p|.record_kinds[]|[$p,.]]) as $all |
(($actual==$expected) and (($actual-$all)==[]) and
all(.memberships[]; (.disposition|type)=="string" and (.disposition|length)>0 and ($root.meanings[.meaning_id]!=null) and all(.evidence_ids[]; $root.evidence[.]!=null)) and
all(.meanings[]; all(.evidence_ids[]; $root.evidence[.]!=null)))' '.worktrees/planning/project08-concept-card-metadata/arc01-metadata-research-and-requirements/slice04-semantic-identity-source-and-graph-families/artifacts/batch01-identity-membership.json'
bash -o pipefail -c 'jq -r '\''.evidence[] | [.sha256,.path] | join("  ")'\'' '\''.worktrees/planning/project08-concept-card-metadata/arc01-metadata-research-and-requirements/slice04-semantic-identity-source-and-graph-families/artifacts/batch01-identity-membership.json'\'' | shasum -a 256 -c -'
git -C .worktrees/planning diff --exit-code 76d284f4 -- project08-concept-card-metadata/arc01-metadata-research-and-requirements/slice01-metadata-inventory-and-research-questions
git -C .worktrees/planning diff --exit-code 76d284f4 -- project08-concept-card-metadata/arc01-metadata-research-and-requirements/slice04-semantic-identity-source-and-graph-families/artifacts/semantic-membership.json project08-concept-card-metadata/arc01-metadata-research-and-requirements/slice04-semantic-identity-source-and-graph-families/artifacts/remainder-membership.json
git -C .worktrees/planning diff --check
~~~

CDC executed every replacement command: the jq assertion returned `true`,
all twelve registered inputs reported `OK`, and both preserved-input diffs
and whitespace check returned exit 0 with no output. No transient checksum
manifest is required. These are structural/identity checks; semantic review
and its scope are recorded separately in `../cdc-verification.md`.

Batch01's ten-pair evidence checkpoint is independently accepted within its
declared sample scope. Slice04 remains changes-required for the remaining
semantics and full-packet integration; no source-book verification, migration,
operator acceptance or whole-profile equivalence is implied.
