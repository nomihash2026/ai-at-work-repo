"""Depth for the tools section.

This is the fastest-moving content on the site, so it is written to be durable:
the shape of each tool's strengths, the questions to ask, and the reasoning —
not vendor terms, feature tables or version numbers, which would be wrong within
a quarter and would need re-checking before every engagement anyway.
"""

from content.helpers import sect

REVIEW = ("<p class='stamp'>Reviewed September 2026. This page describes how we teach "
          "these tools, not what either vendor's current terms say — those get confirmed "
          "at the start of every engagement.</p>")


def _tools_index(ask, illos):
    return {
        "sections": [
            sect("<h2>Tool-fluent, two tools deep</h2>"
                 "<p>Most of the market teaches one tool, which quietly makes the trainer "
                 "a sales channel for one vendor. We teach both, because the skill "
                 "transfers and the interface doesn't — and because the first question a "
                 "practice principal actually has is about where information goes, which "
                 "differs between vendors and between tiers of the same vendor.</p>"
                 + illos.svg_two_tools() +
                 "<p>The rough split: long documents, sustained voice-consistent drafting "
                 "and multi-step reasoning one way; high-volume fast turnaround, "
                 "voice-note-to-draft and photo tasks the other. Plus the third category, "
                 "where the answer is neither.</p>"),
            sect("<h2>What we don't have</h2>"
                 "<p>No reseller agreement, no partner status, no affiliate links and no "
                 "referral fee with either vendor. Where the free tier is genuinely "
                 "sufficient for the work, we say so and you keep the money.</p>"
                 "<p>That's not a virtue signal — it's the only reason the recommendation "
                 "is worth anything. A trainer paid on one vendor's seats will always find "
                 "that vendor suitable.</p>"
                 + ask("Want the split applied to your own jobs rather than in the "
                       "abstract? That's the first twenty minutes of a call."), lift=True),
        ],
        "faq": [
            ("Should we standardise on one tool?",
             "Simpler to administer, and the cost is that your work reshapes itself around "
             "that tool's weak side while staff quietly use the other one on their phones. "
             "One paid plan plus a free account on the other is a common middle ground."),
            ("What if a third tool takes over?",
             "The rule we teach is about the shape of the job, so it survives. The "
             "vendor-specific detail is deliberately quarantined to one page — this "
             "section — so it can be updated without the curriculum changing."),
        ],
    }


def _claude(ask, illos):
    return {
        "sections": [
            sect("<h2>What it's genuinely better at</h2>"
                 "<ul>"
                 "<li><strong>Long inputs held consistently.</strong> A bundle of reports "
                 "or a forty-page contract summarised without the quality tailing off in "
                 "the last third.</li>"
                 "<li><strong>Sustained voice.</strong> A document that has to sound like "
                 "your firm all the way through, not just in the opening paragraph.</li>"
                 "<li><strong>Multi-step reasoning</strong> where the working needs to be "
                 "visible, so you can check the path rather than just the answer.</li>"
                 "<li><strong>Reusable setups</strong> that hold your context and examples "
                 "for a whole team — covered under "
                 "<a href='/tools/claude/projects/'>Projects</a>.</li>"
                 "</ul>" + REVIEW),
            sect("<h2>Where it's the wrong reach</h2>"
                 "<p>Thirty short, near-identical follow-ups where speed of entry is the "
                 "whole game. Talking to it from a van between jobs. Anything where the "
                 "input is a photo of a handwritten note. Those belong on the "
                 "<a href='/tools/chatgpt/'>other side of the split</a>.</p>"
                 + ask("If most of your week is long documents, that's usually the "
                       "starting module. Tell us what they are."), lift=True),
        ],
    }


