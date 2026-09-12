"""The /who-this-is-for/ section.

Every other part of this site is organised by what the business does. This one
is organised by who is in the room, because the four people in a typical team
have four different objections and only one of them is about software.

Written to the same rules as everything else here: no statistics, no invented
research, no client names, no claims about outcomes we cannot stand behind. The
position is stated plainly and repeatedly — this is about the team you have
doing more, not about having fewer of them — because a page that dances around
that question is read as an answer to it.
"""

from content.helpers import sect, faq_section, faq_schema
from data.site import SITE

ORIGIN = SITE["origin"]
BASE = "/who-this-is-for/"

AUDIENCES = [
    ("worried-about-your-job", "If you think this is about replacing you",
     "The honest version of what we are hired to do, who we report to, and what "
     "we will not do."),
    ("never-used-it", "If you have never opened one and don't know where to start",
     "No prior knowledge, no jargon, and one job to try this week."),
    ("teaching-yourself", "If you are already using it and nobody asked you to",
     "You are the most useful person in the business and the most exposed. Both "
     "are fixable."),
    ("owners-and-managers", "If you are the one who has to decide",
     "Three decisions only you can make, and the business case that does not "
     "rely on losing anybody."),
]


def _hero(h1, lede, crumb=None):
    """Crumbs are hand-written here: build.py only normalises them on the
    salvaged routes, and this section was written from scratch."""
    trail = '<a href="/">Home</a>'
    if crumb:
        trail += f' / <a href="{BASE}">Who it\'s for</a>'
    return (f'<section class="phero"><div class="shell">'
            f'<p class="crumb">{trail}</p>'
            f'<h1>{h1}</h1><p class="lede">{lede}</p>'
            f'</div></section>')


def _rows():
    out = ""
    for slug, title, blurb in AUDIENCES:
        out += (f'<a class="row" href="{BASE}{slug}/">'
                f'<span class="row-fam">Start here</span>'
                f'<span class="row-name">{title}<b>{blurb}</b></span></a>')
    return f'<div class="rows">{out}</div>'


# ------------------------------------------------------------------- hub ----

HUB_FAQ = [
    ("Is this training going to be used to justify cutting staff?",
     "Not by us. We are not brought in to review roles and we do not produce "
     "headcount recommendations, efficiency scores or reports on individuals. "
     "What an employer does after any training is their decision and always was, "
     "but nothing we produce is built to support that decision, and we say so in "
     "the room on the day."),
    ("Do people have to want to be there?",
     "They have to be willing to try one thing. Genuine reluctance is easier to "
     "work with than performed enthusiasm, because a sceptic who tests something "
     "properly finds the real limits faster than an optimist who does not."),
    ("What if half the team is already using it and half has never touched it?",
     "That is the normal room, and the sequence is built for exactly that mix. "
     "The people already using it usually have the most to unlearn about where "
     "their information is going, so nobody sits idle."),
    ("Can one session work for four different attitudes at once?",
     "The first half, yes, because the foundations are the same for everybody. "
     "After that people work on their own jobs, which is where the four "
     "positions stop mattering and the work takes over."),
]

HUB_BODY = """
<h2>The same room, four different questions</h2>
<p>Walk into a practice, a clinic, an agency or a workshop and the team splits
roughly four ways. Someone has read enough headlines to be quietly worried about
their job. Someone has never opened one of these tools and is not going to admit
it in front of the room. Someone has been using it every day for a year without
telling anyone, probably in a free account, probably with documents that should
not be in one. And someone is standing at the back of the room paying for the
session and wondering whether any of this survives contact with a Tuesday.</p>
<p>Those are four different objections and only one of them is about software.
Training that answers just the software question loses three of the four people
before lunch.</p>

<h2>Our position, stated once and not moved</h2>
<p>We are hired to make the team a business already has get more of its work
done. That is the whole pitch, and it is not softened for the room and hardened
for the quote. A business that wants a headcount case is not a business we can
help, because the work we do — reusable setups, a written boundary, people
trained on their own documents — is worth nothing to an organisation planning to
have fewer people using it.</p>
<p>The reason is practical rather than noble. The jobs these tools do well in a
small business are the ones that were never going to get a new hire anyway: the
fourth follow-up email, the report that eats a Sunday, the tender that decides a
contract. That work does not disappear when nobody does it. It just gets done
late, by whoever is still there.</p>

<h2>Where to go next</h2>
<p>Pick whichever of the four sounds most like you, or most like the person you
are going to have to convince.</p>
"""


