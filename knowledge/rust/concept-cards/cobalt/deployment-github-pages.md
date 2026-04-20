---
# === CORE IDENTIFICATION ===
concept: Deployment to GitHub Pages
slug: deployment-github-pages

# === CLASSIFICATION ===
category: deployment
tier: advanced

# === PROVENANCE ===
source: "Cobalt Static Site Generator Documentation"
source_slug: cobalt
authors: "Cobalt contributors (cobalt-org)"
chapter: "Docs::Deployment"
chapter_number: null
pdf_page: null
section: "TravisCI"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "GitHub Pages deployment"
  - "gh-pages deployment"
  - "Travis CI deployment"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - cobalt-build
  - cobalt-configuration-file
  - directory-structure
extends: []
related:
  - deployment-gitlab-ci
  - self-hosted-deployment
  - build-options
contrasts_with:
  - deployment-gitlab-ci
  - self-hosted-deployment

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I deploy a Cobalt site to GitHub Pages?"
  - "What must I know before deploying a Cobalt site?"
---

# Quick Definition
Cobalt sites can be deployed to GitHub Pages using Travis CI by configuring a `.travis.yml` that installs Cobalt, builds the site, and pushes the output to the `gh-pages` or `master` branch using a GitHub token.

# Core Definition
Deploying a Cobalt site to GitHub Pages involves setting up a Travis CI pipeline that installs Cobalt via a shell script from `crate-ci/gh-install`, runs `cobalt build`, and uses Travis's `deploy` provider to push the built site to the appropriate branch. The deployment configuration specifies the Cobalt version (`--tag`), the build output directory (`local_dir`, matching the Cobalt `destination` setting), the target branch for GitHub Pages (`target_branch`), and the source branch (`on: branch`). A `GH_TOKEN` (GitHub API token) must be encrypted and added to the Travis configuration. For personal/organization sites, the source is kept in a non-master branch (e.g., `source`) since GitHub serves personal sites from `master` (source: Cobalt docs, "Deployment" page, "TravisCI" section).

# Prerequisites
- A built Cobalt site (see `cobalt-build`)
- A GitHub repository for the site
- Travis CI account linked to the GitHub repository
- A GitHub personal access token (`GH_TOKEN`)
- The `travis` CLI tool for encrypting the token

# Key Properties
1. **Travis CI-based**: Uses `.travis.yml` to automate the build and deploy process.
2. **Cobalt installation via script**: Cobalt is installed in the CI environment using `gh-install` from `crate-ci`.
3. **Configurable version**: The `--tag` parameter specifies which Cobalt version to install.
4. **Deploy provider**: Uses Travis's `pages` deploy provider.
5. **GH_TOKEN**: An encrypted GitHub personal access token is required for pushing to the repository.
6. **Branch configuration**: `target_branch` specifies where GitHub Pages serves from; `on: branch` specifies the source branch.
7. **Project vs. personal sites**: Project sites use `gh-pages` branch; personal/organization sites must serve from `master`, so source goes in a different branch (e.g., `source`).
8. **Import alternative**: Cobalt also supports `cobalt build --import` or `cobalt import` for pushing to `gh-pages` without Travis CI.

# Construction / Recognition
## To Construct/Create:
1. Create `.travis.yml` in your repository:
```yaml
sudo: false
before_script:
  - curl -LSfs https://raw.githubusercontent.com/crate-ci/gh-install/master/v1/install.sh |
    sh -s --
    --git cobalt-org/cobalt.rs
    --crate cobalt
    --force
    --target x86_64-unknown-linux-gnu
    --tag v0.19.0
  - export PATH="$PATH:~/.cargo/bin"
script:
  - cobalt build
deploy:
  provider: pages
  skip_cleanup: true
  github_token: $GH_TOKEN
  local_dir: _site
  target_branch: master
  on:
    branch: source
```
2. Generate a GitHub personal access token at https://github.com/settings/tokens.
3. Encrypt the token using the Travis CLI: `travis encrypt GH_TOKEN=... --add env.global`.
4. Adjust `--tag`, `local_dir`, `target_branch`, and `on: branch` as needed.
5. Push the configuration and source to trigger a build.

# Context & Application
- **Typical contexts**: Automated deployment of a Cobalt blog or documentation site to GitHub Pages.
- **When to use**: When hosting a Cobalt site on GitHub Pages with CI/CD automation.
- **Scope**: Per-repository deployment configuration.

# Examples
**Example 1** (source: Cobalt docs, Deployment page): Encrypting the GitHub token

```console
$ travis encrypt GH_TOKEN=your_token_here --add env.global
```

**Example 2** (source: Cobalt docs, Deployment page): Key configuration fields

- `--tag v0.19.0`: Install Cobalt v0.19.0 (update as needed)
- `local_dir: _site`: Must match Cobalt's `destination` setting
- `target_branch: master`: GitHub Pages source branch
- `on: branch: source`: Source branch containing site content

# Relationships
## Builds Upon
- `cobalt-build`: The deployment runs `cobalt build` as part of the CI pipeline.
- `cobalt-configuration-file`: The `destination` setting must match `local_dir`.

## Enables
- Automated, push-triggered deployment to GitHub Pages.

## Related
- `deployment-gitlab-ci`: Alternative CI-based deployment for GitLab.
- `self-hosted-deployment`: Alternative deployment for self-hosted servers.
- `build-options`: Build-time options that affect the generated output.

## Contrasts With
- `deployment-gitlab-ci`: Uses GitLab CI and Docker instead of Travis CI.
- `self-hosted-deployment`: Deploys to your own server instead of GitHub Pages.

# Common Errors
1. **Mismatched `local_dir` and `destination`**: The `local_dir` in Travis must match the Cobalt `destination` directory.
2. **Unencrypted GH_TOKEN**: Committing the token in plain text is a security risk; always use `travis encrypt`.
3. **Wrong branch configuration**: Personal sites must serve from `master`; project sites typically use `gh-pages`.

# Common Confusions
1. **Project site vs. personal site**: Project sites can use `gh-pages`; personal/org sites must use `master`.
2. **`cobalt build --import` vs. Travis deploy**: Cobalt has a built-in `import` command for pushing to `gh-pages`, which can be used as an alternative to Travis's deploy provider.

# Source Reference
- Cobalt Documentation, "Docs::Deployment" page, "TravisCI" section.

# Verification Notes
- The complete `.travis.yml` example and all configuration notes are directly from the source documentation.
