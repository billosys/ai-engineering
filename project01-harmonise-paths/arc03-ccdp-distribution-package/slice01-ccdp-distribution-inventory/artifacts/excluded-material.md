# Excluded Material

These materials should not be captured automatically by a first-class CCDP
package target unless Slice 02 explicitly changes the package contract.

| Material | Current evidence | Proposed disposition |
|----------|------------------|----------------------|
| Workbench review packets | `ccdp-workbench-prompts-inventory.txt` records 197 on-disk files under `protocols/ccdp/prompts` and `protocols/ccdp/workbench`; `ccdp-workbench-prompts-tracked.txt` records zero tracked files. | Exclude from package. They are source/provenance/review material, not reader-facing distribution content. |
| Local extraction prompt | `protocols/ccdp/prompts/extract-json-corpus-prompt.md` is ignored/untracked and contains local absolute workspace paths. | Exclude. Preserve as provenance outside package or move through a separate approved planning/release slice. |
| Cargo build output | `protocols/ccdp/tools/ccdp-assembler/target/` appears in the raw on-disk inventory and ignored-status summary. | Exclude. Build outputs must not ship from the source tree. |
| Historical review prompts and review notes | `protocols/ccdp/workbench/review-*` appears in raw inventory and ignored status. | Exclude by default. Publish selected release notes separately only through Arc 04/release guidance. |
| Root repository README as-is | Root `README.md` is broad repository documentation with links to `docs/`, `knowledge/`, and skill packaging. | Do not use unchanged as CCDP package entrypoint. Derive a CCDP-local entrypoint instead. |

The exclusion boundary keeps the CCDP package consumer-focused while preserving
source provenance in the repository.
