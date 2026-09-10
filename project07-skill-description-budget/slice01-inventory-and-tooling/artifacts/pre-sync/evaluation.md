# Skill Description Evaluation, 2026-09-10

The warning is reproducible with installed Codex CLI 0.154.0 in this repository.
The diagnostic exposes 55 skills, shortens 21 descriptions, and removes 5,710
characters from 23,319 source description characters. Long descriptions retain
roughly 418-422 characters. No compared file failed parsing.

The configured default model at capture was `gpt-6-astra`; the diagnostic used
the current configuration without a model override. This is one CLI snapshot,
not a claim that every model or desktop task has the same catalog or budget.

## What Codex Counts

The top-level YAML `description` in each host `SKILL.md` is whitespace-normalized
before catalog rendering. `agents/openai.yaml` holds separate UI description and
invocation-policy metadata. Frontmatter `metadata.short-description` is another
field, used by the non-host rendering policy when present. Neither short field
replaces the host discovery description measured here.

The version-pinned renderer allocates 2% of the context window by default, or
8,000 characters when it cannot determine the window. A configured token budget
can override the default (clamped to 10,000); this evaluation changes no setting.
Names and locators consume space alongside descriptions. Aliases can shorten
paths. The renderer caps individual catalog descriptions at 1,024 characters,
then shares remaining description space round-robin. It warns when average
removed characters per catalog entry exceeds 100, or when entries are omitted.
Here, ceiling(5710 / 55) = 104, consistent with the reported warning.

The old checker enforced 1,023 characters per file, parsed YAML with awk, and
did not inspect aggregate or actual rendered costs. All 20 packaged descriptions
passed it. That result could never establish that the full installed catalog
would fit. The replacement keeps the stricter repository policy and measures
decoded and normalized strings through PyYAML.

Sources:

- [Official skill documentation](https://learn.chatgpt.com/docs/build-skills)
- [Codex 0.154.0 renderer](https://github.com/openai/codex/blob/rust-v0.154.0/codex-rs/ext/skills/src/render.rs)
- [Codex 0.154.0 parser](https://github.com/openai/codex/blob/rust-v0.154.0/codex-rs/skills/src/parser.rs)
- [Codex 0.154.0 optional metadata](https://github.com/openai/codex/blob/rust-v0.154.0/codex-rs/ext/skills/src/loader/metadata.rs)

## Packaged Source Pass

All 20 packaged source descriptions total 9,868 normalized characters. The same
20 files were found by the source-tree scan with generated/research workbench
directories excluded. All are valid YAML and within the current packaging gate.

| Skill | Characters | Assessment |
|---|---:|---|
| collaboration-framework | 995 | High priority: long provenance and operational list; live trigger tail lost |
| cobalt-guidelines | 947 | High priority: bibliography and API symbols precede/expand triggers |
| erlang-guidelines | 908 | High priority: source bibliography and exhaustive tool/task lists |
| rust-guidelines | 896 | High priority: bibliography delays triggers; many task families cut off |
| cpp-guidelines | 685 | Condense provenance and examples while preserving ownership/resource scope |
| go-guidelines | 612 | Keep Go tasks and the distinctive Gio UI trigger; move source list out |
| javascript-deno-guidelines | 552 | Preserve project no-Node boundary, JSR, migration, and Deno tasks |
| scientific-methods | 498 | Preserve experiment trigger and exclusion for ordinary implementation |
| visual-design-system | 451 | Preserve project identity; condense repeated design task examples |
| biome-linter | 377 | Keep web language scope; drop brittle rule count and repeated categories |
| tailwindcss | 376 | Keep v4 and CSS-native configuration; condense exhaustive directive list |
| biome-js-linter | 350 | Preserve language-only boundary and all exclusions |
| deno-js-linter | 324 | Preserve distinction between rule provider and supported runtime scope |
| agent-coordination | 298 | Within proposed target; clear delegation trigger, no immediate rewrite |
| project-management | 283 | Within target; specific planning/closure/Expedited Mode triggers |
| contribution-style | 281 | Within target; distinctive upstream-maintainer audience |
| code-auditing | 278 | Within target; useful diagnosis-only boundary |
| engineering-methods | 264 | Within target; methodology design and evaluation scope |
| work-verification | 249 | Within target; ledger lifecycle and evidence-strength scope |
| testing | 244 | Within target; testing/validation quality scope |

300 characters is a proposed editorial target, not a universal Codex limit.
Some skills may need more to retain discriminating triggers. The seven unchanged
descriptions total 1,897 characters. Thirteen proposals reduce their subset from
7,971 to 3,190, taking the packaged total to 5,087: 4,781 characters saved (48.4%).
All candidates pass syntax, length, stale-source, and isolated-replacement checks.
No candidate has been applied. Rationale fields call out details omitted from
each discovery summary; those details remain in the skill bodies.

## Installed Catalog Pass

The filesystem inventory found 82 skill files with 29,689 description characters
and no parse errors. This includes inactive or cached plugins and is deliberately
not treated as the active count. There are seven duplicate-name groups:
collaboration-framework, Go, Rust, PDF, skill-creator, sites-building, sites-hosting.

The real CLI snapshot includes both standalone and `anthropic-skills:` copies of
collaboration-framework, Go, and Rust. Their plugin descriptions consume 2,504
source characters in addition to the standalone copies. These may be intentional;
the tool exposes them for a user decision. Merely scanning a cache cannot establish
whether a duplicate is active, which is why the live diagnostic matters.

The active catalog is broader than this repository's packages. Vendor document
skills and system skills also contribute pressure; source rewrites alone cannot
guarantee the warning disappears. Source changes only affect installed copies
after rebuilding/installing, and plugin copies have separate ownership. Do not
edit vendor caches as a durable fix.

## Reproduction and Artifacts

- `source-inventory.json`: exact Makefile package list, `make audit-skills`.
- `all-source-inventory.json`: source-tree scan, same 20 entrypoints.
- `installed-inventory.json`: `.agents/skills`, `.codex/skills`, plugin cache.
- `live-catalog.json`: real CLI rendering and per-file before/after lengths.
- `rewrites/prompt.md`: provider-independent LLM shortening prompt.
- `rewrites/proposal.json`: 13 LLM-authored candidates with original hashes.
- `research-inclusive-template/`: initial exploratory prompt including ignored
  research clones under `knowledge/go/workbench`; not a proposed source rewrite.
  This exposed a discovery-scope issue, resolved by excluding nested workbenches
  and using the Makefile list for packaged-skill proposals.
- `package-check.log`: full Make packaging and path-validation output.

From the implementation worktree, inspect candidates with:

```sh
sh scripts/skill-descriptions review .worktrees/planning/project01-skill-description-budget/slice01-inventory-and-tooling/artifacts/rewrites/proposal.json --root "$PWD"
```

Add `--apply` only when ready for interactive per-file decisions. After approved
source edits, update affected component versions/history and run the skill and
package gates before installation. Then rerun the live diagnostic on the model
and working directory that originally displayed the warning.

## Limits

This pass measures metadata and reviews its structure; it does not prove unchanged
skill-selection accuracy. Behavioral comparisons using representative positive
and negative prompts remain a follow-up before treating the candidates as tuned
routing metadata. The checker is intentionally stricter than Codex about missing
names and malformed YAML repairs, and its standalone token estimate is not a
replica of the runtime allocator. The live command observes only rendered skills;
it cannot count skills omitted entirely. Remote CI execution was not performed.
