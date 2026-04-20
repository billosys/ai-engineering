# Extraction Log for Cobalt Static Site Generator

## Source Metadata

- **Full title**: Cobalt Static Site Generator (Documentation & API Reference)
- **Authors**: Cobalt contributors (cobalt-org)
- **Publication type**: Software documentation (user docs + rustdoc API)
- **Subject area**: Static site generation, Liquid templating, Rust web tooling
- **Scope**: CLI usage, content authoring, Liquid templating, Rust API

## Source Inventory

| Source | Files | Size | Format | Content |
|--------|-------|------|--------|---------|
| Cobalt user docs | 20 | 96 KB | Markdown | User/developer guides |
| Cobalt API docs | 71 | 2.6 MB | HTML (rustdoc) | Library API reference |
| Liquid crate docs | 84 | 5.6 MB | HTML (rustdoc) | Core templating API |
| Liquid binary docs | 10 | 128 KB | HTML (rustdoc) | CLI tool docs |
| Liquid core docs | 214 | 7.1 MB | HTML (rustdoc) | Templating internals |
| Liquid derive docs | 12 | 76 KB | HTML (rustdoc) | Proc macro docs |
| Liquid help MD docs | 4 | 28 KB | HTML (rustdoc) | Markdown support |
| Liquid stdlib docs | 141 | 3.1 MB | HTML (rustdoc) | Built-in filters/tags/blocks |
| **Total** | **556** | **18.7 MB** | Mixed | Complete SSG ecosystem |

## Complete Concept Inventory

### Agent 1: CLI, Installation & Project Structure (~15 cards)

| # | Concept | Slug | Category | Tier | Source |
|---|---------|------|----------|------|--------|
| 1 | Cobalt | cobalt | cli | foundational | getting-started.md, docs.md |
| 2 | Installation | installation | cli | foundational | install.md |
| 3 | cobalt init | cobalt-init | cli | foundational | usage.md |
| 4 | cobalt build | cobalt-build | cli | foundational | usage.md |
| 5 | cobalt serve | cobalt-serve | cli | foundational | usage.md |
| 6 | cobalt new | cobalt-new | cli | foundational | usage.md |
| 7 | cobalt publish | cobalt-publish | cli | foundational | usage.md |
| 8 | cobalt clean | cobalt-clean | cli | foundational | usage.md |
| 9 | cobalt debug | cobalt-debug | cli | intermediate | usage.md, trouble.md |
| 10 | Directory Structure | directory-structure | project-structure | foundational | directory.md |
| 11 | Source Directory | source-directory | project-structure | foundational | directory.md, config.md |
| 12 | Destination Directory | destination-directory | project-structure | foundational | directory.md, config.md |
| 13 | Layouts Directory | layouts-directory | project-structure | foundational | directory.md |
| 14 | Includes Directory | includes-directory | project-structure | foundational | directory.md |
| 15 | Defaults Directory | defaults-directory | project-structure | intermediate | directory.md |

### Agent 2: Content, Frontmatter & Configuration (~22 cards)

| # | Concept | Slug | Category | Tier | Source |
|---|---------|------|----------|------|--------|
| 16 | Page | page | content | foundational | pages.md |
| 17 | Post | post | content | foundational | posts.md |
| 18 | Draft | draft | content | foundational | posts.md |
| 19 | Content Processing Pipeline | content-processing-pipeline | content | intermediate | pages.md |
| 20 | Frontmatter | frontmatter | frontmatter | foundational | front.md |
| 21 | Title Field | title-field | frontmatter | foundational | front.md |
| 22 | Published Date Field | published-date-field | frontmatter | intermediate | front.md |
| 23 | Format Field | format-field | frontmatter | intermediate | front.md |
| 24 | Layout Field | layout-field | frontmatter | intermediate | front.md |
| 25 | Is Draft Field | is-draft-field | frontmatter | intermediate | front.md |
| 26 | Slug Field | slug-field | frontmatter | intermediate | front.md |
| 27 | Excerpt and Excerpt Separator | excerpt | frontmatter | intermediate | front.md |
| 28 | Categories Field | categories-field | frontmatter | intermediate | front.md |
| 29 | Tags Field | tags-field | frontmatter | intermediate | front.md |
| 30 | Data Field | data-field | frontmatter | intermediate | front.md |
| 31 | Cobalt Configuration File | cobalt-configuration-file | configuration | foundational | config.md |
| 32 | Build Options | build-options | configuration | intermediate | config.md |
| 33 | Site Options | site-options | configuration | intermediate | config.md |
| 34 | Posts Configuration | posts-configuration | configuration | intermediate | config.md |
| 35 | Permalink Templates | permalink-templates | permalink | intermediate | permalink.md |
| 36 | Permalink Template Variables | permalink-template-variables | permalink | intermediate | permalink.md |
| 37 | Pretty URLs | pretty-urls | permalink | intermediate | permalink.md |

