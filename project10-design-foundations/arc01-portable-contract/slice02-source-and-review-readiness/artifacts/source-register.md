# Source register — Slice02

**Scope:** source identity, prepared navigation, cited-resource provenance, and known acquisition/fidelity gaps for the accepted 233-card baseline. This is a source register, not claim-level semantic review. Source pin: `dffa504e851b03b8e4746f1941068e4cc850b612`; accepted index: [Slice01 card-source-index.jsonl](../../slice01-scope-and-portability-contract/artifacts/card-source-index.jsonl). Access date for public web/catalog pages inspected: 2026-10-09. No original files were supplied by the Operator. No source was downloaded, converted, repaired, or edited.

## Primary identities reconciled against the exact raw pair

Counts below are grouped only by the accepted index's literal `source_fields_raw.source` and `authors` pair. Raw JSON strings (including quotes and escapes) are preserved in each locator row. The prepared document identities listed here describe local navigation evidence, not proof of original edition/capture fidelity.

| Local key | Exact accepted raw source | Exact accepted raw authors | Cards | Prepared material and identity status |
|---|---|---|---:|---|
| ARN | `"Art and Visual Perception: A Psychology of the Creative Eye"` | `"Rudolf Arnheim"` | 112 | No original supplied or pinned. No prepared source document in the designated `sources/md` corpus. Edition remains unknown. |
| CLE | `"A Practical Description of The Munsell Color System"` | `"T. M. Cleland"` | 19 | No original supplied or pinned. No prepared book document in designated corpus. Edition and page basis remain unknown. |
| TSCH | `"The New Typography"` | `"Jan Tschichold"` | 19 | No original supplied or pinned. No prepared book document in designated corpus. English edition/translation and page basis remain unknown. |
| BUT | `"Butterick's Practical Typography"` | `"Matthew Butterick"` | 37 | Thirty-seven exact page-title/URL matches in `knowledge/design/sources/md/practical-typography/`; each target is recorded with file SHA-256, complete document line range, and body boundary in `locator-map.jsonl`. The prepared tree has 156 Markdown pages and `_conversion-report.txt`; per-page Markdown navigation is mapped. Original site identity is indicated by prepared frontmatter URLs, but immutable capture time/fidelity is not established for this slice. |
| DRA | `"Working With Colors Guide"` | `"Sarah Drasner"` | 12 | Prepared page `knowledge/design/sources/md/posts/working-with-colours.md`, SHA-256 recorded per target; exact page title, Sarah Drasner, and frontmatter URL correspond to cited page. Public CSS-Tricks page identity and current text were inspected. CSS-Tricks reports original publication 2016-09-12 and update 2024-08-12 in visible page metadata; it is not the identity/date of this local capture. |
| BROWN | `"More Meaningful Typography"` | `"Tim Brown"` | 10 | Prepared page `knowledge/design/sources/md/posts/more-meaningful-typography.md`, SHA-256 recorded per target; page title, author, May 2011 page metadata, and section anchors inspected. Original A List Apart URL was read live on 2026-10-09; current page is not an immutable 2011 snapshot or proof of local capture fidelity. |
| OKLAB | `"A Perceptual Color Space for Image Processing"` | `"Bj\u00f6rn Ottosson"` | 13 | Prepared page `knowledge/design/sources/md/posts/a-perceptual-colour-space.md`, SHA-256 recorded per target; original headings/HTML IDs retained in the Markdown. Bottosson live URL inspected on 2026-10-09. Current page has a 2025 introduction and an earlier article body; no immutable capture date or conversion fidelity is established. |
| OKHSV | `"Okhsv and Okhsl"` | `"Bj\u00f6rn Ottosson"` | 11 | Prepared page `knowledge/design/sources/md/posts/okhsv-and-okhsl.md`, SHA-256 recorded per target; heading/HTML IDs retained. Bottosson live URL inspected on 2026-10-09; local capture date and fidelity remain unknown. |

Index grouping query: `jq -s 'group_by([.source_fields_raw.source[0],.source_fields_raw.authors[0]])|map({source:.[0].source_fields_raw.source,authors:.[0].source_fields_raw.authors,count:length})' <index>`. Observed groups total eight and sum to 233: ARN 112, CLE 19, TSCH 19, BUT 37, DRA 12, BROWN 10, OKLAB 13, OKHSV 11. The 83 local cards are exactly BUT 37 plus four post groups 46. The remaining 150 cards are the three book groups.

## Public acquisition candidates and limits

These pages were read as public metadata/source identity options only; none was acquired as an original file for this work. Access date: 2026-10-09.

