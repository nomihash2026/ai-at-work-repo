"""Depth for the library: guides, resources, company pages and the two index
pages that were carrying the least weight.

The guides and resources are the top of the funnel and they are deliberately
ungated — no email wall anywhere on the site — so they have to be complete
enough to be worth linking to on their own.
"""

from content.helpers import sect
from data.site import INDUSTRIES


def _guides_index(ask, illos):
    return {
        "sections": [
            sect("<h2>Why these three are free</h2>"
                 "<p>Because they're the reason people call. The privacy line, the never "
                 "list and how to get a team started are not trade secrets — they're the "
                 "part you can read at 11pm and act on the next morning. If that's all you "
                 "ever take from this site, it was still worth publishing.</p>"
                 "<p>Nothing here is gated. There is no email wall on this site at all: "
                 "the only form is the <a href='/contact/'>enquiry form</a>, and it exists "
                 "for people who want to talk, not for people who want to read.</p>"),
            sect("<h2>Which one to start with</h2>"
                 "<ul>"
                 "<li><strong>Nobody has written anything down yet.</strong> Start with "
                 "<a href='/guides/what-never-goes-in/'>what never goes in</a> and hand it "
                 "to the team this week. It's the shortest path from exposed to "
                 "bounded.</li>"
                 "<li><strong>You handle client, patient or participant information.</strong> "
                 "Start with <a href='/guides/privacy-basics/'>privacy basics</a>, which "
                 "covers the difference between an obligation and a habit.</li>"
                 "<li><strong>You're about to train people.</strong> Start with "
                 "<a href='/guides/getting-your-team-started/'>getting your team "
                 "started</a>, particularly the section on sequence — most teams begin in "
                 "the wrong place and lose the room.</li>"
                 "</ul>"
                 "<p>Longer pieces, including the industry-specific ones, are on the "
                 "<a href='/insights/'>blog</a>.</p>"
                 + ask("Read one and want it applied to your own work? That's what the "
                       "enquiry form is for."), lift=True),
        ],
    }


def _resources_index(ask, illos):
    return {
        "sections": [
            sect("<h2>What's here and what each one is for</h2>"
                 "<ul>"
                 "<li><strong><a href='/resources/ai-policy-templates/'>AI policy "
                 "templates</a></strong> — starting drafts to mark up. Turning up to a "
                 "policy session with objections to a draft is far faster than turning up "
                 "with a blank page.</li>"
                 "<li><strong><a href='/resources/prompt-library/'>Starting prompt "
                 "library</a></strong> — deliberately short. A handful that match real jobs "
                 "beats fifty that teach copying.</li>"
                 "<li><strong><a href='/resources/vendor-checklist/'>Vendor "
                 "checklist</a></strong> — the questions to ask any AI product aimed at "
                 "your industry, including the two most vendors would rather you didn't "
                 "ask.</li>"
                 "</ul>"
                 "<p>No email address required for any of them, no download gate, no "
                 "follow-up sequence. They're on the page.</p>"),
            sect("<h2>How to use them without us</h2>"
                 "<ol>"
                 "<li>Take the policy template and delete everything that doesn't describe "
                 "your business. What's left is closer to right than most finished "
                 "policies.</li>"
                 "<li>Name the tool and the account type in it. This is the single most "
                 "skipped line and the one that matters most.</li>"
                 "<li>Rewrite the never list using your own document names — not "
                 "\"personal information\" but \"client files, patient notes, participant "
                 "plans\", whatever yours are called.</li>"
                 "<li>Put one name against the checking step, and one name against "
                 "\"who to ask\".</li>"
                 "<li>Hand it out. A page people read beats a manual people don't.</li>"
                 "</ol>"
                 + ask("If step three is where it stalls — and it usually is — that's the "
                       "conversation we have most often."), lift=True),
        ],
    }


