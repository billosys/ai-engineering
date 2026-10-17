# Fennel source provenance

Acquired 2026-10-17. The original Markdown and LICENSE are under `md/`.
These are retained source bytes, not reformatted or corrected derivatives.

## Source chain and selection

- Website: https://git.sr.ht/~technomancy/fennel-lang.org at
  `253e9463c2d6a306feecb37237beee303f9714c1`.
- Its README says documentation comes from the main Fennel repository. Its
  `.gitmodules` names https://git.sr.ht/~technomancy/fennel, and its Makefile
  `%.html: fennel/%.md` rule generates the requested pages from that submodule.
- Website's language gitlink: `9af5e47fa7ddea806544d15507412ddc51bd046d`,
  release 1.6.1. This is the imported snapshot, not an assertion about the
  site's current deployment or the current upstream branch.
- Filtered tip: `a9acb3b88012ac923ff9b23c5cf37d9ed6b7cb7c`.
- Integration merge: `c6a089ba8f0809d9147ea60d66e3d78f02bd4792`. The second parent contains the filtered
  history; no squash, submodule, nested repository or compiler implementation.

| Page / purpose | Retained file |
|---|---|
| https://fennel-lang.org/style | [style.md](./md/style.md) |
| https://fennel-lang.org/values | [values.md](./md/values.md) |
| https://fennel-lang.org/setup | [setup.md](./md/setup.md) |
| https://fennel-lang.org/tutorial | [tutorial.md](./md/tutorial.md) |
| https://fennel-lang.org/reference | [reference.md](./md/reference.md) |
| https://fennel-lang.org/macros | [macros.md](./md/macros.md) |
| Embedding / compiler API | [api.md](./md/api.md) |
| Runtime and standard library | [lua-primer.md](./md/lua-primer.md) |
| Design rationale | [rationale.md](./md/rationale.md) |
| Avoid carrying Clojure semantics into Fennel | [from-clojure.md](./md/from-clojure.md) |
| Compiler sandbox and release provenance | [security.md](./md/security.md) |
| Version boundaries and migration | [changelog.md](./md/changelog.md) |
| Overview and historical ancestor of api.md | [README.md](./md/README.md) |
| General upstream license | [LICENSE](./md/LICENSE) |

README is necessary to retain the earlier API documentation lineage. `git log
--follow` found no other predecessor filenames for the selected paths. The
[retained-paths manifest](./retained-paths.json) records that inspection.
Unselected paths (compiler code, tests, CI, website assets, conduct and contributor
docs) were removed from the disposable filtered clone, not from this repository.
Unmodified upstream documents may reference excluded files or website routes;
those links are source evidence, not promises of a standalone local manual.

## History-preserving import

A full clone was made in a temporary directory, its `fennel` submodule initialized,
and a separate `--no-local` clone of that language repository made for filtering.
Only the pinned import branch was fetched into ai-engineering; no upstream tags
or branch names were installed. Equivalent commands, from a disposable full
Fennel clone checked out at the pin:

```sh
git switch -c fennel-docs-import 9af5e47fa7ddea806544d15507412ddc51bd046d
git filter-repo --force --preserve-commit-hashes --preserve-commit-encoding \
  --path style.md --path values.md --path setup.md --path tutorial.md \
  --path reference.md --path macros.md --path api.md --path lua-primer.md \
  --path rationale.md --path from-clojure.md --path security.md \
  --path changelog.md --path README.md --path LICENSE \
  --to-subdirectory-filter knowledge/fennel/sources/md/
# In ai-engineering, fetch that branch from the disposable filtered clone,
# then merge its tip with --allow-unrelated-histories --no-ff (no squash).
```

The filter changes paths, trees, parents and therefore commit IDs. It removes
unrelated commits and empty/degenerate commits caused by filtering. The
`--preserve-commit-hashes` option prevents rewriting hash references inside
messages; it does not preserve commit IDs. Original author/committer identities,
timestamps and messages were compared with every retained rewritten commit.
Cryptographic commit signatures cannot remain valid after rewriting.

[commit-map.tsv](./commit-map.tsv) maps all 749 retained reachable commits to their
original IDs. [history-verification.json](./history-verification.json) records
14 tip blobs (SHA-1 and SHA-256), 749 complete historical tree/metadata comparisons,
and 7,493 historical blob comparisons. File trees were compared as mode, object
ID and relative path; matching blob IDs establish exact historical bytes.

Review history directly:

```sh
git log --full-history -- knowledge/fennel/sources/md/api.md
git log --follow -- knowledge/fennel/sources/md/README.md
git show a9acb3b88012ac923ff9b23c5cf37d9ed6b7cb7c:knowledge/fennel/sources/md/style.md
python3 knowledge/fennel/sources/verify-import.py /path/to/original/fennel .
```

The verifier needs a full original upstream clone containing the pinned commits,
plus this repository containing the imported graph. It checks historical trees,
identity/message metadata, selected-path history coverage and current source bytes.
Its results establish import fidelity, not correctness of upstream prose or the
derived guides.

## Attribution and licenses

General upstream material: MIT, copyright 2016–2025 Calvin Rose and contributors,
as stated in [the upstream README license section](./md/README.md#license); see
[the original LICENSE](./md/LICENSE). The LICENSE contains the MIT terms but does
not itself name a copyright holder. Individual notices take precedence for
their files. In particular [style.md](./md/style.md) explicitly credits Taylor
R. Campbell (2007–2011), Phil Hagelberg and contributors (2021–2023), and uses
[CC BY-NC-SA 3.0](https://creativecommons.org/licenses/by-nc-sa/3.0/).
It derives from Taylor R. Campbell's Lisp Style Guide.

The Fennel skill's newly adapted prose (SKILL.md and guides) is provided under
CC BY-NC-SA 3.0 with that attribution. It is edited and reorganized for practical
Fennel authoring; it is not an unchanged upstream publication. Upstream source
files retain their own licenses. The repository's root MIT notice does not
relicense the imported style guide or these adaptations. Source files are
excluded from the installable skill zip; the package's source/license guide
carries attribution and pinned upstream references.
