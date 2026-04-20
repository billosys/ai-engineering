---
# === CORE IDENTIFICATION ===
concept: Array Filters
slug: array-filters

# === CLASSIFICATION ===
category: liquid-filters
subcategory: null
tier: intermediate

# === PROVENANCE ===
source: "Cobalt Static Site Generator Documentation"
source_slug: cobalt
authors: "Cobalt contributors (cobalt-org)"
chapter: "Liquid Standard Library"
chapter_number: null
pdf_page: null
section: "Array Filters"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "collection filters"
  - "list filters"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - output-tags
  - liquid-template-language
extends: []
related:
  - string-filters
  - math-filters
  - for-block
  - data-files
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a Liquid filter?"
---

# Quick Definition

Array filters are Liquid filters that operate on arrays (lists), providing operations for sorting, filtering, transforming, combining, and extracting elements. They are applied within output tags using the pipe syntax.

# Core Definition

Array filters are part of the Liquid standard library implemented in the `liquid_lib` crate (source: `stdlib/filters/array/`). They operate on array values and enable manipulation of collections without explicit loop logic. Array filters can be chained together and are commonly used to transform data file content and collections before rendering. Some filters (like `sort`, `where`, `map`) are essential for data-driven templates. (Source: liquid_lib stdlib array filters)

# Prerequisites

- **[Output Tags](/concept-cards/cobalt/output-tags.md)** -- Filters are applied within output tags.
- **[Liquid Template Language](/concept-cards/cobalt/liquid-template-language.md)** -- Understanding the filter pipe syntax.

# Key Properties

The following array filters are available in the liquid_lib standard library:

**Element Access:**
1. **`first`**: Returns the first element of an array. `{{ array | first }}`.
2. **`last`**: Returns the last element of an array. `{{ array | last }}`.
3. **`slice`**: Returns a subset of an array starting at an index. `{{ array | slice: 1, 3 }}` returns 3 elements starting at index 1.

**Sorting:**
4. **`sort`**: Sorts an array. `{{ array | sort }}`. Can sort by a property: `{{ array | sort: "name" }}`.
5. **`sort_natural`**: Sorts an array case-insensitively. `{{ array | sort_natural }}`.
6. **`reverse`**: Reverses the order of an array. `{{ array | reverse }}`.

**Filtering and Deduplication:**
7. **`compact`**: Removes nil values from an array. `{{ array | compact }}`.
8. **`uniq`**: Removes duplicate elements from an array. `{{ array | uniq }}`.
9. **`where`**: Filters an array by a property value. `{{ array | where: "published", true }}`.

**Transformation:**
10. **`map`**: Extracts a property from each element, creating a new array. `{{ array | map: "title" }}` returns an array of titles.
11. **`join`**: Joins array elements into a string with a delimiter. `{{ array | join: ", " }}`.

**Combination:**
12. **`concat`**: Concatenates two arrays. `{{ array1 | concat: array2 }}`.

# Construction / Recognition

## To Construct/Create:
1. Apply an array filter using the pipe after an array value: `{{ array | filter_name }}`.
2. For filters with parameters, use colon syntax: `{{ array | sort: "property" }}`.
3. Chain multiple filters: `{{ array | sort | reverse | first }}`.

## To Identify/Recognize:
1. Look for pipe characters followed by array filter names in output tags.
2. Array filters typically operate on list/array values (from data files, tags, categories).

# Context & Application

- **Typical contexts**: Manipulating data file arrays, filtering post collections, transforming lists for display.
- **Common applications**: Sorting blog posts by date, extracting unique tags, filtering items by property, joining tags into a comma-separated string.

# Examples

**Example 1** (source: Liquid Standard Library): Sorting and filtering an array:
```liquid
{% assign sorted_posts = site.data.posts | sort: "date" | reverse %}
{% for post in sorted_posts %}
  <li>{{ post.title }}</li>
{% endfor %}
```

**Example 2** (source: Liquid Standard Library): Extracting unique tags:
```liquid
{% assign all_tags = site.data.posts | map: "tags" | compact | uniq | sort %}
```

**Example 3** (source: Liquid Standard Library): Joining array elements:
```liquid
{{ page.tags | join: ", " }}
```

# Relationships

## Builds Upon
- **[Output Tags](/concept-cards/cobalt/output-tags.md)** -- Filters are applied within output tags.
- **[Liquid Template Language](/concept-cards/cobalt/liquid-template-language.md)** -- Filter pipe syntax.

## Enables
- Data manipulation and transformation in templates.

## Related
- **[String Filters](/concept-cards/cobalt/string-filters.md)** -- Filters for text operations.
- **[Math Filters](/concept-cards/cobalt/math-filters.md)** -- Filters for numeric operations.
- **[For Block](/concept-cards/cobalt/for-block.md)** -- Arrays processed by filters are often iterated with for.
- **[Data Files](/concept-cards/cobalt/data-files.md)** -- Data files often provide the arrays that filters operate on.

## Contrasts With
- None directly.

# Common Errors

- **Error**: Using an array filter on a non-array value.
  **Correction**: Ensure the input is an array. Use `split` to convert a string to an array first if needed.

- **Error**: Expecting `where` to work with complex conditions.
  **Correction**: The `where` filter only supports simple property-value equality matching. For complex filtering, use a `for` loop with `if` conditions.

# Common Confusions

- **Confusion**: Confusing `map` with `where`.
  **Clarification**: `map` extracts a single property from each element, creating a new array of those values. `where` filters elements based on a property matching a value, keeping the full elements that match.

# Source Reference

Liquid Standard Library, array filter module. Source: liquid_lib rustdoc (stdlib/filters/array/).

# Verification Notes

- Definition source: liquid_lib stdlib array filter structs
- Confidence rationale: All filters verified in the liquid_lib stdlib struct list.
- Uncertainties: None for filter names; specific parameter details may vary.
- Cross-reference status: Verified against liquid_lib stdlib index.
