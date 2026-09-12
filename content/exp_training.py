"""Depth for the training curriculum: the six foundation modules and the index.

Each module page answers the same four questions, because that's what a buyer
needs before committing a team's afternoon: what it covers, what someone can do
afterwards that they couldn't before, where it sits in the order, and where the
module stops.
"""

from content.helpers import sect


def _module(ask, illos, *, covers, after, order, stops, extra=""):
    body = (f"<h2>What this module covers</h2>{covers}"
            f"<h2>What someone can do afterwards</h2>{after}"
            f"<h2>Where it sits in the order</h2>{order}")
    return sect(body) + sect(f"<h2>Where this module stops</h2>{stops}{extra}", lift=True)


def _useful_output(ask, illos):
    return {
        "sections": [_module(
            ask, illos,
            covers="<p>The gap between text that looks finished and text you would "
                   "actually send. Most self-taught use gets stuck here: the output reads "
                   "plausibly, so people either send it and regret it, or rewrite it from "
                   "scratch and conclude the whole thing is a waste of time.</p>"
                   "<ul>"
                   "<li>Giving the tool the three or four facts it can't infer, rather "
                   "than a long instruction.</li>"
                   "<li>Showing it a good past example instead of describing the style "
                   "you want.</li>"
                   "<li>Saying what the document is for and who reads it — the single "
                   "change that most improves output.</li>"
                   "<li>Fixing a draft by naming what's wrong with it, rather than "
                   "starting again.</li>"
                   "<li>Recognising a confident wrong answer, which is the skill that "
                   "makes the rest of this safe.</li>"
                   "</ul>",
            after="<p>Takes a job they do regularly and gets a usable first draft in one "
                  "or two exchanges instead of five, and can tell you why the bad version "
                  "was bad. The second part matters more than the first: it's what "
                  "transfers to the next job and the next tool.</p>",
            order="<p>First, always. Every other module assumes it. A team that can't get "
                  "usable output has nothing to apply reusable setups to, and no basis for "
                  "judging which tool suits which job.</p>",
            stops="<p>This is not a prompt library. We hand out a short one because people "
                  "ask, and the <a href='/resources/prompt-library/'>starting library</a> "
                  "is deliberately brief — fifty prompts teach copying, a handful that "
                  "match your real jobs teach judgement. The module teaches the judgement "
                  "and leaves the copying alone.</p>",
            extra=ask("If you know which job you'd want the room practising on, that's the "
                      "session half planned."))],
        "faq": [
            ("Isn't prompting the whole skill?",
             "It's the smallest part. Knowing what to supply, what to show as an example, "
             "and how to tell a confident wrong answer from a right one is what separates "
             "someone getting value from someone getting plausible text."),
            ("Does this change when the models improve?",
             "The specifics get easier. The judgement doesn't: a better model still can't "
             "know the three facts only you hold, and still produces confident wrong "
             "answers occasionally."),
        ],
    }


def _choosing_your_tool(ask, illos):
    return {
        "sections": [_module(
            ask, illos,
            covers="<p>A rule of thumb for reaching for the right tool without thinking "
                   "about it, built around the shape of the job rather than this month's "
                   "feature list.</p>"
                   "<ul>"
                   "<li>Long, consequential, voice-sensitive work, where drift over a long "
                   "input is the defect that matters.</li>"
                   "<li>High-volume, fast-turnaround, spoken-in work, where friction is "
                   "the thing that kills adoption.</li>"
                   "<li>The third category: work that goes to neither, because a wrong "
                   "output is a regulated harm rather than an inconvenience.</li>"
                   "<li>Why stakes and length are two different axes, and what goes wrong "
                   "when a team treats them as one.</li>"
                   "</ul>"
                   + illos.svg_two_tools(),
            after="<p>Decides which tool to open without asking anyone, and can explain "
                  "the decision to a colleague in a sentence. Teams without this rule "
                  "default to whichever tool one confident person prefers, and the work "
                  "quietly reshapes itself around that tool's weak side.</p>",
            order="<p>Second or third. It needs the first module underneath it, because "
                  "comparing tools is meaningless if neither is producing usable output "
                  "yet.</p>",
            stops="<p>No benchmarks, no model version numbers, no feature tables. They "
                  "date within a quarter and they aren't how the decision actually gets "
                  "made. The longer argument is in "
                  "<a href='/insights/which-tool-rule-of-thumb/'>the rule of thumb</a>, "
                  "and the tool-by-tool detail sits under "
                  "<a href='/tools/'>tools</a>.</p>")],
        "faq": [
            ("Do we have to pay for both tools?",
             "Usually not at first. One paid plan plus a free account on the other covers "
             "most small teams, and which one you pay for depends on which side of the "
             "split your work sits."),
            ("You don't resell either one?",
             "No. No partner arrangement, no affiliate link, no referral fee in either "
             "direction, and where a free tier is genuinely sufficient we say so."),
        ],
    }


