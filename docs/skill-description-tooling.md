# Skill Description Maintenance

The packaging check and Codex's runtime context budget answer different questions.
`make check-skills` enforces this repository's policy of at most 1,023 normalized
Unicode characters per description. It does not guarantee an installed catalog
will fit. Codex 0.154.0 accepts longer descriptions, limits each catalog entry to
1,024 characters, and then shares an aggregate budget across skill metadata.

[OpenAI's skill documentation](https://learn.chatgpt.com/docs/build-skills)
documents a default budget of 2% of the model context window, or 8,000 characters
when the window is unknown. Names and paths also consume space. Descriptions
should start with the key use case and discriminating triggers.

## Setup

Python 3.10+ and PyYAML are required. The launcher uses `SKILL_PYTHON`, then the
repo's `.venv/bin/python` when present, then `python3`. For a new environment:

```sh
python3 -m venv .venv
.venv/bin/python -m pip install -r scripts/requirements-skill-tools.txt
```

Existing virtual environments can install the same requirements without being
recreated. Packaging now requires this parser dependency as well.

## Measure

```sh
make check-skills
make audit-skills
make audit-skills SKILL_AUDIT_ARGS='--json'
make audit-skills SKILL_AUDIT_ARGS='--max-total-chars 10000'
make audit-live-skills
make audit-live-skills SKILL_AUDIT_ARGS='--model MODEL_NAME --output /tmp/live-skills.json'
make test-skill-tools
```

`audit-skills` measures the exact Makefile package list. To scan all source
entrypoints, installed skills, or selected directories:

```sh
sh scripts/skill-descriptions audit knowledge
sh scripts/skill-descriptions audit ~/.agents/skills ~/.codex/skills ~/.codex/plugins/cache --json
```

Source-only skills awaiting packaging appear in the `knowledge` scan but not
the Makefile inventory. Compare like scopes when measuring changes.

Filesystem reports decode YAML before counting, normalize whitespace, and show
decoded characters, normalized characters, UTF-8 bytes, duplicate names, and an
approximate absolute-path line cost. The default 300-character target is an
editorial starting point, not an OpenAI limit or a hard gate. Set `--max-chars`
or `--max-total-chars` for explicit policies. The aggregate policy counts only
descriptions; the approximate token figure uses bytes / 4 rounded per line.
Neither recreates Codex's aliasing, ordering, enabled-plugin selection, or budget
allocation. Errors fail the command; reports still enumerate valid entries.

Directory scans follow symlinks, deduplicate physical paths, include hidden
system skills and `SKILL-*.md` source variants, and exclude generated trees such
as `build`, `target`, `.worktrees`, `.venv`, `workbench`, and `node_modules`. Explicit file
arguments are always inspected. Duplicate names in different files remain
visible. Cached plugin versions and disabled plugins may appear in a filesystem
inventory: do not interpret that count as the active catalog.

`live` runs the real `codex debug prompt-input` diagnostic, without starting a
model turn, then compares rendered local descriptions with their source files.
It saves only skill metadata, not unrelated instructions or the full prompt.
Use the same working directory, model, and environment as the CLI showing the
warning. Configured defaults apply when `--model` is omitted. Codex may initialize
its own caches while running the diagnostic. Unsupported CLI versions fail
explicitly. Skills omitted entirely cannot be inferred from the rendered list.
The report records source parse errors; comparison counts exclude those errors.

The relevant discovery description for host filesystem skills is the top-level
`description` in `SKILL.md`. `metadata.short-description` is also parsed by
Codex and can be used for non-host catalogs. `agents/openai.yaml` contains
UI-facing `interface.short_description` and invocation policy; it is not a
substitute for a concise host discovery description. The inventory reports
these fields separately. The tool deliberately requires valid YAML and explicit
names; it does not imitate Codex's repair of malformed third-party YAML or its
fallback names.

## Prepare and Review Rewrites

```sh
make prepare-skill-rewrites SKILL_REWRITE_DIR=/tmp/skill-rewrites
sh scripts/skill-descriptions prepare knowledge --output-dir /tmp/all-source-rewrites
sh scripts/skill-descriptions review /tmp/skill-rewrites/proposal.json --root "$PWD"
sh scripts/skill-descriptions review /tmp/skill-rewrites/proposal.json --root "$PWD" --apply
```

The Make target selects only packaged entrypoints; `prepare PATH...` also accepts
explicit files or directories for other skill libraries. `prepare` creates a
prompt and a JSON proposal template with source hashes. Give
`prompt.md` to the LLM you choose and put its completed JSON into the proposal
file. This workflow is provider-independent and does not make API calls, spend
model credits, or edit descriptions by itself. It includes the existing
descriptions; the model can consult the source paths for more context.

`review` validates every candidate and prints diffs with the model's rationale.
`--apply` additionally requires a terminal and asks for each file: `y` applies,
Enter or another response skips, and `q` stops. There is no blanket approval
flag. Review capability coverage, triggers, exclusions, and authorization
conditions before approving. A shorter string is not proof of equivalent skill
selection; use representative positive and negative requests to assess routing.

The allowed root is explicit, stale whole-file hashes fail, and only the YAML
description value is replaced. Other metadata and the Markdown body are checked
for semantic/byte preservation. Aliases that prevent isolated replacement fail.
Each accepted file is replaced atomically with its permission bits preserved.
The batch is not transactional: earlier approved edits remain if a later write
fails or you quit. Regenerate proposals after source changes. Null candidates
are reported as unresolved, never silently applied. New report/output paths must
not already exist.

After approval, follow the maintenance contract in `AGENTS.md` and run
`make check-skills` and `make check-package-paths`. Install rebuilt
packages only when ready. Editing a source skill does not change an installed
copy; avoid rewriting vendor plugin caches because updates can replace them.

## Implementation Evidence

Behavior was checked against the installed Codex 0.154.0 diagnostic and these
version-pinned upstream sources:

- [Catalog budget and rendering](https://github.com/openai/codex/blob/rust-v0.154.0/codex-rs/ext/skills/src/render.rs)
- [Frontmatter parser](https://github.com/openai/codex/blob/rust-v0.154.0/codex-rs/skills/src/parser.rs)
- [Optional metadata loader](https://github.com/openai/codex/blob/rust-v0.154.0/codex-rs/ext/skills/src/loader/metadata.rs)

Use `live` again after Codex upgrades rather than assuming these internals remain
unchanged. The tests use the production parser, temporary files, and the real
CLI review command through a PTY; they do not emulate Codex's renderer.
