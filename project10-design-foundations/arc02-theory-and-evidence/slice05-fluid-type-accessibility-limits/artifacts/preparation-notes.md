# Slice05 author preparation — 2026-10-12

CDC Sofie prepared this ordinary T-family assignment after Slice04 independent
close b6acb22f and completed Project13 comparison `dc7b0732fa8a78cf47713aecdaabbc5ef05686b6`. Experiment01 ended
at two registered slices; Slice05 is not T03 or an extension/adoption of that
pilot. Existing framework authoring, independent review and all parent gates apply.
This is an author demonstration, not accepted CC work or browser certification.

## Complete selected contexts and boundaries

SOURCE `dffa504e851b03b8e4746f1941068e4cc850b612`; planning predecessor `dc7b0732fa8a78cf47713aecdaabbc5ef05686b6`.
Seven complete windows/98 lines/five files below are navigation and coverage,
not a known assertion count. Read all lines/qualifiers, including wrapped clauses,
table cells and code. Use exact source-qualified identities and full spans/offsets.

| Window | SOURCE path | Inclusive lines | Lines | Whole-file SHA-256 |
|---|---|---|---:|---|
| W01 | `knowledge/design/SKILL.md` | 63–75 | 13 | `57833e7cecd5984bf1cd6c7b26def1194f7cbbdf83e24a4960bd739a6f26ff63` |
| W02 | `knowledge/design/SKILL.md` | 183–204 | 22 | `57833e7cecd5984bf1cd6c7b26def1194f7cbbdf83e24a4960bd739a6f26ff63` |
| W03 | `knowledge/design/guides/layout.md` | 112–122 | 11 | `361ea7887a69870db6db7aa362455b00b5cf718d6c4ae0d49405785fd5c82aec` |
| W04 | `knowledge/design/guides/layout.md` | 934–946 | 13 | `361ea7887a69870db6db7aa362455b00b5cf718d6c4ae0d49405785fd5c82aec` |
| W05 | `knowledge/design/guides/breaking-the-layout-monoculture.md` | 195–220 | 26 | `76d209306a8ade1da51f62ad86fb7f01f103f0f4d033e7235c3b4b023397b845` |
| W06 | `knowledge/design/guides/design.md` | 148–153 | 6 | `e4953fd1452102c98df6f0fcf33bc17bd3732f011180475daa8fd256e70e687b` |
| W07 | `knowledge/design/guides/type.md` | 472–478 | 7 | `8a9f1ab35dee3373ebbf1460416e334adffcd908f095463fa015c6ef0a5f5d7c` |

Assigned scope: viewport versus font-relative unit definitions, logical-axis
selection, root preference claims, mixed rem/vi clamp behavior and text-enlargement/
WCAG guarantees in these windows. W05's blanket “no jarring layout shifts” and
“accessible” table label need scoped reasoning, not a CSS-unit certificate.
Substantive boundaries remain explicitly owned: W01 other principles/OKLCH,
W02 ratios/generation, W03 ch/px/em descriptions outside root/resize implications,
W04 asymptotic/proportional claims, W05 spacing/harmony/other stack layers,
W07 geometric/perceptual/Bringhurst assertions belong to remaining T/full L,
with accepted Slice01/03/04 evidence retained only for exact previously checked
claims. Each boundary gets its full literal, reason, owner and any exact accepted
pointer; markup has its separate classification. Do not relabel claims as markup.
Full233/eight/16 and R/T/C/L/G remain; no full-file/card review inferred.

## Primary evidence actually inspected and applicability

Access2026-10-12 using read-only web retrieval. CSS Values4 is the published
12 March2024 Working Draft; WCAG2.2 is the12 December2024 Recommendation.
These are technical reading inputs, not immutable local capture/fidelity evidence.

