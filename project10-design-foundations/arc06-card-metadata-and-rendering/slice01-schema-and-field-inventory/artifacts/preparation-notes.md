# Metadata Planning Preparation

Author: CDC Sofie. Date: 2026-10-10. Strength: direct author inspection and
preliminary tool-assisted census; not independent acceptance of Arc06/Slice01.
No design/source file, Project08 record or active Arc02 assignment was edited.

## Authority and schema readiness

The Operator asks for existing-field harmony and consistent GitHub rendering,
allows historical 3.2 when the unified replacement is unavailable, and explicitly
prohibits filling missing fields. Project08's project plan leaves Arc02 metadata
architecture provisional, P-15 remains open, and its discussion agenda prohibits
normative adoption from inventory/templates. Source concept-cards reports a skill
release, 4.8.1, and explicitly describes templates as conventions, not finalized
schemas/validators. These are different authorities and version sequences.

The 3.2 definition is referenced by Project08's
[input register](../../../../project08-concept-card-metadata/arc01-metadata-research-and-requirements/slice01-metadata-inventory-and-research-questions/artifacts/input-register.md).
A preserved copy exists in Project05's
[source-v32 artifact](../../../../project05-concept-card-skill/artifacts/source-v32/source-0009-howto-concept-card-extraction-with-llms-v3.2.md).
The older definition is
[the historical HOWTO](../../../../old/dev/concept-cards/0009-howto-concept-card-extraction-with-claude-code-v3.2.md).
Its Field by Field section provides the fallback representation; it is prose
with examples, not a newly asserted closed machine schema. The copy differs
only in its first title line (“Claude Code” versus “LLMs”); selected schema
sections are byte-equal, but their full-file hashes are not interchangeable.

| Input (repository-relative) | Revision | Git blob | Full lines | Whole-file SHA-256 | Actual inspection |
|---|---|---|---:|---|---|
| `project08-concept-card-metadata/project-plan.md` | `6a016960a77d9dd2e6478aeb3df96ff6b3d905eb` | `52109e7019d8d1768623759a2c8ccadbf4acb687` | 697 | `20c50a2c4c2e4cc19c2b747c72cd560b099af3053e38d498e1415bdfcd878e49` | 1–250; normative status/dependencies/P-15, not all history |
| `project08-concept-card-metadata/ledger.md` | `6a016960a77d9dd2e6478aeb3df96ff6b3d905eb` | `318d2503ba4f597636c0094f162a94474c515225` | 43 | `1bfce0e574c65b32820bd7c812dd798cff4ad7b312331b0917beef7bdc71c0db` | 1–43 complete |
| `project08-concept-card-metadata/artifacts/schema-and-spec-discussion-agenda.md` | `6a016960a77d9dd2e6478aeb3df96ff6b3d905eb` | `89daa1f2992a2b0b58642c8831c54e333a142399` | 87 | `10a74016b63c8afe7d2062d7a9643ca26f6d36daabfa5cdeee3f0da1ff168196` | 1–87 complete |
| `old/dev/concept-cards/0009-howto-concept-card-extraction-with-claude-code-v3.2.md` | `6a016960a77d9dd2e6478aeb3df96ff6b3d905eb` | `a8a47d496235003b3925c98a75676a888a27c3bd` | 862 | `56eb092cfed206edf588748e041df9ed53448f941f1dee43684f96994a898cbd` | 92–221, 632–650, 828–837 plus heading/field queries |
| `project05-concept-card-skill/artifacts/source-v32/source-0009-howto-concept-card-extraction-with-llms-v3.2.md` | `6a016960a77d9dd2e6478aeb3df96ff6b3d905eb` | `dcd45e5c24ade51bb64417c1a9ea8d1361d3dd35` | 862 | `b1cfa8b4114a299f621ada9898b63a4a8b2e4a3dfd961b939b8eea745f3872d9` | 92–220 bytes compared to original; full-file diff only title |
| `knowledge/concept-cards/SKILL.md` | `dffa504e851b03b8e4746f1941068e4cc850b612` | `33880bb84997e3eb00d6eba50e1a09ea9f33330e` | 158 | `a096893e6a908d014b795bcb2e5e38653b6c590982e99951aae3783a9e7c318a` | 1–158 complete; template/skill versus finalized schema distinctions |

Also inspected current Project10 plan/ledger, Arc02 capability/family/current
assignment sections, concept-cards load contract, validation guide's structural/
semantic distinctions, card template and field/validation references. The matrix
card header/body through 125 supplied a concrete raw example; a Project08 newer
Memory Forms card through 36 supplied a representation reference. Neither was a
hosted rendering observation or a source-fidelity verdict.

