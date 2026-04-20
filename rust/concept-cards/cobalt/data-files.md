---
# === CORE IDENTIFICATION ===
concept: Data Files
slug: data-files

# === CLASSIFICATION ===
category: data-files
subcategory: null
tier: intermediate

# === PROVENANCE ===
source: "Cobalt Static Site Generator Documentation"
source_slug: cobalt
authors: "Cobalt contributors (cobalt-org)"
chapter: "Data Files"
chapter_number: null
pdf_page: null
section: "Data Files"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "data directory files"
  - "_data files"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - site-variable
  - for-block
extends: []
related:
  - template-variables
  - cobalt-configuration-file
  - directory-structure
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a data file in Cobalt?"
  - "How do data files relate to the site.data variable?"
  - "How do I use data files in templates?"
---

# Quick Definition

Data files are YAML, JSON, or TOML files placed in the `_data` directory that Cobalt reads and merges into the `site.data` Liquid variable. They allow structured data to be separated from templates and accessed as `site.data.<DIR>.<FILE>`.

# Core Definition

Cobalt reads data from any YAML (`.yml`/`.yaml`), JSON (`.json`), and TOML (`.toml`) files in the `_data` directory and merges them into the `site.data` variable. The directory structure within `_data` is preserved in the variable hierarchy: a file at `_data/animals/dogs.yml` becomes accessible as `site.data.animals.dogs` in Liquid templates. This mechanism allows template authors to separate structured data from presentation logic, making it possible to iterate over data collections, look up values, and reuse data across multiple templates without embedding it in frontmatter or configuration. (Source: Cobalt Data Files documentation)

# Prerequisites

- **[Site Variable](/concept-cards/cobalt/site-variable.md)** -- Data files are accessed through `site.data`.
- **[For Block](/concept-cards/cobalt/for-block.md)** -- Data is typically iterated with `{% for %}` loops.

# Key Properties

1. **Location**: Placed in the `_data` directory.
2. **Supported formats**: YAML, JSON, and TOML.
3. **Path-based access**: Directory structure maps to dot notation: `_data/dir/file.yml` becomes `site.data.dir.file`.
4. **Merge behavior**: Data files are merged with `site: data` from `_cobalt.yml`.
5. **Available globally**: Data is accessible in all templates, layouts, and includes.

# Construction / Recognition

## To Construct/Create:
1. Create the `_data` directory in the project root.
2. Create subdirectories as needed to organize data.
3. Create YAML, JSON, or TOML files with structured data.
4. Access the data in templates as `site.data.<path>.<filename>`.

## To Identify/Recognize:
1. Files with `.yml`, `.yaml`, `.json`, or `.toml` extensions in the `_data` directory.
2. Template references using `site.data.*` paths.

# Context & Application

- **Typical contexts**: Storing lists, lookup tables, configuration data, and structured content that should be accessible across templates.
- **Common applications**: Navigation menus, team member lists, product catalogs, site metadata, any structured data that multiple pages need to access.

# Examples

**Example 1** (source: Cobalt Data Files documentation): A data file `_data/animals/dogs.yml`:
```yml
- name: Corgi
- name: Malamute
```

Accessed in a template:
```html
<ul>
{% for breed in site.data.animals.dogs %}
  <li>{{ breed.name }}</li>
{% endfor %}
</ul>
```

# Relationships

## Builds Upon
- **[Site Variable](/concept-cards/cobalt/site-variable.md)** -- Data files populate `site.data`.
- **[For Block](/concept-cards/cobalt/for-block.md)** -- Data is commonly iterated with for loops.

## Enables
- Data-driven templates -- allowing structured data to drive page content without hardcoding.

## Related
- **[Template Variables](/concept-cards/cobalt/template-variables.md)** -- Data files extend the variable system.
- **[Cobalt Configuration File](/concept-cards/cobalt/cobalt-configuration-file.md)** -- Inline data can also be defined under `site: data:`.
- **[Directory Structure](/concept-cards/cobalt/directory-structure.md)** -- The `_data` directory is a standard part of the project structure.

## Contrasts With
- None directly.

# Common Errors

- **Error**: Placing data files outside the `_data` directory and expecting them to be available in `site.data`.
  **Correction**: Only files in the `_data` directory are automatically loaded into `site.data`.

- **Error**: Using an unsupported file format (e.g., XML or CSV) in the `_data` directory.
  **Correction**: Only YAML, JSON, and TOML files are supported.

# Common Confusions

- **Confusion**: Thinking data files and frontmatter data serve the same purpose.
  **Clarification**: Data files provide site-wide data accessible via `site.data`. Frontmatter data is page-specific and accessible via `page.data`. Data files are global; frontmatter is local to a single page.

# Source Reference

Data Files documentation, "Data Files" and "Example" sections. Source: Cobalt documentation.

# Verification Notes

- Definition source: Direct from Cobalt Data Files documentation
- Confidence rationale: The documentation provides a clear example with path mapping explanation.
- Uncertainties: None.
- Cross-reference status: Verified against Variables documentation which describes `site.data`.
