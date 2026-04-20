# Prompt: Prepare EPUB-Converted Source for Indexing (v2)

Use this prompt with Claude Code to prepare an EPUB-converted book for concept extraction or full-text indexing.

**v2 Changes (from v1):**

- Updated all paths to the unified `ai-engineering` repo layout: per-knowledge-base under `knowledge/<kb>/`, with sources split by format (`sources/md/`, `sources/epub/`).
- Raw EPUBs now live at `knowledge/<kb>/sources/epub/<SourceSlug>/`; converted markdown lands at `knowledge/<kb>/sources/md/<SourceSlug>/`.
- Helper scripts continue to live in the project-root `scripts/` directory (shared across knowledge bases); only the `sources-md/` → `knowledge/<kb>/sources/md/` path for content changed.
- "What Happens Next" reference updated to the v3.2 extraction guide.
- No changes to the processing logic (pandoc conversion, heading-based chapter detection, splitting) — only paths.

---

## Background: Where Things Live

All extraction work lives under a per-knowledge-base directory, `knowledge/<kb>/`, in the unified `ai-engineering` repo. The knowledge-base slug (`<kb>`) is a short name for the domain — for example, `go`, `js`, `rust`, `design`, `biome`, `deno`, `tailwindcss`.

For an EPUB-origin source:

```
<repo-root>/
├── knowledge/<kb>/
│   └── sources/
│       ├── epub/
│       │   └── <SourceSlug>/
│       │       └── book.epub        # the original EPUB (preserved)
│       └── md/
│           └── <SourceSlug>/
│               ├── book.md          # pandoc output
│               ├── media/
│               │   └── media/       # pandoc --extract-media nesting
│               └── NN-*.md          # chapter files (produced by this prompt)
└── scripts/                         # shared across all knowledge bases
    ├── process-epub.sh              # EPUB → book.md via pandoc
    ├── fix-neo-riemannian-images.py # example (reference implementation)
    ├── split-neo-riemannian.py      # example (reference implementation)
    ├── fix-<SourceSlug>-images.py   # produced by this prompt
    └── split-<SourceSlug>.py        # produced by this prompt
```

Before running this prompt, you should have already run the EPUB→Markdown conversion (`scripts/process-epub.sh`) so that `book.md` and the `media/` directory exist under `knowledge/<kb>/sources/md/<SourceSlug>/`.

---

## Instructions to Give Claude Code

Copy and paste the following prompt, replacing `<kb>` with your knowledge-base slug and `<SourceSlug>` with your actual source slug:

---

### PROMPT START

I have a book that was converted from EPUB to Markdown using pandoc (via `scripts/process-epub.sh`). The files are currently organized in this structure:

```
./knowledge/<kb>/sources/md/<SourceSlug>/
  ├── book.md              (complete book in one file)
  └── media/
      └── media/           (extracted media from pandoc --extract-media)
          ├── cover-epub.jpg
          ├── file0.svg
          ├── file1.svg
          └── ... (more SVG/image files)
```

The original EPUB lives at `./knowledge/<kb>/sources/epub/<SourceSlug>/book.epub` (do not modify it — it is preserved so the conversion can be re-run if needed).

I need you to prepare this source for further processing in three steps:

## Step 1: Fix Image References

The `book.md` file currently has image references with full paths from the project root, like:

```markdown
![](knowledge/<kb>/sources/md/<SourceSlug>/media/media/file0.svg){height="24"}
```

These need to be updated to use relative paths from within the source directory:

```markdown
![](./media/media/file0.svg){height="24"}
```

**Task 1a: Create a Python script**

- Script name: `scripts/fix-<SourceSlug>-images.py`
- The script should:
  - Read `knowledge/<kb>/sources/md/<SourceSlug>/book.md`
  - Find all image references containing the full path `knowledge/<kb>/sources/md/<SourceSlug>/media/`
  - Replace them with `./media/`
  - Write the updated content back to `book.md`
  - Print a summary (number of references updated)
- You can use `scripts/fix-neo-riemannian-images.py` as a reference implementation — copy its structure and adapt `MD_DIR` and the regex to match this source's image reference pattern. (Note: the reference script targets the PDF `_page_` pattern; for EPUB you'll be matching the full project-relative path that pandoc emits.)

