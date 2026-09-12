"""Metadata overrides.

The salvaged titles read well on the page but several ran past the length a
search result will show, which buries the useful half. These replace them.
Descriptions are rewritten only where the original was too short to say
anything a person could act on.

Rule of thumb used here: title under about 60 characters including the brand
suffix, description between 140 and 165, and the first six words carrying the
thing someone is actually searching for.
"""

METAS = {
    "/industries/accounting-bookkeeping/": {
        "title": "AI training for accounting practices — AI at work",
    },
    "/industries/real-estate/": {
        "title": "AI training for real estate agencies — AI at work",
    },
    "/industries/legal-conveyancing/": {
        "title": "AI training for law firms and conveyancers — AI at work",
    },
    "/industries/ndis-providers/": {
        "title": "AI training for NDIS providers — AI at work",
    },
    "/resources/": {
        "description": "Free AI policy templates, a short starting prompt library and a "
                        "vendor checklist you can use before any engagement. No email "
                        "address required for any of them.",
    },
    "/terms/": {
        "description": "Terms covering use of this website and the assessment tool, what "
                       "the published guidance is and isn't, and the limits of the "
                       "information on these pages.",
    },
    "/tools/claude/projects/": {
        "description": "How to set up a Claude Project that holds your context, examples "
                       "and house rules, so the whole team gets your format without "
                       "anyone rebuilding the prompt each time.",
    },
    "/insights/": {
        "title": "Blog — practical AI at work — AI at work",
    },
}


# ---------------------------------------------------------------------------
# Length pass.
#
# Thirty-one descriptions ran past what a search result shows, which buries the
# half that would earn the click and gives an answer engine a truncated summary
# to quote. These are rewritten to sit under about 158 characters with the
# query intent in the opening clause. Applied as an update rather than as new
# entries so the title overrides above survive.
# ---------------------------------------------------------------------------