def _hub(ask):
    main = (
        '<main id="main">'
        + _hero("Four people are in the room and they need different things",
                "Every team we train contains someone worried about their job, "
                "someone who has never opened one of these tools, someone "
                "teaching themselves in secret, and someone who has to decide "
                "for all three. Same session, four different starting points.")
        + f'<section class="sect"><div class="shell"><div class="prose">{HUB_BODY}</div>'
        + _rows()
        + '</div></section>'
        + sect("""
<h2>What this is not</h2>
<p>It is not change management, it is not a culture programme, and it is not a
talk about the future of work. There is no slide about the pace of change. The
session is people doing their own work with someone watching over their shoulder
and correcting the habits, and the four pages above exist because the objection
in someone's head decides whether they try anything at all that morning.</p>
<p>If the thing standing between your team and useful work is a rule nobody has
written, that is a different job and it comes first. See
<a href="/services/policy-and-audit/">policy and audit</a>.</p>
""", lift=True)
        + faq_section(HUB_FAQ)
        + "</main>"
    )
    return {
        "title": "Who this is for — four positions on AI in one team — AI at work",
        "description": "Worried about your job, never used it, teaching yourself, "
                       "or the one who has to decide. Four honest starting points "
                       "for AI training in an Australian business, and our position "
                       "on replacement stated plainly.",
        "main": main,
        "schema": [faq_schema(HUB_FAQ)],
        "cta": {
            "h": "Tell us which of the four you are",
            "p": "It changes what the first session looks like more than your "
                 "industry does. One form, one reply from a person.",
        },
    }


# ------------------------------------------------------- worried about job ---

WORRIED_FAQ = [
    ("Will you report back to my employer on how I did?",
     "No. We do not produce per-person assessments, scores or lists of who "
     "struggled. What the business gets afterwards is a note on what the team "
     "worked on and what to reinforce, written about the work rather than about "
     "people."),
    ("If I get faster at my job, doesn't that make me easier to replace?",
     "It makes your output harder to replace, which is the opposite. The part of "
     "your job that is genuinely at risk is the part that is pure retyping, and "
     "that part is at risk whether or not you personally learn anything."),
    ("What if I refuse to use it?",
     "That is your call and we will not push. We would ask you to sit through the "
     "boundary section anyway, because the single most damaging thing anyone does "
     "with these tools is done by accident, by someone who never meant to use one "
     "seriously."),
    ("Is it true these tools make things up?",
     "Yes, confidently and often, which is the main reason the training exists. "
     "Someone who knows the work is the only reliable check on the output, and "
     "that is a description of your job, not a threat to it."),
]

