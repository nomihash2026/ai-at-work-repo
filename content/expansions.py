"""Depth added to the salvaged pages.

Each entry appends sections inside <main>, after the copy that was already
there, and optionally contributes FAQPage schema. Written this way rather than
as full rewrites because the original copy is good and in the right voice — what
it lacked was the specific detail a buyer needs before they'll fill in a form:
what happens in the room, what they walk out with, what it does not cover, and
the answer to the objection they were about to raise.

Nothing here asserts a price, a CPD hour count, a client name or a statistic.
Where a number would be invented, the page says what moves it instead.
"""

from data.site import SITE
from content.helpers import sect as _sect, faq_section, faq_schema
from content import exp_training, exp_tools, exp_library, exp_more

ORIGIN = SITE["origin"]


# --------------------------------------------------------------- services ----

def _team_workshop(ask, illos):
    clock = illos.dg_clock("A half day, as it actually runs", [
        ("0:00", "Where information goes",
         "Which tool, which account, what never goes in, and what stays with a "
         "qualified person. Your documents as the examples, not generic categories. "
         "The owner or principal needs to be in the room for this part."),
        ("0:40", "One real job, all the way through",
         "A job chosen with you beforehand, done by several people in the room, taken "
         "from blank to something you would actually send."),
        ("1:30", "Break", "Genuinely needed. The next block is the hands-on one."),
        ("1:45", "Everyone does it themselves",
         "Same job, own hands, own laptop. This is where the confident half of the room "
         "discovers the habits they picked up are costing them quality."),
        ("2:30", "The tool decision",
         "The rule of thumb for which tool suits which shape of job, including the jobs "
         "that go to neither."),
        ("3:00", "Setups you keep",
         "Two or three saved setups built live: a project holding your context, a saved "
         "instruction that produces your format. This is the block that decides whether "
         "anything survives the week."),
        ("3:45", "What to do on Monday",
         "One job per person, named, with the owner deciding what gets checked before it "
         "leaves the building."),
    ], caption="Half a day is four blocks and a break. A two-hour session covers the "
               "first two and the last one, and skips the hands-on middle — which is "
               "why it changes less.")
    outcomes = illos.dg_beforeafter([
        ("The standard explanatory letter",
         "Written from scratch each time, or copied from an old one and half-edited.",
         "A saved setup produces your version from three or four facts, in your voice."),
        ("A long document you need the gist of",
         "Read in full by whoever has time, usually the most expensive person available.",
         "Summarised against your own checklist, with the source still open beside it "
         "for the parts that matter."),
        ("The monthly or quarterly report",
         "An evening, often a weekend, done by the owner.",
         "Structured draft in an hour, with the judgement still yours."),
        ("A new staff member's first week",
         "Shown by whoever is free, differently each time.",
         "The induction material exists, is current, and reads consistently."),
    ], caption="The four jobs that come up in nearly every room. Yours will differ in "
               "the details and that's the point of choosing the job beforehand.")
    return {
        "sections": [
            _sect(f"<h2>What the room looks like</h2>"
                  f"<p>Between four and about fifteen people, in your office or online, "
                  f"with laptops open and one job from your actual work on the table. Not "
                  f"a lecture with a slide deck — about two thirds of the time is people "
                  f"doing the work themselves while someone who knows the tools watches "
                  f"over their shoulder and corrects the habits.</p>"
                  f"{clock}"),
            _sect("<h2>What changes afterwards</h2>"
                  "<p>The test we hold ourselves to is not the feedback form at the end. "
                  "It's a question three weeks later: which job is now being done "
                  "differently, and by whom? One named job, done differently by more than "
                  "one person, is a successful session.</p>"
                  f"{outcomes}"
                  f"{ask('If you already know which job you would put on the table, you have done most of the preparation. Tell us what it is.')}", lift=True),
            _sect("<h2>Who should be in the room, and who shouldn't</h2>"
                  "<p><strong>Should be:</strong> the people who do the writing-heavy work "
                  "daily, and the person who decides what's permitted. If the second one "
                  "isn't there for the first forty minutes, everyone leaves without "
                  "authority and nothing changes.</p>"
                  "<p><strong>Probably shouldn't:</strong> the whole business, if the whole "
                  "business doesn't share the work. Sales and property management in an "
                  "agency, for instance, have tasks that barely overlap — two focused "
                  "sessions beat one general one, which is why the "
                  "<a href='/industries/real-estate/'>real estate track</a> is split that "
                  "way.</p>"
                  "<p><strong>What we won't do:</strong> teach anything that requires a "
                  "paid feature you haven't bought, or run the session before the privacy "
                  "line is settled. If your work is regulated and there's no written rule "
                  "yet, the <a href='/services/policy-and-audit/'>policy and audit</a> "
                  "engagement comes first — not as an upsell, but because training people "
                  "to use a tool you haven't sanctioned puts the risk on them.</p>"),
        ],
        "faq": [
            ("How many people is too many?",
             "Past about fifteen, the hands-on blocks stop working because nobody can be "
             "helped individually. Larger teams are better served by two sessions split "
             "by the work people actually do, rather than one bigger room."),
            ("Can you run it online?",
             "Yes, and for multi-site businesses it's often better. The hands-on blocks "
             "work as well remotely; the boundary conversation is slightly better in "
             "person because people ask the awkward questions out loud."),
            ("Do we need to prepare anything?",
             "One job, agreed with us beforehand, and de-identified examples of it. "
             "Nothing else. Please don't send client information — describe the document "
             "and we'll tell you what to redact."),
            ("What if half the team has never used these tools?",
             "That's the normal composition of the room, and the sequence is built for it. "
             "The first real win happens in the second block, before anyone has to learn "
             "any terminology."),
            ("Is a two-hour version available?",
             "Yes, and it's honest about what it drops: the hands-on middle block. It "
             "works as a starting point for a team that needs the boundary settled and one "
             "job demonstrated, and it's usually followed by a workflow build rather than "
             "a second workshop."),
        ],
    }


