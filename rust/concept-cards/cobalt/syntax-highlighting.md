---
# === CORE IDENTIFICATION ===
concept: Syntax Highlighting
slug: syntax-highlighting

# === CLASSIFICATION ===
category: content
tier: intermediate

# === PROVENANCE ===
source: "Cobalt Static Site Generator Documentation"
source_slug: cobalt
authors: "Cobalt contributors (cobalt-org)"
chapter: "Docs::Pages"
chapter_number: null
pdf_page: null
section: "Syntax Highlighting"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "code highlighting"
  - "code block highlighting"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - page
  - cobalt-configuration-file
extends:
  - page
related:
  - liquid-template-language
  - post
  - cobalt-build
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I add syntax highlighting to code blocks?"
---

# Quick Definition
Syntax highlighting in Cobalt colorizes code blocks using either the `{% highlight LANG %}` / `{% endhighlight %}` Liquid tags or Markdown fenced code blocks with language annotations, with the theme configurable in `_cobalt.yml`.

# Core Definition
Cobalt provides built-in syntax highlighting for code blocks. Two methods are supported: (1) the Liquid tags `{% highlight LANG %}` and `{% endhighlight %}`, and (2) Markdown fenced code blocks with language annotations (e.g., triple backticks with a language identifier). The highlighting theme is set site-wide in the `_cobalt.yml` configuration file under `syntax_highlight.theme`, with `base16-ocean.dark` as the default. Highlighting can be enabled or disabled globally via `syntax_highlight.enabled`. Custom syntaxes can be added by placing Sublime Text syntax definition files in a `_syntaxes/` directory at the project root (source: Cobalt docs, "Pages" page, "Syntax Highlighting" section; "Configuration" page).

# Prerequisites
- Understanding of pages and how they are processed (see `page`)
- Understanding of the Cobalt configuration file (see `cobalt-configuration-file`)
- For Markdown code blocks: understanding of Markdown fenced code block syntax

# Key Properties
1. **Liquid tag method**: Use `{% highlight LANG %}` ... `{% endhighlight %}` to wrap code that should be highlighted.
2. **Markdown method**: Use GitHub-style fenced code blocks with language annotation (triple backticks followed by language name).
3. **Theme configuration**: Set in `_cobalt.yml` under `syntax_highlight.theme`. Default is `base16-ocean.dark`.
4. **Global enable/disable**: Set `syntax_highlight.enabled` to `true` or `false` in `_cobalt.yml`. Defaults to `true`.
5. **Custom syntaxes**: Add Sublime Text syntax definition files to `_syntaxes/` at the project root.
6. **Discovery commands**: Run `cobalt debug highlight syntaxes` to list supported syntaxes; run `cobalt debug highlight themes` to list available themes.

# Construction / Recognition
## To Construct/Create:
1. Ensure `syntax_highlight.enabled: true` in `_cobalt.yml` (enabled by default).
2. Choose a theme by setting `syntax_highlight.theme` in `_cobalt.yml`, or use the default.
3. In templates, use either the Liquid highlight tag or Markdown fenced code blocks.
4. Optionally add custom syntax definitions to `_syntaxes/`.

## Configuration example:
```yaml
# _cobalt.yml
syntax_highlight:
  theme: "base16-ocean.dark"
  enabled: true
```

## Usage in Liquid:
```
{% highlight rust %}
fn main() {
    println!("Hello, world!");
}
{% endhighlight %}
```

## Usage in Markdown:
````markdown
```rust
fn main() {
    println!("Hello, world!");
}
```
````

# Context & Application
- **Typical contexts**: Blog posts with code samples, technical documentation pages, tutorial content.
- **When to use**: Any time you include code snippets in your pages or posts.
- **Scope**: Site-wide theme and enable/disable; per-block language specification.

# Examples
**Example 1** (source: Cobalt docs, Pages page): Using the Liquid highlight tag

```
{% highlight python %}
def greet(name):
    print(f"Hello, {name}!")
{% endhighlight %}
```

**Example 2** (source: Cobalt docs, Configuration page): Listing supported syntaxes

```console
$ cobalt debug highlight syntaxes
$ cobalt debug highlight themes
```

# Relationships
## Builds Upon
- `page`: Syntax highlighting is applied during page processing.
- `cobalt-configuration-file`: Theme and enable/disable settings are in `_cobalt.yml`.

## Enables
- Readable, colorized code blocks in rendered HTML pages.

## Related
- `liquid-template-language`: The `{% highlight %}` tag is a Liquid tag.
- `post`: Posts support syntax highlighting just as pages do.
- `cobalt-build`: Highlighting is applied during the build process.

## Contrasts With
- None directly; syntax highlighting is an additive feature.

# Common Errors
1. **Misspelling the language name**: If the language is not recognized, the code block will not be highlighted.
2. **Forgetting `{% endhighlight %}`**: The Liquid tag method requires a closing tag.

# Common Confusions
1. **Liquid tag vs. Markdown method**: Both achieve the same result; the Markdown method is simpler but only works in `.md` files.
2. **Theme vs. enabled**: The `theme` setting selects the color scheme, while `enabled` turns highlighting on or off entirely.

# Source Reference
- Cobalt Documentation, "Docs::Pages" page, "Syntax Highlighting" section.
- Cobalt Documentation, "Docs::Configuration" page, `syntax_highlight` settings.

# Verification Notes
- All features (Liquid tag, Markdown method, theme config, custom syntaxes, debug commands) are documented in the source files.