**Task 1b: Run the script**

- Execute the script you just created
- Verify the output shows the expected number of image references updated

## Step 2: Analyze Book Structure from Markdown Headings

Since this source was converted from EPUB (not PDF), there is no `metadata.json` TOC file. Chapter structure must be derived from the Markdown headings themselves.

**Task 2a: Scan for chapter headings**

- Read `knowledge/<kb>/sources/md/<SourceSlug>/book.md`
- Identify all top-level chapter headings (lines matching `# N Title` pattern, where N is a chapter number)
- Distinguish between:
  - Title/cover content (before the first numbered chapter)
  - Table of contents (the inline TOC that EPUB conversions often produce)
  - Numbered chapters (the actual content chapters)
- For each chapter heading, extract:
  - Chapter number
  - Chapter title
  - Markdown line number
- Report what you found:
  - Total chapter headings detected
  - List of chapters with their numbers, titles, and line numbers
  - Any unusual patterns or edge cases (e.g., "(bonus)" chapters, unnumbered sections)

**Task 2b: Create chapter mapping**

- Build a mapping of all chapters:
  - Chapter number → Title → Markdown line number
- Identify frontmatter content (everything before chapter 1)
- Note any non-chapter top-level headings (title pages, TOC, etc.)
- Report the complete mapping

## Step 3: Split Book into Chapters

After analyzing the structure, split `book.md` into individual chapter files using the mapping you created.

**Task 3a: Create a chapter-splitting Python script**

- Script name: `scripts/split-<SourceSlug>.py`
- The script should:
  - Read `knowledge/<kb>/sources/md/<SourceSlug>/book.md`
  - Use the chapter mapping from Step 2b
  - Extract frontmatter (everything before the first numbered chapter) to: `knowledge/<kb>/sources/md/<SourceSlug>/00-frontmatter.md`
  - Extract each chapter to a separate file: `knowledge/<kb>/sources/md/<SourceSlug>/<NN>-<chapter-slug>.md`
    - `<NN>` is zero-padded chapter number (01, 02, ..., 10, 11, etc.)
    - `<chapter-slug>` is a slugified version of the chapter title (lowercase, hyphenated, ASCII-only)
    - Limit slug length to 50 characters if needed
  - Each chapter file should include:
    - A YAML metadata header with: chapter number, title, markdown line number
    - The complete chapter content (including the original heading)
  - Print a summary showing:
    - Book frontmatter extraction confirmation
    - List of all chapter files created with: filename, line count
- You can use `scripts/split-neo-riemannian.py` as a reference implementation. Important adaptations for EPUB sources: (1) the reference script uses an "Abstract and Keywords" marker specific to an academic handbook — replace this with heading-based detection (e.g., `# N Title`) for your EPUB; (2) update `SOURCE_FILE` and `OUTPUT_DIR` to the `knowledge/<kb>/sources/md/<SourceSlug>/` layout; (3) write chapter files directly in that directory (no `chapters/` subdir); (4) emit a YAML frontmatter block as specified below instead of the reference script's `<!-- Original line: N -->` HTML comment.

**Metadata header format:**

```markdown
---
title: [full chapter title]
chapter_number: [integer]
book_md_line: [line number in book.md]
source_format: epub
---

# N [Title]

[Chapter content starts here...]
```

**Task 3b: Run the chapter-splitting script**

- Execute the script you just created
- Verify the output:
  - Confirm frontmatter was extracted
  - Confirm all chapters were split correctly
  - Show the list of created files
  - Validate chapter count matches the detected headings

**Task 3c: Create validation report**

- Compare created chapter files against detected headings
- Report:
  - Total chapters detected: X
  - Total chapter files created: Y
  - Match status: ✓ or ✗
  - Any missing chapters or extra files

## Important Notes

- **No metadata.json**: Unlike PDF-converted sources, EPUB conversions don't produce a `metadata.json` with TOC metadata. Headings in `book.md` are the source of truth.
- **No PDF page numbers**: EPUBs don't have fixed page numbers. Use markdown line numbers for cross-referencing instead.
- **Image references**: After splitting, all chapter files will have image references pointing to `./media/media/` relative to the chapter file location. This is correct - don't change it.
- **EPUB artifacts**: The pandoc conversion may produce artifacts like:
  - Inline TOC with anchor links (`[]{#nav.xhtml}`, `[]{#ch001.xhtml_...}`)
  - Pandoc div markers (`::: {.section .level2}` / `::::`)
  - HTML attributes on headings (`{.title}`, `{.unnumbered}`, `{#anchor}`)
  - Raw HTML/SVG embedded in markdown
  - These should be **preserved as-is** during splitting (cleanup is a separate step)
