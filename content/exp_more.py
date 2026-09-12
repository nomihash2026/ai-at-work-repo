"""Second expansion batch: the pages a buyer reads immediately before or after
deciding to enquire.

The pricing page is the hardest of these, because no figure is published. It
earns its place by saying precisely what moves the number and what you'll be
told on the first call — which is more useful than a range that would be wrong
within a quarter, even if it filters less.
"""

from content.helpers import sect
from data.site import INDUSTRIES


def _what_it_costs(ask, illos):
    drivers = illos.dg_steps([
        ("How many people, and how many sites",
         "One room of eight is a different engagement from four offices of six. "
         "Multi-site work needs the rule to hold in rooms nobody from head office is "
         "standing in."),
        ("Whether policy comes first",
         "In regulated work it does, and it's a separate piece of work before anyone is "
         "trained. That sequencing is a cost and it's also the thing that makes the "
         "training defensible."),
        ("How much is built with you",
         "A workshop teaches method. A workflow build constructs a working setup on your "
         "real documents, with your hands on the keyboard. The second takes longer and "
         "leaves more behind."),
        ("Regulated complexity",
         "Clinical, legal and NDIS settings need content that stands up to review, "
         "sometimes including review by someone qualified in your field. That is time, "
         "and skipping it would be worse than charging for it."),
    ], caption="Four things move the figure. None of them is how much we think you can "
               "afford.")
    return {
        "sections": [
            sect("<h2>What actually moves the number</h2>"
                 f"{drivers}"),
            sect("<h2>What you'll be told on the first call</h2>"
                 "<ol>"
                 "<li>Which engagement shape fits, and if that's a smaller one than you "
                 "asked about, that's what we'll say.</li>"
                 "<li>A figure, in writing, before any commitment — not a range that "
                 "firms up later.</li>"
                 "<li>What it excludes, named, so there's no second invoice for something "
                 "you assumed was in.</li>"
                 "<li>Whether we're the wrong fit. Sometimes the honest answer is that you "
                 "need a systems person, a lawyer, or nothing at all yet.</li>"
                 "</ol>"
                 "<p>What you won't get: a proposal that requires a second meeting to "
                 "understand, or a discount for signing this week. If a figure needs "
                 "urgency to look reasonable, it wasn't reasonable.</p>", lift=True),
            sect("<h2>Why no published range, honestly</h2>"
                 "<p>Because a figure published now would be wrong within a quarter, and a "
                 "stale price is worse than none — it anchors a conversation on a number "
                 "neither side believes.</p>"
                 "<p>The argument against our own position, since it's a fair one: a "
                 "published range filters better. You'd know in ten seconds whether this is "
                 "in your world, and we'd have fewer conversations that end in a polite no. "
                 "We think that trade is worth making for now, and when there is a stable "
                 "figure it goes on this page publicly rather than being quoted "
                 "case by case.</p>"
                 "<h3>What we can tell you now</h3>"
                 "<p>Engagements are scoped as pieces of work, not hourly. Nothing recurs "
                 "unless you've chosen "
                 "<a href='/services/advisory/'>ongoing advisory</a> deliberately. "
                 "Everything built during an engagement is yours, in your own accounts, and "
                 "keeps working if you never speak to us again.</p>"
                 + ask("Tell us the size of the team and what's eating the week, and "
                       "you'll have a figure rather than a conversation about figures.")),
        ],
        "faq": [
            ("Can you give me a ballpark on the phone?",
             "Yes. The reason it isn't on the page is that it depends on the four things "
             "above, not that it's a secret."),
            ("Do you charge for the first call?",
             "No. It's about twenty minutes and its purpose is working out what the actual "
             "problem is, which is sometimes not the one in the enquiry."),
            ("Is there a minimum engagement?",
             "There's a practical floor, in that a session shorter than about two hours "
             "doesn't change anything and we'd rather not sell one. Below that, the free "
             "<a href='/guides/'>guides</a> are a better use of your time than our "
             "invoice."),
            ("What if we need to stop halfway?",
             "You keep everything built to that point, and you're not billed for work not "
             "done. Scopes are written in pieces for that reason."),
        ],
    }