| ID | Primary source and bounded read | Use / limit |
|---|---|---|
| CV | [CSS Values4](https://www.w3.org/TR/2024/WD-css-values-4-20240312/) §6.1.1 rem definition/resolution and user-minimum-font notes; §6.1.2 intro and §6.1.2.2 full unit definitions; §10.2 complete comparison-function section | rem follows computed root metrics; viewport units follow specified viewport/axis. Clamp clips the central value. Definitions do not establish accessibility. No browser-support claim. |
| WC | [WCAG2.2](https://www.w3.org/TR/2024/REC-WCAG22-20241212/) SC1.4.4 complete and SC1.4.10 complete including both notes | Separate AA enlargement and reflow obligations; exceptions and dimensions retained. |
| RT | [Resize Text Understanding](https://www.w3.org/WAI/WCAG22/Understanding/resize-text.html) SC and Intent through all three notes | Informative interpretation: at least one supported enlargement mechanism, intermediate steps/no loss. Do not turn every mechanism into normative AND requirement. |
| RF | [Reflow Understanding](https://www.w3.org/WAI/WCAG22/Understanding/reflow.html) SC/notes, Intent and Basic text reflow | Informative, distinguishes dimensions and exceptions; narrow screenshots do not prove enlargement. |
| F94 | [F94](https://www.w3.org/WAI/WCAG22/Techniques/failures/F94), complete technique body/notes/tests; displayed updated9 March2026 | Viewport-unit failure example has alternatives/qualifications; does not prove every mixed clamp fails or forbid all viewport units. |
| UT | [Utopia calculator](https://utopia.fyi/type/calculator/), complete returned66-line text including generated CSS | Returned default uses vw, differing from local attribution of vi. Record exact observed configuration; no universal claim about all settings/history. Dynamic UI not tested. |

The CV header/status and definitions, normative WC clauses and above informative
sections were received before authoring. Retrieve/reinspect their complete assigned
sections before new judgments; record changed versions/access failures. Missing
historic source captures/lineage/P10-11 leave dependent source-faithfulness unassessed.
No Utopia-history or author-attribution fidelity conclusion is prefilled.

## Four difficult cases and construction example

1. **Logical axis:**800×600 CSS-pixel viewport. For horizontal writing, vi/vw
both use width; vertical inline selection can follow height. A writing-mode
choice is separate from enlargement behavior; preserve specified viewport variants.
2. **Root preference:**rem follows computed root size, not necessarily a user
preference. Author root overrides/minimum-font behavior and text-only enlargement
must not be conflated with deliberately changing computed R in a math model.
3. **Mixed clamp:**toy `clamp(1rem, .5rem + 2vi, 2rem)` is24px at R16/I800.
Under an explicitly assumed page-zoom model with CSS inline extent halved and
R fixed, twice16px is32 apparent units, ratio4/3 rather than2. Changing R to32
with I800 separately yields32px. Pure2vi can cancel that assumed page zoom.
This disproves an inference from unit choice under stated assumptions; it is
not an observed browser failure or proof all fluid type fails WCAG.
4. **Two originals and output:**layout937–940 and breaking202–204 both assert
an accessibility guarantee. They agree in their unsupported inference; they
are not in conflict merely because the replacement will qualify both. Read the
full originals; keep current evidence distinct from historic fidelity.

Author example below targets the entire layout vi/zoom/SC sentence, leaving its
neighboring modular-scale claim intact. Five-dimensional proposal for this
example: source-faithfulness not assessed (missing historical capture/lineage);
correctness not established as stated (unit definition and model cannot imply
conformance); scope/attribution overstates a unit-selection recommendation;
consistency agrees with the other original guarantee at breaking202–204, with
both lacking sufficient conformance evidence; relationship/CQ not assessed (no
card/graph assignment). Evidence IDs CV/WC/RT/F94 support those separate reasons.
The literal replacement preserves logical units and directs actual verification.
Arc04 owns application; Arc03 owns real enlargement/reflow proof. This is a
bounded proposed example subject to CC challenge; don't copy verdicts blindly.

## Exercised source-to-final-edit demonstration

Run read-only Python. It binds complete original→exact source target→qualified
replacement→whole-file composition, independently hand-computed model witnesses
and four invalid records through the same predicate. Structural exactness/type
limits are mechanical; applicability/meaning remain human judgments.

```python
import copy,hashlib,subprocess
from fractions import Fraction as F
REV='dffa504e851b03b8e4746f1941068e4cc850b612'
PATH='knowledge/design/guides/layout.md'
def git(p): return subprocess.check_output(['git','-C','/Users/oubiwann/lab/billosys/ai-engineering','show',REV+':'+p])
data=git(PATH);lines=data.decode().splitlines();span='\n'.join(lines[936:940])
original='The `vi` unit (viewport inline) is\nused instead of `vw` because it respects writing direction and,\ncritically, does not prevent browser zoom from scaling\ntext\u2009---\u2009satisfying WCAG SC 1.4.4.'
assert original in span
replacement=('Use `vi` when viewport-relative sizing should follow the inline axis. '
             'In horizontal writing it follows the same axis as `vw`; neither unit alone '
             'establishes text-resize conformance. Preserve user preferences and verify '
             'actual enlargement without loss of content or functionality, separately from reflow.')
start=data.index(original.encode());end=start+len(original.encode())
record={'source_revision':REV,'source_sha256':hashlib.sha256(data).hexdigest(),
        'path':PATH,'span':[937,940],'original':original,'file_byte_offsets':[start,end],
        'replacement':replacement,'owner':'Arc04 application; Arc03 browser proof',
        'proof_kind':'model','actual_browser_checked':False,'conformance_established':False}
def validate(r):
 assert r['source_revision']==REV and r['path']==PATH and r['source_sha256']==hashlib.sha256(data).hexdigest()
 lo,hi=r['span'];assert 1<=lo<=hi<=len(lines)
 x,y=r['file_byte_offsets'];assert 0<=x<=y<=len(data)
 assert r['original']==original and data[x:y].decode()==original
 assert original in '\n'.join(lines[lo-1:hi])
 assert r['proof_kind']=='model' and not r['actual_browser_checked'] and not r['conformance_established']
 assert r['replacement']==replacement and r['owner']
 out=data[:x]+r['replacement'].encode()+data[y:]
 assert b'The modular scale itself' in out and out.endswith(b'\n')
 return out
out=validate(record)
def clamp(r,i):return max(r,min(F(1,2)*r+F(2)*i/100,F(2)*r))
assert clamp(F(16),F(800))==24
assert 2*clamp(F(16),F(400))==32 # apparent 4/3, not twice24
assert clamp(F(32),F(800))==32   # root change, separate model
assert 2*(F(2)*400/100)==F(2)*800/100==16 # pure viewport cancellation
assert clamp(F(16),F(100))==16 and clamp(F(16),F(2000))==32
bad=[]
for name,mutate in [
 ('clipped WCAG qualifier',lambda r:r.update(original=r['original'].split('text')[0])),
 ('wrong source target',lambda r:r.update(file_byte_offsets=[0,end])),
 ('model promoted to browser proof',lambda r:r.update(actual_browser_checked=True)),
 ('model promoted to conformance',lambda r:r.update(conformance_established=True))]:
 r=copy.deepcopy(record);mutate(r)
 try:validate(r)
 except (AssertionError,ValueError):bad.append(name)
 else:raise AssertionError(('false pass',name))
print({'positive':1,'rejected':bad,'toy_base':24,'toy_zoom_2_apparent':32,'toy_root32':32,
       'pure_vi_apparent':16,'composed_bytes':len(out),'original':original,'replacement':replacement})
```

Author result: positive1/four negatives rejected;24→32 apparent under the stated
zoom model, root32 witness32, pure-viewport16, lower/upper clamps16/32. The
full composed paragraph keeps its next sentence and source EOF. No browser,
AT, source mutation, package or install run. The ordinary framework authoring
readiness check is met: inspected pinned inputs; defined boundaries/owners;
primary guidance applied; executable evidence recipe and discriminating witnesses;
coherent allowlist/ledger/gates with semantic conclusions open to contrary evidence.

## Authoring scope and recovery receipt

Before issue CDC read SOURCE domain entrypoint, all7/98 windows, complete primary
sections declared above, existing semantic procedure83 lines and Slice01
configuration Inputs/method and Published baseline CSS plus Clamp behavior proof.
Selected parent current bodies/criterion tables and current histories govern;
older histories remain reference-only. A guessed Slice01 numerical-reconciliation
path failed; actual configuration-reconciliation path was located with rg --files,
read and fixed in the manifest before issuance. Truncated combined reads were
recovered with complete governing section chunks. These are authoring recoveries,
not CC evidence or claims of full historical-file exposure.

The final author replay accepted the construction and rejected all four invalid
records. Opening-file checks resolved 130 local links and 45 fragments, with
LF/final newlines preserved. The unversioned `python` command was unavailable;
the same example was successfully rerun with `python3`. This is an author-side
command recovery, not an unresolved verification failure.
