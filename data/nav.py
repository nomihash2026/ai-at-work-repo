"""Mega menu and footer structure.

The menu is the interactive path, the footer is the crawlable one; anything that
matters appears in both. Keep them in step.

An item is (href, label) for a real link, or (None, label) for an in-development
vertical rendered as plain text.
"""

MEGA = [
    {
        "id": "who",
        "label": "Who it's for",
        "lead_h": "Four people are in the room",
        "lead_p": "Someone worried about their job, someone who has never opened "
                  "one, someone teaching themselves, and someone who has to decide "
                  "for all three.",
        "lead_href": "/who-this-is-for/",
        "lead_cta": "All four, and our position",
        "groups": [
            ("Where you're starting from", [
                ("/who-this-is-for/worried-about-your-job/", "Worried about your job"),
                ("/who-this-is-for/never-used-it/", "Never used it"),
                ("/who-this-is-for/teaching-yourself/", "Teaching yourself"),
                ("/who-this-is-for/owners-and-managers/", "Owners &amp; managers"),
            ]),
            ("Free, no account", [
                ("/assessment/", "Build your training plan"),
                ("/tools/prompt-builder/", "Prompt builder"),
            ]),
            ("Before you talk to anyone", [
                ("/guides/what-never-goes-in/", "What never goes in"),
                ("/tools/tiers-and-your-data/", "Tiers and your data"),
                ("/services/what-it-costs/", "What it costs"),
            ]),
        ],
    },
    {
        "id": "training",
        "label": "Training",
        "lead_h": "One core skill set, then your industry on top",
        "lead_p": "Everyone learns the same foundations. The industry track applies "
                  "them to the work that actually fills your week.",
        "lead_href": "/training/",
        "lead_cta": "See the full curriculum",
        "groups": [
            ("Foundations", [
                ("/training/useful-output/", "Getting output you can actually use"),
                ("/training/choosing-your-tool/", "Choosing your tool for the job"),
                ("/training/long-documents/", "Working with long documents"),
                ("/training/reusable-setups/", "Building reusable setups"),
                ("/training/what-never-goes-in/", "What never goes in"),
                ("/training/team-ai-policy/", "Writing your team's AI policy"),
            ]),
            ("Industry tracks", [
                ("/industries/accounting-bookkeeping/", "Accounting &amp; bookkeeping"),
                ("/industries/real-estate/", "Real estate &amp; property management"),
                ("/industries/allied-health/", "Allied health clinics"),
                ("/industries/legal-conveyancing/", "Legal support &amp; conveyancing"),
                ("/industries/ndis-providers/", "NDIS &amp; disability providers"),
                ("/industries/trades/", "Trades &amp; field services"),
                ("/industries/cleaning-maintenance/", "Cleaning &amp; property maintenance"),
            ]),
            ("How it's delivered", [
                ("/services/team-workshop/", "Team workshop"),
                ("/services/workflow-build/", "Done-with-you workflow build"),
                ("/services/policy-and-audit/", "AI policy &amp; audit"),
                ("/services/advisory/", "Ongoing advisory"),
            ]),
        ],
    },
    {
        "id": "industries",
        "label": "Industries",
        "lead_h": "Written for how your work actually runs",
        "lead_p": "Not a generic course with your industry's name swapped in. Each "
                  "track names the tasks, the time sinks and the line you can't cross.",
        "lead_href": "/industries/",
        "lead_cta": "All industries",
        "groups": [
            ("Finance &amp; compliance", [
                ("/industries/accounting-bookkeeping/", "Accounting &amp; bookkeeping"),
                (None, "Mortgage and insurance broking"),
                (None, "Payroll bureaux"),
                (None, "Financial planning administration"),
            ]),
            ("Property &amp; construction", [
                ("/industries/real-estate/", "Real estate &amp; property management"),
                (None, "Residential builders"),
                (None, "Strata management"),
                (None, "Building design and drafting"),
            ]),
            ("Health &amp; care", [
                ("/industries/allied-health/", "Allied health clinics"),
                ("/industries/ndis-providers/", "NDIS &amp; disability providers"),
                (None, "Dental practices"),
                (None, "Veterinary clinics"),
                (None, "Aged care providers"),
            ]),
            ("Legal &amp; professional services", [
                ("/industries/legal-conveyancing/", "Legal support &amp; conveyancing"),
                (None, "Migration agents"),
                (None, "Accountancy-adjacent advisory"),
                (None, "Patent and trade mark administration"),
            ]),
            ("Trades &amp; field services", [
                ("/industries/trades/", "Trades &amp; field services"),
                ("/industries/cleaning-maintenance/", "Cleaning &amp; property maintenance"),
                (None, "Landscaping and grounds"),
                (None, "Pest control"),
                (None, "Security and fire services"),
            ]),
        ],
    },
    {
        "id": "tools",
        "label": "Tools",
        "lead_h": "Two tools, taught side by side",
        "lead_p": "We don't sell either one. Where your information goes differs "
                  "between vendors and between tiers, and that is the first thing we cover.",
        "lead_href": "/tools/",
        "lead_cta": "How we teach both",
        "groups": [
            ("Claude", [
                ("/tools/claude/", "What Claude is better at"),
                ("/tools/claude/long-documents/", "Long documents and bundles"),
                ("/tools/claude/projects/", "Projects as reusable setups"),
            ]),
            ("ChatGPT", [
                ("/tools/chatgpt/", "What ChatGPT is better at"),
                ("/tools/chatgpt/voice-to-draft/", "Voice note to finished draft"),
                ("/tools/chatgpt/custom-setups/", "Custom setups and saved instructions"),
            ]),
            ("Free tools", [
                ("/tools/prompt-builder/", "Prompt builder"),
                ("/assessment/", "Build your training plan"),
            ]),
            ("Choosing and checking", [
                ("/tools/which-tool/", "Which tool for which job"),
                ("/tools/tiers-and-your-data/", "Tiers and what happens to your data"),
                ("/tools/vendor-questions/", "Questions to ask any AI vendor"),
            ]),
        ],
    },
    {
        "id": "services",
        "label": "Services",
        "lead_h": "Four shapes, depending on what's in the way",
        "lead_p": "Some businesses need a room and half a day. Some need the rule "
                  "written down before anyone learns anything. The assessment tells you which.",
        "lead_href": "/services/",
        "lead_cta": "How engagements work",
        "groups": [
            ("Engagements", [
                ("/services/team-workshop/", "Team workshop"),
                ("/services/workflow-build/", "Done-with-you workflow build"),
                ("/services/policy-and-audit/", "AI policy &amp; audit"),
                ("/services/advisory/", "Ongoing advisory"),
            ]),
            ("Before you commit", [
                ("/assessment/", "Build your training plan"),
                ("/services/what-it-costs/", "How we scope and price"),
                ("/case-studies/", "What engagements look like"),
            ]),
            ("Free resources", [
                ("/resources/ai-policy-templates/", "AI policy templates"),
                ("/resources/prompt-library/", "Starting prompt library"),
                ("/tools/prompt-builder/", "Prompt builder"),
                ("/resources/vendor-checklist/", "Vendor checklist"),
            ]),
        ],
    },
    {
        "id": "learn",
        "label": "Learn",
        "lead_h": "The parts we'd rather you read for free",
        "lead_p": "The privacy line, the never list and how to get a team started are "
                  "not secrets. They are the reason people call.",
        "lead_href": "/insights/",
        "lead_cta": "Read the blog",
        "groups": [
            ("Guides", [
                ("/guides/getting-your-team-started/", "Getting your team started"),
                ("/guides/privacy-basics/", "Privacy basics for small business"),
                ("/guides/what-never-goes-in/", "What never goes in an AI tool"),
            ]),
            ("Blog", [
                ("/insights/", "All articles"),
                ("/insights/category/privacy-and-policy/", "Privacy &amp; policy"),
                ("/insights/category/getting-started/", "Getting started"),
                ("/insights/category/industry-notes/", "Industry notes"),
            ]),
            ("Resources", [
                ("/resources/", "All resources"),
                ("/resources/ai-policy-templates/", "AI policy templates"),
                ("/resources/prompt-library/", "Starting prompt library"),
                ("/tools/prompt-builder/", "Prompt builder"),
                ("/resources/vendor-checklist/", "Vendor checklist"),
            ]),
            ("About us", [
                ("/about/", "About"),
                ("/about/why-two-tools/", "Why we teach two tools"),
                ("/case-studies/", "What engagements look like"),
                ("/contact/", "Start an enquiry"),
            ]),
        ],
    },
]