WORRIED_BODY = """
<h2>Who pays us, and what we tell them</h2>
<p>Be clear-eyed about this: the person who books us is usually the person who
signs your pay. So the fair question is not whether we will say something
reassuring to a room, it is what we say to the person paying when you are not
there.</p>
<p>What we tell them is that the honest business case here is capacity, not
headcount, and that a business chasing the second one should not book us. Not
because we are squeamish, but because the work would fail. Everything useful in
this training — setups built in the room, a written boundary, people practising
on their own documents — only pays off when experienced people stay to use it. A
team trained and then cut leaves behind a folder of prompts nobody opens.</p>

<h2>What actually changes in your week</h2>
<p>The parts of a job these tools genuinely take over are narrow and specific.
Turning notes you already made into a structured draft. Producing the fourth
version of an email you have written a hundred times. Finding the clause in a
sixty-page document you already know is in there somewhere. Rewriting something
technical into something a client can follow.</p>
<p>What they do not take over is the part where you decide what should be in the
document, whether the answer is right, whether the client can actually be told
that, and what to do when the situation is not the standard one. Those are not
the leftovers of your job. In most roles, that is the job, and the typing around
it was always the tax.</p>

<h2>The risk that is real</h2>
<p>We are not going to tell you nothing changes, because that is not true and you
would stop listening. Here is the honest shape of it.</p>
<p>The person exposed is not the person whose job involves judgement. It is the
person in a room where three colleagues quietly got much faster at the same work
and one did not, and where nobody said anything for eighteen months. That gap
compounds quietly and it is nearly always invisible until a restructure makes it
visible.</p>
<p>Which is a strange thing for us to say, because it is an argument for turning
up to a session you did not ask for. Take it or leave it; we would rather say it
than pretend the question is silly.</p>

<h2>What we will not do</h2>
<ul>
<li>We do not run efficiency reviews, time-and-motion studies or role audits, and
we decline the work when it is described that way.</li>
<li>We do not produce scoring, rankings or per-person reports.</li>
<li>We do not recommend headcount, and we will not answer the question if asked.</li>
<li>We do not use your work as a demonstration without your say-so on the day.</li>
</ul>

<h2>If you want to get on the front foot</h2>
<p>Pick one job you do repeatedly that involves no client information at all —
an internal summary, a first draft of a standard email, notes tidied into a
structure. Do it the normal way, then do it again with a tool, then compare.
Doing that twice tells you more about where the line sits than any article will,
including this one.</p>
<p>If the never-opened-it part is the bigger obstacle, start at
<a href="/who-this-is-for/never-used-it/">never used it</a>. If you have quietly
been using it for months, the exposure worth knowing about is on
<a href="/who-this-is-for/teaching-yourself/">teaching yourself</a>.</p>
"""


# --------------------------------------------------------------- never used --

NEVER_FAQ = [
    ("Will I be the only one in the room who has never used it?",
     "Very unlikely. The normal room is roughly half people who have barely "
     "touched it, and the half who have are usually doing one narrow thing "
     "repeatedly rather than anything sophisticated."),
    ("Do I need to be good with computers?",
     "No. If you can write an email describing what you want to someone competent "
     "who has never met your business, you have the skill. The hard part is being "
     "specific, and that is a writing problem rather than a technical one."),
    ("Do I have to pay for a subscription to start?",
     "No, and we will tell you when the free version is enough. The free and paid "
     "tiers differ in what happens to your information as well as in capability, "
     "which is covered before anyone signs up to anything."),
    ("How long before it is useful rather than a novelty?",
     "For one narrow job you do repeatedly, usually the same sitting. The gap "
     "between novelty and use is almost always specificity: telling it who the "
     "reader is, what the constraint is, and what a good answer looks like."),
]

NEVER_BODY = """
<h2>Nothing about this is obvious</h2>
<p>A blank box with a cursor in it is genuinely bad design for a first-time user.
It offers no clue about what it is for, what it is good at, or what it will do
badly, and then it answers anything you type with total confidence. People who
find it useful are not cleverer than you. They have usually just tried it against
the same job about thirty times.</p>

<h2>The mental model that helps</h2>
<p>Treat it as a very fast, very widely read assistant on their first morning at
your business. They write well, they have read an enormous amount, they will
never say they are unsure, and they know nothing whatsoever about your clients,
your obligations, your house style or the thing everyone in your office knows not
to do.</p>
<p>Everything that follows comes out of that one picture. You would not hand a
first-morning assistant an unexplained task and send the result straight to a
client. You would tell them who it is for, what it must not say, and what good
looks like, and you would read it before it went out. That is the entire skill.
The rest is practice.</p>

<h2>Start with one job, not with the tool</h2>
<p>The usual failure is opening a tool and hunting for something to use it on.
Reverse it. Take one job you already do most weeks that annoys you, that involves
no client information, and where you would recognise a good answer immediately.
An internal update. A first draft of a standard reply. A messy page of notes that
needs a structure.</p>
<p>Do it three times across a week. Not thirty jobs once each, which teaches you
nothing, but one job three times, which teaches you exactly where the tool is
strong and where it quietly invents.</p>

<h2>What good looks like</h2>
<p>A useful instruction is boring and long. It says who the reader is, what you
want at the end, what must not appear, roughly how long it should be, and what
you are going to do with it. Four or five sentences of that produces a different
class of answer from a single line, and the difference is not subtle.</p>
<p>The worked version of this, with the before and after side by side, is
<a href="/training/useful-output/">getting output you can actually use</a>.</p>

<h2>What to ignore for now</h2>
<p>Agents, automations, plug-ins, model release news and anything promising to
run your business while you sleep. None of it matters until you can reliably get
one page of usable text out of one tool. Ignoring all of it costs you nothing;
chasing it is the most common way people conclude the whole category is nonsense.</p>

<h2>The one thing to learn before anything else</h2>
<p>What never goes in. There is a short list of information that does not belong
in a general-purpose AI tool regardless of how careful you are being, and the
damage is done by people who did not know the list existed rather than by people
ignoring it. Read <a href="/guides/what-never-goes-in/">what never goes in an AI
tool</a> before your first real attempt, not after.</p>
"""


