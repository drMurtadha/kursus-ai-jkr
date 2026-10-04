"""Jana prompt.html daripada blok .prompt dalam halaman modul.

Sumber tunggal: kemas kini prompt dalam modul-1/2/3.html atau hands-on.html,
kemudian jalankan:  python3 build.py
"""
import re
from pathlib import Path

ROOT = Path(__file__).parent
SOURCES = [
    ("modul-1.html", "Modul 1: Asas AI"),
    ("modul-2.html", "Modul 2: Seni Membina Prompt"),
    ("modul-3.html", "Modul 3: Komunikasi dan Dokumentasi"),
    ("hands-on.html", "Hands-on 1: Minit Mesyuarat"),
]
START = re.compile(r'<div class="prompt"[^>]*>')


def blocks(html):
    """Pulangkan setiap <div class="prompt">...</div> lengkap (div bersarang dikira)."""
    out = []
    for m in START.finditer(html):
        depth, i = 0, m.start()
        for t in re.finditer(r"<(/?)div\b[^>]*>", html[m.start():]):
            depth += -1 if t.group(1) else 1
            if depth == 0:
                out.append(html[m.start(): m.start() + t.end()])
                break
    return out


def main():
    sections = []
    for fname, title in SOURCES:
        html = (ROOT / fname).read_text(encoding="utf-8")
        items = []
        for b in blocks(html):
            pid = re.search(r'id="([^"]+)"', b).group(1)
            b = b.replace(f'id="{pid}"', f'id="b-{pid}"', 1)
            link = f'<p class="follow"><a href="{fname}#{pid}">Lihat dalam konteks &rarr;</a></p>'
            items.append(b[:-len("</div>")] + link + "</div>")
        sections.append(f'<h2 style="font-size:1.6rem;margin-top:44px">{title}</h2>\n' + "\n".join(items))

    tpl = (ROOT / "prompt.template.html").read_text(encoding="utf-8")
    (ROOT / "prompt.html").write_text(tpl.replace("<!--PROMPTS-->", "\n".join(sections)), encoding="utf-8")
    print("prompt.html dijana:", sum(s.count('class="prompt"') for s in sections), "prompt")


if __name__ == "__main__":
    main()
