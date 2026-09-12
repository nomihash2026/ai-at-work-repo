/* =============================================================================
   The prompt builder.

   Teaches the site's actual method rather than handing out a prompt library:
   a usable instruction states who is writing, for whom, under what constraint,
   what good looks like, and what must never appear. The tool makes you answer
   those in order and assembles the result live, so the lesson is the sequence
   rather than the output.

   Runs entirely in the browser. Nothing is transmitted. The built prompt can be
   carried into the enquiry form via sessionStorage — same tab, no query string,
   same mechanism the assessment uses — so nothing about the business lands in a
   URL or a server log.
   ========================================================================== */
(function () {
  'use strict';

  var root = document.getElementById('builder');
  if (!root) return;

  /* ---------------------------------------------------------------- data -- */

  var JOBS = [
    { id: 'email', label: 'Draft an email I write versions of constantly',
      tool: 'chatgpt',
      task: 'Draft an email.',
      good: ['It reads as though a person in this business wrote it, not a template.',
             'It is short enough to be read on a phone.',
             'It has one clear thing for the reader to do next.'] },
    { id: 'notes', label: 'Turn my notes into a finished document',
      tool: 'claude',
      task: 'Turn the notes below into a finished document. The notes are the ' +
            'source of truth — do not add facts that are not in them.',
      good: ['Everything in the output traces back to something in my notes.',
             'Gaps are listed as questions rather than filled in.',
             'The structure is consistent enough to reuse next time.'] },
    { id: 'long', label: 'Get an answer out of a long document',
      tool: 'claude',
      task: 'I am going to give you a long document and ask a specific question ' +
            'about it. Answer only from the document.',
      good: ['Every claim points at the clause, section or page it came from.',
             'Where the document does not answer it, it says so plainly.',
             'It answers the question asked rather than summarising the document.'] },
    { id: 'explain', label: 'Explain something technical in plain English',
      tool: 'chatgpt',
      task: 'Rewrite the material below so the reader described can follow it.',
      good: ['No term is used before it is explained.',
             'Nothing technically true has been made false in the simplifying.',
             'It would not embarrass me if the reader already knew the subject.'] },
    { id: 'quote', label: 'Write a quote, proposal or scope',
      tool: 'claude',
      task: 'Draft a quote or scope of work from the details below.',
      good: ['Inclusions and exclusions are both stated, not just inclusions.',
             'No price, rate or timeframe appears that I did not supply.',
             'Assumptions are listed where I have not given enough detail.'] },
    { id: 'report', label: 'Produce a recurring report or update',
      tool: 'claude',
      task: 'Produce this period\u2019s version of a recurring report from the ' +
            'material below, in the same structure every time.',
      good: ['The structure is identical to last period so they can be compared.',
             'Changes since last period are stated rather than implied.',
             'Nothing is characterised as good or bad that the data does not support.'] }
  ];

  var READERS = [
    { id: 'client', label: 'A client or customer',
      line: 'The reader is a client of the business. Assume no familiarity with ' +
            'internal terminology or process.' },
    { id: 'colleague', label: 'Someone inside the business',
      line: 'The reader is a colleague inside the business who already knows the ' +
            'context, so do not restate background they have.' },
    { id: 'professional', label: 'Another professional — a referrer, a solicitor, an accountant',
      line: 'The reader is another professional who is competent in their own ' +
            'field but not in mine. Precision matters more than warmth.' },
    { id: 'regulator', label: 'A regulator, auditor or funder',
      line: 'The reader is a regulator, auditor or funder. Every statement must ' +
            'be one I could evidence, and nothing should be overstated.' },
    { id: 'public', label: 'The public — a listing, a post, a website page',
      line: 'The reader is a member of the public with no prior contact with the ' +
            'business.' }
  ];

  var CONSTRAINTS = [
    { id: 'plain', label: 'Plain English, no jargon',
      line: 'Write in plain English. If a technical term is unavoidable, explain ' +
            'it the first time in the same sentence.' },
    { id: 'short', label: 'Must fit on one page',
      line: 'It must fit on a single page. Cut rather than compress.' },
    { id: 'voice', label: 'Must match how we already write',
      line: 'Match the style of the example I have given rather than a generic ' +
            'professional register.' },
    { id: 'noadvice', label: 'Must not give advice or an opinion',
      line: 'Do not give advice, an opinion or a recommendation. State what is ' +
            'the case and stop there.' },
    { id: 'evidence', label: 'Must be defensible if someone audits it',
      line: 'Every claim must be traceable to something I supplied. Where it is ' +
            'not, say so rather than filling the gap.' },
    { id: 'ask', label: 'Should ask me questions before starting',
      line: 'Before drafting, list anything you need from me that is missing. ' +
            'Wait for my answers rather than assuming.' }
  ];

  var NEVER = [
    { id: 'names', label: 'Client or patient names' },
    { id: 'health', label: 'Health or clinical information' },
    { id: 'financial', label: 'Account numbers or financial details' },
    { id: 'ids', label: 'Dates of birth, addresses, ID numbers' },
    { id: 'legal', label: 'Anything under a confidentiality obligation' },
    { id: 'staff', label: 'Information about a named staff member' }
  ];

  var INDUSTRIES = [
    'accounting or bookkeeping practice', 'real estate or property management agency',
    'allied health clinic', 'legal or conveyancing practice',
    'NDIS or disability services provider', 'trades or field services business',
    'cleaning or property maintenance business', 'business'
  ];

  var state = {
    industry: INDUSTRIES[INDUSTRIES.length - 1],
    job: null, reader: null, constraints: [], never: [], extra: ''
  };

  /* ---------------------------------------------------------------- build -- */

  function esc(s) {
    return String(s).replace(/[&<>"]/g, function (c) {
      return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c];
    });
  }

  function job() { return JOBS.filter(function (j) { return j.id === state.job; })[0]; }
  function reader() { return READERS.filter(function (r) { return r.id === state.reader; })[0]; }

  function assemble() {
    var j = job(), r = reader();
    if (!j || !r) return null;

    var out = [];
    out.push('You are writing on behalf of an Australian ' + state.industry + '.');
    out.push('');
    out.push('The job: ' + j.task);
    out.push('');
    out.push('The reader: ' + r.line);

    var cons = CONSTRAINTS.filter(function (c) {
      return state.constraints.indexOf(c.id) > -1;
    });
    if (cons.length) {
      out.push('');
      out.push('Constraints:');
      cons.forEach(function (c) { out.push('- ' + c.line); });
    }

    out.push('');
    out.push('What a good answer looks like:');
    j.good.forEach(function (g) { out.push('- ' + g); });

    out.push('');
    out.push('Do not include:');
    var nev = NEVER.filter(function (n) { return state.never.indexOf(n.id) > -1; });
    nev.forEach(function (n) { out.push('- ' + n.label + '.'); });
    out.push('- Anything you are not certain of. If something is missing, tell me ' +
             'what you need rather than inventing it.');

    if (state.extra.trim()) {
      out.push('');
      out.push('Also: ' + state.extra.trim());
    }

    out.push('');
    out.push('I will paste the material below this line.');
    return out.join('\n');
  }

  var CHECKS = [
    'Read it once as the reader, not as the author.',
    'Check every number, name and date against your own source.',
    'Delete anything the tool asserted that you did not supply.',
    'Ask whether you would be comfortable if the reader knew how it was drafted.'
  ];

  /* --------------------------------------------------------------- render -- */

  function optList(name, items, multi) {
    return items.map(function (it) {
      var on = multi
        ? state[name].indexOf(it.id) > -1
        : state[name] === it.id;
      return '<label class="opt"' + (multi ? ' data-multi' : '') + '>' +
        '<input type="' + (multi ? 'checkbox' : 'radio') + '" name="' + name +
        '" value="' + it.id + '"' + (on ? ' checked' : '') + '>' +
        '<span>' + esc(it.label) + '</span></label>';
    }).join('');
  }

  function render() {
    var prompt = assemble();
    var j = job();

    var h = '';
    h += '<div class="bd-grid">';

    h += '<div class="bd-ask">';

    h += '<fieldset class="bd-step"><legend>What kind of business is this for?</legend>';
    h += '<div class="field"><select name="industry">' + INDUSTRIES.map(function (i) {
      return '<option' + (i === state.industry ? ' selected' : '') + '>' + esc(i) + '</option>';
    }).join('') + '</select></div></fieldset>';

    h += '<fieldset class="bd-step"><legend>What is the job?</legend>';
    h += '<div class="opts">' + optList('job', JOBS, false) + '</div></fieldset>';

    h += '<fieldset class="bd-step"><legend>Who reads the result?</legend>';
    h += '<div class="opts">' + optList('reader', READERS, false) + '</div></fieldset>';

    h += '<fieldset class="bd-step"><legend>What has to be true of it?</legend>';
    h += '<p class="q-help">Choose as many as apply. Each one adds a line the tool ' +
         'will otherwise guess at.</p>';
    h += '<div class="opts">' + optList('constraints', CONSTRAINTS, true) + '</div></fieldset>';

    h += '<fieldset class="bd-step"><legend>What must never appear?</legend>';
    h += '<p class="q-help">This is the half of the instruction almost everybody ' +
         'leaves out. It is also the half that prevents the damage.</p>';
    h += '<div class="opts">' + optList('never', NEVER, true) + '</div></fieldset>';

    h += '<fieldset class="bd-step"><legend>Anything else it must know?</legend>';
    h += '<div class="field"><textarea name="extra" rows="3" placeholder="Optional. ' +
         'One or two sentences.">' + esc(state.extra) + '</textarea></div></fieldset>';

    h += '</div>';

    /* ------------------------------------------------------------ output -- */
    h += '<div class="bd-out" aria-live="polite">';
    if (!prompt) {
      h += '<p class="bd-empty">Choose a job and a reader and the instruction ' +
           'builds here as you go.</p>';
    } else {
      h += '<h3>Your instruction</h3>';
      h += '<pre class="bd-prompt" id="bd-prompt">' + esc(prompt) + '</pre>';
      h += '<div class="actions">';
      h += '<button type="button" id="bd-copy" class="btn-primary">Copy it</button>';
      h += '<a class="btn-quiet" id="bd-hand" href="/contact/">Send it with an enquiry</a>';
      h += '</div>';

      h += '<h3 class="bd-h">Which tool to put it in</h3>';
      h += '<p>' + (j.tool === 'claude'
        ? 'Reach for <strong>Claude</strong>. This job involves sustained writing ' +
          'or a long source document, which is where it holds a thread better.'
        : 'Reach for <strong>ChatGPT</strong>. This job is short, repeated and ' +
          'fast, which is what it is good at.') +
        ' Neither is a recommendation to pay for anything — check ' +
        '<a href="/tools/tiers-and-your-data/">what the tier does with your ' +
        'material</a> first.</p>';

      h += '<h3 class="bd-h">Before you send whatever comes back</h3>';
      h += '<ol class="bd-checks">' + CHECKS.map(function (c) {
        return '<li>' + c + '</li>';
      }).join('') + '</ol>';

      if (!state.never.length) {
        h += '<p class="bd-warn">You have not marked anything as off limits. ' +
             'Almost every business has something. <a href="/guides/what-never-goes-in/">' +
             'The never list</a> takes three minutes to read.</p>';
      }
    }
    h += '</div></div>';

    root.innerHTML = h;
    wire();
  }

  /* ----------------------------------------------------------------- wire -- */

  function wire() {
    root.querySelectorAll('input[type=radio]').forEach(function (el) {
      el.addEventListener('change', function () {
        state[el.name] = el.value;
        render();
      });
    });
    root.querySelectorAll('input[type=checkbox]').forEach(function (el) {
      el.addEventListener('change', function () {
        var arr = state[el.name], i = arr.indexOf(el.value);
        if (el.checked && i === -1) arr.push(el.value);
        if (!el.checked && i > -1) arr.splice(i, 1);
        render();
      });
    });
    var sel = root.querySelector('select[name=industry]');
    if (sel) sel.addEventListener('change', function () {
      state.industry = sel.value;
      render();
    });
    var ta = root.querySelector('textarea[name=extra]');
    if (ta) {
      ta.addEventListener('input', function () { state.extra = ta.value; });
      ta.addEventListener('blur', render);
    }

    var copy = document.getElementById('bd-copy');
    if (copy) copy.addEventListener('click', function () {
      var text = assemble();
      if (!text) return;
      var done = function () {
        copy.textContent = 'Copied';
        setTimeout(function () { copy.textContent = 'Copy it'; }, 2000);
      };
      if (navigator.clipboard && navigator.clipboard.writeText) {
        navigator.clipboard.writeText(text).then(done, fallback);
      } else { fallback(); }
      function fallback() {
        var el = document.getElementById('bd-prompt');
        var r = document.createRange();
        r.selectNodeContents(el);
        var s = window.getSelection();
        s.removeAllRanges();
        s.addRange(r);
        done();
      }
    });

    var hand = document.getElementById('bd-hand');
    if (hand) hand.addEventListener('click', stash);
  }

  /* Carry the answers into the enquiry form. Same tab only, no query string,
     so nothing about the business lands in a URL or a server log. */
  function stash() {
    try {
      var j = job(), r = reader();
      if (!j || !r) return;
      var lines = ['Prompt builder — ' + state.industry];
      lines.push('Job: ' + j.label);
      lines.push('Reader: ' + r.label);
      if (state.constraints.length) {
        lines.push('Must be: ' + CONSTRAINTS.filter(function (c) {
          return state.constraints.indexOf(c.id) > -1;
        }).map(function (c) { return c.label; }).join('; '));
      }
      lines.push('Off limits: ' + (state.never.length
        ? NEVER.filter(function (n) { return state.never.indexOf(n.id) > -1; })
            .map(function (n) { return n.label; }).join('; ')
        : 'nothing marked — worth a conversation'));
      lines.push('Suggested tool: ' + (j.tool === 'claude' ? 'Claude' : 'ChatGPT'));
      var existing = sessionStorage.getItem('aiw_plan');
      sessionStorage.setItem('aiw_plan',
        existing ? existing + '\n\n' + lines.join('\n') : lines.join('\n'));
    } catch (e) { /* private browsing: the form still works, just unprefilled */ }
  }

  render();
})();