def _long_documents(ask, illos):
    return {
        "sections": [_module(
            ask, illos,
            covers="<p>Work where the input is long: a contract, a bundle of reports, a "
                   "tender pack, a year of meeting minutes. The failure mode here is "
                   "specific and easy to miss — a summary that's accurate for twelve pages "
                   "and subtly wrong for the last three.</p>"
                   "<ul>"
                   "<li>Summarising against your own checklist rather than accepting a "
                   "general summary.</li>"
                   "<li>Asking questions of a document instead of asking for its "
                   "contents.</li>"
                   "<li>Keeping the source open beside the output, and which parts always "
                   "get checked against it.</li>"
                   "<li>Comparing two versions of a document and getting the differences "
                   "that matter rather than every changed comma.</li>"
                   "<li>Working with scans and photographs of documents, and when that "
                   "goes wrong.</li>"
                   "</ul>",
            after="<p>Gets the three facts they needed out of a forty-page document in "
                  "minutes, with a defensible account of what was checked and what was "
                  "taken on trust.</p>",
            order="<p>Anywhere after the first module. It's the highest-value module for "
                  "legal, conveyancing, accounting and NDIS documentation work, and often "
                  "the reason those teams book at all.</p>",
            stops="<p>It does not make anyone a reader of contracts. Where the document "
                  "carries a regulated judgement — advice, a clinical decision, a tax "
                  "position, a sign-off — the judgement stays with the qualified person, "
                  "and no amount of careful summarising moves that line.</p>")],
    }


def _reusable_setups(ask, illos):
    return {
        "sections": [_module(
            ask, illos,
            covers="<p>The difference between a good afternoon and a change that's still "
                   "there in a month. A setup holds your context, your examples and your "
                   "house rules, so getting your format stops depending on whoever happens "
                   "to be typing.</p>"
                   "<ul>"
                   "<li>What belongs in a setup and what belongs in the individual "
                   "request.</li>"
                   "<li>Building one from a good past output rather than from a "
                   "description.</li>"
                   "<li>Sharing it across a team so quality doesn't depend on the "
                   "keenest person.</li>"
                   "<li>Writing down what to change when the template changes — the step "
                   "that stops a setup being stranded with the person who built it.</li>"
                   "<li>Where the checking step lives, and who owns it.</li>"
                   "</ul>"
                   + illos.svg_stack(),
            after="<p>Produces your monthly report, your standard letter or your tender "
                  "section from a handful of inputs, in your voice, without rebuilding the "
                  "instruction each time — and can fix the setup themselves when the format "
                  "moves.</p>",
            order="<p>Last of the practical modules, and the one that decides whether the "
                  "session was worth the afternoon. A workshop that ends here produces a "
                  "change you can point at three weeks later.</p>",
            stops="<p>It isn't automation. Nothing here connects systems together or runs "
                  "without a person; the output still gets read before it leaves. Teams "
                  "that want the pipeline version are usually better served by a "
                  "<a href='/services/workflow-build/'>workflow build</a> on one real "
                  "job.</p>")],
        "faq": [
            ("Who owns the setups afterwards?",
             "You do, in your own accounts. Nothing is held on our side and nothing stops "
             "working if you never speak to us again."),
            ("What happens when our template changes?",
             "One documented part of the setup changes. That's why the module includes "
             "writing that page down, and why you build the setup rather than us."),
        ],
    }


def _what_never_goes_in(ask, illos):
    return {
        "sections": [_module(
            ask, illos,
            covers="<p>The boundary, written in the terms of your own documents rather "
                   "than as generic categories. Generic lists get nodded at and ignored; a "
                   "list that names the actual file types people handle gets followed.</p>"
                   "<ul>"
                   "<li>Which account and which tier, named — the fact that matters more "
                   "than the brand.</li>"
                   "<li>What never goes in, using your documents as the examples.</li>"
                   "<li>What can go in once it's de-identified, and how to do that "
                   "properly rather than by deleting a name.</li>"
                   "<li>The reframe that resolves most objections: the majority of "
                   "time-sink work involves no client information at all.</li>"
                   "<li>What to do about the six months before there was a rule.</li>"
                   "</ul>"
                   + illos.svg_boundary(),
            after="<p>Knows, without asking, whether the thing in front of them can go "
                  "into a tool — and knows who to ask about the cases the rule doesn't "
                  "cover.</p>",
            order="<p>First, in any regulated setting. In allied health, legal, "
                  "conveyancing and NDIS work this module <em>is</em> the product, and "
                  "everything else is easier once it's settled.</p>",
            stops="<p>It is not legal advice and it doesn't certify compliance. Where your "
                  "obligations turn on professional rules we name what needs checking and "
                  "who should check it. Clinical privacy content should be reviewed by "
                  "someone qualified in your field, and we say so before the engagement "
                  "rather than during it. The free version of the content is on the "
                  "<a href='/guides/what-never-goes-in/'>never list guide</a>.</p>")],
        "faq": [
            ("Our information is confidential. Does that rule us out?",
             "Almost never. Most of the work costing your team time — tenders, policies, "
             "induction material, standard explanatory letters, reports from de-identified "
             "inputs — involves no client information at all. That reframe is usually where "
             "the conversation turns."),
            ("What if someone has already put client material in?",
             "You establish which account, roughly when and what kind of document, fix the "
             "setting, write the rule and move on. Handling it as misconduct guarantees you "
             "never hear about the next one."),
        ],
    }


