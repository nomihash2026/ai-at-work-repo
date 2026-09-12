"""Re-derive src/assessment.js from the original engine and apply our changes.

The engine itself is not ours — it was ported in, question set and scoring
intact — so this keeps our modifications as a reviewable patch rather than a
hand-edited fork. Run it if the engine is ever re-extracted.

Three changes, all in service of one rule: the enquiry form is the only
conversion action on the site, so the plan is never traded for an email address.
  1. the email capture block becomes a handoff to /contact/
  2. submit() and the CRM endpoint go, since nothing posts from here any more
  3. stash() writes a plan summary to sessionStorage for the form to read
"""
import re
import sys

PATH = "src/assessment.js"
js = open(PATH).read()

CAPTURE_OLD_START = "    /* Capture */"
CAPTURE_OLD_END = "    h += '<div id=\"sent\"></div>';\n    h += '</div>';"

CAPTURE_NEW = """    /* Handoff. The enquiry form is the only conversion action on the site, so
       the plan is never traded for an address — it walks across to the form. */
    h += '<div class="capture" id="capture">';
    h += '<h3>Take this plan to a conversation</h3>';
    h += '<p>The plan above is yours either way — print it, or leave the tab open. If you send an enquiry from here, a summary of your answers travels with you into the form, so the first conversation starts from your week rather than from scratch.</p>';
    h += '<div class="actions"><a class="btn-primary" id="handoff" href="/contact/">Start an enquiry</a>';
    h += '<a class="btn-quiet" href="' + esc(offer.href) + '">Read what this involves</a>';
    h += '<button class="btn-quiet" id="print">Print it instead</button></div>';
    h += '<p class="capture-note">No email address is asked for here, and nothing is sent anywhere until you fill in the form yourself. The summary is held in this browser tab only.</p>';
    h += '</div>';"""

STASH = """    var handoff = document.getElementById('handoff');
    if (handoff) handoff.addEventListener('click', function(){ stash(label, plan, offer); });
  }

  /* Hand the plan to the enquiry form via sessionStorage: same tab only, and
     no query string, so nothing about the business lands in a URL or a log. */
  function stash(label, plan, offer){
    try {
      var lines = ['Assessment summary — ' + label];
      lines.push('Recommended starting point: ' + offer.name);
      lines.push('Exposure reading: ' + plan.band);
      if (plan.modules.length){
        lines.push('Modules in order: ' + plan.modules.map(function(m){ return m.name; }).join('; '));
      }
      var jobs = plan.chosen.map(function(c){ return c.label; });
      if (jobs.length) lines.push('Jobs selected: ' + jobs.join('; '));
      if (plan.byTool.neither.length){
        lines.push('Stays with a qualified person: ' + plan.byTool.neither.join('; '));
      }
      sessionStorage.setItem('aiw_plan', lines.join('\\n'));
    } catch (e) { /* private browsing: the form still works, just unprefilled */ }
  }"""


def cut(text, start_marker, end_marker, replacement):
    i = text.index(start_marker)
    j = text.index(end_marker, i) + len(end_marker)
    return text[:i] + replacement + text[j:]


if "id=\"handoff\"" in js:
    print("already patched, nothing to do")
    sys.exit(0)

# 1. capture block -> handoff block
js = cut(js, CAPTURE_OLD_START, CAPTURE_OLD_END, CAPTURE_NEW)

# 2. the send button wiring -> handoff wiring + stash()
js = js.replace("    document.getElementById('send').addEventListener('click', submit);\n  }",
                STASH)

# 3. submit() is now dead code, and so is the endpoint config
js = cut(js, "  function submit(){", "\n  renderQuestion();\n})();", "\n  renderQuestion();\n})();")
js = re.sub(r"\n *endpoint: null,",
            "\n  /* No endpoint by design: the plan hands off to /contact/. */", js)

open(PATH, "w").write(js)
print(f"patched {PATH}: handoff in place, submit() removed, endpoint retired")
