# Current Skill Description Evaluation

Updated 2026-09-10 against main `c8909905` and planning `361cdc6f`, with local
tooling restored from stash. The user assigned this work project07; existing
projects01 through06 and the canonical planning AGENTS.md are unchanged.

## Findings

The real Codex 0.154.0 diagnostic currently exposes 43 skills, all comparable
with source, with zero changed descriptions and zero characters removed. This
follows removal of `anthropic-skills@claude-cowork` at the user's request, not
application of source rewrites. Other Design and Cowork plugins remain installed.
No claim is made about another model, working directory or future catalog.

The source scan finds 22 skills, 10,598 normalized description characters and
15 descriptions above the proposed 300-character editorial target. The Makefile
packages 20 of those skills, totaling 9,868 characters. `document-extraction`
and `concept-cards` are source-only pending Project05's packaging work; this
project does not change their package disposition.

All source descriptions satisfy the existing 1,023-character repository policy.
That per-file policy does not guarantee that an aggregate runtime catalog fits.
The filesystem installation scan finds 70 files and 22,970 characters, including
inactive cached copies. Only sites-building and sites-hosting have duplicate
names in that scan. Filesystem and active-catalog counts are not interchangeable.

## Source Pass

| Skill | Current chars | Proposed chars | Review focus |
|---|---:|---:|---|
| collaboration-framework | 995 | 285 | Retain engineering posture, lifecycle and domain-routing boundary |
| cobalt-guidelines | 947 | 252 | Keep Cobalt/Liquid and site/build/API triggers |
| erlang-guidelines | 908 | 279 | Keep OTP, supervision, BEAM and tooling coverage |
| rust-guidelines | 896 | 234 | Keep ownership, async, unsafe and API triggers |
| cpp-guidelines | 685 | 246 | Keep RAII, lifetime, concurrency and CMake triggers |
| go-guidelines | 612 | 245 | Keep concurrency, APIs, tests, profiling and Gio |
| javascript-deno-guidelines | 552 | 266 | Keep Deno, JSR, no-Node and project-idiom boundaries |
| scientific-methods | 498 | 288 | Preserve controlled inquiry and ordinary-implementation exclusion |
| visual-design-system | 451 | 247 | Preserve project-specific visual-design scope |
| biome-linter | 377 | 212 | Keep JS/TS/JSX/CSS and accessibility scope |
| tailwindcss | 376 | 199 | Keep v4, CSS-native configuration and responsive variants |
| document-extraction | 372 | 250 | Preserve format/preparation triggers and usable-source/card exclusions |
| concept-cards | 358 | 253 | Preserve card lifecycle, evidence, admission and extraction handoff |
| biome-js-linter | 350 | 238 | Preserve language-only scope and framework/runtime exclusions |
| deno-js-linter | 324 | 199 | Preserve language-only scope, not Deno runtime guidance |
| agent-coordination | 298 | unchanged | Clear delegation-policy trigger |
| project-management | 283 | unchanged | Clear planning/closure/Expedited Mode triggers |
| contribution-style | 281 | unchanged | Distinct upstream-maintainer audience |
| code-auditing | 278 | unchanged | Important diagnosis-only boundary |
| engineering-methods | 264 | unchanged | Methodology design/evaluation scope |
| work-verification | 249 | unchanged | Ledger lifecycle and evidence-strength scope |
| testing | 244 | unchanged | Testing and validation quality scope |

The 15 proposed replacements reduce their subset from 8,701 to 3,693 characters.
With seven unchanged descriptions, the source total would become 5,590, saving
5,008 characters (47.3%). The packaged subset would save 4,781 (48.4%). These are
metadata savings, not measured model-routing improvements or exact token savings.

Thirteen candidates were retained only after matching their original name and
description; all hashes were regenerated from current files. Two candidates were
added after reading the new source skills. Their rationales disclose compressed
distinctions. Review validates 15 candidates, zero unresolved, zero applied.
No source or installed description was edited, and no packages were installed.

## Evidence

- `source-inventory.json`: exact Makefile package list, `make audit-skills`.
- `all-source-inventory.json`: `sh scripts/skill-descriptions audit knowledge`.
- `installed-inventory.json`: `.agents/skills`, `.codex/skills`, plugin cache.
- `live-catalog.json`: real `make audit-live-skills`, configured model default.
- `rewrites/prompt.md`: fresh provider-independent prompt with current hashes.
- `rewrites/proposal.json`: 15 unapplied candidates with individual rationales.
- `proposal-review.log`: actual read-only review output.
- `test-checks.log`: description and version tests plus source check.
- `package-check.log`: rebuilt packages, version and path validation.
- `initial-test-checks.log`: retained first-run version-test failure.
- `pre-sync/`: historical inventories, evaluation, 13-candidate proposal,
  closing report and verification; old paths/hashes are historical, not current.

From main, review the current packet with:

```sh
sh scripts/skill-descriptions review .worktrees/planning/project07-skill-description-budget/slice01-inventory-and-tooling/artifacts/rewrites/proposal.json --root "$PWD"
```

`--apply` adds interactive per-file approval. Follow the source maintenance
contract before rebuilding/installing accepted edits. No API calls are made by
prepare/review. The runtime diagnostic required normal Codex cache access outside
the sandbox and was rerun with approval.

## Limits and History

The initial pre-sync diagnostic observed 55 skills, 21 shortened descriptions
and 5,710 characters removed. The post-plugin-removal snapshot and this refreshed
snapshot both observe 43 with no shortening. Raw evidence is retained separately;
the original warning is not being inferred solely from the repository scan.

The first combined test run passed all 18 description tests but failed an
installed Codex validator output assertion in the existing version suite. A
standalone rerun and the final combined run passed. The original test did not
report stderr or the specific failing process status, so the cause is unknown.
The assertion now requires the expected rejection exit code 1 and includes
stderr on failure. This is improved diagnostics, not a claimed root-cause fix.

Parsing is deliberately stricter than Codex's malformed-YAML repair/fallback
names. Filesystem token estimates do not emulate Codex's allocator. The live
report cannot infer omitted skills. Semantic skill-selection equivalence remains
unverified and user acceptance is pending. Remote CI was not executed.

See `pre-sync/evaluation.md` and the implementation usage guide for pinned Codex
source references and the original metadata-field investigation.