## Preliminary complete header census

SOURCE `dffa504e851b03b8e4746f1941068e4cc850b612`. Git's tracked concept-card path set contains 233 Markdown files.
All 233 start with a leading `---` block and parse as YAML mappings using
YAML::XS 0.82 and JSON::PP 4.06. A root-key spelling scan found no duplicate
root keys; nested duplicates and full schema validity were not assessed here.
The census extracted headers only. No complete-body semantic reading occurred.
The incidental helper and its JSON are temporary author preparation, not a
maintained validator; Slice01 must supply the durable inventory and replay.

Collections: Arnheim 112, Cleland 19, Tschichold 19, Butterick 37, posts 46; total 233.
All 19 historical fields are present in every card: `aliases`, `answers_questions`, `authors`, `category`, `chapter`, `chapter_number`, `concept`, `contrasts_with`, `extends`, `extraction_confidence`, `pdf_page`, `prerequisites`, `related`, `section`, `slug`, `source`, `source_slug`, `subcategory`, `tier`.
This contradicts the initial suspicion that many historical fields are absent;
it says nothing about completeness under a future unified profile. Do not add
its missing modern control/provenance fields from templates.

Existing extensions: `layer` 233, `rosetta_stone` 232, `css_implementation` 222.
One absent rosetta field and eleven absent CSS fields remain absent; absence is
not permission to insert empty/default values. Full extension meanings still
need the crosswalk. Nulls already occur in subcategory 24, section 75,
chapter_number 83 and pdf_page 83; authors remain scalar strings in all 233.

Wrong-shape empty sentinels `[[]]` occur 106 times across 59 distinct cards:
`extends` 42, `contrasts_with` 37, `prerequisites` 14, `aliases` 13. The historical
method describes string-valued lists and empty arrays; this warrants an explicit
field-specific empty-list correction, not arbitrary flattening. All other
existing values and list members require preservation checks. These counts do
not establish the cause of the Operator-reported GitHub rendering failure.

## Primary rendering evidence and future oracle

Inspected on 2026-10-10: [GitHub's metadata rendering announcement](https://github.blog/news-insights/product-news/viewing-yaml-metadata-in-your-documents/),
body lines 429–449, documents native repository metadata presentation; its age
makes a current exact-commit host check essential. [GitHub Markup README](https://github.com/github/markup/blob/master/README.md),
rendering pipeline at 189–197, distinguishes local markup conversion from
additional GitHub processing. Therefore parse success/local GFM is supporting
evidence, and future Slice04 requires actual rendered file-view observations.
No current design card was inspected in a native GitHub rendered view this turn;
the symptom remains Operator-reported and its precise cause unconfirmed.

Every final card gets a baseline/current/revision/URL/check/result row. Local
preservation checks cover the whole corpus; hosted checks cover all final cards
and retain failed/blocked observations. A missing hosted candidate is a named
rendering-evidence blocker, not a reason to publish without authority or claim
success. Arc04 owns package composition; Arc05 repeats affected checks after
later changes. No package, installation, original acquisition or release check
was performed by this planning work.

## Recovery and concurrency record

Initial historical-path lookups ran from SOURCE instead of planning and failed;
explicit planning paths recovered the actual inputs. A guessed metadata guide
and two guessed/example paths were unavailable; the live guide map/input register
supplied actual routes instead. System Python lacked PyYAML; the already-present
YAML::XS/JSON::PP parser was used, with no install. A preliminary full-copy-equality
assertion failed because the title was renamed; the full diff and selected-section
comparison recovered the true relationship. All 233 headers then parsed.

Concurrent CC work advanced planning commits and staged/modified Arc02 outputs
while this request was investigated. All edits/commits from this planning change
use an exact allowlist of Project10 plan/ledger plus new Arc06 files. Active CC
outputs, issued prompts, source/main and unrelated Project12/knowledge/lfe are
outside that set. Preparation input revision is `6a016960a77d9dd2e6478aeb3df96ff6b3d905eb`; it is not a claim
that concurrent work was reviewed or accepted. Arc06 is queued, with no CC prompt
issued and no interruption of the current Arc02 assignment.

## Planning validation

The 13-file planning allowlist passed checks: all eleven prior project criterion
rows are byte-identical; two new project rows and 31 arc/slice rows remain open;
five new plan frontmatters parse with planned status; six upstream input
revision/blob/hash/extent receipts match committed objects. No CC prompt,
closing report or acceptance record is pre-created. SOURCE HEAD and tracked/index
remain unchanged. Local-link/fragment and LF/diff checks are run before the
scoped commit; they are planning checks, not migration or GitHub success.