# ----------------------------------------------------------- self-taught ----

SELF_FAQ = [
    ("Am I in trouble if I have been using a free account with work documents?",
     "You are in a common position rather than an unusual one. The useful move is "
     "to establish which account was used and what went into it, then fix the "
     "account and write the rule. Handled quickly and quietly, it is an admin "
     "problem."),
    ("Should I tell my manager?",
     "Almost always yes, and sooner is much better than after an incident. It "
     "lands very differently when it arrives as what I have been doing and what I "
     "think the rule should be than when it surfaces during an audit."),
    ("I am already fast at this. What would training give me?",
     "Usually three things: the account and data settings you never looked at, the "
     "difference between a clever prompt and a reusable setup, and a defensible "
     "answer for where the line sits — which is what turns personal speed into "
     "something the business can rely on."),
    ("Why does it matter which account I used?",
     "Because what happens to your information differs between vendors and between "
     "tiers of the same product, and the defaults are not the same. That is the "
     "first thing covered, on the "
     "<a href=\"/tools/tiers-and-your-data/\">tiers page</a>."),
]

SELF_BODY = """
<h2>You are the most useful person here and the most exposed</h2>
<p>Somebody in most Australian small businesses has been using these tools daily
for a year without being asked to, has got genuinely good at one or two things,
and has never mentioned it because nobody asked and the rule was unclear. If that
is you, you are simultaneously the best asset the business has on this and the
largest single piece of unmanaged risk it carries.</p>
<p>Both of those are fixable in about a fortnight, and neither is a
disciplinary matter unless it is allowed to surface the wrong way.</p>

<h2>The three gaps self-teaching leaves</h2>
<p>They are consistent, and none of them is about skill.</p>
<h3>The account, not the tool</h3>
<p>People who teach themselves almost always start on a free tier, because that is
what you do when you are experimenting on your own time. What happens to the
material you paste in differs between tiers and between vendors, and the defaults
are not what most people assume. This is the first thing to check and the fastest
to fix.</p>
<h3>Clever prompts rather than reusable setups</h3>
<p>Self-taught fluency tends to live in your head and in a chat history nobody
else can see. It reproduces the work each time instead of setting it up once. The
difference between a folder of prompts and a configured setup is the difference
between being fast personally and the business being fast, and it is the single
biggest step up available to someone already competent.</p>
<h3>No defensible line</h3>
<p>You have an instinct for what feels acceptable to paste in. An instinct is not
something you can hand to a new starter, and it is not something you can point to
when somebody asks why a document was handled that way.</p>

<h2>How to bring it into the open</h2>
<p>Go to whoever decides with three things, in this order. What you have been
using and for which jobs. Which account, and what that account does with the
material. What you think the rule should be, written as three or four plain
sentences.</p>
<p>That framing matters. Arriving with a proposed rule makes you the person
setting the standard. Arriving with a confession makes you the incident. The work
is identical; the sequence is not.</p>

<h2>What to do this week if nothing is written down</h2>
<ul>
<li>Establish which accounts are actually in use across the team, not which ones
people were told to use.</li>
<li>Check the data settings on each one. They are not the same across tiers.</li>
<li>Write the never list before the policy — it is shorter, it is the part that
prevents harm, and it can be handed out the same day.</li>
<li>Take the two setups you rebuild most often and make them properly reusable,
so they survive you being on leave.</li>
</ul>
<p>The templates are on <a href="/resources/ai-policy-templates/">AI policy
templates</a>, and the version of this done for you is
<a href="/services/policy-and-audit/">policy and audit</a>.</p>
"""


