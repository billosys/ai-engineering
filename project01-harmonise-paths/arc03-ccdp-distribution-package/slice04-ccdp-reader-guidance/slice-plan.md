# Slice 04: CCDP Reader Guidance

```yaml
project: project01-harmonise-paths
arc: arc03-ccdp-distribution-package
slice: slice04-ccdp-reader-guidance
status: open
opened-on: 2026-08-29
artifact-home: artifacts/
depends-on:
  - slice01-ccdp-distribution-inventory
  - slice02-ccdp-package-contract-design
  - slice03-ccdp-package-implementation
implementation-checkout: /Users/oubiwann/lab/billosys/ai-engineering
planning-worktree: /Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning
```

## Capability

Teach humans and LLMs how to consume CCDP from either the source clone or the
generated package without rediscovering file locations.

This is the reader-facing guidance complement to Slice 03's package mechanics.

## Inputs

- `../slice03-ccdp-package-implementation/cdc-verification.md`
- `../slice03-ccdp-package-implementation/closing-report.md`
- `../slice02-ccdp-package-contract-design/cdc-verification.md`
- `../slice02-ccdp-package-contract-design/artifacts/package-path-semantics.md`
- implementation checkout `README.md`
- implementation checkout `Makefile`
- implementation checkout `scripts/check-ccdp-package`
- implementation checkout `protocols/ccdp/`
- implementation checkout generated `ccdp.zip`

## Scope

Update reader guidance in the source checkout so:

- the root README distinguishes skill zips from the CCDP protocol package;
- the root README names `make ccdp-package` and `make check-ccdp-package`;
- source-clone CCDP entrypoints are explicit;
- package/unzipped CCDP entrypoints are explicit;
- the generated package README is clear, package-local, and kept aligned with
  source guidance;
- references point to files that exist in the relevant context.

Strongly consider adding `protocols/ccdp/README.md` as a protocol-root
entrypoint whose relative links work both in the source tree and when staged as
`ccdp/README.md`. If that is the cleanest shape, update package staging to copy
that file rather than embedding README prose in the root Makefile.

## Out of Scope

- CCDP runtime behavior.
- Protocol semantic rewrites.
- URL liveness checks.
- Release publication mechanics.
- Arc 04 release/adoption hardening.
- Broad mature language skill warning burn-down.
- Including workbench/prompts in the package.

## Verification Approach

Run from `/Users/oubiwann/lab/billosys/ai-engineering`:

```sh
make ccdp-package
make check-ccdp-package
unzip -p ccdp.zip ccdp/README.md
make check-package-paths
make all
make ccdp
git diff --check
git status --short --untracked-files=all
```

Also inspect changed README/protocol guidance for:

- source-clone paths that resolve from the repository root or protocol root;
- package paths that resolve from the unzipped `ccdp/` root;
- clear distinction between skill bundles and the CCDP protocol package;
- no unlabelled references to excluded workbench/prompts material.

Run from the planning worktree:

```sh
git diff --check
find project01-harmonise-paths/arc03-ccdp-distribution-package/slice04-ccdp-reader-guidance/artifacts -maxdepth 2 -type f -print
test -f project01-harmonise-paths/arc03-ccdp-distribution-package/slice04-ccdp-reader-guidance/closing-report.md
rg -n "F-1|F-2|F-3|F-4|F-5|F-6|F-7|F-8|F-9|F-10|Artifacts|Bubble-up to Arc 03" project01-harmonise-paths/arc03-ccdp-distribution-package/slice04-ccdp-reader-guidance/closing-report.md
```

## Exit Criteria

- Source-clone CCDP usage is documented with correct paths.
- Package/unzipped CCDP usage is documented with correct paths.
- CCDP build/check targets are documented without changing skill-bundle
  semantics.
- The package README is package-local and passes the CCDP validator.
- Existing package checks still pass.
- Slice-produced durable evidence lives under this slice's `artifacts/`
  directory.
- The close report walks every ledger row and bubbles findings up to Arc 03,
  including whether Arc 03 can close or needs a remediation slice.
