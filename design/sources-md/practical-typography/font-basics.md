---
title: "Font Basics"
source: "Butterick's Practical Typography"
author: "Matthew Butterick"
url: "https://practicaltypography.com/font-basics.html"
---

<div id="content">

<div id="doc">

font basicsfrequently asked questions

<div id="what-are-fonts" class="subhead" style="margin-top:0">

[What are fonts?](#what-are-fonts)

</div>

Fonts control the visual appearance of all text rendered by a computer. Every word you read on screen—whether through your word processor, web browser, or mobile app—uses a font. As does every word that the computer <span class="no-hyphens">prints.</span>

Fonts are not programs, like your word processor or web browser. They’re static data files, like MP3s or PDFs. Each font file contains information that defines the shapes of the letters, plus spacing, <a href="kerning.html" class="xref">kerning</a>, <a href="opentype-features.html" class="xref">OpenType features</a>, and so on. There’s one font file for each style in the family. (A style means one visual variant, like roman, italic, bold, <span class="no-hyphens">etc.)</span>

<div id="why-use-professional-fonts" class="subhead">

[Why use professional fonts?](#why-use-professional-fonts)

</div>

The best professional fonts are better than any <a href="system-fonts.html" class="xref">system font</a> or <a href="free-fonts.html" class="xref">free font</a>—and in ways that everyone, even those who think they don’t have an eye for typography, can appreciate. Though you can’t have the world’s best typographers lay out your documents, you can incorporate their work into your documents with a <span class="no-hyphens">font.</span>

<div id="but-they-cost-money-right" class="subhead">

[But they cost money, right?](#but-they-cost-money-right)

</div>

Right. But as a writing tool, they’re a great value. You can get a top-quality professional-font family for under \$200. These fonts will improve the appearance of every document you create. And unlike most tech purchases, they don’t break, they don’t go obsolete in three years, and they don’t need to be upgraded monthly (if ever). Best of all, you can put them to work without learning anything new. What other hardware or software can you say that <span class="no-hyphens">about?</span>

Really, the hardest thing about using professional fonts is choosing from the thousands available. But once you narrow them down—by practical requirements, by cost, by personal taste—you’ll have a reasonably small set to choose <span class="no-hyphens">from.</span>

<div id="how-do-i-pick-a-font" class="subhead">

[How do I pick a font?](#how-do-i-pick-a-font)

</div>

Since this is an introduction to the world of professional fonts, on the next pages, I’ve taken some fonts that you’re likely familiar with—namely, common system fonts—and chosen some professional fonts that would make good <span class="no-hyphens">alternatives.</span>

Also keep in mind that nearly every font you see in a book, newspaper, or magazine can be licensed for your own use. To figure out the name of the font you’re looking at, see <a href="identifying-fonts.html" class="xref">identifying fonts</a> in the <span class="no-hyphens">appendix.</span>

<div id="how-do-i-buy-fonts" class="subhead">

[how do I buy fonts?](#how-do-i-buy-fonts)

</div>

Fonts are sold online. You can buy fonts either direct from the websites of font designers or from retailers who sell fonts from many designers. There’s not much difference in price, which is in the range of \$20 to 50 per style. After you pay, you download the fonts and install them. For <a href="body-text.html" class="xref">body text</a>, the core styles you will want are roman, italic, bold, bold italic, and roman <a href="small-caps.html" class="xref">small caps</a>.

<div id="about-font-names" class="subhead">

[about font names](#about-font-names)

</div>

Font names are confusing, even for professional typographers. Certain font names (e.g., Myriad, Minion) are trademarked, so their names are distinct. But names of long-dead typographers (e.g., Baskerville, Garamond, Caslon) are not protected, and their names get included in many font names whether the association is apt or not. These names connote nothing about the quality of the font or how it appears on the page. For instance, Stempel Garamond and ITC Garamond are as similar as Bart Simpson and Lisa Simpson. To further complicate the picture, some fonts with trademarked names (e.g., Helvetica, Palatino) have been revised and released under slightly different names (e.g., Helvetica Neue, Palatino <span class="no-hyphens">Nova).</span>

<div class="howto">

<div class="howto-name">

How to install (or remove) fonts

</div>

WindowsStart menu → Control Panel → Fonts. This will open a folder with all your installed fonts. Drag your new fonts into this folder. (To remove fonts, delete font files from this same <span class="no-hyphens">folder.)</span>

Mac OSIn the Applications folder, launch Font Book. Drag your new fonts into the font list. (To remove fonts, delete fonts from the <span class="no-hyphens">list.)</span>

CSSWebfonts are provided either as a remotely hosted resource, or as a set of files that you host on your own server. Either way, once you have access to the file, you establish a name for the font in your CSS with the `@font-face` declaration. After that, you can incorporate it into any of your CSS styles using the `font-family` <span class="no-hyphens">property.</span>

</div>

<div id="how-to-use-fonts" class="subhead">

[how to use fonts](#how-to-use-fonts)

</div>

Once installed, new fonts show up in your font menu along with the usual system fonts. Use them the same <span class="no-hyphens">way.</span>

<div id="respect-your-license" class="subhead">

[Respect your license](#respect-your-license)

</div>

Fonts are software. Like most software, fonts are offered under a license. Fonts are usually licensed per user. The most common way font licenses are violated is when someone buys a single-user license and then shares it with others in the organization. Please—be a good typographic citizen. Buy the number of licenses you need and follow the license <span class="no-hyphens">terms.</span>

<div id="disclosure" class="subhead">

[disclosure](#disclosure)

</div>

I have no financial stake in any of the fonts shown here, except the ones I designed—, , , , , and <a href="advocate.html" class="xref">Advocate</a>.

<div class="btw">

<div class="btw-title">

by the way

</div>

- Most professional fonts are delivered in the OpenType format (.otf extension). Some are offered in the older TrueType format (.ttf). OpenType and TrueType files can be used on either Windows or Mac OS, so the technological distinctions are largely moot. One notable exception: Microsoft Office on Windows, for various historical reasons, still does better with TrueType fonts. So if you’re getting a professional font to use with Office, be sure to get the TrueType <span class="no-hyphens">versions.</span>

- What’s the difference between a font and a typeface? I’ll tell you, then you can forget about it. Historically, typeface referred to the overall family (e.g., Baskerville) and font referred to a specific instance of the family (e.g., 10-point Baskerville Bold Italic). This distinction made sense in the letterpress age, when each font corresponded to a drawer of metal type. But, as lexicographer Bryan Garner has pointed out, “\[t\]echnology has changed the meaning of this term … *font* most often denotes a whole family of styles that can be printed at almost any size.” (Garner’s Modern English Usage, 4th ed., p. 399.) Internet pedants may carp, but it’s fine to use *font* to mean both the family and a specific style. I <span class="no-hyphens">do.</span>

</div>

</div>

<span id="links"></span>

<div class="gap" style="height:1em">

</div>

</div>

<a href="font-recommendations.html" class="nav"></a>

<div id="prev" class="side">

</div>

<a href="equity.html" class="nav"></a>

<div id="next" class="side">

</div>

<div id="switcher" onmousedown="drag_switcher(event, this)">

<span id="switcher_undock" class="switcher_icon"><span class="icon"></span></span> <span id="switcher_move" class="switcher_icon"><span class="icon"></span></span> <span id="switcher_info" class="switcher_icon" onclick="handle_font_info_click(this)" onmousedown="event.stopPropagation()"><span class="icon"></span></span> <span id="switcher_hide" class="switcher_icon" onclick="move_switcher_inside_toolbar()" onmousedown="event.stopPropagation()"><span class="icon"></span></span>

</div>

<div id="toolbar">

<div id="navtable">

<div class="center">

<a href="font-recommendations.html" class="box-link">chapter</a>

</div>

</div>

</div>