def _claude_long_docs(ask, illos):
    return {
        "sections": [
            sect("<h2>How we teach it</h2>"
                 "<ol>"
                 "<li><strong>Bring your own checklist.</strong> A general summary is "
                 "worth little; a summary against the eight things you always need to know "
                 "is worth an hour. Most teams already have that list in their heads.</li>"
                 "<li><strong>Ask questions of the document</strong> rather than asking "
                 "for its contents. \"Does this lease allow subletting, and where does it "
                 "say so\" beats \"summarise this lease\".</li>"
                 "<li><strong>Keep the source open.</strong> The output points at the "
                 "document; the document is still the authority. Which parts always get "
                 "verified is a decision the business makes once, not per document.</li>"
                 "<li><strong>Compare versions</strong> so you get the differences that "
                 "matter rather than every changed comma.</li>"
                 "</ol>"),
            sect("<h2>The failure mode worth naming</h2>"
                 "<p>A summary that is accurate for most of a long document and subtly "
                 "wrong about one clause is more dangerous than no summary, because it "
                 "reads as complete. The habit that prevents it is asking for the location "
                 "of each claim, not just the claim — then the check takes seconds and is "
                 "actually done.</p>"
                 "<p>This is the module that legal, conveyancing, accounting and NDIS "
                 "documentation teams get the most out of, and it's covered in the "
                 "curriculum under "
                 "<a href='/training/long-documents/'>working with long documents</a>.</p>"
                 + ask("If there's one document type that eats your week, a workflow "
                       "build can be pointed straight at it."), lift=True),
        ],
    }


def _claude_projects(ask, illos):
    return {
        "sections": [
            sect("<h2>What goes in a Project, and what doesn't</h2>"
                 "<p><strong>In:</strong> the context that's true every time — your house "
                 "style, two or three good past outputs as examples, the structure your "
                 "documents follow, the things you never say, and the checking step.</p>"
                 "<p><strong>Not in:</strong> anything specific to one instance of the job, "
                 "and anything from your never list. A Project is shared and durable, which "
                 "makes it exactly the wrong place for client material.</p>"
                 + illos.svg_stack()),
            sect("<h2>Why this is the block that makes training stick</h2>"
                 "<p>A session that teaches method produces a good afternoon. A session "
                 "that ends with two or three setups built on your real documents produces "
                 "a change that's still there next month, because the effort of getting a "
                 "good result has dropped to nearly zero for at least one job.</p>"
                 "<p>The part teams skip: writing down what to change when the template "
                 "changes. Without that page, the setup is stranded with whoever built "
                 "it.</p>"
                 + ask("A workflow build ends with exactly this, on one job, with your "
                       "hands on the keyboard."), lift=True),
        ],
        "faq": [
            ("Does everyone need a paid plan for this?",
             "Shared setups are a paid-tier feature at the time of writing, and it's one of "
             "the few places we'd say the paid plan earns its money for a team. We confirm "
             "the current position at the start of an engagement rather than quoting it "
             "here."),
        ],
    }


def _chatgpt(ask, illos):
    return {
        "sections": [
            sect("<h2>What it's genuinely better at</h2>"
                 "<ul>"
                 "<li><strong>Volume and speed.</strong> Twenty follow-ups that each need "
                 "to differ slightly, done in the time it takes to write two by hand.</li>"
                 "<li><strong>Talking instead of typing.</strong> A voice note from the "
                 "van becomes a quote email before the next job — the single highest-value "
                 "use in trade and field businesses.</li>"
                 "<li><strong>Photos of things.</strong> A handwritten site note, a "
                 "whiteboard, a form someone filled in by hand.</li>"
                 "<li><strong>Saved instructions</strong> for the jobs one person repeats "
                 "constantly.</li>"
                 "</ul>" + REVIEW),
            sect("<h2>Where it's the wrong reach</h2>"
                 "<p>A long bundle that has to be held consistently end to end, and any "
                 "document where the voice has to stay steady across several pages. Those "
                 "belong on the <a href='/tools/claude/'>other side</a>.</p>"
                 "<p>The trap we see most often: a team that started here, got good "
                 "results on short work, and then assumed the same approach would hold for "
                 "a tender. It doesn't, and the failure is quiet.</p>"
                 + ask("If your week is mostly fast turnaround, the training looks "
                       "different. Tell us what the volume is."), lift=True),
        ],
    }


