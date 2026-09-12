
/* ============================================================
   CONFIG
   ============================================================ */
var CONFIG = {
  brand: 'AI at work',

  /* Open decision 6. One of:
     'free'        results and full plan shown, email optional
     'plan_gated'  reading shown, module list gated behind email
     'gated'       nothing shown until email
     Starting at 'free': the plan is the proof of competence, and
     a principal who reads it and recognises their own week is a
     better lead than one who traded an address for a PDF. */
  gating: 'free',

  /* null = demo mode. The form validates and shows what would be
     sent, and posts nowhere. Wire this to the CRM before launch. */
  /* No endpoint by design: the plan hands off to /contact/. */

  contact: '/contact/'
};

/* ============================================================
   SPINE — the core curriculum, written once for every vertical.
   Industry tracks sit on top of this, they do not replace it.
   ============================================================ */
var SPINE = {
  'useful-output': {
    name: 'Getting output you can actually use',
    href: '/training/useful-output/',
    why: 'The gap between a disappointing answer and a usable one is almost always in the brief, not the tool.'
  },
  'choosing-your-tool': {
    name: 'Choosing your tool for the job',
    href: '/training/choosing-your-tool/',
    why: 'A rule of thumb for which tool to reach for, so the team stops defaulting to whichever one they opened first.'
  },
  'long-documents': {
    name: 'Working with long documents',
    href: '/training/long-documents/',
    why: 'Reading, comparing and pulling structure out of documents too long to read twice.'
  },
  'reusable-setups': {
    name: 'Building reusable setups',
    href: '/training/reusable-setups/',
    why: 'This is what turns one good session into a change that survives the month. The rest is a party trick without it.'
  },
  'what-never-goes-in': {
    name: 'What never goes in',
    href: '/training/what-never-goes-in/',
    why: 'One page your team can actually remember, specific to the records you hold.'
  },
  'team-ai-policy': {
    name: "Writing your team's AI policy",
    href: '/training/team-ai-policy/',
    why: 'A written rule, in your words, that covers which tool, which tier and which records.'
  }
};

/* ============================================================
   PACKS — one per vertical. Wave 1 only; Wave 2 verticals get a
   pack file each and appear in Q1 automatically.

   tier_emphasis  how hard the free-vs-paid tier question lands
   entry_offer    the default starting engagement
   lead_with      'policy' verticals route to policy first at a
                  lower exposure threshold than the rest
   ============================================================ */
