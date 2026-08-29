# Generated Output Freshness Decision

Decision: Slice 03 must reconcile generated assembled-spec output before
building `ccdp.zip`.

## Evidence

Slice 01 captured `ccdp-assembly-generated-drift.patch`. CDC reproduced the
assembly path with:

```sh
make -C protocols/ccdp ccdp-rfc OUTPUT=/private/tmp/cdc-arc03-slice01-ccdp-assembled.md
```

Slice 02 also ran:

```sh
make -C protocols/ccdp ccdp-rfc OUTPUT=/private/tmp/ccdp-slice02-assembled.md
```

The Slice 02 command exited 0 and wrote a temporary assembled file without
dirtying the implementation checkout.

## Contract

- The package target must not silently package stale generated output.
- Slice 03 must start with a freshness check that regenerates the assembled
  spec to a temporary output path and compares it with
  `protocols/ccdp/composite-cognition-dispatch-protocol.md`.
- If the diff is non-empty, Slice 03 may update the committed assembled spec as
  a named pre-package step in the implementation slice, then rerun the
  freshness check to clean.
- Packaging may proceed only after the temporary regenerated output and the
  committed assembled spec match.
- The package target itself should stage from the committed fresh assembled
  spec, not regenerate in a way that leaves source files dirty.

No separate repair slice is required before Slice 03, but the Slice 03 ledger
must include the freshness check/update as an explicit row.