def _chatgpt_voice(ask, illos):
    return {
        "sections": [
            sect("<h2>Why this one changes field businesses</h2>"
                 "<p>The bottleneck in a trade or field business is rarely the work. It's "
                 "the writing that has to happen after the work: the quote, the follow-up, "
                 "the defect note, the variation email. All of it lands on the person who "
                 "was on site, at the end of a day when they have nothing left.</p>"
                 "<p>Talking for ninety seconds and getting a structured draft removes "
                 "that step rather than speeding it up. Same-day quoting is a commercial "
                 "advantage in most trades, and this is the mechanism.</p>"),
            sect("<h2>How we teach it</h2>"
                 "<ol>"
                 "<li>Say the facts in any order — the tool handles the ordering, which is "
                 "the part people don't believe until they see it.</li>"
                 "<li>One saved setup per document type, so the format is consistent "
                 "whoever dictated it.</li>"
                 "<li>The check step: read it before it sends, always, because a confident "
                 "wrong price is worse than a slow right one.</li>"
                 "<li>What not to dictate — client details, site security information, "
                 "anything on your never list.</li>"
                 "</ol>"
                 + ask("This is usually a workflow build rather than a workshop. One job, "
                       "on your real work, in two sessions."), lift=True),
        ],
    }


def _chatgpt_custom(ask, illos):
    return {
        "sections": [
            sect("<h2>Saved instructions, in practice</h2>"
                 "<p>The same principle as a Project on the other side: put the context "
                 "that's true every time in one place, so nobody rebuilds it. The "
                 "difference is scope — saved instructions tend to suit one person's "
                 "repeated job, where a shared setup suits a team's standard document.</p>"
                 "<p>What belongs in there: your format, your tone, the things you never "
                 "say, and the output length you actually want. What doesn't: anything from "
                 "your never list, and anything true only this week.</p>"),
            sect("<h2>The version-drift problem</h2>"
                 "<p>Saved setups on individual accounts drift. Three people end up with "
                 "three formats, and nobody notices until a client gets two documents that "
                 "don't match. The fix is boring and effective: one owner per document "
                 "type, and the setup written down somewhere outside the tool.</p>"
                 + ask("If your team has quietly grown three versions of the same "
                       "document, that's a good first job to fix."), lift=True),
        ],
    }


def _which_tool(ask, illos):
    return {
        "sections": [
            sect("<h2>The four questions that settle it</h2>"
                 "<ol>"
                 "<li>How long is the input — a paragraph, or a bundle?</li>"
                 "<li>How many times will I do this today — once, or thirty?</li>"
                 "<li>Does it have to sound like us, sustained, all the way through?</li>"
                 "<li>If this output were wrong and nobody caught it, what's the worst "
                 "outcome?</li>"
                 "</ol>"
                 "<p>The fourth is the one people skip and the one that matters. If the "
                 "honest answer involves a regulator, a patient, a court or a roof, the job "
                 "is in the third category and the tool choice is irrelevant.</p>"
                 + illos.svg_two_tools()),
            sect("<h2>Two mistakes to avoid</h2>"
                 "<p><strong>Treating long as important.</strong> A two-line email to your "
                 "largest client is high-stakes and short. Stakes decide how carefully you "
                 "check; length decides which tool you open. Two different axes, and "
                 "conflating them is why some teams over-engineer short work and "
                 "under-check long work.</p>"
                 "<p><strong>Using the third category as an excuse.</strong> \"Our work is "
                 "regulated so none of this applies\" is an expensive sentence. The "
                 "regulated judgement stays with the qualified person. The tender, the "
                 "induction pack, the standard explanatory letter and the monthly report do "
                 "not — and that's where the hours are.</p>"
                 + ask("Twenty minutes on a call usually sorts your jobs by shape and "
                       "ends the internal argument."), lift=True),
        ],
        "faq": [
            ("Does this change with every model release?",
             "The shapes don't. Specific strengths shift, which is why the rule is about "
             "input length, volume and consequence rather than benchmarks."),
            ("What if we only want to use one tool?",
             "Then learn which jobs sit on its weak side, and check those outputs harder. "
             "That's a reasonable position, as long as it's a decision rather than an "
             "accident."),
        ],
    }