### Agent 3: Liquid Templating (~25 cards)

| # | Concept | Slug | Category | Tier | Source |
|---|---------|------|----------|------|--------|
| 38 | Liquid Template Language | liquid-template-language | liquid-basics | foundational | layouts.md, liquid docs |
| 39 | Output Tags | output-tags | liquid-basics | foundational | variables.md, liquid docs |
| 40 | Logic Tags | logic-tags | liquid-basics | foundational | liquid docs |
| 41 | Layout | layout | templating | foundational | layouts.md |
| 42 | Include | include | templating | intermediate | layouts.md, liquid_lib |
| 43 | Template Variables | template-variables | templating | foundational | variables.md |
| 44 | Site Variable | site-variable | templating | foundational | variables.md |
| 45 | Page Variable | page-variable | templating | foundational | variables.md |
| 46 | Collection Variable | collection-variable | templating | intermediate | variables.md |
| 47 | Data Files | data-files | data-files | intermediate | data.md |
| 48 | If Block | if-block | liquid-blocks | foundational | liquid_lib |
| 49 | Unless Block | unless-block | liquid-blocks | intermediate | liquid_lib |
| 50 | For Block | for-block | liquid-blocks | foundational | liquid_lib |
| 51 | Case Block | case-block | liquid-blocks | intermediate | liquid_lib |
| 52 | Capture Block | capture-block | liquid-blocks | intermediate | liquid_lib |
| 53 | Comment Block | comment-block | liquid-blocks | foundational | liquid_lib |
| 54 | Raw Block | raw-block | liquid-blocks | intermediate | liquid_lib |
| 55 | Assign Tag | assign-tag | liquid-tags | foundational | liquid_lib |
| 56 | Cycle Tag | cycle-tag | liquid-tags | intermediate | liquid_lib |
| 57 | Increment and Decrement Tags | increment-decrement-tags | liquid-tags | intermediate | liquid_lib |
| 58 | Break and Continue Tags | break-continue-tags | liquid-tags | intermediate | liquid_lib |
| 59 | Forloop Object | forloop-object | liquid-blocks | intermediate | liquid_lib |
| 60 | String Filters | string-filters | liquid-filters | intermediate | liquid_lib |
| 61 | Array Filters | array-filters | liquid-filters | intermediate | liquid_lib |
| 62 | Math Filters | math-filters | liquid-filters | intermediate | liquid_lib |

### Agent 4: Advanced Features, Feeds, Deployment & Rust API (~18 cards)

| # | Concept | Slug | Category | Tier | Source |
|---|---------|------|----------|------|--------|
| 63 | Pagination | pagination | pagination | advanced | posts.md |
| 64 | Paginator Variable | paginator-variable | pagination | advanced | posts.md |
| 65 | Pagination Include Types | pagination-include-types | pagination | advanced | posts.md |
| 66 | Syntax Highlighting | syntax-highlighting | content | intermediate | pages.md, config.md |
| 67 | Sass and SCSS Support | sass-scss-support | assets | intermediate | assets.md, config.md |
| 68 | Assets | assets | assets | foundational | assets.md |
| 69 | RSS Feed | rss-feed | feeds | intermediate | rss.md |
| 70 | HTML and URL Filters | html-url-filters | liquid-filters | intermediate | liquid_lib |
| 71 | Date Filter | date-filter | liquid-filters | intermediate | liquid_lib |
| 72 | Utility Filters | utility-filters | liquid-filters | intermediate | liquid_lib |
| 73 | Deployment to GitHub Pages | deployment-github-pages | deployment | advanced | deployment.md |
| 74 | Deployment to GitLab CI | deployment-gitlab-ci | deployment | advanced | deployment.md |
| 75 | Self-Hosted Deployment | self-hosted-deployment | deployment | advanced | deployment.md |
| 76 | Liquid Parser and ParserBuilder | liquid-parser | rust-api | advanced | liquid docs |
| 77 | Liquid Template Object | liquid-template-object | rust-api | advanced | liquid docs |
| 78 | Liquid Value System | liquid-value-system | rust-api | advanced | liquid_core docs |
| 79 | ObjectView and ValueView Traits | objectview-valueview-traits | rust-api | advanced | liquid docs |
| 80 | Cobalt Config Struct | cobalt-config-struct | rust-api | advanced | cobalt API docs |

