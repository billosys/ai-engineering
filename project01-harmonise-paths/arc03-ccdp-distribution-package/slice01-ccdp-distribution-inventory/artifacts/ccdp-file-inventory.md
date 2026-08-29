# CCDP File Inventory Summary

Inventory sources:

- `ccdp-file-inventory.txt`: raw on-disk `find protocols/ccdp -maxdepth 4 -type f -print`.
- `ccdp-file-inventory-tracked.txt`: `git ls-files protocols/ccdp README.md Makefile`.
- `ccdp-file-counts.tsv`: tracked-file count by distribution area.
- `ccdp-workbench-prompts-inventory.txt`: on-disk workbench/prompt files.
- `ccdp-tracking-status-summary.txt`: tracked, ignored, and on-disk status summary.

## Tracked Reader-Facing Surface

| Area | Count | Distribution disposition |
|------|------:|--------------------------|
| `protocols/ccdp/composite-cognition-dispatch-protocol.md` | 1 | Include as primary assembled spec. |
| `protocols/ccdp/src/` | 22 | Include for source-chapter traceability and rebuild-capable packages. |
| `protocols/ccdp/json/` | 62 | Include as canonical JSON corpus and descriptive extraction evidence. |
| `protocols/ccdp/visual-guide/` | 2 | Candidate include; check HTML asset assumptions during implementation. |
| `protocols/ccdp/templates/` | 1 | Include only if kramdown-rfc assembly ships. |
| `protocols/ccdp/tools/` | 13 | Optional; required for rebuild-capable package, unnecessary for read-only package. |
| `protocols/ccdp/Makefile` | 1 | Optional; only useful if rebuild-capable package ships. |

## On-Disk But Not Package Defaults

| Area | Evidence | Disposition |
|------|----------|-------------|
| `protocols/ccdp/prompts/` | Present on disk, ignored/untracked. | Exclude by default; contains local prompt/provenance material. |
| `protocols/ccdp/workbench/` | Present on disk, ignored/untracked. | Exclude by default; review packets and release-note drafts are provenance material. |
| `protocols/ccdp/tools/ccdp-assembler/target/` | Present on disk as Cargo build output. | Exclude always. |

## Inventory Findings

- The raw on-disk inventory has 301 files at `maxdepth 4`.
- The tracked inventory has 104 files when root `README.md` and root `Makefile`
  are included for context.
- Workbench and prompts have 197 on-disk files and zero tracked files.
- Package design should be based on tracked reader-facing and tool source
  material, with ignored workbench/prompt material handled as explicit
  exclusions.