_DESCRIPTIONS = {
    "/": "Practical AI training for Australian practices, clinics, firms, agencies "
         "and trades. Claude and ChatGPT taught side by side, tool-neutral.",
    "/industries/": "AI training tracks built from the real tasks of Australian "
                    "accounting, real estate, allied health, legal, NDIS, trades "
                    "and cleaning businesses.",
    "/industries/trades/": "AI training for trades and field services. Get the "
                           "quote out the same day as the site visit and follow "
                           "it up without thinking about it.",
    "/industries/allied-health/": "AI training for allied health clinics, with the "
                                  "privacy line settled first. Built for the "
                                  "practice owner who carries the risk.",
    "/industries/real-estate/": "AI training for real estate agencies and property "
                                "management. Sales and PM run separately, because "
                                "the work barely overlaps.",
    "/industries/accounting-bookkeeping/": "AI training for accounting and "
                                           "bookkeeping practices, with the "
                                           "client-data line settled first. Claude "
                                           "and ChatGPT, side by side.",
    "/training/": "The six foundation modules behind every industry track: useful "
                  "output, choosing your tool, long documents, reusable setups, the "
                  "boundary, and policy.",
    "/services/": "Four engagements: a team workshop, a done-with-you workflow "
                  "build, an AI policy and audit, or ongoing advisory. Which one "
                  "depends on what is in the way.",
    "/services/policy-and-audit/": "Find out what is already happening with AI in "
                                   "your business, then write a rule people follow. "
                                   "The first step where exposure is the real "
                                   "question.",
    "/assessment/": "Nine questions about how your business runs. Get training "
                    "modules ordered for your work, a reading on exposure, and one "
                    "place to start. No account.",
    "/who-this-is-for/": "Worried about your job, never used it, teaching yourself, "
                         "or the one who decides. Four starting points, and our "
                         "position on replacement stated plainly.",
    "/who-this-is-for/never-used-it/": "Never used Claude or ChatGPT? The mental "
                                       "model that helps, the one job to try first, "
                                       "and what to ignore entirely for now.",
    "/who-this-is-for/owners-and-managers/": "The three decisions only the owner can "
                                             "make, the AI business case that is not "
                                             "headcount, and what to measure three "
                                             "weeks later.",
    "/who-this-is-for/teaching-yourself/": "Already using AI at work unasked? The "
                                           "three gaps self-teaching leaves, and how "
                                           "to raise it without it becoming an "
                                           "incident.",
    "/contact/": "Tell us what your business does and which jobs cost you time. One "
                 "form, read and answered by a person. AI training for Australian "
                 "businesses.",
    "/guides/what-never-goes-in/": "The five categories that belong on every "
                                   "business's AI never list, how to write yours in "
                                   "twenty minutes, and how to de-identify properly.",
    "/guides/privacy-basics/": "What the Australian Privacy Principles mean when "
                               "staff paste client information into an AI tool, and "
                               "the four decisions that matter.",
    "/tools/prompt-builder/": "A free browser-based prompt builder. Five questions — "
                              "the job, the reader, the constraints, what good looks "
                              "like, what must never appear. Nothing is sent.",
    "/tools/claude/projects/": "How to set up a Claude Project holding your context, "
                               "examples and house rules, so nobody rebuilds the "
                               "prompt each time.",
    "/insights/": "Articles on using Claude and ChatGPT in real business work: where "
                  "the privacy line sits, what to teach first, and what stays with a "
                  "qualified person.",
    "/insights/which-tool-rule-of-thumb/": "A rule for choosing between Claude and "
                                           "ChatGPT by the shape of the job, "
                                           "including the third case where the "
                                           "answer is neither.",
    "/insights/the-report-that-keeps-the-contract/": "In cleaning, maintenance and "
                                                     "trades the tender wins the work "
                                                     "and the monthly report keeps "
                                                     "it. Both land on the owner, "
                                                     "after hours.",
    "/insights/free-tier-paid-tier-your-data/": "The account type matters more than "
                                                "the brand. What happens to text you "
                                                "paste differs between vendors and "
                                                "between tiers of the same vendor.",
    "/insights/training-that-didnt-stick/": "Most businesses that have done AI "
                                            "training have nothing to show for it. "
                                            "Four of the five reasons are decided "
                                            "before the session starts.",
    "/insights/first-ninety-minutes/": "Most AI training starts with prompts and "
                                       "loses the room. The sequence that works "
                                       "starts with where information goes, then one "
                                       "real job.",
    "/insights/pick-the-one-job/": "Fix one job properly before touching anything "
                                   "else. A test for choosing which, and why the most "
                                   "annoying job is usually the wrong answer.",
    "/insights/reusable-setups-relearning/": "A saved setup is the difference between "
                                             "a good afternoon of training and a "
                                             "change still there in March. What goes "
                                             "in one, and what keeps it alive.",
    "/insights/your-team-is-already-using-ai/": "Most Australian businesses have "
                                                "unreported AI use somewhere. How you "
                                                "ask about it decides whether you get "
                                                "the truth or a clean sheet.",
    "/insights/real-estate-sales-vs-pm/": "In an agency, sales and property "
                                          "management have almost no tasks in common. "
                                          "Training them together bores half the room "
                                          "for half the time.",
    "/insights/accounting-where-the-hours-are/": "The client-data objection is real "
                                                 "and aimed at the wrong target. Most "
                                                 "of the work eating a practice week "
                                                 "involves no client data at all.",
    "/insights/audit-readiness-is-the-lever/": "In NDIS, allied health and legal "
                                               "work, staff are usually already using "
                                               "AI unreported. The principal's real "
                                               "question is exposure.",
}

_TITLES = {
    "/industries/cleaning-maintenance/": "AI for cleaning and maintenance — AI at work",
    "/industries/trades/": "AI training for trades and field services — AI at work",
    "/insights/": "Blog — practical AI in Australian business — AI at work",
    "/who-this-is-for/": "Who AI training is for — four positions — AI at work",
    "/who-this-is-for/owners-and-managers/": "Deciding on AI for your team — AI at work",
}

for _route, _desc in _DESCRIPTIONS.items():
    METAS.setdefault(_route, {})["description"] = _desc
for _route, _title in _TITLES.items():
    METAS.setdefault(_route, {})["title"] = _title
