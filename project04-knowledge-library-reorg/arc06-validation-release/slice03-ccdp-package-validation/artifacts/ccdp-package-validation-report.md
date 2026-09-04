# CCDP package validation report

## Commands

Package build:

```sh
make ccdp-package
```

Validation:

```sh
make check-ccdp-package
```

## Validation Result

Result: pass.

`make ccdp-package` passed after the assembled protocol refresh. It generated
`ccdp.zip` with root `ccdp/` and 122 entries.

`make check-ccdp-package` passed. Validator summary:

```text
ccdp package check
zip: ccdp.zip
markdown files scanned: 42
package references checked: 14
protocol syntax skipped: 91
external URLs skipped: 4
shape errors: 0
README errors: 0
Markdown path failures: 0
```

Extracted package validation also passed:

```text
cd tools/ccdp-assembler && cargo build --release
Finished `release` profile [optimized] target(s) in 9.36s
tools/ccdp-assembler/target/release/ccdp-assembler --validate --src-dir src --output /private/tmp/ccdp-package-assembled.md --version 0.2
```

## Remaining Failures / Accepted Disposition

No remaining CCDP package validation fail result was observed.

No accepted disposition or waiver was required because both `make ccdp-package`
and `make check-ccdp-package` are now green.