- **No subdirectory**: Create all chapter files directly in `knowledge/<kb>/sources/md/<SourceSlug>/` - don't create a `chapters/` subdirectory.
- **Preserve content**: Don't modify chapter content except for adding the metadata header.
- **Don't touch the raw EPUB**: `knowledge/<kb>/sources/epub/<SourceSlug>/` is preserved for re-conversion; this prompt only operates on the `sources/md/` side.
- **Slug creation**: For slugifying chapter titles:
  - Convert to lowercase
  - Remove special characters (backticks, parentheses, etc.)
  - Replace spaces with hyphens
  - Limit to 50 characters
  - Strip trailing hyphens
- **Chapter heading pattern**: This book uses `# N Title` (e.g., `# 2 Type coercion in JavaScript`), not `# Chapter N: Title`. If your book uses a different pattern, adjust the detection logic accordingly.

## Expected Output

After all three steps complete, the directory structure should look like:

```
knowledge/<kb>/sources/md/<SourceSlug>/
├── book.md                            (updated with relative image paths)
├── media/                             (unchanged)
│   └── media/
│       ├── cover-epub.jpg
│       ├── file0.svg
│       └── ... (all images)
├── 00-frontmatter.md                  (NEW - title page, TOC, intro material)
├── 01-about-this-book.md              (NEW)
├── 02-type-coercion-in-javascript.md  (NEW)
└── ... (all other chapter files)

scripts/
├── fix-<SourceSlug>-images.py         (NEW)
└── split-<SourceSlug>.py              (NEW)
```

## Final Verification

After completing all three steps:

1. Show the total number of image references updated
2. Show the chapter mapping (number → title → line number → file)
3. Show the total number of chapter files created
4. Verify chapter count matches detected headings
5. Show a sample of the first chapter file (first 25 lines, showing metadata header)
6. Confirm that the source is ready for concept extraction or full-text indexing

### PROMPT END

---

## Usage Notes

1. **Replace `<kb>` and `<SourceSlug>`** with your actual values before sending the prompt
2. **Knowledge-base slug examples**: `go`, `js`, `rust`, `design`, `biome`, `deno`, `tailwindcss`
3. **Source slug examples**:
   - `deep-js`
   - `eloquent-js`
   - `exploring-js`
4. **Prerequisites**: Ensure the directory structure exists with `book.md` and `media/` directory under `knowledge/<kb>/sources/md/<SourceSlug>/` (produced by `scripts/process-epub.sh`)
5. **Model recommendation**: Sonnet is sufficient for this task (Opus not required)
6. **Expected time**: 5-10 minutes total for all three steps

## Example Usage

For the book "Deep JavaScript" with slug `deep-js` in the `js` knowledge base:

```
I have a book that was converted from EPUB to Markdown using pandoc (via `scripts/process-epub.sh`). The files are currently organized in this structure:

./knowledge/js/sources/md/deep-js/
  ├── book.md              (complete book in one file)
  └── media/
      └── media/           (extracted media from pandoc --extract-media)
          ├── cover-epub.jpg
          ├── file0.svg
          ├── file1.svg
          └── ... (22 SVG files + 1 cover JPG)

I need you to prepare this source for further processing in three steps:

[... rest of prompt ...]
```

## What Happens Next

After running this prompt, your source will be ready for:

1. **Concept extraction**: Use `docs/dev/concept-cards/0008-a-guide-for-parallel-concept-card-re-extraction-v3.2.md` (or the equivalent fresh-extraction guide) to extract concept cards into `knowledge/<kb>/concept-cards/<SourceSlug>/` (using line numbers instead of PDF pages — set `pdf_page: null` in frontmatter)
2. **Full-text indexing**: Use the individual chapter files for search/indexing systems
3. **Analysis**: Read individual chapters without loading the entire book

## Differences from PDF-Converted Sources

