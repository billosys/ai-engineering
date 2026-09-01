# Prompt: Prepare PDF-Converted Source for Indexing

Use this prompt with Claude Code to prepare a PDF-converted book for concept extraction or full-text indexing.

---

## Instructions to Give Claude Code

Copy and paste the following prompt, replacing `<SourceSlug>` with your actual source slug:

---

### PROMPT START

I have a book that was converted from PDF to Markdown using a converter tool (like Marker). The files are currently organized in this structure:

```
./sources-md/<SourceSlug>/
  ├── book.md              (complete book in one file)
  ├── metadata.json            (metadata from converter with TOC)
  └── images/              (directory with all extracted images)
      ├── _page_1_Picture_1.jpeg
      ├── _page_2_Picture_1.jpeg
      └── ... (many more images)
```

I need you to prepare this source for further processing in three steps:

## Step 1: Fix Image References

The `book.md` file currently has image references that look like:

```markdown
![](_page_5_Picture_1.jpeg)
```

These need to be updated to point to the `./images/` subdirectory:

```markdown
![](./images/_page_5_Picture_1.jpeg)
```

**Task 1a: Create a Python script**

- Script name: `scripts/fix-<SourceSlug>-images.py`
- The script should:
  - Read `sources-md/<SourceSlug>/book.md`
  - Find all image references matching the pattern `![](_page_`
  - Replace them with `![](./images/_page_`
  - Write the updated content back to `book.md`
  - Print a summary (number of references updated)
- You can use the following script as an example, just be sure to make the changes necessary to work for the book you are processing: `scripts/fix-neo-riemannian-images.py`

**Task 1b: Run the script**

- Execute the script you just created
- Verify the output shows the expected number of image references updated

## Step 2: Analyze Book Structure Using metadata.json

Before splitting, extract chapter information from the converter's metadata.

**Task 2a: Parse metadata.json table of contents**

- Read `sources-md/<SourceSlug>/metadata.json`
- Extract the `table_of_contents` array
- Identify chapter entries (look for patterns like "Chapter X", "Abstract and Keywords", or other chapter markers)
- For each chapter entry, extract:
  - Chapter title
  - PDF page number (`page_id`)
  - Position in TOC
- Report what you found:
  - Total TOC entries
  - Total chapter entries detected
  - List of chapters with their titles and PDF page numbers
  - Any unusual patterns or edge cases

**Task 2b: Create chapter mapping**

- Cross-reference metadata.json TOC with actual headings in `book.md`
- For each chapter:
  - Find the corresponding heading line in book.md
  - Record: chapter number, title, PDF page, markdown line number
  - Note any chapters in metadata.json that don't appear in book.md (or vice versa)
- Report the complete mapping:
  - Chapter number → Title → PDF page → Markdown line
  - Any discrepancies between metadata.json and book.md

## Step 3: Split Book into Chapters

After analyzing the structure, split `book.md` into individual chapter files using the mapping you created.

**Task 3a: Create a chapter-splitting Python script**

- Script name: `scripts/split-<SourceSlug>.py`
- The script should:
  - Read `sources-md/<SourceSlug>/metadata.json` to get PDF page numbers
  - Read `sources-md/<SourceSlug>/book.md` to get content
  - Use the chapter mapping from Step 2b
  - Extract frontmatter (everything before the first chapter) to: `sources-md/<SourceSlug>/00-frontmatter.md`
  - Extract each chapter to a separate file: `sources-md/<SourceSlug>/<NN>-<chapter-slug>.md`
    - `<NN>` is zero-padded chapter number (01, 02, ..., 10, 11, etc.)
    - `<chapter-slug>` is a slugified version of the chapter title (lowercase, hyphenated, ASCII-only)
    - Limit slug length to 50 characters if needed
  - Each chapter file should include:
    - A YAML chapter metadata header with: chapter number, title, PDF page number, markdown line number
    - The complete chapter content
  - Print a summary showing:
    - Book frontmatter extraction confirmation
    - List of all chapter files created with: filename, PDF page, line count
- You can use the following script as an example, just be sure to make the changes necessary to work for the book you are processing: `scripts/split-neo-riemannian.py`

**Metadata header format:**

```markdown
---
title: [full chapter name]
chapter_number: [integer]
pdf_page: [page number from metadata.json]
book_md_line: [line number in book.md]
---

# Chapter X: [Title]

[Chapter content starts here...]
```

**Task 3b: Run the chapter-splitting script**

- Execute the script you just created
- Verify the output:
  - Confirm frontmatter was extracted
  - Confirm all chapters were split correctly
  - Show the list of created files with PDF page mappings
  - Validate chapter count matches metadata.json TOC count

**Task 3c: Create validation report**

- Compare created chapter files against metadata.json TOC
- Report:
  - Total chapters in metadata.json: X
  - Total chapter files created: Y
  - Match status: ✓ or ✗
  - Any missing chapters or extra files

## Important Notes

- **metadata.json is the source of truth** for PDF page numbers - always use it when available
- **Fallback**: If metadata.json doesn't have useful TOC data, fall back to regex pattern matching (see Troubleshooting)
- **Image references**: After splitting, all chapter files will have image references pointing to `./images/` relative to the chapter file location. This is correct - don't change it.
- **No subdirectory**: Create all chapter files directly in `sources-md/<SourceSlug>/` - don't create a `chapters/` subdirectory.
- **Preserve content**: Don't modify chapter content except for adding the metadata header.
- **Slug creation**: For slugifying chapter titles:
  - Convert to lowercase
  - Remove special characters
  - Replace spaces with hyphens
  - Limit to 50 characters
  - Strip trailing hyphens
