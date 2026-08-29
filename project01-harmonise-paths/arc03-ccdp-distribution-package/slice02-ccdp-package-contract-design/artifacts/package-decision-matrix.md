# CCDP Package Decision Matrix

| Decision | Selected Contract | Alternatives Rejected | Evidence Basis |
|----------|-------------------|-----------------------|----------------|
| Archive name | `ccdp.zip` | `ccdp-distribution.zip`, skill-name-derived archive names | CCDP is a protocol package, not an installable assistant skill. A short archive name matches the protocol identity. |
| Archive root | `ccdp/` | `protocols/ccdp/`, top-level files with no root directory | Slice 01 recommended `ccdp/`; it avoids leaking repository layout and prevents archive tarbomb behavior. |
| Entrypoint | Generated package-local `ccdp/README.md` | Root repository `README.md` unchanged; assembled spec only | Slice 01 found root README links into repo-wide `docs/`, `knowledge/`, and `templates/`. A package-local README can point to CCDP materials only. |
| Package mode | One rebuild-capable package | Read-only only; separate read-only and rebuild targets in Slice 03 | Rebuild-capable includes a read-only consumer path while preserving `src/README.md`'s `../tools/` relationship and assembler transparency. |
| Visual guide | Include `visual-guide/` in `ccdp.zip` | Separate visual-guide package | Current visual guide has only two files and is reader-facing. Keeping it with the spec reduces package discovery work. |
| Assembler tooling | Include `tools/ccdp-assembler/` source and `Cargo.lock`; exclude `target/` | Exclude tools; ship build output | Tool source is required for rebuild-capable package. Cargo build output is ignored/generated and must not ship. |
| RFC template | Include `templates/draft-rfcxml-general-template-standard-00.xml-edited.md` | Exclude templates | The kramdown-rfc Make targets require the template. Including it keeps CCDP-local Make targets coherent. |
| Workbench/prompts | Exclude by default | Include current on-disk material | Slice 01 verified zero tracked files under workbench/prompts and local absolute paths in prompt material. |
| Freshness policy | Slice 03 must refresh or reconcile generated assembled spec before packaging | Package whatever committed composite currently contains | Slice 01 and CDC both observed assembly drift when regenerating the assembled spec. |
| Validator | Add CCDP-specific package validation | Reuse skill-bundle checker unchanged | Existing checker semantics are tuned for `SKILL.md + guides/`; CCDP has JSON pointers, protocol slash paths, and source/tool/package content. |