# ------------------------------------------------------------ decision maker --

OWNER_FAQ = [
    ("What is the business case if it is not headcount?",
     "Work that is currently done late, done badly or not done at all, getting "
     "done. Quotes going out the same day, reports not eating a Sunday, tender "
     "responses actually submitted. In most small businesses that is where the "
     "money is, and it does not require anybody to leave."),
    ("Do I need a policy before training, or after?",
     "Before, if your work is regulated or if information handling is the "
     "exposure. Training a team to move faster in a direction nobody has decided "
     "on is a worse position than an untrained one, and there are engagements we "
     "have turned down until that was sorted."),
    ("How do I know whether it stuck?",
     "Three weeks later, look for whether the setups built on the day are still "
     "being used and whether anybody has built a new one without being asked. "
     "Enthusiasm on the day tells you nothing."),
    ("What if my team thinks this is a prelude to cuts?",
     "Some of them will, and silence confirms it. Say what the training is for "
     "before the date is announced rather than after, and say what will not "
     "happen as a result. If you cannot say that honestly, the training is not "
     "the right next step."),
]

OWNER_BODY = """
<h2>Three decisions only you can make</h2>
<p>Everything else about this can be delegated, bought or learned. These cannot.</p>
<h3>Whether it is allowed</h3>
<p>Not whether you would like people to use it, but whether it is permitted, in
writing, in a form a new starter could read on their first day. The most common
position in Australian small business is no stated position, which people
reliably read as quiet permission, and then handle accordingly.</p>
<h3>What never goes in</h3>
<p>A short, specific, business-shaped list. Not a policy document — a list.
Yours will have categories a generic template does not, and the categories that
matter most are usually the ones that feel obvious to you and are invisible to
someone in their second week.</p>
<h3>Who owns it</h3>
<p>One named person who keeps the setups current, who new starters are pointed
at, and who notices when a tool changes underneath you. Without that, whatever
gets built in a training session decays into a folder nobody opens.</p>

<h2>The business case, honestly</h2>
<p>We will not tell you these tools will let you run the same business with fewer
people, because in businesses of this size that is usually not what happens and
we would rather not be quoted saying it.</p>
<p>What happens is narrower and more useful. Work that was structurally never
getting done starts getting done. The quote goes out the afternoon of the site
visit instead of the following Tuesday. The report that consumed a Sunday takes
an hour on Thursday. The tender that decides a contract gets a proper response
rather than a rushed one. None of that shows up as a line you can cut. All of it
shows up in what the business can take on.</p>
<p>The scope and what it costs is on
<a href="/services/what-it-costs/">what it costs</a>, and what the engagements
actually involve is on <a href="/services/">services</a>.</p>

<h2>What to say to the team, and when</h2>
<p>Before the date is in the calendar, not on the morning. Cover four things: why
this is happening, what the training is for, what will not happen as a result,
and that people are expected to bring their own real work rather than watch a
demonstration.</p>
<p>The third one is the one people are listening for. If you cannot say it
plainly and mean it, they will hear the omission, and you will spend the session
with a room that has decided the exercise is a trap. If you genuinely cannot say
it, the useful conversation to have is not about training.</p>

<h2>What to measure</h2>
<p>Not satisfaction scores on the day. Three weeks later, look at whether the
setups built in the session are still in use, whether anyone has built a new one
unprompted, and whether one named job that used to run late is now running on
time. If the answer to all three is no, the training did not stick and we would
rather know.</p>

<h2>If you want the short version of where you stand</h2>
<p>The <a href="/assessment/">assessment</a> is nine questions and about four
minutes. It gives you the modules ordered for your work, a reading on where you
are exposed right now, and one recommended starting point — which is sometimes a
policy engagement rather than training, and it says so when it is.</p>
"""


