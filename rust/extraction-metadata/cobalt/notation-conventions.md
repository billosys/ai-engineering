# Notation Conventions for Cobalt

## Frontmatter Delimiters

Cobalt frontmatter uses YAML format delimited by triple dashes:

```
---
title: My Page Title
layout: default.liquid
is_draft: false
---
Content goes here...
```

## Liquid Template Syntax

### Output Tags (Variable Interpolation)
```
{{ variable_name }}
{{ page.title }}
{{ site.base_url }}
```

### Logic Tags (Control Flow and Execution)
```
{% if condition %}...{% endif %}
{% for item in collection %}...{% endfor %}
{% include "partial.liquid" %}
{% highlight LANG %}...{% endhighlight %}
```

### Raw Tags (Escape Liquid Processing)
```
{% raw %}{{ this will not be processed }}{% endraw %}
```

### Comment Tags
```
{% comment %}This is not rendered{% endcomment %}
```

## Configuration File Format

Site configuration uses YAML in `_cobalt.yml`:

```yaml
source: "."
destination: _site
site:
  title: My Site
  base_url: http://example.com
posts:
  dir: posts
  rss: rss.xml
```

## Permalink Template Variables

Permalink templates use Liquid-style double braces within the `permalink` frontmatter field:

```yaml
permalink: /{{categories}}/{{slug}}
permalink: /{{year}}/{{month}}/{{slug}}
permalink: path  # Built-in style
```

## File Naming Conventions

### Content Files
- `slug.md` or `slug.liquid` — standard page/post
- `YYYY-MM-DD-slug.md` — date-prefixed post (recognized on build)

### Template Files
- `name.liquid` — layout and include files use `.liquid` extension

### Special Directories (prefixed with `_`)
- `_cobalt.yml` — site configuration
- `_layouts/` — layout templates
- `_includes/` — reusable template snippets
- `_data/` — data files (YAML, JSON, TOML)
- `_sass/` — Sass/SCSS partials
- `_site/` — build output
- `_defaults/` — templates for `cobalt new`
- `_drafts/` — draft posts
- `_syntaxes/` — custom syntax highlighting definitions

## CLI Command Format

```
cobalt <command> [options]
cobalt init [directory]
cobalt build [-d destination]
cobalt serve [--host HOST] [--port PORT] [--drafts]
cobalt new "Title" [--file path]
cobalt publish <path>
cobalt clean
cobalt debug <subcommand>
```

## Liquid Variable Access Patterns

### Dot Notation
```
{{ page.title }}
{{ site.data.animals.dogs }}
{{ collections.posts.title }}
```

### Array Iteration
```
{% for post in collections.posts.pages %}
  {{ post.title }}
{% endfor %}
```

## Sass Output Styles

Four options for CSS output: `Nested`, `Expanded`, `Compact`, `Compressed`

## Date Format

Published dates use the format: `YYYY-MM-DD HH:MM:SS TZ`
Example: `2016-01-01 21:00:00 +0100`
