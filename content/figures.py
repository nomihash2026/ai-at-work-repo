"""The five figures that replaced the screenshot slots.

Each of these was originally registered in data/media.py as a screenshot of a
vendor's interface. They are diagrams instead, for three reasons: inventing a
vendor's interface is not ours to do, nothing on this site is made up, and a
screenshot of a UI is stale the quarter after it is taken while a diagram of
what goes where is not.

Appended inside <main> on their route, after the expansion pass, in the same
position the image slot would have used — directly after the hero.
"""


def figures(illos):
    """route -> figure html. Built lazily so illos is injected, matching the
    pattern used by the expansion modules."""

    out = {}

    # ------------------------------------------------- a prompt, twice -------
    out["/training/useful-output/"] = illos.dg_prompt(
        [
            ("What almost everybody types first",
             "Write an email to a client about their overdue invoice.",
             "What comes back is a competent, generic chase letter that could "
             "have been sent by any business to any client. It is polite, it is "
             "slightly too formal, it invents a payment term you never agreed, "
             "and rewriting it takes longer than writing the email would have."),
            ("The same job with four sentences of context",
             "You are writing on behalf of a small bookkeeping practice in "
             "Australia.\n\n"
             "The job: a second reminder about an invoice that is three weeks "
             "overdue.\n\n"
             "The reader is a long-standing client who is usually prompt, so the "
             "tone is a check-in rather than a chase — assume something has gone "
             "astray rather than that they are avoiding it.\n\n"
             "Keep it under 120 words, no attachments referenced, and do not "
             "state a payment term or a consequence, because I have not decided "
             "on one yet. End by asking whether they would like it reissued.",
             "What comes back is close enough to send after one read. The "
             "difference between the two is not a trick or a magic word. It is "
             "four sentences that a first-morning assistant would have needed "
             "anyway."),
        ],
        caption="The whole skill, in one comparison. Who the reader is, what the "
                "constraint is, and what must not appear.")

    # ------------------------------------------ Claude Projects: what sits where
    out["/tools/claude/projects/"] = illos.dg_where(
        "What goes in the project, and what you still type each time",
        [
            ("Stated once, in the project", [
                "Who the business is and what it does, in three lines.",
                "House style: the words you use and the ones you never use.",
                "The standing boundary — what must never appear in an output.",
                "Reference documents: your templates, a good past example, the "
                "current fee schedule.",
                "The format you want back, if it is always the same.",
            ]),
            ("Typed fresh in each conversation", [
                "The specific job, in one or two sentences.",
                "Who this particular output is for.",
                "Anything unusual about this instance.",
                "The material for this job, if it is not already a reference file.",
            ]),
        ],
        caption="The test of a good setup is whether a new starter could produce "
                "an acceptable first draft using the right-hand column alone.")

    # ------------------------------------------- ChatGPT custom setups --------
    out["/tools/chatgpt/custom-setups/"] = illos.dg_where(
        "The same division, in a saved setup",
        [
            ("In the standing instructions", [
                "The role: who it is writing as, and for what kind of business.",
                "The reading level and the tone, described rather than named.",
                "A standing instruction to ask before assuming anything missing.",
                "The never list, written out in full rather than referred to.",
                "The default length and structure.",
            ]),
            ("In the conversation", [
                "This job, this reader, this deadline.",
                "The notes, the transcript or the draft you are working from.",
                "Any one-off constraint that does not apply to the next job.",
            ]),
        ],
        caption="A setup that has to be explained before it works is not a setup. "
                "Write the standing half so somebody else could use it cold.")

    # ------------------------------------------- long documents, four steps ---
    out["/training/long-documents/"] = illos.dg_steps(
        [
            ("Say what the document is",
             "One line of context before the question. A lease, a tender, a "
             "clinical guideline and a board paper are read differently, and the "
             "tool cannot tell which it is holding."),
            ("Ask a question, not for a summary",
             "A summary of a sixty-page document is a document you still have to "
             "read. Ask the thing you actually need to know, which is usually "
             "narrower and always more checkable."),
            ("Make it point at the source",
             "Ask for the clause, the section or the page behind every claim. "
             "This is the single habit that separates useful work from a "
             "confident invention, because it makes the answer verifiable in "
             "seconds."),
            ("Verify the two that matter",
             "Not all of it — that defeats the point. Check the two answers the "
             "decision actually rests on, against the section it cited. If the "
             "citation is wrong, stop trusting the rest of that session."),
        ],
        caption="The order matters more than the wording. Step three is the one "
                "people skip and the one that prevents the damage.")

    # ---------------------------------------------- tiers: what to check ------
    out["/tools/tiers-and-your-data/"] = illos.dg_figure(
        '<h3 class="wh-h">The five questions, and where the answer lives</h3>'
        '<div class="table-wrap"><table class="kv">'
        '<thead><tr><th scope="col">What you are asking</th>'
        '<th scope="col">Where to find the answer</th>'
        '<th scope="col">Why it changes the decision</th></tr></thead><tbody>'
        '<tr><th scope="row">Is this account personal or business?</th>'
        '<td>The billing or workspace screen, not the logo in the corner.</td>'
        '<td>It decides who controls the settings below, and whether anyone but '
        'the user can see or revoke them.</td></tr>'
        '<tr><th scope="row">Does what I type train the model?</th>'
        '<td>The data controls or privacy settings screen.</td>'
        '<td>The default is not the same on every tier of every product, which '
        'is the part most people get wrong.</td></tr>'
        '<tr><th scope="row">How long is it retained, and by whom?</th>'
        '<td>The vendor\'s published retention terms, not the marketing page.</td>'
        '<td>Deleting a conversation and deleting the record behind it are not '
        'always the same action.</td></tr>'
        '<tr><th scope="row">Where is it processed?</th>'
        '<td>The terms, or the enterprise documentation if there is one.</td>'
        '<td>It is the question your own obligations are most likely to have an '
        'opinion about.</td></tr>'
        '<tr><th scope="row">Can the business get the answers in writing?</th>'
        '<td>Ask. A vendor that will not put it in writing has answered.</td>'
        '<td>An instinct is not something you can hand an auditor.</td></tr>'
        '</tbody></table></div>',
        caption="Ask these of any tool, not just the two taught here. The answers "
                "differ between vendors and between tiers of the same product.",
        cls="fig-tiers")

    return out


def apply(pages, illos):
    """Insert each figure directly after the page hero, which is the same slot
    the image registry uses — one visual position per page, held everywhere."""
    for route, fig in figures(illos).items():
        page = pages.get(route)
        if not page:
            continue
        block = f'<section class="sect" style="padding-block:0"><div class="shell">{fig}</div></section>'
        main = page["main"]
        i = main.find("</section>")
        if i == -1:
            page["main"] = main.replace("</main>", block + "</main>", 1)
        else:
            i += len("</section>")
            page["main"] = main[:i] + block + main[i:]
