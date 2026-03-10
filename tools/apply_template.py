#!/usr/bin/env python3
"""
Simple utility to apply `global.html` template to an existing page.
Usage:
  ./tools/apply_template.py equipe.html generated/equipe.html
This will wrap the body of `equipe.html` into the template and write to generated/equipe.html
"""
import sys
from pathlib import Path

def extract_body(html_text):
    # naive extraction between <body>...</body>
    low = html_text.lower()
    start = low.find('<body')
    if start == -1:
        return html_text
    start = low.find('>', start) + 1
    end = low.rfind('</body>')
    if end == -1:
        end = len(html_text)
    return html_text[start:end].strip()


def main():
    if len(sys.argv) < 3:
        print('usage: apply_template.py source.html dest.html')
        sys.exit(1)
    src = Path(sys.argv[1])
    dst = Path(sys.argv[2])
    tpl = Path('global.html')
    if not src.exists() or not tpl.exists():
        print('source or template not found')
        sys.exit(1)
    page = src.read_text(encoding='utf-8')
    body = extract_body(page)
    out = tpl.read_text(encoding='utf-8')
    out = out.replace('<!-- PAGE_TITLE -->', src.stem.capitalize())
    out = out.replace('<!-- PAGE_CONTENT -->', body)
    dst.parent.mkdir(parents=True, exist_ok=True)
    dst.write_text(out, encoding='utf-8')
    print('Wrote', dst)

if __name__ == '__main__':
    main()
