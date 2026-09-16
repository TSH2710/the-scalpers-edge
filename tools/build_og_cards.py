#!/usr/bin/env python3
"""Build og:image share cards (1200x630 PNGs) into og/.

Renders each card as a small HTML file that reuses index.html's design tokens
(Inter + JetBrains Mono, #fafafa, black bolt, film grain), then screenshots it
with headless Edge. Safe to re-run: regenerates everything.

Usage: python tools/build_og_cards.py
"""
import os
import shutil
import subprocess
import sys
import tempfile
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from build_blog import POSTS, DOMAIN  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, 'og')
SRC = os.path.join(OUT, '_src')

GRAIN = ("data:image/svg+xml,%3Csvg viewBox='0 0 256 256' xmlns='http://www.w3.org/2000/svg'%3E"
         "%3Cfilter id='noise'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.9' "
         "numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' "
         "filter='url(%23noise)'/%3E%3C/svg%3E")

BOLT = ('<svg width="22" height="28" viewBox="0 0 14 18" fill="none" '
        'xmlns="http://www.w3.org/2000/svg"><path d="M8 1L1 10h5.5L5 17l8-9H7L8 1z" '
        'fill="currentColor"/></svg>')
BOLT_SM = ('<svg width="12" height="15" viewBox="0 0 14 18" fill="none" '
           'xmlns="http://www.w3.org/2000/svg"><path d="M8 1L1 10h5.5L5 17l8-9H7L8 1z" '
           'fill="currentColor"/></svg>')

PAGE = '''<!DOCTYPE html>
<html><head><meta charset="utf-8">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:ital,wght@0,400;0,500;0,600;0,700;0,800;1,700&family=JetBrains+Mono:wght@500&display=swap" rel="stylesheet">
<style>
  * {{ box-sizing: border-box; }}
  body {{ margin:0; width:1200px; height:630px; overflow:hidden;
         background:#fafafa; color:#111;
         font-family:'Inter',-apple-system,'Segoe UI',sans-serif; }}
  .card {{ position:relative; width:1200px; height:630px; padding:64px 80px;
          display:flex; flex-direction:column; }}
  .grain {{ position:absolute; inset:0; background-image:url("{grain}");
           opacity:0.035; pointer-events:none; }}
  .glow  {{ position:absolute; inset:0;
           background:radial-gradient(720px 360px at 16% -12%, rgba(17,17,17,0.05), transparent 70%);
           pointer-events:none; }}
  .top {{ display:flex; justify-content:space-between; align-items:center; }}
  .brand {{ display:flex; align-items:center; gap:12px; font-weight:700;
           font-size:19px; letter-spacing:-0.01em; }}
  .label {{ font-family:'JetBrains Mono',monospace; font-size:15px;
           letter-spacing:0.14em; text-transform:uppercase; color:#8a8a8a; }}
  .mid {{ flex:1; display:flex; flex-direction:column; justify-content:center; }}
  h1 {{ margin:0; font-weight:800; letter-spacing:-0.03em; line-height:1.06;
       max-width:1010px; }}
  .dek {{ margin:24px 0 0; font-size:22px; line-height:1.45; color:#555;
         max-width:860px; }}
  .foot {{ display:flex; justify-content:space-between; align-items:center;
          color:#8a8a8a; font-family:'JetBrains Mono',monospace; font-size:16px; }}
  .dom {{ display:flex; align-items:center; gap:9px; color:#8a8a8a; }}
  .pill {{ background:#111; color:#fafafa; font-family:'Inter',sans-serif;
          font-weight:600; font-size:19px; padding:15px 30px; border-radius:999px; }}
  .idx  {{ font-family:'JetBrains Mono',monospace; font-size:16px; color:#8a8a8a; }}
</style></head>
<body><div class="card">
  <div class="glow"></div><div class="grain"></div>
  <div class="top">
    <div class="brand">{bolt}The Scalper's Edge</div>
    <div class="label">{label}</div>
  </div>
  <div class="mid">
    {body}
  </div>
  <div class="foot">{foot}</div>
</div></body></html>'''


