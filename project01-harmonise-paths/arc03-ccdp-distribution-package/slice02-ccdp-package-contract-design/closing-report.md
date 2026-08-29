---
status: proposed-done
closed: 2026-08-29
implementation_checkout: /Users/oubiwann/lab/billosys/ai-engineering
implementation_state: clean at 4168a57
planning_checkout: /Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning
---

# Slice 02 Close Report: CCDP Package Contract Design

## Summary

Slice 02 produced the design contract for a rebuild-capable CCDP distribution
package. Slice 03 can proceed to implementation using the package identity,
contents manifest, path semantics, generated-output freshness policy, and
validation strategy captured under this slice's `artifacts/` directory.

No implementation files were changed in this slice.

## Package Contract

- Archive: `ccdp.zip`
- Archive root: `ccdp/`
- Entrypoint: generated package-local `ccdp/README.md`
- Package mode: one rebuild-capable package that is also usable read-only
- Root target: `make ccdp-package`
- Validation target: `make check-ccdp-package`
- Validator: `scripts/check-ccdp-package`

The package includes the assembled spec, source chapters, JSON corpus,
visual-guide files, RFC XML template, assembler source/Cargo metadata,
package-local `Makefile`, and package-local `README.md`.

The package excludes workbench material, prompts, Cargo build output, the root
repository README as-is, and the root repository Makefile.

## Generated-Output Freshness

Slice 03 must compare a temporary regenerated assembly output against
`protocols/ccdp/composite-cognition-dispatch-protocol.md` before building the
package. If the comparison shows drift, Slice 03 should refresh the committed
assembled spec as a named pre-package step, rerun the comparison, then build the
package only from the fresh committed state.

The temporary assembly command ran successfully during this slice:

`make -C protocols/ccdp ccdp-rfc OUTPUT=/private/tmp/ccdp-slice02-assembled.md`

The command output is captured in `artifacts/ccdp-temp-assembly-check.txt`.

## Artifacts

- `artifacts/artifact-inventory.txt`
- `artifacts/ccdp-package-contract-design.md`
- `artifacts/ccdp-temp-assembly-check.txt`
- `artifacts/generated-output-freshness-decision.md`
- `artifacts/git-diff-check-implementation.txt`
- `artifacts/git-diff-check-planning.txt`
- `artifacts/git-status-implementation.txt`
- `artifacts/package-contents-manifest-draft.md`
- `artifacts/package-decision-matrix.md`
- `artifacts/package-path-semantics.md`
- `artifacts/README.md`
- `artifacts/slice03-implementation-inputs.md`
- `artifacts/validation-checker-strategy.md`

## Ledger Walk

- F-1: done. `artifacts/ccdp-package-contract-design.md` derives the design
  from Slice 01 CDC verification, inventory, risk map, candidate contents,
  exclusions, and design inputs.
- F-2: done. `artifacts/package-decision-matrix.md` and the design report name
  `ccdp.zip`, `ccdp/`, generated `ccdp/README.md`, and one rebuild-capable
  package mode.
- F-3: done. `artifacts/package-contents-manifest-draft.md` lists included
  reader-facing and rebuild material and excluded non-package material.
- F-4: done. `artifacts/package-path-semantics.md` specifies package-local link
  semantics, generated README behavior, `../tools/` handling, `src/...`
  references, and protocol-syntax filters.
- F-5: done. `artifacts/generated-output-freshness-decision.md` records the
  Slice 03 pre-package freshness requirement and repair policy.
- F-6: done. `artifacts/validation-checker-strategy.md` specifies
  `scripts/check-ccdp-package`, zip/unzip checks, package-local Markdown link
  checks, protocol syntax filters, and extracted assembly validation.
- F-7: done. `artifacts/slice03-implementation-inputs.md` provides concrete
  implementation steps and proposed ledger anchors.
- F-8: done. `artifacts/git-diff-check-implementation.txt` and
  `artifacts/git-status-implementation.txt` show the implementation checkout is
  clean and design-only.
- F-9: done. `artifacts/artifact-inventory.txt` inventories durable evidence
  under this slice's `artifacts/` directory.
- F-10: done. This report names the implementation state, inventories artifacts,
  walks every row, and bubbles the Slice 03 contract forward.

## Bubble-up to Arc 03

Slice 02 is proposed-done pending CDC verification. Arc 03 now has a package
contract ready for Slice 03 implementation.

Slice 03 can proceed without a separate repair slice. It must treat generated
assembled-spec freshness as an implementation precondition and ledger anchor:
compare temporary assembly output against the committed assembled spec, repair
committed generated output if needed, then build and validate `ccdp.zip`.
