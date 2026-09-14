#!/usr/bin/env python3
"""Build blog HTML pages from blog/*.md.

Usage: python tools/build_blog.py
Writes blog/index.html and one HTML file per post in blog/.
Design tokens intentionally mirror index.html so the pages feel native.
"""
import html
import os
import re

DOMAIN = "https://thescalpersedge.com"
TWITTER = "https://x.com/scalpersedge"

# (source md, output slug, title, dek, date, post number)
POSTS = [
    ("001-why-scalpers-skip-journaling.md", "001-why-scalpers-skip-journaling",
     "Why 90% of Scalpers Skip Journaling (And Lose Money Because of It)",
     "The one tool that separates consistent traders from hopeful gamblers — and why most people never use it.",
     "2026-09-06", 1),
    ("002-pre-trade-checklist.md", "002-pre-trade-checklist",
     "The Pre-Trade Checklist That Saved My Account (Free Download)",
     "The 12-point checklist that eliminated my bad entries and doubled my win rate in 3 weeks. Free Notion template inside.",
     "2026-09-06", 2),
    ("003-r-multiples-explained.md", "003-r-multiples-explained",
     "R-Multiples Explained: The Only Metric That Matters for Scalpers",
     "Stop obsessing over win rate. Start tracking R-multiples — the metric that predicts whether you'll be profitable.",
     "2026-09-06", 3),
    ("004-revenge-trading.md", "004-revenge-trading",
     "How to Stop Revenge Trading After a Bad Loss",
     "The psychology problem that costs scalpers more money than any strategy mistake — and the simple rule that fixed it.",
     "2026-09-06", 4),
    ("005-wash-sales-day-traders.md", "005-wash-sales-day-traders",
     "Wash Sales & Day Traders: What You Need to Know for Tax Season",
     "That \"free\" wash sale you triggered by rebuying at 9:45AM just cost you $400 in deductions. Here's how to track it.",
     "2026-09-06", 5),
    ("006-scalping-psychology-10am.md", "006-scalping-psychology-10am",
     "Scalping Psychology: Why You Keep Taking Losses at 10 AM",
     "It's not the strategy. It's your brain. Why 10AM is the danger zone for scalpers — and what to do about it.",
     "2026-09-06", 6),
    ("007-spread-costs-killing-profitability.md", "007-spread-costs-killing-profitability",
     "Spread Costs Are Killing Your Profitability — Here's How to Track Them",
     "You're tracking P&L and win rate, but missing the single biggest drain on your account.",
     "2026-09-06", 7),
    ("008-first-year-scalping.md", "008-first-year-scalping",
     "From $500 to Consistent: My First Year of Scalping (And What I Wish I Knew Day 1)",
     "I turned $500 into a consistent scalper in 12 months. Not because I'm smart — because I failed enough times to learn.",
     "2026-09-06", 8),
]