- **Arnheim:** [University of California Press, second edition](https://www.ucpress.edu/books/art-and-visual-perception-second-edition/epub-pdf) describes the second edition; [Open Library edition record](https://openlibrary.org/works/OL980214W/Art_and_visual_perception?edition=artvisualpercept00arnh) and [Google Books record](https://books.google.com/books/about/Art_and_Visual_Perception.html?id=V2lhMORfIUAC) expose different catalog metadata for a 1974 edition. These do not identify the exact edition/page basis represented by each card.
- **Cleland:** [Munsell-hosted scan listing](https://www.munsell.com/wp-content/uploads/2011/03/munsell-color-system-cleland.pdf) identifies a 1937 publication; the PDF itself was not opened/downloaded. [Huntington Library catalog](https://www.huntington.org/collections/lib-710228) identifies a 1937 item by T. M. Cleland. A listing/catalog record does not verify bytes, edition, printed pages, or the card's asserted page 4.
- **Tschichold:** [University of California Press](https://www.ucpress.edu/book/9780520250123/the-new-typography) identifies its English translation and edition; [Open Library](https://openlibrary.org/books/OL1096211M/The_new_typography) gives different pagination metadata. The page-count discrepancy reinforces that page identity cannot be inferred from title alone.
- **Butterick:** Each exact prepared page has its own `url` in its frontmatter. The locator map records those as prepared-page identity witnesses; this run did not treat a URL/frontmatter witness as proof that the live original matches the saved conversion.

## Additional citations found in exact raw reference scan and target context

The full 233 `source_reference_raw` values were inspected after grouping by accepted primary identity. Additional citations remain outside the eight primary identities and do not automatically support the associated claims.

| Literal citation observation | Card population | Role observed or unresolved |
|---|---|---|
| “Also referenced in ‘Further Reading’: Robert Bringhurst, *The Elements of Typographic Style*, ‘Shaping the Page.’” | `knowledge/design/concept-cards/posts/golden-ratio.md` | Explicit further reading in Brown's article. Not a primary source identity and not support for all Golden Ratio claims. |
| Bringhurst quotation attributed within “Modular scales and how they apply to web design”; Brown's “Further Reading” entry for “More Perfect Typography” | `knowledge/design/concept-cards/posts/musical-interval-typographic-ratio.md` | Attributed quotation/supplement. The talk is identified as “more inspiration than information.” Neither is an additional accepted primary pair. |
| “Adolf Loos quotation from p.73” | `knowledge/design/concept-cards/the-new-typography/ornament-rejection.md` | An attributed quotation reproduced in the cited Tschichold material; Loos is not thereby a verified source/edition in this register. |
| “DIN 476 specification reproduced on pp.97-98” | `knowledge/design/concept-cards/the-new-typography/din-paper-formats.md` | Embedded/reproduced external standard; exact DIN publication/version and relationship to cited book passage are unverified. |
| RIT Munsell color-chart data link in the prepared Oklab article's “Munsell data” section; article describes chart data as originating from experimental work in the 1940s and qualifies its quality | `knowledge/design/concept-cards/posts/chroma-perceptual.md`; `knowledge/design/concept-cards/posts/colour-space-comparison.md` | Linked comparison dataset/source, not the article's primary identity. The RIT target and underlying experiment were not inspected in this task. Preserve article's caveat; do not convert plotted comparison to verified experimental truth. |
| Luo-Rigg dataset link in Oklab article section “Luo-Rigg dataset and full gamut” (`https://github.com/nschloe/colorio/tree/master/colorio/data/luo-rigg`) | `knowledge/design/concept-cards/posts/colour-space-comparison.md` | Linked dataset cited for plotted ellipses; underlying files, provenance and method were not inspected. Article's plotted comparison is not independently verified by the citation inventory. |

The Brown article's local “Further Reading” section (prepared lines 358–363) was inspected. The Oklab “Munsell data” section (prepared lines 251–328) was inspected as context for its linked data reference. These observations are citation-role inventory only; no external citation has been independently reviewed as claim support.

## Design source corpus inventory

Direct `find` inventory of `knowledge/design/sources/md/`: 161 files, comprising 160 Markdown files and one conversion report. Every path is recorded with byte size and SHA-256 at source pin `dffa504e851b03b8e4746f1941068e4cc850b612`. The Markdown page corpus contains the four article captures and 156 Butterick pages. The report records five broken internal links. This is an identity inventory; it is not a fidelity comparison or content-read assertion for all 161 files.

| Source-tree path | Bytes | SHA-256 |
|---|---:|---|
| `knowledge/design/sources/md/posts/a-perceptual-colour-space.md` | 64438 | `ffe5494da6f0d040fb341d8e1f03d3e396600f6787088b6d57e32613798375f4` |
| `knowledge/design/sources/md/posts/more-meaningful-typography.md` | 38167 | `6b63c1ca5bf9d2d92ebb0f8cda8bf05ecd2fffdabf3d068e496b42c2794f33b9` |
| `knowledge/design/sources/md/posts/okhsv-and-okhsl.md` | 99663 | `227d62385a8ca4dfa77e9f5a10d55c9bd8d1c2f29d8964f59a1059bfb67d5d19` |
| `knowledge/design/sources/md/posts/working-with-colours.md` | 49571 | `f4cf46139cd45b5e8d78865666520520493dbafe4fe39a89b9c0e32227c0e4af` |
| `knowledge/design/sources/md/practical-typography/_conversion-report.txt` | 2944 | `071d1a3237ef9598b60e8501a223b52409da46170877174b04448ecdc0f338a3` |
| `knowledge/design/sources/md/practical-typography/about-matthew-butterick.md` | 1856 | `148d988bdaa44217e06ea0e3cab4f9867e5c3bd31f62b37580f1fc701c47ba28` |
| `knowledge/design/sources/md/practical-typography/accented-characters.md` | 3127 | `82393d7adb29b2ee6a80c0333eef0905deb647b0ec62c252147c7ddc29e20c43` |
| `knowledge/design/sources/md/practical-typography/acknowledgments.md` | 4359 | `1f62ef5e8b42595c17b4ef010f6ac5bfbe6f9e93346545230fa3ae688fb4ed05` |
| `knowledge/design/sources/md/practical-typography/advocate.md` | 5927 | `ca5344204b745c53ad759fa2b30c7623fef4b9c162991269b47c4e64310ff961` |
| `knowledge/design/sources/md/practical-typography/afterword.md` | 4722 | `91dc49e5832702c8b9462f99baa312dba8c2cfe8f1a1db92737290a501eafe3b` |
| `knowledge/design/sources/md/practical-typography/all-caps.md` | 7490 | `20bd4ee7b2d505b18f090325213a7cddd5a67fcfec723b241df4693f2ff6a7f8` |
| `knowledge/design/sources/md/practical-typography/alternate-figures.md` | 8804 | `2cdb62ee2831723bd5d70aad6fd11f1dea3fac2542c2b8b26f5528e8db8e4357` |
| `knowledge/design/sources/md/practical-typography/ampersands.md` | 1948 | `ab2a3026e805175b7312f5abaad5bda63aa185bf993fd57186c6923b25fcae50` |
| `knowledge/design/sources/md/practical-typography/apostrophes.md` | 5327 | `b009f04c2f9e32adc553f1ae4dc06cec4fdd7ada08f09ab9983b3cee72eef452` |
| `knowledge/design/sources/md/practical-typography/appendix.md` | 2378 | `72e128bea5945b14c42976a9042c8afa6533e6fc683573dfc08b8bc7feb73dcf` |
| `knowledge/design/sources/md/practical-typography/are-two-spaces-better-than-one.md` | 26509 | `885c841dca27e247cd825c064572928bac78b3743430683bd4b5d0783bfc0319` |
| `knowledge/design/sources/md/practical-typography/bad-fonts.md` | 3540 | `e39ce3980ae1c5b2b408c56c85c157f7c1efe491d61a183c0b0e0275bee2f8ba` |
| `knowledge/design/sources/md/practical-typography/baskerville-alternatives.md` | 2516 | `132d59c942e083fda7da511c7d799ff1bc929145aeffd36c99fbb3db58f93d67` |
| `knowledge/design/sources/md/practical-typography/bibliography.md` | 6374 | `7ec3eb47aa9363f92c02390c7a2a3b97233647f1ea0b2dc9bc1cb1a64d96fc35` |
| `knowledge/design/sources/md/practical-typography/billionaires-typewriter.md` | 38266 | `42e7d5dd99f44eb393d5d717dc00dc733dd4eee3e73b4f43bde86cc24b46076c` |
| `knowledge/design/sources/md/practical-typography/block-quotations.md` | 2856 | `594977aaf6d32069ac15bb72bd460b5f10c7fd0efec72309ae31f805698baa18` |
| `knowledge/design/sources/md/practical-typography/body-text.md` | 2738 | `055b9af901105e12fd37ef1b0651e6bea9ff9eaf2ba4162da0bfc6ffc2d62a97` |
| `knowledge/design/sources/md/practical-typography/bold-or-italic.md` | 5087 | `e9e414c02cce129086220a0c437e01e18a608cecc9ee8295b26e96ad30e98802` |
| `knowledge/design/sources/md/practical-typography/bulleted-and-numbered-lists.md` | 3773 | `012bd136da76668b01dbbc266723ce42d0a92ea041351ed7b9880945e0ec1214` |
| `knowledge/design/sources/md/practical-typography/business-cards.md` | 5089 | `7dd7cc29145cdad1236e3d400c00be4d099deca2fd1c47d95a00d73d4824414f` |
| `knowledge/design/sources/md/practical-typography/calibri-alternatives.md` | 2595 | `8c5234a5af2d354b97b206f0ab1255ab35a155f69a8f6e2607c7e5c5039dd1e7` |
| `knowledge/design/sources/md/practical-typography/cambria-alternatives.md` | 2827 | `95f1a30f03bd2ddf2a226fef6a0c5fc62ca7235cc6448955b0d64dea868519ac` |
| `knowledge/design/sources/md/practical-typography/carriage-returns.md` | 4652 | `e2b179001fadbdbc2bf005e0f21251bbb74bb34e8319d530155cfa2d8f3d334d` |
| `knowledge/design/sources/md/practical-typography/centered-text.md` | 2522 | `0642c57aeef6de9b77449c50c1233744ba8f9984e3a739d926a372cdbdc2401e` |
| `knowledge/design/sources/md/practical-typography/century-schoolbook-alternatives.md` | 4011 | `485d6401a1ec2f09798df6dd1308aa6b2eca37b6b6d51a52107e9dcffc3d6285` |
| `knowledge/design/sources/md/practical-typography/century-supra.md` | 7123 | `a4370790db3758ffdd3abe9a1542382ba087efe36f3b740935957ca945942d31` |
| `knowledge/design/sources/md/practical-typography/charter.md` | 4698 | `e1d41ad5e363f3887af67dffa12b05b59c85da2cb5554d4e55347f1226402a33` |
| `knowledge/design/sources/md/practical-typography/color.md` | 7797 | `7dbd3f8c25e016d2cb91eab699d21231595b53830954a385d8ccdb02dac44ee1` |
| `knowledge/design/sources/md/practical-typography/columns.md` | 3078 | `d99c374b97ce8d632b89bb10293caf5e971a14fbdc9df50dac93648df578bbc9` |
| `knowledge/design/sources/md/practical-typography/commentary.md` | 2677 | `f693d417f6fbb42f1392d76606407b6a58ac80f6f0c2a4fb25cc2553dbe7f5ee` |
| `knowledge/design/sources/md/practical-typography/common-accented-characters.md` | 4406 | `171a458676109731fdb3ad37e1f1b2f4e9cabdb4b7f9715f3dfcc779478149d0` |
| `knowledge/design/sources/md/practical-typography/concourse-index.md` | 3841 | `ff8adff837080d30a7fa349ec026b66f5000343f069ce2368f14a2547075b905` |
| `knowledge/design/sources/md/practical-typography/concourse.md` | 6975 | `e6bf960b055e2006bcf30846f636f06cc16fd9af063b8f3c1cfbd1840ceb4f39` |
| `knowledge/design/sources/md/practical-typography/contact.md` | 2023 | `e94199ff6d16df45e57e275c34df2c365be5431bce84c17eb0d4722d74453415` |
| `knowledge/design/sources/md/practical-typography/courier-alternatives.md` | 3207 | `5e4da2764c444bddfc6ad2211938dcc357b1c752a2e99ab99771a683788ac00c` |
| `knowledge/design/sources/md/practical-typography/drowning-the-crystal-goblet.md` | 5645 | `e3f7a16ff73180012bacfed42fdc76d0724d5a60a92a492e5752a98ed3b3268b` |
| `knowledge/design/sources/md/practical-typography/economics-year-one.md` | 14186 | `412f9453008bdabbf6e88631405ddb52ecb0db1d5c1f81f3659a82838c4113e5` |
| `knowledge/design/sources/md/practical-typography/effluents-influence-affluence.md` | 20107 | `12e1b8f61e704391e8e661039568a96576a87726ffb91865a6db53ff886fe478` |
| `knowledge/design/sources/md/practical-typography/ellipses.md` | 3919 | `d163b5de65e616e6e7d6de68b269b92789bf6137a1824a6bd2eb7b712cd0f701` |
| `knowledge/design/sources/md/practical-typography/em-sizing.md` | 5309 | `7edfba39584147cab484bed2733f028c0ae8907d2ded03f85cb48ae1f34af3f6` |
| `knowledge/design/sources/md/practical-typography/emails.md` | 2595 | `2016e35f8eced0f2f60a9eccb821b1a59bf46ee1a5b307638b65cf440f072953` |
| `knowledge/design/sources/md/practical-typography/emoticons-and-emoji.md` | 4282 | `a36b38e5d4068ed2b839ccd2fbab2a1d9c6fbc331a74133d100c348a5767c875` |
| `knowledge/design/sources/md/practical-typography/equity.md` | 7058 | `f420bff934470b9589613989cbcac397c5efb526f8621df0050bc70090669dc7` |
| `knowledge/design/sources/md/practical-typography/first-line-indents.md` | 5341 | `7a102923633d24dbfa56b35a9ad8ab063f26fe8cac00561099f116758f1bc77c` |
| `knowledge/design/sources/md/practical-typography/font-basics.md` | 8832 | `3e501b2cea0d19257c82dddd2b5ba0db62a64f31fa729aa596c5ce066661e616` |
| `knowledge/design/sources/md/practical-typography/font-recommendations.md` | 3998 | `c1598eff832aed41f036c584485efa389a1a53c970fd12f09f9fd197361aa9ee` |
| `knowledge/design/sources/md/practical-typography/foot-and-inch-marks.md` | 5012 | `f679415847ac6488d3d0deeb34b1b53a16b43bbb84582382cfa0d86af6b4f9ee` |
| `knowledge/design/sources/md/practical-typography/free-fonts.md` | 6324 | `ba4e3727b7aaa4b1b810eacc044c2311732ba796bebe50c22504f4ce229b87e5` |
| `knowledge/design/sources/md/practical-typography/georgia-alternatives.md` | 2701 | `4e3799948718e5add0683320c14549d9fe4f68752c909bfccc2e60491696909f` |
| `knowledge/design/sources/md/practical-typography/gill-sans-alternatives.md` | 4050 | `8e912707f18d8c3362061ea98dda1325d34368cabd6f6f4cc543f3ee2519cc89` |
| `knowledge/design/sources/md/practical-typography/goofy-fonts.md` | 2462 | `e485ed20f01e69316491d86ad713989fe2122c2a75f169cecefcf01df28c8026` |
| `knowledge/design/sources/md/practical-typography/grids-of-numbers.md` | 7592 | `167c12c282eade9db509fb3302cb63fcc2ee4e498a74cb361b228fcfcb2809de` |
| `knowledge/design/sources/md/practical-typography/grids.md` | 5898 | `30c2740c2f92145b66686c2b197166bd9c56cb53abde3a49430e744137f35bcd` |
| `knowledge/design/sources/md/practical-typography/hard-line-breaks.md` | 3179 | `4d99a8f16abf44a87672222272098857bd64c4f999f9cd6b162b66d7673a7945` |
| `knowledge/design/sources/md/practical-typography/hard-page-breaks.md` | 2963 | `0ea2e39601b2ddedf73aa78445413b36f77c2266dd0ead98ecd5ac04b220b670` |
| `knowledge/design/sources/md/practical-typography/headings.md` | 6424 | `5dd4275cf58d4c921391564b7c4a5f6f79e1a5e71a9ddebfe9055c9a1f9ff186` |
| `knowledge/design/sources/md/practical-typography/heliotrope.md` | 7061 | `a73a061d063612f411b9de9831dd38be0dd540516a80bce4c9bb467f95da75b3` |
| `knowledge/design/sources/md/practical-typography/helvetica-and-arial-alternatives.md` | 3831 | `b1e86baeffdbb78452b116695bfb6e4abaebc4a1d8e5e7138ec3ad1cd00e2dd2` |
| `knowledge/design/sources/md/practical-typography/hermes-maia.md` | 6693 | `56bc02d69affbd65c612e12adbb96caf3c62820d0e8c7d6316435f8f97f6c709` |
| `knowledge/design/sources/md/practical-typography/hierarchical-headings.md` | 3863 | `505cb0e465877540cfff77caec5203badd4b76ed56832d9d37f9a153de03deea` |
| `knowledge/design/sources/md/practical-typography/how-this-book-was-made.md` | 10100 | `213224237c6452d84bfa848f3d4fdaafa030fd78236f6d20225a814161314bcc` |
| `knowledge/design/sources/md/practical-typography/how-to-embed-fonts-in-a-word-document.md` | 6962 | `c8361df3e9abaeb03cbef04620f327753aaa4e5f46c0d872b0cc98e179480123` |
| `knowledge/design/sources/md/practical-typography/how-to-make-a-pdf.md` | 4322 | `e86ced7dc85b9838813cecec57bb802257daedc0304ccc00aa7a6d78bf42be26` |
| `knowledge/design/sources/md/practical-typography/how-to-pay-for-this-book.md` | 4892 | `d1ccb0d2a473bee97aca19c33c67671ffef2f44dbfcc0c96cdf869b27fdfd10a` |
| `knowledge/design/sources/md/practical-typography/how-to-use.md` | 3795 | `0bb4db85cca6112ec7cd3edfab9e1795a4bf4677a3271af09df5bdaddc1fd613` |
| `knowledge/design/sources/md/practical-typography/how-to-work-with-a-designer.md` | 4545 | `da24539829d53895904200a5183a90e6e4e43cb3d954f8f2eefd3adac9b0902b` |
| `knowledge/design/sources/md/practical-typography/hyphenation.md` | 5545 | `6f437e3dbdcca0268a65be92760bc7f5804c1ed8f87fe70ef34a6cbae1b50140` |
| `knowledge/design/sources/md/practical-typography/hyphens-and-dashes.md` | 6183 | `65943925a2742bb86fccc8cf00c8285a29283009282b400133c73bc821e5d523` |
| `knowledge/design/sources/md/practical-typography/identifying-fonts.md` | 4485 | `ad065c17faa646d60339c90841566ce66a060f85671f95d2ecd455d329d22c20` |
| `knowledge/design/sources/md/practical-typography/index.md` | 957 | `6b8ffacecfb2e802b3be6588770aa6ebcf7fb4ce4bb3408951f2113dea88a783` |
| `knowledge/design/sources/md/practical-typography/introduction.md` | 9334 | `f14cb42da722ed8e0162e47176e26d32ba8016826ff08089c48c73bf7942e36b` |
| `knowledge/design/sources/md/practical-typography/justified-text.md` | 3648 | `5d989c6c096eb73f9ae1993879499243c68ea53e0fc4f5c5ef17f28b81e985af` |
| `knowledge/design/sources/md/practical-typography/keep-lines-together.md` | 3737 | `cd6f251d359346423becd322ff5efd477f4a9f62654573c3105de868e1eb2ab1` |
| `knowledge/design/sources/md/practical-typography/keep-with-next-paragraph.md` | 3582 | `37bde77ecbab9b5660c24f9d21f1e47c7bfc4b29fb10adc6db5c0036edc3b755` |
| `knowledge/design/sources/md/practical-typography/kerning.md` | 3150 | `d94a221b5a5a733a6a7868b4f92c67fa9be5f9b59a5a111c4cadce432d3a5063` |
| `knowledge/design/sources/md/practical-typography/legal.md` | 3545 | `5bb9d0d733e67a2bc7f09c1fb72241155e30271fd175a01245a0e4f5144d30f4` |
| `knowledge/design/sources/md/practical-typography/letterhead.md` | 9340 | `62e98d4d92d312362a233e5edd90894e9a64470ba74dcdc9a898319464559f82` |
| `knowledge/design/sources/md/practical-typography/letterspacing.md` | 4662 | `ae79e2ace6b225db746bf4c32fb3eb6e1318aee36afd17f690b8d22450fabce8` |
| `knowledge/design/sources/md/practical-typography/ligatures-in-programming-fonts-hell-no.md` | 9622 | `7f061ea7fed4a6061612f038487d12cf6ed04cd1dd51b8201d83dbd208a30de1` |
| `knowledge/design/sources/md/practical-typography/ligatures.md` | 4701 | `133240bd1aad183636260e64ba67d054ae2953df216aa48eb7c6440560e78d65` |
| `knowledge/design/sources/md/practical-typography/line-length.md` | 4279 | `c746cf4dff19c3bdead7218d63179f7c2916bd0691632bf9d39d40b54fafc61a` |
| `knowledge/design/sources/md/practical-typography/line-spacing.md` | 5445 | `ba52f1c3f5ed41990f96b300cce2fd2b5308c689738f792086d8d810343fd4c3` |
| `knowledge/design/sources/md/practical-typography/math-symbols.md` | 2980 | `df8db8303cb457944d27ce0eb9cb3e0cc6d846b0e15e6a4015ea11e714400e8d` |
| `knowledge/design/sources/md/practical-typography/maxims-of-page-layout.md` | 4657 | `880b9b1f0a1ca637feeeedf3302b9d57f1d11f24991ead38d3f51fcbf2249f82` |
| `knowledge/design/sources/md/practical-typography/mb-fonts.md` | 3435 | `95277ee3349a0237125149d79ee0d052eada55d2c08ebbeca5899a4e1826e802` |
| `knowledge/design/sources/md/practical-typography/mb-lectures-and-articles.md` | 2777 | `9959f6d6c032697270dbf62e64ee92fe870790596c204e902835fdd212d4bff0` |
| `knowledge/design/sources/md/practical-typography/metrics-vs-optical-spacing.md` | 6896 | `1141951142b4724ea4f6ece98c68e7103cb2eaaa93e33d6f4ac9c8ee837c479f` |
| `knowledge/design/sources/md/practical-typography/minion-alternatives.md` | 4236 | `0fe685cec1dbe6fa25f4928a9aa702a7bc341017b1cbb6877dc9ed69d70681db` |
| `knowledge/design/sources/md/practical-typography/mixing-fonts.md` | 4347 | `0d2cd104b9536c752740a6508d63d229e606db45bdc5df5168951bb6ed904937` |
| `knowledge/design/sources/md/practical-typography/monospaced-fonts.md` | 3635 | `c70a38b9db0d8601d846102b61b74acc82c259024a3c365720f350514a63cfff` |
| `knowledge/design/sources/md/practical-typography/nonbreaking-spaces.md` | 4250 | `02f6511990a595df42b2dc97ef008a4971250cf1a5bba91609fa19be72c709eb` |
| `knowledge/design/sources/md/practical-typography/one-space-between-sentences.md` | 8944 | `942b66541079ce2bf80f6cc4f60b213729671d287fddb8dfc0871b23cbb7b84b` |
| `knowledge/design/sources/md/practical-typography/opentype-features.md` | 4824 | `4a65e01b0778d9be0c4e176f8413475d66fb0cc01dd65621ea1f5f325d69501e` |
| `knowledge/design/sources/md/practical-typography/optional-hyphens.md` | 3607 | `d54d0f660a6bcb3c5417e18fc78f3dcf6a3f46abe5693174843119d0e78c6311` |
| `knowledge/design/sources/md/practical-typography/ordinals.md` | 3079 | `aa6e7302b715ff520e8b4648c3556880b1b75a1c2b15cfbcd77013a0656ee77c` |
| `knowledge/design/sources/md/practical-typography/oscars-2020.md` | 9261 | `ae21ea9c7a19cacec1056151b54a493c06a7170ac6928f5002730d20843f9340` |
| `knowledge/design/sources/md/practical-typography/page-break-before.md` | 2952 | `3199877a96e934b7247c8b87b955efdb2ddcecf90751d107090b4e6165cdb5d5` |
| `knowledge/design/sources/md/practical-typography/page-layout.md` | 4007 | `070412e2e59d4d2084bc5e3a40059e21997689494b7a35a5cc40e819019cc840` |
| `knowledge/design/sources/md/practical-typography/page-margins.md` | 9735 | `6f56b61b97a152dcc1d6f4f47402e53ef17d63a9638190e43909f7c813a43d05` |
| `knowledge/design/sources/md/practical-typography/palatino-alternatives.md` | 3907 | `9f31746ae742c926730be706283b4a7e0faf983063842aeba40573396b5bb07c` |
| `knowledge/design/sources/md/practical-typography/paragraph-and-character-styles.md` | 6981 | `3da1e08beee202df40ea212aac29bfb3ea7b4dffe6ca47dce92b44c433fd29e7` |
| `knowledge/design/sources/md/practical-typography/paragraph-and-section-marks.md` | 3637 | `2b55d76f87259493f7d0a761769b341af9b1a88e201e695d659840ff8ff0fef5` |
| `knowledge/design/sources/md/practical-typography/parentheses-brackets-and-braces.md` | 3099 | `45b389428c67c2fdbb85c6335fb9d5c33b11e82e100dae4ed261f85e32f328a2` |
| `knowledge/design/sources/md/practical-typography/point-size.md` | 8634 | `a578f425f2ad5541fb458032c5734767e9ef886197ebc003923cc0c0170b6afe` |
| `knowledge/design/sources/md/practical-typography/presentations.md` | 8761 | `b383a41d18c75c534d9e570c7b63cf6a0a8b08f9dbdb2e7914b58ab9ad351068` |
| `knowledge/design/sources/md/practical-typography/printers-and-paper.md` | 10253 | `b4cc90fa44cf1e9f91dd7470010b667195ba9f2f660e9c6a3e5b5f9311a9fe62` |
| `knowledge/design/sources/md/practical-typography/question-marks-and-exclamation-points.md` | 3001 | `598e188ecf96ece32328a3ca9fecf8dec01214c8b53299b9d4fe9200d39d5a93` |
| `knowledge/design/sources/md/practical-typography/research-papers.md` | 5595 | `489dfca18d567ee2956ffc79f8345e5b5d07a6099c66520d914d63214ffbf4da` |
| `knowledge/design/sources/md/practical-typography/responsive-web-design.md` | 6338 | `d0c7f626441abb73eea9505c415ba394320034043ddc46403f7c1e28935f8423` |
| `knowledge/design/sources/md/practical-typography/resumes.md` | 7563 | `f6291e0979dfa84400793e569be91c1dc512f150a51ff1c649ea4b4adaffabb8` |
| `knowledge/design/sources/md/practical-typography/rules-and-borders.md` | 5603 | `6bfe97fef23e5e321a23451dad26163bd82b33ce610e587433b1c25bffbf8fff` |
| `knowledge/design/sources/md/practical-typography/sample-documents.md` | 2809 | `03e8ac21b7d9421f5b633b1d112d9f85ab526d4f9d6c0406e55e480754fccd9a` |
| `knowledge/design/sources/md/practical-typography/screen-reading-considerations.md` | 7660 | `24b8aa2ec7bc6cb8e0ef05268ae4ec95f5d5407b97d6779d339b9400c34f0e99` |
| `knowledge/design/sources/md/practical-typography/semicolons-and-colons.md` | 2607 | `ef8ac07885adccb135bccfc39d4692a2ccc37265aad0a97be480ffd35a7f52e6` |
| `knowledge/design/sources/md/practical-typography/signature-lines.md` | 3990 | `676217ceff68e5b23bccad5300a633fcd082653568fbcb0d2c197dc59a9f343b` |
| `knowledge/design/sources/md/practical-typography/small-caps.md` | 6113 | `8ca9dd84fb35c91efbb70eb7a9b7a6814777400269f3f85343964baa8ea62149` |
| `knowledge/design/sources/md/practical-typography/space-above-and-below.md` | 4167 | `a4815bbf0a155fa430be87fcbe7d384ebbbbe02d7d8b9c8f164e0377bc8539a4` |
| `knowledge/design/sources/md/practical-typography/space-between-paragraphs.md` | 3399 | `b607c35699a0cbe24cf1392f4183a0195c3487aa8b9e4218be3c7e2536aab395` |
| `knowledge/design/sources/md/practical-typography/straight-and-curly-quotes.md` | 8908 | `4263dd8660cb5733b9a44bb56c0c3c5e1ff18eb4a068642ba061d1ef93ca13f8` |
| `knowledge/design/sources/md/practical-typography/summary-of-key-rules.md` | 5656 | `25c0b4ebf505bd117bd0452b3c48982634297180a8d9c022011356eb8cec7abb` |
| `knowledge/design/sources/md/practical-typography/system-fonts.md` | 10024 | `41362ca766cd3d5694014bbb44fa8a6c56eb20024f12eb00ff52454ac45c14fc` |
| `knowledge/design/sources/md/practical-typography/tables.md` | 8330 | `47b74582dbe317d246950956b560b9609e479ab1a8580f8125a364a64267ee25` |
| `knowledge/design/sources/md/practical-typography/tabs-and-tab-stops.md` | 6463 | `282f72d2402ec6c59cefe70dcf2385d86b31eb5af0ff13fc20aef73293c41c87` |
| `knowledge/design/sources/md/practical-typography/text-formatting.md` | 3307 | `1b66b137343b97c1c05e535ffa97bb973699d9501fedbc8bc1d4ea77e1ccb89c` |
| `knowledge/design/sources/md/practical-typography/the-copyright-status-of-fonts.md` | 5306 | `f4641846bfc92dda6d2e5572f55627d79bdf2c7cb3cf1708f88de12b664d894d` |
| `knowledge/design/sources/md/practical-typography/the-cowardice-of-brave.md` | 36573 | `7303715b9a1de3eac2d64238d0349b03d4d45302be812b20dee8dd675d9e2231` |
| `knowledge/design/sources/md/practical-typography/the-infinite-pixel-screen.md` | 26341 | `b6c51358d0f512b371d61ce83665c2f61f0cc12750cf1b5ee8ea785cf726595e` |
| `knowledge/design/sources/md/practical-typography/the-scorpion-express.md` | 86091 | `4e94fc7bb41866fc118066ceb7657c5aeecc6bb6b224a432b2d9a5e80872c119` |
| `knowledge/design/sources/md/practical-typography/times-new-roman-alternatives.md` | 7136 | `7270bc6b3683e3be5dd17e33ff71883470ee629915ebff0287776837aa38d9a2` |
| `knowledge/design/sources/md/practical-typography/to-pay-or-not-to-pay.md` | 10908 | `f772344a938d0650d5f7a1a77beacdcd55ff873878c148fa66210017497d633b` |
| `knowledge/design/sources/md/practical-typography/trademark-and-copyright-symbols.md` | 4331 | `0261da708b0e4730c2aa96247cb8f26229f1329a03b10f5f2e2984a54df0d906` |
| `knowledge/design/sources/md/practical-typography/triplicate.md` | 7351 | `555d7f1b0b34e4f859ff1772fa4936f146702449d1830d4ad136f9598f403e94` |
| `knowledge/design/sources/md/practical-typography/type-composition.md` | 4659 | `c1edd8c9dfcf9929ae91314abf03ee2b8fcb5951cb8fce236727140b3819a70b` |
| `knowledge/design/sources/md/practical-typography/typewriter-habits.md` | 4344 | `f19e461d37bd4076d618af3c3a701dc18ef53ddc7eb4dc074821a9b15228e497` |
| `knowledge/design/sources/md/practical-typography/typographic-humor.md` | 3794 | `01d0604518c6bdc818a5d15da57d27bf312326d9ce5a72f344aa918f1bf654fe` |
| `knowledge/design/sources/md/practical-typography/typography-2020.md` | 30448 | `2e9d4fa886526704123d3c3780e42ee509c424f066990f09e853391ce36be49f` |
| `knowledge/design/sources/md/practical-typography/typography-2024.md` | 17960 | `de42275177642f372054e47ecabaf8f57779119b9a6476f154d48020ade07445` |
| `knowledge/design/sources/md/practical-typography/typography-in-ten-minutes.md` | 5303 | `8f23ea1dda0486b0e14edc8f1945bebff7870f2e6d4981b1414550b416dcf83e` |
| `knowledge/design/sources/md/practical-typography/underlining.md` | 4803 | `4d7bb8dfa56800da0975699d2f2dc9c10cc008652fba9ff3484e493ab5bb606d` |
| `knowledge/design/sources/md/practical-typography/valkyrie.md` | 6879 | `4a27cae9058de30534fa8713cd65d27024f601f585a2872a874b2bcb58db69a8` |
| `knowledge/design/sources/md/practical-typography/verdana-alternatives.md` | 2966 | `86253343e2febf0c2243f0710925cb675c27ab4e1fa653357a1c4ea44fce7953` |
| `knowledge/design/sources/md/practical-typography/vote-with-your-wallet.md` | 7972 | `7875f5a25cceac7b2c1ef8544dff68741919d83a384374f760b37a357baf79fe` |
| `knowledge/design/sources/md/practical-typography/web-and-email-addresses.md` | 4475 | `4eeebf701e663d6b2e256f265dc890fa884f193c53870b99cf396f4a8af9b715` |
| `knowledge/design/sources/md/practical-typography/websites.md` | 11249 | `8e9fb78f5696dfc5aedc7e8f68029bb91e400486a449a662aa5922d9fa59ff3b` |
| `knowledge/design/sources/md/practical-typography/what-is-good-typography.md` | 5990 | `278cfabe56e93caa21d316a98265e6cabb2d54938c4780263f72507c38ba4816` |
| `knowledge/design/sources/md/practical-typography/what-is-typography.md` | 2753 | `75faba808464ca07f74f053ed57d521e7a31dfe84f4ff017ce3c9aab38912cbb` |
| `knowledge/design/sources/md/practical-typography/where-do-the-rules-come-from.md` | 4124 | `94c5cf73fc696e2e0a69ad81bad8291667e1e7bba54d3da04d070d0d83718830` |
| `knowledge/design/sources/md/practical-typography/white-space-characters.md` | 4783 | `16d6e13c82b8968e98bb46544f4d298ae46c50d0c0effe7d6a7cad1f0c25d437` |
| `knowledge/design/sources/md/practical-typography/who-is-typography-for.md` | 3657 | `19df5d0dd412041931a62f333e04767df87396a1369e11f189e7d7743e1a5130` |
| `knowledge/design/sources/md/practical-typography/why-does-typography-matter.md` | 9358 | `bb10497f7349cf7de36430b258f3bfc822542ace14620d9c99b7d60fb5347333` |
| `knowledge/design/sources/md/practical-typography/why-racket-why-lisp.md` | 36190 | `891b27ff49ee44977eeaae741b938daf7060cb6fcdb3a4586d15e3409517a8b2` |
| `knowledge/design/sources/md/practical-typography/why-theres-no-e-book-or-pdf.md` | 16675 | `99baf8216128d2b1d37646af59ae1de5d92e88bfb339ad975c9c6af58c63747e` |
| `knowledge/design/sources/md/practical-typography/why-typography-matters.md` | 3337 | `223db7ec7f0d4f399163427204a96dbe8a3822311e2184ed2f25bb26ed3d9090` |
| `knowledge/design/sources/md/practical-typography/why-you-should-pay.md` | 4276 | `2135ddb8e722e12bdb60c1e710d709d4654aa191e3ac4c5798160f3b4e6ca3e5` |
| `knowledge/design/sources/md/practical-typography/widow-and-orphan-control.md` | 4390 | `dde4d586ae692259bc3a58f852413a18f386f29a8e0a012f5b4f5e368304cf54` |
| `knowledge/design/sources/md/practical-typography/word-spaces.md` | 3022 | `bae27382af6b429c5893a1d4876072bcbbb8486ba68e2054a724591c860d0ada` |

## Active caveat register (iteration01)

Membership is by full card path and literal primary pair in `locator-map.jsonl`; equal basenames do not imply equal source identity. These definitions supersede earlier caveat notes.

| ID | Exact population / pair | Current handling and next action |
|---|---|---|
| `C-ARN-ORIGINAL-EDITION` | 112 Rudolf Arnheim / *Art and Visual Perception: A Psychology of the Creative Eye* cards | Exact edition/bytes unavailable; Operator to supply/select, CDC to scope comparison. |
| `C-ARN-PAGE-BASIS` | Same 112 cards | Printed/physical page mapping and cited positions unverified; resolve against pinned original. |
| `C-CLE-ORIGINAL-EDITION` | 19 T. M. Cleland / *A Practical Description of The Munsell Color System* cards | Exact edition/bytes unavailable; public listing is candidate metadata only. Operator input, then CDC-scoped comparison. |
| `C-CLE-PAGE-BASIS` | Same 19 cards | Printed versus physical scan page basis unverified. Newly named applicable issue; no former web-local ID is implied. |
| `C-TSCH-ORIGINAL-EDITION` | 19 Jan Tschichold / *The New Typography* cards | Exact edition/translation and bytes unavailable; public pagination conflicts. Operator input, then CDC-scoped comparison. |
| `C-TSCH-PAGE-BASIS` | Same 19 cards | Printed/physical page mapping unverified; resolve against pinned edition. |
| `C-BOOK-FIDELITY` | 112 Arnheim + 19 Cleland + 19 Tschichold = 150 book cards | Source-to-card comparison blocked until exact originals/editions are supplied and page mappings checked. |
| `C-BUTTERICK-CAPTURE-IDENTITY` | 37 Matthew Butterick / *Butterick's Practical Typography* cards | All 37 prepared pages fully read and locally identified by exact frontmatter title, URL and body boundary. Original capture identity/revision/date and conversion lineage remain unavailable. |
| `C-BUTTERICK-CAPTURE-FIDELITY` | Same 37 cards | Compare supplied immutable capture/manifest with full prepared page, media/examples and cited context; not established here. |
| `C-WEB-CAPTURE-IDENTITY` | 46 post cards across four online article pairs: Drasner 12, Brown 10, Oklab 13, Okhsv 11 | Prepared navigation exists. Immutable capture date/revision, scope and lineage unavailable; Operator/CDC to supply or authorize scoped capture. |
| `C-WEB-CAPTURE-FIDELITY` | Same 46 cards | Source-to-prepared comparison and dynamic/media completeness not established; requires immutable captures and scoped comparison. |

### Retired issue IDs and resolved local targets

- `C-BUTTERICK-TITLE-UNRESOLVED` is retired: all 37 joins use literal primary pair, raw citation title, observed frontmatter title, URL and body boundary. Nine title differences retain `citation_title_raw`; no title alone is identity.
- `C-WEB-LOCAL-LOCATOR-UNRESOLVED` is retired for ten Brown cards: exact prepared spans were checked, including the unheaded line-109 opening on the two cards whose raw references name it.
- HSL Values is locally resolved at `working-with-colours.md#lines-97-125`, retained ID `aa-hsl-values`, for `hsl.md` and the post Munsell card. This does not resolve primary Okhsv capture identity/fidelity.
- Conversion report broken links: `free-fonts`, `the-scorpion-express`, `times-new-roman-alternatives`, `to-pay-or-not-to-pay`, `websites`. None intersects the 37 selected Butterick target pages; other conversion/media impacts remain unassessed; no repair is authorized.
