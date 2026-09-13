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
Provenance/frontmatter and specify pdf_page/section may be null. The v3.2 text
adds a source-slug directory description but neither guide supplies a snapshot
identity, locator type/basis, original/prepared counterpart, or
mapping-evidence record. Thus the historical guidance supports preservation of
legacy field values, while the current locator material supplies distinctions
that the old flat frontmatter does not represent.

The registry connects each field to evidence that bears on it. It does not
claim a schema, migration equivalence, resolved original source, page-offset
calculation, source-support verification, or automated mapping. CDC's prior
S7-2/S7-7 reproduction remains independent evidence; this inspection is CC
attestation only.