CSS = """
    :root {
      --bg: #fafafa; --surface: #ffffff; --surface-2: #f5f5f5; --surface-3: #eeeeee;
      --text: #111111; --text-secondary: #555555; --text-tertiary: #999999;
      --border: #e5e5e5; --border-strong: #d4d4d4;
      --accent: #111111; --accent-hover: #333333;
      --green: #16a34a; --green-bg: #f0fdf4; --green-border: #bbf7d0;
      --red: #dc2626;
    }
    * { margin: 0; padding: 0; box-sizing: border-box; }
    html { scroll-behavior: smooth; }
    body {
      font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
      background: var(--bg); color: var(--text); line-height: 1.6;
      -webkit-font-smoothing: antialiased; overflow-x: hidden;
    }
    nav {
      position: fixed; top: 0; left: 0; right: 0; z-index: 100;
      padding: 0 2rem; height: 60px; display: flex; align-items: center;
      justify-content: space-between; background: rgba(250,250,250,0.85);
      backdrop-filter: blur(20px); -webkit-backdrop-filter: blur(20px);
      border-bottom: 1px solid var(--border);
    }
    .nav-brand {
      display: flex; align-items: center; gap: 0.5rem; font-size: 0.85rem;
      font-weight: 700; letter-spacing: -0.01em; color: var(--text); text-decoration: none;
    }
    .nav-right { display: flex; align-items: center; gap: 1.75rem; }
    .nav-right a:not(.nav-cta) {
      color: var(--text-secondary); text-decoration: none; font-size: 0.85rem;
      font-weight: 500; transition: color 0.15s;
    }
    .nav-right a:not(.nav-cta):hover { color: var(--text); }
    .nav-cta {
      padding: 0.45rem 1.1rem; background: var(--accent); color: #ffffff;
      border-radius: 8px; font-weight: 600; font-size: 0.82rem;
      text-decoration: none; white-space: nowrap; transition: background 0.15s;
    }
    .nav-cta:hover { background: var(--accent-hover); }
    @media (max-width: 600px) { .nav-right a:not(.nav-cta) { display: none; } }

    .article {
      max-width: 680px; margin: 0 auto; padding: 7.5rem 1.5rem 4rem;
    }
    .post-number {
      font-size: 0.68rem; font-weight: 600; letter-spacing: 0.09em;
      text-transform: uppercase; color: var(--text-tertiary); margin-bottom: 1rem;
    }
    h1 {
      font-size: clamp(1.9rem, 5vw, 2.7rem); font-weight: 800;
      letter-spacing: -0.03em; line-height: 1.15; margin-bottom: 1rem;
    }
    .dek {
      font-size: 1.05rem; color: var(--text-secondary); line-height: 1.65;
      margin-bottom: 1.25rem;
    }
    .meta {
      font-size: 0.78rem; color: var(--text-tertiary); margin-bottom: 1rem;
      display: flex; gap: 0.6rem; align-items: center;
    }
    .meta .divider { width: 1px; height: 11px; background: var(--border-strong); }
    .meta a { color: var(--text-secondary); text-decoration: none; font-weight: 600; }
    .meta a:hover { text-decoration: underline; text-underline-offset: 3px; }

    .article-body { font-size: 1rem; color: #2a2a2a; }
    .article-body h2 {
      font-size: 1.45rem; font-weight: 800; letter-spacing: -0.025em;
      line-height: 1.25; margin: 2.75rem 0 0.9rem;
    }
    .article-body h3 {
      font-size: 1.12rem; font-weight: 700; letter-spacing: -0.02em;
      line-height: 1.3; margin: 2rem 0 0.7rem;
    }
    .article-body p { margin-bottom: 1.15rem; line-height: 1.75; }
    .article-body strong { color: var(--text); }
    .article-body a { color: var(--text); text-decoration: underline; text-underline-offset: 3px; text-decoration-color: var(--border-strong); }
    .article-body a:hover { text-decoration-color: var(--text); }
    .article-body hr {
      border: none; height: 1px; background: var(--border);
      margin: 2.5rem auto; width: 100%;
    }
    .article-body pre {
      background: #111111; color: #e8e8e8; border-radius: 12px;
      padding: 1.1rem 1.25rem; overflow-x: auto; margin: 1.5rem 0;
      font-family: 'JetBrains Mono', 'SF Mono', Consolas, monospace;
      font-size: 0.84rem; line-height: 1.6;
    }
    .article-body code {
      font-family: 'JetBrains Mono', 'SF Mono', Consolas, monospace;
      font-size: 0.86em; background: var(--surface-2);
      border: 1px solid var(--border); border-radius: 5px; padding: 0.1rem 0.35rem;
    }
    .article-body pre code { background: none; border: none; padding: 0; font-size: inherit; }
    .article-body ul, .article-body ol { margin: 0 0 1.15rem 1.4rem; }
    .article-body li { margin-bottom: 0.4rem; line-height: 1.65; }
    .article-body table {
      width: 100%; border-collapse: collapse; margin: 1.5rem 0;
      font-size: 0.88rem;
    }
    .article-body th {
      text-align: left; font-size: 0.66rem; font-weight: 600;
      letter-spacing: 0.06em; text-transform: uppercase; color: var(--text-tertiary);
      padding: 0.55rem 0.75rem; border-bottom: 2px solid var(--border-strong);
    }
    .article-body td {
      padding: 0.55rem 0.75rem; border-bottom: 1px solid var(--border);
      color: var(--text-secondary);
    }
    .article-body tr:last-child td { border-bottom: none; }
    .ps-marker { background: var(--green-bg); color: var(--green); border: 1px solid var(--green-border); border-radius: 4px; padding: 0 0.3rem; font-weight: 700; font-size: 0.8em; }
    .about-box {
      border: 1px solid var(--border); background: var(--surface-2);
      border-radius: 14px; padding: 1.25rem 1.4rem; margin: 2.5rem 0 0;
    }
    .about-box p { font-size: 0.85rem; color: var(--text-secondary); margin: 0; line-height: 1.65; }
    .about-box strong { color: var(--text); }

    .prevnext {
      max-width: 680px; margin: 0 auto; padding: 0 1.5rem 4rem;
      display: grid; grid-template-columns: 1fr 1fr; gap: 1rem;
    }
    .pn-card {
      border: 1px solid var(--border); border-radius: 14px; padding: 1.1rem 1.25rem;
      text-decoration: none; background: var(--surface);
      transition: border-color 0.15s, box-shadow 0.15s;
    }
    .pn-card:hover { border-color: var(--border-strong); box-shadow: 0 2px 8px rgba(0,0,0,0.05); }
    .pn-card.next { text-align: right; }
    .pn-label { font-size: 0.66rem; font-weight: 600; letter-spacing: 0.08em; text-transform: uppercase; color: var(--text-tertiary); margin-bottom: 0.35rem; }
    .pn-title { font-size: 0.88rem; font-weight: 600; color: var(--text); line-height: 1.4; }
    .pn-spacer { visibility: hidden; }
    @media (max-width: 600px) { .prevnext { grid-template-columns: 1fr; } .pn-card.next { text-align: left; } .pn-spacer { display: none; } }

    .email-mini {
      max-width: 680px; margin: 0 auto; padding: 0 1.5rem 5rem;
    }
    .email-mini-inner {
      background: var(--surface-2); border: 1px solid var(--border);
      border-radius: 16px; padding: 2rem 1.75rem; text-align: center;
    }
    .email-mini-inner h3 { font-size: 1.15rem; font-weight: 800; letter-spacing: -0.02em; margin-bottom: 0.4rem; }
    .email-mini-inner > p { font-size: 0.86rem; color: var(--text-secondary); margin-bottom: 1.25rem; line-height: 1.6; }
    .email-form { display: flex; gap: 0.5rem; max-width: 380px; margin: 0 auto; }
    .email-input {
      flex: 1; padding: 0.7rem 0.9rem; background: var(--surface);
      border: 1px solid var(--border); border-radius: 10px; color: var(--text);
      font-size: 0.86rem; outline: none; min-width: 0; font-family: inherit;
      transition: border-color 0.15s, box-shadow 0.15s;
    }
    .email-input:focus { border-color: var(--text); box-shadow: 0 0 0 3px rgba(0,0,0,0.06); }
    .email-submit {
      padding: 0.7rem 1.2rem; background: var(--accent); color: #fff; border: none;
      border-radius: 10px; font-size: 0.86rem; font-weight: 600; cursor: pointer;
      white-space: nowrap; min-width: 110px; position: relative; font-family: inherit;
      transition: background 0.15s;
    }
    .email-submit:hover { background: var(--accent-hover); }
    .email-submit.loading { pointer-events: none; }
    .email-submit .btn-text { transition: opacity 0.15s; }
    .email-submit.loading .btn-text { opacity: 0; }
    .email-submit .spinner {
      position: absolute; top: 50%; left: 50%; transform: translate(-50%,-50%);
      width: 14px; height: 14px; border: 2px solid rgba(255,255,255,0.25);
      border-top-color: #fff; border-radius: 50%; opacity: 0;
      animation: spin 0.6s linear infinite; transition: opacity 0.15s;
    }
    .email-submit.loading .spinner { opacity: 1; }
    @keyframes spin { to { transform: translate(-50%,-50%) rotate(360deg); } }
    .email-success {
      display: none; align-items: center; justify-content: center; gap: 0.5rem;
      color: var(--green); font-weight: 600; font-size: 0.9rem; padding: 0.5rem;
    }
    .email-error { display: none; color: var(--red); font-size: 0.78rem; margin-top: 0.6rem; }
    @media (max-width: 600px) { .email-form { flex-direction: column; } .email-submit { width: 100%; } }

    footer {
      padding: 2.5rem 2rem; text-align: center; border-top: 1px solid var(--border);
      color: var(--text-secondary); font-size: 0.82rem;
    }
    footer a { color: var(--text); text-decoration: none; font-weight: 500; }
    footer a:hover { text-decoration: underline; text-underline-offset: 3px; }
    .footer-links { display: flex; justify-content: center; gap: 1.75rem; margin-bottom: 1rem; flex-wrap: wrap; }

    @keyframes fadeUp { from { opacity: 0; transform: translateY(16px); } to { opacity: 1; transform: translateY(0); } }
    .post-number { animation: fadeUp 0.5s ease 0.05s both; }
    h1 { animation: fadeUp 0.5s ease 0.1s both; }
    .dek { animation: fadeUp 0.5s ease 0.16s both; }
    .meta { animation: fadeUp 0.5s ease 0.22s both; }
"""

