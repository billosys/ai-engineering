---
concept: Data URL
slug: data-url
category: http-forms
subcategory: browser-api
tier: intermediate
source: "Eloquent JavaScript, 4th Edition"
source_slug: eloquent-js
authors: "Marijn Haverbeke"
chapter: "Project: A Pixel Art Editor"
chapter_number: 19
pdf_page: null
section: "Saving and loading"
extraction_confidence: high
aliases:
  - data URI
  - toDataURL
prerequisites:
  - canvas-element
  - url
extends: []
related:
  - file-reader
  - drawimage
contrasts_with: []
answers_questions:
  - "How do I create a downloadable image from a canvas?"
  - "What is a data URL?"
---

# Quick Definition
A data URL embeds the entire resource content directly in the URL string using the `data:` scheme, created from canvases via `toDataURL()` or from files via `FileReader.readAsDataURL()`.

# Core Definition
"The `toDataURL` method on a canvas element creates a URL that uses the `data:` scheme. Unlike `http:` and `https:` URLs, data URLs contain the whole resource in the URL. They are usually very long, but they allow us to create working links to arbitrary pictures, right here in the browser" (Ch. 19, "Saving and loading").

# Prerequisites
- **Canvas element**: toDataURL is a canvas method
- **URL**: Data URLs are a URL scheme

# Key Properties
1. `canvas.toDataURL()` creates a data URL from canvas content
2. `FileReader.readAsDataURL(file)` creates a data URL from a file
3. Format: `data:[mediatype];base64,[data]`
4. Can be used as `src` for images or `href` for download links

# Construction / Recognition
```javascript
let canvas = elt("canvas");
drawPicture(this.picture, canvas, 1);
let link = elt("a", {
  href: canvas.toDataURL(),
  download: "pixelart.png"
});
link.click();
```

# Context & Application
Used for saving canvas content, previewing uploads, embedding small images in HTML/CSS, and creating downloadable files client-side.

# Examples
Loading a file as a data URL for preview:
```javascript
reader.readAsDataURL(file);
// reader.result → "data:image/png;base64,..."
```

# Relationships
## Builds Upon
- canvas-element, url
## Enables
- Client-side image saving, file previews, inline images
## Related
- file-reader, drawimage
## Contrasts With
- Regular URLs (reference remote resources)

# Common Errors
- **Error**: Using data URLs for large files (performance issue)
  **Correction**: Data URLs are best for small files; use Blob URLs for larger content

# Common Confusions
- **Confusion**: Data URLs are the same as regular URLs
  **Clarification**: Data URLs contain the entire resource inline; they don't reference external files

# Source Reference
Chapter 19: Project: A Pixel Art Editor, Section "Saving and loading", lines 662-711 of 19-project-a-pixel-art-editor.md.

# Verification Notes
- Definition source: direct from source text
- Confidence rationale: Clear explanation with usage
- Cross-reference status: verified