def _team_ai_policy(ask, illos):
    checklist = illos.dg_checklist("A policy people actually follow answers four things", [
        "Which tool and which account, named rather than described",
        "What never goes in, in the terms of your own documents",
        "What gets checked before it leaves the building, and by whom",
        "Who to ask when something isn't covered — a name, not a process",
    ], caption="If it runs longer than about two pages, the part people remember is "
               "usually the first line.")
    return {
        "sections": [_module(
            ask, illos,
            covers="<p>Writing the rule, in the room, with the person who can approve it "
                   "present. Not a template to take away and adapt — a draft that exists "
                   "by the end of the session.</p>"
                   f"{checklist}"
                   "<p>We also cover the two failure modes: the one-line prohibition that "
                   "moves all the use onto personal phones, and the six-page generic policy "
                   "that doesn't name a single document the business actually produces.</p>",
            after="<p>The business has a written rule its staff can follow, and the "
                  "cautious half of the team — usually the most senior — knows where the "
                  "line is and stops treating the whole category as risky.</p>",
            order="<p>Before the practical modules in regulated work; after them "
                  "elsewhere. If the answer to \"is anyone using this already\" is unclear, "
                  "an <a href='/services/policy-and-audit/'>audit</a> comes before the "
                  "policy, because a rule built on a guess is a rule you can't enforce.</p>",
            stops="<p>We draft, you approve. We're not your lawyer and this isn't a "
                  "compliance sign-off; where your professional obligations are the "
                  "governing factor we'll tell you what needs a qualified review. Starting "
                  "drafts are free on the "
                  "<a href='/resources/ai-policy-templates/'>templates page</a> — mark one "
                  "up with your objections and the session goes faster.</p>")],
        "faq": [
            ("Can't we just use a template?",
             "You can, and the free ones on this site are a reasonable start. What a "
             "template can't do is name your documents, your tools and your approver, which "
             "is the part that makes a policy get followed rather than filed."),
            ("How often does it need revisiting?",
             "The structure holds. The vendor-specific answers move, which is why the "
             "policy names the tool and tier in one place rather than throughout."),
        ],
    }


def _training_index(ask, illos):
    return {
        "sections": [
            sect("<h2>Why one spine and thin industry tracks</h2>"
                 "<p>The jobs people need AI training for are roughly the same across "
                 "industries: drafting, summarising long documents, structuring messy "
                 "information, client communication, reusable setups, and knowing when not "
                 "to use it at all. What differs is which of those jobs dominates the week, "
                 "what the compliance line is, and what the documents are called.</p>"
                 "<p>So the curriculum is written once and applied to your work, rather "
                 "than rebuilt per industry with a noun swapped. Six foundation modules, "
                 "then an industry track on top.</p>"
                 + illos.svg_spine() +
                 "<p>The practical consequence: you're not paying for a course built for "
                 "someone else's industry, and you're not paying for a general course "
                 "either. The modules are the same; the examples on the table are "
                 "yours.</p>"),
            sect("<h2>The order matters more than the list</h2>"
                 "<p>Most AI training opens with prompt technique and loses the room. The "
                 "sequence that holds: where information goes, then one real job start to "
                 "finish, then the tool decision, then the setups you keep. We set out "
                 "<a href='/insights/first-ninety-minutes/'>the reasoning for that "
                 "order</a> in full.</p>"
                 "<p>In regulated work the order changes: the boundary and the written rule "
                 "come first, because training people to use a tool the business hasn't "
                 "sanctioned puts the risk on them. If you're not sure which order applies "
                 "to you, the <a href='/assessment/'>assessment</a> returns the modules "
                 "sequenced for your work in about four minutes.</p>"
                 + ask("Or skip the tool and tell us what's eating the week — we'll tell "
                       "you which module comes first."), lift=True),
        ],
        "faq": [
            ("How long does the whole curriculum take?",
             "A half day covers the foundations with hands-on time on one real job. The "
             "modules are not a fixed syllabus to get through — which ones matter, and in "
             "what order, depends on the work."),
            ("Can we do one module rather than all six?",
             "Yes, and for some businesses that's the right call. Long documents alone is "
             "a common starting point for legal and conveyancing teams; the never list "
             "alone is a common one for clinics."),
            ("Is this for staff or for owners?",
             "Both are in the room, and the owner needs to be there for the boundary "
             "block. Without the person who decides what's permitted, the team leaves "
             "without authority and nothing changes."),
        ],
    }


BUILDERS = {
    "/training/": _training_index,
    "/training/useful-output/": _useful_output,
    "/training/choosing-your-tool/": _choosing_your_tool,
    "/training/long-documents/": _long_documents,
    "/training/reusable-setups/": _reusable_setups,
    "/training/what-never-goes-in/": _what_never_goes_in,
    "/training/team-ai-policy/": _team_ai_policy,
}
