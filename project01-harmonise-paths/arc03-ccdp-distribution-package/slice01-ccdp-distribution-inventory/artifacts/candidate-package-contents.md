# Candidate CCDP Package Contents

Recommended package root for Slice 02 design discussion: `ccdp/`.

| Candidate | Current path | Include? | Rationale |
|-----------|--------------|----------|-----------|
| Package entrypoint | New package-local `README.md` or existing assembled spec as root entrypoint | Yes, design in Slice 02 | Consumers need a stable first file that works outside the repo root. |
| Assembled specification | `protocols/ccdp/composite-cognition-dispatch-protocol.md` | Yes | Primary reader-facing protocol artifact. |
| Source chapters | `protocols/ccdp/src/` | Yes | Required for traceability, review, and assembler-based regeneration. |
| JSON corpus | `protocols/ccdp/json/` | Yes | Canonical/extracted JSON evidence base, examples, inventories, and discrepancy register. |
| Visual guide | `protocols/ccdp/visual-guide/index.html`, `protocols/ccdp/visual-guide/ccdp-reference.md` | Yes or separate static-site bundle | Useful reader aid; `index.html` should be checked for asset assumptions during package implementation. |
| RFC template | `protocols/ccdp/templates/draft-rfcxml-general-template-standard-00.xml-edited.md` | Include if kramdown targets ship | Required only if package supports local kramdown-rfc assembly. |
| Assembler source | `protocols/ccdp/tools/ccdp-assembler/` | Optional | Needed for source-package self-assembly; not required for read-only distribution. |
| Root Make target notes | Root `Makefile`, `protocols/ccdp/Makefile` | Package-local docs or generated manifest | Current build targets are source-clone oriented. Slice 02 should define whether package consumers can rebuild. |

Minimum read-only package:

- assembled spec
- source chapters
- JSON corpus
- visual guide/reference
- package-local entrypoint
- manifest/checksum or inventory

Rebuild-capable package adds:

- CCDP-local `Makefile`
- assembler crate source and `Cargo.lock`
- RFC template
- validation instructions