BODIES = {
    "worried-about-your-job": (
        "If you think this is about replacing you",
        "The honest version: who pays us, what we tell them, what actually "
        "changes in your week, and the one risk we are not going to pretend "
        "away.",
        WORRIED_BODY, WORRIED_FAQ,
        "AI training and your job — the honest version — AI at work",
        "What AI training actually changes in a job, who we report to, and what "
        "we will not do. Written for the person in the room who did not ask to "
        "be there.",
        {"h": "Bring the question into the room",
         "p": "If the person booking the session cannot say plainly what will "
              "not happen afterwards, the training is not the right next step. "
              "We will say that to them too."}),
    "never-used-it": (
        "If you have never opened one and don't know where to start",
        "No prior knowledge assumed, no jargon, and one job to try this week.",
        NEVER_BODY, NEVER_FAQ,
        "Never used AI before — where to start — AI at work",
        "A first-principles start for people who have never used Claude or "
        "ChatGPT: the mental model that helps, the one job to try first, and "
        "what to ignore entirely for now.",
        {"h": "Half the room has never opened one either",
         "p": "The sequence is built for a team that is split, so nobody is "
              "sitting idle and nobody is being talked down to."}),
    "teaching-yourself": (
        "If you are already using it and nobody asked you to",
        "You are the most useful person in the business on this, and the most "
        "exposed. Both are fixable in about a fortnight.",
        SELF_BODY, SELF_FAQ,
        "Already using AI at work without being asked — AI at work",
        "The three gaps self-teaching leaves: the account and what it does with "
        "your material, reusable setups rather than clever prompts, and a line "
        "you can actually point to. Plus how to raise it without it becoming an "
        "incident.",
        {"h": "Turn personal speed into something the business can rely on",
         "p": "Usually a fortnight of work: fix the account, write the never "
              "list, make two setups reusable. We can do it with you or leave "
              "you to it."}),
    "owners-and-managers": (
        "If you are the one who has to decide",
        "Three decisions nobody can make for you, and a business case that does "
        "not depend on losing anybody.",
        OWNER_BODY, OWNER_FAQ,
        "Deciding on AI for your team — owners and managers — AI at work",
        "The three decisions only the owner can make, the honest business case "
        "for AI training in a small Australian business, what to say to the team "
        "beforehand, and what to measure three weeks later.",
        {"h": "Start with nine questions rather than a proposal",
         "p": "The assessment gives you the modules ordered for your work and a "
              "reading on exposure. Sometimes it says the policy comes first."}),
}


def pages(ask, illos):
    out = {BASE: _hub(ask), "/tools/prompt-builder/": _builder()}
    for slug, (h1, lede, body, faq, title, desc, cta) in BODIES.items():
        main = (
            '<main id="main">'
            + _hero(h1, lede, crumb=True)
            + f'<section class="sect"><div class="shell"><div class="prose">{body}</div></div></section>'
            + faq_section(faq)
            + '<section class="sect sect-lift"><div class="shell"><div class="prose">'
            + '<h2>The other three</h2><p>Same session, different starting point. '
            + " ".join(
                f'<a href="{BASE}{s}/">{t}</a>.'
                for s, t, _ in AUDIENCES if s != slug)
            + '</p></div></div></section>'
            + "</main>"
        )
        out[f"{BASE}{slug}/"] = {
            "title": title,
            "description": desc,
            "main": main,
            "schema": [faq_schema(faq)],
            "cta": cta,
        }
    return out


# --------------------------------------------------------- the prompt builder --