def _workflow_build(ask, illos):
    arc = illos.dg_steps([
        ("Pick the job", "One job, named, that you do at least monthly and currently do "
                         "yourself after hours. The tender. The monthly report. The "
                         "quote follow-up."),
        ("Watch you do it", "Screen shared, your real work, no tidying up beforehand. "
                            "The inefficiencies we're looking for are usually the "
                            "habits nobody mentions."),
        ("Build it with you", "Not for you. Your hands on the keyboard for most of it, "
                              "because a setup you didn't build is a setup you can't "
                              "adjust when the format changes."),
        ("Run it on the next one", "The real test is the next live instance of the job, "
                                   "not the one we practised on. We stay for that."),
    ], caption="Four steps, usually across two sessions with a week between them so the "
               "job comes around again naturally.")
    return {
        "sections": [
            _sect("<h2>How it differs from a workshop</h2>"
                  "<p>A workshop is a room of people learning method. A workflow build is "
                  "one job, constructed on real work, with the person who owns that job "
                  "sitting next to you. Different shape, different outcome, and the two "
                  "are not longer and shorter versions of each other.</p>"
                  "<p>This is the right engagement when there's one document that keeps "
                  "costing you an evening, and the wrong one when the problem is that "
                  "eight people are each doing something slightly unsafe.</p>"
                  f"{arc}"),
            _sect("<h2>What you own at the end</h2>"
                  "<ul>"
                  "<li>A working setup — a project or saved instruction holding your "
                  "context, your examples and your format — that produces the document "
                  "from your inputs.</li>"
                  "<li>A written page explaining how it works and what to change when the "
                  "template changes, so it isn't stranded with whoever was in the room.</li>"
                  "<li>The checking step, written down: what a person confirms before "
                  "anything leaves the building, and who that person is.</li>"
                  "<li>The transferable part, which is the method. The second job you "
                  "build yourself, and most clients do.</li>"
                  "</ul>"
                  f"{ask('If you can name the document, we can usually tell you on a first call whether this is a two-session build or something smaller.')}", lift=True),
            _sect("<h2>Jobs this works well on</h2>"
                  "<p>Long, templated, repetitive, and currently done by someone senior at "
                  "night. Tenders and capability statements. Monthly client reports. Scopes "
                  "of works. Site instructions for a casual workforce. Standard letters "
                  "that explain a process. Induction and policy documents that are "
                  "permanently out of date.</p>"
                  "<h3>Jobs it doesn't work on</h3>"
                  "<p>Anything where the output is a regulated judgement rather than a "
                  "document: clinical decisions, financial advice, tax positions as "
                  "distinct from tax admin, safety sign-off. We'll say so on the first "
                  "call rather than three sessions in.</p>"),
        ],
        "faq": [
            ("Do you build it for us or with us?",
             "With you, deliberately. A setup built for you breaks the first time your "
             "template changes and nobody knows which part to edit."),
            ("How long does it take?",
             "Usually two sessions a week or so apart, so the job comes around again "
             "naturally and we're there for the live run. Some jobs are one session."),
            ("What do you need from us?",
             "The job, a de-identified example of a good past output, and the person who "
             "actually does it. The last one is not optional."),
            ("Will this work if our template changes every year?",
             "That's the normal case, and it's why you build it rather than us. The "
             "written page covers what to change when the format moves."),
        ],
    }