def _policy_templates(ask, illos):
    checklist = illos.dg_checklist("Before you circulate any policy, check it names", [
        "The specific tool and the specific account type",
        "Your own documents in the never list, by the names you use for them",
        "What gets checked before anything leaves, and by whom",
        "One person to ask when something isn't covered",
        "A date, so everyone knows whether they're reading the current one",
    ])
    return {
        "sections": [
            sect("<h2>What a usable policy looks like</h2>"
                 "<p>Short. A page, occasionally two. Long policies fail in a specific "
                 "way: people read the first line, infer the rest, and get the inference "
                 "wrong.</p>"
                 f"{checklist}"),
            sect("<h2>The two versions that don't work</h2>"
                 "<p><strong>The one-line ban.</strong> \"Staff must not use AI tools.\" "
                 "Sounds decisive, and it moves every bit of usage onto personal phones "
                 "where you can't see it. You end up with the same exposure and no "
                 "record.</p>"
                 "<p><strong>The generic six-pager.</strong> Downloaded, lightly edited, "
                 "and it doesn't name a single document your business actually produces. "
                 "Staff can't tell whether their Tuesday afternoon task is covered, so they "
                 "decide for themselves — which is the situation the policy was meant to "
                 "fix.</p>"
                 "<p>If you want to go further, "
                 "<a href='/training/team-ai-policy/'>the policy module</a> writes the "
                 "draft in the room with the person who can approve it, and "
                 "<a href='/services/policy-and-audit/'>the audit</a> establishes what's "
                 "actually happening first — because a rule built on a guess is a rule you "
                 "can't enforce.</p>"
                 + ask("Happy to review a draft you've already written. It's usually "
                       "quicker than starting again."), lift=True),
        ],
        "faq": [
            ("Can we just adopt this as written?",
             "You can, and it's better than nothing. It won't name your tools, your "
             "documents or your approver, which is the part that decides whether a policy "
             "gets followed or filed."),
            ("Is this legal advice?",
             "No. It's a practical starting draft. Where your obligations turn on "
             "professional rules — a practice standard, a regulator's guidance, a court's "
             "practice note — those need a qualified review."),
        ],
    }


def _prompt_library(ask, illos):
    return {
        "sections": [
            sect("<h2>Why this is short on purpose</h2>"
                 "<p>Long prompt libraries teach copying. A team with fifty prompts has "
                 "fifty things to search through and no way to tell which one is nearly "
                 "right; a team with six and an understanding of why they work adapts them "
                 "to the seventh job themselves.</p>"
                 "<p>Each one here follows the same structure, which is the actual lesson: "
                 "what the document is for, who reads it, the three or four facts only you "
                 "hold, and a good past example to match.</p>"),
            sect("<h2>How to turn one of these into your own</h2>"
                 "<ol>"
                 "<li>Take the closest one and run it on a job you did last week, where "
                 "you already know what good looks like.</li>"
                 "<li>Compare the output to what you actually sent. The gap is the missing "
                 "context, not a prompting flaw.</li>"
                 "<li>Add the two or three facts that were missing, and attach the example "
                 "you sent.</li>"
                 "<li>When it produces something you'd send, move it into a reusable setup "
                 "so nobody types it again — see "
                 "<a href='/training/reusable-setups/'>reusable setups</a>.</li>"
                 "</ol>"
                 "<p>Nothing in a shared prompt or setup should contain client information. "
                 "The <a href='/guides/what-never-goes-in/'>never list</a> applies to "
                 "prompts as much as to documents, and shared prompts are the place it gets "
                 "forgotten.</p>"
                 + ask("If you'd rather this was done on your real documents than on "
                       "examples, that's a workflow build."), lift=True),
        ],
    }