BUILDER_FAQ = [
    ("Does this send my answers anywhere?",
     "No. The whole thing runs in your browser and nothing is transmitted. If "
     "you choose to carry the result into the enquiry form, it travels in the "
     "same browser tab rather than through a URL or a server, and you see "
     "exactly what it says before you send anything."),
    ("Is this just a prompt library with extra steps?",
     "It is the opposite. A library hands you somebody else's wording for their "
     "job. This makes you state who is writing, for whom, under what constraint "
     "and what must never appear, because that sequence is the transferable "
     "skill and the wording is not."),
    ("Why does it ask what must never appear?",
     "Because that is the half of an instruction almost everyone leaves out, and "
     "it is the half that prevents the damage. If you cannot name anything that "
     "is off limits in your work, that is worth five minutes rather than none."),
    ("Will the instruction work in any tool?",
     "It is written to be tool-neutral, which is the point of teaching two. The "
     "builder suggests which of the two suits the job, and says plainly that "
     "neither suggestion is a reason to pay for anything."),
]

BUILDER_BODY = """
<h2>What this is teaching</h2>
<p>A usable instruction answers five things, in order: who is writing, who reads
it, what has to be true of the result, what a good answer looks like, and what
must never appear. Almost every disappointing output traces back to one of the
five being left for the tool to guess.</p>
<p>The builder is not a shortcut around learning that. It is the five questions
with the answers assembled for you, so that after a dozen goes you stop needing
it. That is the intended outcome — a tool you outgrow.</p>

<h2>The part people skip</h2>
<p>The fifth question. Most people write an instruction that describes what they
want and says nothing about what must not happen, then are surprised when a
client's name, an invented figure or a confident guess turns up in the draft. A
named boundary costs one line and is the difference between a first draft you
can edit and one you have to check line by line.</p>
<p>If nothing on that list applies to your work, read
<a href="/guides/what-never-goes-in/">what never goes in an AI tool</a> before
you decide that is true.</p>

<h2>What it will not do</h2>
<p>It will not write the thing for you, it does not connect to any AI tool, and
it will not tell you a paid tier is required. The instruction it produces is
plain text you copy into whichever tool you already have open.</p>
"""


def _builder():
    main = (
        '<main id="main">'
        '<section class="phero"><div class="shell">'
        '<p class="crumb"><a href="/">Home</a> / <a href="/tools/">Tools</a></p>'
        '<h1>Build an instruction worth giving it</h1>'
        '<p class="lede">Five questions, answered in order, assembled into '
        'something you can paste into Claude or ChatGPT. Nothing is sent '
        'anywhere and no account is needed.</p>'
        '</div></section>'
        '<section class="sect" style="padding-top:0"><div class="shell">'
        '<div id="builder"><noscript><p>This builder needs JavaScript. The same '
        'method written out in full is on <a href="/training/useful-output/">'
        'getting output you can actually use</a>.</p></noscript></div>'
        '</div></section>'
        + sect(BUILDER_BODY, lift=True)
        + faq_section(BUILDER_FAQ)
        + '</main>'
    )
    return {
        "title": "Prompt builder — a better AI instruction — AI at work",
        "description": "A free browser-based prompt builder for Australian "
                       "businesses. Five questions — who is writing, who reads it, "
                       "the constraints, what good looks like and what must never "
                       "appear — assembled into an instruction for Claude or "
                       "ChatGPT. Nothing is transmitted.",
        "main": main,
        "schema": [
            faq_schema(BUILDER_FAQ),
            {
                "@type": "WebApplication",
                "name": "Prompt builder",
                "url": f"{ORIGIN}/tools/prompt-builder/",
                "applicationCategory": "BusinessApplication",
                "operatingSystem": "Any modern browser",
                "browserRequirements": "Requires JavaScript",
                "description": "Assembles a structured AI instruction from five "
                               "questions about the job, the reader, the "
                               "constraints and what must never appear.",
                "isAccessibleForFree": True,
                "offers": {"@type": "Offer", "price": "0",
                           "priceCurrency": "AUD"},
                "provider": {"@id": f"{ORIGIN}/#organization"},
            },
        ],
        "cta": {
            "h": "The builder is the method. We teach the judgement",
            "p": "Knowing what to ask for is half of it. Knowing when the answer "
                 "is wrong, and when the job should never have gone near a tool, "
                 "is the half that needs someone in the room.",
        },
    }