def _policy_and_audit(ask, illos):
    split = illos.dg_split(
        {"head": "Fine, once the rule names it",
         "items": ["Tenders, capability statements and scopes of works",
                   "Policies, procedures and position descriptions",
                   "Induction and training material",
                   "Standard letters explaining a process, with no client in them",
                   "Reports written from de-identified inputs",
                   "Job ads, inductions and internal summaries"]},
        {"head": "Stays with a qualified person",
         "items": ["Clinical judgement and anything diagnostic",
                   "Financial advice",
                   "Tax positions, as distinct from tax admin",
                   "Safety sign-off",
                   "Anything needing expertise nobody in the room holds",
                   "Any output nobody will check before it leaves"]},
        caption="The line on the right doesn't move with the tool, the tier or the "
                "vendor. That's what makes the left side safe to teach quickly.")
    return {
        "sections": [
            _sect("<h2>What the audit actually establishes</h2>"
                  "<p>Four facts, and most businesses can't currently answer any of them "
                  "with confidence:</p>"
                  "<ol>"
                  "<li>Which tools and which accounts are in use right now — named, and "
                  "free versus paid, personal versus business.</li>"
                  "<li>What categories of information have gone into them. Not "
                  "\"was it confidential\", which produces a defensive no, but what the "
                  "documents were.</li>"
                  "<li>Whether any of it is recorded anywhere you could produce if someone "
                  "asked.</li>"
                  "<li>Who decides what's permitted when something new comes up. A name, "
                  "not a process.</li>"
                  "</ol>"
                  "<p>We ask about the work rather than the tool, which is the difference "
                  "between getting the truth and getting a clean sheet that means nothing. "
                  "There's more on how that conversation goes in "
                  "<a href='/insights/your-team-is-already-using-ai/'>this article</a>.</p>"),
            _sect("<h2>Where the line ends up</h2>"
                  f"{split}"
                  f"{ask('If the honest version of this conversation would go better with the questions coming from outside the business, that is exactly what this engagement is for.')}", lift=True),
            _sect("<h2>What you get, and what it is not</h2>"
                  "<p><strong>You get:</strong> a written picture of current use, a policy "
                  "short enough that people remember it without looking it up, the never "
                  "list written in your own documents' terms, and the checking step named "
                  "with an owner. Usually a page or two, not a manual.</p>"
                  "<p><strong>It is not legal advice</strong>, and it isn't a compliance "
                  "certification. Where your obligations turn on professional rules — a "
                  "practice standard, a court's practice note, a regulator's guidance — we "
                  "name what needs checking and who should check it, and we'll tell you "
                  "plainly when something needs a qualified review rather than ours. In "
                  "clinical settings the privacy content should be reviewed by someone "
                  "qualified in your field, and we'd rather say that up front than have you "
                  "discover it later.</p>"
                  "<p>Training after this is easier, faster and safer, which is why the "
                  "two are usually sequenced rather than bundled. See the "
                  "<a href='/services/team-workshop/'>team workshop</a> for what follows.</p>"),
        ],
        "faq": [
            ("Is a ban not simpler?",
             "Simpler to write, and it fails quietly. The use moves to personal phones, "
             "your visibility goes to zero, and the first you hear of it is when something "
             "has already gone out. A rule people can follow beats a rule that sounds "
             "strict."),
            ("What if we find something serious?",
             "You deal with the exposure rather than the person. Which account, roughly "
             "when, what kind of information — then the setting gets fixed, the rule gets "
             "written, and everyone moves on. Treating it as misconduct guarantees you "
             "never hear about the next one."),
            ("We already have a policy. Is this worth doing?",
             "Often yes, and it's faster. Most existing policies are either a one-line "
             "prohibition or a generic template that doesn't name a single document the "
             "business actually produces. Reviewing one is quicker than writing one."),
            ("Does the policy need updating as tools change?",
             "The structure doesn't. The vendor-specific answers do, which is why the "
             "policy names the tool and the account type in one place where it can be "
             "changed, rather than throughout."),
        ],
    }