var PACKS = {

'accounting-bookkeeping': {
  name: 'Accounting & bookkeeping',
  family: 'Finance & compliance',
  tier_emphasis: 'high',
  entry_offer: 'workshop',
  lead_with: 'work',
  privacy_line: 'Identifiable client financial data does not go into a consumer account. Almost everything that is actually eating your week involves no client data at all.',
  privacy_src: 'The usual objection in an accounting practice is that client data is confidential. It is — and most of the time-sink work never touches it.',
  risk_boundary: 'Tax positions, advice and anything that lands in a return stay with the practitioner. The training covers admin, drafting and document work, and is explicit about where that line sits.',
  sinks: [
    { id:'a1', label:'Drafting client emails that explain something technical', tool:'chatgpt', mods:['useful-output','reusable-setups'] },
    { id:'a2', label:'Turning a messy client spreadsheet into something workable', tool:'claude', mods:['long-documents','useful-output'] },
    { id:'a3', label:'File notes, workpaper narratives and write-ups', tool:'claude', mods:['useful-output','reusable-setups'] },
    { id:'a4', label:'Reading a long ruling, standard or policy update', tool:'claude', mods:['long-documents'] },
    { id:'a5', label:'Chasing outstanding information from clients', tool:'chatgpt', mods:['reusable-setups'] },
    { id:'a6', label:'Engagement letters, onboarding packs and checklists', tool:'claude', mods:['reusable-setups'] },
    { id:'a7', label:'Proposals and scope letters for new work', tool:'chatgpt', mods:['useful-output'] }
  ]
},

'real-estate': {
  name: 'Real estate & property management',
  family: 'Property & construction',
  tier_emphasis: 'moderate',
  entry_offer: 'workshop',
  lead_with: 'work',
  /* Sales and PM tasks barely overlap. Q2 splits them and the
     plan is built from one list, never both. Do not merge these. */
  split: {
    question: 'Which side of the business is this plan for?',
    help: 'Sales and property management share a tool and almost nothing else. Running both in one room wastes half the day for both halves of the team.',
    options: [
      { id:'sales', label:'Sales' },
      { id:'pm', label:'Property management' },
      { id:'both', label:'Both — but I understand these run as separate sessions' }
    ]
  },
  privacy_line: 'Owner and tenant personal details stay out of the tool. Listing copy, vendor reports and follow-up do not need a single name to be written well.',
  privacy_src: 'Agents are already using AI personally. The training improves what they are doing rather than asking them to stop.',
  risk_boundary: 'Contract interpretation, disclosure obligations and anything a solicitor signs stay out of scope. Reading a document to understand it is not the same as advising on it, and the training says so out loud.',
  sinks: [
    { id:'s1', label:'Listing copy and campaign emails', tool:'chatgpt', mods:['useful-output','reusable-setups'], side:'sales' },
    { id:'s2', label:'Vendor reports and weekly updates', tool:'claude', mods:['reusable-setups'], side:'sales' },
    { id:'s3', label:'Buyer follow-up after opens', tool:'chatgpt', mods:['reusable-setups'], side:'sales' },
    { id:'s4', label:'Appraisal and listing pitch documents', tool:'claude', mods:['useful-output','reusable-setups'], side:'sales' },
    { id:'s5', label:'Social captions and short video scripts', tool:'chatgpt', mods:['useful-output'], side:'sales' },
    { id:'p1', label:'Arrears and breach correspondence', tool:'claude', mods:['reusable-setups','useful-output'], side:'pm' },
    { id:'p2', label:'Routine inspection reports written up from notes', tool:'chatgpt', mods:['useful-output'], side:'pm' },
    { id:'p3', label:'Owner updates and maintenance approvals', tool:'chatgpt', mods:['reusable-setups'], side:'pm' },
    { id:'p4', label:'Tenant enquiries answered consistently across the team', tool:'claude', mods:['reusable-setups'], side:'pm' },
    { id:'p5', label:'Reading a strata report or tribunal document', tool:'claude', mods:['long-documents'], side:'pm' },
    { id:'p6', label:'End-of-lease and renewal packs', tool:'claude', mods:['reusable-setups'], side:'pm' }
  ]
},

'allied-health': {
  name: 'Allied health clinics',
  family: 'Health & care',
  tier_emphasis: 'critical',
  entry_offer: 'policy_session',
  lead_with: 'policy',
  privacy_line: 'No identifiable client information in any tool, on any tier, until the written rule says which tool and which tier. That sentence comes before the productivity conversation, not after it.',
  privacy_src: 'In a clinic the privacy module is the product. Trust on this unlocks everything else.',
  risk_boundary: 'No clinical reasoning, no diagnosis, no treatment decisions. The training covers the writing and the paperwork around clinical work, and is reviewed by someone qualified before it is taught.',
  sinks: [
    { id:'h1', label:'Letters back to referrers', tool:'claude', mods:['useful-output','reusable-setups'] },
    { id:'h2', label:'Turning session notes into a progress report', tool:'claude', mods:['long-documents','what-never-goes-in'] },
    { id:'h3', label:'Plain-language handouts and home programs', tool:'chatgpt', mods:['useful-output'] },
    { id:'h4', label:'Funding and plan-review paperwork', tool:'claude', mods:['long-documents','reusable-setups'] },
    { id:'h5', label:'Reception, enquiry and recall replies', tool:'chatgpt', mods:['reusable-setups'] },
    { id:'h6', label:'Policies, consent forms and practice documents', tool:'claude', mods:['reusable-setups','team-ai-policy'] },
    { id:'h7', label:'Anything against a named client record', tool:'neither', mods:['what-never-goes-in','team-ai-policy'] }
  ]
},

'legal-conveyancing': {
  name: 'Legal support & conveyancing',
  family: 'Legal & professional',
  tier_emphasis: 'critical',
  entry_offer: 'policy_audit',
  lead_with: 'policy',
  privacy_line: 'Matter detail does not go into a free account. The difference between the free and paid terms is the whole question, and most staff have never read either.',
  privacy_src: 'Staff in most firms are already using AI, usually on a free tier, usually unreported. The principal\u2019s real question is how exposed the firm is.',
  risk_boundary: 'Nothing that becomes advice to a client. Court and regulator guidance on generative AI moves quickly and differs by jurisdiction, so current practice notes are checked before anything is taught.',
  sinks: [
    { id:'l1', label:'Summarising a long contract or document bundle', tool:'claude', mods:['long-documents'] },
    { id:'l2', label:'Client update letters and matter status emails', tool:'chatgpt', mods:['reusable-setups','useful-output'] },
    { id:'l3', label:'Precedent and template tidy-ups', tool:'claude', mods:['reusable-setups'] },
    { id:'l4', label:'File notes and attendance notes', tool:'claude', mods:['useful-output'] },
    { id:'l5', label:'Searches, settlement and checklist admin', tool:'claude', mods:['reusable-setups'] },
    { id:'l6', label:'Anything that becomes advice to a client', tool:'neither', mods:['what-never-goes-in','team-ai-policy'] }
  ]
},

'ndis-providers': {
  name: 'NDIS & disability providers',
  family: 'Health & care',
  tier_emphasis: 'critical',
  entry_offer: 'documentation',
  lead_with: 'policy',
  privacy_line: 'Participant detail stays out until the tool, the tier and the written rule are all settled — and the rule has to hold across a large casual workforce, not just the office.',
  privacy_src: 'The audit is the lever. Providers spend on audit-readiness far faster than on efficiency.',
  risk_boundary: 'No clinical content, no decisions about a participant\u2019s supports or funding. Documentation quality and consistency is the work. NDIS Practice Standards are revised periodically and the current version is confirmed before anything is taught.',
  sinks: [
    { id:'n1', label:'Progress notes worked up into reports', tool:'claude', mods:['long-documents','what-never-goes-in'] },
    { id:'n2', label:'Service agreements and plan documents', tool:'claude', mods:['reusable-setups'] },
    { id:'n3', label:'Audit evidence and policy documents', tool:'claude', mods:['long-documents','reusable-setups'] },
    { id:'n4', label:'Rostering messages and family communication', tool:'chatgpt', mods:['reusable-setups'] },
    { id:'n5', label:'Position descriptions, induction and training material', tool:'chatgpt', mods:['useful-output'] },
    { id:'n6', label:'Incident detail and participant records', tool:'neither', mods:['what-never-goes-in','team-ai-policy'] }
  ]
},

'trades': {
  name: 'Trades & field services',
  family: 'Trades & field services',
  tier_emphasis: 'low',
  entry_offer: 'workflow_build',
  lead_with: 'work',
  privacy_line: 'Customer names and addresses can stay out of it. A quote does not need them to be written in four minutes instead of forty.',
  privacy_src: 'Nobody in the trades is searching for AI training. The work is same-day quoting and follow-up, with the tool as the method.',
  risk_boundary: 'Certification, compliance sign-off and safety determinations stay with the licensed person. The training covers the writing and the chasing.',
  sinks: [
    { id:'t1', label:'Getting a quote out the same day as the site visit', tool:'chatgpt', mods:['reusable-setups','useful-output'] },
    { id:'t2', label:'Following up quotes that went quiet', tool:'chatgpt', mods:['reusable-setups'] },
    { id:'t3', label:'Job notes and variation write-ups', tool:'chatgpt', mods:['useful-output'] },
    { id:'t4', label:'Reading a spec, plan set or scope document', tool:'claude', mods:['long-documents'] },
    { id:'t5', label:'Invoices, reminders and chasing payment', tool:'chatgpt', mods:['reusable-setups'] },
    { id:'t6', label:'Review replies, website text and ads', tool:'chatgpt', mods:['useful-output'] },
    { id:'t7', label:'Safety and compliance paperwork', tool:'claude', mods:['reusable-setups','what-never-goes-in'] }
  ]
},

'other': {
  name: 'Something else',
  family: 'Not yet published',
  tier_emphasis: 'moderate',
  entry_offer: 'workshop',
  lead_with: 'work',
  privacy_line: 'Identifiable records about the people you serve stay out of the tool until there is a written rule covering which tool and which tier.',
  privacy_src: '',
  risk_boundary: 'Where a wrong output is a regulated harm rather than an inconvenience, that work stays with the qualified person. The line gets drawn explicitly for your industry before anything is taught.',
  sinks: [
    { id:'o1', label:'Drafting the same kinds of emails and letters repeatedly', tool:'chatgpt', mods:['useful-output','reusable-setups'] },
    { id:'o2', label:'Reading documents too long to read twice', tool:'claude', mods:['long-documents'] },
    { id:'o3', label:'Turning messy notes or data into something structured', tool:'claude', mods:['long-documents','useful-output'] },
    { id:'o4', label:'Client and customer communication', tool:'chatgpt', mods:['reusable-setups'] },
    { id:'o5', label:'Internal documents, policies and process notes', tool:'claude', mods:['reusable-setups'] },
    { id:'o6', label:'Knowing when not to use it at all', tool:'neither', mods:['what-never-goes-in','team-ai-policy'] }
  ]
}

};

