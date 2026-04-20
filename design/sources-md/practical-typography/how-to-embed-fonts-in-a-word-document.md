---
title: "How To Embed Fonts In A Word Document"
source: "Butterick's Practical Typography"
author: "Matthew Butterick"
url: "https://practicaltypography.com/how-to-embed-fonts-in-a-word-document.html"
---

<div id="content">

<div id="doc">

How to embed fonts in a Word document

Many have told me they’d switch to professional fonts (like those shown in <a href="font-recommendations.html" class="xref">font recommendations</a>) if only they could embed the fonts in a Word document (meaning, the .docx format) so that the typography & layout would be preserved when they send the document to others for further <span class="no-hyphens">editing.</span>

(If you just need your fonts to show up correctly in a PDF, you can ignore the rest of this page and instead read <a href="how-to-make-a-pdf.html" class="xref">how to make a PDF</a>. The instructions below are only necessary for embedding fonts in a Word <span class="no-hyphens">document.)</span>

There’s good news and bad news. The good: contrary to urban legend, it is possible to embed fonts in a Word document. The bad: the technique has some Microsoft-imposed limitations that may make the feature too disappointing to bother with. <span class="no-hyphens">Namely—</span>

1.  Word can only embed fonts on your system that have been installed in the TTF format. If your font files are in the OTF format, you can’t embed them in Word <span class="no-hyphens">documents.</span>

    How do you know which are TTF? It’s the most common format for Windows fonts, but you can verify by double-clicking the font file and looking for the label “TrueType <span class="no-hyphens">outlines”.</span>

    On Mac OS, open Font Book, select the font, and type ⌘I to reveal its info sheet. The “Kind” must be “TrueType”, not “OpenType PostScript”. Unfortunately the most common format for Mac OS fonts is OpenType PostScript, so these can’t be <span class="no-hyphens">embedded.</span>

2.  Confidential to font nerds: embedding permission is controlled by the [fsType flag](https://learn.microsoft.com/en-us/typography/opentype/spec/os2#fstype) in the OS/2 <span class="no-hyphens">table.</span>

    Word can only embed fonts that are marked (by the designer or manufacturer) as permitting embedding. [My fonts](/mb-fonts.html) allow embedding, but many professional fonts unfortunately do <span class="no-hyphens">not.</span>

    How do you know which fonts are so marked? In the Windows font explorer, look for fonts where the “font embeddability” field is set to “editable” or <span class="no-hyphens">“installable”.</span>

    On Mac OS, open Font Book, select the font, and type ⌘I to reveal its info sheet. The “Embedding” value must be “Editable” or <span class="no-hyphens">“Installable”.</span>

3.  Perhaps most infuriating, Word will embed any number of styles per family, but it will only display **one**. Meaning, if you’re using regular, italic, bold, and bold italic in your document, all four styles will be embedded. But when your recipient opens the file, only the regular will display correctly; the italic, bold, and bold italic will be Word-synthesized approximations, not the embedded <span class="no-hyphens">fonts.</span>

This last limitation means that Microsoft Word has reached the exalted state where it is not compatible with itself: it is writing data into its file format that it cannot read. Worst of all, this is not a bug—it’s the [intended <span class="no-hyphens">behavior.</span>](https://learn.microsoft.com/en-us/openspecs/office_standards/ms-oe376/22da0d03-7202-4731-9518-b96bfbe4de61)

“Word synthesizes the bold and italic styles? Doesn’t that change the layout?” Yes. So if you were hoping that embedding the fonts would preserve your layout—because isn’t that the whole point of having font embedding at all?—it won’t. Recipients of your Word document can still open & edit the file. But except for the regular style, the typography will look janky, and the line breaks and page breaks won’t necessarily be <span class="no-hyphens">accurate.</span>

If, having considered these limitations, you conclude that you’d rather not tangle with embedding fonts in Word, I can’t blame you. As for the fog of confusion, rage, and despair—it’s a normal side effect, and will eventually <span class="no-hyphens">dissipate.</span>

For the few <span class="no-hyphens">remaining—</span>

<div class="howto">

<div class="howto-name">

How to embed fonts in a Word document

</div>

WindowsGo to File and select Options from the left-hand menu (if your window is short, it will be stashed under More…). In the resulting “Word Options” box, choose Save from the left side. Scroll to the section named “Preserve fidelity when sharing this document”. Check the box named Embed fonts in this file. Confirm that the other two boxes are not checked (Embed only the characters used … and Do not embed common system fonts).

Mac OSGo to the Word menu, select Preferences…, and then the Save icon (bewilderingly illustrated with a 1980s floppy disk). Under the Font Embedding section, check the box named Embed fonts in this file.

</div>

<div class="btw">

<div class="btw-title">

by the way

</div>

- Read Microsoft’s support articles at your own risk: [“Document font embedding demystified”](https://www.microsoft.com/en-us/microsoft-365/blog/2015/07/06/document-font-embedding-demystified/) and [“How to embed a TrueType font in a <span class="no-hyphens">document”.</span>](https://support.microsoft.com/en-us/topic/how-to-embed-a-truetype-font-in-a-document-883f5212-0c1a-28df-8bb1-21273fa67e7e)

- Officially speaking, Microsoft Office [doesn’t support *any*](https://learn.microsoft.com/en-us/office/troubleshoot/third-party-add-ins/third-party-installed-font-fails-appearing) user-installed fonts on Mac OS. I salute the outlaws who <span class="no-hyphens">persist.</span>

</div>

</div>

<span id="links"></span>

<div class="gap" style="height:1em">

</div>

</div>

<a href="how-to-make-a-pdf.html" class="nav"></a>

<div id="prev" class="side">

</div>

<a href="typewriter-habits.html" class="nav"></a>

<div id="next" class="side">

</div>

<div id="switcher" onmousedown="drag_switcher(event, this)">

<span id="switcher_undock" class="switcher_icon"><span class="icon"></span></span> <span id="switcher_move" class="switcher_icon"><span class="icon"></span></span> <span id="switcher_info" class="switcher_icon" onclick="handle_font_info_click(this)" onmousedown="event.stopPropagation()"><span class="icon"></span></span> <span id="switcher_hide" class="switcher_icon" onclick="move_switcher_inside_toolbar()" onmousedown="event.stopPropagation()"><span class="icon"></span></span>

</div>

<div id="toolbar">

<div id="navtable">

<div class="center">

<a href="appendix.html" class="box-link">chapter</a>

</div>

</div>

</div>
