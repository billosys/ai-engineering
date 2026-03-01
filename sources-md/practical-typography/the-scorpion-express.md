---
title: "The Scorpion Express"
source: "Butterick's Practical Typography"
author: "Matthew Butterick"
url: "https://practicaltypography.com/the-scorpion-express.html"
---

<div id="content">

<div id="doc">

The scorpion express:  
Thoughts on variable fonts

Have you heard the story of the scorpion and the frog? It goes like this: a scorpion wants to cross a river. But he can’t swim. So he asks a nearby frog to carry him across. The frog says, “how do I know you won’t sting me?” The scorpion replies, “Don’t be silly. We’d both <span class="no-hyphens">drown.”</span>

Mollified, the frog invites the scorpion onto his back. Halfway across the river, the scorpion stings him. As the venom paralyzes the frog, he says, “Why did you do that? Now we’ll both <span class="no-hyphens">drown.”</span>

With that, the scorpion unfurls a set of high-tech motorized wings and flies to the other side of the river. With his dying breath, the frog says, “So you’re a rich scorpion? Why did you need me at all?” The scorpion says, “I may be a rich scorpion—but I’m still a <span class="no-hyphens">scorpion.”</span>

If the ending surprises you, maybe you should spend more time on the committees that make technology <span class="no-hyphens">standards.</span>

<div class="gap" style="height:1.5em">

</div>