def _services_index(ask, illos):
    return {
        "sections": [
            sect("<h2>Choosing between the four</h2>"
                 "<ul>"
                 "<li><strong>Several people, each doing something slightly unsafe or "
                 "slightly inefficient</strong> — a <a href='/services/team-workshop/'>team "
                 "workshop</a>. One room, one method, everyone leaves with the same "
                 "boundary.</li>"
                 "<li><strong>One document that keeps costing you an evening</strong> — a "
                 "<a href='/services/workflow-build/'>workflow build</a>. One job, "
                 "constructed on real work with the person who owns it.</li>"
                 "<li><strong>You don't know what's already being used, and the work is "
                 "regulated</strong> — <a href='/services/policy-and-audit/'>policy and "
                 "audit</a>, first, before anyone is trained.</li>"
                 "<li><strong>Use is spreading and you want it spreading "
                 "deliberately</strong> — <a href='/services/advisory/'>ongoing "
                 "advisory</a>, but only after the first piece of work.</li>"
                 "</ul>"
                 "<p>They're not tiers and there's no upgrade path. A workflow build isn't "
                 "a bigger workshop; it's a different thing, and businesses often need the "
                 "smaller-sounding one.</p>"),
            sect("<h2>What every engagement has in common</h2>"
                 "<ol>"
                 "<li><strong>A written scope and a figure before any commitment.</strong> "
                 "Including what's excluded.</li>"
                 "<li><strong>Built with you, not for you.</strong> Setups you didn't build "
                 "are setups you can't adjust when the template changes.</li>"
                 "<li><strong>The boundary settled first.</strong> Which tool, which "
                 "account, what never goes in, and what stays with a qualified person.</li>"
                 "<li><strong>Everything is yours.</strong> In your accounts, documented, "
                 "working whether or not we ever speak again.</li>"
                 "<li><strong>An honest no where it applies.</strong> Some problems are a "
                 "systems problem, a staffing problem or a lawyer's problem wearing an AI "
                 "costume.</li>"
                 "</ol>"
                 + ask("Not sure which shape fits? Say what's in the way and we'll tell "
                       "you — including if the answer is none of them."), lift=True),
        ],
        "faq": [
            ("Can we combine two of these?",
             "Frequently. Policy and audit followed by a workshop is the most common "
             "sequence in regulated work, scoped as two pieces rather than one bundle so "
             "you can stop after the first."),
            ("Do you deliver online or in person?",
             "Both. Multi-site businesses are often better served online; the boundary "
             "conversation goes slightly better in person because people ask the awkward "
             "questions out loud."),
            ("How far ahead do you book?",
             "It varies with capacity, and we'd rather give you a real date than a "
             "reassuring one. Ask on the first call."),
        ],
    }


def _why_two_tools(ask, illos):
    return {
        "sections": [
            sect("<h2>The commercial reason most trainers teach one</h2>"
                 "<p>It's cheaper to build, cheaper to maintain and easier to sell. It also "
                 "makes the trainer a distribution channel for one vendor, which is fine "
                 "for the vendor and quietly expensive for you: your work reshapes itself "
                 "around one tool's weak side, and the jobs it handles badly either get "
                 "done badly or get done by hand.</p>"
                 "<p>We have no reseller agreement, partner status, affiliate link or "
                 "referral fee with either vendor, and where a free tier is genuinely "
                 "sufficient we say so. That's the only reason the recommendation carries "
                 "any weight.</p>"),
            sect("<h2>Three places the difference shows up immediately</h2>"
                 "<ol>"
                 "<li><strong>Where your information goes.</strong> Data handling differs "
                 "between vendors <em>and</em> between tiers of the same vendor. That's the "
                 "first question a practice principal or an NDIS director actually has, so "
                 "it's the opening module rather than a closing "
                 "disclaimer — see <a href='/tools/tiers-and-your-data/'>tiers and your "
                 "data</a>.</li>"
                 "<li><strong>Long work versus quick work.</strong> These pull toward "
                 "different tools, and a rule of thumb for which to reach for beats any "
                 "prompt list. The rule is on "
                 "<a href='/tools/which-tool/'>which tool for which job</a>.</li>"
                 "<li><strong>Reusable setups.</strong> Both tools have a version of this, "
                 "they work differently, and it's the feature that turns a one-off session "
                 "into a lasting change.</li>"
                 "</ol>"
                 + ask("Want the split applied to your own jobs? That's twenty minutes on "
                       "a call, not a project."), lift=True),
        ],
        "faq": [
            ("Isn't two tools twice the training?",
             "No, because the skill is the same. What differs is the interface and the "
             "reach-for-this rule, and the rule takes about fifteen minutes to teach."),
            ("What if we've already standardised on one?",
             "Then the useful work is knowing which of your jobs sit on its weak side, so "
             "those outputs get checked harder. That's a decision rather than an accident, "
             "and it's a legitimate one."),
        ],
    }