/* Offer definitions. Open decision 1 — the shape is assumed, not
   pinned. Change the copy here and the whole tool follows. */
var OFFERS = {
  policy_audit: {
    verdict: 'Start with the policy, not the training',
    href: '/services/policy-and-audit/',
    body: 'Your team is already using these tools and there is no written rule covering it. Training first means training people to do faster what you have not yet decided they can do at all. A short audit and a policy in your words comes first; the workshop lands properly once it exists.'
  },
  policy_session: {
    verdict: 'Start with the privacy line, then train',
    href: '/services/policy-and-audit/',
    body: 'The records you hold make this a privacy question before a productivity one. One session settles which tool, which tier and which records — then the team training has something solid to stand on.'
  },
  documentation: {
    verdict: 'Start where the audit will look',
    href: '/services/policy-and-audit/',
    body: 'Documentation is both the biggest time sink and the thing an auditor reads. A documentation and policy engagement covers both at once, which is why it comes before general team training.'
  },
  workshop: {
    verdict: 'Start with a half-day workshop',
    href: '/services/team-workshop/',
    body: 'Nothing in your answers needs fixing before the team can learn this properly. A half-day on your own work, with the setups built in the room, gets the whole team to the same standard in one go.'
  },
  workflow_build: {
    verdict: 'Start with one workflow, built with you',
    href: '/services/workflow-build/',
    body: 'A classroom is the wrong shape for this. We take the one job that costs you the most time, build it with you until it works on a real job, and leave you with something running rather than notes.'
  }
};

