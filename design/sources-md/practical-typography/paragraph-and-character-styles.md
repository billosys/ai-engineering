---
title: "Paragraph And Character Styles"
source: "Butterick's Practical Typography"
author: "Matthew Butterick"
url: "https://practicaltypography.com/paragraph-and-character-styles.html"
---

<div id="content">

<div id="doc">

paragraph and character stylesThe secret to typographic success

Implementing good typography can be a chore and a bore. Paragraph and character styles eliminate most of the <span class="no-hyphens">drudgery.</span>

A full tutorial on implementing styles, either in your word processor or in CSS, is beyond the scope of this book, because so many details are <span class="no-hyphens">software-specific.</span>

But I can tell you the advantages of using styles, which are the same <span class="no-hyphens">everywhere.</span>

Styles are the DNA of document layout. Styles make it easy to control typography across a document or website. They can also be reused across multiple documents or websites. The result is better, more consistent typography with less work each <span class="no-hyphens">time.</span>

Thus, it’s always curious to me that so many writers don’t know how to use styles. They format their documents the old-fashioned way: word by word and paragraph by <span class="no-hyphens">paragraph.</span>

Do you verify your spelling by having a human being read your draft? No, you use an automated spell-checker. Do you copy a document by putting each page on the photocopier glass? No, you put the whole thing in the sheet <span class="no-hyphens">feeder.</span>

Lawyers who believe typography doesn’t matter often never bother to learn to use paragraph and character styles. But this means, ironically, that they end up spending more time fussing with the layout of every document than their typographically enlightened <span class="no-hyphens">colleagues.</span>

If you plan to have a long-term relationship with good typography, I recommend you learn how to use styles <span class="no-hyphens">too.</span>

<div id="why-you-should-care-about-styles" class="subhead">

[Why you should care about styles](#why-you-should-care-about-styles)

</div>

1.  Styles let you *define sets of formatting attributes* that get applied together. So instead of selecting a heading, changing it to 13 point, bold, and all caps, you can define a style that includes these three attributes, and apply the style to the <span class="no-hyphens">heading.</span>

    What’s the benefit? When you come across the next heading, you don’t need to individually apply those three attributes. You apply the style you defined before. The headings will then <span class="no-hyphens">match.</span>

2.  Styles let you *change formatting* across a class of related elements. Suppose you want to change your headings from 13 point to 13.5 point. Instead of selecting each heading separately and changing the point size—a tedious project—you can change the point size in the heading style definition from 13 point to 13.5 point. Headings using that style will be automatically <span class="no-hyphens">updated.</span>

    What’s the benefit? Updating the formatting is centralized and automatic. You can experiment with formatting and layout ideas with little manual <span class="no-hyphens">effort.</span>

3.  Styles can *inherit formatting* from other styles. A change to the parent style will propagate to all the substyles. But a change to the substyle will only affect that one <span class="no-hyphens">style.</span>

    What’s the benefit? Inheritance adds another layer of centralized automation—it’s like having styles of styles. You can define a set of foundation styles and use them as the basis for more elaborate <span class="no-hyphens">styles.</span>

<div id="how-to-use-styles-effectively" class="subhead">

[How to use styles effectively](#how-to-use-styles-effectively)

</div>

In word processors, *character styles* can incorporate attributes of words and sentences, like font, <a href="point-size.html" class="xref">point size</a>, <a href="letterspacing.html" class="xref">letterspacing</a>, <a href="bold-or-italic.html" class="xref">bold or italic</a>, <a href="all-caps.html" class="xref">all caps</a>, and <a href="small-caps.html" class="xref">small caps</a>.

*Paragraph styles* can incorporate those attributes and also layout attributes like <a href="line-spacing.html" class="xref">line spacing</a>, <a href="first-line-indents.html" class="xref">first-line indents</a>, and <a href="rules-and-borders.html" class="xref">rules and borders</a>.

(CSS doesn’t make a distinction between these two kinds of styles, but it’s analogous to styles applied to inline elements (like `<em>`) vs. block-level elements (like `<div>`).)

As a rule of thumb, any time you have two document elements that should be formatted identically, you’ll want to use a <span class="no-hyphens">style.</span>

Initially, you may be inclined to define styles like Caslon Bold 11.5 point. That’s better than applying the same formatting manually. But it overlooks another benefit of styles, which is to define formatting in terms of what each paragraph is used for, rather than how it looks. If you’re creating a style for a block quotation, the name Caslon Bold 11.5 point is not as good as Block Quotation. And later, if you change the formatting, the name will still be <span class="no-hyphens">accurate.</span>

Word processors come with a long list of built-in styles. Word, for instance, has Heading 1 through Heading 9, Quote, Caption, Header, Footer, and so on. Many of these styles are wired into other functions. It’s good practice to modify the built-in styles when possible rather than create new <span class="no-hyphens">ones.</span>

When you do this, you’ll also notice that many built-in styles are woefully ugly. For example, Word’s Header 1 is 14-point blue Cambria, a style with no redeeming qualities. I’m not worried that you’d use it without fixing it first. At this point, you know <span class="no-hyphens">better.</span>

</div>

<span id="links"></span>

<div class="gap" style="height:1em">

</div>

</div>

<a href="grids.html" class="nav"></a>

<div id="prev" class="side">

</div>

<a href="maxims-of-page-layout.html" class="nav"></a>

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