def _vendor_checklist(ask, illos):
    return {
        "sections": [
            sect("<h2>Using it in the actual call</h2>"
                 "<p>Vendor demos are built to answer questions you didn't ask. The "
                 "checklist works best read out loud, in order, with the answers written "
                 "down — partly for the answers, partly because a vendor who can't answer "
                 "question one has told you something important.</p>"
                 "<p>The two most people skip: whose model is underneath, and what happens "
                 "to your setups when you stop paying. Both are awkward to ask and both "
                 "materially change the decision.</p>"),
            sect("<h2>What a good answer sounds like</h2>"
                 "<p>Specific, and slightly boring. \"It's built on [named model], your "
                 "content isn't used for training, retention is X days, and here's the "
                 "export\" is a good answer. \"We take security very seriously and use "
                 "enterprise-grade encryption\" is not an answer to any of the questions on "
                 "the list.</p>"
                 "<p>The other test worth applying: what does this do that a general tool "
                 "plus a good setup wouldn't? Sometimes the answer is real — genuine domain "
                 "structure, the forms and formats a regulator expects. Sometimes you're "
                 "paying a subscription for vocabulary. More on that under "
                 "<a href='/tools/vendor-questions/'>questions to ask any AI vendor</a>.</p>"
                 + ask("Weighing up a specific product? We have no stake in which way that "
                       "goes, which is the point."), lift=True),
        ],
    }


def _guide_started(ask, illos):
    return {
        "sections": [
            sect("<h2>The order that holds a room</h2>"
                 "<p>Where information goes, then one real job start to finish, then the "
                 "tool decision, then the setups the team keeps. Prompt technique is "
                 "somewhere in the middle and it is not the opener — a session that starts "
                 "there loses half the room in twenty minutes.</p>"
                 "<p>The reasoning for each block, and what to leave out entirely, is in "
                 "<a href='/insights/first-ninety-minutes/'>the first ninety minutes</a>.</p>"),
            sect("<h2>How to tell three weeks later whether it worked</h2>"
                 "<p>Not with a feedback form, which measures whether people enjoyed "
                 "themselves. Ask one question instead: <em>which job is now being done "
                 "differently, and by whom?</em></p>"
                 "<p>One named job, done differently by more than one person, is a "
                 "successful session. Enthusiasm with no named job is a pleasant afternoon "
                 "that changed nothing — and it's the most common outcome of AI training "
                 "generally.</p>"
                 + ask("If you'd rather not run it yourself, a half-day workshop is this "
                       "sequence on your own work."), lift=True),
        ],
    }


def _guide_privacy(ask, illos):
    return {
        "sections": [
            sect("<h2>Obligation, habit, and the difference</h2>"
                 "<p>Most small-business privacy worry is a mix of two things: an actual "
                 "obligation — to a client, a patient, a participant, a professional body — "
                 "and a habit of treating everything in the business as equally sensitive. "
                 "Separating them is most of the work.</p>"
                 "<p>The practical test: if this document leaked, who would be harmed and "
                 "how? A tender response leaking is a commercial problem. A participant's "
                 "plan leaking is a different category entirely. Treating both the same way "
                 "means either over-protecting the tender or under-protecting the plan, and "
                 "in practice it's usually both.</p>"),
            sect("<h2>De-identifying properly</h2>"
                 "<p>Deleting a name is not de-identification. In a small community, a role "
                 "plus a suburb plus a date identifies someone as surely as a name does — "
                 "which matters in regional clinics and disability services more than "
                 "anywhere.</p>"
                 "<ul>"
                 "<li>Remove the combination, not just the name: role, location, date, "
                 "rare condition, unusual circumstance.</li>"
                 "<li>Replace rather than blank, so the document still reads and the output "
                 "still makes sense.</li>"
                 "<li>Decide once, as a business, which document types can be de-identified "
                 "at all — some can't be, and that's a legitimate answer.</li>"
                 "</ul>"
                 "<p>Where the information can't be safely de-identified, the work stays "
                 "with the qualified person. That line is the subject of the "
                 "<a href='/guides/what-never-goes-in/'>never list</a>, and in clinical "
                 "settings this content should be reviewed by someone qualified in your "
                 "field — we say that plainly rather than implying our version is "
                 "enough.</p>"
                 + ask("If you handle patient or participant information, the privacy work "
                       "comes before any training. That's the engagement to ask about."),
                 lift=True),
        ],
    }