def _assessment(ask, illos):
    return {
        "sections": [
            sect("<h2>Why the plan shows before anything is asked of you</h2>"
                 "<p>Nine questions, about four minutes, and the full plan renders on "
                 "screen — modules in order, recommended starting engagement, and a reading "
                 "on where your current exposure sits. No email address, no gate, no "
                 "download.</p>"
                 "<p>That's a deliberate trade. A principal who reads the plan and "
                 "recognises their own week is a better conversation than someone who "
                 "traded an address for a PDF they never opened, and we'd rather have fewer "
                 "and better ones. Nothing you type is transmitted anywhere — the whole "
                 "thing runs in your browser.</p>"),
            sect("<h2>What the plan gives you</h2>"
                 "<ul>"
                 "<li>The six foundation modules, ordered for your work rather than listed "
                 "as a syllabus — in regulated settings the policy module usually moves to "
                 "the front.</li>"
                 "<li>A recommended starting engagement out of the five shapes, with the "
                 "reasoning.</li>"
                 "<li>Which of your selected jobs suit which tool, and which stay with a "
                 "qualified person.</li>"
                 "<li>A reading on current exposure, based on what you've said about "
                 "accounts, information types and whether a written rule exists.</li>"
                 "</ul>"
                 "<h3>Who should fill it in</h3>"
                 "<p>Whoever can approve a change: an owner, a principal, a practice or "
                 "office manager, a director. The questions are about how the business runs "
                 "and what it's exposed to, and an employee guessing at those produces a "
                 "plan for a business that doesn't exist.</p>", lift=True),
            sect("<h2>What happens to your answers</h2>"
                 "<p>Nothing leaves your browser unless you choose to carry the plan into "
                 "the <a href='/contact/'>enquiry form</a>, in which case a summary is held "
                 "in this tab's session storage and appears in an editable field you can "
                 "change or clear. Nothing about your business goes into a URL, and there "
                 "is no tracking pixel on the tool. The full position is in the "
                 "<a href='/privacy/'>privacy policy</a>.</p>"
                 "<h3>If you'd rather not use the tool</h3>"
                 "<p>Then don't — it's a shortcut, not a gate. Two sentences in the "
                 "enquiry form about what the business does and what's eating the week gets "
                 "you to the same first call. The tool exists because it makes that call "
                 "shorter and more accurate, not because we need the answers.</p>"
                 + ask("Prefer to skip straight to a conversation? The form takes about a "
                       "minute.")),
        ],
        "faq": [
            ("Is this a lead magnet?",
             "It's a planning tool that we'd rather you used than not. The distinction that "
             "matters: the plan shows in full before anything is asked of you, and no email "
             "address is collected anywhere in it."),
            ("What if my industry isn't in the list?",
             "There's a path for that, and it produces a plan from the foundations rather "
             "than an industry track. It's less specific and still useful."),
            ("Can I send the plan to someone else?",
             "Print it, or carry it into the enquiry form and send it with a note. It isn't "
             "emailed to you, because nothing here asks for your email."),
        ],
    }


BUILDERS = {
    "/services/what-it-costs/": _what_it_costs,
    "/services/": _services_index,
    "/about/why-two-tools/": _why_two_tools,
    "/assessment/": _assessment,
}


