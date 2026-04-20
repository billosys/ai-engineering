---
title: "Opentype Features"
source: "Butterick's Practical Typography"
author: "Matthew Butterick"
url: "https://practicaltypography.com/opentype-features.html"
---

<div id="content">

<div id="doc">

OpenType featuresFont support + application support

OpenType is a font format invented in the 1990s by Microsoft and Adobe, and later adopted by Apple. A major goal of OpenType was to provide better support for international languages and writing systems than previous formats (PostScript and TrueType).

To do this, OpenType includes layout features—commonly known as OpenType features—that allow fonts to specify alternate letterforms, and rules for how they should be inserted into the text. These features are mandatory for handling languages like Arabic and <span class="no-hyphens">Urdu.</span>

They’re not mandatory in English. But as a side effect, OpenType layout features have allowed type designers to add luxuries to their fonts—like <a href="alternate-figures.html" class="xref">alternate figures</a>, <a href="small-caps.html" class="xref">small caps</a>, <a href="ligatures.html" class="xref">ligatures</a>, <a href="ordinals.html" class="xref">ordinals</a>, and fractions—that had previously been difficult or impossible. That’s the good <span class="no-hyphens">news.</span>

Type designers add these features at their discretion. Thus, an OpenType-format font can have any number of OpenType features, including <span class="no-hyphens">none.</span>

The bad news is that merely selecting an OpenType font doesn’t make its features available. Rather, your typesetting program also has to support the features you want to use. Even though many OpenType-enhanced fonts are available today, software companies have been slow to upgrade their <span class="no-hyphens">applications.</span>

This bit of background just sets the stage for the annoying truth—that OpenType features can add a lot of typographic sophistication to your document, but you can only use a given feature if it’s supported by both the font *and* the <span class="no-hyphens">application.</span>

If you still want to use OpenType features, some <span class="no-hyphens">tips:</span>

1.  Designers of professional fonts (see <a href="font-recommendations.html" class="xref">font recommendations</a>) will have downloadable specimen sheets that show you which OpenType features are supported by their <span class="no-hyphens">fonts.</span>

2.  All major desktop web browsers support OpenType features. Support is spottier among mobile web <span class="no-hyphens">browsers.</span>

3.  The best OpenType feature support is found in professional page-layout applications like Adobe InDesign, Adobe Illustrator, and Quark Xpress.

4.  Recent versions of Microsoft Word (≥ 2010 for Windows, ≥ 2011 for Mac) support a limited set of OpenType features (ligatures, alternate figures, and stylistic sets). But Excel and PowerPoint don’t support any. If you think this is ironic and a little sad given that Microsoft introduced the OpenType format in 1996, me <span class="no-hyphens">too.</span>

<div class="howto">

<div class="howto-name">

How to activate OpenType features

</div>

WordRight-click in the text and select Font from the menu. Click the Advanced tab. The Advanced Typography panel is in the middle, and supports <a href="ligatures.html" class="xref">ligatures</a>, <a href="alternate-figures.html" class="xref">alternate figures</a> (via the Number spacing and Number forms menus), and stylistic <span class="no-hyphens">sets.</span>

PagesFont panel (⌘ + t) → gear icon → Typography. This will open a panel showing you the OpenType features in the current <span class="no-hyphens">font.</span>

CSS`font-feature-settings` followed by a list of <span class="no-hyphens">features.</span>

</div>

</div>

<span id="links"></span>

<div class="gap" style="height:1em">

</div>

</div>

<a href="mixing-fonts.html" class="nav"></a>

<div id="prev" class="side">

</div>

<a href="metrics-vs-optical-spacing.html" class="nav"></a>

<div id="next" class="side">

</div>

<div id="switcher" onmousedown="drag_switcher(event, this)">

<span id="switcher_undock" class="switcher_icon"><span class="icon"></span></span> <span id="switcher_move" class="switcher_icon"><span class="icon"></span></span> <span id="switcher_info" class="switcher_icon" onclick="handle_font_info_click(this)" onmousedown="event.stopPropagation()"><span class="icon"></span></span> <span id="switcher_hide" class="switcher_icon" onclick="move_switcher_inside_toolbar()" onmousedown="event.stopPropagation()"><span class="icon"></span></span>

</div>

<div id="toolbar">

<div id="navtable">

<div class="center">

<a href="text-formatting.html" class="box-link">chapter</a>

</div>

</div>

</div>
