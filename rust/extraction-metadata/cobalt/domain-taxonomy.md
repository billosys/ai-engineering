# Domain Taxonomy for Cobalt

## Categories

- **cli**: Command-line interface commands and usage (`cobalt init`, `cobalt build`, etc.)
- **project-structure**: Directory layout, file organization, and naming conventions
- **content**: Pages, posts, drafts, and content processing pipeline
- **templating**: Liquid templates, layouts, includes, and template variables
- **frontmatter**: YAML frontmatter fields, defaults, and metadata
- **configuration**: `_cobalt.yml` settings and site-wide options
- **permalink**: URL generation, permalink templates, and pretty URLs
- **pagination**: Post pagination, paginator variables, and indexing
- **data-files**: External data (YAML/JSON/TOML) and the `site.data` variable
- **assets**: Static files, Sass/SCSS compilation, and asset handling
- **deployment**: Building for production, GitHub Pages, GitLab CI, self-hosted
- **liquid-basics**: Core Liquid syntax: output tags, logic tags, variables, operators
- **liquid-filters**: Built-in Liquid filters (string, array, math, HTML, URL, date)
- **liquid-tags**: Built-in Liquid tags (assign, capture, cycle, include, render, increment)
- **liquid-blocks**: Liquid control flow blocks (if, unless, for, case, tablerow, raw, comment)
- **liquid-advanced**: Liquid partials, custom filters, value types, parser/runtime API
- **rust-api**: Cobalt and Liquid Rust API types, traits, and programmatic usage
- **feeds**: RSS and JSON Feed generation

## Tiers

- **foundational**: No prerequisites from this source. Entry-point concepts that a newcomer must learn first.
  - Examples: What is Cobalt, installation, basic CLI commands, what is Liquid, directory structure
- **intermediate**: Requires foundational concepts. Building on basics to create functional sites.
  - Examples: Frontmatter fields, layouts, includes, template variables, data files, permalink templates, pagination
- **advanced**: Requires intermediate concepts. Deep customization, Rust API, deployment, complex Liquid.
  - Examples: Custom Liquid filters in Rust, Liquid parser/runtime API, pagination with date indexing, deployment pipelines, Sass configuration, Cobalt Rust model types
