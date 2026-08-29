# Later-Arc Backlog

The following findings remain visible after Slice 04. They are not hidden behind
exceptions and should be handled by later package, guide, or release-adoption
work.

| Area | Current evidence | Backlog disposition |
|------|------------------|---------------------|
| Rust CLI guide references | 6 bundled-reference warnings for `09-common-pitfalls.md`. | Decide whether to ship the missing guide, remove the references, or redirect them to shipped Rust CLI material. |
| C++ parameter-passing images | 2 bundled-reference warnings for `param-passing-normal.png` and `param-passing-advanced.png`. | Either package the assets with stable paths or revise the guide prose to avoid absent image links. |
| JavaScript/Deno guide shorthand | 81 bundled-reference warnings for `12-deno/*.md` and `13-biome/*.md` references. | Normalize guide-internal references so package-relative paths resolve from the rendered bundle layout. |
| Repo/provenance references | 146 non-exception `repo-only/provenance` warnings remain, plus 3 narrow explicit exceptions. | Keep provenance and placeholder references visible unless a later arc defines durable source-clone documentation policy. |
| Source-clone references | 26 warnings remain for paths that resolve in source but not in packaged bundles. | Decide case-by-case whether package users need those references or whether source-only references should be reworded. |
| Example project paths | 25 warnings remain. | Keep examples visible and avoid broad exception classes unless later policy distinguishes examples from bundle usability. |
| Parser false positives | 9 warnings remain. | Consider a narrow checker reporting improvement only after higher-value package usability defects are addressed. |

CCDP package targets, URL liveness checks, mature guide directory moves, and broad
guide rewrites remain outside Slice 04.
