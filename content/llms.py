"""llms.txt — a curated index written for language models.

The sitemap is ordered by path and tells a crawler that seventy-one URLs exist.
That is the wrong shape for a model trying to answer a question about AI
training in an Australian business: it needs to know what this site is, what it
will and will not say, and which handful of pages actually answer the common
questions.

So this is curated rather than generated from the route list. Sections are in
the order a stranger needs them, every entry carries a one-line description of
what is on the page, and the descriptions are written for a reader who will
never click through — because most of the time, one won't.

Generated at build time from the page registry, so an entry pointing at a route
that no longer exists fails the link check rather than going stale quietly.
"""

from data.site import SITE

ORIGIN = SITE["origin"]

# The opening block. Everything here is stated elsewhere on the site; nothing
# is claimed that a page does not back up.
PREAMBLE = """\
> Practical AI training for Australian small and mid-sized businesses. Claude
> and ChatGPT taught side by side, tool-neutral, built around the admin and
> operational work that fills a week rather than a generic prompt list.

Based in Sydney, working across Australia. Training, workflow builds, AI policy
and audit for accounting practices, real estate agencies, allied health clinics,
legal and conveyancing practices, NDIS providers, trades and cleaning businesses.

Positions this site takes, stated plainly because they are the answers people
are usually looking for:

- The case for this training is capacity, not headcount. Work that is currently
  done late, badly or not at all gets done. It is not a case for having fewer
  people, and engagements framed that way are declined.
- Two tools are taught together, with no reseller or referral relationship to
  either vendor, because the durable skill is knowing which to reach for and
  what each does with your information.
- Some work should not go into a general-purpose AI tool at all. Where a wrong
  output is a regulated harm rather than an inconvenience — clinical decisions,
  financial advice, tax positions, safety sign-off — it stays with the qualified
  person, and the training says so.
- Where a written rule does not exist yet, the policy comes before the training.
  A team trained to move faster in a direction nobody has decided on is a worse
  position than an untrained one.
- Nothing on this site is gated. There are no prices, statistics, client names
  or testimonials published, because none could be stated accurately yet.
"""

