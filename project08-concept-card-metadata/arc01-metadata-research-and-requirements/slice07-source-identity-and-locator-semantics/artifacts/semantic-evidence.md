# Slice07 Semantic Evidence

## Registered inputs and inspected contexts

The registry names every input below with exact path, SHA-256, inspected section
and role. frozenInventory is the typed frozen census; legacy is the populated
Complete Musician card; and erlangSample is a populated non-book OTP card. The
latter records source OTP Design Principles, source_slug otp-design-principles,
authors Ericsson AB, chapter Overview, chapter_number null, pdf_page null, and
section Behaviours in PROVENANCE. It demonstrates an actual null context without
treating either null as inapplicability.

The literal census recorded in validation-evidence.md covers all seven legacy
fields. It finds 390 music cards and 1,664 Erlang cards. Both families have
string authors, chapter, source_slug, and source; music has numeric
chapter_number and pdf_page throughout, while Erlang has 1,108/556 number/null
chapter_number and 224/1,440 number/null pdf_page. section is string/null in
342/48 music and 1,651/13 Erlang cards. These are observed stored shapes, not
a cross-source normalization rule.

legacy records Complete Musician title, slug, author text, chapter title and
ordinal, section, and pdf_page 33; its cited body pages differ, so the
frontmatter field alone does not disclose a page basis. This supports retaining
legacy values and shapes rather than asserting a recovered address.

## Current locator contexts

locatorTemplate supplies the root record fields and explicitly separates
identity/address from Original And Prepared Mapping. locatorModel requires
record identity before position. Together they support the registry's
source/source-snapshot/resource/representation separation and the distinction
between an address and claim support.

pdfHandoff is synthetic: P-L1 is a converter index of unknown base, P-L2 a
physical PDF page 2, P-L3 printed label 1, P-L4 output lines 13--20, and P-M1
is bounded mapping evidence. epubHandoff is also synthetic: E-L1 is a
resource-scoped anchor, E-L2/E-L3 are output ranges, and E-M1/E-M2 are mapping
examples. They demonstrate field semantics and possible conventions, not an
actual successful conversion or claim support.

arc07LocatorMap is the separate, actual generated map: loc-ch01-emergence
names chapter-01.md, source lines 53--57, with one-based inclusive endpoints.
It is an external map, not populated standalone source-locator frontmatter,
and does not independently verify a source claim. arc07 only shows generated
card references to prepared-source records; it does not fill the unavailable
original/mapping evidence.

## Historical comparison and limits

v31Guide and checked successor v32Guide both treat the seven fields as
Provenance/frontmatter. Both define source_slug as the source directory name;
v3.2 adds that it is the common leaf under sources/md/ and concept-cards/.
The OTP sample's concept-cards/otp-design-principles leaf conforms to that
card-side convention, but no paired source-tree directory was inspected.
Therefore the relation is retained as intended local lookup behavior, not as
global identity, a snapshot, or proof of current layout conformance.

Both guides say pdf_page comes from the chapter metadata header or may be null.
That is an intended input relationship, not evidence of which header produced
Accent Types, its coordinate basis, or its conversion lineage; its body page
citations remain separate. v3.2 additionally says chapter_number is null for
preludes, introductions, unnumbered sections and appendices rather than using
non-integers, and says no-PDF Markdown/HTML-origin sources use pdf_page null
and a section-heading or URL-fragment fallback in Source Reference. These are
normative historical conventions. Neither a sampled chapter_number/pdf_page/
section null nor a source-family pattern proves its particular reason.

The frozen source-family census has thirteen observed source_slug groups and
retains all seven fields' presence, shapes and distinct-value counts per group.
It shows that all 224 numeric Erlang pdf_page values are in
design-scale-erlang-otp; erlang-in-anger has 94 null pages and chapter
numbers 93 numeric/1 null; otp-design-principles has 105 null pages and 105
null chapter numbers. All seven fields are present in these groups, but values
and shapes vary by family. Those observations motivate preserving local lookup,
header/null, and fallback semantics without normalizing families or diagnosing
their formats.

Neither guide supplies a snapshot identity, locator type/basis,
original/prepared counterpart, or mapping-evidence record. Thus historical
guidance supports preservation of legacy values and intended relations, while
the current locator material supplies distinctions that old flat frontmatter
does not represent.

The registry connects each field to evidence that bears on it. It does not
claim a schema, migration equivalence, resolved original source, page-offset
calculation, source-support verification, or automated mapping. CDC's prior
S7-2/S7-7 reproduction remains independent evidence; this inspection is CC
attestation only.