def _guide_never(ask, illos):
    split = illos.dg_split(
        {"head": "Usually fine, once the rule names it",
         "items": ["Tenders, capability statements, scopes of works",
                   "Policies, procedures, position descriptions",
                   "Induction and training material",
                   "Standard letters explaining a process, with no client in them",
                   "Job ads and internal summaries",
                   "Reports built from properly de-identified inputs"]},
        {"head": "Never, regardless of tier",
         "items": ["Client, patient or participant identifying information",
                   "Anything under a confidentiality obligation you can't vary",
                   "Credentials, keys, banking or payroll detail",
                   "Documents you haven't got the right to share",
                   "Anything where nobody will check the output",
                   "Regulated judgement: clinical, legal, financial, safety sign-off"]},
        caption="The right-hand column doesn't move with the tool, the tier or the vendor.")
    return {
        "sections": [
            sect("<h2>The two columns</h2>"
                 f"{split}"
                 "<p>Rewrite the left column using your own document names before you hand "
                 "this to anyone. A list that says \"participant plans\" gets followed; a "
                 "list that says \"personal information\" gets nodded at.</p>"),
            sect("<h2>The question people ask next</h2>"
                 "<p><em>What about the six months before we had a rule?</em></p>"
                 "<p>Establish which account, roughly when, and what kind of document. Fix "
                 "the setting. Write the rule. Move on. Treating it as misconduct "
                 "guarantees you never hear about the next one, and unreported use is the "
                 "thing you're trying to eliminate — not honesty about it. There's more on "
                 "how to run that conversation in "
                 "<a href='/insights/your-team-is-already-using-ai/'>this article</a>.</p>"
                 + ask("If you'd rather the awkward questions came from outside the "
                       "business, that's what a policy and audit engagement does."),
                 lift=True),
        ],
        "faq": [
            ("Does the paid tier change this list?",
             "It changes the left column's edges slightly. It does not change the right "
             "column at all."),
            ("Who should own this list?",
             "One person, named on the document, with the authority to answer the cases it "
             "doesn't cover. A list without an owner stops being current within a month."),
        ],
    }


def _industries_index(ask, illos):
    rows = "".join(
        f'<li>{illos.svg_industry_mark(slug)}<div><strong>'
        f'<a href="/industries/{slug}/">{name}</a></strong></div></li>'
        for slug, name in INDUSTRIES)
    return {
        "sections": [
            sect("<h2>Published tracks</h2>"
                 f'<ul class="chips" style="list-style:none;padding:0;display:grid;'
                 f'gap:1rem;grid-template-columns:repeat(auto-fit,minmax(16rem,1fr))">'
                 f'{rows}</ul>'
                 "<p>Seven published, and the taxonomy behind them covers ten families and "
                 "around forty-five verticals. We publish one when the task detail is real "
                 "enough that an owner reads three lines and recognises their own Tuesday — "
                 "not before. Forty pages that are ninety percent template with a swapped "
                 "noun would read as thin to you, to Google and to the AI assistants people "
                 "now ask for recommendations.</p>"),
            sect("<h2>If your industry isn't here yet</h2>"
                 "<p>The foundations don't change — roughly seventy percent of the work is "
                 "identical across industries, which is the whole basis of the "
                 "<a href='/training/'>curriculum</a>. What an unpublished track means is "
                 "that we haven't written your version of the task detail down, not that we "
                 "can't run the engagement.</p>"
                 "<p>In practice the first call does the work the page would have done: we "
                 "ask which jobs are done by the person who also signs the cheque, and the "
                 "answer sequences the modules. Brokers, recruitment, builders, beauty and "
                 "aesthetics, hospitality, ecommerce, not-for-profits and migration agents "
                 "are the ones most often asked for.</p>"
                 + ask("Tell us what the business does and what's eating the week. An "
                       "unpublished industry is not a barrier."), lift=True),
        ],
        "faq": [
            ("Why not just publish all forty?",
             "Because thin pages with a swapped noun are obvious to a reader and to a "
             "search engine, and they cost the credibility that is the entire product."),
            ("Do you charge more for an unpublished industry?",
             "No. What moves the figure is team size, number of sites, regulated "
             "complexity and how much is built with you — set out on the "
             "<a href='/services/what-it-costs/'>scope and price</a> page."),
        ],
    }


