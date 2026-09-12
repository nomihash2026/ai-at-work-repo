"""Pages written here rather than salvaged, plus the engagement modules that
get injected into salvaged pages.

The enquiry form is the only conversion action on the site. Everything else —
the assessment, the guides, the resources, the blog — exists to make filling it
in an obvious next step, and ends by pointing at it.
"""

from data.site import SITE, INDUSTRIES

ORIGIN = SITE["origin"]


# --------------------------------------------------------------------- form --

TEAM_BANDS = ["Just me", "2–5 people", "6–15 people", "16–50 people", "More than 50"]
HELP_WITH = [
    "Not sure yet — that's fine",
    "Half-day team workshop",
    "Done-with-you workflow build",
    "AI policy and audit",
    "Ongoing advisory",
    "Something else",
]
CURRENT_USE = [
    "Nobody, as far as I know",
    "A few people, no written rule",
    "A few people, and we have a written rule",
    "Most of the team, no written rule",
    "Most of the team, and we have a written rule",
]


def _opts(values, first=""):
    out = f'<option value="">{first}</option>' if first else ""
    for v in values:
        out += f'<option value="{v}">{v}</option>'
    return out


def enquiry_form():
    industry_opts = '<option value="">Choose the closest one</option>' + "".join(
        f'<option value="{name}">{name}</option>' for _, name in INDUSTRIES
    ) + '<option value="Something else">Something else</option>'
    return f'''<form class="eform" name="enquiry" method="POST" action="{SITE['thanks']}" data-netlify="true" netlify-honeypot="bot-field">
<input type="hidden" name="form-name" value="enquiry">
<p class="pot"><label>Leave this empty <input name="bot-field" tabindex="-1" autocomplete="off"></label></p>
<div class="fld-2">
<div class="fld"><label for="q-name">Your name <span class="req">required</span></label>
<input id="q-name" name="name" type="text" autocomplete="name" required></div>
<div class="fld"><label for="q-business">Business name <span class="req">required</span></label>
<input id="q-business" name="business" type="text" autocomplete="organization" required></div>
</div>
<div class="fld-2">
<div class="fld"><label for="q-email">Email <span class="req">required</span></label>
<input id="q-email" name="email" type="email" autocomplete="email" inputmode="email" required></div>
<div class="fld"><label for="q-phone">Phone</label>
<input id="q-phone" name="phone" type="tel" autocomplete="tel" inputmode="tel">
<span class="hint">Only if you'd rather we called.</span></div>
</div>
<div class="fld-2">
<div class="fld"><label for="q-industry">What the business does</label>
<select id="q-industry" name="industry">{industry_opts}</select></div>
<div class="fld"><label for="q-team">How many people</label>
<select id="q-team" name="team_size">{_opts(TEAM_BANDS, "Choose a range")}</select></div>
</div>
<div class="fld"><label for="q-help">What you think you need</label>
<select id="q-help" name="help_with">{_opts(HELP_WITH, "Choose one")}</select>
<span class="hint">A guess is useful. Being wrong about it costs nothing — half the first call is working out which shape actually fits.</span></div>
<div class="fld"><label for="q-week">What's eating the week <span class="req">required</span></label>
<textarea id="q-week" name="whats_eating_the_week" required placeholder="One or two jobs that keep costing you time. The more specific, the more useful the first call is — &quot;the monthly report for four sites takes me a Sunday&quot; beats &quot;we want to be more efficient&quot;."></textarea>
<span class="hint">Please don't include client information, even as an example. We'll ask for redacted documents if and when they become relevant.</span></div>
<div class="fld"><label for="q-using">Is anyone using AI already</label>
<select id="q-using" name="current_use">{_opts(CURRENT_USE, "Choose one")}</select></div>
<div class="fld"><label for="q-plan">Your assessment summary</label>
<textarea id="q-plan" name="plan_summary" rows="4" placeholder="If you've run the assessment in this tab, your summary appears here automatically. Otherwise leave it blank."></textarea>
<p class="plan-note" id="plan-note">Your assessment summary has been carried across. Edit or clear it if you'd rather not send it.</p></div>
<div class="fld"><label for="q-heard">How you heard about us</label>
<input id="q-heard" name="heard_via" type="text"></div>
<button type="submit">Send enquiry</button>
<p class="legal">We use this to reply to you and to prepare a scope if you ask for one. We don't add you to a mailing list, we don't pass your details to anyone, and we don't put your enquiry into an AI tool. See the <a href="/privacy/">privacy policy</a>.</p>
</form>'''


CONTACT_JS = """
(function(){
  var ta = document.getElementById('q-plan');
  var note = document.getElementById('plan-note');
  if (!ta) return;
  try {
    var plan = sessionStorage.getItem('aiw_plan');
    if (plan && !ta.value){
      ta.value = plan;
      if (note) note.setAttribute('data-has','true');
    }
  } catch (e) { /* private browsing: the field just stays empty */ }
})();
"""