def title_size(t: str) -> str:
    if len(t) > 90:
        return 'font-size:44px;'
    if len(t) > 60:
        return 'font-size:52px;'
    return 'font-size:58px;'


def cards() -> list:
    out = []
    home_body = (f'<h1 style="font-size:62px;">Stop guessing.<br>Start journaling.<br>'
                 f'<span style="color:#9a9a9a;font-style:italic;">Know your edge.</span></h1>'
                 f'<p class="dek">The Notion trade journal built specifically for scalpers — '
                 f'R-multiples, spread tracking, psychology flags, session heatmaps.</p>')
    home_foot = ('<div class="pill">Get the template — $49</div>'
                 f'<div class="dom">{BOLT_SM}thescalpersedge.com</div>')
    out.append(('home', 'Notion Trade Journal', home_body, home_foot))

    blog_body = ('<h1 style="font-size:64px;">Edge Notes</h1>'
                 '<p class="dek">Field notes on scalping discipline: R-multiples, pre-trade '
                 'checklists, revenge trading, spread costs, and the psychology of the first '
                 'hour. Written for traders who take 10+ trades a day.</p>')
    blog_foot = ('<div class="idx">Free, every week</div>'
                 f'<div class="dom">{BOLT_SM}thescalpersedge.com/blog</div>')
    out.append(('blog', 'The Blog', blog_body, blog_foot))

    for src, slug, title, dek, date, num in POSTS:
        body = (f'<h1 style="{title_size(title)}">{title}</h1>'
                f'<p class="dek">{dek}</p>')
        foot = (f'<div class="idx">Edge Notes · {num:02d} / {len(POSTS):02d}</div>'
                f'<div class="dom">{BOLT_SM}thescalpersedge.com/blog</div>')
        out.append((f'{num:02d}', f'Edge Notes · #{num:02d}', body, foot))
    return out


def find_edge() -> str:
    for p in (r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe',
              r'C:\Program Files\Microsoft\Edge\Application\msedge.exe'):
        if os.path.exists(p):
            return p
    raise SystemExit('msedge.exe not found')


def png_size(path: str):
    with open(path, 'rb') as f:
        head = f.read(24)
    return head[16:20].hex(), head[20:24].hex()


def main():
    edge = find_edge()
    if os.path.exists(SRC):
        shutil.rmtree(SRC)
    os.makedirs(SRC)

    names = []
    for name, label, body, foot in cards():
        html = PAGE.format(grain=GRAIN, bolt=BOLT, label=label, body=body, foot=foot)
        with open(os.path.join(SRC, f'{name}.html'), 'w', encoding='utf-8') as f:
            f.write(html)
        names.append(name)

    os.makedirs(OUT, exist_ok=True)
    for name in names:
        src_url = 'file:///' + os.path.join(SRC, f'{name}.html').replace('\\', '/')
        png = os.path.join(OUT, f'{name}.png')
        # Fresh profile per card: a lingering headless instance would otherwise
        # swallow subsequent launches via single-instance delegation.
        profile = tempfile.mkdtemp(prefix='og-edge-')
        try:
            subprocess.run([
                edge, '--headless=new', '--disable-gpu', '--hide-scrollbars',
                '--force-device-scale-factor=1', '--window-size=1200,630',
                '--virtual-time-budget=15000', '--no-first-run',
                '--user-data-dir=' + profile,
                '--screenshot=' + png, src_url,
            ], check=True, capture_output=True, timeout=120)
        finally:
            shutil.rmtree(profile, ignore_errors=True)
        # Edge may return before the file is flushed; poll until the PNG exists
        # and its size has stabilized.
        deadline, last = time.time() + 45, -1
        while time.time() < deadline:
            size = os.path.getsize(png) if os.path.exists(png) else -1
            if size > 10240 and size == last:
                break
            last = size
            time.sleep(0.5)
        else:
            raise SystemExit(f'{png} never appeared or kept changing')
        print(f'wrote og/{name}.png ({last} bytes)')
    shutil.rmtree(SRC, ignore_errors=True)

    for name in names:
        w, h = png_size(os.path.join(OUT, f'{name}.png'))
        print(f'og/{name}.png  {int(w, 16)}x{int(h, 16)}')


if __name__ == '__main__':
    main()