FOOTER = [
    ("Who it's for", [
        ("/who-this-is-for/", "All four"),
        ("/who-this-is-for/worried-about-your-job/", "Worried about your job"),
        ("/who-this-is-for/never-used-it/", "Never used it"),
        ("/who-this-is-for/teaching-yourself/", "Teaching yourself"),
        ("/who-this-is-for/owners-and-managers/", "Owners &amp; managers"),
    ]),
    ("Training", [
        ("/training/", "Full curriculum"),
        ("/training/useful-output/", "Useful output"),
        ("/training/choosing-your-tool/", "Choosing your tool"),
        ("/training/long-documents/", "Long documents"),
        ("/training/reusable-setups/", "Reusable setups"),
        ("/training/what-never-goes-in/", "What never goes in"),
        ("/training/team-ai-policy/", "Your team's AI policy"),
    ]),
    ("Industries", [
        ("/industries/", "All industries"),
        ("/industries/accounting-bookkeeping/", "Accounting &amp; bookkeeping"),
        ("/industries/real-estate/", "Real estate &amp; property management"),
        ("/industries/allied-health/", "Allied health clinics"),
        ("/industries/legal-conveyancing/", "Legal support &amp; conveyancing"),
        ("/industries/ndis-providers/", "NDIS &amp; disability providers"),
        ("/industries/trades/", "Trades &amp; field services"),
        ("/industries/cleaning-maintenance/", "Cleaning &amp; property maintenance"),
    ]),
    ("Tools", [
        ("/tools/prompt-builder/", "Prompt builder"),
        ("/tools/", "How we teach both"),
        ("/tools/which-tool/", "Which tool for which job"),
        ("/tools/claude/", "Claude"),
        ("/tools/claude/long-documents/", "Claude for long documents"),
        ("/tools/claude/projects/", "Claude Projects"),
        ("/tools/chatgpt/", "ChatGPT"),
        ("/tools/chatgpt/voice-to-draft/", "Voice to draft"),
        ("/tools/chatgpt/custom-setups/", "Custom setups"),
        ("/tools/tiers-and-your-data/", "Tiers and your data"),
        ("/tools/vendor-questions/", "Vendor questions"),
    ]),
    ("Services", [
        ("/services/", "How engagements work"),
        ("/services/team-workshop/", "Team workshop"),
        ("/services/workflow-build/", "Workflow build"),
        ("/services/policy-and-audit/", "Policy &amp; audit"),
        ("/services/advisory/", "Ongoing advisory"),
        ("/services/what-it-costs/", "Scope and price"),
        ("/assessment/", "Build your plan"),
    ]),
    ("Learn", [
        ("/insights/", "Blog"),
        ("/guides/", "Guides"),
        ("/guides/getting-your-team-started/", "Getting started"),
        ("/guides/privacy-basics/", "Privacy basics"),
        ("/guides/what-never-goes-in/", "The never list"),
        ("/resources/", "Resources"),
        ("/case-studies/", "Engagement examples"),
    ]),
    ("Company", [
        ("/about/", "About"),
        ("/about/why-two-tools/", "Why two tools"),
        ("/contact/", "Start an enquiry"),
        ("/privacy/", "Privacy"),
        ("/terms/", "Terms"),
    ]),
]

