# Slice01 Input Register

Iteration 01, 2026-09-12. Inputs are read-only; availability is not semantic verification.

| Input | Exact identity / use |
| --- | --- |
| Source checkout | `/Users/oubiwann/lab/billosys/ai-engineering`, `main` `e763c661592ff1097a94bb470db9cf924524579d`; `knowledge/concept-cards/SKILL.md` blob `33880bb84997e3eb00d6eba50e1a09ea9f33330e`, `metadata.version: 4.8.1`. |
| Planning checkout | `.worktrees/planning`, HEAD `03c5b20756cfbb797ab6142021c8d4a8cd5555f8`; historical prompts, Project05 inputs and Project08 plan. |
| Prompts | `old/dev/concept-cards/0009-howto-concept-card-extraction-with-claude-code-v3.2.md` blob `a8a47d496235003b3925c98a75676a888a27c3bd`; `0010-a-guide-for-parallel-concept-card-re-extraction-v3.2.md` blob `34ac0599d2ce1e0e3e64d1964fdf4e8cf221f258`; v3.1 predecessors `0007` and `0008` inspected. |
| Legacy corpora | Complete Musician external Git `2e23e2635681a17da6083634e142249dccf8ae58`, 390 files; wider Erlang census 1,664 files, including the separately identified 224-file `design-scale-erlang-otp/` subset. |
| Current method prose | Concept-cards load/re-extraction/lifecycle/graph/validation guides; templates/examples; references `record-field-groups`, `vocabulary`, `semantic-audit-boundaries`, `operator-review-gates`; document-extraction `concept-card-handoff` and Output Contract. Read as prose, not claimed parsed frontmatter. |
| Arc07 candidates | Two Arc07 candidate-card directories: ten concept cards, four source-support records and two prose READMEs. |
| CompCogNeuro source | Observed 2026-09-12 at `/private/tmp/project05-compcogneuro-book-e0c697b4`: clean, exact HEAD `e0c697b4d4d134f29cb5c2bbde41b1b6b409b63d`, `chapter-01.md` and `chapter-07.md` present. No semantic source-support re-verification was performed. |

## Preserved baseline and parser

The rich tree has 14 files and teaching tree 13: 27 total. Their mapped copies
and `source-sha256sums.txt`/`copy-sha256sums.txt` preserve all 27 pairs.

`inventory-frontmatter.fnl` is the active route. Fennel 1.6.1 on Lua 5.5 owns
discovery, ordering, root/error reporting and report assembly; the explicit
local parser bridge uses installed `YAML::XS 0.82`, `JSON::PP 4.06` and
`Digest::SHA`. YAML::XS emits dates/booleans as scalars rather than the initial
Psych draft's Ruby classes. Fixtures exercise null, empty, nested, malformed,
non-mapping, unterminated and missing-root states. No global install/configuration
was changed.