def _case_studies(ask, illos):
    return {
        "sections": [
            sect("<h2>Why there are no logos on this page</h2>"
                 "<p>Client work in accounting, legal, health and NDIS settings is "
                 "confidential by default. Publishing a named case study needs written "
                 "consent, which takes longer to get than a composite takes to write — and "
                 "a composite dressed up as a case study is the kind of thing this site "
                 "exists to argue against.</p>"
                 "<p>So what's described here is the honest shape of each engagement: what "
                 "the problem usually is, what gets built, and what changes. When there are "
                 "named studies with consent, they'll appear here and they'll be worth "
                 "reading.</p>"),
            sect("<h2>What to ask us instead</h2>"
                 "<p>On a first call, these are fair questions and we'll answer them "
                 "directly:</p>"
                 "<ul>"
                 "<li>Have you done this in my industry, and what did the engagement look "
                 "like?</li>"
                 "<li>What's the most common thing you find when you audit a business like "
                 "mine?</li>"
                 "<li>What did you get wrong in a recent engagement, and what changed as a "
                 "result?</li>"
                 "<li>Which part of this do you think won't work for us?</li>"
                 "</ul>"
                 "<p>The last two are the useful ones. Anyone can describe a success.</p>"
                 + ask("Ask them on a call rather than reading a page written to flatter "
                       "us."), lift=True),
        ],
    }


def _about(ask, illos):
    return {
        "sections": [
            sect("<h2>What we won't take on</h2>"
                 "<p>Published up front rather than discovered halfway through an "
                 "engagement:</p>"
                 "<ul>"
                 "<li>Anything where a wrong output is a regulated harm rather than an "
                 "inconvenience — clinical medicine, financial advice, tax positions as "
                 "distinct from tax admin, safety sign-off. Those stay with the qualified "
                 "person.</li>"
                 "<li>Anything needing domain expertise we don't hold. Credibility is the "
                 "whole product, and it doesn't survive one confident wrong answer in front "
                 "of a room of specialists.</li>"
                 "<li>Training a team to use a tool the business hasn't sanctioned. The "
                 "rule comes first, or the risk lands on the staff.</li>"
                 "<li>Marketing agencies as a flagship audience. It's the most AI-literate "
                 "cohort in business and the least in need of fundamentals.</li>"
                 "</ul>"),
            sect("<h2>How we're paid, and by whom</h2>"
                 "<p>By the business that books the engagement, and by nobody else. No "
                 "reseller agreement, no partner status, no affiliate links, no referral "
                 "fees, and no commission on any tool we recommend. Where the free tier is "
                 "genuinely enough for the work, we say so.</p>"
                 "<p>Pricing isn't published, and the reasoning for that — along with what "
                 "actually moves the number — is on the "
                 "<a href='/services/what-it-costs/'>scope and price</a> page. You get a "
                 "written figure before any commitment, every time.</p>"
                 + ask("If that sounds like the way you'd want this handled, the form is "
                       "one page and a person reads it."), lift=True),
        ],
    }


BUILDERS = {
    "/guides/": _guides_index,
    "/guides/getting-your-team-started/": _guide_started,
    "/guides/privacy-basics/": _guide_privacy,
    "/guides/what-never-goes-in/": _guide_never,
    "/resources/": _resources_index,
    "/resources/ai-policy-templates/": _policy_templates,
    "/resources/prompt-library/": _prompt_library,
    "/resources/vendor-checklist/": _vendor_checklist,
    "/industries/": _industries_index,
    "/case-studies/": _case_studies,
    "/about/": _about,
}