def _tiers(ask, illos):
    return {
        "sections": [
            sect("<h2>Why this page names no vendor terms</h2>"
                 "<p>Because they would be wrong within a quarter, and a privacy answer "
                 "that's stale is worse than no answer. What's durable is the five "
                 "questions; the current answers get confirmed at the start of every "
                 "engagement, for the tier you're actually on.</p>"
                 "<ol>"
                 "<li>Is what I type used to train the model?</li>"
                 "<li>How long is it retained, and where?</li>"
                 "<li>Who inside the vendor can see it, and in what circumstances?</li>"
                 "<li>Where is it processed?</li>"
                 "<li>Can an administrator turn any of this off — and would you know if "
                 "someone turned it back on?</li>"
                 "</ol>"
                 "<p>The fifth separates a business account from a personal one. A setting "
                 "any user can change is not a control.</p>" + REVIEW),
            sect("<h2>Why the free tier is where risk collects</h2>"
                 "<p>Not because free tiers are careless, but because of who uses them and "
                 "for what. A free account is a personal account: personal email, often a "
                 "personal phone, no administrator, no record, and nothing happens to it "
                 "when someone changes roles or leaves.</p>"
                 "<p>That's the real exposure — not that a vendor does something sinister "
                 "with a paragraph of a client letter, but that you have no visibility, no "
                 "control and no record, for work done on your behalf. The longer version "
                 "is in "
                 "<a href='/insights/free-tier-paid-tier-your-data/'>free tier, paid "
                 "tier</a>.</p>"
                 + ask("If you don't currently know which accounts your team is on, that's "
                       "the first thing an audit establishes."), lift=True),
        ],
        "faq": [
            ("Is the paid tier safe for client information?",
             "Safer is not the same as safe. The tier changes what the vendor does with "
             "your text; it doesn't change your obligations to the client, your "
             "professional body, or the person whose information it is."),
            ("Can we use the free tier for non-sensitive work?",
             "Often yes, and we'll say so when it's true. The risk isn't the free tier "
             "itself — it's that the line between sensitive and non-sensitive work gets "
             "blurry at 6pm on a deadline."),
            ("How current is this page?",
             "It carries a review date, and deliberately doesn't reproduce vendor terms. "
             "Treat it as the questions to ask, not the answers."),
        ],
    }


def _vendor_questions(ask, illos):
    return {
        "sections": [
            sect("<h2>Beyond the two we teach</h2>"
                 "<p>Every month brings another AI product aimed at your industry, usually "
                 "a wrapper around one of the big models with your sector's vocabulary on "
                 "the front. Some are genuinely useful. The questions that separate them:</p>"
                 "<ul>"
                 "<li><strong>Whose model is underneath, and does the answer change?</strong> "
                 "If a vendor won't say, your data answer is unknowable.</li>"
                 "<li><strong>What happens to our content</strong> — the same five "
                 "questions as any tier, applied to the wrapper and to the model "
                 "underneath.</li>"
                 "<li><strong>Where does it sit when you stop paying?</strong> Setups, "
                 "templates and history — exportable, or stranded?</li>"
                 "<li><strong>What does it do that a general tool plus a good setup "
                 "doesn't?</strong> Sometimes a real answer. Often the answer is a nicer "
                 "interface for something you could build in an afternoon.</li>"
                 "<li><strong>Who is accountable for a wrong output</strong> in a regulated "
                 "context? Read that clause before the pricing.</li>"
                 "</ul>"),
            sect("<h2>The industry-specific wrapper question</h2>"
                 "<p>A tool built for your profession can be worth paying for when it "
                 "carries genuine domain structure — the forms, the codes, the report "
                 "formats a regulator expects. It's worth less when the domain knowledge is "
                 "a prompt you could write yourself, and you're paying a subscription for "
                 "vocabulary.</p>"
                 "<p>The test we suggest: ask what it does that you couldn't reproduce in a "
                 "setup in an hour. A confident, specific answer is a good sign. A vague one "
                 "is the answer.</p>"
                 "<p>There's a free "
                 "<a href='/resources/vendor-checklist/'>vendor checklist</a> you can take "
                 "into the call — no email required.</p>"
                 + ask("Assessing a specific tool right now? Advisory conversations often "
                       "start exactly here."), lift=True),
        ],
    }


BUILDERS = {
    "/tools/": _tools_index,
    "/tools/claude/": _claude,
    "/tools/claude/long-documents/": _claude_long_docs,
    "/tools/claude/projects/": _claude_projects,
    "/tools/chatgpt/": _chatgpt,
    "/tools/chatgpt/voice-to-draft/": _chatgpt_voice,
    "/tools/chatgpt/custom-setups/": _chatgpt_custom,
    "/tools/which-tool/": _which_tool,
    "/tools/tiers-and-your-data/": _tiers,
    "/tools/vendor-questions/": _vendor_questions,
}