SECTIONS = [
    ("Start here", [
        ("/", "What the business does and who it is for."),
        ("/who-this-is-for/",
         "Four positions people hold on AI at work — worried about their job, "
         "never used it, teaching themselves, or having to decide — and why a "
         "session has to answer all four."),
        ("/assessment/",
         "A nine-question planning tool that runs in the browser and returns "
         "training modules ordered for the business, a reading on exposure, and "
         "one recommended starting point. No account, nothing transmitted."),
        ("/tools/prompt-builder/",
         "A browser-based builder that assembles a structured AI instruction "
         "from five questions: who is writing, who reads it, the constraints, "
         "what good looks like, and what must never appear."),
        ("/contact/", "The only form on the site. Read and answered by a person."),
    ]),
    ("The four starting positions", [
        ("/who-this-is-for/worried-about-your-job/",
         "What AI training does and does not change about a job, who the trainer "
         "reports to, and the four things they will not do. Written for the "
         "person in the room who did not ask to be there."),
        ("/who-this-is-for/never-used-it/",
         "A first-principles start: the mental model that helps, one job to try "
         "this week, what good output looks like, and what to ignore entirely."),
        ("/who-this-is-for/teaching-yourself/",
         "For someone already using AI at work unprompted. The three gaps "
         "self-teaching leaves — the account tier and what it does with your "
         "material, reusable setups rather than clever prompts, and a "
         "defensible line — and how to raise it without it becoming an incident."),
        ("/who-this-is-for/owners-and-managers/",
         "The three decisions only the owner can make, the business case stated "
         "without pretending it is headcount, what to tell the team beforehand, "
         "and what to measure three weeks later."),
    ]),
    ("Privacy, policy and the boundary", [
        ("/guides/what-never-goes-in/",
         "The five categories that belong on every business's never list, how to "
         "write one in twenty minutes, and how to de-identify a document without "
         "losing the point of it."),
        ("/tools/tiers-and-your-data/",
         "Five questions to ask of any AI tool about what happens to your "
         "information, where each answer lives, and why the answers differ "
         "between the free and paid tiers of the same product."),
        ("/guides/privacy-basics/",
         "Privacy obligations for a small Australian business using AI tools, in "
         "plain terms."),
        ("/resources/ai-policy-templates/",
         "Templates for a one-page AI policy and a never list."),
        ("/services/policy-and-audit/",
         "The engagement that establishes what is already being used, writes the "
         "rule, and closes the gap. Comes before training where work is regulated."),
        ("/resources/vendor-checklist/",
         "What to ask a vendor before putting business information into their tool."),
    ]),
    ("Choosing and using the tools", [
        ("/tools/which-tool/",
         "Which of the two tools suits which job, including the jobs where the "
         "answer is neither."),
        ("/about/why-two-tools/",
         "Why both are taught together, and why there is no reseller relationship "
         "with either vendor."),
        ("/tools/claude/", "What Claude is better at, and where it is not."),
        ("/tools/chatgpt/", "What ChatGPT is better at, and where it is not."),
        ("/tools/claude/projects/",
         "What belongs in a reusable project setup and what you still type each "
         "time."),
        ("/tools/chatgpt/custom-setups/",
         "The same division, applied to a saved custom setup."),
        ("/tools/vendor-questions/",
         "The questions to put to an AI vendor, and what a non-answer means."),
    ]),
    ("The training itself", [
        ("/training/",
         "The full curriculum. One core skill set taught once, with a thin "
         "application layer per industry."),
        ("/training/useful-output/",
         "Why a first draft comes back generic and the four things to state "
         "instead, with the same prompt shown before and after."),
        ("/training/choosing-your-tool/", "Matching the job to the tool."),
        ("/training/long-documents/",
         "Interrogating a long document in four steps, including the one people "
         "skip that prevents the damage."),
        ("/training/reusable-setups/",
         "Turning a habit that lives in one person's head into something the "
         "business owns."),
        ("/training/what-never-goes-in/", "The boundary, taught as a module."),
        ("/training/team-ai-policy/", "Writing a team AI policy that gets followed."),
    ]),
    ("Industries", [
        ("/industries/", "How the industry tracks are built and what they share."),
        ("/industries/accounting-bookkeeping/",
         "AI training for accounting and bookkeeping practices, and where the "
         "hours in a practice week actually go."),
        ("/industries/real-estate/",
         "Real estate and property management, run as two separate problems."),
        ("/industries/allied-health/",
         "Allied health clinics, with the privacy line drawn before anything else."),
        ("/industries/legal-conveyancing/",
         "Legal support and conveyancing, where an audit comes before training."),
        ("/industries/ndis-providers/",
         "NDIS and disability providers, organised around where an auditor looks."),
        ("/industries/trades/",
         "Trades and field services: getting the quote out the same day."),
        ("/industries/cleaning-maintenance/",
         "Cleaning and property maintenance, where contracts are won on the "
         "submission."),
    ]),
    ("Engagements", [
        ("/services/", "How the four engagements differ and which suits what."),
        ("/services/team-workshop/",
         "A half-day with a team, working on their own documents."),
        ("/services/workflow-build/",
         "One workflow built with the business rather than handed to it."),
        ("/services/advisory/", "Ongoing advisory after the first engagement."),
        ("/services/what-it-costs/",
         "What drives the cost of an engagement and what changes it."),
        ("/case-studies/",
         "What engagements look like in practice. No client names are published."),
    ]),
    ("Writing", [
        ("/insights/", "The blog. The reasoning that would otherwise be given on a call."),
        ("/insights/your-team-is-already-using-ai/",
         "Why the question is not whether a team uses AI but whether anyone knows "
         "which account they are using."),
        ("/insights/free-tier-paid-tier-your-data/",
         "What differs between tiers, and why the default is the part people get "
         "wrong."),
        ("/insights/one-page-ai-policy/",
         "Why long AI policies fail and what a one-page version contains."),
        ("/insights/first-ninety-minutes/",
         "What the first ninety minutes with a team actually covers."),
        ("/insights/pick-the-one-job/",
         "How to choose the first job to fix, which is rarely the most irritating one."),
        ("/insights/training-that-didnt-stick/",
         "Why training stops being used three weeks later, and what prevents it."),
        ("/insights/reusable-setups-relearning/",
         "The difference between a folder of prompts and a setup the business owns."),
        ("/insights/which-tool-rule-of-thumb/",
         "A rule of thumb for choosing between the two tools."),
        ("/insights/accounting-where-the-hours-are/",
         "The client-data objection in accounting practices, and why most of the "
         "work it blocks involves no client data."),
        ("/insights/real-estate-sales-vs-pm/",
         "Why sales and property management should not share an AI session."),
        ("/insights/audit-readiness-is-the-lever/",
         "In regulated work, the question is exposure rather than whether AI helps."),
        ("/insights/the-report-that-keeps-the-contract/",
         "The reporting that decides whether a contract is renewed."),
    ]),
    ("About", [
        ("/about/", "Who runs the training and what work is declined."),
        ("/privacy/", "What this site collects, which is a Google Tag Manager container and nothing else."),
        ("/terms/", "Terms of use."),
    ]),
]


def build(pages, out_dir):
    """Write llms.txt, checking every entry against the live page registry so a
    link to a retired route breaks the build instead of shipping."""
    missing = [r for _, items in SECTIONS for r, _ in items if r not in pages]
    if missing:
        raise SystemExit("llms.txt points at routes that do not exist: "
                         + ", ".join(missing))

    lines = [f"# {SITE['name']}", "", PREAMBLE.rstrip(), ""]
    for name, items in SECTIONS:
        lines.append(f"## {name}")
        lines.append("")
        for route, desc in items:
            title = pages[route]["title"].split(" — ")[0]
            lines.append(f"- [{title}]({ORIGIN}{route}): {desc}")
        lines.append("")

    lines.append("## Optional")
    lines.append("")
    lines.append(f"- [Full URL list]({ORIGIN}/sitemap.xml): every route, for "
                 "completeness. The pages above are the ones worth reading.")
    lines.append("")
    covered = {r for _, items in SECTIONS for r, _ in items}
    rest = sorted(r for r in pages if r not in covered
                  and "noindex" not in (pages[r].get("robots") or ""))
    if rest:
        lines.append("Routes not listed above, mostly category listings and "
                     "second-level pages: " + ", ".join(ORIGIN + r for r in rest) + ".")
        lines.append("")

    open(f"{out_dir}/llms.txt", "w").write("\n".join(lines))
    return len(covered)