| Aspect | PDF (0005) | EPUB (this prompt) |
|--------|-----------|-------------------|
| Converter | Marker | pandoc |
| Raw source location | `sources/pdf/<SourceSlug>/` | `sources/epub/<SourceSlug>/` |
| Metadata file | `metadata.json` with TOC | None — headings are source of truth |
| Page numbers | PDF page numbers tracked | No page numbers (use line numbers) |
| Image format | JPEG (`_page_N_Picture_M.jpeg`) | SVG/JPG (`fileN.svg`) |
| Image path issue | Missing `./images/` prefix | Full project path instead of relative |
| Media directory | `images/` | `media/media/` (pandoc nesting) |
| Heading format | Varies by book | Typically clean from EPUB structure |
| Artifacts | OCR noise, page headers | Pandoc divs, anchor spans, HTML attrs |
| Frontmatter `pdf_page` | Integer from TOC | `null` |

## Troubleshooting

### Issue: Chapter heading pattern doesn't match `# N Title`

**Symptoms**: No chapters detected, or wrong lines matched

**Solution**: Ask Claude Code to:
- Show the first 20 top-level headings (`# ...`) from book.md
- Identify the actual pattern used
- Adjust the regex accordingly
- Common EPUB patterns: `# Chapter N: Title`, `# Part N`, `# N. Title`

### Issue: Image references use unexpected paths

**Symptoms**: Images not found after path fix

**Solution**: Ask Claude Code to:
- Show 10 sample image references from the original book.md
- Check what path pattern pandoc actually used
- Adjust the fix script regex to match the actual pattern
- Verify images exist at the corrected paths

### Issue: Duplicate chapter headings

**Symptoms**: The TOC section contains headings that look like chapter headings

**Solution**: EPUB conversions often include an inline TOC with the same heading text. The splitting script should:
- Identify the TOC section (usually between nav anchors)
- Skip headings within the TOC section
- Only split on headings in the actual content sections

### Issue: `media/media/` double nesting

**Symptoms**: pandoc creates `media/media/` instead of just `media/`

**Explanation**: This is normal pandoc behavior when using `--extract-media=DIR/media` — it creates a `media/` subdirectory within the specified directory. The image references in `book.md` will already point to the correct nested path.

### Issue: Special characters in chapter titles

**Solution**: The slugify function should handle this. Common cases in EPUB-converted books:
- Backticks in code references (`` `%` is a remainder operator ``)
- Parenthetical notes (`(bonus)`)
- Colons and other punctuation

### Issue: Scripts written to the wrong directory

**Cause**: Agent placed scripts under `knowledge/<kb>/scripts/` (legacy per-KB location) instead of the shared project-root `scripts/`

**Solution**:

- Spell out the full path (`scripts/fix-<SourceSlug>-images.py`) in the prompt
- Move any mis-located scripts into the top-level `scripts/` directory and delete the empty per-KB `scripts/` folder if one was created

## Notes

- This is a **preparatory step** before concept extraction
- The Python scripts are saved under the project-root `scripts/` directory (shared across knowledge bases) for future use and documentation
- The original `book.md` is modified (image paths updated) but can be regenerated from the EPUB at `knowledge/<kb>/sources/epub/<SourceSlug>/book.epub` by re-running `scripts/process-epub.sh`
- Chapter files can be regenerated by re-running the split script
- This process is **non-destructive** relative to the original EPUB source
- Line numbers serve as the cross-referencing mechanism in place of PDF page numbers
- The metadata headers in chapter files will be used by concept extraction to populate source location fields (with `pdf_page: null`)

---

## Version History

- **v1**: Original prompt (flat project-root layout with `sources-md/` for content and top-level `scripts/` for helpers)
- **v2**: Updated content paths for the unified `ai-engineering` repo (`knowledge/<kb>/sources/md/<SourceSlug>/`, raw EPUBs at `knowledge/<kb>/sources/epub/<SourceSlug>/`). Scripts remain in the project-root `scripts/` directory (shared across knowledge bases). Added background section explaining the layout; pointed the Task-1a and Task-3a references at concrete example scripts (`scripts/fix-neo-riemannian-images.py`, `scripts/split-neo-riemannian.py`); updated "What Happens Next" to point at the v3.2 extraction guide. No changes to processing logic.
