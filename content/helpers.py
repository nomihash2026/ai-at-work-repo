"""Shared helpers for the expansion modules."""

import re


def sect(body, lift=False):
    cls = "sect sect-lift" if lift else "sect"
    return f'<section class="{cls}"><div class="shell"><div class="prose">{body}</div></div></section>'


def faq_section(faq, heading="The questions we get asked about this"):
    items = "".join(f'<div class="qa-item"><h3>{q}</h3><p>{a}</p></div>' for q, a in faq)
    return ('<section class="sect"><div class="shell">'
            f'<h2 class="sect-hd">{heading}</h2>'
            f'<div class="qa">{items}</div></div></section>')


def faq_schema(faq):
    return {
        "@type": "FAQPage",
        "mainEntity": [{"@type": "Question", "name": q,
                        "acceptedAnswer": {"@type": "Answer",
                                           "text": re.sub(r"<[^>]+>", "", a)}}
                       for q, a in faq],
    }