BLOG_INDEX_CSS = CSS + """
    .blog-head { max-width: 720px; margin: 0 auto; padding: 7.5rem 1.5rem 2.5rem; }
    .blog-head .section-label {
      font-size: 0.68rem; font-weight: 600; letter-spacing: 0.09em;
      text-transform: uppercase; color: var(--text-tertiary); margin-bottom: 0.75rem;
      animation: fadeUp 0.5s ease 0.05s both;
    }
    .blog-head h1 { margin-bottom: 0.75rem; }
    .blog-head p { color: var(--text-secondary); font-size: 1rem; line-height: 1.65; max-width: 560px; }
    .post-list { max-width: 720px; margin: 0 auto; padding: 0 1.5rem 5rem; display: grid; gap: 0.9rem; }
    .post-card {
      display: block; background: var(--surface); border: 1px solid var(--border);
      border-radius: 14px; padding: 1.3rem 1.5rem; text-decoration: none;
      transition: border-color 0.15s, box-shadow 0.15s, transform 0.15s;
    }
    .post-card:hover { border-color: var(--border-strong); box-shadow: 0 2px 10px rgba(0,0,0,0.05); transform: translateY(-1px); }
    .post-card .num { font-size: 0.64rem; font-weight: 600; letter-spacing: 0.08em; text-transform: uppercase; color: var(--text-tertiary); margin-bottom: 0.4rem; }
    .post-card h2 { font-size: 1.05rem; font-weight: 700; letter-spacing: -0.015em; line-height: 1.35; margin-bottom: 0.35rem; color: var(--text); }
    .post-card p { font-size: 0.84rem; color: var(--text-secondary); line-height: 1.6; margin-bottom: 0.5rem; }
    .post-card .read { font-size: 0.76rem; font-weight: 600; color: var(--text); }
"""


