---
title: "Why Racket Why Lisp"
source: "Butterick's Practical Typography"
author: "Matthew Butterick"
url: "https://practicaltypography.com/why-racket-why-lisp.html"
---

<div id="content">

<div id="doc">

Why Racket? Why Lisp?

This book was made possible by a publishing system called [Pollen.](http://pollenpub.com) I created Pollen with the [Racket](http://racket-lang.org) programming language. Racket is a descendant of [Scheme,](http://schemers.org/) which in turn is a descendant of <span class="no-hyphens">Lisp.</span>

An [updated version](https://beautifulracket.com/appendix/why-racket-why-lisp.html) of this piece is part of [Beautiful Racket,](https://beautifulracket.com/) my book about making programming languages with <span class="no-hyphens">Racket.</span>

So while Racket is not Lisp (in the specific Common Lisp sense), it is *a* Lisp (in the familial sense) which means that its core ideas—and core virtues—are shared with Lisp. So talking about Racket means talking about <span class="no-hyphens">Lisp.</span>

In practical programming projects, Lisps are rare, and Racket especially so. Thus, before I embarked on my Lisp adventure, I wanted to understand the costs & benefits of using a Lisp. Why do Lisps have such a great reputation, but so few users? Was I seeing something everyone else missed? Or did they know something I didn’t? To find out, I read whatever I could find about Lisps, including Paul Graham’s *Hackers & Painters* and Peter Seibel’s *Practical Common Lisp*. (OK, parts. It’s a big <span class="no-hyphens">book.)</span>

What I found was plenty of Lisp flattery from expert Lisp programmers. (Also plenty of Lisp kvetchery from its detractors.) What I didn’t find were simple, persuasive arguments in its favor. So here’s why Racket was the right tool for this project, and what I see as the practical virtues of Lisps in <span class="no-hyphens">general.</span>

<div id="consider-the-source" class="subhead">

[Consider the source](#consider-the-source)

</div>

I didn’t study computer science in college (though I was a math major for two years, before switching to design). I’ve never held an official job as a programmer. Rather, programming has been a secondary skill I’ve used in my work as a web designer, type designer, and <span class="no-hyphens">writer.</span>

These days, I spend an increasing amount of my time programming. This programming generates income. So by the simplest definition—does the skill make you money?—I suppose I qualify as a professional programmer. And since most of my programming efforts are in Racket, I qualify as a professional Racket <span class="no-hyphens">programmer.</span>

Mind you, I’m not claiming that I’m a *good* programmer. (You can [decide for yourself.](http://pollenpub.com)) Among the Racket community, which is laden with computer-science PhDs & professors, I (have no choice but to) embrace my relative ignorance. Hence the title of my talk at [RacketCon 2014:](http://con.racket-lang.org/) *Like a Blind Squirrel in a Ferrari*.

Yet despite my flaws as a programmer, with Racket I’ve been able to render bigger ideas into programs more quickly, and with fewer bugs, than any language I’ve used before (and there have been many—Basic, C, C++, Perl, Java, JavaScript, Python, and others). Since I haven’t gotten a brain transplant recently, there must be something special about Racket as a <span class="no-hyphens">language.</span>

<div id="if-youre-not-familiar-with-lisp" class="subhead">

[If you’re not familiar with Lisp](#if-youre-not-familiar-with-lisp)

</div>

Lisp is a language most programmers have heard of, for two reasons. First, it’s one of the oldest computer languages, in use since 1958. Second, it’s accrued a reputation as a language for brainiacs. Originally this reputation arose from its association with the field of artificial intelligence. Since then, this reputation has been maintained by periodic endorsements from respected programmers (latterly, [Eric Raymond](http://www.catb.org/esr/faqs/hacker-howto.md) and [Paul Graham](http://www.paulgraham.com/avg.html)) and the enduring fame of the textbook used in introductory computer-science courses at MIT, *[Structure and Interpretation of Computer Programs](http://mitpress.mit.edu/sicp/)* (which uses Scheme, and that one I did read start to <span class="no-hyphens">finish).</span>

But as mainstream programming tools, Lisp and its descendants have been largely ignored. Popularity of programming languages is tricky to measure, but here’s a simple proxy—let’s count the number of projects currently hosted on [GitHub.](http://github.com) One could quibble about the accuracy of this method, except that the results aren’t even <span class="no-hyphens">close:</span>

| Language    | GitHub projects |
|-------------|-----------------|
| JavaScript  | 885,467         |
| Java        | 644,711         |
| Ruby        | 622,088         |
| Python      | 432,533         |
| PHP         | 420,913         |
| C           | 218,287         |
| Clojure     | 21,108          |
| Common Lisp | 6883            |
| Scheme      | 5128            |
| Racket      | 2727            |

The last four languages are Lisps, and together account for only 35,846 projects. Racket itself only accounts for a small fraction of this small <span class="no-hyphens">fraction.</span>

“\[JavaScript\] has a lot of stupid in it …   
The good parts of \[JavaScript\] go back to Scheme and Self”  
—Brendan Eich,  
[here](http://www.jwz.org/blog/2010/10/every-day-i-learn-something-new-and-stupid/#comment-1020) and [here](http://www.jwz.org/blog/2010/10/every-day-i-learn-something-new-and-stupid/#comment-1089)

Popular programming languages aren’t necessarily good—look what’s at the top of that list—but unpopular languages often have fatal flaws that prevent wider adoption. As I was considering languages, Racket had a lot to recommend it. But was there a fatal flaw I was overlooking? And by committing to a Lisp, would I be painting myself into a corner? I wanted to understand the risks and <span class="no-hyphens">benefits.</span>

<div id="flattery-gets-you-nowhere" class="subhead">

[Flattery gets you nowhere](#flattery-gets-you-nowhere)

</div>

I said above that Lisp flattery is easy to find. The problem with Lisp flattery is that it makes sense only to experienced Lisp programmers. To others—especially those who are trying to decide whether to learn and use a Lisp—it just comes across as unsubstantiated <span class="no-hyphens">hoodoo.</span>

For example, in his essay *[How to Become a Hacker,](http://www.catb.org/esr/faqs/hacker-howto.html)* Eric Raymond says “Lisp is worth learning for … the profound enlightenment experience you will have when you finally get it. That experience will make you a better programmer for the rest of your days, even if you never actually use Lisp itself a lot.” Unfortunately Raymond doesn’t follow up this claim with a description of the “enlightenment experience”, nor why it’s “profound”, nor how it will improve your programming skills <span class="no-hyphens">generally.</span>

To be fair, Raymond’s essay is not focused on Lisp. But compare *[Beating the Averages,](http://www.paulgraham.com/avg.html)* by Paul Graham, which is. Graham starts off by citing Raymond’s compliment to Lisp and seems ready to make the claim <span class="no-hyphens">concrete.</span>

Instead, he breaks it into smaller chunks of flattery. “We knew Lisp was a really good language for writing software quickly.” Because of what characteristics? He doesn’t say, but then describes Lisp as his “secret weapon”. OK, so what’s the secret? He says “programming languages vary in power”. Fine, but what exactly makes Lisp more <span class="no-hyphens">powerful?</span>

Graham offers one concrete example: Lisp’s macro facility, which he describes as its ability to make “programs that write programs”. After 18 months using a Lisp language, I’d agree with Graham that macros are great when you need them. But for someone new to Lisp languages, they’re not a bread-and-butter benefit. (They only make it to \#8 on my list of favorite features <span class="no-hyphens">below.)</span>

I was hopeful when I opened Peter Seibel’s *[Practical Common Lisp](http://www.gigamonkeys.com/book)* and saw that the [introduction](http://www.gigamonkeys.com/book/introduction-why-lisp.html) was subtitled “Why Lisp?” Yes, tell me! Seibel echoes Graham’s claim: “You’ll get more done, faster, using \[Lisp\] than you would using pretty much any other language.” OK, but how? Seibel wonders whether “I like Lisp because of some quirk in the way my brain is wired. It could even be genetic, since my dad has it too.” That’s not encouraging to those of us outside your family. Ultimately, he sums up the appeal of Lisp by describing it as “the programmable programming language”. But I’ve never used a programmable programming language. Why should I <span class="no-hyphens">start?</span>

And by the way, when do I get the speed and power you keep <span class="no-hyphens">promising?</span>

In short—*what’s in it for me, <span class="no-hyphens">now?</span>*

This is the fundamental question that Lisp advocates have to answer for new users. But more often, it’s sidestepped. I’m not picking on Raymond or Graham or Seibel. They’re excellent writers, and as programmers, they’re way out of my league. As I learn more about Lisps, I return to these pieces and they make more <span class="no-hyphens">sense.</span>

But these pieces are also emblematic of a general weakness of messaging about Lisp. I say that not as a ranking member of the Lisp community, but rather as someone who spent a lot of time seeking an answer to that fundamental question. I never got <span class="no-hyphens">it.</span>

Seibel is passing the buck when he says that to understand the benefits of Lisp, “you’re going to have to learn some Lisp and see for yourself”. Sure, this method works—using Racket for a few months finally made the benefits of Lisp clear to me. But it also requires an investment of about 100–200 <span class="no-hyphens">hours.</span>

<span class="no-hyphens">For more on the perils of taxing reader patience, see  
<a href="why-does-typography-matter.html" class="xref">why does typography matter</a>.</span>

That’s asking too much. If Lisp languages are so great, then it should be possible to summarize their benefits in concise, practical terms. If Lisp advocates refuse to do this, then we shouldn’t be surprised when these languages remain stuck near the bottom of the <span class="no-hyphens">charts.</span>

<div id="so-really--whats-in-it-for-me-now" class="subhead">

[So really—what’s in it for me, now?](#so-really--whats-in-it-for-me-now)

</div>

In a word, *expressiveness:* the measure of how easy it is to put your ideas into code. For instance, an expressive language like Racket lets you write the “Hello world” program like <span class="no-hyphens">this:</span>

`"Hello world"`

Whereas a less expressive language—I won’t name names—requires <span class="no-hyphens">this:</span>

`public class HelloWorld {`  
`    public static void main(String[] args) {`  
`        System.out.println("Hello world");`  
`    }`  
`}`

Concision is valuable, but expressiveness also embodies other qualities: precision, readability, flexibility, potential for <span class="no-hyphens">abstraction.</span>

Me, before <span class="no-hyphens">Racket.</span>

Compared to other languages, Lisps are tremendously expressive. Like the overpowered Japanese motorcycle I once owned, they go where you want, very quickly, with a minimum of input. If you’ve ridden a motorcycle, then you know what I mean. If you haven’t, good news—Lisps are cheaper and <span class="no-hyphens">safer.</span>

Here’s my ranking of the language features that have offered the most immediate value to me, a programmer new to the Lisp world. For each, I’ve noted whether it’s a feature of Racket specifically, or Lisps <span class="no-hyphens">generally.</span>

1.  **Everything is an expression.** \[Lisps\] Most programming languages are a combination of two syntactically distinct ingredients: *expressions* (things that are evaluated to produce a value) and *statements* (things that express an action). For instance, in Python, `x = 1` is a statement, and `(x + 1)` is an <span class="no-hyphens">expression.</span>

    Statements and expressions are distinct because while expressions can be naturally nested with each other, statements and expressions cannot. For instance, in Python, this is still a valid <span class="no-hyphens">expression:</span>

    `(x + (y + `<span class="no-hyphens">`1))`</span>

    but this is <span class="no-hyphens">not:</span>

    `(x + (if is_true(): 1 else: `<span class="no-hyphens">`2))`</span>

    because the if–else conditional is a statement, and can only be used in certain <span class="no-hyphens">positions.</span>

    By making everything an expression, however, Lisps remove this limitation. Since expressions are nestable, anything in the language can be combined with nearly anything else. For instance, because an if–else conditional is an expression, you can use it in place of a <span class="no-hyphens">value:</span>

    I’m using infix notation to make a visual analogy. Lisps typically use prefix notation, with the function at the front: `(+ x (+ y `<span class="no-hyphens">`1))`</span>

    `(x . + . (if (is_true) 1 `<span class="no-hyphens">`2)`</span>

    You could also use a conditional in place of an <span class="no-hyphens">operator:</span>

    `(x . (if (wants_sum) + *) . `<span class="no-hyphens">`1)`</span>

    You could even nest another conditional within <span class="no-hyphens">that:</span>

    `(x . (if ((if (cond) cond_1 cond_2)) `<span class="no-hyphens">`...)`</span>

    And so forth. This is a synthetic example. The point is not that you’d necessarily want to do this, but that Lisps permit it. As a programmer, this both simplifies your work (because everything snaps together easily) and expands your possibilities (because you can combine parts of the language in unusual ways if you feel like <span class="no-hyphens">it).</span>

    It’s similar to the basic idea behind Legos. Other building sets offer specialized pieces that can only fit together certain ways. But by sharing uniform measurements, Lego bricks offer maximum possibilities for combinations. This ends up being more flexible & more <span class="no-hyphens">fun.</span>

    So it is with an expression-based language. If you find this idea exciting, congratulations—you might be a Lisp programmer. (If you find this idea weird and scary, this is a good moment to [bail out.](http://www.buzzfeed.com/search?q=puppies))

2.  **Every expression is either a single value or a list.** \[Lisps\] Single values are things like numbers and strings and hash tables. (In Lisps, they’re sometimes called *atoms*.) That part is no big <span class="no-hyphens">deal.</span>

    The name “Lisp” is derived from “list <span class="no-hyphens">processing”.</span>

    The list part, however, is a big deal. In a language like Python, the list is one data type within the language. But in Lisps, the list is more like an organizing principle for everything that happens. So yes, you can use the list as a data type. But a function call is also a list. In fact, the source code for the function is a list. Actually, the rest of the program is too. Lists are everywhere. (The fancy CS term for this property is *homoiconicity*.)

    The benefits of lists are similar to that of expressions. By bringing more of the language into a consistent form, more possibilities arise for how pieces can be combined and <span class="no-hyphens">manipulated.</span>

    Seibel describes Lisp as a tool for getting “more done, faster”. Here, you can start to see why this is so. Lisp languages are immensely flexible and permissive in how their pieces can be connected. This means that the way you *think* about a programming problem can be quite close to the way you actually program it. (This is also why Lisps have traditionally excelled for prototypes and exploratory <span class="no-hyphens">work.)</span>

    To be fair, getting the most out of a Lisp means learning to think more in the Lisp idiom of lists and expressions. So I can see why Seibel says that trying it yourself is the best way to be convinced of the benefits. As you get a feel for lists and expressions, it does pay increasing dividends throughout the language. You see how tiny lines of code can produce epic amounts of work. You also start to appreciate that even in a well-designed language like Python, you’re spending a lot of time shaping your ideas to fit its limitations, like shaving an invisible <span class="no-hyphens">yak.</span>

3.  **Functional programming.** \[Lisps\] Yes, I know that other languages offer functional-programming features, and that Lisps aren’t considered pure functional languages. But many programmers haven’t been exposed to this idiom, and thus tend to underrate its benefits. I know I was in that <span class="no-hyphens">category.</span>

    Functional programming doesn’t mean programming with functions. Everybody does that. Functional programming refers to a stricter style where functions receive certain data as input, process only that data, and return a result. In functional programming, functions avoid two habits common in other languages: *data mutation* (= changing data in-place rather than returning a value) and relying on *state* (= extra context that’s not provided as input, for instance global <span class="no-hyphens">variables).</span>

    “Wait—I love state and data mutation. Why would you take them away?” Because they’re false friends. They contradict the essential concept of a function, which is to encapsulate data and algorithms. When a function relies on state or mutation, it’s operating outside those boundaries. You either take on an increasing housekeeping burden to keep track of how functions affect each other, or watch the program sink into a swamp of mysterious, complicated <span class="no-hyphens">bugs.</span>

    Programming in a functional style takes more effort at the outset. But it encourages you to structure the program in a clean, compartmentalized way. This pays off immediately in programs that are easier to test and debug. It’s also more likely to lead to reusable components, since functions are truly <span class="no-hyphens">independent.</span>

    This bite-the-bullet aspect of functional programming is another reason why you can get “more done, faster” with a Lisp. The difference between prototype and production code often ends up being small, because you don’t take as many shortcuts at the start. The program grows and evolves more smoothly because it’s easy to change one part without causing ripple effects <span class="no-hyphens">elsewhere.</span>

4.  **Libraries & documentation.** \[Racket\] This might not look like a competitive differentiator—doesn’t every programming language have libraries & <span class="no-hyphens">documentation?</span>

    Yes, but probably not like this. As a consequence of being used in research settings for many years—Racket’s core development team is mostly CS professors—Racket’s libraries & docs are more like a transmission from a highly evolved alien <span class="no-hyphens">intelligence.</span>

    You get the essentials, of course: [web server,](http://docs.racket-lang.org/web-server-internal/index.html) [JSON,](http://docs.racket-lang.org/json/index.html) [XML,](http://docs.racket-lang.org/xml/index.html) [drawing,](http://docs.racket-lang.org/draw/index.html) [foreign-function interface,](http://docs.racket-lang.org/foreign/index.html) and so on. Then you notice packages you maybe didn’t expect: [GUI application framework,](http://docs.racket-lang.org/framework/index.html) [math plotting,](http://docs.racket-lang.org/plot/index.html) [package-distribution system,](http://docs.racket-lang.org/pkg/index.html) [unit tester.](http://docs.racket-lang.org/rackunit/index.html) Beyond that, your face starts to melt a little bit: [semantics engineering?](http://docs.racket-lang.org/redex/index.html) [Futures <span class="no-hyphens">visualizer?</span>](http://docs.racket-lang.org/future-visualizer/index.html)

    I won’t pretend to know what all this shit does. A lot of it is over my head. But I like that. Each week I use Racket, I end up exploring a new part of the library, and learning something new. As opposed to other languages that seem to kill brain cells on contact (= pretty much anything named \*Script, I <span class="no-hyphens">find).</span>

    If you don’t like the design of the docs, blame me—that’s my major contribution to Racket thus <span class="no-hyphens">far.</span>

    This learning is only possible because of Racket’s truly outstanding documentation. It’s vast, thorough, precise, and approachable. [See for <span class="no-hyphens">yourself.</span>](http://docs.racket-lang.org/)

5.  **DrRacket.** \[Racket\] Yes, I know how to use a command line. But Racket includes a cross-platform graphical IDE called [DrRacket](http://docs.racket-lang.org/drracket/index.html) that’s pretty great. DrRacket lets you edit, run, and debug Racket source files (or any other language based on Racket—see item \#9 on this <span class="no-hyphens">list.)</span>

    No, it doesn’t have the Ginsu-level search-and-replace facilities of something like Sublime Text. But it does have helpful editing features optimized for Racket code (for instance, you can right-click on a symbol name and rename it throughout the file, or jump from a function to its <span class="no-hyphens">documentation).</span>

    Moreover, the command line within DrRacket doesn’t just show plain text—it can show stacked fractions, [drawings,](http://docs.racket-lang.org/teachpack/2htdpimage.html) [math plots,](http://docs.racket-lang.org/plot/renderer3d.html?q=plot) and other unexpected guests. If your command line does all that, by all means keep using <span class="no-hyphens">it.</span>

6.  **X-expressions.** \[Lisps\] This choice is somewhat biased by my work with Racket, which mostly involves document processing and typesetting. But related topics arise in most web programming. An X-expression is a special native data structure that Lisps use to represent HTML and other XML-ish <span class="no-hyphens">data.</span>

    Well, not “special” in a Lispy sense—keeping with the usual policy, an X-expression is just another list—but special in the sense that other programming languages don’t have it. Usually your choice is to represent HTML either as a string or as a full XML tree. A string is wrong because it doesn’t capture the structure of the HTML, as defined by its tags and attributes. An XML tree shows this structure, but conceals the sequential nature of the data elements, and is unwieldy to work <span class="no-hyphens">with.</span>

    An X-expression ends up being an ideal hybrid between a string and a tree. Moreover, because it’s just another list-based expression in the language, you have a lot of options for processing it. Translating an X-expression to or from a text representation using angle brackets is trivial and fast. ([Details.](http://pkg-build.racket-lang.org/doc/pollen/second-tutorial.html#%28part._.X-expressions%29))

    Given the close kinship between XML-ish data structures and Lisp languages, I have no explanation why, during the internet era, they’ve not been paired more often. They’re like peanut butter and <span class="no-hyphens">jelly.</span>

7.  **Scribble.** \[Racket\] Pollen wouldn’t have been possible without [Scribble,](http://docs.racket-lang.org/scribble/index.html) so for me, this has been the stone-cold killer feature of Racket. But that won’t be true for everyone, so I’m moving it down on the <span class="no-hyphens">list.</span>

    Scribble was originally created to serve as Racket’s [documentation language](https://www.cs.utah.edu/plt/publications/icfp09-fbf.pdf) (a job it does <span class="no-hyphens">well).</span>

    Scribble is a dialect of Racket that inverts the ordinary relationship of plain text and code: rather than embedding text strings within source, a Scribble document consists of code expressions embedded within plain <span class="no-hyphens">text.</span>

    “So it’s like an HTML template language.” Yes, in the sense that a template language allows code to be embedded in text. But also no, because a template language is usually a pidgin version of a real programming language. Scribble, by contrast, lets you invoke any Racket code simply by adding a command character to the front. In keeping with the theme already established, this approach is both simpler (because there’s almost nothing new to learn) and more powerful (because you can invoke anything in <span class="no-hyphens">Racket).</span>

    In its combination of text and code, Scribble has more kinship with LaTeX. While it doesn’t have the typesetting facilities of LaTeX, the programming facilities are much <span class="no-hyphens">better.</span>

8.  **Macros.** \[Racket\] Also known in Racket as *syntax transformations*. Serious Racketeers sometimes prefer that term because a Racket [macro](http://docs.racket-lang.org/guide/macros.html) can be far more sophisticated than the usual Common Lisp <span class="no-hyphens">macro.</span>

    A macro in Common Lisp is a function that runs at compile-time, accepting symbols as input and injecting them into a template to produce new code. Syntax transformations in Racket, on the other hand, rely on the concept of [hygiene](https://en.wikipedia.org/wiki/Hygienic_macro) and can offer Common Lisp-style macros, but also more elaborate syntax <span class="no-hyphens">rearrangements.</span>

    But forget that—what’s in it for you? As a programmer, you end up getting two bites at the apple every time you run a file: Racket runs the syntax transformations (which alter the source code), and then the source code <span class="no-hyphens">itself.</span>

    Unlike something like the C preprocessor, which is basically a separate mini-language, Racket syntax transformations are themselves Racket functions that give you access to everything in Racket. Like lists and expressions, syntax transformations add another layer of expressive <span class="no-hyphens">possibilities.</span>

9.  **Create new programming languages.** \[Racket\] When I first read that Racket could be used to [create new languages,](http://docs.racket-lang.org/guide/languages.html) I had two thoughts—*are they serious?* and *would I really want to do that?* The answers were *yes* and *oh hell yes.*

    Between expressions, lists, and syntax transformations, Racket gives you a huge amount of semantic flexibility. But on top of that, it also adds syntactic flexiblity, in that you can define a *[reader](http://docs.racket-lang.org/guide/hash-reader.html)* that converts surface syntax into standard <span class="no-hyphens">Racket.</span>

    Paul Graham’s programming language [Arc,](http://arclanguage.org/) a dialect of Lisp, was built on top of <span class="no-hyphens">Racket.</span>

    You can use this facility to make [specialized dialects](http://docs.racket-lang.org/ts-guide/index.html) of Racket. Or implement [earlier languages.](http://docs.racket-lang.org/r6rs/index.html) Or create entirely [new languages](http://docs.racket-lang.org/datalog/datalog.html) with their own rules. You can use any of these languages within DrRacket to code new projects. (These special languages are sometimes called *domain-specific languages*, or *DSLs*.) Scribble is a DSL based on Racket; Pollen is a set of DSLs based on <span class="no-hyphens">Scribble.</span>

    If you’re like most programmers, you’ve never had a tool for making a new language, so you’ve not considered it a realistic approach to a problem. And maybe you’ll never use it. But when you do, it is awesome, in both the new and old senses of that <span class="no-hyphens">word.</span>

10. **Opportunities to participate.** \[Racket\] In theory, open-source software projects create the opportunity for groups of developers to join together and make better things in collaboration than they could <span class="no-hyphens">separately.</span>

    In practice, I’ve found that open-source projects sort into a bimodal distribution: over here, the underdocumented solo projects that sputter along fitfully (if at all); over there, the mature, popular projects that can be intimidating for new <span class="no-hyphens">contributors.</span>

    As an open-source project, [Racket](https://github.com/plt/racket) is positioned at a happy medium. The core development team has been working together for years, and the commits remain [fast & furious.](https://github.com/plt/racket/commits/master) But they’re friendly scientists, not Shire-dwelling egotists, and remain receptive to improvements across the whole system. If you have a better idea, they’ll listen; if you code it up to their standards and make a pull request, they’ll take <span class="no-hyphens">it.</span>

    *\[2021 update: I [no longer contribute](https://beautifulracket.com/appendix/why-i-no-longer-contribute-to-racket.html) to Racket due to abuse & bullying by the project leadership. Everyone in the broader Racket community, however, has always been helpful and <span class="no-hyphens">kind.\]</span>*

The point of this list has been to tell you about the positives. That doesn’t mean there aren’t negatives. The small pool of Racket programmers means that when you hit a pothole, it’s possible no one’s ever seen your problem (= the inverse of [Linus’s Law](http://en.wikipedia.org/wiki/Linus's_Law)). If I wanted to hire a Racket programmer, the options would be <span class="no-hyphens">few.</span>

Still, why shouldn’t I be enthusiastic? What I’ve been able to accomplish so far with Racket has been tremendously useful, educational, and fun—the most fun I’ve had in 25+ years of <span class="no-hyphens">programming.</span>

If you think I sound like a fanboy or cult member, I can live with that. But those are people whose enthusiasm is disproportionate to reality. Here, I’ve tried to stay out of the clouds (and the weeds) and explain the concrete, practical features that have made Racket such a pleasure in my own <span class="no-hyphens">work.</span>

As always, your mileage may vary. But if I persuade a few people to [download Racket](http://racket-lang.org/download/) and try it, I’ll be happy. In fact, if you try it and *don’t* like it, I invite you to <a href="contact.html" class="xref">contact</a> me, because I’m always curious to hear dissenting <span class="no-hyphens">opinions.</span>

I will end by taking on the big <span class="no-hyphens">kahuna—</span>

<div id="does-profound-enlightenment-await" class="subhead">

[Does “profound enlightenment” await?](#does-profound-enlightenment-await)

</div>

I won’t claim I’ve reached the top of the mountain. But I can tell you what the view looks like so <span class="no-hyphens">far.</span>

There’s a sense in which Lisp and its descendants are more than programming languages. They’re tools in the broader intellectual inquiry into the theory of computation. Lisp’s inventor, John McCarthy, originally [considered Lisp](http://www-formal.stanford.edu/jmc/history/lisp.ps) a “way of describing computable functions much neater than the Turing machines”, adapting the notation of lambda calculus to do so. Racket, likewise, has grown out of scientific research and <span class="no-hyphens">exploration.</span>

The theory of computation is just one of many great scientific discoveries in the last 100 years. But I don’t get to use quantum mechanics or relativity or DNA sequencing in my daily work. When I’m programming, however, I’m using <span class="no-hyphens">computation.</span>

Racket, as a Lisp dialect, has many practical benefits. But it also opens a window onto this vast theoretical world that underlies everything we can do with programs. I’m not a brainiac computer scientist. But some days, through that window, I can start to see a bit of what they see—some math, some science, a lot of truth, and more than a little beauty and <span class="no-hyphens">mystery.</span>

Paul Graham calls Lisp a “secret weapon”. I would clarify: Lisp itself isn’t the secret weapon. Rather, *you* are—because a Lisp language offers you the chance to discover your potential as a programmer and a thinker, and thereby raise your expectations for what you can <span class="no-hyphens">accomplish.</span>

If that’s not a step toward enlightenment, I don’t know what <span class="no-hyphens">is.</span>

<div id="further-reading" class="subhead">

[Further reading](#further-reading)

</div>

The aforementioned *[Structure and Interpretation of Computer Programs](http://mitpress.mit.edu/sicp/)* deserves every compliment it gets. It’s mind-bendingly great, and accessible to anyone with a mild curiosity about software. By using Scheme to illustrate meta-topics about programs, it impliedly makes a great case for <span class="no-hyphens">Lisps.</span>

Likewise, Peter Norvig’s *[Paradigms of Artificial Intelligence Programming](http://norvig.com/paip.html)* is not intended as a general introduction to Lisp, but it ends up doing that job well, by showing how sophisticated programs can arise from small constructions of Lisp <span class="no-hyphens">code.</span>

As I’ve already mentioned, Racket’s documentation is consistently excellent. Simply reading through *[The Racket Guide](http://docs.racket-lang.org/guide/index.html)* and trying some examples is <span class="no-hyphens">rewarding.</span>

I explain more about why Racket was essential for Pollen in the [Pollen <span class="no-hyphens">documentation.</span>](http://pkg-build.racket-lang.org/doc/pollen/)

<div id="getting-racket" class="subhead">

[Getting Racket](#getting-racket)

</div>

If you want to try Racket, you can download [the current stable version](http://racket-lang.org/download/) (easy), [a nightly build](http://www.cs.utah.edu/plt/snapshots/) (easy), or [compile it from source](https://github.com/plt/racket) (slightly daunting the first time but then <span class="no-hyphens">easy).</span>

—Matthew Butterick  
20 Aug <span class="no-hyphens">2014</span>

<div class="btw">

<div class="btw-title">

by the way

</div>

- At RacketCon in September 2014, I gave a short talk about Pollen, typography, and digital bookmaking. Here’s [the <span class="no-hyphens">video.</span>](http://youtu.be/IMz09jYOgoc)

</div>

</div>

<span id="links"></span>

<div class="gap" style="height:1em">

</div>

</div>

<a href="economics-year-one.html" class="nav"></a>

<div id="prev" class="side">

</div>

<a href="billionaires-typewriter.html" class="nav"></a>

<div id="next" class="side">

</div>

<div id="switcher" onmousedown="drag_switcher(event, this)">

<span id="switcher_undock" class="switcher_icon"><span class="icon"></span></span> <span id="switcher_move" class="switcher_icon"><span class="icon"></span></span> <span id="switcher_info" class="switcher_icon" onclick="handle_font_info_click(this)" onmousedown="event.stopPropagation()"><span class="icon"></span></span> <span id="switcher_hide" class="switcher_icon" onclick="move_switcher_inside_toolbar()" onmousedown="event.stopPropagation()"><span class="icon"></span></span>

</div>

<div id="toolbar">

<div id="navtable">

<div class="center">

<a href="commentary.html" class="box-link">chapter</a>

</div>

</div>

</div>