THANKS_JS = """
(function(){
  window.dataLayer = window.dataLayer || [];
  window.dataLayer.push({ event: 'enquiry_submitted', form_name: 'enquiry' });
})();
"""


# -------------------------------------------------------------------- pages --

def _contact(ask, illos):
    main = f'''<main id="main"><section class="phero"><div class="shell">
<p class="crumb"><a href="/">Home</a></p>
<h1>Start an enquiry</h1>
<p class="lede">One form, read by a person, answered by a person. Tell us what the business does and what's eating the week. If we're the wrong fit we'll say so, and we can usually point you somewhere better.</p>
<p class="stamp">We reply to everything, usually within one business day.</p>
</div></section>
<section class="sect" style="padding-top:0"><div class="shell"><div class="form-wrap">
<div>{enquiry_form()}</div>
<aside class="form-side">
<h3>What happens after you send it</h3>
<ol class="rows-foot" style="margin:0 0 1.4rem;padding-left:1.15rem;display:grid;gap:.5rem">
<li>A short reply confirming we've read it, with anything we need clarified.</li>
<li>A call of about twenty minutes to work out what the actual problem is, which is sometimes not the one in the form.</li>
<li>A written scope and a figure, before any commitment.</li>
<li>A date, or an honest no.</li>
</ol>
<h3>What we'll ask on the call</h3>
<ul>
<li>Which jobs are done by the person who also signs the cheque.</li>
<li>What's already being used, and whether anyone has written a rule about it.</li>
<li>What information is genuinely sensitive, and what only feels sensitive.</li>
<li>What would have to be true in three months for this to have been worth it.</li>
</ul>
<p>Nothing on that list needs preparing. It's the conversation, not a test.</p>
<div class="direct">
<h3>Or write to us directly</h3>
<p><a href="mailto:{SITE['email']}">{SITE['email']}</a> reaches the same person. The form is faster only because it asks the questions we'd otherwise have to email you for.</p>
</div>
</aside>
</div></div></section>
<section class="sect sect-lift"><div class="shell"><div class="prose">
<h2>Not ready to enquire</h2>
<p>Then don't. There are three things on this site worth reading before you talk to anyone, and none of them ask for an email address:</p>
<ul>
<li><a href="/guides/what-never-goes-in/">What never goes in an AI tool</a> — the list to hand a team before they start, not after something goes wrong.</li>
<li><a href="/tools/tiers-and-your-data/">Tiers and what happens to your data</a> — the five questions to ask about any tool, and why the answers differ between the free and paid versions of the same product.</li>
<li><a href="/assessment/">The assessment</a> — nine questions, about four minutes, and the full plan shows before anything is asked of you. If you run it in this tab, the summary travels into the form above.</li>
</ul>
<h2>Please don't send client information</h2>
<p>Not in an enquiry, and not as an example of the problem. Describe the shape of the document rather than pasting it. If we end up working together, we'll ask for redacted material at the point it actually matters, and we'll tell you what to redact.</p>
</div></div></section></main>'''
    return {
        "title": "Start an enquiry — AI at work",
        "description": "Tell us what your business does and which jobs are costing you "
                       "time. One form, read and answered by a person. AI training for "
                       "Australian businesses, Claude and ChatGPT taught side by side.",
        "main": main,
        "inline_js": CONTACT_JS,
        "cta": {
            "h": "The form is above, and it's the only one on the site",
            "p": "No sequences, no gated PDFs, no chatbot pretending to be a person. "
                 "One enquiry, one reply, and a straight answer about whether we can help.",
            "label": "Back to the form",
        },
        "schema": [{
            "@type": "ContactPage",
            "name": "Start an enquiry",
            "url": f"{ORIGIN}/contact/",
            "description": "Enquiry form for AI training engagements with Australian businesses.",
            "isPartOf": {"@id": f"{ORIGIN}/#website"},
            "about": {"@id": f"{ORIGIN}/#organization"},
        }],
    }