# Route → (crumb label, parent route). Drives BreadcrumbList and the page crumb.
PARENTS = {
    "/about/why-two-tools/": "/about/",
    "/guides/getting-your-team-started/": "/guides/",
    "/guides/privacy-basics/": "/guides/",
    "/guides/what-never-goes-in/": "/guides/",
    "/resources/ai-policy-templates/": "/resources/",
    "/resources/prompt-library/": "/resources/",
    "/resources/vendor-checklist/": "/resources/",
    "/services/team-workshop/": "/services/",
    "/services/workflow-build/": "/services/",
    "/services/policy-and-audit/": "/services/",
    "/services/advisory/": "/services/",
    "/services/what-it-costs/": "/services/",
    "/tools/claude/": "/tools/",
    "/tools/chatgpt/": "/tools/",
    "/tools/claude/long-documents/": "/tools/claude/",
    "/tools/claude/projects/": "/tools/claude/",
    "/tools/chatgpt/voice-to-draft/": "/tools/chatgpt/",
    "/tools/chatgpt/custom-setups/": "/tools/chatgpt/",
    "/tools/which-tool/": "/tools/",
    "/tools/tiers-and-your-data/": "/tools/",
    "/tools/vendor-questions/": "/tools/",
    "/training/useful-output/": "/training/",
    "/training/choosing-your-tool/": "/training/",
    "/training/long-documents/": "/training/",
    "/training/reusable-setups/": "/training/",
    "/training/what-never-goes-in/": "/training/",
    "/training/team-ai-policy/": "/training/",
}
for slug, name in [
    ("accounting-bookkeeping", "Accounting & bookkeeping"),
    ("real-estate", "Real estate & property management"),
    ("allied-health", "Allied health clinics"),
    ("legal-conveyancing", "Legal support & conveyancing"),
    ("ndis-providers", "NDIS & disability providers"),
    ("trades", "Trades & field services"),
    ("cleaning-maintenance", "Cleaning & property maintenance"),
]:
    PARENTS[f"/industries/{slug}/"] = "/industries/"

CRUMB_LABELS = {
    "/tools/prompt-builder/": "Prompt builder",
    "/who-this-is-for/": "Who it's for",
    "/who-this-is-for/worried-about-your-job/": "Worried about your job",
    "/who-this-is-for/never-used-it/": "Never used it",
    "/who-this-is-for/teaching-yourself/": "Teaching yourself",
    "/who-this-is-for/owners-and-managers/": "Owners & managers",
    "/": "Home",
    "/about/": "About",
    "/assessment/": "Build your plan",
    "/case-studies/": "Engagement examples",
    "/contact/": "Contact",
    "/guides/": "Guides",
    "/industries/": "Industries",
    "/insights/": "Blog",
    "/privacy/": "Privacy",
    "/resources/": "Resources",
    "/services/": "Services",
    "/terms/": "Terms",
    "/tools/": "Tools",
    "/tools/claude/": "Claude",
    "/tools/chatgpt/": "ChatGPT",
    "/training/": "Training",
}