def _home(ask, illos):
    """The homepage. The week list in the hero already does the job a hero should
    do, so nothing is added above the fold except a change of destination on the
    primary button: the enquiry form is the conversion action, and the
    assessment is demoted to the quiet one."""
    clock = illos.dg_clock("Half a day, as it actually runs", [
        ("0:00", "Where information goes",
         "Which tool, which account, what never goes in, and what stays with a "
         "qualified person — using your documents as the examples."),
        ("0:40", "One real job, start to finish",
         "A job from your business, taken from blank to something you would send."),
        ("1:45", "Everyone does it themselves",
         "Own hands, own laptop. Where the habits get corrected."),
        ("3:00", "Setups you keep",
         "Two or three saved setups on your most common documents. This is the part "
         "that's still there in a month."),
    ], caption="A two-hour session covers the first two blocks and the last one. The "
               "hands-on middle is what a half day buys.")
    ba = illos.dg_beforeafter([
        ("The standard explanatory letter",
         "Rewritten from scratch, or copied from an old one and half-edited.",
         "A saved setup produces your version from three or four facts, in your voice."),
        ("A long document you need the gist of",
         "Read in full by whoever has time, usually the most expensive person available.",
         "Answered against your own checklist, with the source open beside it."),
        ("The monthly report",
         "An evening, often a weekend, done by the owner.",
         "A structured draft in an hour. The judgement stays yours."),
    ])
    return {
        "replace": [
            ('<a class="btn-primary" href="/assessment/">Build your training plan</a>\n'
             '      <a class="btn-quiet" href="/industries/">Find your industry</a>',
             '<a class="btn-primary" href="/contact/">Start an enquiry</a>\n'
             '      <a class="btn-quiet" href="/assessment/">Build your training plan</a>'),
        ],
        "sections": [
            # The salvaged page already argues the one-spine case under "why the
            # industry page matters more than the course", and already lists the
            # industries. Repeating either would pad the page, so what gets added
            # here is only what was missing: what a session is actually like, what
            # changes afterwards, and the boundary drawn rather than described.
            sect("<h2>What a session actually looks like</h2>"
                 "<p>Not a lecture with a slide deck. About two thirds of the time is your "
                 "team doing their own work while someone who knows the tools watches over "
                 "their shoulder and corrects the habits.</p>"
                 f"{clock}", lift=True),
            sect("<h2>What's different three weeks later</h2>"
                 "<p>The test isn't the feedback form at the end of the day. It's one "
                 "question later: which job is now being done differently, and by whom? One "
                 "named job, done differently by more than one person, is a session that "
                 "worked.</p>"
                 f"{ba}"
                 + ask("Tell us which of these is your version and we'll tell you which "
                       "engagement fits.")),
            sect("<h2>The boundary, drawn</h2>"
                 "<p>Two columns, and the right-hand one doesn't move with the tool, the "
                 "tier or the vendor. Tenders, policies, induction material, standard "
                 "explanatory letters and reports from de-identified inputs sit on the "
                 "left. Clinical judgement, financial advice, tax positions and safety "
                 "sign-off sit on the right, permanently.</p>"
                 + illos.svg_boundary() +
                 "<p>We also teach both Claude and ChatGPT with no reseller agreement, "
                 "partner status or referral fee in either direction, and we'll tell you "
                 "when a free tier is enough. The reasoning is on "
                 "<a href='/about/why-two-tools/'>why we teach two tools</a>.</p>",
                 lift=True),
        ],
        "faq": [
            ("Who is this for?",
             "The person who owns the P&L and carries the risk — an owner, principal, "
             "practice or office manager, or director. Staff are in the room; the decision "
             "isn't theirs to make."),
            ("Do we need to know anything already?",
             "No. The normal room is half cautious, half already using it unofficially, and "
             "the sequence is built for exactly that mix."),
            ("What if our work is regulated?",
             "Then the written rule comes before any training, and that's a separate piece "
             "of work. See <a href='/services/policy-and-audit/'>policy and audit</a>."),
            ("Is there anything to read before enquiring?",
             "Plenty, and none of it is gated. The <a href='/guides/'>guides</a> and the "
             "<a href='/insights/'>blog</a> carry the reasoning we'd give you on a call."),
        ],
        "faq_heading": "Questions we get before the first call",
    }


BUILDERS["/"] = _home