def _thanks(ask, illos):
    steps = illos.dg_steps([
        ("We've got it", "Your enquiry is in. Nothing else is needed from you right now."),
        ("A reply from a person", "Usually within one business day, with anything we need clarified."),
        ("A twenty-minute call", "To work out what the actual problem is, which is sometimes not the one in the form."),
        ("A scope and a figure", "In writing, before any commitment. Then a date, or an honest no."),
    ], caption="No sequence follows this. The next message you get is a reply to what you wrote.")
    main = f'''<main id="main"><section class="phero"><div class="shell ty">
<h1>Thanks — that's come through</h1>
<p class="lede">Your enquiry has been sent and is sitting with a person rather than a queue. Here's what happens from here.</p>
{steps}
</div></section>
<section class="sect" style="padding-top:0"><div class="shell"><div class="prose">
<h2>While you wait</h2>
<p>If you'd like to arrive at the call further along, these three are the ones that tend to change the conversation:</p>
<ul>
<li><a href="/guides/what-never-goes-in/">What never goes in an AI tool</a> — worth reading before the call, because the first thing we'll ask is what your team is already pasting into things.</li>
<li><a href="/resources/ai-policy-templates/">AI policy templates</a> — a starting point you can mark up. Turning up with an objection to a draft is more useful than turning up with a blank page.</li>
<li><a href="/assessment/">The assessment</a> — if you haven't run it, nine questions will tell you which engagement shape fits and in what order the modules should go.</li>
</ul>
<h2>Something to add</h2>
<p>Reply to the confirmation email, or write to <a href="mailto:{SITE['email']}">{SITE['email']}</a>. Please keep client information out of it — describe the shape of the document instead, and we'll tell you what to redact if it becomes relevant.</p>
</div></div></section></main>'''
    return {
        "title": "Thanks — your enquiry is in — AI at work",
        "description": "Your enquiry has been received. A reply from a person usually "
                       "follows within one business day.",
        "robots": "noindex,follow",
        "main": main,
        "no_cta": True,
        "inline_js": THANKS_JS,
    }


def _privacy(ask, illos):
    """Rewritten because the site now loads Google Tag Manager. The old page
    said there were no third-party scripts, which stopped being true the moment
    the container went on, and a privacy page that is quietly wrong is worse
    than no privacy page at all."""
    main = '''<main id="main"><section class="phero"><div class="shell">
<p class="crumb"><a href="/">Home</a></p>
<h1>Privacy policy</h1>
<p class="lede">Short, because we collect very little, and specific about the parts that involve someone else's code running on this page.</p>
<p class="stamp">Reviewed September 2026. This page names fast-moving vendor detail, so it carries a review date.</p>
</div></section>
<section class="sect" style="padding-top:0"><div class="shell"><div class="prose">
<h2>What we collect</h2>
<ul>
<li>What you type into the enquiry form: your name, business name, email, optionally a phone number, and what you tell us about the work.</li>
<li>The assessment summary, but only if it is in the form when you send it. You can edit or clear that field before submitting.</li>
<li>What you send us by email.</li>
<li>Aggregate analytics about page visits, described below.</li>
</ul>
<h2>The enquiry form</h2>
<p>The form posts to our own domain and the submission is stored by our host, Netlify, which emails it to us. It is not connected to an advertising platform and it does not create a marketing contact record anywhere. There is one hidden field on the form which exists to catch automated spam; it collects nothing about you.</p>
<h2>The assessment</h2>
<p>The assessment runs entirely in your browser. Your answers are not transmitted anywhere. If you choose to carry the plan into the enquiry form, the summary is held in your browser's session storage — the same tab, until you close it — and travels no further unless you submit the form yourself. Nothing about it appears in a URL.</p>
<h2>Analytics</h2>
<p>This site loads Google Tag Manager, which in turn loads Google Analytics. That gives us aggregate numbers: which pages get read, roughly where visitors are, which links get followed, and how many enquiries arrive. It sets cookies in your browser and Google processes that data on its own terms as well as ours.</p>
<p>What it is not doing: there are no advertising pixels, no remarketing audiences, no cross-site tracking and no third-party ad network on this site. If that changes, this section changes first. You can block it with any content blocker or by refusing cookies in your browser, and the site works identically without it.</p>
<h2>Fonts</h2>
<p>Typefaces load from Google Fonts, which means Google sees the request. That is the only other external request the site makes.</p>
<h2>Why we hold what we hold</h2>
<p>To reply to you, and to prepare a scope if you ask for one. Nothing else.</p>
<h2>What we don't do</h2>
<ul>
<li>Sell, rent or share your details with anyone for marketing.</li>
<li>Add you to a mailing list. There isn't one.</li>
<li>Put your enquiry into an AI tool. The irony would be considerable.</li>
</ul>
<h2>How long we keep it</h2>
<p>Enquiries are kept while there's an active conversation and for a reasonable period after, then deleted. Analytics data is retained on Google's default schedule.</p>
<h2>Access, correction and deletion</h2>
<p>Email <a href="mailto:hello@ai-at-work.au">hello@ai-at-work.au</a> and ask. We'll confirm what we hold, correct it, or delete it.</p>
<h2>Complaints</h2>
<p>If we've handled your information badly, tell us and we'll fix it. If you're not satisfied with our response, you can complain to the Office of the Australian Information Commissioner.</p>
<h2>Changes</h2>
<p>If this policy changes materially, the date on the page changes with it.</p>
</div></div></section></main>'''
    return {
        "title": "Privacy policy — AI at work",
        "description": "What we collect through the enquiry form, what the assessment "
                       "does and doesn't transmit, and exactly which third-party scripts "
                       "run on this site.",
        "main": main,
        "no_cta": True,
    }


def pages(ask, illos):
    return {
        "/contact/": _contact(ask, illos),
        "/thank-you/": _thanks(ask, illos),
        "/privacy/": _privacy(ask, illos),
    }
