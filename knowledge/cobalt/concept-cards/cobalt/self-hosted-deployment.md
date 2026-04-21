---
# === CORE IDENTIFICATION ===
concept: Self-Hosted Deployment
slug: self-hosted-deployment

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
section: "Self-hosted"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "self-hosted site deployment"
  - "VPS deployment"
  - "rsync deployment"
  - "git-based deployment"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - cobalt-build
  - cobalt-configuration-file
extends: []
related:
  - deployment-github-pages
  - deployment-gitlab-ci
  - build-options
contrasts_with:
  - deployment-github-pages
  - deployment-gitlab-ci

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What must I know before deploying a Cobalt site?"
---

# Quick Definition
Cobalt sites can be deployed to self-hosted servers using rsync for simple file synchronization, or via a git-based workflow using a bare repository with a `post-update` hook that runs Cobalt on the server.

# Core Definition
For self-hosted deployment, Cobalt documentation describes two primary approaches: (1) Simple uploading using `rsync` or similar file synchronization tools to copy the rendered site to a web server; and (2) Git-based publishing, where Cobalt and git are installed on the web server, a bare git repository is configured with a `post-update` hook that calls the `cobalt-git-deploy` script, and site updates are triggered by `git push`. The git-based approach is advantageous in multi-user settings as it leverages git's conflict resolution. The `cobalt-git-deploy` script handles checking out the latest code, building the site, and deploying it to the web root (source: Cobalt docs, "Deployment" page, "Self-hosted" section).

# Prerequisites
- A built Cobalt site (see `cobalt-build`)
- A web server (e.g., VPS with nginx or Apache)
- For rsync: SSH access to the server
- For git-based: Cobalt and git installed on the server, basic familiarity with git

# Key Properties
1. **rsync method**: Simple, direct file synchronization from local build output to the server's web directory.
2. **`--delete` flag**: Using `rsync --delete` removes extraneous files on the server, keeping it in sync with the local build.
3. **Git-based method**: Uses a bare git repository on the server with a `post-update` hook.
4. **`cobalt-git-deploy` script**: A helper script provided in the Cobalt repository (`contrib/cobalt-git-deploy`) that handles checkout, build, and deployment.
5. **Multi-user advantage**: The git-based approach prevents users from overwriting each other's changes by leveraging git's merge/rebase conflict resolution.
6. **Staging directory**: `cobalt-git-deploy` uses a staging directory (e.g., `~/cobalt-stage`) for the build, separate from the web root.

# Construction / Recognition
## Method 1: Simple rsync upload
```console
$ rsync --delete -a _site/ YOUR-SERVER:public_html/
```
Note: `--delete` removes files on the server that no longer exist locally.

## Method 2: Git-based deployment
1. Install Cobalt and git on the server.
2. Create a bare git repository on the server: `git init --bare homepage.git`
3. Add the server as a remote in your local repository: `git remote add server user@server:homepage.git`
4. Create a `post-update` hook on the server:
```sh
#!/bin/sh
# homepage.git/hooks/post-update

PATH="$HOME/bin:/usr/local/bin:/usr/bin:/bin"
export PATH

exec cobalt-git-deploy ~/cobalt-stage ~/public_html
```
5. Make the hook executable: `chmod +x homepage.git/hooks/post-update`
6. Push to deploy: `git push server master`

## Expected output on push:
```
No previous state saved. First run?
Checking out master to /home/foo/cobalt-stage/left
Already on 'master'
HEAD is now at 9ef95c1 New exciting blog post
Building site
[info] Building from "/home/foo/cobalt-stage/left/" into "/home/foo/cobalt-stage/left/_site"
[info] Build successful
Deploying site in /home/foo/public_html
```

# Context & Application
- **Typical contexts**: Deploying to a VPS, dedicated server, or any self-managed hosting.
- **When to use rsync**: For simple, single-user sites where you want quick deployment.
- **When to use git-based**: For multi-user sites or when you want git's version control benefits on the server.
- **Scope**: Per-server deployment configuration.

# Examples
**Example 1** (source: Cobalt docs, Deployment page): rsync deployment

```console
$ rsync --delete -a _site/ YOUR-SERVER:public_html/
```

**Example 2** (source: Cobalt docs, Deployment page): Git hook with `cobalt-git-deploy`

The `post-update` hook invokes `cobalt-git-deploy` with two arguments: the staging directory and the web root. Run `cobalt-git-deploy --help` for additional options.

# Relationships
## Builds Upon
- `cobalt-build`: Both methods require a successful Cobalt build.

## Enables
- Self-hosted site deployment without relying on third-party platforms.
- Multi-user collaborative publishing via git.

## Related
- `deployment-github-pages`: Alternative using GitHub's hosting.
- `deployment-gitlab-ci`: Alternative using GitLab's hosting.

## Contrasts With
- `deployment-github-pages`: GitHub Pages is managed hosting; self-hosted gives full control.
- `deployment-gitlab-ci`: GitLab Pages is managed hosting via CI/CD; self-hosted uses direct server access.

# Common Errors
1. **Forgetting `--delete` with rsync**: Without it, deleted pages will persist on the server.
2. **Non-executable hook**: The `post-update` hook must be executable (`chmod +x`).
3. **Missing Cobalt on server**: The git-based method requires Cobalt to be installed on the server.
4. **Pre-existing staging directory**: The `cobalt-git-deploy` documentation notes that the directories it is invoked with should not already exist on first run.

# Common Confusions
1. **rsync vs. git-based**: rsync is simpler but lacks version control on the server; git-based is more complex but supports collaboration and rollback.
2. **`cobalt build --import`**: Cobalt's built-in `import` command is designed for `gh-pages` branch deployment, not for self-hosted rsync/git deployment.

# Source Reference
- Cobalt Documentation, "Docs::Deployment" page, "Self-hosted" section (including "Simple uploading" and "Publishing with git" subsections).

# Verification Notes
- Both deployment methods (rsync and git-based) and the `cobalt-git-deploy` script reference are directly documented in the source.
