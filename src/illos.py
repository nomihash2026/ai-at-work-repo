"""Original artwork and diagrams.

Two kinds of visual here, and the distinction matters:

* svg_* functions are artwork — geometry echoing the logo's node-and-rule
  construction. Decorative, so aria-hidden, no text inside.
* dg_* functions are diagrams — the information IS the content, so they are
  built from real HTML (headings, lists, tables) styled to read as a figure.
  Text reflows, screen readers get structure, and nothing goes illegible at
  380px the way SVG label text does.

Everything is drawn with brand tokens, so a palette change propagates.
No third-party assets, nothing to license.
"""

import hashlib


# ---------------------------------------------------------------- artwork ----

# ---------------------------------------------------------------------------
# Artwork, retired.
#
# The minimalism pass allows no icons or illustrations: none of these carried
# information the surrounding text did not already state. The builders stay so
# every call site keeps working; they emit nothing.
# ---------------------------------------------------------------------------

def svg_spine(cls="art art-spine"): return ""
def svg_boundary(cls="art art-boundary"): return ""
def svg_two_tools(cls="art art-tools"): return ""
def svg_stack(cls="art art-stack"): return ""
def svg_industry_mark(slug, cls="imark"): return ""
def svg_post_cover(seed, cls="cover"): return ""

def dg_figure(body, caption=None, cls=""):
    cap = f'<figcaption>{caption}</figcaption>' if caption else ""
    return f'<figure class="fig {cls}">{body}{cap}</figure>'


def dg_clock(title, blocks, caption=None):
    """A session broken into time blocks. Genuinely a sequence, so it's numbered."""
    items = "".join(
        f'<li><span class="clk-t">{t}</span><span class="clk-b">'
        f'<strong>{h}</strong>{"<span>" + d + "</span>" if d else ""}</span></li>'
        for t, h, d in blocks)
    return dg_figure(
        f'<div class="clk"><h3>{title}</h3><ol class="clk-list">{items}</ol></div>',
        caption, "fig-clock")


def dg_split(left, right, caption=None):
    """Two columns with a hard rule between them. Used for the never list."""
    def col(c, tone):
        items = "".join(f'<li>{i}</li>' for i in c["items"])
        return (f'<div class="spl-col" data-tone="{tone}"><h4>{c["head"]}</h4>'
                f'<ul>{items}</ul></div>')
    return dg_figure(
        f'<div class="spl">{col(left, "ok")}{col(right, "stop")}</div>',
        caption, "fig-split")


def dg_steps(steps, caption=None):
    items = "".join(
        f'<li><strong>{h}</strong><span>{d}</span></li>' for h, d in steps)
    return dg_figure(f'<ol class="arc">{items}</ol>', caption, "fig-arc")


def dg_beforeafter(rows, caption=None):
    """The same task, the way it runs now and the way it runs after."""
    body = "".join(
        f'<tr><th scope="row">{task}</th><td>{now}</td><td>{after}</td></tr>'
        for task, now, after in rows)
    return dg_figure(
        '<div class="table-wrap"><table class="ba"><thead><tr><th scope="col">The job</th>'
        '<th scope="col">How it runs now</th><th scope="col">How it runs after</th></tr>'
        f'</thead><tbody>{body}</tbody></table></div>', caption, "fig-ba")


def dg_checklist(head, items, caption=None):
    li = "".join(f'<li>{i}</li>' for i in items)
    return dg_figure(f'<div class="chk"><h3>{head}</h3><ul>{li}</ul></div>', caption, "fig-chk")


def dg_prompt(specimens, caption=None):
    """Two or more prompt specimens, stacked. The prompt itself is the content,
    so it is set in the same face as everything else and separated by an indent
    and an italic label rather than by a box or a second typeface."""
    items = ""
    for label, prompt, result in specimens:
        res = f'<p class="pr-out">{result}</p>' if result else ""
        items += (f'<div class="pr-item"><p class="pr-lab">{label}</p>'
                  f'<p class="pr-txt">{prompt}</p>{res}</div>')
    return dg_figure(f'<div class="pr">{items}</div>', caption, "fig-pr")


def dg_where(head, columns, caption=None):
    """What lives where. Two or three columns of plain lists under a heading,
    for setups where the whole point is which things are stated once and which
    are restated every time."""
    cols = ""
    for title, items in columns:
        li = "".join(f"<li>{i}</li>" for i in items)
        cols += f'<div class="spl-col"><h4>{title}</h4><ul>{li}</ul></div>'
    return dg_figure(
        f'<h3 class="wh-h">{head}</h3><div class="spl">{cols}</div>',
        caption, "fig-where")
