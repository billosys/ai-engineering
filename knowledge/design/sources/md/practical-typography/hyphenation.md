---
title: "Hyphenation"
source: "Butterick's Practical Typography"
author: "Matthew Butterick"
url: "https://practicaltypography.com/hyphenation.html"
---

<div id="content">

<div id="doc">

hyphenationMandatory for justified text; optional otherwise

Hyphenation is the automated process of breaking words between lines to create more consistency across a text <span class="no-hyphens">block.</span>

In <a href="justified-text.html" class="xref">justified text</a>, hyphenation is <span class="no-hyphens">mandatory.</span>

In left-aligned text, hyphenation evens the irregular right edge of the text, called the rag. Hyphenation is optional for left-aligned text because the rag will still be somewhat irregular, even with hyphenation. Hyphenation doesn’t improve text legibility. In this case, consider turning it <span class="no-hyphens">off.</span>

As <a href="line-length.html" class="xref">line length</a> gets shorter, hyphenation becomes essential. Why? With hyphenation off, your word processor or web browser can only break lines at word spaces. As the lines get shorter, there are fewer words and hence fewer possible break points in each line, making awkward breaks more <span class="no-hyphens">likely.</span>

<div class="howto">

<div class="howto-name">

How to turn hyphenation on (or off)

</div>

WordPage Layout → Page Setup panel → Hyphenation → Automatic (or None)

Mac OS WordTools → Hyphenation → check (or uncheck) Automatically hyphenate <span class="no-hyphens">document</span>

PagesView → Show Toolbar (or option + ⌘ + t) → Document button → Document pane → check (or uncheck) Hyphenation

CSSUse `hyphens: auto`, though support is [still <span class="no-hyphens">spotty</span>](http://caniuse.com/#search=hyphens)

</div>

Sometimes you may want to suppress automatic hyphenation. For instance, <a href="headings.html" class="xref">headings</a> are relatively short, so hyphenation often causes more problems than it <span class="no-hyphens">solves.</span>

<table class="example">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="font-size: 120%"><span>B. Your proposal contains contradic-<br />
tions that render it utterly use-<br />
less for our current needs.</span></td>
<td>wrong</td>
</tr>
<tr>
<td style="font-size: 120%"><span>B. Your proposal contains<br />
contradictions that render it utterly<br />
useless for our current needs.</span></td>
<td>right</td>
</tr>
</tbody>
</table>

Hyphenation can be suppressed in a single paragraph, or a set of paragraphs, if you suppress hyphenation within <a href="paragraph-and-character-styles.html" class="xref">paragraph and character styles</a>.

<div class="howto">

<div class="howto-name">

How to suppress hyphenation in a paragraph

</div>

WordRight-click in the text and select Paragraph → Line and Page Breaks → Don’t <span class="no-hyphens">hyphenate</span>

PagesView → Show Toolbar (or option + ⌘ + t) → Format button → More pane → Remove paragraph <span class="no-hyphens">hyphenation</span>

CSSUse `hyphens: `<span class="no-hyphens">`none`</span>

</div>

<div class="btw">

<div class="btw-title">

by the way

</div>

- In word processors, you can exert rudimentary control over automatic hyphenation. If you’re curious, search your help file for “hyphenation options.” Over the years, I’ve never touched these, so I doubt you’ll need to either. The nonbreaking hyphen and the <a href="optional-hyphens.html" class="xref">optional hyphen</a> solve most hyphenation problems, and even those are pretty <span class="no-hyphens">rare.</span>

- In pro page-layout programs, you can exert a lot of control over automatic hyphenation (usually in conjunction with justification, so all the settings together are known as H&Js).

- In web browsers, you can exert almost no control over automatic hyphenation, so if you use CSS hyphenation, be prepared for some <span class="no-hyphens">clunkers.</span>

- If you’re using a web content-management system like WordPress, an alternative hyphenation method is to use a plugin that puts soft hyphens (aka <a href="optional-hyphens.html" class="xref">optional hyphens</a>) in the text. Soft hyphens are well supported in web browsers, even browsers that don’t support CSS hyphenation (e.g., desktop Chrome). This also allows somewhat more control over hyphenation. But it’s more work. If your project demands full justification, this might be worth it. Otherwise, probably <span class="no-hyphens">not.</span>

</div>

</div>

<span id="links"></span>

<div class="gap" style="height:1em">

</div>

</div>

<a href="body-text.html" class="nav"></a>

<div id="prev" class="side">

</div>

<a href="block-quotations.html" class="nav"></a>

<div id="next" class="side">

</div>

<div id="switcher" onmousedown="drag_switcher(event, this)">

<span id="switcher_undock" class="switcher_icon"><span class="icon"></span></span> <span id="switcher_move" class="switcher_icon"><span class="icon"></span></span> <span id="switcher_info" class="switcher_icon" onclick="handle_font_info_click(this)" onmousedown="event.stopPropagation()"><span class="icon"></span></span> <span id="switcher_hide" class="switcher_icon" onclick="move_switcher_inside_toolbar()" onmousedown="event.stopPropagation()"><span class="icon"></span></span>

</div>

<div id="toolbar">

<div id="navtable">

<div class="center">

<a href="page-layout.html" class="box-link">chapter</a>

</div>

</div>

</div>