def esc(t: str) -> str:
    return html.escape(t, quote=True)


def inline(text: str) -> str:
    s = esc(text)
    s = re.sub(r'\[([^\]]+)\]\(([^)\s]+)\)',
               lambda m: f'<a href="{m.group(2)}">{m.group(1)}</a>', s)
    s = re.sub(r'\*\*([^*]+)\*\*', r'<strong>\1</strong>', s)
    s = re.sub(r'(?<!\w)\*([^*\n]+)\*(?!\w)', r'<em>\1</em>', s)
    s = re.sub(r'(?<!\w)(P\.P\.S\.|P\.S\.)(?=[\s<])', r'<span class="ps-marker">\1</span>', s)
    return s


def md_to_html(md: str) -> str:
    lines = md.split('\n')
    out, para, in_code, code_buf, list_type = [], [], False, [], None

    def flush_para():
        if para:
            out.append(f'<p>{inline(" ".join(para))}</p>')
            para.clear()

    def close_list():
        nonlocal list_type
        if list_type:
            out.append(f'</{list_type}>')
            list_type = None

    i = 0
    while i < len(lines):
        line = lines[i]

        if line.strip().startswith('```'):
            flush_para(); close_list()
            if in_code:
                out.append(f'<pre><code>{esc("\n".join(code_buf))}</code></pre>')
                code_buf, in_code = [], False
            else:
                in_code = True
            i += 1
            continue
        if in_code:
            code_buf.append(line)
            i += 1
            continue

        stripped = line.strip()
        next_stripped = lines[i + 1].strip() if i + 1 < len(lines) else ''

        if stripped.startswith('|') and re.match(r'^\|[\s:|-]+\|$', next_stripped):
            flush_para(); close_list()
            header = [c.strip() for c in stripped.strip('|').split('|')]
            i += 2
            rows = []
            while i < len(lines) and lines[i].strip().startswith('|'):
                rows.append([c.strip() for c in lines[i].strip().strip('|').split('|')])
                i += 1
            t = ['<table>', '<thead><tr>']
            t += [f'<th>{inline(c)}</th>' for c in header]
            t.append('</tr></thead><tbody>')
            for r in rows:
                t.append('<tr>' + ''.join(f'<td>{inline(c)}</td>' for c in r) + '</tr>')
            t.append('</tbody></table>')
            out.append(''.join(t))
            continue

        if re.match(r'^-{3,}$', stripped):
            flush_para(); close_list()
            out.append('<hr>')
            i += 1
            continue
        if stripped.startswith('### '):
            flush_para(); close_list()
            out.append(f'<h3>{inline(stripped[4:])}</h3>')
            i += 1
            continue
        if stripped.startswith('## '):
            flush_para(); close_list()
            out.append(f'<h2>{inline(stripped[3:])}</h2>')
            i += 1
            continue
        if stripped.startswith('# '):
            i += 1
            continue  # post title rendered separately
        if re.match(r'^\d+\.\s', stripped):
            flush_para()
            if list_type != 'ol':
                close_list()
                out.append('<ol>')
                list_type = 'ol'
            out.append(f'<li>{inline(re.sub(r"^\\d+\\.\\s", "", stripped))}</li>')
            i += 1
            continue
        if stripped.startswith('- '):
            flush_para()
            if list_type != 'ul':
                close_list()
                out.append('<ul>')
                list_type = 'ul'
            out.append(f'<li>{inline(stripped[2:])}</li>')
            i += 1
            continue
        if not stripped:
            flush_para(); close_list()
            i += 1
            continue

        if list_type:
            close_list()
        para.append(stripped)
        i += 1

    flush_para(); close_list()
    if in_code and code_buf:
        out.append(f'<pre><code>{esc("\n".join(code_buf))}</code></pre>')
    return '\n'.join(out)


