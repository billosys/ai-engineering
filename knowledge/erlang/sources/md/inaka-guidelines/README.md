Erlang Coding Standards & Guidelines
====================================

Suggested reading material: http://www.erlang.se/doc/programming_rules.shtml

***

Table of Contents:
* [Contact Us](#contact-us)
* [Conventions & Rules](#conventions--rules)
  * [Source Code Layout](#source-code-layout)
    * [Maintain existing style](#maintain-existing-style)
    * [Spaces over tabs](#spaces-over-tabs)
    * [Use your spacebar](#use-your-spacebar)
    * [No Trailing Whitespace](#no-trailing-whitespace)
    * [100 column per line](#100-column-per-line)
    * [More, smaller functions over case expressions](#more-smaller-functions-over-case-expressions)
    * [Group functions logically](#group-functions-logically)
    * [Get your types together](#get-your-types-together)
    * [No God modules](#no-god-modules)
    * [Simple unit tests](#simple-unit-tests)
    * [Honor DRY](#honor-dry)
    * [Group modules in subdirectories by functionality](#group-modules-in-subdirectories-by-functionality)
    * [Header files](#header-files)
  * [Syntax](#syntax)
    * [Don't write spaghetti code](#dont-write-spaghetti-code)
    * [Avoid dynamic calls](#avoid-dynamic-calls)
    * [Avoid deep nesting](#avoid-deep-nesting)
    * [Avoid if expressions](#avoid-if-expressions)
    * [Avoid nested try...catches](#avoid-nested-try-catches)
    * [Avoid non-local returns](#avoid-non-local-returns)
  * [Naming](#naming)
    * [Be consistent when naming](#be-consistent-when-naming-concepts)
    * [Explicit state should be explicitly named](#explicit-state-should-be-explicitly-named)
    * [Don't use _Ignored variables](#dont-use-_ignored-variables)
    * [Avoid boolean parameters](#avoid-boolean-parameters)
    * [Stick to one convention for naming modules](#stick-to-one-convention-for-naming-modules)
    * [Lowercase atoms](#lowercase-atoms)
    * [Function Names](#function-names)
    * [Variable Names](#variable-names)
  * [Strings](#strings)
    * [IOLists over string concatenation](#iolists-over-string-concatenation)
  * [Macros](#macros)
    * [No Macros](#no-macros)
    * [Uppercase Macros](#uppercase-macros)
    * [No module or function name macros](#no-module-or-function-name-macros)
  * [Records](#records)
    * [Record names](#record-names)
    * [Records go first](#records-go-first)
    * [Don't share your records](#dont-share-your-records)
    * [Avoid records in specs](#avoid-records-in-specs)
    * [Types in records](#types-in-records)
  * [Misc](#misc)
    * [Write function specs](#write-function-specs)
    * [Use -callback attributes over behaviour_info/1](use--callback-attributes-over-behaviour_info1)
    * [Use atoms or tagged tuples for messages](#use-atoms-or-tagged-tuples-for-messages)
    * [No nested header inclusion](#no-nested-header-inclusion)
    * [No types in include files](#no-types-in-include-files)
    * [Don't import](#dont-import)
    * [Don't export_all](#dont-export_all)
    * [Encapsulate OTP server APIs](#encapsulate-otp-server-apis)
    * [No debug calls](#no-debug-calls)
    * [Don't use case catch](#dont-use-case-catch)
  * [Tools](#tools)
    * [Lock your dependencies](#lock-your-dependencies)
    * [Loud errors](#loud-errors)
    * [Properly use logging levels](#properly-use-logging-levels)
    * [Prefer the https protocol when specifying dependency locations](#prefer-the-https-protocol-over-others-when-specifying-dependency-urls)
    * [No implicit functions with mixer](#no-implicit-functions-with-mixer)
* [Suggestions & Great Ideas](#suggestions--great-ideas)
  * [Prefer pattern-matching over testing for equality](#prefer-pattern-matching-over-testing-for-equality)
  * [Favor higher-order functions over manual use of recursion](#favor-higher-order-functions-over-manual-use-of-recursion)
  * [CamelCase over Under_Score](#camelcase-over-under_score)
  * [Prefer shorter (but still meaningful) variable names](#prefer-shorter-but-still-meaningful-variable-names)
  * [Comment levels](#comment-levels)
  * [Keep functions small](#keep-functions-small)
  * [Use behaviours](#use-behaviours)
  * [When programming defensively, do so on client side](#when-programming-defensively-do-so-on-client-side)
  * [Avoid unnecessary calls to length/1](#avoid-unnecessary-calls-to-length1)
  * [Move stuff to independent applications](#move-stuff-to-independent-applications)
  * [Use the facade pattern on libraries](#use-the-facade-pattern-on-libraries)
  * [Types in exported functions](#types-in-exported-functions)
  * [Separate responsibilities in sumo_db](#separate-responsibilities-in-sumo_db)

## Contact Us

If you find any **bugs** or have a **problem** while using this library, please [open an issue](https://github.com/inaka/erlang_guidelines/issues/new) in this repo (or a pull request :)).

And you can check all of our open-source projects at [inaka.github.io](http://inaka.github.io)

## Conventions & Rules

These are _"Things that may be used as reason to reject a Pull Request"_.

### Source Code Layout

***
##### Maintain existing style
> When editing a module written by someone else, stick to the style in which it was written. If a project has an overall style, stick to that when writing new modules as well.

*Examples*: 

```erlang
-module(existing_style).

-export([bad/0, good/0]).

bad() ->
  % existing code
  List = [ {elem1, 1}
         , {elem2, 2}
  % new code (not respecting the format)
         , {elem3, 3}, {elem4, 4},
           {elem5, 5}
         ],
  other_module:call(List).

good() ->
  % existing code
  List = [ {elem1, 1}
         , {elem2, 2}
  % new code (respecting the format)
         , {elem3, 3}
         , {elem4, 4}
         , {elem5, 5}
         ],
  other_module:call(List).
```


*Reasoning*: It's better to keep a module that just looks ugly to you than to have a module that looks half ugly to you, half ugly to somebody else.

***
##### Spaces over tabs
> Spaces over tabs, 2 space indentation.

*Examples*: 

```erlang
-module(indent).

-export([bad/0, better/0, good/0]).

%% @doc inconsistent 
bad() ->
  try
    ThisBlock = is:indented(with, two, spaces),
    that:is_good(ThisBlock)
  catch
      _:_ ->
          this_block:is_indented(with, four, spaces)
  end.

%% @doc consistent, but with 4 spaces
better() ->
    receive
        {this, block} -> is:indented(with, four, spaces);
        _That -> is:not_good()
    after 100 ->
        but:at_least(it, is, consistent)
    end.

%% @doc good
good() ->
  case indentation:block() of
    {2, spaces} -> me:gusta();
    {_, _} -> not_sure:if_gusta()
  end.
```


*Reasoning*: This is *not* intended to allow deep nesting levels in the code. 2 spaces are enough if the code is clean enough, and the code looks more concise, allowing more characters in the same line.

***
##### Use your spacebar
> Surround operators and commas with spaces.

*Examples*: 

```erlang
-module(spaces).

-export([bad/3, good/3]).

% @doc no spaces
bad(_My,_Space,_Bar)->[is,'not',working].

% @doc spaces!!
good(_Hey, _Now, _It) -> ["works " ++ "again, " | [hooray]].
```


*Reasoning*: It produces cleaner code that's easier to find / read / etc.

***
##### No Trailing Whitespace
> Remove trailing whitespaces from your lines

*Examples*: 

```erlang
-module(trailing_whitespace).

-export([bad/0, good/0]).

bad() -> "this line has trailing whitespace".       

good() -> "this line has not".
```


*Reasoning*: It's commit noise. As a reference, check out [this long argument](https://programmers.stackexchange.com/questions/121555/why-is-trailing-whitespace-a-big-deal).

***
##### 100 column per line
> Stick to 100 chars per line, maximum.

*Examples*: 

```erlang
-module(col_width).

-record(rec, {field1 :: any(), field2 :: any(), field3 :: any()}).

-export([bad/2, good/2]).

%$ @doc too wide
bad([#rec{field1 = FF1, field2 = FF2, field3 = FF3}, #rec{field1 = BF1, field2 = BF2, field3 = BF3} | Rest], Arg2) ->
  other_module:bad(FF1, FF2, FF3, BF1, BF2, BF3, bad(Rest, Arg2)).

%% @doc good (< 100 chars)
good([Foo, Bar | Rest], Arg2) ->
  #rec{field1 = FF1, field2 = FF2, field3 = FF3} = Foo,
  #rec{field1 = BF1, field2 = BF2, field3 = BF3} = Bar,
  other_module:good(FF1, FF2, FF3, BF1, BF2, BF3, good(Rest, Arg2)).
```


*Reasoning*: Excessively long lines are a pain to deal with: you either have to scroll horizontally while editing, or live with ugly line wrapping at arbitrary points.
The 100 character limit also keeps lines short enough that you can comfortably work with two source files side by side on a typical laptop screen, or three on a 1080p display.

***

##### More, smaller functions over case expressions
> Use pattern-maching in clause functions rather than case's. Specially important if the case is:
> - the top-level expression of the function
> - huge

*Examples*: 

```erlang
-module(smaller_functions).

-export([bad/0, bad/1, good/0, good/1]).

%% @doc function with just a case
bad(Arg) ->
  case Arg of
    this_one -> should:be(a, function, clause);
    and_this_one -> should:be(another, function, clause)
  end.

%% @doc usage of pattern matching
good(this_one) -> is:a(function, clause);
good(and_this_one) -> is:another(function, clause).


%% @doc function with an internal case
bad() ->
  InitialArg = some:initial_arg(),
  InternalResult =
    case InitialArg of
      this_one -> should:be(a, function, clause);
      and_this_one -> should:be(another, function, clause)
    end,
  some:modification(InternalResult).

%% @doc usage of function clauses instead of an internal case
good() ->
  InitialArg = some:initial_arg(),
  InternalResult = good(InitialArg),
  some:modification(InternalResult).
```


*Reasoning:* it is usually the case that a case in a function body represents some sort of decision, and functions should be as simple as possible. If each branch of a decision's outcome is implemented as a function clause instead of as a case clause, the decision may be given a meaningful name. In other words, the case is acting as an 'anonymous function', which unless they are being used in the context of a higher-order function, merely obscure meaning.

***
##### Group functions logically
> Try to always separate **unexported** and **exported** functions in groups, with the exported ones first, unless it helps readability and code discovery.

*Examples*: 

`src/grouping_functions/bad.erl`:

```erlang
%%% @doc Mixing priv and public functions
-module(bad).

-export([public1/0, public2/0]).

public1() -> private3(atom1).

private1() -> atom2.

public2() -> private2(private1()).

private2(Atom) -> private3(Atom).

private3(Atom) -> Atom.
```

`src/grouping_functions/better.erl`:

```erlang
%%% @doc associated functions are closer
-module(better).

-export([public1/0, public2/0]).

public1() ->
  case application:get_env(atom_for_public_1) of
    {ok, X} -> public1(X);
    _ -> throw(cant_do)
  end.
%% @doc This is a private function but it's related just to the one before
public1(X) -> private3(X).

public2() -> private2(private1()).

private1() -> atom2.

private2(Atom) -> private3(Atom).

private3(Atom) -> Atom.
```

`src/grouping_functions/good.erl`:

```erlang
-module(good).

-export([public1/0, public2/0]).

public1() ->
  case application:get_env(atom_for_public_1) of
    {ok, X} -> private3(X);
    _ -> throw(cant_do)
  end.

public2() -> private2(private1()).

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% PRIVATE FUNCTIONS %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

private1() -> atom2.

private2(Atom) -> private3(Atom).

private3(Atom) -> Atom.
```


*Reasoning*: Well structured code is easier to read/understand/modify.

***
##### Get your types together
> Place all types at the beginning of the file

*Examples*: 

```erlang
-module(type_placement).

-export([good/0, bad/0]).

-type good_type() :: 1..3.

-spec good() -> good_type().
good() -> 2.


-type bad_type() :: 1..3.
-spec bad() -> bad_type().
bad() -> 2.
```


*Reasoning*: Types are used to define data structures that will most likely be used by multiple functions on the module, so their definition can not be tied to just one of them. Besides it's a good practice to place them in code in a similar way as the documentation presents them and edoc puts types at the beginning of each module documentation

***
##### No God modules
> Don't design your system using **god**  modules (modules that have a huge number of functions and/or deal with very unrelated things)

*Examples*: 

```erlang
%%% @doc all of your db operations belong to us!
-module(god).

-export([create_user/1, create_user/2, create_user/3]).
-export([update_user/2, update_user/3]).
-export([delete_user/1]).
-export([create_post/1, create_post/2, create_post/3]).
-export([update_post/2, update_post/3]).
-export([delete_post/1]).
-export([create_comment/2, create_comment/3]).
-export([update_comment/3, update_comment/4]).
-export([delete_comment/2]).

create_user(Name) -> create_user(Name, undefined).

create_user(Name, Email) -> create_user(Name, Email, undefined).

create_user(Name, Email, Phone) ->
  some_db:insert(users, [{name, Name}, {email, Email}, {phone, Phone}]).

update_user(Name, Changes) ->
  some_db:update(users, [{name, Name}], Changes).

update_user(Name, Key, Value) ->
  update_user(Name, [{Key, Value}]).

delete_user(Name) ->
  some_db:delete(users, [{name, Name}]).

create_post(Text) -> create_post(Text, undefined).

create_post(Text, Title) -> create_post(Text, Title, undefined).

create_post(Text, Title, Image) ->
  some_db:insert(posts, [{text, Text}, {title, Title}, {image, Image}]).

update_post(Text, Changes) ->
  some_db:update(posts, [{text, Text}], Changes).

update_post(Text, Key, Value) ->
  update_post(Text, [{Key, Value}]).

delete_post(Text) ->
  some_db:delete(posts, [{text, Text}]).

create_comment(PostId, Text) -> create_comment(PostId, Text, undefined).

create_comment(PostId, Text, Image) ->
  some_db:insert(comments, [{post_id, PostId}, {text, Text}, {image, Image}]).

update_comment(PostId, CommentId, Changes) ->
  some_db:update(comments, [{post_id, PostId}, {id, CommentId}], Changes).

update_comment(PostId, CommentId, Key, Value) ->
  update_comment(PostId, CommentId, [{Key, Value}]).

delete_comment(PostId, CommentId) ->
  some_db:delete(comments, [{post_id, PostId}, {id, CommentId}]).
```


*Reasoning*: God modules, like god objects, are modules that do too much or know too much. God modules usually come into existence by feature accretion. A beautiful, to-the-point module with one job, one responsibility done well, gains a function. Then another, which does the same thing but with different parameters. Then one day, you have a 6000-line module with 500 functions. Having modules (and functions) that do one and only one thing well makes it easy to explore and reason about code, and thus maintain it.

***
##### Simple unit tests
> Single responsibility applies to tests as well. When writing **unit** tests, keep them short and don't put more than 1 or 2 asserts per test

*Examples*: 

```erlang
-module(test_SUITE).

-export([bad/1, good1/1, good2/1, good3/1]).

bad(_Config) ->
  ct:comment("When input is 0, it should return 0"),
  0 = should:return(0),
  ct:comment("When input is positive, it should return 1"),
  1 = should:return(2),
  ct:comment("When input is negative, it should return -1"),
  -1 = should:return(-100),
  {comment, ""}.

good1(_Config) ->
  ct:comment("When input is 0, it should return 0"),
  0 = should:return(0),
  {comment, ""}.

good2(_Config) ->
  ct:comment("When input is positive, it should return 1"),
  1 = should:return(2),
  {comment, ""}.

good3(_Config) ->
  ct:comment("When input is negative, it should return -1"),
  -1 = should:return(-100),
  {comment, ""}.
```


*Reasoning*: Multiple tests can identify multiple errors in one run, if you put all the things you want to test into one test you'll have to fix one thing at a time until the test passes.

***
##### Honor DRY
> Don't write the same code in many places, use functions and variables for that

*Examples*: 

```erlang
%% @doc this is a very very trivial example, DRY has a much wider scope but it's
%%      provided just as an example
-module(dry).

-export([bad/0, good/0]).

bad() ->
  case something:from(other, place) of
    {show, _} ->
      display:nicely(something:from(other, place));
    nothing ->
      display:nothing()
  end.

good() ->
  case something:from(other, place) of
    {show, _} = ThingToShow ->
      display:nicely(ThingToShow);
    dont_show_me ->
      display:nothing()
  end.
```


*Reasoning*: This convention is specifically put in this list (instead of treat it as a [great idea](#great-ideas)) so that reviewers can reject PRs that include the same code several times or PRs that re-implement something that they know it's already done somewhere else.

***
##### Group modules in subdirectories by functionality
> When having lots of modules, use subdirectories for them, named with a nice descriptive name for what that "package" does.

*Reasoning*: That way it's easier to find what you need and determine what a certain module does.

*Note*: Remember to properly configure your ``Emakefile`` to handle that, if you use it.

***
##### Header files
> Header files:
> - SHOULD NOT include type definitions nor record definitions nor function definitions.
> - MAY include macros definitions, although macros should be [avoided](#no-macros).

*Examples*: 

```erlang
% Bad
-record(nasty_non_encapsulated_record, {
    dont_use_me_directly,
    me_neither
    }).

-type who_knows_what_this_is() :: binary().

cool_function_everyone_uses(Thingy) -> 
    Thingy.

% OK
-define(?COOKIE, <<""Cookie: ">>).
```


*Reasoning*:
Type definitions should be located in the modules where the data and its associated functions are defined. In type specs types may be module-prefixed which also makes it clear where the data type is defined, so there is no reason to need to share them via headers.

Including record definitions in header files promotes sharing internal details of those records across modules, increasing coupling and preventing encapsulation, in turn making it more difficult to change and maintain the code. Records should be defined in their own modules which should provide an opaque data type and functions to access and manipulate the record.

Function definitions should most definitely not be included in header files because it leads to code duplication.

### Syntax

Erlang syntax is horrible amirite? So you might as well make the best of it, right? _Right_?

***
##### Don't write spaghetti code
> Don't write spaghetti code (A list comprehension with a case inside, or blocks with begin/end, and nested stuff)

*Examples*: 

```erlang
-module(spaghetti).

-export([bad/0, good/0]).

bad() ->
  Client = active_user:get_current_client(),
  [binary_to_list(Org)
   || Org <- autocomplete_db:members(
              case Client of
                home_client ->
                  <<"our:organizations">>;
                aperture_science ->
                  <<"client:", (prefix_for(aperture_science))/binary, ":orgs">>;
                wayne_ents ->
                  <<"client:", (prefix_for(wayne_ents))/binary, ":orgs">>
              end)].

good() ->
  Client = active_user:get_current_client(),
  RawOrgs = autocomplete_db:members(client_ac_key(Client)),
  [binary_to_list(Org) || Org <- RawOrgs].

client_ac_key(home_client) -> <<"our:organizations">>;
client_ac_key(Client) ->
  Prefix = prefix_for(Client),
  <<"client:", Prefix/binary, ":orgs">>.

prefix_for(aperture_science) -> <<"as">>;
prefix_for(wayne_ents) -> <<"we">>.
```


*Reasoning*: Spaghetti code is harder to read, understand and edit. The function callgraph for your program should strive to be a directed acyclic graph.

***
##### Avoid dynamic calls
> If there is no specific need for it, don't use dynamic function calling.

*Examples*: 

```erlang
-module(dyn_calls).

-export([bad/1, good/1]).

bad(Arg) ->
  Mods = [module_1, module_2, module_3],
  Fun = my_function,
  lists:foreach(
    fun(Mod) ->
      Mod:Fun(Arg)
    end, Mods).

good(Arg) ->
  module_1:my_function(Arg),
  module_2:my_function(Arg),
  module_3:my_function(Arg).
```


*Reasoning*: Dynamic calls can't be checked by [``xref``](http://erlang.org/doc/apps/tools/xref_chapter.html), one of the most useful tools in the Erlang world. ``xref`` is a cross reference checking/observing tool.

***
##### Avoid deep nesting
> Try not to nest more than 3 levels deep.

*Examples*: 

```erlang
-module(nesting).

-export([bad/0, good/0]).

bad() ->
  case this:function() of
    has ->
      try too:much() of
        nested ->
          receive
            structures ->
              it:should_be(refactored);
            into ->
              several:other(functions)
          end
      catch
        _:_ ->
          dont:you("think?")
      end;
    _ ->
      i:do()
  end.

good() ->
  case this:function() of
    calls ->
      other:functions();
    that ->
      try do:the(internal, parts) of
        what ->
          was:done(in)
      catch
        _:the ->
          previous:example()
      end
  end.
```


*Reasoning*: Nested levels indicate deep logic in a function, too many decisions taken or things done in a single function. This hinders not only readability, but also maintainability (making changes) and debugging, and writing unit tests.
See also: [More, smaller functions over case expressions](#more-smaller-functions-over-case-expressions).

***
##### Avoid if expressions
> Don't use `if`.

*Examples*: 

```erlang
-module(no_if).

-export([bad/1, better/1, good/1]).

bad(Connection) ->
  {Transport, Version} = other_place:get_http_params(),
  if
    Transport =/= cowboy_spdy, Version =:= 'HTTP/1.1' ->
      [{<<"connection">>, utils:atom_to_connection(Connection)}];
    true ->
      []
  end.


better(Connection) ->
  {Transport, Version} = other_place:get_http_params(),
  case {Transport, Version} of
    {cowboy_spdy, 'HTTP/1.1'} ->
      [{<<"connection">>, utils:atom_to_connection(Connection)}];
    {_, _} ->
      []
  end.
 

good(Connection) ->
  {Transport, Version} = other_place:get_http_params(),
  connection_headers(Transport, Version, Connection).
  
connection_headers(cowboy_spdy, 'HTTP/1.1', Connection) ->
    [{<<"connection">>, utils:atom_to_connection(Connection)}];
connection_headers(_, _, _) ->
    [].
```


*Reasoning*: In some circumstances `if` introduces static boolean logic in your code, reducing code flexibility. In other cases, a `case` or a function call with pattern matching in its clauses is just more declarative. For newcommers (that have learned to use `if` in other languages), Erlang's `if` can be either hard to understand or easily abused.

*Debate*:
- [The Erlang Rationale - The problem with 'if'](http://rvirding.blogspot.com/2008/11/erlang-rationale-problem-with-if.html)
- [In this repo](erlang_guidelines/issues/14)
- [In erlang-questions](http://erlang.org/pipermail/erlang-questions/2014-September/080827.html)

***
##### Avoid nested try...catches
> Don't nest `try…catch` clauses

*Examples*: 

```erlang
-module(nested_try_catch).

-export([bad/0, good1/0, good2/0]).

bad() ->
  try
    maybe:throw(exception1),
    try
      maybe:throw(exception2),
      "We are safe!"
    catch
      _:exception2 ->
        "Oh, no! Exception #2"
    end
  catch
    _:exception1 -> "Bummer! Exception #1"
  end.

good1() ->
  try
    maybe:throw(exception1),
    maybe:throw(exception2),
    "We are safe!"
  catch
    _:exception1 ->
      "Bummer! Exception #1";
    _:exception2 ->
      "Oh, no! Exception #2"
  end.

good2() ->
  try
    maybe:throw(exception1),
    a_function:that_deals(with, exception2),
    "We are safe!"
  catch
    _:exception1 ->
      "Bummer! Exception #1"
  end.
```


*Reasoning*: Nesting `try…catch` blocks defeats the whole purpose of them, which is to isolate the code that deals with error scenarios from the nice and shiny code that deals with the expected execution path.

***
##### Avoid non-local returns
> Don't use `throw` and `catch`

*Examples*: 

```erlang
-module(catch_and_throw).

-export([bad/2, good/2]).

%% We use catch and throw to find the first element that matches a predicate on a list
bad(Pred, List) ->
    catch lists:foreach(
        fun(Elem) ->
            case Pred(Elem) of
                true -> throw(Elem);
                _ -> noop
            end
        end, List).

%% We use recursion to find the first element that matches a predicate on a list
good(_Pred, []) -> false;
good(Pred, [Elem|Elems]) ->
    case Pred(Elem) of
        true -> Elem;
        _ -> good(Pred, Elems)
    end.
```


*Reasoning*:
On one hand, `throw` is not meant to be used to _throw exceptions_, so it shouldn't be used for that.
On the other hand, `throw` is meant to be used for non-local returns. While they might seem to be useful in terms of performance, they tend to produce more complex code that is harder to understand or reason about. Particularly if the result being thrown in one place is caught in another very distant part of the application. You can find more in [this conversation at the Erlang Forums](https://erlangforums.com/t/should-we-eventually-improve-catch-throw-semantics/1210/6):

> IMO, it is a really bad style, especially in the context of a functional language. It is returning something through side effects. That may have its uses to [quickly break out of deep recursion](https://learnyousomeerlang.com/errors-and-exceptions#try-a-try-in-a-tree), but they are rare. I think I never used throw even once. In any case, I think it should not be made “socially acceptable” to return stuff via throw, much less encouraged.
(said @Maria-12648430)

> I definitely agree. I prefer to use tail-recursive functions instead of non-local returns unless that turns out to be too cumbersome. That is, if the code becomes convoluted written in a tail-recursive way, I will write it in a body-recursive way and use throw to break out of the recursion. I have typically used that in complicated optimization passes in the compiler; that is, the code will do the optimization in recursive functions, but if anything turns up that makes the optimization impossible I will throw a `not_possible` exception to break out of the recursion.
(said @bjorng)

### Naming

***
##### Be consistent when naming concepts
> Use the same variable name for the same concept everywhere (even in different modules).

*Examples*: 

```erlang
-module(consistency).

-export([bad/1, good/1]).

bad(UserId) -> internal_bad(UserId).

internal_bad(User_Id) -> internal_bad2(User_Id).

internal_bad2(Usr) -> db:get_by_id(Usr).


good(UserId) -> internal_good(UserId).

internal_good(UserId) -> internal_good2(UserId).

internal_good2(UserId) -> db:get_by_id(UserId).
```


*Reasoning*: When trying to figure out all the places where an ``OrgID`` is needed (e.g. if we want to change it from ``string`` to ``binary``), it's way easier if we can just grep for ``OrgID`` instead of having to check all possible names.

***
##### Explicit state should be explicitly named
> Name your state records ``#mod_state`` and use ``-type state():: #mod_state{}`` in all your modules that implement OTP behaviors.

*Examples*: 

`src/state/bad.erl`:

```erlang
-module(bad).

-behaviour(gen_server).

-export([start/1, increment/0, retrieve/0]).
-export([init/1, terminate/2, code_change/3,
         handle_call/3, handle_cast/2, handle_info/2]).

-spec start(pos_integer()) -> {ok, pid()}.
start(InitialValue) ->
  gen_server:start_link({local, ?MODULE}, ?MODULE, InitialValue, []).

-spec retrieve() -> pos_integer().
retrieve() -> gen_server:call(?MODULE, retrieve).

-spec increment() -> ok.
increment() -> gen_server:cast(?MODULE, increment).


-spec init(pos_integer()) -> {'ok', pos_integer()}.
init(InitialValue) -> {ok, InitialValue}.

-spec handle_call(retrieve, {pid(), term()}, pos_integer()) ->
        {'reply', pos_integer(), pos_integer()}.
handle_call(retrieve, _From, Value) ->
  {reply, Value, Value}.

-spec handle_cast(increment, pos_integer()) -> {'noreply', pos_integer()}.
handle_cast(increment, Value) ->
  {noreply, Value + 1}.

-spec handle_info(any(), pos_integer()) -> {'noreply', pos_integer()}.
handle_info(_Msg, Value) -> {noreply, Value}.

-spec terminate(
        normal | shutdown | {shutdown, term()} | term(), pos_integer()) -> 'ok'.
terminate(_Reason, _Value) -> ok.

-spec code_change(term() | {down, term()}, pos_integer(), term()) ->
        {'ok', pos_integer()}.
code_change(_OldVersion, Value, _Extra) -> {ok, Value}.
```

`src/state/good.erl`:

```erlang
-module(good).

-behaviour(gen_server).

-export([start/1, increment/0, retrieve/0]).
-export([init/1, terminate/2, code_change/3,
         handle_call/3, handle_cast/2, handle_info/2]).

-record(good_state, {value :: pos_integer()}).

-type state() :: #good_state{}.

-spec start(pos_integer()) -> {ok, pid()}.
start(InitialValue) ->
  gen_server:start_link({local, ?MODULE}, ?MODULE, InitialValue, []).

-spec retrieve() -> pos_integer().
retrieve() -> gen_server:call(?MODULE, retrieve).

-spec increment() -> ok.
increment() -> gen_server:cast(?MODULE, increment).


-spec init(pos_integer()) -> {'ok', state()}.
init(InitialValue) -> {ok, #good_state{value = InitialValue}}.

-spec handle_call(retrieve, {pid(), term()}, state()) ->
        {'reply', pos_integer(), state()}.
handle_call(retrieve, _From, State) ->
  {reply, State#good_state.value, State}.

-spec handle_cast(increment, state()) -> {'noreply', state()}.
handle_cast(increment, State) ->
  {noreply, State#good_state{value = State#good_state.value + 1}}.

-spec handle_info(any(), state()) -> {'noreply', state()}.
handle_info(_Msg, State) -> {noreply, State}.

-spec terminate(
        normal | shutdown | {shutdown, term()} | term(), state()) -> 'ok'.
terminate(_Reason, _State) -> ok.

-spec code_change(term() | {down, term()}, state(), term()) -> {'ok', state()}.
code_change(_OldVersion, State, _Extra) -> {ok, State}.
```


*Reasoning*: OTP behaviours implementations usually require a state, and if it has a recognizable name it makes it more easily identifiable. Defining a type for it, helps _dialyzer_ detect leaks (where an internal type as the state is used outside of the module).
The usage of the module prefix in the record name has the goal of distinguishing different state tuples while debugging: Since records are just tuples when one is dumped into the shell it is easier to read `{good_state, att1, attr2}` than `{state, attr1, attr2, attr3}` or `{state, attr1, att2}`.
At a glance you know that the tuple/record can be found in the `good.erl`module.


***
##### Don't use _Ignored variables
> Variables beginning with _ are still variables, and are matched and bound, the _ just keeps the compiler from warning when you don't use them. If you add the _ to a variable's name, don't use it.

*Examples*: 

```erlang
-module(ignored_vars).

-export([good/1, bad/1]).

bad(_Number) -> 2 * _Number.

good(Number) -> 2 * Number.
```


*Reasoning*: They are **not** supposed to be used.

***
##### Avoid boolean parameters
> Don't use boolean parameters (i.e. `true` and `false`) to control clause selection.

*Examples*: 

```erlang
-module(boolean_params).

-export([bad/1, good/1]).

bad(EdgeLength) -> bad_draw_square(EdgeLength, true).

bad_draw_square(EdgeLength, true) ->
  square:fill(square:draw(EdgeLength));
bad_draw_square(EdgeLength, false) ->
  square:draw(EdgeLength).

good(EdgeLength) -> good_draw_square(EdgeLength, full).

good_draw_square(EdgeLength, full) ->
  square:fill(square:draw(EdgeLength));
good_draw_square(EdgeLength, empty) ->
  square:draw(EdgeLength).
```


*Reasoning*: Clarity of intention and not requiring the reader to check the function definition to understand what it does.

***
##### Stick to one convention for naming modules
> Stick to one convention when naming modules (i.e: ik_something vs iksomething vs something).

*Examples*: 

`src/naming_modules/bad/house.erl`:

```erlang
-module(house).
```

`src/naming_modules/bad/xmpl_user.erl`:

```erlang
-module(xmpl_user).
```

`src/naming_modules/good/xmpl_house.erl`:

```erlang
-module(xmpl_house).
```

`src/naming_modules/good/xmpl_user.erl`:

```erlang
-module(xmpl_user).
```


*Reasoning*: It gives coherence to your system.

***
##### Lowercase atoms
> Atoms should use only lowercase characters. Words in atom names should be separated with `_`. Special cases are allowed (like `'GET'`, `'POST'`, etc.) but should be properly justified.

*Examples*: 

```erlang
-module(atoms).

-export([bad/0, good/0]).

bad() -> ['BAD', alsoBad, bad_AS_well].

good() -> [good, also_good, 'good@its.mail'].
```


*Reasoning*: Adhering to one convention makes it easier not to have "duplicated" atoms all around the code. Also, not using caps or special characters reduces the need for `'` around atoms.

***
##### Function Names
> Function names must use only lowercase characters or digits. Words in function names must be separated with `_`.

*Examples*: 

```erlang
-module(function_names).

-export([badFunction/0, 'BAD_FUNCTION'/0, good_function/0, base64_encode/0]).

badFunction() -> {not_allowed, camel_case}.

'BAD_FUNCTION'() -> {not_allowed, upper_case}.

good_function() -> ok.

base64_encode() -> ok.
```


*Reasoning*: Function names are atoms, they should follow the same rules that apply to them.

***
##### Variable Names
> CamelCase must be used for variables. Don’t separate words in variables with `_`.

*Examples*: 

```erlang
-module(variable_names).

-export([bad/2, good/2]).

bad(Variablename, Another_Variable_Name) ->
  [Variablename, Another_Variable_Name].

good(Variable, VariableName) ->
  [Variable, VariableName].
```


*Reasoning*: Adhering to one convention makes it easier not to have "duplicated" variables all around the code. Camel-case makes variable names more visually distinguishable from atoms and it matches the OTP standard.

### Strings

***
##### IOLists over string concatenation
> Use iolists instead of string concatenation whenever possible

*Examples*: 

```erlang
-module(iolists).

-export([good/1, bad/1]).

bad(Param) -> "Hello " ++ binary_to_list(Param) ++ "! Have a nice day!".

good(Param) -> ["Hello ", Param, "! Have a nice day!"].
```


*Reasoning*: Performance and errors during conversion. [iolists](http://www.erlangpatterns.org/iolist.html) are just deeply nested lists of integers and binaries to represent IO data to avoid copying when concatenating strings or binaries.

### Macros

***
##### No Macros
> Don't use macros, except for very specific cases, that include
> * Predefined ones: ``?MODULE``, ``?MODULE_STRING`` and ``?LINE``
> * Literal constants: ``?DEFAULT_TIMEOUT``

*Examples*: 

```erlang
-module(macros).

-define(OTHER_MODULE, other_module).
-define(LOG_ERROR(Error),
        error_logger:error_msg(
          "~p:~p >> Error: ~p~n\tStack: ~p",
          [?MODULE, ?LINE, Error, erlang:get_stacktrace()])).

-define(HTTP_CREATED, 201).

-export([bad/0, good/0]).

bad() ->
  try
    ?OTHER_MODULE:some_function(that, may, fail, 201)
  catch
    _:Error ->
      ?LOG_ERROR(Error)
  end.

good() ->
  try
    other_module:some_function(that, may, fail, ?HTTP_CREATED)
  catch
    _:Error ->
      log_error(?LINE, Error)
  end.

log_error(Line, Error) ->
  error_logger:error_msg(
    "~p:~p >> Error: ~p~n\tStack: ~p",
    [?MODULE, Line, Error, erlang:get_stacktrace()]).
```


*Reasoning*: Macros make code harder to debug. If you're trying to use them to avoid repeating the same block of code over and over, you can use functions for that.
See [related blog post](https://medium.com/@erszcz/when-not-to-use-macros-in-erlang-1d3f10d377f#.xc9b4bsl9) by [@erszcz](https://github.com/erszcz).

***
##### Uppercase macros
> Macros should be named in ALL_UPPER_CASE:

*Examples*: 

```erlang
-module(macro_names).

-define(bad, 1).
-define(BADMACRONAME, 2).
-define(Bad_Macro_Name, 3).
-define(Bad_L33t_M@Cr0, 4).

-define(GOOD, 5).
-define(GOOD_MACRO_NAME, 6).
```


*Reasoning*: It makes it easier not to duplicate macro names, to find them using grep, etc.

***
##### No module or function name macros
> Don't use macros for module or function names

*Examples*: 

```erlang
-module(macro_mod_names).

-define(SERVER, ?MODULE). % Oh, god! Why??
-define(TM, another_module).

-export([bad/1, good/1]).

bad(Arg) ->
  Parsed = gen_server:call(?SERVER, {parse, Arg}),
  ?TM:handle(Parsed).

good(Arg) ->
  Parsed = gen_server:call(?MODULE, {parse, Arg}),
  another_module:handle(Parsed).
```


*Reasoning*: Copying lines of code to the console for debugging (something that happens *a lot*) becomes a really hard task if we need to manually replace all the macros.

### Records

***
##### Record names
> Record names must use only lowercase characters. Words in record names must be separated with `_`. Same rule applies to record field names

*Examples*: 

```erlang
-module(record_names).

-export([records/0]).

-record(badName, {}).
-record(bad_field_name, {badFieldName :: any()}).
-record('UPPERCASE', {'THIS_IS_BAD' :: any()}).

-record(good_name, {good_field_name :: any()}).

records() -> [#badName{}, #bad_field_name{}, #'UPPERCASE'{}, #good_name{}].
```


*Reasoning*: Record and field names are atoms, they should follow the same rules that apply to them.

***
##### Records go first
> Records that are used within a module should be defined before any function bodies.

*Examples*: 

```erlang
-module(record_placement).

-export([good/0, bad/0]).

-record(good, { this_record   :: any()
              , appears       :: any()
              , before        :: any()
              , the_functions :: any()}).

good() -> [#good{}].

-record(bad,  { this_record :: any()
              , appears     :: any()
              , below       :: any()
              , a_function  :: any()}).

bad() -> [#bad{}].
```


*Reasoning*: Records are used to define data types that will most likely be used by multiple functions on the module, so their definition can not be tied to just one. Also, since records will be associated to types, it's a good practice to place them in code in a similar way as the documentation does (and edoc puts types at the beginning of each module documentation)

***
##### Don't share your records
> Records should not be shared among multiple modules. If you need to share _objects_ that are represented as records, use opaque exported types and provide adequate accessor functions in your module.

*Examples*: 

```erlang
-module(record_sharing).

-include("record_sharing.hrl").

-export([bad/0, good/0, good_field/1, good_field/2]).

-record(good, {good_field :: string()}).
-opaque good() :: #good{}.
-export_type([good/0]).

-spec good() -> good().
good() -> #good{}.

-spec good_field(good()) -> string().
good_field(#good{} = Good) -> Good#good.good_field.

-spec good_field(good(), string()) -> good().
good_field(#good{} = Good, Value) -> Good#good{good_field = Value}.

-spec bad() -> #bad{}.
bad() -> #bad{}.
```


*Reasoning*: Records are used for data structure definitions. Hiding those structures aids encapsulation and abstraction. If a record structure needs to be changed and its definition is written in a .hrl file, the developer should find all the files where that .hrl and verify that his change hasn't broken anything. That's not needed if the record structure is internal to the module that manages it.

***
##### Avoid records in specs
> Avoid using records in your specs, use types.

*Examples*: 

```erlang
-module(record_spec).

-record(state, {field1:: any(), field2:: any()}).

-opaque state() :: #state{}.

-export_type([state/0]).

-export([bad/1, good/1]).

-spec bad(#state{}) -> {any(), #state{}}.
bad(State) -> {State#state.field1, State}.

-spec good(state()) -> {any(), state()}.
good(State) -> {State#state.field1, State}.
```


*Reasoning*: Types can be exported, which aids documentation and, using ``opaque`` types it also helps with encapsulation and abstraction.

***
#####  Types in records
> Always add type definitions to your record fields

*Examples*: 

```erlang
-module(record_types).

-export([records/0]).

-record(bad, {no_type}).

-record(good, {with_type :: string()}).

records() -> [#bad{}, #good{}].
```


*Reasoning*: Records define data structures, and one of the most important parts of that definition is the type of the constituent pieces.

### Misc

***
##### Write function specs
> Write the **-spec**'s for your exported fun's, and for unexported fun's when it adds real value for documentation purposes. Define as many types as needed.

*Examples*: 

```erlang
-module(specs).

-export([bad/2, good/2]).

bad(InitialValue, Commands) ->
  gen_server:call(?MODULE, {compute, InitialValue, Commands}).

-type command() :: inc | dec.
-spec good(pos_integer(), [command()]) -> pos_integer().
good(InitialValue, Commands) ->
  gen_server:call(?MODULE, {compute, InitialValue, Commands}).
```


*Reasoning*: Dialyzer output is complicated as is, and it is improved with good type names. In general, having semantically loaded type names for arguments makes reasoning about possible type failures easier, as well as the function's purpose.

***
##### Use -callback attributes over behaviour_info/1.
> Unless you know your project will be compiled with R14 or lower, use ``-callback`` instead of ``behavior_info/1`` for your behavior definitions.

*Examples*: 

`src/callbacks/bad.erl`:

```erlang
-module(bad).

-export([behavior_info/1]).

behavior_info(callbacks) -> [{function1, 2}].
```

`src/callbacks/good.erl`:

```erlang
-module(good).

-callback function1(binary(), State) -> {ok, State}.
```


*Reasoning*: Avoid deprecated functionality

***
##### Use atoms or tagged tuples for messages
> When sending a message between processes, you should typically either send a single, human-readable atom, or a tuple with a human-readable atom placed in element 1. This includes messages being sent via ``gen_server:call`` and the like.

*Examples*: 

```erlang
-module(message_formatting).

-export([bad/1, good/1]).

bad(Pid) ->
    %% These are error-prone and confusing, as there's no indication of what the message
    %% is supposed to be used for on the receiving end:
    Pid ! -1,
    gen_server:cast(Pid, self()),
    %% These are better, but still less readable, as first tuple element
    %% is not being used to tag the message:
    gen_server:call(Pid, {123, set_count}),
    gen_server:call(Pid, {make_ref(), notify, <<"something">>}).

good(Pid) ->
    %% These are examples of well-formatted messages:
    gen_server:cast(Pid, reload_config),
    gen_server:call(Pid, {set_count, 123}),
    gen_server:call(Pid, get_count),
    Pid ! {notify, make_ref(), <<"hello world">>}.
```


*Reasoning*: Tagging messages with a distinctive, human-readable atom helps clarify the purpose of a message for anyone reading or debugging the code. Using element 1 of the tuple makes code more consistent and predictable, and improves readability when browsing through multiple clauses of functions like ``handle_call``.

This pattern also helps avoid bugs where different messages get confused with one another, or where messages get sent to the wrong recipient; it's much easier to find the source of an unexpected message if it looks like ``{set_foobar_worker_pid, <0.312.0>}`` than if you just find a bare pid in your mailbox.

***
##### No nested header inclusion
> When having many _nested_ "include files", use -ifndef(HEADER_FILE_HRL) .... -endif so they can be included in any order without conflicts.

*Examples*: [nested](include/nested.hrl)

*Reasoning*: ``-include`` directives in included headers may lead to duplication of inclusions and/or other conflicts and it also hides things from the developer view.

***
##### No types in include files
> No `-type` in hrl files

*Examples*: 

```erlang
-module(types).

-include("bad_types.hrl").

-type id() :: pos_integer().

-record(type, {id :: id(), name :: binary()}).
-opaque type() :: #type{}.

-export_type([id/0, type/0]).
%% If you later want to use these types on your specs you DO NOT have to include
%% any file and you just write -spec my_function(types:id()) -> types:type().
```


*Reasoning*: Defining types in public header files (especially those intended for inclusion via `-include_lib()`) might lead to type name clashes between projects and even modules of a single big project.
Instead, types should be defined in modules which they correspond to (with `-export_type()`) and this way take advantage of the namespacing offered by module names.
In other words, "no type definitions in header files" rule means that we will always need to use `some_mod:some_type()` unless referring to a type from the same module it's defined in.
Following this rule you also get the benefits that `-opaque` types provide, for instance, to dialyzer.

***
##### Don't import
> Do not use the `-import` directive

*Examples*: 

```erlang
-module(import).

-export([good/1, bad/1]).

-import(lists, [map/2]).

bad(L) -> map(fun(X) -> X * 2 end, L).

good(L) -> lists:map(fun(X) -> X * 2 end, L).
```


*Reasoning*: Importing functions from other modules makes the code harder to read and debug since you cannot directly distinguish local from external functions. In appropriately named functions, the module is _part_ of the function name, it gives meaning to it.

***
##### Don't export_all
> Do not use the `-compile(export_all)` directive

*Examples*: 

```erlang
-module(export_all).

-compile(export_all). % Avoid, better to do
% -export([real_fun/0, other_fun/0]).

real_fun()  -> does_something.
other_fun() -> does_something_else.
```


*Reasoning*: It's generally considered best to only export the specific functions that make up your module's known and documented external API. Keeping this list of functions small and consistent encourages good encapsulation and allows for more aggressive refactoring and internal improvements without altering the experience for those who make use of your module.

***
##### Encapsulate OTP server APIs
> Never do raw ``gen_server`` calls across module boundaries; the call should be encapsulated in an API function in the same module that implements the corresponding ``handle_call`` function. The same goes for other such OTP constructs (``gen_server`` casts, ``gen_fsm`` events, etc).

*Examples*: 

```erlang
-module(otp_encapsulation).

-behavior(gen_server).

-export([start_link/0]).
-export([init/1, handle_call/3, handle_cast/2, handle_info/2, terminate/2, code_change/3]).
-export([good/0, bad/0]).

start_link() ->
  gen_server:start_link({local, ?MODULE}, ?MODULE, nil, []).

good() ->
  %% Good, because this function is an API call that encapsulates our gen_server implementation:
  gen_server:call(?MODULE, do_good).

bad() ->
  %% Bad, because we're sending an event to some other process whose implementation is defined
  %% in another module. This breaks encapsulation:
  gen_fsm:send_all_state_event(some_fsm, make_everyone_sad).

%% gen_server implementation

init(nil) ->
  {ok, nostate}.

handle_call(do_good, _From, State) ->
  {reply, yay, State}.

handle_cast(_Msg, State) ->
  {noreply, State}.

handle_info(_Msg, State) ->
  {noreply, State}.

terminate(_Reason, _State) ->
  ok.

code_change(_OldVersion, State, _Extra) ->
  {ok, State}.
```


*Reasoning*: By sticking to this pattern of encapsulation, we make it _much_ easier to find out where calls/events might originate from.
Instead of having to search through the entire source tree for e.g. ``gen_server`` calls that look like they might send a certain message to a given process, we can just search for calls to the corresponding API function.
This makes it much easier to modify APIs, and also allows us to benefit more from Dialyzer's checks, assuming our API functions have appropriate type specs on them.
We can also change the underlying message format without disturbing any code outside of the module in question, and we can more easily avoid issues with RPC calls when running a mixed cluster.
With good encapsulation, you can even do things like convert a ``gen_server`` to a ``gen_fsm`` without any code changes beyond just the one module.

***
##### No debug calls
> Unless your project is meant to be run as an escript, there should be no `io:format` nor `ct:pal` calls in your production code (i.e. in the modules inside the `src` folder). Same rule applies for `lager` or `error_logger` calls if they're used just for debugging purposes during test stages.

*Examples*: 

```erlang
-module(debug_calls).

-export([bad/1, good/1]).

-spec bad(any()) -> any().
bad(Input) ->
  io:format("About to do something with ~p~n", [Input]),
  R = god:create_user(Input),
  ct:pal("The result was ~p", [R]),
  R.

-spec good(any()) -> any().
good(Input) ->
  god:create_user(Input).
```


*Reasoning*: Leaving unnecessary logs on production code impacts performance. It increases the processing time for the functions you're debugging and also consumes disk space if the logs are written to a file (as they usually are). Besides, more often than not the log messages are only understood in the context of the test or debugging round in which they were created, therefore the become useless pretty fast.

***
##### Don't Use Case Catch
> Don't capture errors with `case catch`, use `try ... of ... catch` instead.

*Examples*: 

```erlang
-module(case_catch).

-export([bad/1, good/1]).

bad(List) ->
  case catch hd(List) of
    {'EXIT', {badarg, Reason}} ->
      {badarg, Reason};
    Hd ->
      Hd
  end.

good(List) ->
  try hd(List) of
    Hd ->
      Hd
  catch
    badarg:T ->
      {badarg,T}
  end.
```


*Reasoning*: `case catch ...` mixes good results with errors which is confusing. By
using `try ... of ... catch` the golden path is kept separate from the error
handling.


### Tools

***
##### Lock your dependencies
> In your rebar.config or Erlang.mk, specify a tag or commit, but not master.

*Examples*:
- [erlang.mk](priv/Makefile)
- [rebar.config](priv/rebar.config)

*Reasoning*: You don't want to be suddenly affected by a change in one of your dependencies. Once you've found the right version for you, stick to it until you *need* to change.

***
##### Loud errors
> Don't let errors and exceptions go unlogged. Even when you handle them, write a log line with the stack trace.

*Examples*: 

```erlang
-module(loud_errors).

-export([bad1/1, bad2/1, good1/1, good2/1]).

bad1(WithThis) ->
  try
    something:that(may, fail, WithThis)
  catch
    _:Error ->
      {error, Error}
  end.

bad2(WithThis) ->
  try
    something:that(may, fail, WithThis)
  catch
    _:Error ->
      throw({error, Error})
  end.

good1(WithThis) ->
  try
    something:that(may, fail, WithThis)
  catch
    _:Error ->
      lager:error("Error here: ~p~n"
                  " Arguments: ~p~n"
                  " Stack: ~p", [Error, WithThis, erlang:get_stacktrace()]),
      {error, Error}
  end.

good2(WithThis) ->
  try
    something:that(may, fail, WithThis)
  catch
    _:Error ->
      exit({error, Error})
  end.
```


*Reasoning*: The idea is that somebody watching the logs has enough info to understand what's happening.

***
##### Properly use logging levels
> When using lager, use the different logging levels with the following meanings:

*Meanings*:
  * ``debug``: Very low-level info, that may cover your screen and don't let you type in it :P
  * ``info``: The system's life, in some detail. Things that happen usually, but not all the time. You should be able to use the console with acceptable interruptions in this level.
  * ``notice``: Meaningful things that are worth noticing, like the startup or termination of supervisors or important gen_servers, etc…
  * ``warning``: Handled errors, the system keeps working as usual, but something out of the ordinary happened
  * ``error``: Something bad and unexpected happen, usually an exception or error (**DO** log the **stack trace** here)
  * ``critical``: The system (or a part of it) crashed and somebody should be informed and take action about it
  * ``alert``: _There is no rule on when to use this level_
  * ``emergency``: _There is no rule on when to use this level_

***
##### Prefer the https protocol over others when specifying dependency URLs
> When specifying dependencies in erlang.mk Makefiles or rebar.config, prefer using the https protocol to download the dependency repository.

*Examples*:
 * [makefile example](src/dependency_protocol/dep_protocol.makefile)
 * [rebar example](src/dependency_protocol/dep_protocol.config)

*Reasoning*: HTTPS is recommended by GitHub and is easier for CI.

* [Git on the Server - The Protocols](http://git-scm.com/book/ch4-1.html)
* [GitHub Official Recommendation](https://help.github.com/articles/which-remote-url-should-i-use/)
* [GitHub Protocol Comparison](https://gist.github.com/grawity/4392747#file-github-protocol-comparison-md)

***
##### No implicit functions with mixer
> Don't implicitly include all functions from a module when using the [mixer](https://github.com/chef/mixer) library. Explicitly list all mixed-in functions.

*Examples*: 

```erlang
-module(mixer).

-mixer([bad]).

-mixin(
  [ { good,
      [ a_function/3
      , another_function/2
      , yet_another_one/2
      ]}
  ]).
```


*Reasoning*: Knowing all the functions that are included in a module makes it easier to reason about it. If any number of functions are implicitly brought from another module, it introduces an extra level of unnecessary indirection that requires jumping back and forth between files. The less information we have to keep in our heads the better.

## Suggestions & Great Ideas

Things that should be considered when writing code, but do not cause a PR rejection, or are too vague to consistently enforce.

***
##### Prefer pattern-matching over testing for equality
> When you want to write a conditional statement based on a comparison of two values, don't use equality and then switch according to the boolean result value. Use pattern matching instead.

*Examples*: 

```erlang
-module(prefer_pm).

-export ([good/3, bad/3]).

%% @doc Uses equality comparisons (=:=) for everything
-spec bad(T, T, 0|1|2) -> ok.
bad(A, B, 0) ->
  case A =:= B of
    true -> proceed();
    false -> fail(A)
  end;
bad(A, B, 1) ->
  case change(A) =:= B of
    true -> proceed();
    false -> fail(A)
  end;
bad(A, B, 2) ->
  case change(A) =:= change(B) of
    true -> proceed();
    false -> fail(A)
  end.

%% @doc Uses pattern-matching everywhere
-spec good(T, T, 0|1|2) -> ok.
good(A, B, 0) ->
  case A of
    B -> proceed();
    A -> fail(A)
  end;
good(A, B, 1) ->
  case change(A) of
    B -> proceed();
    C -> fail(C)
  end;
good(A, B, 2) ->
  case {change(A), change(B)} of
    {C, C} -> proceed();
    {D, _} -> fail(D)
  end.

change(X) -> {changed, X}.
proceed() -> ok.
fail(E) -> exit({error, E}).
```


*Reasoning*:
From a semantic standpoint, _boolean switches_ after _equality_ introduce static boolean logic in your code, reducing its flexibility. Besides, pattern matching is just more declarative. And, specially in the case where there is a function involved, using pattern matching you get a chance to _do something_ with the result of such a function call.

***
##### Favor higher-order functions over manual use of recursion
> Occasionally recursion is the best way to implement a function, but often a fold or a list comprehension will yield safer, more comprehensible code.

*Examples*: 

```erlang
-module(recursion).

-export([recurse/1, fold/1, map/1, comprehension/1]).

%%
%% Example:
%% Different functions to capitalize a string
%%

%% BAD: makes unnecessary use of manual recursion
recurse(S) ->
    lists:reverse(recurse(S, [])).

recurse([], Acc) ->
    Acc;
recurse([H | T], Acc) ->
    NewAcc = [string:to_upper(H) | Acc],
    recurse(T, NewAcc).

%% GOOD: uses a fold instead to achieve the same result,
%% but this time more safely, and with fewer lines of code
fold(S) ->
    Result = lists:foldl(fun fold_fun/2, [], S),
    lists:reverse(Result).

fold_fun(C, Acc) ->
    [string:to_upper(C) | Acc].

%% BETTER: uses a map instead of a fold to yield a simpler
%% implementation, since in this case a fold is overkill
map(S) ->
    lists:map(fun string:to_upper/1, S).

%% BEST: in this case, a list comprehension yields the
%% simplest implementation (assuming we ignore the fact
%% that string:to_upper can also be used directly on strings)
comprehension(S) ->
    [string:to_upper(C) || C <- S].
```


*Reasoning*: Manually writing a recursive function is error-prone, and mistakes can be costly. In the wrong circumstances, a buggy recursive function can miss its base case, spiral out of control, and take down an entire node. This tends to counteract one of the main benefits of Erlang, where an error in a single process does not normally cause the entire node to crash.

Additionally, to an experienced Erlang developer, folds and list comprehensions are much easier to understand than complex recursive functions. Such contstructs behave predictably: they always perform an action for each element in a list. A recursive function may work similarly, but it often requires careful scrutiny to verify what path the control flow will actually take through the code in practice.

***
##### CamelCase over Under_Score
> Symbol naming: Use variables in CamelCase and atoms, function and module names with underscores.

*Examples*: 

```erlang
-module(camel_case).

-export([bad/0, good/0]).

bad() ->
  Variable_Name = moduleName:functionName(atomConstant),
  another_ModuleName:another_Function_Name(Variable_Name).

good() ->
  VariableName = module_name:function_name(atom_constant),
  another_module_name:another_function_name(VariableName).
```


*Reasoning*: It helps a lot with the next issue in this list ;)

***
##### Prefer shorter (but still meaningful) variable names
> As long as it's easy to read and understand, keep variable names short

*Examples*: 

```erlang
-module(var_names).

-export([bad/1, good/1]).

bad(OrganizationToken) ->
  OID = organization:get_id(OrganizationToken),
  OID.

good(OrgToken) ->
  OrgID = organization:get_id(OrgToken),
  OrgID.
```


*Reasoning*: It helps reducing line lengths, which is also described above

***
##### Comment levels
> Module comments go with **%%%**, function comments with **%%**, and code comments with **%**.

*Examples*: 

```erlang
% this comment is badbad
%%% @doc This comment is good
-module(comment_levels).

-export([bad/0, good/0]).

% @doc This comment is bad
%%% @doc This comment is also bad
bad() ->
  R = 1 + 2, %%% This comment is not good
  R. %% This comment is bad again

%% @doc I like this comment
good() ->
  % This comment is approved by the International Commenting Association
  % and Chuck Norris
  R = 1 + 2,
  R. % This comment (megusta)
```


*Reasoning*: It clearly states what the comment is about, also helpful to search for specific comments, like "%% @".

***
##### Keep functions small
> Try to write functions with a small number of expressions, and that do only one thing. **12** expressions per function except for integration tests is a good measure.

*Examples*: 

```erlang
-module(small_funs).

-export([bad/2, good/2]).

bad(UserEmail, Message) ->
  User =
    case users:find_by_email(UserEmail) of
      notfound ->
        users:new_with_email(UserEmail);
      FoundUser ->
        FoundUser
    end,
  
  EscapedMessage = message_utils:escape(Message),
  CleanMessage = bad_word_checker:clean(EscapedMessage),

  db:store_message(User, CleanMessage),
  
  DeviceIds = user:get_devices(User),
  lists:foreach(
    fun(DeviceId) ->
      case devices:get_device(DeviceId) of
        notfound -> ok;
        Device ->
          case device:get_push_info(Device) of
            {apns, Token} ->
              ApnsMsg = apns:build_message(CleanMessage),
              apns:send_msg(Token, ApnsMsg);
            {gcm, Token} ->
              GcmMsg = gcm:new_message(CleanMessage),
              gcm:send_message(Token, GcmMsg);
            _ -> ok
          end
      end
    end, DeviceIds).

good(UserEmail, Message) ->
  User = find_or_create_user(UserEmail),
  CleanMessage = clean_message(Message),

  db:store_message(User, CleanMessage),

  deliver_message(User, CleanMessage).


find_or_create_user(UserEmail) ->
  case users:find_by_email(UserEmail) of
    notfound ->
      users:new_with_email(UserEmail);
    FoundUser ->
      FoundUser
  end.

clean_message(Message) ->
  EscapedMessage = message_utils:escape(Message),
  bad_word_checker:clean(EscapedMessage).

deliver_message(User, Message) ->
  DeviceIds = user:get_devices(User),
  Devices =
    [devices:get_device(DeviceId) || DeviceId <- DeviceIds],
  lists:foreach(
    fun(notfound) -> ok;
       (Device) -> send_message(device:get_push_info(Device), Message)
    end, Devices).

send_message({apns, Token}, Message) ->
  ApnsMsg = apns:build_message(Message),
  apns:send_msg(Token, ApnsMsg);
send_message({gcm, Token}, Message) ->
  GcmMsg = gcm:new_message(Message),
  gcm:send_message(Token, GcmMsg);
send_message(_, _) -> ok.
```


*Reasoning*: From 3 different sources:
- Small functions aid readability and composeability. Readability aids maintainability. This cannot be stressed enough. The smaller your code, the easier it is to fix and change.
- A small function allows one to see its purpose clearly, so that you need to only understand the small subset of operations it performs, which makes it very simple to verify it works correctly.
- These are all compeling reasons:
  + a function should do one thing, if it's too large you are likely to be doing work better suited for multiple functions
  + clarity, it's easier to see what a function does when it's short and concise
  + reuse, keeping them short means you can use them later for something else (specially true for Erlang)
  + screen size: you want to be able to see the whole function if you want to connect via ssh to a server for whatever reason

*Notes*:

This guideline, together with **[Avoid deep nesting](#avoid-deep-nesting)** and **[More, smaller functions over case expressions](#more-smaller-functions-over-case-expressions)**, can be well followed by structuring your functions as follows:

```erlang
some_fun(#state{name=foo} = State) ->
  do_foo_thing(),
  continue_some_fun(State);
some_fun(#state{name=bar} = State) ->
  do_bar_thing(),
  continue_some_fun(State).

continue_some_fun(State) ->
  ...,
  ok.

```

Remember:

- There is no cost for a tail call like that.
- This pattern is efficient, compact, clear.
- It "resets" indentation so the code doesn't wander off the right edge of the screen.

Most importantly:

- It's easier to test because the functions delineate the testing hinge points.
- It gives more surface for tracing, so one can get very specific about where the computation goes off the rails. Nested cases are opaque at runtime.

***
##### Use behaviours.
> Encapsulate reusable code in behaviors.

*Examples*: 

```erlang
-module(behavior).

-type element() :: binary().
-type id() :: pos_integer().

-export_type([element/0, id/0]).

-callback store(element()) -> id().
-callback retrieve(id()) -> notfound | element().
-callback delete(id()) -> ok.
-callback count() -> non_neg_integer().
```


*Reasoning*: It's the OTP way ;)

***
##### When programming defensively, do so on client side
Do validations on the outmost layers of your code.

*Examples*: 

```erlang
-module(validations).

-export([bad/1, good/1]).

bad(X) ->
  gen_server:call(?MODULE, {add, X}).

good(X) when is_integer(X) ->
  gen_server:call(?MODULE, {add, X});
good(X) ->
  throw({invalid_input, X}).
```


*Reasoning*: One aspect of choosing where want you to crash is how you design your API: A function that checks the input before calling the gen_server behind it will avoid a full roundtrip to the gen_server and maybe even a gen_server crash.
do_it(Pid, X) when is_integer(X) -> gen_server:call(Pid, {do_it, X}).
If you design this way, the caller crashes if the arg is wrong.
If you don't tighten up the function head, the gen_server will crash.

***
##### Avoid unnecessary calls to length/1
> Lots of use cases of length/1 can be replaced by pattern matching, this is specially true when checking if the list has at least one element.

*Examples*: 

```erlang
-module(pattern_matching).

-export([bad/1, good/1]).

bad(L) ->
  case length(L) of
    0 -> error;
    _ -> ok
  end.

good([]) ->
  error;
good(_L) ->
  ok.
```


*Reasoning*: Pattern matching is one of the core aspects of Erlang and as such it's both performant and readable. Pattern matching is also more flexible so changes to the logic get simpler.

***
##### Move stuff to independent applications
> When you identify a block of functionality that is self-contained (it may be several modules or just a big one) and actually independent of the main purpose of your application, place that in a separate application. And consider open-sourcing it.

*Reasoning*: It's easier to share among apps. If open-sourced, you're sharing it with the community and you get the benefits of the community being involved in it.

*Note*: Do **not** create highly specific libraries that are too coupled with the project you're working on. Use this rule for libraries that will likely be reused in other projects.

***
##### Use the facade pattern on libraries
> [The facade pattern](http://en.wikipedia.org/wiki/Facade_pattern) is great to simplify library usage and serves as a form of self-documentation.

*Examples*: [kafkerl](https://github.com/inaka/kafkerl/blob/master/src/kafkerl.erl)

*Reasoning*: Having the relevant functions in a single module means that the end user doesn't have a hard time figuring out which functions to call. Note that to avoid making it too complex, you probably want to carefully consider which functionality you wish to support here; exposing fewer functions (the ones that show the basic use of the library) as opposed to just creating a dummy module containing every single exported function in the library is preferred.
This greatly reduces the learning curve of the library and therefore makes it more tempting to use.

***
##### Types in exported functions
> Custom data types used in exported functions should be defined with Erlang type declarations and exported from the module

*Examples*: 

```erlang
-module(data_types).

-export([bad/1, good/1]).

-type your_type() :: {integer(), string()}.
-opaque my_type() :: {binary(), binary()}.
-export_type([your_type/0, my_type/0]).

-spec good(your_type()) -> {ok, my_type()}.
good({I, S}) -> {ok, {integer_to_binary(I), list_to_binary(S)}}.

-spec bad({integer(), string()}) -> {ok, {binary(), binary()}}.
bad({I, S}) -> {ok, {integer_to_binary(I), list_to_binary(S)}}.
```


*Reasoning*: It helps with function documentation and, when using opaque types, we ensure encapsulation.

***
##### Separate responsibilities in sumo_db
> When using sumo_db you should separate the responsibilities clearly, creating for each entity:
> - one module (usually called MODELs) to describe the entity and allow administrating instances of the model in memory
> - one module (usually called MODEL_repo) to handle the various operations that require business logic relating to the entity

*Examples*: [separate responsibilities in sumo_db](https://github.com/inaka/fiar/tree/master/src/models)

*Reasoning*: By dividing the functions into two different modules we increase understandability of the functionality especially if these are called from external modules. It also allows us to better organize the code and have smaller modules.
