# Optional design examples

These HTML, CSS and JavaScript files are developer specimens, not part of the
installable Visual Design skill. The skill package contains Markdown methods
and text cases and does not depend on this directory or on a running app.

The image-story page refers to three files by their relative names under
`lfe-image-assets/`. The artwork is not included here. Without those files, the
images and full-image links intentionally remain unavailable; the story titles,
summaries, captions, index, article links and static navigation still provide a
useful text path. This missing-image state is expected, not a packaging error.

For optional local inspection, copy these text fixtures into an owned temporary
root. Link only the image directory to a supplied LFE checkout; the mode-study
method link is mirrored at the path it expects. Run this from the repository
root, replacing the LFE path with a supplied checkout:

```sh
tmp=$(mktemp -d "${TMPDIR:-/tmp}/design-examples.XXXXXX")
mkdir -p "$tmp/examples/design" "$tmp/knowledge/design/guides"
cp -R examples/design/. "$tmp/examples/design/"
ln -s /path/to/lfe-checkout/src/images "$tmp/examples/design/lfe-image-assets"
ln -s "$PWD/knowledge/design/guides/system-evolution.md" "$tmp/knowledge/design/guides/system-evolution.md"
```

Serve `$tmp` as the static root and open
`/examples/design/lfe-image-stories.html` or
`/examples/design/lfe-mode-study.html`. Remove the temporary root after
inspection. Do not copy the artwork into the AI repository, fetch replacement
images, or treat the local overlay as permission to redistribute the images.