def split_about(md: str):
    idx = md.find('*About the author:')
    if idx == -1:
        return md, ''
    body = md[:idx]
    about_line = md[idx:].strip().strip('*').replace('*', '').strip()
    return body, about_line


def jsonld_post(slug, title, dek, date):
    import json
    data = {
        "@context": "https://schema.org",
        "@type": "BlogPosting",
        "headline": title,
        "description": dek,
        "url": f"{DOMAIN}/blog/{slug}",
        "datePublished": date,
        "author": {"@type": "Person", "name": "The Scalper's Edge"},
        "publisher": {"@type": "Organization", "name": "The Scalper's Edge", "url": DOMAIN},
        "mainEntityOfPage": f"{DOMAIN}/blog/{slug}",
    }
    payload = json.dumps(data, ensure_ascii=False, indent=2)
    # payload already includes its own outer { } braces, so no extra wrapping needed.
    return f'  <script type="application/ld+json">\n  {payload}\n  </script>'


EMAIL_MINI = '''
    <!-- Email capture (Netlify Forms) -->
    <div class="email-mini">
      <div class="email-mini-inner">
        <h3>Not ready to buy? Grab the free lite.</h3>
        <p>Daily trade log + R-multiple calculator. No credit card. The Notion link lands in your inbox instantly.</p>
        <div id="emailFormWrap">
          <div class="email-form">
            <input type="email" class="email-input" id="emailInput" placeholder="your@email.com" autocomplete="email">
            <button class="email-submit" id="emailSubmit" type="button" onclick="handleEmailSubmit()">
              <span class="btn-text">Send it free</span>
              <span class="spinner"></span>
            </button>
          </div>
          <p class="email-error" id="emailError">Something went wrong — try again, or DM <a href="TWITTER_URL" style="color:inherit;">@scalpersedge</a>.</p>
          <p style="margin-top:0.7rem;font-size:0.7rem;color:var(--text-tertiary);">No spam. Unsubscribe any time.</p>
        </div>
        <div class="email-success" id="emailSuccess">
          <span style="font-size:1.05rem;">✓</span>
          <span>Check your inbox — template link is on its way.</span>
        </div>
      </div>
    </div>
'''.replace('TWITTER_URL', TWITTER)

