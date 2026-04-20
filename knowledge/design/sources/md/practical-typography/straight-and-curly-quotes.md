---
title: "Straight And Curly Quotes"
source: "Butterick's Practical Typography"
author: "Matthew Butterick"
url: "https://practicaltypography.com/straight-and-curly-quotes.html"
---

<div id="content">

<div id="doc">

straight and curly quotesAlways use curly quotes

Straight quotes are the two generic vertical quotation marks located near the return key: the straight single quote (') and the straight double quote (").

Curly quotes are the quotation marks used in good typography. There are four curly quote characters: the opening single quote (‘), the closing single quote (’), the opening double quote (“), and the closing double quote (”).

Windows To use the alt codes, hold down the alt key and type the four-digit character code on your numeric keypad (num lock must be <span class="no-hyphens">activated).</span>

Mac OS Where multiple keys are listed, type them <span class="no-hyphens">simultaneously.</span>

|     |                       | Windows  | Mac OS              | HTML      |
|-----|-----------------------|----------|---------------------|-----------|
| '   | straight single quote | '        | '                   | '         |
| "   | straight double quote | "        | "                   | "         |
| ‘   | opening single quote  | alt 0145 | option + \]         | `&lsquo;` |
| ’   | closing single quote  | alt 0146 | option + shift + \] | `&rsquo;` |
| “   | opening double quote  | alt 0147 | option + \[         | `&ldquo;` |
| ”   | closing double quote  | alt 0148 | option + shift + \[ | `&rdquo;` |

Most bad habits endemic to digital typography are former <a href="typewriter-habits.html" class="xref">typewriter habits</a>. They arose from necessity, not because anyone liked them. After all, were typewriters ever used to typeset books, magazines, or newspapers? <span class="no-hyphens">Nope.</span>

Straight quotes are a <a href="typewriter-habits.html" class="xref">typewriter habit</a>. In traditional printing, all quotation marks were curly. But typewriter character sets were limited by mechanical constraints and physical space. By replacing the curly opening and closing quotes with ambidextrous straight quotes, two slots became available for other <span class="no-hyphens">characters.</span>

Word processors are not limited in this way. You can always get curly quotes. Compared to straight quotes, curly quotes are more legible on the page and match the other characters better. Therefore, straight quotes should never, ever appear in your <span class="no-hyphens">documents.</span>

|                          |       |
|--------------------------|-------|
| "That's a 'magic' shoe." | wrong |
| “That’s a ‘magic’ shoe.” | right |

See <a href="foot-and-inch-marks.html" class="xref">foot and inch marks</a> for the one exception to this <span class="no-hyphens">rule.</span>

Fortunately, avoiding straight quotes is easy: use your word processor’s smart-quote feature, which will substitute curly quotes automatically. Smart quotes are typically turned on by <span class="no-hyphens">default.</span>

<div class="howto">

<div class="howto-name">

How to turn smart quotes on or off

</div>

WordFile → Options → Proofing → AutoCorrect Options → AutoFormat As You Type → check or uncheck "Straight Quotes" with “Smart Quotes”

Mac OS WordWord → Preferences → AutoCorrect → AutoFormat As You Type → check or uncheck "Straight Quotation Marks" with “Smart Quotation Marks”

PagesEdit → Substitutions → check or uncheck Smart <span class="no-hyphens">Quotes</span>

</div>

Smart-quote substitution has been built into word processors for nearly 30 years. That’s why straight quotes are one of the most grievous and inept typographic <span class="no-hyphens">errors.</span>

When you paste or import text with straight quotes in it, your word processor may not always convert the straight quotes properly. Fix <span class="no-hyphens">them.</span>

One caveat: if you’ve corrected any <a href="apostrophes.html" class="xref">apostrophes</a> that appear at the start of a word (Patent ’211, ’70s rock), this tip will goof them up again. So fix the quotes first, then the <span class="no-hyphens">apostrophes.</span>

<div class="howto">

<div class="howto-name">

How to convert all quotes to curly quotes

</div>

1.  Use the search-and-replace function to search for all instances of the straight single quote (') and replace it with the same character—a straight single quote (').

2.  Use the search-and-replace function to search for all instances of the straight double quote (") and replace it with the same character—a straight double quote (").

</div>

Before you say “that won’t do anything”, try it. When your word processor replaces each quotation mark, it also performs the straight-to-curly <span class="no-hyphens">conversion.</span>

<div id="curly-quotes-on-the-web" class="subhead">

[Curly quotes on the web](#curly-quotes-on-the-web)

</div>

You can also enter curly quotes into HTML documents using the key shortcuts above. They’re non-ASCII glyphs, however, so you need to specify a non-ASCII encoding for the file (like UTF‑8), otherwise they’ll get garbled on <span class="no-hyphens">decode.</span>

HTML & CSS have no automatic facility for converting straight quotes to curly. But inserting these characters using HTML escape codes is <span class="no-hyphens">dreary.</span>

If you use a CMS like WordPress, plugins are available that handle this automatically. There are also JavaScript-based converters that work in the browser. If you’re tempted to write your own straight-to-curly converter, reconsider—the good ones cover tricky edge cases that you’re apt to miss on your <span class="no-hyphens">own.</span>

Another option is to use the little-known `q` tag, which automatically appends curly quotes to the enclosed elements. So `<q>Hello</q>` renders as “Hello”. Two caveats. First, a parent element (like `html`) must have a `lang` attribute (like `lang="en"`) so the `q` tag knows what kind of curly quotes to use. Second, this change in markup removes the quote marks from the character stream, and doesn’t help with <a href="apostrophes.html" class="xref">apostrophes</a>, so it may be a long drive for a short day at the <span class="no-hyphens">beach.</span>

<div class="btw">

<div class="btw-title">

by the way

</div>

- Straight quotes are acceptable in email. It’s hard to see the difference between straight and curly quotes on screen at small sizes. And if you’re typing with thumbs on a smartphone, it can be irrationally difficult to insert <span class="no-hyphens">them.</span>

- Some older digital documents are stored with double quotes made of two single quotes (' ') or two grave accents (\`\`). (The grave accent, also sometimes called a backtick, is that character above the tab key you’ve never used.) These can be fixed by adapting the search-and-replace technique described <span class="no-hyphens">above.</span>

- Don’t use quotation marks for emphasis. Use <a href="bold-or-italic.html" class="xref">bold or italic</a>.

- Quotation marks are an area of [vast typographic diversity](http://en.wikipedia.org/wiki/Non-English_usage_of_quotation_marks) among other languages—both the glyphs used and how they’re spaced. Now you know why quote-curling algorithms have to be <span class="no-hyphens">smart.</span>

- Confidential to computer scientists and documentation writers: straight quotes and backticks in software code should never be converted to curly quotes. Those marks are, of course, part of the code syntax and must be reproduced literally. In particular, though fans of LaTeX have often written me to trumpet its typesetting superiority, I’ve never seen any LaTeX-created documentation that’s gotten this <span class="no-hyphens">right.</span>

</div>

</div>

<span id="links"></span>

<div class="gap" style="height:1em">

</div>

</div>

<a href="type-composition.html" class="nav"></a>

<div id="prev" class="side">

</div>

<a href="one-space-between-sentences.html" class="nav"></a>

<div id="next" class="side">

</div>

<div id="switcher" onmousedown="drag_switcher(event, this)">

<span id="switcher_undock" class="switcher_icon"><span class="icon"></span></span> <span id="switcher_move" class="switcher_icon"><span class="icon"></span></span> <span id="switcher_info" class="switcher_icon" onclick="handle_font_info_click(this)" onmousedown="event.stopPropagation()"><span class="icon"></span></span> <span id="switcher_hide" class="switcher_icon" onclick="move_switcher_inside_toolbar()" onmousedown="event.stopPropagation()"><span class="icon"></span></span>

</div>

<div id="toolbar">

<div id="navtable">

<div class="center">

<a href="type-composition.html" class="box-link">chapter</a>

</div>

</div>

</div>