Last week, an update to the 20-year-old OpenType font standard was announced, officially called [OpenType Font Variations](https://medium.com/@tiro/https-medium-com-tiro-introducing-opentype-variable-fonts-12ba6cd2369#.6zdexe50k) but more commonly known as *variable fonts*. It’s being driven by the usual suspects—Google, Apple, Microsoft, and Adobe. Also participating are an assortment of independent tool developers, and—always valued for their swimming skills—individual type <span class="no-hyphens">designers.</span>

Without diminishing the effort that’s been put into this new standard, I’m not convinced there’s a plausible rationale for it. It would impose significant costs on type designers, provide no obvious advantage to our customers, and mostly benefit a small set of wealthy corporate <span class="no-hyphens">sponsors.</span>

Below, I’ll explain my reasoning. But agree or disagree, I hope other type designers will give this proposed standard the critical scrutiny and reflection it deserves. Because if we end up at the bottom of the river, we won’t be able to say we didn’t know who was riding on our <span class="no-hyphens">back.</span>

<div id="font-interpolation-back-to-the-future" class="subhead">

[Font interpolation: Back to the future](#font-interpolation-back-to-the-future)

</div>

OT Font Variations is an update to the OpenType font format that will allow font files to contain multiple sets of outlines. Today, a single font file can only contain one set of outlines. So a font family with, say, weight and width variants has to be rendered into a matrix of individual <span class="no-hyphens">fonts:</span>

Diagram of the Greta font family by [Peter <span class="no-hyphens">Biľak</span>](https://www.typotheque.com/fonts/greta_text)

But under the new standard, the width and weight variations can be packaged into a single font <span class="no-hyphens">file.</span>

Furthermore, customers will be able to interpolate between styles. So rather than, say, a set of discrete weight <span class="no-hyphens">options:</span>

Weight becomes continuously variable, and a customer can choose anything in <span class="no-hyphens">between:</span>

This idea is not new. In the early ’90s, Apple and Adobe launched competing font-interpolation systems. Apple’s was called [TrueType GX;](http://www.truetype-typography.com/ttgx.htm) Adobe’s was called [Multiple Master fonts.](https://en.wikipedia.org/wiki/Multiple_master_fonts) Apple’s had the advantage of being built into the Mac OS. Adobe’s had the advantage of being supported by PostScript and <span class="no-hyphens">PDF.</span>

In fact, during 1993, I was one of several type designers who worked with Matthew Carter on [Skia,](https://en.wikipedia.org/wiki/Skia_(typeface)) a font with weight and width variants that Apple commissioned to show off TrueType GX. In true time-is-a-flat-circle fashion, Skia [has a starring role](https://www.microsoft.com/typography/otspec180/otvaroverview.htm) in Microsoft’s new OT Font Variations white paper. (Pearl Jam, unfortunately, was not available as an opening <span class="no-hyphens">act.)</span>

“So why haven’t we been using this amazing technology for the last 20 years?” Because it was a [Newton-esque](http://www.oldcomputers.net/apple-newton.html) flop. Beyond the Apple–Adobe taffy pull, professional printers didn’t want to deal with more font headaches (in the ’90s, they already had plenty). And customers were delighted to have *any* kind of selection of digital fonts—the incremental value of interpolated styles was small. Thus, companies that made page-layout programs didn’t want to support GX or MM either. Ultimately, too much cost and not enough <span class="no-hyphens">benefit.</span>

**The lesson:** if the customer doesn’t benefit, no one <span class="no-hyphens">can.</span>

<div id="the-case-for-and-against-obsolescence" class="subhead">

[The case for (and against) obsolescence](#the-case-for-and-against-obsolescence)

</div>

The stagnation of digital-font formats is one of the most nettlesome aspects of type design. OpenType has now been with us for nearly 20 years (its parent, TrueType, has been around for 25). One of the distinguishing features of OT Font Variations is that it’s not meaningfully backward compatible with OpenType. Essentially, it’s a new format that proposes to eventually supplant today’s OpenType font <span class="no-hyphens">families.</span>

(By the way, when I say the new fonts are not “backward compatible”, I mean that they won’t work with operating systems and programs that currently support OpenType. I don’t mean that the new standard will break existing OpenType <span class="no-hyphens">fonts.)</span>

In one sense, it’s interesting to think that the fonts I ship to customers today could be installed and used equally well on a Windows 95 machine. But in most senses, it’s pointless. Because in practice, my fonts will never be used on computers from that <span class="no-hyphens">era.</span>

The converse is not true, however. Fonts made 20 or more years ago are still usable on today’s machines. In fact, they make up the bulk of the [Monotype](http://fonts.com) and [Adobe](http://www.adobe.com/products/type.html) font libraries. Many remain on today’s [bestseller lists.](https://www.fontshop.com/search/families#?order=bestseller) So in fonts, unlike other categories of software, type designers have a peculiar problem: our new work has to compete against decades of accumulated <span class="no-hyphens">competitors.</span>

Is that a good thing? In terms of turning over inventory, no. All technology companies depend on a certain level of obsolescence. It creates recurring revenue, of course. But it also helps avoid the escalating costs and constraints of backward <span class="no-hyphens">compatibility.</span>

Moreover, this is a new situation for type. Long ago, when type was made of wood and metal, it would naturally wear out with use, and need to be replaced. In the 20th century, advancements in typesetting technology meant that font libraries would have to be tossed out and replaced with new formats. So obsolescence was always in the mix. These days, digital fonts seem endlessly <span class="no-hyphens">durable.</span>

Still, these historical comparisons are strained. Now 30 years old, digital typefounding seems mature relative to other digital technology. But relative to other typefounding technology, it’s just a blip. For most of typesetting history, being a typefounder meant spending your career near molten metal and carcinogens, not an Aeron chair and Keurig coffee <span class="no-hyphens">pods.</span>

Furthermore, though in the past I’ve [complained about the persistence of digital fonts,](https://web.archive.org/web/20120106010113/http://fontfeed.com/archives/why-you-should-invest-in-the-future-of-typography/) it veers toward one of my least favorite arguments: the idea that a creative person has a right to make a living from their work. Sorry, but no one does. The market—though [artificial and imperfect](http://www.simonandschuster.com/books/The-End-of-Normal/James-K-Galbraith/9781451644937)—sets the rules. Other fonts exist. Hundreds of thousands, in fact. As type designers, we can either deal with that fact, or find something else to do with our <span class="no-hyphens">time.</span>

To be fair, format stagnation isn’t all bad. As a result of running my own type foundry since 2011, I’ve learned firsthand that no matter how much customers love fonts, they’re looking for a low-maintenance relationship. Possibly complicating this relationship is the fact that fonts are called upon to perform in a countless combinations of operating systems, typesetting programs, and output devices. But in practice, fonts just work. This is miraculous. As an independent type designer, if I had to troubleshoot every setup separately, I couldn’t stay in business. As it stands, I get almost zero support <span class="no-hyphens">requests.</span>

Why is this possible? Because font formats have been so stable for so long. I have to imagine the calculus is similar for other independent type designers. So yes, format stagnation is bad for business in the sense of putting a ceiling on what we can accomplish. But it’s arguably a necessary ingredient for <span class="no-hyphens">independence.</span>

Coming full circle, though it’s tempting to fiddle with the mile-high Jenga tower that comprises today’s font-technology stack, there are risks as well. Not of the [“who moved my cheese”](https://en.wikipedia.org/wiki/Who_Moved_My_Cheese%3F) variety, but rather of customers getting annoyed with newfangled fonts that overpromise and underdeliver. As we’ve discovered, when customers get frustrated with fonts, they [blame type designers.](https://web.archive.org/web/20100107062837/http://diveintomark.org/archives/2009/04/21/fuck-the-foundries) Or they blame corporations, who [in turn blame type designers.](https://support.microsoft.com/en-us/kb/295062) See the pattern? (The most common response to my few requests for technical support is “That problem isn’t being caused by my fonts, but I wish it were, because then I could fix it for <span class="no-hyphens">you.”)</span>

**The lesson:** Be careful what you wish <span class="no-hyphens">for.</span>

<div id="learning-from-opentype" class="subhead">

[Learning from OpenType](#learning-from-opentype)

</div>

Though neither TrueType GX nor Multiple Master fonts caught on, Adobe and Microsoft [collaborated](https://en.wikipedia.org/wiki/OpenType) on the OpenType specification in the mid-’90s. (Apple joined in later.) The impetus for this change was not aesthetic, but practical: in order to support the more complex written languages that are common outside the US and Europe, fonts and layout systems needed to be more sophisticated. And without support for those languages, nobody could sell their products in those parts of the <span class="no-hyphens">world.</span>

Needless to say, with huge economic incentives on the table, the new format took off. Well, sort of: the parts of OpenType that supported new language systems took off quickly. What didn’t were the parts, like <a href="opentype-features.html" class="xref">OpenType features</a>, that improved typography in current language <span class="no-hyphens">systems.</span>

For instance, though the OpenType specification was released in 1996, Microsoft Word didn’t support OpenType features until 2010. Excel and PowerPoint still don’t. Apple stopped supporting OpenType features in Pages for several years, in deference to its iOS version. And today’s crop of web browsers support these features with [different levels of <span class="no-hyphens">competence.</span>](http://caniuse.com/#search=font-feature)

**The lesson:** when customers and corporations definitely benefit (e.g., OpenType language support), designers can too. When customers and designers might benefit (e.g., OpenType typography features), corporations are <span class="no-hyphens">unreliable.</span>

<div id="learning-from-woff" class="subhead">

[Learning from WOFF](#learning-from-woff)

</div>

The last collaboration between the scorpions and the frogs was WOFF (= Web-Only File Format). In 2009, the near-total absence of fonts on the web had become a source of frustration for web designers, who [blamed type designers](https://web.archive.org/web/20100107062837/http://diveintomark.org/archives/2009/04/21/fuck-the-foundries) for embargoing the global font supply, like some scheming Bond villain (Dr. No Kerning? <span class="no-hyphens">Glyphfinger?)</span>

Some type designers, wisely sensing an opportunity for a diplomatic resolution, proposed what became WOFF—a format derived from OpenType that would put fonts into browsers quickly while protecting type-designer interests (mostly, by making it harder to copy and use webfonts on the desktop). Browser makers got involved. The [W3C got involved.](https://www.w3.org/TR/2010/WD-WOFF-20100727/) Soon, WOFF was off to the races. That was the good <span class="no-hyphens">news.</span>

The bad news? Once the dust settled, a type designer who was involved in the effort wrote me that “the foundries who organized behind this effort didn’t get <u>**A SINGLE THING**</u> that they wanted”. (Emphasis in original.) In other words, in terms of issues that mattered to designers, WOFF was a waste of time—even though it was a designer-germinated <span class="no-hyphens">proposal.</span>

I wasn’t involved in WOFF. But it’s no criticism of those who were to observe that this kind of outcome has [never been unusual](https://www.eff.org/deeplinks/2016/06/w3c-eme-and-eff-frequently-asked-questions) at the W3C, or within any standards process. Those who can pay to protect their interests often do. Those who can’t, <span class="no-hyphens">don’t.</span>

Moreover, one of the by-design side effects of a standards process is to achieve political peace with possible future opponents. When you provide opponents an opportunity to be heard, they’re permanently disarmed. How can anyone complain about the result of a process that they participated <span class="no-hyphens">in?</span>

**The lesson:** when customers and corporations benefit, designers should think twice about standing in the way, because our negotiating leverage is <span class="no-hyphens">limited.</span>

<div id="learning-from-woff2" class="subhead">

[Learning from WOFF2](#learning-from-woff2)

</div>

WOFF2 is an update to WOFF that was [first proposed](https://www.w3.org/TR/2014/WD-WOFF2-20140508/) in May 2014. Unlike WOFF Classic, WOFF2 was not a collaboration between type designers and browser makers. It was just something Monotype and Google wanted. And, since they’re [both paying members](https://www.w3.org/Consortium/Member/List) of the W3C, they got <span class="no-hyphens">it.</span>

Why did they want it? The only significant change in WOFF2 was that it added a new compression scheme that can make font files smaller. Why did Google and Monotype want smaller files? Because they’re two of the three biggest providers of hosted webfonts. (The other is Adobe, who [supported it](http://blog.typekit.com/2015/08/26/woff2-support-added-to-typekit/) quickly.) Cut your file sizes = cut your hosting bills. Simple. For customers and designers, it was met with a shrug, since WOFF2 didn’t change anything inside the <span class="no-hyphens">font.</span>

**The lesson:** when corporations benefit, and customers and designers are unaffected, they get what they <span class="no-hyphens">want.</span>

<div id="the-file-size-myth" class="subhead">

[The file-size myth](#the-file-size-myth)

</div>

“But customers benefit from smaller file sizes too, because that makes web pages faster.” Certainly, that was true in 1996. And some web developers persist with [political objections.](http://mrmrs.io/writing/2016/03/17/webfonts/) But with today’s faster connections—even on mobile—optimizing for file size is [less useful than <span class="no-hyphens">ever.</span>](https://www.keycdn.com/blog/web-font-performance/%0A)

Network latency—that is, the number of requests a web page makes to various servers multiplied by how long each takes to establish—is the real bugaboo. In 1996, a web page might have made a few requests to download images. These days, thanks to the [nothing-but-advertising](http://typo.la/bitg) economy of the web, a page might make “hundreds or even thousands of requests to fully load all of the advertisements and analytics”, according to [one study](http://www.forbes.com/sites/kalevleetaru/2016/02/06/why-the-web-is-so-slow-and-what-it-tells-us-about-the-future-of-online-journalism/#78877a53bf60) by *Forbes*.

Together, streaming-video services consume 75% of the internet’s bandwidth. Their support for [net neutrality](https://media.netflix.com/en/press-releases/netflix-applauds-appeals-court-ruling-on-net-neutrality) is mostly about not wanting to pay for what they <span class="no-hyphens">use.</span>

For Google in particular, we should shed a giant crocodile tear whenever it concern-trolls us about file sizes on the web. YouTube (owned by Google) consumes [an astonishing 18%](http://www.businessinsider.com/which-services-use-the-most-bandwidth-2015-12) of all internet bandwidth, second only to Netflix (an eye-watering 37%). The file sizes of fonts—geez, that [seems low on the list](https://www.keycdn.com/blog/web-font-performance/) of the internet’s bandwidth <span class="no-hyphens">problems.</span>

FWIW, since 2013, *Practical Typography* has been an ongoing experiment in extreme webfonting. I’ve pushed about a megabyte of fonts to millions of readers, who are using all kinds of web browsers and platforms (including mobile). Total complaints I’ve received about page performance: zero. Of course, I don’t have ads or trackers either. So it’s a question of <span class="no-hyphens">priorities.</span>

For reasons unclear, this claim about network latency has always provoked [howls of outrage](https://adactio.com/links/11218) among the web-dev Twitterati. Folks, let’s work from evidence, not superstition. For example, here’s a quick test [I did in September 2016,](http://tools.pingdom.com) with home pages ranked in order of load time. As you can see, load time correlates more strongly with number of requests than download size. And *Practical Typography* beats everyone but the world’s biggest corporation. Since I only pay [\$6 a month](http://digitalocean.com) for hosting, I can live with <span class="no-hyphens">that:</span>

| website                 | bytes   | requests | load time |
|-------------------------|---------|----------|-----------|
| apple.com               | 1.9 MB  | 47       | 0.62s     |
| practicaltypography.com | 1.8 MB  | 10       | 1.21s     |
| medium.com              | 1.4 MB  | 55       | 1.37s     |
| alistapart.com          | 0.54 MB | 45       | 1.44s     |
| stackoverflow.com       | 0.36 MB | 43       | 1.60s     |
| microsoft.com           | 1.8 MB  | 119      | 1.87s     |
| youtube.com             | 2.1 MB  | 165      | 2.39s     |
| yahoo.com               | 2.6 MB  | 117      | 2.56s     |
| amazon.com              | 3.9 MB  | 128      | 2.58s     |
| adobe.com               | 2.0 MB  | 218      | 2.65s     |
| nytimes.com             | 5.4 MB  | 501      | 5.20s     |

<div id="new-year-same-rodeo" class="subhead">

[New year, same rodeo](#new-year-same-rodeo)

</div>

“The nice thing about standards is that you have so many to choose from.”  
—Andrew S. <span class="no-hyphens">Tanenbaum</span>

The basic improvement offered by variable fonts—interpolated styles—has already failed twice in the market. What’s the justification to try it all <span class="no-hyphens">again?</span>

With commendable candor, type designer John Hudson, who worked on OT Font Variations, [has tried to address this question.](https://medium.com/@tiro/https-medium-com-tiro-introducing-opentype-variable-fonts-12ba6cd2369#.6zdexe50k) (John is a friend & a terrific type designer, so I’m going to break with protocol and not refer to him as “Mr. <span class="no-hyphens">Hudson.”)</span>

This time, the corporations at the table—Apple, Adobe, Google, Microsoft—have “designed \[the new standard\] collaboratively” rather than pushing multiple standards. That’s the good <span class="no-hyphens">news.</span>

The bad news is that unlike previous evolutions of the TrueType/OpenType lineage, OT Font Variations requires [“substantial updates”](https://medium.com/@tiro/https-medium-com-tiro-introducing-opentype-variable-fonts-12ba6cd2369#.6zdexe50k) to operating systems and applications, and has [“very limited backwards compatibility”.](https://medium.com/@tiro/https-medium-com-tiro-introducing-opentype-variable-fonts-12ba6cd2369#.6zdexe50k) When we see those words, we should conclude that things are about to get very expensive for type designers, and very broken for <span class="no-hyphens">customers.</span>

But sometimes this is the price of progress. What will be the benefit of all this upheaval? [According to John,](https://medium.com/@tiro/https-medium-com-tiro-introducing-opentype-variable-fonts-12ba6cd2369#.6zdexe50k) “a big part of the answer is webfonts, and the need for more compact and faster ways to deliver dynamic fonts for the <span class="no-hyphens">Web”.</span>

That sounds like WOFF2. Sure, corporations that serve a lot of fonts over the network will always want to make them smaller, thereby saving money. But as we saw above, that’s not likely to benefit type designers or <span class="no-hyphens">customers.</span>

Using variable fonts would reduce the number of server requests too, but we can already do that—for instance, by encoding fonts into CSS files with <span class="no-hyphens">Base64.</span>

The file-size savings may be overstated anyhow. For instance, a Microsoft manager [gave the example](https://www.wired.com/2016/09/apple-google-adobe-microsoft-join-forces-make-typographic-history/) that a “a conventional five-weight font family” that uses 656 KB as individual fonts might only weigh 199 KB when repackaged as a variable font. But have you ever seen a website that uses five weights of a single font? Not me. Two weights, however, are very common, and in that case, [it’s not yet clear](http://typedrawers.com/discussion/comment/23062/#Comment_23062) that the new format confers any <span class="no-hyphens">advantage.</span>

What else? The new fonts “[have the potential](https://medium.com/@tiro/https-medium-com-tiro-introducing-opentype-variable-fonts-12ba6cd2369#.6zdexe50k) to enable new kinds of typography for electronic documents, responsive to things like device orientation or even viewing <span class="no-hyphens">distance”.</span>

That sounds like TrueType GX or Multiple Master fonts, which went nowhere with customers, or OpenType typographic features, which went nowhere with corporations who had to build support for them. First, since we’re being candid, most professional graphic and web designers don’t care much about fonts at all. (For instance: [Oxford University Press,](http://global.oup.com/?cc=gb) one of the most respected book publishers, nevertheless sets nearly all its books in [Minion,](http://practicaltypography.com/minion-alternatives.html) a font that every Adobe customer has gotten for free for 20 years.) Second, those that do care about fonts are looking for a low-maintenance relationship, not a lab-monkey experience. Third, think of the struggles that it took to bring fonts to the web at all. Having just reached the point where webfonts have been accepted within the mainstream web, what’s the virtue of breaking everything again? “Potential” is not quite <span class="no-hyphens">enough.</span>

What’s more, font licensing as a business can only be as healthy as the industry it serves. In this case, if variable fonts are largely being pitched as an improvement for the web, we ought to ask: how much money is there is in web publishing? The answer: [not damn much.](http://www.nytimes.com/2016/04/18/business/media-websites-battle-falteringad-revenue-and-traffic.html) (My font-revenue reports for the first six years of the webfont era back that up.) To my mind, that’s another big difference from OpenType in the mid-’90s, which was introduced into what was still a healthy print-publishing industry. (My font-revenue reports back that up too.) As an independent designer, I can’t do much with technological potential unless it also implies revenue <span class="no-hyphens">potential.</span>

What else? Variable fonts “[provide significant advantages](https://medium.com/@tiro/https-medium-com-tiro-introducing-opentype-variable-fonts-12ba6cd2369#.6zdexe50k) for embedding fonts in devices, especially for East Asian (CJK) and other fonts with very large glyph sets and character <span class="no-hyphens">coverage”.</span>

That sounds like the language-support aspects of OpenType. If broadening the market for technology products is the best argument for revising font standards, then this will likely end up being the best rationale for variable fonts. But for type designers who work with Western scripts—which describes the majority of professional type designers, me included—it doesn’t move the needle. The original OpenType spec let us expand our reach into other Western-script markets (e.g., Esperanto and Maltese), because those languages were basically similar to languages we already supported (e.g., English and French). But fonts for East Asian languages are a completely different kettle of <span class="no-hyphens">fish.</span>

In saying that, I take nothing away from the type designers who make East Asian fonts. For them, variable fonts might be huge. Wonderful—may they profit greatly. In time, the Western corner of the type market might even look comparatively small. Wonderful—I will be [doing something else](http://beautifulracket.com/) by <span class="no-hyphens">then.</span>

Before we had webfonts, it was apparent that customers were eager for them, judging by the number of [hacks](https://mikeindustries.com/blog/sifr) [that](cufon%20font) [arose](https://css-tricks.com/typefacejs-a-sifr-alternative/) to approximate them, and the number of [complaints](https://web.archive.org/web/20100107062837/http://diveintomark.org/archives/2009/04/21/fuck-the-foundries) about their absence. There has been no similar activity in the absence of variable <span class="no-hyphens">fonts.</span>

As a designer, I’m sure variable fonts would be entertaining to work with. But from what I can see, there’s no evidence that my customers are interested in that capability—let alone prepared to open their wallets for it. Therefore, the benefits don’t outweigh the significant cost of losing backward compatibility (meaning, packaging font families into a new format that’s not supported by any platforms or applications currently in <span class="no-hyphens">use).</span>

On the contrary, based on historical patterns, it’s easy to imagine a scenario where I spend a lot of time developing variable fonts that basically nobody wants, and the few who do buy them discover that they rarely work as advertised. If this seems sullen or hard-hearted, no—type designers have to make these choices all the time. I often get asked to support new character sets—Greek, Russian, Vietnamese, math & science, and so on. These would all be fantastic projects. But I can’t reach enough paying customers to make any of them worthwhile. If type design were my hobby, I’d be delighted to pursue these projects. But since it’s my work, I have to <span class="no-hyphens">pass.</span>

<div id="so-who-benefits" class="subhead">

[So who benefits?](#so-who-benefits)

</div>

John [also summarizes](https://medium.com/@tiro/https-medium-com-tiro-introducing-opentype-variable-fonts-12ba6cd2369#.6zdexe50k) how far the corporate participants have progressed with variable fonts. With this, we can make some educated guesses about what they’re getting out of <span class="no-hyphens">it:</span>

1.  The “Windows engineering team at Microsoft” is planning to add support for variable fonts in 2017. That sounds great, unless you know anything about the culture at Microsoft, where every division sets their own development agenda, and they basically all [hate each other.](http://www.bonkersworld.net/organizational-charts/) Office is in a separate division from Windows, which is why OpenType support in Office has lagged far behind OT support in Windows: if a feature doesn’t sell more copies of Office, they’re not much interested in implementing <span class="no-hyphens">it.</span>

    Unlike Office, the Edge web browser is part of the Windows division, so it’s likely to support variable fonts sooner. John [notes that](https://medium.com/@tiro/https-medium-com-tiro-introducing-opentype-variable-fonts-12ba6cd2369#.6zdexe50k) the browser team is also working on a “formal proposal for support of variable fonts in Cascading Style Sheets (CSS) for the Web”. Again, that sounds great, unless you know anything about the culture at Microsoft. They’ve always been eager to make web standards, and [never been eager](http://www.theregister.co.uk/2015/07/20/microsoft_edge_good_for_web_sucky_standards/) to support <span class="no-hyphens">them.</span>

    **I predict**: Don’t bet against history. Regardless of Microsoft’s participation in variable fonts, Office may not meaningfully support it for decades; Edge may not meaningfully support the web-standard version of it <span class="no-hyphens">ever.</span>

2.  Apple “[characteristically, \[is\] least forthcoming](https://medium.com/@tiro/https-medium-com-tiro-introducing-opentype-variable-fonts-12ba6cd2369#.6zdexe50k) about future plans, but they have a head start on variable font support in their TrueType GX infrastructure”. GX dates from 1993, so I’m skeptical how much of a technical “head start” Apple really has, when everything else in the Apple ecosystem is completely different. (That was also the last time Apple took any kind of leading role in font technology.) Apple’s business has also completely changed since 1993. Then, they were primarily a desktop-computer company; now, they’re primarily a mobile-phone company. Their support for variable fonts likely reduces to the question of whether it will help them sell more iPhones in China and elsewhere in <span class="no-hyphens">Asia.</span>

    **I predict**: Apple will follow their original OpenType strategy—let everyone else go first, and implement the standard only if it proves to be valuable in the mobile-phone <span class="no-hyphens">market.</span>

3.  Adobe’s font-technology team is [updating its tools](https://medium.com/@tiro/https-medium-com-tiro-introducing-opentype-variable-fonts-12ba6cd2369#.6zdexe50k) for font developers, but there are “no details about support for variable fonts in Adobe’s application suite”. As with Microsoft, Adobe’s application group is a different division with different priorities. I don’t think they hate each other as much. But Creative ~~Suite~~ Cloud is Adobe’s cash cow. They’re not going to let variable fonts mess with those teats. Adobe also carefully protects its relationships with big publishers and printers. They’re not going to let variable fonts foul them up (especially after recent misfires like [Adobe Digital Editions](http://www.adobe.com/solutions/ebook/digital-editions.md)).

    **I predict**: Adobe will exert minimal effort to support variable fonts for Western languages. Though consistent with ’90s nostalgia, they will release versions of Myriad and Minion in the new format (and they *better* bring Pearl Jam to [Adobe MAX](https://max.adobe.com) this year). Otherwise, they’ll reserve most of their effort for supporting variable fonts in East Asian <span class="no-hyphens">fonts.</span>

4.  Finally, Google has [apparently been working](https://medium.com/@tiro/https-medium-com-tiro-introducing-opentype-variable-fonts-12ba6cd2369#.6zdexe50k) on variable-font technology for two years, getting it ready for “Google Chrome \[and\] the Google Fonts webfont platform”. That’s no surprise. First, we know Google saves money with small files. Second, Google Fonts shifted its focus to East Asian scripts a while ago, having conquered the west. Third, because Google spends more freely than Adobe or Microsoft, and they’ve already amassed an army of underpaid type designers, these designers will probably be deployed to convert many existing Google fonts to the new format. These fonts will be [just as terrible](why-google-fonts-arent-really-open-source.md) as the originals. But since Google has no customers in professional publishing, and no taste, everything will still be <span class="no-hyphens">awesome.</span>

    <div class="iframe">

    <div id="player">

    </div>

    <div class="player-unavailable">

    # An error occurred.

    <div class="submessage">

    Unable to execute JavaScript.

    </div>

    </div>

    </div>

5.  **I predict**: Google will continue to be the most vigorous early adopter of variable fonts, but the benefits will be restricted to the <span class="no-hyphens">Googleverse.</span>

<div id="the-customer-is-still-right" class="subhead">

[The customer is (still) right](#the-customer-is-still-right)

</div>

I could’ve discussed problems with specific technical aspects of variable fonts (e.g., if this format won’t be backward compatible, why stick with a binary-table structure held over from the ’80s? Or why is interpolation the only kind of transformation <span class="no-hyphens">supported?)</span>

But there’s no point. Market considerations will always override technical considerations. Thus, to forecast what will happen with variable fonts, it’s far more important to consider the market interests of the stakeholders, rather than the particulars of the format. The *how* is less important than the *what* and *why*.

[As John says](https://medium.com/@tiro/https-medium-com-tiro-introducing-opentype-variable-fonts-12ba6cd2369#.6zdexe50k) in his article, “font makers ... have a long collective memory” about these things. (True.) The downside is that it extends this kind of article to epic length. (Sorry.) The upside is that if you want to know what happens in these situations, there’s a decades-long trail of breadcrumbs for you to study. I’m sure this kind of homework will seem crusty and tedious to those who entered type design more recently than I did. (Sorry about that <span class="no-hyphens">too.)</span>

But look across this history, and a simple principle emerges. It’s a cliché, but as usual, **the customer is always right**. When type designers have accepted what customers want (e.g., better OpenType language support) the market has rewarded us. When type designers have resisted what customers want (e.g., easy access to webfonts) the market has punished <span class="no-hyphens">us.</span>

Why does this principle work? First, because customers pay us—duh. Second, because the corporate participants in the type market have to serve those same customers. Ultimately, they can’t afford to alienate customers any more than we can. So where the customers lead, everyone <span class="no-hyphens">follows.</span>

The corollary to this principle is that when customer demand is removed from the picture, things get murky. In this case, we might ask: if the variable-fonts standard has been built outside the practical influence of customer demand, then who does it <span class="no-hyphens">serve?</span>

The idealist might say that a standard provides a level playing field for market participants. But in practice, standards tend to reflect the interests of whoever has the most weight to throw <span class="no-hyphens">around.</span>

The idealist might also say that new standards are necessary for technological progress. But in the market, the costs of progress end up being strictly weighed against the <span class="no-hyphens">benefits.</span>

Ultimately, I see no evidence that variable fonts are something my customers want. But I see plenty of evidence that it will help Apple, Google, et al. sell more products in certain countries, or save money on bandwidth. I’m sure these corporations would love more help from type designers to make their technology look good. And if you want to go for a swim, don’t let me stop you. But this frog is going to stay right here on the side of the river, where it’s sunny and <span class="no-hyphens">dry.</span>

—Matthew Butterick  
20 Sept <span class="no-hyphens">2016</span>

<div id="industry-update-october-2017" class="subhead">

[Industry update, October 2017](#industry-update-october-2017)

</div>

**Microsoft**: The newest [Windows 10 update](https://msdn.microsoft.com/en-us/library/windows/desktop/mt492454(v=vs.85).aspx) contains an “initial implementation” of variable fonts. (Translation: buggy and incomplete.) *But:* no support yet in Office or the Edge web browser. This, even though [Microsoft claimed](https://www.wired.com/2016/09/apple-google-adobe-microsoft-join-forces-make-typographic-history/) last year that it would “support variable fonts on all its products” by the end of 2017. Microsoft did manage to [ship its first variable font](https://blogs.windows.com/windowsexperience/2017/08/23/announcing-windows-10-insider-preview-build-16273-pc/), Bahnschrift. *Overall:* about what I <span class="no-hyphens">expected.</span>

**Apple**: Since September 2016, a handful of [special-purpose Apple system fonts](https://twitter.com/jenskutilek/status/778344281845141505) have relied on variable fonts. As of last month, the Safari web browser supports variable fonts (on both iOS and Mac OS). *But:* still no support for variable fonts in desktop typesetting applications (like Pages). Nor any showcase variable fonts in the OS. *Overall:* Apple is dragging its feet less than I expected. But they’re not at the front of the pack <span class="no-hyphens">either.</span>

**Adobe**: After I published the original version of this piece, an Adobe employee told me that “for us it really is all about the variation, not the file size savings ... I expect you’ll be pleasantly surprised by support in Adobe apps”. A year later, some progress has emerged. Variable fonts are supported in the newest versions of Photoshop and Illustrator. *But:* so far, that support is [buggy and incomplete.](http://typedrawers.com/discussion/comment/31049/#Comment_31049) And no support at all in Adobe’s flagship page-layout program, InDesign, used by a huge number of professional designers. Perhaps most strangely, Adobe hasn’t released any showcase variable fonts, save for some [“Concept” fonts](https://blog.typekit.com/2017/10/19/new-variable-fonts-from-adobe-originals/) (translation: buggy and incomplete). And none of those are East Asian fonts. *Overall:* even lazier than I <span class="no-hyphens">predicted.</span>

**Google**: Support for variable fonts will be included in the [Chrome 62 browser,](https://blog.chromium.org/2017/09/chrome-62-beta-network-quality.html) which will start percolating out to users this month. Google also funded the development of two free variable fonts ([\#1,](https://www.typenetwork.com/brochure/opentype-variable-fonts-moving-right-along/) [\#2](https://www.typenetwork.com/brochure/decovar-a-decorative-variable-font-by-david-berlow#?skelID=SA&skel=1&termID=TA&term=1)) that are, um, interesting technical demos but not exactly practical. *But:* Google has not made any visible push to convert fonts in its [existing library](https://developers.google.com/fonts/) to use variations technology. *Overall:* I predicted Google would be out in front. But they’ve put in less effort than I expected. [Sorry to be the party <span class="no-hyphens">pooper.</span>](https://twitter.com/behdadesfahbod/status/778751562642436098)

<div class="gap" style="height:1.5em">

</div>

Taken together, a mediocre effort. So far, variable fonts are not emitting the aroma of aggressive action, but rather the milder scent of bets being <span class="no-hyphens">hedged.</span>

The brightest sign is the web-browser support. Chrome and Safari are the [most popular](https://en.wikipedia.org/wiki/Usage_share_of_web_browsers#W3Counter_.28May_2007_to_August_2017.29) web browsers (the others are lingering in the single digits). Given that it took [about 15 years](https://unitscale.com/mb/reversing-the-tide/) to get webfonts in browsers to begin with, that seems like relatively encouraging momentum. Still, even in the best case, it takes months for newer browser versions to displace the <span class="no-hyphens">old.</span>

But the darkest sign is the lack of useful fonts built with variable fonts technology. Google and Adobe have made some demo fonts. But nobody is shipping or showing off solid, usable variable fonts. In fact, one [variable-font demo site](http://www.axis-praxis.org/) is so starved for demo fonts that it includes fonts originally made nearly 25 years ago to show off Apple’s TrueType GX technology (converted to the new <span class="no-hyphens">format).</span>

I’ve heard this called a chicken-and-egg problem: type designers don’t have any incentive to make variable fonts until application support is more widespread. Meanwhile, application programmers don’t have any incentive to update their programs until there’s more <span class="no-hyphens">fonts.</span>

But this overlooks a key fact: this isn’t some grassroots campaign. The technology supporting variable fonts is supposedly backed by four of the biggest tech companies in the world. They have the money and staff to capitalize the effort. If they want <span class="no-hyphens">to.</span>

Do they? The middling progress during the first year of variable fonts leaves me even more confused about how these companies plan to benefit. I [originally figured](#new-year-same-rodeo) it had something to do with reducing the costs of serving webfonts, especially for East Asian scripts. Adding support to web browsers is a necessary first step. But the lack of actual showcase fonts—and simple demo websites using them—is extremely <span class="no-hyphens">weird.</span>

And demos count. An old marketing maxim holds that effective advertising doesn’t talk about the shovel—it talks about the hole in the ground. This is why demos are historically important in the tech world: they help illustrate the benefit of using the technology, which in turn persuades customers that a) it works and b) they want <span class="no-hyphens">it.</span>

Based on their weak output in year one, Microsoft, Apple, Adobe, and Google still seem unable to articulate what customer problems will be solved by variable fonts. If that remains true, this technology will have a short ride to the bottom of the river, coming to rest near the moss-covered skeletons of [Multiple Masters and TrueType <span class="no-hyphens">GX.</span>](#learning-from-opentype)

<div class="gap" style="height:1.5em">

</div>

<div id="industry-update-october-2018" class="subhead">

[Industry update, October 2018](#industry-update-october-2018)

</div>

[In October 2017,](#industry-update-october-2017) I wrote that during the 12 months after OT Variable Fonts [were announced](https://medium.com/@tiro/https-medium-com-tiro-introducing-opentype-variable-fonts-12ba6cd2369#.6zdexe50k) (in Sept 2016) we hadn’t seen “aggressive action” from the four main corporate sponsors of variable fonts (= Microsoft, Apple, Adobe, and Google). Rather, I detected only the “milder scent of bets being <span class="no-hyphens">hedged”.</span>

The underlying revenue model for web publishers hasn’t improved since last year. But we’ll sidestep that wrinkle for <span class="no-hyphens">now.</span>

In year two, this already languid pace has slowed to a crawl. After the first year, the brightest sign for variable fonts was “web-browser support”. Since then, remarkably little has happened, as measured by shipped products. The declining forward momentum that once signaled “bets being hedged” now looks more like tents being <span class="no-hyphens">folded:</span>

**Microsoft**: the [Edge browser](https://blogs.windows.com/msedgedev/2018/03/13/bringing-expressive-performant-typography-to-microsoft-edge-with-variable-fonts/) now supports variable fonts. But [no sign](https://developer.microsoft.com/en-us/microsoft-edge/testdrive/demos/variable-fonts/#shipping%0A) of support in MS Office. Nor any new showcase <span class="no-hyphens">fonts.</span>

**Apple**: no significant news that I can detect. Still no support for variable fonts in desktop apps like Pages or Numbers. No new showcase variable fonts in the <span class="no-hyphens">OS.</span>

**Adobe**: [no news](https://blog.typekit.com/variable-font-technology-from-adobe/) since last October. In particular, still no support for variable fonts in InDesign, Adobe’s flagship typesetting package. Adobe has continued [to plod along](https://github.com/adobe-fonts/adobe-variable-font-prototype) with its experimental variable fonts, though one of the [“current limitations”](https://github.com/adobe-fonts/adobe-variable-font-prototype#current-limitations) is that the OTF versions “cannot be displayed by macOS or <span class="no-hyphens">Windows”.</span>

**Google**: AFAICT the number of variable fonts released this past year via Google Fonts is zero. No support in Google apps (Docs, Slides) either. Once again, [sorry to be the party <span class="no-hyphens">pooper.</span>](https://twitter.com/behdadesfahbod/status/778751562642436098)

Though they weren’t part of the core variable-fonts consortium, what about our friends at **Monotype**? They released a demo version of [FF Meta Variable.](https://www.monotype.com/fonts/variable-fonts/) And also—nope, that’s it. One demo <span class="no-hyphens">font.</span>

<div class="gap" style="height:1em">

</div>

Meanwhile, work on the OT Font Variations standard itself has hit at least one major snag, related to support for what are known as [“virtual axes”.](https://github.com/Microsoft/OpenTypeDesignVariationAxisTags/issues/22#issuecomment-401510073) Without delving into the details, even John Hudson, [original evangelist](https://medium.com/@tiro/https-medium-com-tiro-introducing-opentype-variable-fonts-12ba6cd2369#.6zdexe50k) for variable fonts, [has conceded](http://typedrawers.com/discussion/comment/33872/#Comment_33872) that the issue is sufficiently important that “a lot of \[work with variable fonts\] is effectively on hold” until the problem is resolved. Not exactly the turbo boost that variable fonts could’ve <span class="no-hyphens">used.</span>

<div class="gap" style="height:1em">

</div>

If you’re eager to try variable fonts, the good news is that the [Axis-Praxis](https://www.axis-praxis.org) variable-fonts demo site has continued to grow. It’s been joined by the new [v-fonts.com.](https://v-fonts.com/) Most of the fonts on these sites have been made by independent type designers, who have done more than anyone else to churn out entertaining demo fonts. I compliment all of you. A lot of these variable fonts are very clever and well <span class="no-hyphens">made.</span>

And yet. This is only “good news” in a narrow sense. More broadly, it fulfills my original prediction from two years ago: that the corporate sponsors of variable fonts (= Microsoft, Apple, Adobe, Google) would minimize their effort. Rather than stick out their own necks, they’d let independent type designers donate their time to make variable fonts technology look <span class="no-hyphens">good.</span>

Last year, my friend S. said “MB, you’re being too harsh. There’s a lot of activity happening behind the scenes.” Perhaps. But what’s happening in front of the curtain also counts. Notably, after two years, **customers aren’t paying for variable fonts**. The whole notion of a variable-fonts economy is still theoretical. This key problem remains <span class="no-hyphens">unaddressed.</span>

Though not unexamined. Type designer Johannes Neumeier [considered](https://underscoretype.com/2018/07/05/is-the-future-of-variable-fonts-stuck-in-the-licensing-past/) an interesting thought experiment: if usable variable fonts actually existed, what would they need to cost? [He concluded](https://underscoretype.com/2018/07/05/is-the-future-of-variable-fonts-stuck-in-the-licensing-past/)—and I agree—that variable fonts are “incompatib\[le\] with current licensing models”. Customers won’t want to pay the same for one variable font as they would for, say, a large set of discrete styles, even if the variable font covers the same design space. Though variable fonts have been touted as a bold new future for type design, it’s equally possible that they’ll lead to a new downward spiral of more work for less <span class="no-hyphens">pay.</span>

Still, to give my critic S. her due: I agree I was too harsh. I doubt this doom-and-gloom scenario will come to pass. Why? Because it’s apparent that even if you have essentially unlimited time and money—e.g., you are Microsoft, Apple, Adobe, or Google—it’s still [painfully difficult](https://www.monotype.com/resources/articles/variable-fonts-making-the-promise-a-reality/) to make variable fonts that work well. As proof, consider that other than a handful of special-purpose OS fonts, **not one of these corporate sponsors has shipped a no-caveats variable font**. (Meaning, something that is complete and usable and not labeled a “demo” or “concept”, etc.) I remain dubious that independent type designers should do for huge corporations what these corporations won’t (or can’t) do for <span class="no-hyphens">themselves.</span>

At some point, a well-informed source told me that the corporate sponsors of variable fonts were “basically motivated by one thing only: smaller font footprint”. If so, it’s starting to look like variable fonts are the world’s most labor-intensive—and therefore least practical—file-compression <span class="no-hyphens">scheme.</span>

<div class="gap" style="height:1.5em">

</div>

<div id="2019-update" class="subhead">

[2019 update](#2019-update)

</div>

**Microsoft**: No new applications released with support for variable fonts since the Edge web browser in 2018. (We’ll leave aside the fact that Edge remains [even less popular](https://netmarketshare.com/browser-market-share.aspx) than Internet Explorer.) Microsoft Office? Surely you jest. What about new variable fonts? <span class="no-hyphens">Nope.</span>

**Adobe**: The good news—in November, InDesign [introduced support](https://blogs.adobe.com/creative/adobe-indesign-2020/) for variable fonts. The bad news—early reports suggest that [not all variable fonts](https://mobile.twitter.com/FontFabrik/status/1191671599491174400) work equally well, or more ominously, that Adobe might be [privileging its new CFF2 font format.](https://mobile.twitter.com/jenskutilek/status/1191675176775225346) As for new variable fonts: none that I’ve been able to <span class="no-hyphens">find.</span>

**Apple**: No updates for the iWork office suite (Pages / Numbers / Keynote) with variable fonts. Nor has Apple released any new variable fonts of its <span class="no-hyphens">own.</span>

**Google**: In October, Google [updated](https://twitter.com/googlefonts/status/1185048007781355521) its [font API](https://developers.google.com/fonts/docs/css2) to support variable fonts, including [10 variable upgrades of existing Google fonts.](https://developers.google.com/fonts/docs/css2#list_of_variable_fonts) [Demo <span class="no-hyphens">here.</span>](https://codepen.io/nlwilliams/full/JjPJewp)

Strictly speaking, Microsoft didn’t end up building variable-font support for Edge. In an unexpected turn, it [shifted Edge onto the Chromium browser engine,](https://thenextweb.com/microsoft/2018/12/06/microsoft-edge-is-officially-switching-to-chromium-in-2019-heres-why-thats-a-good-thing/) which already supported variable <span class="no-hyphens">fonts.</span>

In general, my original predictions from 2016 are holding up pretty well. Microsoft, Apple, and Adobe are doing as little as possible to support variable fonts. (Though I was wrong that the Microsoft Edge browser would never support variable fonts—it does.) Meanwhile, Google has indeed become the “most vigorous early adopter of variable fonts, but the benefits \[are\] restricted to the Googleverse.” The reason being that as the world’s biggest server of webfonts, Google potentially saves money with variable <span class="no-hyphens">fonts.</span>

<div class="gap" style="height:1em">

</div>

Still, 3+ years into the variable-font era, it remains unclear how & when the economy of variable fonts is supposed to emerge. Meaning, if type designers can’t make variable fonts at reasonable cost and sell them at a profit to font customers—who have to get their money’s worth—the variable-font market will remain an experimental <span class="no-hyphens">niche.</span>

To be fair, these days Adobe is largely a [digital-marketing company.](https://www.technologyreview.com/s/614727/the-convergence-of-advertising-and-marketing/) Creative Cloud is a side project, and fonts are a side project of that side <span class="no-hyphens">project.</span>

Here, we would’ve hoped to see Adobe leading by example, as the leading purveyor of tools to the pro-design market. The support for variable fonts in InDesign (however spotty) is encouraging. But the total lack of momentum on the type-development side is not. For instance, two years after [the announcement](https://blog.typekit.com/2017/10/19/new-variable-fonts-from-adobe-originals/) of variable-font demos of Acumin, Minion, and Myriad, no apparent progress has been <span class="no-hyphens">made.</span>

This past year, a number of independent foundries—e.g., [Dalton Maag](https://www.daltonmaag.com/library/objektiv) and [Fontsmith](https://www.variable-fonts.com/about)—have started selling what may be the first no-excuses variable-font families. My compliments to you. (FWIW, Dalton Maag has also done [custom font work](https://www.daltonmaag.com/work/google-scope-one) for <span class="no-hyphens">Google.)</span>

In his own year-end report, variable-font optimist (and sometime Google consultant) [Jason Pamental acknowledges](https://rwt.io/typography-tips/what-web-wants) the ongoing “frustration about lack of sales” among type designers and suggests “offering \[customers\] a deal ... in return for having a case study.” You mean—if we work for free, it’ll be great exposure? Where have I heard this before? As I said when I first wrote this piece, there’s little money being made in web publishing. Therefore there’s also little money being put into web-publishing tools, including webfonts. The idea that variable fonts can break even primarily as a web format is magical <span class="no-hyphens">thinking.</span>

Still, if type foundries and their customers don’t adopt variable fonts, the format won’t necessarily die. For instance, variable fonts could mostly become known as a feature of Google Fonts, even as the broader possibility of the format fades away. If variable fonts save Google enough money, Google has ample incentive to keep them <span class="no-hyphens">alive.</span>

<div id="the-google-factor" class="subhead">

[The Google factor](#the-google-factor)

</div>

I mentioned Google’s connection to Dalton Maag and Mr. Pamental. Over the last 10 years—and especially since the announcement of variable fonts—Google has bought a lot of influence in what is the relatively small world of typography. Much more than Apple, Microsoft, and Adobe have <span class="no-hyphens">done.</span>

[Early on,](https://practicaltypography.com/why-google-fonts-arent-really-open-source.html) Google built its free-font library by working with type designers who weren’t typically involved with the professional type world. Since then, Google has learned to spread money around [more liberally.](https://www.typenetwork.com/brochure/opentype-variable-fonts-moving-right-along/) To my mind, this campaign has gotten professional type designers and typographers to take Google more seriously. Though perhaps at the cost of being less careful about scrutinizing Google’s <span class="no-hyphens">motives.</span>

To be fair, Google has done some positive things for typography. As I’ve [said before,](why-google-fonts-arent-really-open-source.html#update-nearly-four-years-later) I think Google’s promotion of webfonts helped spur acceptance within mainstream web design. They’ve also contributed some useful [open-source software](https://github.com/googlefonts) for making <span class="no-hyphens">fonts.</span>

But for Google, fonts are strictly a tool to enhance their core business of surveillance and advertising. And the only price Google cares about is *free*. No one at Google has ever sold a font license, or ever will. So the idea that there could be deeper common cause between Google and professional type designers is strained. Maybe like the common cause between dairy farmers and cows. Or scorpions and <span class="no-hyphens">frogs.</span>

<div class="gap" style="height:1em">

</div>

I know that some think this article is just a multiyear series of pessimistic put-downs. But truly—I would’ve been happy to see variable fonts succeed. As I said in 2016, “I’m sure variable fonts would be entertaining to work with.” *If* customers would pay for them. *If* these fonts could be made with reasonable time and effort. And maybe there are niches of the type market where these two conditions will turn out to be <span class="no-hyphens">true.</span>

Parametric type design is arguably the grail—or maybe white whale—of the digital-type era. I would’ve been delighted to discover that the (very wealthy corporate) stakeholders in variable fonts had, after 40+ years of attempts by others, sorted out these issues. By and large, I don’t think they have. In 1977, Donald Knuth’s [METAFONT system](http://metafont.tutorial.free.fr/downloads/mftut.pdf) showed off the typographic promise of parameteric type. Today, it seems the potential of this grand idea is being flattened into a way of increasing Google’s profits. What an <span class="no-hyphens">accomplishment.</span>

<div class="gap" style="height:1.5em">

</div>

<div id="december-2020-update" class="subhead">

[December 2020 update](#december-2020-update)

</div>

**Microsoft**: No new variable fonts. No support in Office apps for variable fonts. The discussion area Microsoft opened in 2017 for variable-font developers [has been essentially dead for two <span class="no-hyphens">years.</span>](https://github.com/microsoft/OpenTypeDesignVariationAxisTags)

**Apple**: No new variable fonts. Still no support in iWork apps for variable <span class="no-hyphens">fonts.</span>

**Adobe**: Released several “concept” variable fonts, including Acumin, Minion, and—oops, my mistake. [That all happened in 2017.](https://blog.typekit.com/2017/10/19/new-variable-fonts-from-adobe-originals/) None of those fonts ever moved past the concept designation, so as of 2020, Adobe’s catalog of finished variable fonts still stands at a perfect zero. No new app <span class="no-hyphens">support.</span>

**Google**: The only member of the original variable-fonts consortium that has released a big batch of variable fonts [at a steady pace.](https://fonts.google.com/?vfonly=true) Though this isn’t surprising—from the beginning, variable fonts have been primarily a Google-germinated and Google-dominated <span class="no-hyphens">project.</span>

Don’t take my word for <span class="no-hyphens">it:</span>

1.  This year we got a [first-hand account](https://docs.google.com/document/d/1MVNNjtoejIqvJrVruFo20qfW36ydLEebj0dRN7-bZrA/edit#) of the origin of variable fonts from former Google engineer Behdad Esfahbod, who takes credit for “secretly” inventing variable <span class="no-hyphens">fonts:</span>

    No sign that anyone at Google investigated *why* these previous efforts failed before starting to reanimate the moldering <span class="no-hyphens">skeletons.</span>

    “I studied Apple’s & Adobe’s separate failed attempts at \[adjustable-font technology\] from the 90s, picked the better one, and started work on expanding it to OpenType ... While \[my team of Google engineers\] worked on our implementation, Microsoft formed a working group of them, us, Apple, and Adobe, or the Big Four as the group became to be known in the font industry. The group started officially but secretly working on adding runtime font interpolation to OpenType. My whitepaper formed the blueprint of the work. The group met face-to-face each month, and six months later, on September 14, 2016 at the ATypI conference in Warsaw, the four of us companies announced OpenType Font Variations as part of OpenType <span class="no-hyphens">1.8.”</span>

2.  Recently, Bruno Maag, whose company has done [font-design work](https://www.daltonmaag.com/work/google-scope-one) for Google and thus has better information than me, [said that](https://twitter.com/bruno_maag/status/1329111382575419393) “other than Google nobody wanted \[variable fonts\] in the first place. The sole reason it was pushed for so hard is for reducing web load when having multiple styles of a font family in a <span class="no-hyphens">website.”</span>

Still, all that would be irrelevant origin-story detail if type users had embraced buying & using variable fonts. Have they? I can’t really prove a negative. But evidence of this embrace is <span class="no-hyphens">scant:</span>

1.  Monotype, owner of the world’s biggest type library, maintains a [page of marketing material](https://www.monotype.com/resources/variable-fonts) about variable fonts that tellingly includes no customer uses, aside from “the world’s first variable font <span class="no-hyphens">logo”.</span>

2.  Similarly, Adobe Max is Adobe’s annual marketing event. If variable fonts were a big deal to Adobe or its customers, we’d expect to see at least a few sessions about that, right? But no—[there was only one.](https://www.adobe.com/max/2020/sessions/acrobatic-sentient-shapeshifting-typography-with-v-s6908.html) and it wasn’t even given by an Adobe <span class="no-hyphens">designer.</span>

<div class="gap" style="height:1.5em">

</div>

This is my fifth time writing about variable fonts. I won’t say it’ll be my last. But it’s gotten boring. Nothing is <span class="no-hyphens">happening.</span>

We’re more than four years into the variable-fonts era. The honeymoon is definitely over. If you still think that widespread acceptance of variable fonts is just around the corner, the burden of proof is now upon you. Otherwise, I agree with [Brijan Powell](https://twitter.com/brijanp/status/1328737676992757762) that variable fonts are turning out to be “the [vocoder](https://www.youtube.com/watch?v=0kEHP2aUItA) of graphic <span class="no-hyphens">design.”</span>

In the details, not all my predictions from 2016 were accurate. But in the large, they were. Including my main thesis: that big tech companies would induce independent type designers to make variable fonts look good—mostly for free—while type customers would ignore them. And that Google would be the major <span class="no-hyphens">beneficiary.</span>

If Google had been truly serious about variable fonts, they could’ve removed all non-variable fonts from their library, forcing users to switch. But that’s never going to happen, because Google collects [valuable user information](https://brycewray.com/posts/2020/08/google-fonts-privacy/) from serving webfonts. So valuable that it [remains unresolved](https://github.com/google/fonts/issues/1495) whether Google Fonts complies with the GDPR. (Update, Jan 2022: a German court has ruled that Google Fonts [violates the GDPR.](https://twitter.com/FascinatingTech/status/1487342734906171393))

Still, it’s [only been a year or so](https://twitter.com/googlefonts/status/1185048007781355521) since Google added variable fonts to its library. During that time, Google’s own font-development efforts seem to have [slowed considerably.](https://groups.google.com/forum/#!forum/googlefonts-discuss) So Google’s commitment to variable fonts remains an open <span class="no-hyphens">question.</span>

When we consider that Google has a record of vigorously [murdering its underperforming projects,](https://killedbygoogle.com/) the likely endgame comes into view. As the financial evidence piles up, Google will be forced to conclude that variable fonts don’t actually save money—because Google hasn’t aggressively migrated its users, and from every account I’ve heard, variable fonts are painfully difficult and expensive to make. At that point, Google will abandon variable fonts altogether. After that, Microsoft, Apple, and Adobe will breathe a sigh of relief and officially deprecate variable fonts across their platforms. But [the web demos](https://v-fonts.com/) will live on. In 2045, a software engineer will come across these demos, and it will be time to learn these lessons all over <span class="no-hyphens">again.</span>

<div class="gap" style="height:1.5em">

</div>

<div id="december-2021-update" class="subhead">

[December 2021 update](#december-2021-update)

</div>

It’s that time of the year again! Like [Punxsutawney Phil,](https://www.groundhog.org/) I gingerly stick my head out of my sad little hole of retrograde typography and see what’s happened in the whizzy world of variable fonts over the past year. To mix things up, and hopefully prevent me from falling asleep at the keyboard, let’s try a new approach and take a look at the [variable-fonts support chart](https://v-fonts.com/support) on <span class="no-hyphens">v-fonts.com.</span>

This past year, Microsoft introduced a bug in Mac OS Word that prevents it from [displaying bold italics,](https://techcommunity.microsoft.com/t5/office-for-mac/bold-italics-not-working-on-word/m-p/2625182) which it had been able to do for the 30 years previous. I know, I know. Microsoft’s sick of our mean <span class="no-hyphens">jokes.</span>

**Operating systems**: All major operating systems support variable fonts. Well, except Windows. Which only supports [“named instances of a variable font”](https://docs.microsoft.com/en-us/windows/win32/directwrite/opentype-variable-fonts#using-opentype-variable-fonts) (“named instances” are fixed points in the variable-font design space that have been pre-selected by the designer). In other words, after five years, Windows still fails to support the signature feature of variable fonts, which is user-controllable design axes. Perhaps it won’t surprise anyone to hear that Microsoft’s main evangelist for variable fonts has been trying to [shift the conversation](https://typedrawers.com/discussion/4252/why-dont-we-hear-about-more-use-of-variable-fonts-on-the-web) toward the web, and away from Windows. I see what you did <span class="no-hyphens">there!</span>

**Web browsers**: All major web browsers support variable fonts. Terrific. I don’t think the no-money-in-web-publishing problem has been fixed. But never mind that, I <span class="no-hyphens">guess.</span>

**Design & graphics apps**: Pretty good support, with the notable exceptions of UI prototyping tools Adobe XD and Figma, which are used widely in workgroups for specifying typography, so [one theory is that](https://typedrawers.com/discussion/comment/55571/#Comment_55571) their lack of variable-font support tends to inhibit variable-font adoption more <span class="no-hyphens">widely.</span>

**Video & motion apps**: Even though [animation](https://speckyboy.com/variable-font-examples/) has been touted as an ideal niche for variable fonts, none of the Adobe or Apple motion-graphics apps support variable fonts. So much for that <span class="no-hyphens">idea.</span>

**Office apps**: None of the Apple or Microsoft office apps support variable fonts. That’s not surprising—users of office apps are still routinely stymied by tabular figures and <a href="small-caps.html" class="xref">small caps</a>. Variable fonts—surely you <span class="no-hyphens">jest.</span>

In sum: here in 2021, the only set of apps that offer reasonably complete & consistent support for variable fonts are web browsers. No surprise, since that’s been true [since 2017.](#industry-update-october-2017) For all other apps, support is uneven (design apps) or basically nonexistent (motion-graphics and office <span class="no-hyphens">apps).</span>

Thus, for variable fonts, it’s web or bust. But economically speaking, can variable fonts survive purely as a webfont <span class="no-hyphens">format?</span>

Consider that a key advantage of variable webfonts has always been [ostensible performance improvements](https://typographica.org/on-typography/variable-fonts/) due to reduced file size. But as I [said in 2016](#the-file-size-myth)—and others [have said since](https://blog.logrocket.com/variable-fonts-is-the-performance-trade-off-worth-it/)—it’s far from obvious that file size is still the critical factor in web performance. Or that variable fonts offer any file-size benefit at all in typical situations where only two or three weights are <span class="no-hyphens">used.</span>

Spoiler: they don’t. To be fair, no one is claiming so. And yet. This specious file-size argument remains tenacious, largely because it was part of the [origin myth of variable fonts.](https://www.wired.com/2016/09/apple-google-adobe-microsoft-join-forces-make-typographic-history/) Five years on, no one wants to pop that bubble, apparently out of <span class="no-hyphens">pity.</span>

Earlier in the variable-font era, a type-designer friend was considering whether to offer variable fonts. He told me he ran a script to gather data on how many customers of his webfonts used multiple styles of a family within a web page. Almost all of them used only one or two. For those customers, variable fonts would have no benefit. But one customer used 20 styles—surely this typomaniac would pay for a variable font! He inspected the logs more closely to discover the identity of this outlier. Answer: his own foundry <span class="no-hyphens">website.</span>

A certain contingent of responsive-web devotées would likely say that I’m (still) missing the point. Once you have a variable webfont, [the thinking goes,](https://noti.st/mandy/2W12mw/slides) you can accomplish fancy typographic tricks that would’ve been impractical with old-fashioned fonts. For instance: headlines that adapt smoothly to the width of a browser window. This argument isn’t wrong, exactly. But it amounts to a large-scale shifting of goalposts: OK, variable fonts aren’t viable for mainstream web design as we know it, but if we just create a new global web-design cult based *around* variable fonts, everyone will profit. This is the argument once made famous by the [Underpants <span class="no-hyphens">Gnomes.</span>](https://southpark.fandom.com/wiki/Underpants_Gnomes)

Friends, how many more years are we going to do this? We haven’t spoken of it so far, but it’s time to start: there’s an opportunity cost to pursuing variable fonts. Meaning—all the energy and attention that gets bulldozed into this effort is energy that can’t be invested in solving other typographic problems that customers might—*gasp*—actually pay <span class="no-hyphens">for.</span>

In one sense, this doesn’t affect me, because I choose not to make variable fonts. But in another sense, it does, because I’d like to see font technology move forward in ways that make our work more valuable to more customers. Wouldn’t <span class="no-hyphens">you?</span>

By that measure, where are we? Over the last five years, the font industry has collectively placed a very expensive bet on variable fonts. In so doing, we have thereby excluded other options. (Lordy, even [color fonts](https://www.colorfonts.wtf/) that weren’t a shitshow would’ve been more of an opportunity.) If variable fonts disappear, a consequence is that we will have done nothing to arrest the natural obsolescence of our work that was happening in the meantime. Technology marched on; we stood <span class="no-hyphens">still.</span>

Worse, by betting on variable fonts at all, the independent type-design industry has necessarily become even more reliant on a small group of Big Tech gatekeepers to determine how and where customers can use our fonts. (We could’ve, for instance, been developing more [typesetting tools](https://docs.racket-lang.org/quad/) that circumvent these gatekeepers.) Once we forfeit our autonomy, we don’t get it <span class="no-hyphens">back.</span>

How many times do we need to learn that lesson? What’s happening with variable fonts in 2021 feels similar to what happened after 2010 as Monotype consolidated the major retail channels for fonts. Designers who had been selling outside those channels were largely unaffected. But those who relied on those channels felt the pinch, as prices and royalty rates faced downward pressure. In that case, however, the retail-font market was still financially strong. The gatekeepers were still pumping money into the independent type industry (though less as time <span class="no-hyphens">passed).</span>

With variable fonts, there has never, ever been an economic benefit for independent type designers. The variable-font gatekeepers just keep expecting more hope. More patience. More optimism. More demos. More work. All for <span class="no-hyphens">free.</span>

By any reasonable objective measure—platform & app support, customer interest, profit—variable fonts have been a failure. Truly, I would’ve been glad to discover evidence otherwise. Sure, there have been a few [success stories.](https://typedrawers.com/discussion/comment/55586/#Comment_55586) But variable fonts can’t survive as a niche of a corner of the type <span class="no-hyphens">market.</span>

“Reality is that which, when you stop believing in it, doesn’t go away”  
—Philip K. <span class="no-hyphens">Dick</span>

At times, some have been annoyed that I keep pointing out these flaws. But why? First and foremost, no one cares what I think. Second, I could be persuaded that there’s a trajectory for variable fonts where they become useful and profitable. It wouldn’t be the first pivot in tech history, certainly. But that would require a deliberate adjustment, which starts with an honest appraisal of reality. Advocates of variable fonts who’d prefer to [skip over](https://typedrawers.com/discussion/comment/55632/#Comment_55632) the inconvenient facts of the last five years are just prolonging the <span class="no-hyphens">pain.</span>

If anything, I worry that expectations for variable fonts have been set so low for so long—*just wait, things will be better next year!*—that objective measures no longer mean anything. Like a meme stock or cryptocurrency, perhaps variable fonts are now valued by their abstract potential, not by any real-world consideration. If that’s the case, then I take it back: there’s no way for variable fonts to fail, because the very idea of failure has been <span class="no-hyphens">vaporized.</span>

<div class="gap" style="height:1em">

</div>

Speaking of variable-font gatekeepers—[in last year’s report](#december-2020-update) I observed that Google had been the most vigorous adopter and developer of variable fonts, but that we ought to stay alert for signs of flagging enthusiasm. In November 2021, the Google Fonts project manager [conceded](https://typedrawers.com/discussion/comment/55568/#Comment_55568) that after many busy years, “Google Fonts isn’t actively commissioning fonts.” Also, though Google-sponsored work on variable fonts had been prominently featured at five consecutive [ATypI](https://atypi.org/) events—[2016,](https://www.youtube.com/watch?v=6kizDePhcFU) [2017,](https://www.youtube.com/watch?v=Vukv7nH-10s&list=PL0oMAzSh5W9oJSx9BsXeF8UzA44FwB255&index=16) [2018,](https://www.youtube.com/watch?v=Ec65S6stpiM&list=PL0oMAzSh5W9q64iHo9pMa0WdgUdz411hD&index=41) [2019,](https://www.youtube.com/watch?v=CY1ztyGF9fs&list=PL0oMAzSh5W9qekqvcVFsSYaoO7U_5K6rR&index=18) and [2020](https://www.youtube.com/watch?v=6OKE6p9E0eY)—Google is conspicuously absent from the upcoming [2021 event.](https://events.bizzabo.com/356258/agenda) Oh well—probably [nothing to worry <span class="no-hyphens">about.</span>](https://killedbygoogle.com/)

<div class="gap" style="height:1.5em">

</div>

<div id="december-2022-update" class="subhead">

[December 2022 update](#december-2022-update)

</div>

Variable fonts are dead. Cause of death: financial malnutrition caused by complete lack of interest from the professional design community and the handful of other enthusiasts who pay for <span class="no-hyphens">fonts.</span>

Some true believers will disagree. They are in denial. Which, to be fair, is the [first step](https://www.cruse.org.uk/understanding-grief/effects-of-grief/five-stages-of-grief/) along the path to <span class="no-hyphens">acceptance.</span>

Some people paid by Google and Microsoft will continue to insist otherwise. They know better. But until someone higher up remembers that they exist and then cuts off their budget, they will <span class="no-hyphens">persist.</span>

Though it won’t change the minds of these denialists, let’s survey the evidence <span class="no-hyphens">anyhow:</span>

1.  Since last year, [OS and app support](https://v-fonts.com/support) for variable fonts has stagnated. The only new app to support variable fonts was [Figma](https://www.figma.com/typography/variable-fonts/) in May 2022. Though by September, Figma had been [acquired by Adobe.](https://news.adobe.com/news/news-details/2022/Adobe-to-Acquire-Figma/default.aspx) If you’re new here, that’s a fate [equivalent to <span class="no-hyphens">death.</span>](https://www.theverge.com/2022/9/21/23363188/adobe-destroy-figma-designers-ux-ui-creative-cloud)

2.  On [v-fonts.com,](https://v-fonts.com/) the indie showcase for new and nifty variable fonts, only two fonts were added in the year 2022—back in April. Since <span class="no-hyphens">then—nothing.</span>

3.  At its developer conference in June 2022, [Apple announced](https://developer.apple.com/videos/play/wwdc2022/110381/) [variable versions](https://developer.apple.com/design/human-interface-guidelines/foundations/typography/) of its core Mac OS fonts San Francisco and New York. Though the fonts also seem to [contain variable axes](https://v-fonts.com/publishers/apple) for weight and width, only the axis for [optical size](https://developer.apple.com/design/human-interface-guidelines/foundations/typography/) is <span class="no-hyphens">documented.</span>

4.  One purported benefit of variable fonts was giving users more typographic choices. I have [predicted since 2016](#font-interpolation-back-to-the-future)—as someone with thousands of paying font customers—that this was never going to fly. Why? Because fonts are already complicated enough. Customers aren’t looking for new headaches. Nevertheless, Google—a company with zero paying font customers—[pushed this](https://variablefonts.io/about-variable-fonts/) narrative for years. It was only in December 2021 that Google’s variable-font promoter [finally conceded](https://typedrawers.com/discussion/comment/55797/#Comment_55797) that “the vast majority of users aren’t able to achieve those artful effective uses”. No <span class="no-hyphens">kidding.</span>

5.  Even [this tool](https://variablefonts.typenetwork.com/examples/families/file-size-benefits) intended to prove the file-size advantage of variable fonts—using Google’s Roboto as an example—does the opposite, showing that a standard four-style family is only half the size of the corresponding variable <span class="no-hyphens">fonts.</span>

    The most pernicious myth of variable fonts—[repeated relentlessly](https://fonts.google.com/knowledge/introducing_type/introducing_variable_fonts) by Google since the [initial rollout](https://12ft.io/proxy?&q=https%3A%2F%2Fwww.wired.com%2F2016%2F09%2Fapple-google-adobe-microsoft-join-forces-make-typographic-history)—was that variable fonts would produce meaningful file-size savings for web users. That seemed unlikely even [back in 2016.](#the-file-size-myth) Others have [debunked it since then.](https://blog.logrocket.com/variable-fonts-is-the-performance-trade-off-worth-it/) Tellingly, Google never has put forth any evidence in support. Indeed, in a rare moment of candor, Google [has admitted](https://typedrawers.com/discussion/comment/55782/#Comment_55782) it’s not true. So let’s call it what it is and always was: Big Tech <span class="no-hyphens">bullshit.</span>

<div class="gap" style="height:1.5em">

</div>

With that, we have traveled full circle. In 2016, the impetus for this piece was to point out that the differences in incentives between Big Tech and indie type designers made variable fonts at best an uneasy alliance; at worst, a redistribution of resources upward. By that I meant that indie designers would be asked to put time & money into making variable-font technology look good, while Big Tech—mostly Google, it turned out—would reap the <span class="no-hyphens">benefits.</span>

Six years on, that thesis has been proved repeatedly. The only good news, perhaps, is that judging by the rate of variable-font releases, type designers seem to have [lost interest,](https://v-fonts.com/) and are no longer putting energy into this black <span class="no-hyphens">hole.</span>

Still, as recently as September 2022, Microsoft’s variable-fonts evangelist [was lamenting](https://typedrawers.com/discussion/comment/59502/#Comment_59502) to type designers about the “challenge of explaining the benefits to customers and a big need to educate graphic designers generally.” Hoping, I guess, that someone would volunteer for this long-overdue homework assignment? That one more frog would give one more ride to one more <span class="no-hyphens">scorpion?</span>

There’s one born every minute, I <span class="no-hyphens">suppose.</span>

As for me—I rest my <span class="no-hyphens">case.</span>

—Matthew <span class="no-hyphens">Butterick</span>

<div class="gap" style="height:1.5em">

</div>

<div class="btw">

<div class="btw-title">

by the way

</div>

- I’m necessarily glossing over a lot of details in 30 years of font-format history. I welcome clarifications and corrections if you feel I short-shrifted something <span class="no-hyphens">vital.</span>

- I’ve ended up making more predictions than I expected. If they don’t come true, I promise to note where I was wrong. I might be updating this piece for 20 years, <span class="no-hyphens">however.</span>

- Wired published a [breathless introduction](https://www.wired.com/2016/09/apple-google-adobe-microsoft-join-forces-make-typographic-history/) to variable fonts. Time between [the announcement](https://medium.com/@tiro/https-medium-com-tiro-introducing-opentype-variable-fonts-12ba6cd2369#.6zdexe50k) of this unreleased technology and the first claim that it has “virtually infinite” possibilities: eight <span class="no-hyphens">days.</span>

- *Practical Typography* uses a variable-font-like trick to serve different grades of the <a href="body-text.html" class="xref">body text</a> font to different platforms. For instance, Windows users get a slightly heavier version than Mac users, to account for lighter screen rasterization. All this can be done easily with today’s technology. But I seem to be the only person on the internet who was sufficiently motivated to <span class="no-hyphens">try.</span>

</div>

</div>

<span id="links"></span>

<div class="gap" style="height:1em">

</div>

</div>

<a href="to-pay-or-not-to-pay.html" class="nav"></a>

<div id="prev" class="side">

</div>

<a href="are-two-spaces-better-than-one.html" class="nav"></a>

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