EMAIL_MINI_JS = '''
    // ─── Email capture (Netlify Forms) ───
    let emailSubmitting = false;

    async function handleEmailSubmit() {
      const input    = document.getElementById('emailInput');
      const btn      = document.getElementById('emailSubmit');
      const formWrap = document.getElementById('emailFormWrap');
      const success  = document.getElementById('emailSuccess');
      const errorEl  = document.getElementById('emailError');

      if (!input || !btn || !formWrap || !success || emailSubmitting) return;

      const email = input.value.trim();
      if (!email || !/^[^\\s@]+@[^\\s@]+\\.[^\\s@]+$/.test(email)) {
        input.focus();
        input.style.borderColor = 'var(--red)';
        setTimeout(() => { input.style.borderColor = ''; }, 1500);
        return;
      }

      emailSubmitting = true;
      btn.classList.add('loading');
      if (errorEl) errorEl.style.display = 'none';

      try {
        const res = await fetch('/', {
          method: 'POST',
          headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
          body: new URLSearchParams({ 'form-name': 'free-lite', email }).toString()
        });
        if (!res.ok) throw new Error('Submission failed');
        formWrap.style.display = 'none';
        success.style.display = 'flex';
      } catch (err) {
        if (errorEl) errorEl.style.display = 'block';
      } finally {
        emailSubmitting = false;
        btn.classList.remove('loading');
      }
    }

    const emailInput = document.getElementById('emailInput');
    if (emailInput) {
      emailInput.addEventListener('keydown', e => {
        if (e.key === 'Enter') handleEmailSubmit();
      });
    }
'''

HIDDEN_FORM = '''        <form name="free-lite" method="POST" data-netlify="true" netlify-honeypot="bot-field" hidden>
          <input type="hidden" name="form-name" value="free-lite">
          <p hidden><label>Don't fill this out: <input name="bot-field"></label></p>
        </form>
'''

FOOTER = '''
  <footer>
    <div class="footer-links">
      <a href="/index.html">Home</a>
      <a href="/blog/index.html">Blog</a>
      <a href="/index.html#pricing">Pricing</a>
      <a href="/privacy.html">Privacy</a>
      <a href="/terms.html">Terms</a>
      <a href="TWITTER_URL">Twitter / X</a>
    </div>
    <p>Built by a scalper, for scalpers. <a href="TWITTER_URL">@scalpersedge</a></p>
    <p style="margin-top:0.4rem;font-size:0.72rem;color:var(--text-tertiary);">© 2026 The Scalper's Edge. All rights reserved.</p>
  </footer>
'''.replace('TWITTER_URL', TWITTER)


def nav_html(active='') -> str:
    bolt = ('<svg width="14" height="18" viewBox="0 0 14 18" fill="none" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">'
            '<path d="M8 1L1 10h5.5L5 17l8-9H7L8 1z" fill="currentColor"/></svg>')
    return f'''  <nav>
    <a href="/index.html" class="nav-brand">{bolt}
      The Scalper's Edge
    </a>
    <div class="nav-right">
      <a href="/blog/index.html"{ ' style="color:var(--text);font-weight:600;"' if active == 'blog' else ''}>Blog</a>
      <a href="/index.html#features">Features</a>
      <a href="/index.html#pricing">Pricing</a>
      <a href="/index.html#pricing" class="nav-cta">Get Template — $49</a>
    </div>
  </nav>'''


def head(title, desc, canonical, extra=''):
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{esc(title)}</title>
  <meta name="description" content="{esc(desc)}">
  <meta property="og:title" content="{esc(title)}">
  <meta property="og:description" content="{esc(desc)}">
  <meta property="og:type" content="article">
  <meta property="og:url" content="{canonical}">
  <meta name="twitter:card" content="summary">
  <meta name="twitter:title" content="{esc(title)}">
  <meta name="twitter:description" content="{esc(desc)}">
  <link rel="canonical" href="{canonical}">
  <link rel="icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><text y='75' font-size='75' fill='%23111111'>📊</text></svg>">
{extra}<link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:ital,wght@0,400;0,500;0,600;0,700;0,800;0,900;1,400&family=JetBrains+Mono:wght@400;500;600&display=swap" rel="stylesheet">
  <style>{CSS}</style>
