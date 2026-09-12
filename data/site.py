"""Single source of truth for site-wide constants."""

SITE = {
    "name": "AI at work",
    "origin": "https://ai-at-work.au",
    "locale": "en-AU",
    "email": "hello@ai-at-work.au",
    "city": "Sydney",
    "region": "NSW",
    "country": "AU",
    "gtm": "GTM-5BL56Z44",
    "tagline": "Practical AI training for Australian businesses. Claude and ChatGPT, "
                "taught side by side, tool-neutral.",
    "og_image": "/brand/og-image.png",
    "maintainer": {"name": "DigiWolf", "url": "https://digiwolf.au"},
    # The one conversion action on the site.
    "cta": {"href": "/contact/", "label": "Start an enquiry", "short": "Enquire"},
    "thanks": "/thank-you/",
}

# Published verticals, used for the enquiry form select and internal linking.
INDUSTRIES = [
    ("accounting-bookkeeping", "Accounting & bookkeeping"),
    ("real-estate", "Real estate & property management"),
    ("allied-health", "Allied health clinics"),
    ("legal-conveyancing", "Legal support & conveyancing"),
    ("ndis-providers", "NDIS & disability providers"),
    ("trades", "Trades & field services"),
    ("cleaning-maintenance", "Cleaning & property maintenance"),
]

ENGAGEMENTS = [
    ("team-workshop", "Team workshop"),
    ("workflow-build", "Done-with-you workflow build"),
    ("policy-and-audit", "AI policy & audit"),
    ("advisory", "Ongoing advisory"),
]