def _advisory(ask, illos):
    return {
        "sections": [
            _sect("<h2>What ongoing actually means</h2>"
                  "<p>A standing line to someone who knows your setup, for the questions "
                  "that arrive after the training: a new tier has appeared and nobody knows "
                  "whether it changes the data answer, a staff member has built something "
                  "clever and you can't tell whether it's safe, a client has asked whether "
                  "you use AI and you'd like the answer to be steady.</p>"
                  "<p>Concretely, it tends to be: a monthly or quarterly check-in, review "
                  "of new setups before they spread, a look at the vendor answers when they "
                  "move, and a hand in onboarding new staff into the rule rather than around "
                  "it.</p>"),
            _sect("<h2>Who this suits</h2>"
                  "<ul>"
                  "<li>Businesses past the first engagement, where use is spreading and you "
                  "want it spreading deliberately.</li>"
                  "<li>Multi-site operations where one office's habits drift from another's.</li>"
                  "<li>Regulated settings where the answer to \"can we\" needs to be "
                  "consistent, and where an audit conversation could happen any quarter.</li>"
                  "<li>Businesses hiring quickly, where every new starter is a new person "
                  "deciding for themselves what's acceptable.</li>"
                  "</ul>"
                  "<h3>Who it doesn't suit</h3>"
                  "<p>Anyone who hasn't done the first piece of work yet. There's nothing to "
                  "advise on until there's a rule and at least one job running differently. "
                  "If that's where you are, start with the "
                  "<a href='/assessment/'>assessment</a> and it will tell you which "
                  "engagement comes first.</p>"
                  f"{ask('Not sure whether you need this or a one-off? Say what changed since the last session and we will tell you.')}", lift=True),
        ],
        "faq": [
            ("Is this a retainer?",
             "It's an ongoing arrangement with a defined rhythm rather than a block of "
             "hours to burn down. What moves the figure is how many sites, how regulated "
             "the work is and how fast you're hiring — the same things that move any "
             "engagement, set out on the "
             "<a href='/services/what-it-costs/'>scope and price</a> page."),
            ("Can we stop?",
             "Yes, with notice, and without losing anything. Every setup and document from "
             "the work is yours and doesn't depend on us continuing."),
            ("Do you monitor our accounts?",
             "No. We don't have access to your systems and don't want it. This is advisory "
             "on what you tell us and what we review with you."),
        ],
    }


# ------------------------------------------------------------------ wiring ----

BUILDERS = {
    "/services/team-workshop/": _team_workshop,
    "/services/workflow-build/": _workflow_build,
    "/services/policy-and-audit/": _policy_and_audit,
    "/services/advisory/": _advisory,
}
BUILDERS.update(exp_training.BUILDERS)
BUILDERS.update(exp_tools.BUILDERS)
BUILDERS.update(exp_library.BUILDERS)
BUILDERS.update(exp_more.BUILDERS)


def expand(pages, ask, illos):
    """Append sections inside <main> and attach any FAQ schema."""
    for route, builder in BUILDERS.items():
        if route not in pages:
            continue
        spec = builder(ask, illos)
        page = pages[route]
        for old, new in spec.get("replace", []):
            if old not in page["main"]:
                raise SystemExit(f"expansion for {route}: replacement text not found:\n  {old[:90]}")
            page["main"] = page["main"].replace(old, new, 1)
        added = "".join(spec.get("sections", []))
        if spec.get("faq"):
            added += faq_section(spec["faq"],
                                 spec.get("faq_heading",
                                          "The questions we get asked about this"))
            page["schema"].append(faq_schema(spec["faq"]))
        page["main"] = page["main"].replace("</main>", added + "</main>", 1)
    return pages