**Total estimated cards: ~80**

## CQ-to-Concept Mapping

| CQ# | Competency Question | Primary Concepts |
|-----|---------------------|------------------|
| 1 | What is Cobalt? | cobalt |
| 2 | What is a page in Cobalt? | page |
| 3 | What is a post in Cobalt? | post |
| 4 | What is a draft in Cobalt? | draft |
| 5 | What is frontmatter in Cobalt? | frontmatter |
| 6 | What is a layout in Cobalt? | layout |
| 7 | What is an include in Cobalt? | include |
| 8 | What is a permalink in Cobalt? | permalink-templates |
| 9 | What is a data file in Cobalt? | data-files |
| 10 | What is an asset in Cobalt? | assets |
| 11 | What is the `_cobalt.yml` configuration file? | cobalt-configuration-file |
| 12 | What is the Liquid templating language? | liquid-template-language |
| 13 | What is a Liquid filter? | string-filters, array-filters, math-filters |
| 14 | What is a Liquid tag? | assign-tag, cycle-tag |
| 15 | What is a Liquid block? | if-block, for-block |
| 16 | How does a layout relate to page content? | layout, page-variable |
| 17 | How do includes relate to layouts? | include, layout |
| 18 | How does frontmatter relate to Liquid template variables? | frontmatter, template-variables |
| 19 | How do data files relate to the site.data variable? | data-files, site-variable |
| 20 | How does the permalink frontmatter field relate to URL generation? | permalink-templates, permalink-template-variables |
| 21 | How do posts relate to pages in Cobalt? | post, page |
| 22 | How does _cobalt.yml relate to frontmatter defaults? | cobalt-configuration-file, frontmatter |
| 23 | How does Liquid Rust relate to Ruby Liquid? | liquid-template-language |
| 24 | How do collections relate to posts? | collection-variable, post |
| 25 | How does pagination relate to posts? | pagination, post |
| 26 | How do I install Cobalt? | installation |
| 27 | How do I create a new Cobalt site? | cobalt-init |
| 28 | How do I build a Cobalt site? | cobalt-build |
| 29 | How do I preview a Cobalt site locally? | cobalt-serve |
| 30 | How do I create a new page or post? | cobalt-new |
| 31 | How do I publish a draft post? | cobalt-publish |
| 32 | How do I configure site-wide settings? | cobalt-configuration-file, site-options |
| 33 | How do I create and use layouts? | layout |
| 34 | How do I use Liquid template variables? | template-variables, output-tags |
| 35 | How do I set up RSS feeds? | rss-feed |
| 36 | How do I deploy to GitHub Pages? | deployment-github-pages |
| 37 | How do I use data files in templates? | data-files |
| 38 | How do I configure pagination? | pagination |
| 39 | How do I use Sass/SCSS with Cobalt? | sass-scss-support |
| 40 | How do I add syntax highlighting? | syntax-highlighting |
| 41 | How do I set up permalink templates? | permalink-templates |
| 42 | How do I use cobalt debug? | cobalt-debug |
| 43 | What must I know before creating a Cobalt site? | cobalt, installation, directory-structure |
| 44 | What must I know before writing Liquid templates? | liquid-template-language, output-tags, logic-tags |
| 45 | What must I know before configuring pagination? | pagination, post, frontmatter |
| 46 | What must I know before deploying? | cobalt-build, deployment-github-pages |
| 47 | What must I know for the Cobalt Rust API? | cobalt-config-struct, liquid-parser |
| 48 | What distinguishes a page from a post? | page, post |
| 49 | What distinguishes a layout from an include? | layout, include |
| 50 | What distinguishes serve from build? | cobalt-serve, cobalt-build |
| 51 | What distinguishes Cobalt's Liquid from Ruby Liquid? | liquid-template-language |
| 52 | What distinguishes path permalink style from custom? | permalink-templates |
| 53 | What distinguishes frontmatter data from data files? | data-field, data-files |
| 54 | What distinguishes cobalt new from manual file creation? | cobalt-new |
| 55 | What distinguishes {{ }} from {% %}? | output-tags, logic-tags |

## Agent Assignment Verification

- [x] Every concept assigned to exactly one agent
- [x] No gaps in concept coverage
- [x] Card count estimates balanced (15/22/25/18 = ±20% from mean of 20)
- [x] Each agent has clear thematic coherence
- [x] CQ coverage distributed across all agents
