---
# === CORE IDENTIFICATION ===
concept: Deployment to GitLab CI
slug: deployment-gitlab-ci

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
section: "GitLab CI"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "GitLab Pages deployment"
  - "GitLab CI/CD deployment"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - cobalt-build
  - cobalt-configuration-file
extends: []
related:
  - deployment-github-pages
  - self-hosted-deployment
  - build-options
contrasts_with:
  - deployment-github-pages

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What must I know before deploying a Cobalt site?"
---

# Quick Definition
Cobalt sites can be deployed to GitLab Pages using GitLab CI with a `.gitlab-ci.yml` configuration that uses a Docker image to install Cobalt and build the site into a `public/` directory, which GitLab Pages serves automatically.

# Core Definition
GitLab CI deployment for Cobalt uses a `.gitlab-ci.yml` file that defines a `pages` job. The job runs in a Docker container (e.g., `debian:latest`), installs Cobalt via the same `gh-install` script used for Travis CI, and builds the site into the `public/` directory, which GitLab Pages requires as its artifact path. The Cobalt version is controlled via a CI variable (`COBALT_VERSION`). The job's `artifacts.paths` must include `public/`, and it is typically restricted to the `master` branch via the `only` directive (source: Cobalt docs, "Deployment" page, "GitLab CI" section).

# Prerequisites
- A built Cobalt site (see `cobalt-build`)
- A GitLab repository with GitLab CI enabled
- Basic understanding of Docker and GitLab CI/CD pipelines

# Key Properties
1. **Docker-based**: GitLab CI runs in Docker containers, providing a clean environment.
2. **`pages` job name**: GitLab Pages requires the CI job to be named `pages`.
3. **`public/` output directory**: GitLab Pages serves content from the `public/` directory artifact.
4. **Cobalt version variable**: The version is stored in a CI variable (`COBALT_VERSION`) for easy updates.
5. **Same installation script**: Uses the same `crate-ci/gh-install` script as the Travis CI method.
6. **Artifact-based deployment**: The `artifacts.paths` section specifies `public/` so GitLab knows what to deploy.

# Construction / Recognition
## To Construct/Create:
1. Create `.gitlab-ci.yml` in the repository root:
```yaml
image: debian:latest

variables:
  COBALT_VERSION: "v0.19.0"
pages:
  script:
  - apt-get update && apt-get -y install curl
  - curl -LSfs https://raw.githubusercontent.com/crate-ci/gh-install/master/v1/install.sh |
    sh -s --
    --git cobalt-org/cobalt.rs
    --crate cobalt
    --force
    --target x86_64-unknown-linux-gnu
    --tag $COBALT_VERSION
  - export PATH="$PATH:~/.cargo/bin"
  - mkdir -p public
  - cobalt build -d public
  artifacts:
    paths:
    - public/
  only:
  - master
```
2. Push to the `master` branch to trigger deployment.
3. The site will be available at your GitLab Pages URL.

# Context & Application
- **Typical contexts**: Hosting a Cobalt site on GitLab Pages with automated CI/CD deployment.
- **When to use**: When your repository is on GitLab and you want automated deployment.
- **Scope**: Per-repository deployment configuration.

# Examples
**Example 1** (source: Cobalt docs, Deployment page): The complete `.gitlab-ci.yml` is shown in the Construction section above. Key points:
- Uses `debian:latest` as the base Docker image.
- Installs `curl` for downloading Cobalt.
- Builds into `public/` using `cobalt build -d public`.
- Artifacts path is `public/`.

# Relationships
## Builds Upon
- `cobalt-build`: The deployment runs `cobalt build` as part of the CI pipeline.
- `cobalt-configuration-file`: Build settings are read from `_cobalt.yml`.

## Enables
- Automated deployment to GitLab Pages on push.

## Related
- `deployment-github-pages`: Equivalent deployment for GitHub using Travis CI.
- `self-hosted-deployment`: Deployment to your own server.

## Contrasts With
- `deployment-github-pages`: GitHub uses Travis CI and `gh-pages` branch; GitLab uses GitLab CI, Docker, and `public/` artifacts.

# Common Errors
1. **Job not named `pages`**: GitLab Pages requires the CI job to be named exactly `pages`.
2. **Missing `public/` in artifacts**: The built output must be in `public/` and listed in `artifacts.paths`.
3. **Forgetting to install `curl`**: The Docker base image (`debian:latest`) does not include `curl` by default.

# Common Confusions
1. **`-d public` flag**: The `-d` flag overrides Cobalt's `destination` setting, directing output to `public/` as required by GitLab Pages.
2. **GitLab Pages URL**: The URL depends on your GitLab username/namespace and project name (e.g., `https://username.gitlab.io/project`).

# Source Reference
- Cobalt Documentation, "Docs::Deployment" page, "GitLab CI" section.

# Verification Notes
- The complete `.gitlab-ci.yml` example is taken directly from the source documentation.
