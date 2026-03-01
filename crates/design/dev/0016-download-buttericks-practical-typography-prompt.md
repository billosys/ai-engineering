# Download *Butterick's Practical Typography* Prompt

## Context

*Butterick's Practical Typography* (2nd edition) by Matthew Butterick is a complete web-based book on typography, freely available at <https://practicaltypography.com/>. The author intentionally does not offer PDF or EPUB versions — the book exists only as individual HTML pages. We need a local archive of every page for use as a source in a design knowledge engineering project.

**Legal basis:** The author explicitly makes the book free to read online. We are downloading for personal reference and knowledge extraction, not redistribution.

---

## Task

Download every page of the book as individual HTML files into `./sources-html/practical-typography/`.

---

## Complete Table of Contents (authoritative — scraped from the live site)

Use this as the **primary manifest**. Every slug listed below MUST have a corresponding `.html` file in the output directory. After downloading via link discovery, cross-reference against this list to catch anything missed.

### Top-level pages

- `typography-in-ten-minutes`
- `summary-of-key-rules`

### Start

- `introduction`
- `how-to-use`
- `acknowledgments`
- `about-matthew-butterick`
- `legal`

### Please pay for this book

- `how-to-pay-for-this-book`
- `why-you-should-pay`
- `mb-fonts`

### Why typography matters

- `why-typography-matters` *(section landing page)*
- `what-is-typography`
- `who-is-typography-for`
- `why-does-typography-matter`
- `what-is-good-typography`
- `where-do-the-rules-come-from`

### Type composition

- `type-composition` *(section landing page)*
- `straight-and-curly-quotes`
- `one-space-between-sentences`
- `question-marks-and-exclamation-points`
- `emoticons-and-emoji`
- `semicolons-and-colons`
- `paragraph-and-section-marks`
- `parentheses-brackets-and-braces`
- `hyphens-and-dashes`
- `ampersands`
- `signature-lines`
- `trademark-and-copyright-symbols`
- `ellipses`
- `apostrophes`
- `accented-characters`
- `foot-and-inch-marks`
- `white-space-characters`
- `word-spaces`
- `nonbreaking-spaces`
- `tabs-and-tab-stops`
- `hard-line-breaks`
- `carriage-returns`
- `hard-page-breaks`
- `optional-hyphens`
- `math-symbols`
- `ligatures`

### Text formatting

- `text-formatting` *(section landing page)*
- `underlining`
- `goofy-fonts`
- `monospaced-fonts`
- `bold-or-italic`
- `all-caps`
- `point-size`
- `headings`
- `letterspacing`
- `kerning`
- `color`
- `alternate-figures`
- `ordinals`
- `web-and-email-addresses`
- `emails`
- `small-caps`
- `hierarchical-headings`
- `opentype-features`
- `mixing-fonts`
- `metrics-vs-optical-spacing`

### Font recommendations

- `font-recommendations` *(section landing page)*
- `font-basics`
- `equity`
- `valkyrie`
- `century-supra`
- `concourse`
- `hermes-maia`
- `heliotrope`
- `triplicate`
- `advocate`
- `system-fonts`
- `free-fonts`
- `charter`
- `helvetica-and-arial-alternatives`
- `times-new-roman-alternatives`
- `courier-alternatives`
- `palatino-alternatives`
- `baskerville-alternatives`
- `century-schoolbook-alternatives`
- `georgia-alternatives`
- `verdana-alternatives`
- `gill-sans-alternatives`
- `cambria-alternatives`
- `calibri-alternatives`
- `minion-alternatives`
- `bad-fonts`

### Page layout

- `page-layout` *(section landing page)*
- `centered-text`
- `justified-text`
- `first-line-indents`
- `space-between-paragraphs`
- `line-spacing`
- `line-length`
- `page-margins`
- `body-text`
- `hyphenation`
- `block-quotations`
- `bulleted-and-numbered-lists`
- `tables`
- `rules-and-borders`
- `widow-and-orphan-control`
- `space-above-and-below`
- `page-break-before`
- `keep-lines-together`
- `keep-with-next-paragraph`
- `columns`
- `grids`
- `paragraph-and-character-styles`
- `maxims-of-page-layout`

### Sample documents

- `sample-documents` *(section landing page)*
- `research-papers`
- `letterhead`
- `business-cards`
- `resumes`
- `grids-of-numbers`
- `presentations`
- `websites`

### Afterword

- `afterword`

### Appendix

- `appendix` *(section landing page)*
- `typewriter-habits`
- `printers-and-paper`
- `how-to-make-a-pdf`
- `how-to-embed-fonts-in-a-word-document`
- `identifying-fonts`
- `em-sizing`
- `bibliography`
- `screen-reading-considerations`
- `responsive-web-design`
- `how-to-work-with-a-designer`
- `the-copyright-status-of-fonts`
- `how-this-book-was-made`
- `typographic-humor`
- `common-accented-characters`
- `concourse-index`
- `contact`

### Commentary

