# Audit Artifact Relocation

Established 2026-10-08 at the Operator's request. Shared destination:
`project09-design-audit/artifacts/` on branch `planning`.

The three reports originated in the implementation checkout's ignored
`workbench/`; they were not previously tracked. Their original audit date and
source baseline remain in their bodies. Filename dates are removed as requested.
This commit records their admission to planning; it does not backdate the audit
or claim a pre-existing Git history for the ignored originals.

## Original-to-current mapping

All original paths below are relative to the source checkout's `workbench/`.
All current names are relative to this directory. Hashes are SHA-256 of UTF-8
file bytes, including their final newlines.

| Original name | Current name | Original SHA-256 | Current SHA-256 |
|---|---|---|---|
| `2026.10.08-audit-results-design.md` | [audit-results-design.md](audit-results-design.md) | `9534821a8911d56e2cf402e47616cf6b55898af73945bf4dd15cd9de835d80a7` | `4b2417ec2dd70690d360709a81d9bc2f13a64b4520cb36bf2063e25f2eb4d93e` |
| `2026.10.08-audit-modernization-synthesis.md` | [audit-modernization-synthesis.md](audit-modernization-synthesis.md) | `8fd3f5f7e12f7f9770ffa61ab886edf4be52ba88f827d142c15b798b71427528` | `314035750f94e36d9d572cfb06f70bc6de20199a78f8872691bc965b38854bde` |
| `2026.10.08-audit-index.md` | [audit-index.md](audit-index.md) | `35662e9e803559a270afca634231567821d448c6b7fe13c6ede0f62dac6ccda6` | `bdc8e885e11a8ea77f7512b07d61bea15fd936f9c3aec1bbad0f03196fe46127` |

## Administrative changes

- All three reports: update local links to the undated filenames.
- Findings: qualify the original no-mutation statement as referring to the audit
  itself and link this relocation record. All DES findings remain unchanged.
- Synthesis: replace the former tentative Project09/Project10 mapping with
  Project09 audit ownership, Project10 foundation repair and Project11 unified
  practice; link the two release plans; retire the already-resolved identity
  decision while retaining substantive scope/version decisions.
- Index: update the release numbering and replace the obsolete workbench-location
  paragraph with the current shared home and project links.

No substantive finding, numerical result, source reference, recommendation or
verification limit was changed. No skill source or concept-card file was edited.
Original files were removed from `workbench/` only after verifying the relocated
bytes against the explicit administrative transformations. Independent substantive
acceptance of the audit remains open in the project ledger.

## Bootstrap self-check

The relocation script compared the written bytes to the exact transformed inputs
before removing the originals. A separate check of the saved originals and
transformations verified hashes, preserved finding bodies and report counts.
All relative Markdown links in the new project files resolve; dependency metadata
and DES-001–016 coverage were checked. These are author self-checks of the move
and project bootstrap, not independent verification of the audit's conclusions.
