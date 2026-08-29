# Transitional Exception Disposition

Slice 04 reviewed every `expires=after-arc02` row that existed in
`package-path-exceptions.tsv`.

| Package | Document | Target | Prior disposition | Slice 04 disposition | Rationale |
|---------|----------|--------|-------------------|----------------------|-----------|
| `rust-guidelines.zip` | `guides/README.md` | `./14-cli-tools/09-common-pitfalls.md` | `transitional-warning`, `after-arc02` | `warning`, `later-rust-guide-maintenance` | The referenced file is still absent from the packaged Rust guide. It remains a visible backlog warning. |
| `rust-guidelines.zip` | `guides/14-cli-tools/README.md` | `09-common-pitfalls.md*` | `transitional-warning`, `after-arc02` | `warning`, `later-rust-guide-maintenance` | The CLI pitfalls references still resolve to a file not shipped in the package. |
| `cpp-guidelines.zip` | `guides/03-functions.md` | `./param-passing-*.png` | `transitional-warning`, `after-arc02` | `warning`, `later-cpp-asset-maintenance` | The image references are still not packaged. They should stay visible until asset packaging or prose is corrected. |
| `javascript-deno-guidelines.zip` | `guides/*` | `12-deno/*.md` | `transitional-warning`, `after-arc02` | `warning`, `later-js-guide-harmonisation` | Guide-internal shorthand still produces package-relative misses and should be normalized later. |
| `javascript-deno-guidelines.zip` | `guides/*` | `13-biome/*.md` | `transitional-warning`, `after-arc02` | `warning`, `later-js-guide-harmonisation` | Guide-internal shorthand still produces package-relative misses and should be normalized later. |

No transitional row was promoted to `explicit-exception`. No stale `after-arc02`
expiry remains in the post-change inventory.
