# Changed Guidance Reference Disposition

Source inspected:

- `README.md`
- `protocols/ccdp/README.md`

Search artifact:

- `artifacts/changed-guidance-search.txt`

## Disposition

- `protocols/ccdp` appears only in source-checkout guidance in the root README
  and in the protocol README's explanation that the same directory becomes the
  package root when staged.
- `ccdp.zip` appears as the standalone CCDP protocol package. It is explicitly
  distinguished from installable skill zips.
- `ccdp/README.md` appears as the unzipped package entrypoint.
- `workbench` and `prompts` appear only in source-only/excluded-material
  guidance. The changed docs say those directories are intentionally excluded
  from `ccdp.zip` and are not package entrypoints.
- `target` appears in ordinary README prose about Make targets and a
  pre-existing sentence about coverage targets, not as a reference to Cargo
  target output or packaged content.
- `/Users/` does not appear in the changed guidance.
- `/private/tmp` does not appear in the changed guidance.

No changed reader guidance points package users at unlabeled source-only
material or local absolute paths.
