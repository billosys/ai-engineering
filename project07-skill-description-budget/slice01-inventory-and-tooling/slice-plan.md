# Inventory and Tooling

Implement Python tooling consistent with existing repository packaging scripts.
Use a real YAML parser, count decoded and normalized Unicode characters and UTF-8
bytes, report all descriptions and duplicate names, and expose configurable
per-skill and aggregate thresholds. Retain the existing packaging check entrypoint.
Use Codex's real prompt diagnostic to evaluate the live rendered catalog; do not
claim a filesystem scan duplicates Codex plugin enablement or rendering.

Generate an LLM prompt with source descriptions and explicit output requirements.
Validate candidate descriptions, show a diff, require interactive approval for
each applied edit, reject stale source files, and preserve other frontmatter and
body bytes. Default behavior produces a review without modifying skills.

Artifacts: `artifacts/` in this slice. Include source and installed inventories,
current Codex evidence, findings, and a source-description rewrite proposal.
No automatic rewrite of repository skills, installed skills, or plugin caches.

Verify parser boundaries, Unicode, YAML forms, invalid metadata, stale proposals,
approval decisions, and byte preservation with real unit tests and temporary
files. Run Make checks and a real dry-run of the proposal workflow.

## Version History

- 1.1 (2026-09-10): Refresh after upstream synchronization under project07.
  Distinguish all 22 source skills from 20 packaged skills; regenerate proposal
  hashes, include two new source-only candidates, retain version/history gates,
  and archive pre-sync evidence. Actual source rewrites remain approval-gated.
- 1.0 (2026-09-10): Initial implementation and evidence scope.