</head>'''


def render_post(idx: int) -> str:
    src, slug, title, dek, date, num = POSTS[idx]
    with open(os.path.join('blog', src), encoding='utf-8') as f:
        md = f.read()
    body_md, about = split_about(md)
    body_html = md_to_html(body_md)
    url = f'{DOMAIN}/blog/{slug}'

    prev_card, next_card = '', ''
    if idx > 0:
        p = POSTS[idx - 1]
        prev_card = (f'<a class="pn-card" href="{p[1]}.html"><div class="pn-label">← Previous</div>'
                     f'<div class="pn-title">{esc(p[2])}</div></a>')
    else:
        prev_card = '<div class="pn-card pn-spacer"></div>'
    if idx < len(POSTS) - 1:
        n = POSTS[idx + 1]
        next_card = (f'<a class="pn-card next" href="{n[1]}.html"><div class="pn-label">Next →</div>'
                     f'<div class="pn-title">{esc(n[2])}</div></a>')
    else:
        next_card = '<div class="pn-card pn-spacer"></div>'

    about_html = ''
    if about:
        about_html = f'''    <div class="about-box">
      <p><strong>About the author:</strong> {inline(about.replace('About the author:', '').strip())} Read more on <a href="{TWITTER}">X&nbsp;/&nbsp;Twitter</a>.</p>
    </div>'''

    return f'''{head(title, dek, url, extra=jsonld_post(slug, title, dek, date) + '\n')}
<body>
{nav_html()}
  <article class="article">
    <p class="post-number">Edge Notes · #{num:02d}</p>
    <h1>{esc(title)}</h1>
    <p class="dek">{esc(dek)}</p>
    <div class="meta">
      <span>{date}</span>
      <span class="divider"></span>
      <span>~8 min read</span>
      <span class="divider"></span>
      <a href="{TWITTER}">@scalpersedge</a>
    </div>
    <div class="article-body">
{body_html}
{about_html}
    </div>
  </article>

  <div class="prevnext">
    {prev_card}
    {next_card}
  </div>
{EMAIL_MINI}
{FOOTER}
  <script>{EMAIL_MINI_JS}
  </script>
</body>
</html>'''


def render_index() -> str:
    title = "Edge Notes — The Scalper's Edge Blog"
    desc = ("Field notes on scalping discipline: R-multiples, pre-trade checklists, revenge trading, "
            "spread costs, and the psychology of the first hour. Written for traders who take 10+ trades a day.")
    url = f'{DOMAIN}/blog/'

    cards = []
    for src, slug, t, dek, date, num in POSTS:
        cards.append(f'''    <a class="post-card" href="{slug}.html">
      <div class="num">Edge Notes · #{num:02d}</div>
      <h2>{esc(t)}</h2>
      <p>{esc(dek)}</p>
      <div class="read">Read the post →</div>
    </a>''')

    return f'''{head(title, desc, url)}
<body>
{nav_html('blog')}
  <header class="blog-head">
    <div class="section-label">The Blog</div>
    <h1>Edge Notes</h1>
    <p>Field notes from a year of scalping: what the data says about journaling, psychology, and where the money actually leaks. No hype, no lambos.</p>
  </header>
  <div class="post-list">
{chr(10).join(cards)}
  </div>
{FOOTER}
</body>
</html>'''


def main():
    os.makedirs('blog', exist_ok=True)
    with open(os.path.join('blog', 'index.html'), 'w', encoding='utf-8', newline='\n') as f:
        f.write(render_index())
    print(f'wrote blog/index.html')
    for i in range(len(POSTS)):
        slug = POSTS[i][1]
        path = os.path.join('blog', f'{slug}.html')
        with open(path, 'w', encoding='utf-8', newline='\n') as f:
            f.write(render_post(i))
        print(f'wrote {path}')


if __name__ == '__main__':
    main()