- `commentary` *(section landing page)*
- `why-theres-no-e-book-or-pdf`
- `economics-year-one`
- `why-racket-why-lisp`
- `billionaires-typewriter`
- `the-infinite-pixel-screen`
- `effluents-influence-affluence`
- `vote-with-your-wallet`
- `drowning-the-crystal-goblet`
- `to-pay-or-not-to-pay`
- `the-scorpion-express`
- `are-two-spaces-better-than-one`
- `ligatures-in-programming-fonts-hell-no`
- `typography-2020`
- `the-cowardice-of-brave`
- `oscars-2020`
- `typography-2024`
- `mb-lectures-and-articles`

**Total expected pages: ~153** (count may vary slightly if the site has been updated since this manifest was created).

---

## Step-by-step instructions

### 1. Setup

```bash
mkdir -p ./sources-html/practical-typography
```

### 2. Download strategy

Write a Python or Node.js script (your choice) that does the following:

#### Phase 1 — Discovery

1. Fetch `https://practicaltypography.com/` (the index/TOC page).
2. Parse all `<a href="...">` links from the page.
3. Keep only links that:
   - Are relative paths ending in `.html` (e.g., `typography-in-ten-minutes.html`)
   - OR are relative paths without a scheme that point to the same domain
4. Discard:
   - Any link to an external domain (e.g., `mbtype.com`, `pollenpub.com`, `beautifulracket.com`, `typographyforlawyers.com`, `matthewbutterick.com`, `forums.matthewbutterick.com`)
   - Anchor-only links (`#something`)
   - Links to image files (`.png`, `.jpg`, `.gif`, `.svg`, `.webp`)
   - Links to non-HTML resources (`.css`, `.js`, `.zip`, `.pdf`)
5. Deduplicate the URL list.

#### Phase 2 — Cross-reference with manifest

6. Compare the discovered URLs against the manifest list above.
2. Log any pages that are in the manifest but NOT discovered (these must be added manually to the download queue).
3. Log any pages that were discovered but NOT in the manifest (download these too — the site may have new pages).
4. Build the final deduplicated download queue from the union of both lists.

#### Phase 3 — Download

10. Also save the index page itself as `index.html`.
2. For each page in the queue:
    - Fetch `https://practicaltypography.com/{slug}.html`
    - Save the raw HTML response to `./sources-html/practical-typography/{slug}.html`
    - **Respect the server:** Add a 1.5-second delay between requests.
    - Set a User-Agent header: `Mozilla/5.0 (compatible; DesignKnowledgeArchiver/1.0; personal-reference)`
    - Handle HTTP errors gracefully:
      - On 404: log the URL, skip it, continue.
      - On 429 (rate limit): wait 30 seconds, retry up to 3 times.
      - On 5xx: wait 10 seconds, retry up to 3 times.
      - On network error/timeout: retry up to 3 times with exponential backoff (5s, 15s, 45s).
3. Log each download as it completes: `[OK] typography-in-ten-minutes.html (23.4 KB)`

#### Phase 4 — Verification

13. After all downloads complete, run a verification pass:
    - Count total `.html` files in the output directory.
    - Compare the list of downloaded filenames against the manifest.
    - Report:
      - ✅ Total files downloaded
      - ✅ Files matching manifest
      - ⚠️ Manifest entries with no corresponding file (MISSING — needs investigation)
      - ℹ️ Extra files not in manifest (likely new content — fine to keep)
    - Check for any 0-byte files (failed downloads that created empty files) and flag them.
    - Check that each file contains `<html` or `<!DOCTYPE` (basic validity — not a server error page).

### 3. Output structure

```
./sources-html/practical-typography/
├── index.html                          # The main TOC page
├── typography-in-ten-minutes.html
├── summary-of-key-rules.html
├── introduction.html
├── how-to-use.html
├── ...
├── typography-2024.html
├── mb-lectures-and-articles.html
└── _download-report.txt                # Verification report (see below)
```

### 4. Generate a download report

Save a report as `./sources-html/practical-typography/_download-report.txt` containing:

- Timestamp of download run
- Total pages attempted
- Total pages successfully downloaded (with total size in KB)
- Any failed pages with error details
- Any manifest mismatches
- Any 0-byte or invalid files

---

## Important safeguards

1. **Do NOT download images, CSS, JS, or fonts.** We only want the HTML content for text extraction.
2. **Do NOT follow links to external domains** — only `practicaltypography.com`.
3. **Do NOT recursively spider the entire site.** Use the TOC + manifest as the source of truth. Only follow one level of internal links beyond the TOC to catch any sub-pages that might not be directly linked from the index.
4. **Do NOT make concurrent requests.** Download sequentially with the 1.5-second delay.
5. **Do NOT overwrite existing files** without checking — if the script is re-run, skip files that already exist and are non-empty (idempotent runs).
6. **Do NOT strip or modify the HTML content.** Save the raw response body exactly as received.
7. **Handle encoding properly.** The site likely uses UTF-8. Save files with the encoding specified in the response headers, defaulting to UTF-8.

---

## Success criteria

The task is complete when:

- [ ] The output directory contains ~150+ `.html` files
- [ ] Every entry in the manifest has a corresponding non-empty file
- [ ] The `_download-report.txt` shows 0 missing manifest entries
- [ ] No 0-byte files exist
- [ ] The index page is saved as `index.html`
