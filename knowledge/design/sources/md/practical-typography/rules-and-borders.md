---
title: "Rules And Borders"
source: "Butterick's Practical Typography"
author: "Matthew Butterick"
url: "https://practicaltypography.com/rules-and-borders.html"
---

<div id="content">

<div id="doc">

rules & bordersUse sparingly

In traditional printing terminology, a rule is a line; a border is a box. But in word processors and web browsers, they’re variations of the same function. Rules and borders can be applied to pages, paragraphs, or <a href="tables.html" class="xref">tables</a>.

Like <a href="centered-text.html" class="xref">centered text</a>, <a href="bold-or-italic.html" class="xref">bold or italic</a>, and <a href="all-caps.html" class="xref">all caps</a>, rules and borders are best used sparingly. Ask yourself: do you really need a rule or border to make a visual distinction? You can usually get equally good results by increasing the <a href="space-above-and-below.html" class="xref">space above and below</a> the text. Try that <span class="no-hyphens">first.</span>

For borders, set the thickness between half a point and one point. Thinner borders can work on professionally printed goods but are too fine to reproduce well on an office printer or computer screen. Thicker borders are counterproductive—they create noise that upstages the information inside. You want to see the data, not the lines around the <span class="no-hyphens">data.</span>

Edward Tufte coined the word chartjunk to describe markings that are unnecessary to communicate visual information. Thick grid lines are a common kind of <span class="no-hyphens">chartjunk.</span>

Tufte’s excellent books on information design are included in the <a href="bibliography.html" class="xref">bibliography</a>.

<div class="gap" style="height:0.7em">

</div>

<div class="indented">

| Wrong | Athos          | Porthos        | Aramis         |
|-------|----------------|----------------|----------------|
| Phone | (617) 555 1453 | (508) 555 3232 | (603) 555 8490 |
| Cell  | (617) 555 3145 | (508) 555 2323 | (603) 555 8491 |
| Fax   | (617) 555 5413 | (508) 555 4545 | (603) 555 8492 |

</div>

<div class="indented">

| Right | Athos          | Porthos        | Aramis         |
|-------|----------------|----------------|----------------|
| Phone | (617) 555 1453 | (508) 555 3232 | (603) 555 8490 |
| Cell  | (617) 555 3145 | (508) 555 2323 | (603) 555 8491 |
| Fax   | (617) 555 5413 | (508) 555 4545 | (603) 555 8492 |

</div>

Similarly, don’t use patterned borders (i.e., anything other than a single solid line, like dots, dashes, or double lines). They’re unnecessarily <span class="no-hyphens">complicated.</span>

With rules, you have more latitude because they don’t accumulate the way borders do. If you want to make a rule thicker than one point or use a pattern, go ahead. But thick or patterned rules still wear out their welcome faster than the classic half-point solid <span class="no-hyphens">rule.</span>

<div class="howto">

<div class="howto-name">

How to edit rules & borders

</div>

WordHome tab → Paragraph panel → look for the button that resembles a windowpane → click the arrow on the right edge → select Borders and <span class="no-hyphens">Shading</span>

PagesClick inside the table and press ⌘ + a to select all cells. Then do View → Show Toolbar (or option + ⌘ + t) → Format button → Cell pane → use the controls under Border

CSSUse the `borders` property. To get borders only between columns, set the `border-left` property on the `td+td` selector. To get borders only between rows, set the `border-top` property on the `tr+tr` <span class="no-hyphens">selector.</span>

</div>

Never make rules and borders out of repeated typographic characters, like punctuation, <a href="hyphens-and-dashes.html" class="xref">hyphens and dashes</a>, or <a href="math-symbols.html" class="xref">math symbols</a>. Especially ridiculous is the habit in certain offices of using stacked parentheses to make a vertical line. Not only is it uglier than a vertical rule, it’s much harder to assemble. These are <a href="typewriter-habits.html" class="xref">typewriter habits</a>. They’re <span class="no-hyphens">obsolete.</span>

<div class="btw">

<div class="btw-title">

by the way

</div>

- If you attach a rule to <a href="headings.html" class="xref">headings</a>, try putting it above the heading (rather than below, which is usually the default). Then the rule will separate the end of the previous section and the current heading, instead of separating the current heading from its own <span class="no-hyphens">section.</span>

</div>

</div>

<span id="links"></span>

<div class="gap" style="height:1em">

</div>

</div>

<a href="tables.html" class="nav"></a>

<div id="prev" class="side">

</div>

<a href="space-above-and-below.html" class="nav"></a>

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