/* ============================================================
   ENGINE
   ============================================================ */
(function(){
  'use strict';

  var card = document.getElementById('card');
  var state = { industry:null, side:null, role:null, size:null, use:null, policy:null, sinks:[], data:[], goal:null, when:null };
  var step = 0;
  var plan = null;

  function esc(s){
    return String(s).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;').replace(/"/g,'&quot;');
  }
  function pack(){ return PACKS[state.industry] || PACKS.other; }

  function sinkList(){
    var p = pack(), out = [];
    for (var i=0;i<p.sinks.length;i++){
      var s = p.sinks[i];
      if (!s.side || state.side === 'both' || s.side === state.side) out.push(s);
    }
    return out;
  }

  /* ---------- Question definitions ---------- */
  var QUESTIONS = [
    {
      key:'industry', type:'single',
      q:'What kind of business is this for?',
      help:'Pick the closest fit. If nothing here matches, the last option still produces a plan — the foundations are the same, only the examples change.',
      options:function(){
        var ids = ['accounting-bookkeeping','real-estate','allied-health','legal-conveyancing','ndis-providers','trades','other'], out = [];
        for (var i=0;i<ids.length;i++) out.push({ id:ids[i], label:PACKS[ids[i]].name });
        return out;
      }
    },
    {
      key:'side', type:'single',
      when:function(){ return !!pack().split; },
      q:function(){ return pack().split.question; },
      help:function(){ return pack().split.help; },
      options:function(){ return pack().split.options; }
    },
    {
      key:'role', type:'single',
      q:'What is your role?',
      help:'This changes who the plan is written to, not what is in it.',
      options:[
        { id:'owner', label:'Owner, principal or partner' },
        { id:'manager', label:'Practice, office or operations manager' },
        { id:'lead', label:'Team lead — I would need sign-off' },
        { id:'staff', label:'Staff — I want to bring this to someone' }
      ]
    },
    {
      key:'size', type:'single',
      q:'How many people would need to know this?',
      help:'Including casuals, contractors and anyone who touches client work.',
      options:[
        { id:'1', label:'Just me' },
        { id:'2-5', label:'2 to 5' },
        { id:'6-15', label:'6 to 15' },
        { id:'16-40', label:'16 to 40' },
        { id:'40+', label:'More than 40' }
      ]
    },
    {
      key:'use', type:'single',
      q:'What is happening with these tools in your business right now?',
      help:'Answer this one honestly rather than tidily. It changes the recommendation more than any other question here.',
      options:[
        { id:'none', label:'Nobody is using anything', note:'As far as you know' },
        { id:'unofficial', label:'A few people are, unofficially' },
        { id:'free', label:'Most of us are, on free accounts' },
        { id:'paid', label:'We pay for business accounts' },
        { id:'managed', label:'We pay, and there is a written rule' }
      ]
    },
    {
      key:'policy', type:'single',
      q:'Is there a written rule about what can be pasted into one of these tools?',
      help:'Written down somewhere findable, not said once in a meeting.',
      options:[
        { id:'yes', label:'Yes, and the team has read it' },
        { id:'partial', label:'Something exists but I doubt anyone has read it' },
        { id:'no', label:'No' },
        { id:'unsure', label:"I don't know" }
      ]
    },
    {
      key:'sinks', type:'multi', min:1,
      q:'Which of these actually cost you time?',
      help:'Pick as many as apply. The plan is ordered by what you choose here, so choose the ones you would notice disappearing.',
      options:function(){
        var l = sinkList(), out = [];
        for (var i=0;i<l.length;i++) out.push({ id:l[i].id, label:l[i].label });
        return out;
      }
    },
    {
      key:'data', type:'multi',
      q:'Which of these does your business hold?',
      help:'This sets how hard the free-versus-paid tier question lands for you.',
      options:[
        { id:'financial', label:'Client financial records' },
        { id:'health', label:'Health or clinical records' },
        { id:'identity', label:'Identity documents' },
        { id:'legal', label:'Court or legal documents' },
        { id:'support', label:'Participant or support notes' },
        { id:'staff', label:'Staff and payroll records' },
        { id:'none', label:'None of these', exclusive:true }
      ]
    },
    {
      key:'goal', type:'single',
      q:'What would make this worth doing?',
      help:'One answer. The honest one is more useful than the complete one.',
      options:[
        { id:'consistency', label:'Get the whole team to the same standard' },
        { id:'risk', label:'Stop worrying about what people are pasting in' },
        { id:'speed', label:'Make one specific job much faster' },
        { id:'decide', label:'Work out what we should be paying for' }
      ]
    },
    {
      key:'when', type:'single',
      q:'When would you want this done?',
      help:'',
      options:[
        { id:'now', label:'This month' },
        { id:'quarter', label:'This quarter' },
        { id:'later', label:'Just working out what it involves' }
      ]
    }
  ];

  function active(){
    var out = [];
    for (var i=0;i<QUESTIONS.length;i++){
      var q = QUESTIONS[i];
      if (!q.when || q.when()) out.push(q);
    }
    return out;
  }
  function val(v){ return typeof v === 'function' ? v() : v; }

  /* ---------- Scoring ----------
     Every input is the user's own answer. Nothing is modelled,
     benchmarked or estimated. The bands are a reading of what
     they told us, not a prediction. */
  var USE_RISK    = { none:2,  unofficial:34, free:30, paid:12, managed:4 };
  var POLICY_RISK = { yes:0,   partial:14,    no:25,   unsure:20 };
  var SIZE_RISK   = { '1':0,   '2-5':4,       '6-15':8,'16-40':12, '40+':16 };
  var TIER_RISK   = { critical:12, high:7, moderate:3, low:0 };

  function score(){
    var p = pack();
    var dataCount = 0;
    for (var i=0;i<state.data.length;i++) if (state.data[i] !== 'none') dataCount++;

    var exposure =
      (USE_RISK[state.use] || 0) +
      (POLICY_RISK[state.policy] || 0) +
      Math.min(dataCount * 7, 28) +
      (SIZE_RISK[state.size] || 0) +
      (TIER_RISK[p.tier_emphasis] || 0);
    exposure = Math.max(0, Math.min(100, exposure));

    var band = exposure >= 55 ? 'attention' : (exposure >= 30 ? 'tighten' : 'low');

    /* Reasons are written from the specific answers, so the reading
       is auditable by the person reading it. */
    var reasons = [];
    if (state.use === 'unofficial') reasons.push('Unofficial use is the hardest kind to manage. You cannot set a rule for something you are not meant to know is happening.');
    if (state.use === 'free') reasons.push('Free-tier accounts across the team is the single biggest item here. The paid terms are the difference, and that is a purchasing decision rather than a training one.');
    if (state.use === 'none') reasons.push('Nothing in use yet, which means you get to set the rule before the habit — much cheaper than correcting it later.');
    if (state.use === 'paid' && state.policy !== 'yes') reasons.push('Paid accounts cover the vendor side. Without a written rule they do not cover the human side, which is where the mistakes happen.');
    if (state.policy === 'no' || state.policy === 'unsure') reasons.push('No written rule the team can point to. This is the cheapest thing on the list to fix and the one that changes the answer most.');
    if (state.policy === 'partial') reasons.push('A document nobody has read is not a control. It is a document.');
    if (dataCount >= 3) reasons.push('You hold several categories of sensitive record, so which tool and which tier stops being a preference and becomes a decision.');
    else if (dataCount >= 1) reasons.push('The records you hold mean the tier question needs a definite answer rather than a default.');
    if (state.size === '16-40' || state.size === '40+') reasons.push('At your headcount the rule has to survive people who were not in the room when it was explained.');
    if (p.tier_emphasis === 'critical') reasons.push('In your industry being confidently wrong about data handling does real damage, so this is the part that gets covered first and properly.');

    /* Route to an offer. Policy-led verticals route earlier. */
    var threshold = p.lead_with === 'policy' ? 40 : 55;
    var offer;
    if (exposure >= threshold && p.entry_offer !== 'workflow_build') {
      offer = p.lead_with === 'policy' ? p.entry_offer : 'policy_audit';
      if (offer === 'workshop') offer = 'policy_audit';
    } else if (state.goal === 'risk' && exposure >= 30) {
      offer = p.lead_with === 'policy' ? p.entry_offer : 'policy_audit';
    } else if (state.goal === 'speed' || p.entry_offer === 'workflow_build') {
      offer = 'workflow_build';
    } else {
      offer = 'workshop';
    }

    /* Module ordering by how much of their own list each covers. */
    var chosen = [], all = sinkList();
    for (var j=0;j<all.length;j++) if (state.sinks.indexOf(all[j].id) > -1) chosen.push(all[j]);

    var tally = {};
    for (var k=0;k<chosen.length;k++){
      for (var m=0;m<chosen[k].mods.length;m++){
        var id = chosen[k].mods[m];
        if (!tally[id]) tally[id] = [];
        tally[id].push(chosen[k].label);
      }
    }
    /* Governance modules are always in the plan. */
    if (!tally['what-never-goes-in']) tally['what-never-goes-in'] = [];
    if (band !== 'low' && !tally['team-ai-policy']) tally['team-ai-policy'] = [];
    /* Tool choice is the differentiator; include it whenever both
       tools are in play across their selections. */
    var tools = {};
    for (var t=0;t<chosen.length;t++) tools[chosen[t].tool] = true;
    if ((tools.claude && tools.chatgpt) || state.goal === 'decide') {
      if (!tally['choosing-your-tool']) tally['choosing-your-tool'] = [];
    }

    var order = Object.keys(tally).sort(function(a,b){
      var d = tally[b].length - tally[a].length;
      if (d) return d;
      return Object.keys(SPINE).indexOf(a) - Object.keys(SPINE).indexOf(b);
    });
    /* Policy-first routes teach the rule before the technique. */
    if (offer !== 'workshop' && offer !== 'workflow_build') {
      order.sort(function(a,b){
        var gov = { 'what-never-goes-in':0, 'team-ai-policy':1 };
        var ga = a in gov ? gov[a] : 9, gb = b in gov ? gov[b] : 9;
        return ga - gb;
      });
    }

    var modules = [];
    for (var o=0;o<order.length;o++){
      var mid = order[o], sp = SPINE[mid];
      if (!sp) continue;
      modules.push({ id:mid, name:sp.name, href:sp.href, why:sp.why, covers:tally[mid] });
    }

    var byTool = { claude:[], chatgpt:[], neither:[] };
    for (var c=0;c<chosen.length;c++) byTool[chosen[c].tool].push(chosen[c].label);

    return { exposure:exposure, band:band, reasons:reasons, offer:offer, modules:modules, byTool:byTool, chosen:chosen };
  }

  /* ---------- Rendering ---------- */
  function renderQuestion(){
    var qs = active(), q = qs[step];
    var opts = val(q.options), help = val(q.help), text = val(q.q);
    var multi = q.type === 'multi';
    var chosen = multi ? state[q.key] : [state[q.key]];

    var h = '';
    h += '<div class="prog">';
    h += '<span class="prog-n">Question ' + (step+1) + ' of ' + qs.length + '</span>';
    h += '<span class="prog-rail"><span class="prog-fill" style="width:' + Math.round((step/qs.length)*100) + '%"></span></span>';
    h += '</div>';
    h += '<fieldset><legend>' + esc(text) + '</legend>';
    if (help) h += '<p class="q-help">' + esc(help) + '</p>';
    h += '<div class="opts">';
    for (var i=0;i<opts.length;i++){
      var o = opts[i], checked = chosen.indexOf(o.id) > -1;
      h += '<label class="opt"' + (multi ? ' data-multi' : '') + '>';
      h += '<input type="' + (multi ? 'checkbox' : 'radio') + '" name="' + esc(q.key) + '" value="' + esc(o.id) + '"' + (checked ? ' checked' : '') + (o.exclusive ? ' data-exclusive' : '') + '>';
      h += '<span>' + esc(o.label) + (o.note ? '<small>' + esc(o.note) + '</small>' : '') + '</span>';
      h += '</label>';
    }
    h += '</div></fieldset>';
    h += '<div class="actions">';
    h += '<button class="btn-primary" id="next"' + (multi && chosen.length < (q.min||0) ? ' disabled' : '') + '>' + (step === qs.length-1 ? 'Build my plan' : 'Next') + '</button>';
    if (step > 0) h += '<button class="btn-quiet" id="back">Back</button>';
    if (multi) h += '<span class="hint" id="count">' + chosen.length + ' selected</span>';
    h += '</div>';

    card.innerHTML = h;

    var inputs = card.querySelectorAll('input');
    for (var n=0;n<inputs.length;n++){
      inputs[n].addEventListener('change', function(e){
        if (multi){
          var ex = e.target.hasAttribute('data-exclusive');
          if (ex && e.target.checked){
            for (var x=0;x<inputs.length;x++) if (inputs[x] !== e.target) inputs[x].checked = false;
          } else if (!ex && e.target.checked){
            for (var y=0;y<inputs.length;y++) if (inputs[y].hasAttribute('data-exclusive')) inputs[y].checked = false;
          }
          var picked = [];
          for (var p2=0;p2<inputs.length;p2++) if (inputs[p2].checked) picked.push(inputs[p2].value);
          state[q.key] = picked;
          document.getElementById('count').textContent = picked.length + ' selected';
          document.getElementById('next').disabled = picked.length < (q.min||0);
        } else {
          state[q.key] = e.target.value;
          /* Changing industry invalidates downstream industry answers. */
          if (q.key === 'industry'){ state.side = null; state.sinks = []; }
        }
      });
    }

    var next = document.getElementById('next');
    next.addEventListener('click', function(){
      var old = card.querySelector('.err');
      if (old) old.parentNode.removeChild(old);
      if (!multi && !state[q.key]){ next.insertAdjacentHTML('afterend', '<span class="err" role="alert">Pick one to continue.</span>'); return; }
      step++;
      if (step >= active().length) renderPlan(); else renderQuestion();
      window.scrollTo({ top:0, behavior:'smooth' });
    });
    var back = document.getElementById('back');
    if (back) back.addEventListener('click', function(){ step--; renderQuestion(); });

    var first = card.querySelector('input');
    if (first && step > 0) first.focus();
  }

  var BANDS = {
    low:       { name:'Low',                lede:'Nothing here needs fixing before you can start training people properly.' },
    tighten:   { name:'Worth tightening',   lede:'Not alarming, but there are one or two gaps worth closing in the same engagement as the training.' },
    attention: { name:'Needs attention first', lede:'Based on what you have told us, the gap is in what is permitted rather than in what people can do. Training first would be training people to go faster in an undecided direction.' }
  };

  var AUDIENCE = {
    owner:   'Written for you — you sign this off.',
    manager: 'Written for you, with the budget conversation flagged where it comes up.',
    lead:    'Written so you can hand it to whoever signs off, without translating it first.',
    staff:   'Written so you can send it to whoever signs off. The recommendation speaks to them, not to you.'
  };

  function renderPlan(){
    plan = score();
    var p = pack();
    var offer = OFFERS[plan.offer];
    var b = BANDS[plan.band];
    var label = p.name + (state.side && state.side !== 'both' ? ' — ' + (state.side === 'pm' ? 'property management' : 'sales') : '');

    var h = '<div class="plan">';

    h += '<div class="verdict">';
    h += '<p class="verdict-for">' + esc(label) + ' &middot; ' + esc(AUDIENCE[state.role] || '') + '</p>';
    h += '<h2>' + esc(offer.verdict) + '</h2>';
    h += '<p>' + esc(offer.body) + '</p>';
    h += '</div>';

    /* Exposure reading */
    h += '<div class="blk"><h3>Where you are exposed right now</h3>';
    h += '<p class="blk-lede">' + esc(b.lede) + '</p>';
    h += '<div class="gauge"><div class="gauge-band"><span class="gauge-name">' + esc(b.name) + '</span></div>';
    h += '<div class="gauge-rail"><span class="gauge-fill" data-band="' + esc(plan.band) + '" style="width:' + plan.exposure + '%"></span></div></div>';
    h += '<ul class="reasons">';
    for (var r=0;r<plan.reasons.length;r++) h += '<li>' + esc(plan.reasons[r]) + '</li>';
    h += '</ul>';
    h += '<p class="blk-lede" style="margin-top:1.5rem">Every line above is drawn from an answer you gave. Nothing is estimated or benchmarked against anyone else.</p>';
    h += '</div>';

    /* The line */
    h += '<div class="blk"><h3>The line that does not move</h3>';
    h += '<div class="line"><p>' + esc(p.privacy_line) + '</p>';
    if (p.privacy_src) h += '<p class="line-src">' + esc(p.privacy_src) + '</p>';
    h += '</div></div>';

    /* Modules */
    h += '<div class="blk"><h3>Your training plan, in this order</h3>';
    h += '<p class="blk-lede">The same foundations everyone learns, ordered by how much of your list each one covers. The industry track sits on top of these.</p>';
    h += '<ol class="mods">';
    for (var m=0;m<plan.modules.length;m++){
      var mod = plan.modules[m];
      h += '<li><span><span class="mod-name"><a href="' + esc(mod.href) + '">' + esc(mod.name) + '</a></span>';
      if (mod.covers.length){
        h += '<span class="mod-why">Covers ' + mod.covers.length + ' of the jobs you picked: ' + esc(mod.covers.slice(0,2).join('; ')) + (mod.covers.length > 2 ? ', and more.' : '.') + '</span>';
      } else {
        h += '<span class="mod-why">' + esc(mod.why) + '</span>';
      }
      h += '</span></li>';
    }
    h += '</ol></div>';

    /* Tool split */
    if (plan.chosen.length){
      h += '<div class="blk"><h3>Which tool, for which of your jobs</h3>';
      h += '<p class="blk-lede">Two tools taught side by side, because the skill transfers and the interface does not. This split is a starting rule of thumb, not a rule.</p>';
      h += '<div class="tools">';
      if (plan.byTool.claude.length){
        h += '<div class="tool"><p class="tool-sub">Reach for Claude</p><h4>Long documents and sustained drafting</h4><ul>';
        for (var c1=0;c1<plan.byTool.claude.length;c1++) h += '<li>' + esc(plan.byTool.claude[c1]) + '</li>';
        h += '</ul></div>';
      }
      if (plan.byTool.chatgpt.length){
        h += '<div class="tool"><p class="tool-sub">Reach for ChatGPT</p><h4>Volume, speed and voice notes</h4><ul>';
        for (var c2=0;c2<plan.byTool.chatgpt.length;c2++) h += '<li>' + esc(plan.byTool.chatgpt[c2]) + '</li>';
        h += '</ul></div>';
      }
      if (plan.byTool.neither.length){
        h += '<div class="tool"><p class="tool-sub">Use neither</p><h4>Not until the rule is written</h4><ul>';
        for (var c3=0;c3<plan.byTool.neither.length;c3++) h += '<li>' + esc(plan.byTool.neither[c3]) + '</li>';
        h += '</ul></div>';
      }
      h += '</div></div>';
    }

    /* Boundary */
    h += '<div class="blk"><h3>What this training will not do</h3>';
    h += '<p class="bound">' + esc(p.risk_boundary) + '</p></div>';

    /* Handoff. The enquiry form is the only conversion action on the site, so
       the plan is never traded for an address — it walks across to the form. */
    h += '<div class="capture" id="capture">';
    h += '<h3>Take this plan to a conversation</h3>';
    h += '<p>The plan above is yours either way — print it, or leave the tab open. If you send an enquiry from here, a summary of your answers travels with you into the form, so the first conversation starts from your week rather than from scratch.</p>';
    h += '<div class="actions"><a class="btn-primary" id="handoff" href="/contact/">Start an enquiry</a>';
    h += '<a class="btn-quiet" href="' + esc(offer.href) + '">Read what this involves</a>';
    h += '<button class="btn-quiet" id="print">Print it instead</button></div>';
    h += '<p class="capture-note">No email address is asked for here, and nothing is sent anywhere until you fill in the form yourself. The summary is held in this browser tab only.</p>';
    h += '</div>';

    h += '<div class="actions"><button class="btn-quiet" id="restart">Start again with different answers</button></div>';
    h += '</div>';

    card.innerHTML = h;
    document.getElementById('intro').style.display = 'none';

    document.getElementById('print').addEventListener('click', function(){ window.print(); });
    document.getElementById('restart').addEventListener('click', function(){
      state = { industry:null, side:null, role:null, size:null, use:null, policy:null, sinks:[], data:[], goal:null, when:null };
      step = 0;
      document.getElementById('intro').style.display = '';
      renderQuestion();
      window.scrollTo({ top:0, behavior:'smooth' });
    });
    var handoff = document.getElementById('handoff');
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
      sessionStorage.setItem('aiw_plan', lines.join('\n'));
    } catch (e) { /* private browsing: the form still works, just unprefilled */ }
  }


  renderQuestion();
})();
