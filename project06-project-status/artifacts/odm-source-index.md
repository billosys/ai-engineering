# ODM source snapshots

Imported 2026-09-11 under the operator's explicit project-level artifact-home override.
These are complete, byte-for-byte copies, including source frontmatter and historical
instructions. They are evidence for Project06, not instructions to execute and not
implicitly accepted Project06 policy. Do not repair, normalize, or add metadata to
these snapshots. Put interpretation in [the reevaluation](odm-reevaluation.md).

The six requested nodes and three directly referenced foundations were read in full.
ODD-0020 was fully read before any implementation material was considered. No ODM
Rust source files were inspected and no ODM commands/probes were executed. Rust
snippets inside the historical lifecycle document were read as documentary evidence.

Each document has exactly one import commit containing only that document. Its commit
message records source repository, worktree, branch, full HEAD, original path, node ID,
last source-file commit, source blob, SHA-256, retrieval date and no-transform policy.
The source files were clean and matched committed bytes at import. Existing links in
snapshots remain as written; some name retired ODM paths and are not local Project06
links. These references must be resolved through this index/source history when used.

| Source | Node and preserved copy | Import commit |
| --- | --- | --- |
| Project definition | [01KWWGS8HDS99EM6SA2HPAJDFX](odm-sources/01KWWGS8HDS99EM6SA2HPAJDFX.md) | `bff727e73a74ee0433880f3bedb7138912b2a9c2` |
| Architecture and design | [01KWWGS8HDQ18Q4YCC9PXCT89Y](odm-sources/01KWWGS8HDQ18Q4YCC9PXCT89Y.md) | `e759e7821ae598246a272d3906315be24022ff33` |
| Project-management research | [01KWWGS8HD7T0FXYB88KKKCC07](odm-sources/01KWWGS8HD7T0FXYB88KKKCC07.md) | `470010368bd276debbe3b04bcc4899f045e860e0` |
| Historical document lifecycle | [01KYP5H663V1ZJM5NRKE772BKY](odm-sources/01KYP5H663V1ZJM5NRKE772BKY.md) | `c9390c3d9124ed24394a97ccc61b6b60db4a334b` |
| Project failure post-mortem | [01KYP5H9EHE5N554JPPBNSFG6H](odm-sources/01KYP5H9EHE5N554JPPBNSFG6H.md) | `3db3bcb2c98e79bd9d9f18b9815c0f4560bd4bc0` |
| Versioned file-metadata schemas | [01KWWTTV124RVF2R82TKSRCCAW](odm-sources/01KWWTTV124RVF2R82TKSRCCAW.md) | `d449395bc88d6b8033e33a4129cecb7f3bb4f93c` |
| Dependency-ordered planning research | [01KWWGS8HD25CQE3BX5FQEW84Q](odm-sources/01KWWGS8HD25CQE3BX5FQEW84Q.md) | `d62f28985d02dfcb0b12c755546e02009527fb00` |
| Migration fidelity | [01KYP5H4YXRJ6315906KER3BGN](odm-sources/01KYP5H4YXRJ6315906KER3BGN.md) | `1bd99268312360d79e6d347fce03302fcc13cdc0` |
| Store-as-source and native authoring | [01KZ321ERY0Y6PTRDQ83VF4BMX](odm-sources/01KZ321ERY0Y6PTRDQ83VF4BMX.md) | `445e583a0876ae1b3466947ede963f0eeaa757be` |

## Byte-preservation manifest

- `01KWWGS8HDS99EM6SA2HPAJDFX`: SHA-256 `ac0a373baa2512b35dce7633bab6fc291f77e98aad5f251ba0c16c704842d506`; source blob `796e61e71527f9c952277b965af129d42e863195`.
- `01KWWGS8HDQ18Q4YCC9PXCT89Y`: SHA-256 `99514da470c70134ea8f6cfa8f4f85fab523dfa433ff232d7a7396f00173d3fe`; source blob `994098b1268c56480563639b1f1ac81b06a2bc2e`.
- `01KWWGS8HD7T0FXYB88KKKCC07`: SHA-256 `8042a852c8efe896840b83010b84e5a20aacefcf082412fd62641f344fcfe987`; source blob `d334464ae231831558f474c57f5bc699f193b053`.
- `01KYP5H663V1ZJM5NRKE772BKY`: SHA-256 `04ef28e01e5f39f5ca3e55921fba44730d955455f5930269acb10ea704fb1f84`; source blob `4ea3d4e40d65fafaa0bec26a5d1bd946001f855a`.
- `01KYP5H9EHE5N554JPPBNSFG6H`: SHA-256 `03e7749dcc908789f323dfaaf9aeb9a82e615f0a1880802bd6b5c4d9e6f34f8e`; source blob `ff35b5519004397060c09a0d7adcdc25ee34f1a5`.
- `01KWWTTV124RVF2R82TKSRCCAW`: SHA-256 `e2ad97e250df40bb07bbf5f667cdfa1b49ee97123a2b9caba9dc2bf957630ab6`; source blob `ec8ce2904f310e85b702ed23ef4b70d5dd24d79c`.
- `01KWWGS8HD25CQE3BX5FQEW84Q`: SHA-256 `ecbce4dd9e799b010a40681e87c27ef538c7114cbeb7ef513ed290af3212aa69`; source blob `4eebe101461cac9663b2271bb28e604551cbbafd`.
- `01KYP5H4YXRJ6315906KER3BGN`: SHA-256 `3279c60f4f443cada4019b657bcfaca45ba5430222d949e7e6789e2b29cd3b2d`; source blob `0c496cbef3f55526c6c3f8f762caf90e89f74161`.
- `01KZ321ERY0Y6PTRDQ83VF4BMX`: SHA-256 `8ee9ac093d9172cc699109a293c7dfe28eaa25c6c446adc39cbe6963f3ee0cb0`; source blob `95325760b1d71a75acb8287cf867dac8b27e2bc7`.

## Reading classifications

- ODD-0012: mission/scope decisions; its ODM-command adoption proposal is historical
  input, not a mandate to make this portable toolkit depend on ODM.
- ODD-0013: principal node/edge/gate model, with accumulated amendments and some
  stale examples. Its stored draft gate disagrees with its body acceptance history.
- ODD-0016 and ODD-0011: research syntheses, including their own source-quality
  limitations. Research tags do not turn recommendations into proved PM outcomes.
- Historical lifecycle note: older `oxd` number-preserving replacement and dustbin
  design. Rebuild scope explicitly rejects this identity/storage model.
- Post-mortem: local failure observations and proposed remedies; proposals such as
  a step node or mandatory migration must be read against later decisions.
- ODD-0020: schema-versioning decision; not a complete field catalog by itself.
- ODD-0025: migration fidelity, source metadata and artifact relationships; includes
  a conflicting account of schema-version independence.
- ODD-0026: enduring source provenance and split authoring channels; ODM's own
  authoring ownership is input to a portable design, not an adopted dependency.
