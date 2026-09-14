#!/usr/bin/env python3
"""Sanity checks: HTML tag balance and internal link integrity for the site."""
import html.parser
import os
import re
import sys

VOIDS = {'area', 'base', 'br', 'col', 'embed', 'hr', 'img', 'input', 'link',
         'meta', 'param', 'source', 'track', 'wbr'}


class Checker(html.parser.HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.stack = []
        self.errors = []

    def handle_starttag(self, tag, attrs):
        if tag not in VOIDS:
            self.stack.append((tag, self.getpos()))

    def handle_endtag(self, tag):
        if tag in VOIDS:
            return
        if self.stack and self.stack[-1][0] == tag:
            self.stack.pop()
        else:
            self.errors.append(f'mismatched </{tag}> at {self.getpos()}')


def check_file(path):
    with open(path, encoding='utf-8') as f:
        content = f.read()
    c = Checker()
    c.feed(content)
    errs = [f'</> unclosed: {t} at {pos}' for t, pos in c.stack] + c.errors
    # internal link check
    here = os.path.dirname(path)
    for m in re.finditer(r'(?:href|src)="([^"#]+)(?:#[^"]*)?"', content):
        target = m.group(1)
        if target.startswith(('http://', 'https://', 'mailto:', 'data:', '//')):
            continue
        clean = target.split('?')[0]
        if not clean:
            continue
        if clean.startswith('/'):
            resolved = os.path.normpath(clean.lstrip('/'))
        else:
            resolved = os.path.normpath(os.path.join(here, clean))
        if not os.path.exists(resolved):
            errs.append(f'broken link "{target}" -> {resolved}')
    return errs


def main():
    targets = ['index.html', 'landing.html', 'privacy.html', 'terms.html',
               '404.html', 'blog/index.html'] + \
              [f'blog/{f}' for f in sorted(os.listdir('blog')) if f.endswith('.html') and f != 'index.html']
    failures = 0
    for path in targets:
        errs = check_file(path)
        if errs:
            failures += 1
            print(f'FAIL {path}')
            for e in errs[:8]:
                print(f'   {e}')
        else:
            print(f'OK   {path}')
    sys.exit(1 if failures else 0)


if __name__ == '__main__':
    main()