- **PDF page tracking**: The PDF page numbers will be crucial for concept extraction - ensure they're accurate

## Expected Output

After all three steps complete, the directory structure should look like:

```
sources-md/<SourceSlug>/
├── book.md                        (updated with image paths)
├── metadata.json                      (unchanged)
├── images/                        (unchanged)
│   └── ... (all images)
├── 00-frontmatter.md             (NEW - includes PDF page reference)
├── 01-<first-chapter-slug>.md    (NEW - includes PDF page reference)
├── 02-<second-chapter-slug>.md   (NEW - includes PDF page reference)
└── ... (all other chapter files with PDF page references)

scripts/
├── fix-<SourceSlug>-images.py    (NEW)
└── split-<SourceSlug>.py         (NEW)
```

## Final Verification

After completing all three steps:

1. Show the total number of image references updated
2. Show the chapter mapping (number → title → PDF page → file)
3. Show the total number of chapter files created
4. Verify chapter count matches metadata.json TOC
5. Show a sample of the first chapter file (first 25 lines, showing metadata header)
6. Confirm that the source is ready for concept extraction or full-text indexing

### PROMPT END

---

## Usage Notes

1. **Replace `<SourceSlug>`** with your actual source slug before sending the prompt
2. **Source slug examples**:
   - `21st-century-classroom`
   - `neo-riemannian-handbook`
   - `quantum-mechanics-sakurai`
3. **Prerequisites**: Ensure the directory structure exists with `book.md`, `metadata.json`, and `images/` directory
4. **Model recommendation**: Sonnet is sufficient for this task (Opus not required)
5. **Expected time**: 5-10 minutes total for all three steps

## Example Usage

For a book with slug `music-theory-basics`:

```
I have a book that was converted from PDF to Markdown using a converter tool (like Marker). The files are currently organized in this structure:

./sources-md/music-theory-basics/
  ├── book.md              (complete book in one file)
  ├── metadata.json            (metadata from converter with TOC)
  └── images/              (directory with all extracted images)
      ├── _page_1_Picture_1.jpeg
      ├── _page_2_Picture_1.jpeg
      └── ... (many more images)

I need you to prepare this source for further processing in three steps:

[... rest of prompt ...]
```

## What Happens Next

After running this prompt, your source will be ready for:

1. **Concept extraction**: Use `parallel-concept-extraction-template-v2.md` to extract concept cards with PDF page references
2. **Full-text indexing**: Use the individual chapter files for search/indexing systems
3. **Analysis**: Read individual chapters without loading the entire book
4. **Academic citation**: Reference original PDF pages in concept cards and documentation

## Troubleshooting

### Issue: metadata.json has no useful TOC data

**Symptoms**: The table_of_contents array is empty or doesn't contain chapter entries

**Solution**: Ask Claude Code to fall back to regex pattern matching:

- Use the original method: scan book.md for chapter heading patterns
- Look for: `# Chapter 1`, `# <span...>Chapter 1`, `# **Chapter 1**`, etc.
- Manually create the chapter mapping without PDF page numbers
- Continue with splitting using markdown line numbers only

### Issue: TOC entries don't match book.md headings

**Symptoms**: metadata.json says 35 chapters but book.md only has 30 chapter headings

**Solution**:

- Compare the mismatches - show examples
- Check if TOC includes non-chapter sections (preface, appendices, index)
- Manually identify which TOC entries are actual chapters vs. front/back matter
- Adjust the chapter detection logic accordingly

### Issue: No chapters detected in metadata.json

**Symptoms**: No entries in TOC match common chapter patterns

**Solution**: Ask Claude Code to:

- Show the first 20 TOC entries from metadata.json
- Identify what pattern the source uses for divisions (e.g., "Part X", "Section X", "Abstract and Keywords")
- Manually specify the pattern to look for

### Issue: Chapter titles too long for filenames

**Solution**: The script already limits slugs to 50 characters. If still too long, ask Claude Code to shorten further.

### Issue: Image references not all fixed

**Solution**: There may be variant image reference patterns. Ask Claude Code to:

- Check for other patterns like `![](page_X` or `![img](_page_X`
- Update the script to handle all variants

### Issue: Special characters in chapter titles

**Solution**: The slugify function should handle this, but if issues occur, ask Claude Code to:

- Show examples of problematic titles
- Enhance the slugify function to handle those cases

### Issue: PDF page numbers seem wrong

**Symptoms**: Chapter 1 shows PDF page 150, which seems incorrect

**Solution**:

- Check if metadata.json page_id is 0-indexed or 1-indexed
- Check if PDF includes many front-matter pages before Chapter 1
- Verify a few PDF page numbers manually by checking book.md content
- Adjust if converter used a different page numbering scheme

## Notes

- This is a **preparatory step** before concept extraction
- All three Python scripts are saved for future use and documentation
- The original `book.md` is modified (image paths updated) but can be regenerated from the PDF if needed
- Chapter files can be regenerated by re-running the split script
- This process is **non-destructive** - you can always reconvert the PDF if something goes wrong
- **PDF page numbers are critical** - they enable academic citation and cross-referencing with the original source
- The metadata headers in chapter files will be used by concept extraction to populate PDF page fields

## Benefits of Using metadata.json

- **More reliable**: No regex pattern matching needed
- **Complete data**: Get PDF page numbers automatically
- **Validation**: Cross-check against actual chapter count
- **Academic rigor**: Enable proper citations with original page numbers
- **Error detection**: Catch missing or extra chapters immediately
