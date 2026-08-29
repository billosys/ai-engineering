# Slice 02 Design Inputs

## Recommended Contract Decisions

- Choose archive name: likely `ccdp.zip` or `ccdp-distribution.zip`; do not
  reuse skill-bundle naming semantics because CCDP is not a skill.
- Choose root directory: `ccdp/` is the simplest package root and avoids
  leaking `protocols/ccdp/` into packaged paths.
- Choose entrypoint: a package-local `README.md` that links to the assembled
  spec, JSON corpus, source chapters, and visual guide; or make the assembled
  spec the primary entrypoint and include a short package manifest.
- Decide read-only versus rebuild-capable package. A read-only package can
  exclude the assembler crate; a rebuild-capable package must include tools,
  template, Cargo metadata, and a package-local validation command.
- Define path semantics: all package-local links should resolve from `ccdp/`
  or from each document location after unzip.
- Define transforms: `src/README.md` needs treatment for `../tools/` if tools
  are excluded; root README should not ship unchanged.
- Define validation: extend package-path checking to CCDP only after the
  package shape is selected; account for JSON Pointer and protocol slash paths
  so they are not false filesystem failures.
- Decide generated-output freshness policy: `make ccdp` currently succeeds but
  rewrites the tracked assembled spec. Package implementation should either
  regenerate and commit the assembled spec in a dedicated repair step or define
  packaging from a clean committed generated state.

## Questions for Slice 02

1. Should the first package be read-only, rebuild-capable, or both as separate
   targets?
2. Should the visual guide ship in the same archive as the spec and JSON corpus,
   or as a separate static-site artifact?
3. Should the assembler source ship for transparency, or should the package
   remain documentation-only until a release workflow exists?
4. Is generated assembled-spec drift a blocker for package implementation or a
   pre-package repair row?
5. Which checker policy should own CCDP path validation: reuse
   `check-package-paths`, add CCDP-specific mode, or create a separate package
   manifest validator?
