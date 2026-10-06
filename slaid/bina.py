"""Jana slaid HTML dan fail MD daripada kandungan.py.

Sumber tunggal: sunting slaid dalam slaid/kandungan.py, kemudian jalankan
    python3 slaid/bina.py
Hasil: slaid/modul-1.html, modul-2.html, modul-3.html, hands-on.html dan slaid/md/*.md
"""
import html as H
import re
from pathlib import Path

HERE = Path(__file__).parent
import sys
sys.path.insert(0, str(HERE))
from kandungan import DECKS  # noqa: E402

ICONS = {
    "text": '<path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><path d="M14 2v6h6M16 13H8M16 17H8M10 9H8"/>',
    "image": '<rect x="3" y="3" width="18" height="18" rx="2"/><circle cx="9" cy="9" r="2"/><path d="m21 15-3.1-3.1a2 2 0 0 0-2.8 0L6 21"/>',
    "music": '<path d="M9 18V5l12-2v13"/><circle cx="6" cy="18" r="3"/><circle cx="18" cy="16" r="3"/>',
    "video": '<path d="m22 8-6 4 6 4V8z"/><rect x="2" y="6" width="14" height="12" rx="2"/>',
    "eye": '<path d="M2 12s3-7 10-7 10 7 10 7-3 7-10 7-10-7-10-7z"/><circle cx="12" cy="12" r="3"/>',
    "check": '<path d="M20 6 9 17l-5-5"/>',
    "x": '<path d="M18 6 6 18M6 6l12 12"/>',
    "alert": '<path d="m21.7 18-8-14a2 2 0 0 0-3.4 0l-8 14A2 2 0 0 0 4 21h16a2 2 0 0 0 1.7-3z"/><path d="M12 9v4M12 17h.01"/>',
    "clock": '<circle cx="12" cy="12" r="10"/><path d="M12 6v6l4 2"/>',
    "mail": '<rect x="2" y="4" width="20" height="16" rx="2"/><path d="m22 7-10 5L2 7"/>',
    "users": '<path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M22 21v-2a4 4 0 0 0-3-3.9M16 3.1a4 4 0 0 1 0 7.8"/>',
    "user": '<circle cx="12" cy="8" r="4"/><path d="M4 21v-1a6 6 0 0 1 6-6h4a6 6 0 0 1 6 6v1"/>',
    "spark": '<path d="M12 3l1.9 5.8L20 11l-6.1 2.2L12 19l-1.9-5.8L4 11l6.1-2.2z"/>',
    "slides": '<path d="M2 3h20M21 3v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V3M7 21l5-5 5 5"/>',
    "shield": '<path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/>',
    "cpu": '<rect x="4" y="4" width="16" height="16" rx="2"/><rect x="9" y="9" width="6" height="6"/><path d="M9 1v3M15 1v3M9 20v3M15 20v3M20 9h3M20 14h3M1 9h3M1 14h3"/>',
    "trend": '<path d="m22 7-8.5 8.5-5-5L2 17"/><path d="M16 7h6v6"/>',
    "list": '<path d="M8 6h13M8 12h13M8 18h13M3 6h.01M3 12h.01M3 18h.01"/>',
    "chat": '<path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/>',
    "hat": '<path d="M2 18h20M4 18v-3a8 8 0 0 1 16 0v3M10 7V4h4v3"/>',
    "gem": '<path d="M6 3h12l4 6-10 13L2 9z"/><path d="M2 9h20M12 22 8 9l4-6 4 6"/>',
    "search": '<circle cx="11" cy="11" r="8"/><path d="m21 21-4.3-4.3"/>',
    "pen": '<path d="M12 20h9"/><path d="M16.5 3.5a2.1 2.1 0 0 1 3 3L7 19l-4 1 1-4z"/>',
    "target": '<circle cx="12" cy="12" r="10"/><circle cx="12" cy="12" r="6"/><circle cx="12" cy="12" r="2"/>',
    "map": '<path d="M9 3 3 6v15l6-3 6 3 6-3V3l-6 3z"/><path d="M9 3v15M15 6v15"/>',
    "cal": '<rect x="3" y="4" width="18" height="18" rx="2"/><path d="M16 2v4M8 2v4M3 10h18"/>',
    "route": '<circle cx="6" cy="19" r="3"/><path d="M9 19h8.5a3.5 3.5 0 0 0 0-7h-11a3.5 3.5 0 0 1 0-7H15"/><circle cx="18" cy="5" r="3"/>',
    "cone": '<path d="M9.5 3h5L20 21H4z"/><path d="M7.5 10h9M6 15h12M2 21h20"/>',
    "globe": '<circle cx="12" cy="12" r="10"/><path d="M2 12h20M12 2a15 15 0 0 1 0 20M12 2a15 15 0 0 0 0 20"/>',
    "lock": '<rect x="3" y="11" width="18" height="11" rx="2"/><path d="M7 11V7a5 5 0 0 1 10 0v4"/>',
    "repeat": '<path d="m17 2 4 4-4 4"/><path d="M3 11V9a4 4 0 0 1 4-4h14M7 22l-4-4 4-4"/><path d="M21 13v2a4 4 0 0 1-4 4H3"/>',
    "link": '<path d="M10 13a5 5 0 0 0 7.5.5l3-3a5 5 0 0 0-7-7l-1.7 1.7"/><path d="M14 11a5 5 0 0 0-7.5-.5l-3 3a5 5 0 0 0 7 7l1.7-1.7"/>',
    "q": '<circle cx="12" cy="12" r="10"/><path d="M9.1 9a3 3 0 0 1 5.8 1c0 2-3 3-3 3M12 17h.01"/>',
}


def ic(name):
    return f'<svg class="ic" viewBox="0 0 24 24" aria-hidden="true">{ICONS[name]}</svg>' if name else ""


LABELS = r"(Peranan|Konteks|Tugasan|Output|Kekangan|Templat|Nota|Susulan|Pusingan \d)"


def code_html(text):
    t = H.escape(text)
    return re.sub(rf"(?m)^{LABELS}:", r'<span class="k">\1:</span>', t)


def P(x):
    """Teks dengan HTML ringkas dibenarkan (b, em, code)."""
    return x or ""


# ---------- Pemapar HTML mengikut jenis ----------

def r_title(s, ctx):
    pills = "".join(f'<span class="pill{" gold" if i == 0 else ""}">{p}</span>' for i, p in enumerate(s.get("pills", [])))
    return f'''<div class="giant">{s.get("giant","")}</div>
<div class="t-title"><div class="stripe"></div><p class="eyebrow">{s.get("eyebrow","")}</p><h1>{s["h"]}</h1>
<p class="sub">{P(s.get("sub"))}</p><div class="meta-row">{pills}</div></div>'''


r_section = r_title


def head(s):
    k = f'<p class="kicker">{s["kicker"]}</p>' if s.get("kicker") else ""
    sub = f'<p class="sub">{s["sub"]}</p>' if s.get("sub") else ""
    return f'{k}<h2>{s["h"]}</h2>{sub}'


def note(s):
    return f'<p class="note">{s["note"]}</p>' if s.get("note") else ""


def r_big(s, ctx):
    k = f'<p class="kicker">{s["kicker"]}</p>' if s.get("kicker") else ""
    sub = f'<p class="sub" style="font-size:26px;margin-top:26px">{s["sub"]}</p>' if s.get("sub") else ""
    return f'<div class="big-wrap">{k}<p class="big">{s["h"]}</p>{sub}</div>'


def r_quote(s, ctx):
    k = f'<p class="kicker">{s["kicker"]}</p>' if s.get("kicker") else ""
    return f'<div class="big-wrap">{k}<div class="quote-mark">&ldquo;</div><p class="quote">{s["h"]}</p><p class="src">{s.get("src","")}</p></div>'


def r_points(s, ctx):
    items = []
    for i, it in enumerate(s["items"]):
        hd, d = (it if isinstance(it, (list, tuple)) else (it, ""))
        mark = {"check": ic("check"), "warn": ic("alert")}.get(s.get("style"), f"{i+1:02d}")
        items.append(f'<li><span class="dot">{mark}</span><div><b>{hd}</b>{f"<span class=d>{d}</span>" if d else ""}</div></li>')
    return f'{head(s)}<div class="body"><ul class="points {s.get("style","")}">{"".join(items)}</ul>{note(s)}</div>'


def r_cards(s, ctx):
    cs = []
    for c in s["cards"]:
        big = f'<div class="iconbig">{ic(c["icon"])}</div>' if c.get("bigicon") else ""
        lab = f'<p class="lab">{"" if c.get("bigicon") else ic(c.get("icon"))}{c.get("lab","")}</p>' if (c.get("lab") or (c.get("icon") and not c.get("bigicon"))) else ""
        cs.append(f'<div class="card{" hl" if c.get("hl") else ""}">{big}{lab}<h3>{c["h"]}</h3><p>{c.get("p","")}</p></div>')
    return f'{head(s)}<div class="body"><div class="cards c{s.get("cols", len(cs))}">{"".join(cs)}</div>{note(s)}</div>'


def r_flow(s, ctx):
    st = []
    for i, x in enumerate(s["steps"]):
        n, h_, p = (list(x) + ["", ""])[:3]
        on = " on" if i in s.get("on", []) else ""
        st.append(f'<div class="st{on}"><p class="n">{n}</p><h3>{h_}</h3>{f"<p>{p}</p>" if p else ""}</div>')
    return f'{head(s)}<div class="body"><div class="flow">{"".join(st)}</div>{note(s)}</div>'


def r_table(s, ctx):
    th = "".join(f"<th>{x}</th>" for x in s["head"])
    rows = "".join("<tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>" for r in s["rows"])
    return f'{head(s)}<div class="body"><div class="tbl"><table><thead><tr>{th}</tr></thead><tbody>{rows}</tbody></table></div>{note(s)}</div>'


def r_agenda(s, ctx):
    rows = "".join(
        f'<div class="row{" cs" if k == "Cuba Sekarang" else ""}"><span class="tm">{t}</span><span class="cd">{c}</span><span>{x}</span><span class="kd">{k}</span></div>'
        for t, c, x, k in s["rows"])
    return f'{head(s)}<div class="body"><div class="agenda">{rows}</div>{note(s)}</div>'


def r_act(s, ctx):
    steps = "".join(f"<li><span>{x}</span></li>" for x in s.get("steps", []))
    steps = f'<ol class="act-steps">{steps}</ol>' if steps else ""
    timer = f'<button class="timer" data-min="{s["min"]}" title="Klik untuk mula / jeda">{ic("clock")}<span></span></button>' if s.get("min") else ""
    codes = []
    for pr in (s["prompt"] if isinstance(s["prompt"], list) else [s["prompt"]]):
        lbl, txt = pr if isinstance(pr, tuple) else ("Prompt", pr)
        size = s.get("size", "")
        codes.append(f'<div class="code {size}"><div class="bar"><span class="dots"><i></i><i></i><i></i></span><span class="lbl">{lbl}</span><button class="copy" type="button">Salin</button></div><pre>{code_html(txt)}</pre></div>')
    fol = "".join(f'<div class="follow"><b>{a}</b>{b}</div>' for a, b in s.get("follow", []))
    return f'''<div class="act-grid"><div class="act-left"><span class="badge">{ic("spark")}{s.get("badge","Cuba Sekarang")}</span>
<h2>{s["h"]}</h2>{f'<p class="sub">{s["sub"]}</p>' if s.get("sub") else ""}{steps}{timer}</div>
<div class="code-wrap">{"".join(codes)}{fol}</div></div>'''


def r_compare(s, ctx):
    def side(cls, d):
        pre = f'<pre>{H.escape(d["pre"])}</pre>' if d.get("pre") else ""
        return f'<div class="side {cls}"><p class="tagl">{d["label"]}</p>{pre}<p>{d.get("p","")}</p></div>'
    return f'{head(s)}<div class="body"><div class="compare">{side("bad", s["bad"])}{side("good", s["good"])}</div>{note(s)}</div>'


def r_lights(s, ctx):
    ls = "".join(f'<div class="l {c}"><div class="bulb"></div><h3>{h_}</h3><p>{p}</p></div>' for c, h_, p in s["items"])
    return f'{head(s)}<div class="body"><div class="lights">{ls}</div>{note(s)}</div>'


def r_quiz(s, ctx):
    lab = {"g": "Hijau", "y": "Kuning", "r": "Merah"}
    qs = "".join(
        f'<div class="qz {c}"><span class="qn">SENARIO {i+1}</span><p>{t}</p><div class="ans"><b>{lab[c]}</b>{a}</div></div>'
        for i, (t, c, a) in enumerate(s["items"]))
    return f'{head(s)}<div class="body"><div class="quiz">{qs}</div><p class="hint">Klik setiap kad untuk mendedahkan jawapan.</p></div>'


def r_anatomy(s, ctx):
    lines = []
    for x in s["doc"]:
        k, kind, txt = x
        badge = f'<span class="k">{k}</span>' if k else ""
        if kind == "bar":
            body = "".join(f'<div class="bar" style="width:{w}%"></div>' for w in txt)
            lines.append(f'<div class="ln">{badge}<div class="tx">{body}</div></div>')
        else:
            lines.append(f'<div class="ln {kind}">{badge}<span class="tx" style="flex:none">{txt}</span></div>' if kind in ("r", "ctr")
                         else f'<div class="ln">{badge}<span class="tx">{txt}</span></div>')
    leg = "".join(f'<li><span class="k">{k}</span>{t}</li>' for k, t in s["legend"])
    return f'{head(s)}<div class="anat"><div class="doc">{"".join(lines)}</div><div><ul class="legend">{leg}</ul>{note(s)}</div></div>'


def r_email(s, ctx):
    m = s["mail"]
    www = "".join(f"<span>{a}<small>{b}</small></span>" for a, b in s["www"])
    return f'''{head(s)}<div class="anat" style="margin-top:20px"><div class="mail"><div class="mh"><span>Kepada: <b>{m["to"]}</b></span><span>Perkara: <b>{m["subj"]}</b></span></div>
<div class="mb"><p class="first">{m["first"]}</p><p>{m["body"]}</p></div></div><div><div class="www">{www}</div>{note(s)}</div></div>'''


MAP_SVG = '''<svg viewBox="0 0 480 440" width="100%" height="100%" preserveAspectRatio="xMidYMid slice" aria-label="Lakaran lokasi rekaan">
<defs><pattern id="d" width="24" height="24" patternUnits="userSpaceOnUse"><circle cx="2" cy="2" r="1.4" fill="rgba(255,255,255,.08)"/></pattern></defs>
<rect width="480" height="440" fill="url(#d)"/>
<path d="M-10 330 C 120 300, 180 210, 300 190 S 470 120, 500 90" stroke="#3b4a60" stroke-width="34" fill="none" stroke-linecap="round"/>
<path d="M-10 330 C 120 300, 180 210, 300 190 S 470 120, 500 90" stroke="rgba(255,255,255,.55)" stroke-width="2" stroke-dasharray="14 12" fill="none"/>
<path d="M60 318 C 90 380, 250 420, 330 360 S 420 240, 430 130" stroke="var(--p-gold)" stroke-width="5" stroke-dasharray="2 12" stroke-linecap="round" fill="none"/>
<g fill="var(--p-accent)" stroke="#fff" stroke-width="2"><circle cx="196" cy="236" r="8"/><circle cx="214" cy="224" r="7"/><circle cx="232" cy="214" r="8"/><circle cx="252" cy="206" r="7"/><circle cx="270" cy="199" r="8"/><circle cx="288" cy="193" r="7"/></g>
<g font-family="Plus Jakarta Sans, Arial" font-weight="800" fill="#fff">
<text x="160" y="276" font-size="15">KM 3.0</text><text x="300" y="234" font-size="15">KM 3.2</text>
<text x="24" y="40" font-size="13" fill="rgba(255,255,255,.6)" letter-spacing="2">LAKARAN REKAAN</text>
<text x="24" y="66" font-size="20">Jalan Kg. Contoh, Rembau</text>
<text x="250" y="414" font-size="14" fill="var(--p-gold)">Jalan Sekolah (laluan alternatif)</text>
<text x="330" y="160" font-size="14" fill="#ffb4b4">6 lubang + bahu jalan</text></g></svg>'''


def r_case(s, ctx):
    fs = "".join(f'<div class="fact">{ic(i)}<div><small>{l}</small>{t}</div></div>' for i, l, t in s["facts"])
    return f'{head(s)}<div class="case" style="margin-top:22px"><div class="facts">{fs}</div><div class="map">{MAP_SVG}</div></div>'


def r_close(s, ctx):
    cs = "".join(f'<div class="card"><div class="big-n">{n}</div><h3>{h_}</h3><p>{p}</p></div>' for n, h_, p in s["items"])
    nx = ""
    if s.get("next"):
        t, href, lab = s["next"]
        nx = f'<div class="next"><span>{t}</span><a href="{href}">{lab} &rarr;</a></div>'
    return f'{head(s)}<div class="body"><div class="takeaways">{cs}</div>{nx}</div>'


def r_memo(s, ctx):
    side = "".join(f'<li><span class="dot">{ic(i)}</span><div><b>{h_}</b><span class="d">{d}</span></div></li>' for i, h_, d in s["side"])
    return f'''{head(s)}<div class="anat" style="grid-template-columns:1.25fr 1fr;gap:34px;margin-top:18px;align-items:start">
<div class="memo">{s["memo"]}</div><ul class="points warn" style="gap:14px">{side}</ul></div>'''


def r_guess(s, ctx):
    fs = "".join(
        f'<figure class="gf"><div class="ph"><img src="{src}" alt="Potret {lab}" loading="lazy"><span class="gl">{lab}</span></div>'
        f'<figcaption><b>{ans}</b>{det}</figcaption></figure>'
        for lab, src, ans, det in s["items"])
    return f'{head(s)}<div class="body" style="margin-top:14px"><div class="guess">{fs}</div><p class="hint">{s.get("hint", "Klik setiap foto untuk dedah jawapan.")}</p></div>'


RENDER = {k[2:]: v for k, v in globals().items() if k.startswith("r_")}
DARK = {"title", "section"}


def strip(x):
    x = re.sub(r"</?em>", "*", x or "")
    x = re.sub(r"</?b>", "**", x)
    x = re.sub(r"<code>(.*?)</code>", r"`\1`", x)
    x = re.sub(r"<br\s*/?>", " ", x)
    x = re.sub(r"<[^>]+>", "", x)
    return H.unescape(x).strip()


VISUAL = {
    "title": "Latar gelap warna utama, nombor modul gergasi bergaris di kanan bawah, jalur emas kecil, tajuk besar putih dengan satu perkataan italik emas.",
    "section": "Latar penuh warna utama, nombor seksyen gergasi bergaris, tajuk besar putih.",
    "big": "Pernyataan besar pada latar kertas cerah, satu perkataan berwarna aksen.",
    "quote": "Petikan besar fon serif italik, tanda petik emas besar.",
    "points": "Senarai bernombor dengan kotak nombor gelap di kiri setiap poin.",
    "cards": "Grid kad putih bersudut bulat, ikon kecil dan label aksen di atas tajuk kad.",
    "flow": "Aliran kotak dari kiri ke kanan dengan anak panah di antara langkah.",
    "table": "Jadual bersih, baris kepala gelap, baris berselang warna lembut.",
    "agenda": "Garis masa baris demi baris: masa, kod, perkara, label jenis aktiviti (Cuba Sekarang diserlahkan emas).",
    "act": "Latar emas lembut. Kiri: lencana 'Cuba Sekarang', tajuk, langkah bernombor, butang pemasa. Kanan: kotak prompt gelap gaya terminal dengan butang Salin.",
    "compare": "Dua lajur: kiri merah lembut (sebelum), kanan hijau lembut (selepas).",
    "lights": "Tiga kad lampu isyarat: bulatan hijau, kuning, merah.",
    "quiz": "Grid 3 x 2 kad senario; klik untuk dedah jawapan berwarna.",
    "anatomy": "Kiri: lakaran surat dengan nombor pada setiap bahagian. Kanan: petunjuk bernombor.",
    "email": "Kiri: tetingkap e-mel dengan baris pertama diserlahkan. Kanan: tiga blok Siapa, Apa, Bila.",
    "case": "Kiri: kad fakta dengan ikon. Kanan: lakaran peta gelap jalan, 6 titik merah lubang, laluan alternatif bertitik emas.",
    "close": "Tiga kad rumusan bernombor besar, jalur gelap di bawah menunjuk modul seterusnya.",
    "guess": "Tiga potret sebaris berlabel A, B, C; klik setiap foto untuk dedah jawapan di bawahnya.",
    "memo": "Kiri: nota tulisan tangan atas kertas bergaris dengan bahagian bermasalah diserlahkan. Kanan: senarai amaran.",
}


def md_body(s):
    t = s["t"]
    out = []
    if t in ("title", "section"):
        out += [f"- Label: {strip(s.get('eyebrow'))}", f"- Tajuk: {strip(s['h'])}"]
        if s.get("sub"): out.append(f"- Subtajuk: {strip(s['sub'])}")
        if s.get("pills"): out.append("- Maklumat: " + " | ".join(strip(p) for p in s["pills"]))
        return out
    if s.get("kicker"): out.append(f"- Label: {strip(s['kicker'])}")
    out.append(f"- Tajuk: {strip(s['h'])}")
    if s.get("sub"): out.append(f"- Subtajuk: {strip(s['sub'])}")
    if t == "quote": out.append(f"- Sumber: {strip(s.get('src'))}")
    if t == "points":
        out += [f"  {i+1}. **{strip(a if isinstance(a, str) else a[0])}**" + (f": {strip(a[1])}" if isinstance(a, (list, tuple)) and a[1] else "") for i, a in enumerate(s["items"])]
    if t == "cards":
        out += [f"  - **{strip(c['h'])}**" + (f" ({strip(c['lab'])})" if c.get("lab") else "") + (f": {strip(c.get('p'))}" if c.get("p") else "") for c in s["cards"]]
    if t == "flow":
        out += [f"  {i+1}. **{strip(x[1])}**" + (f": {strip(x[2])}" if len(x) > 2 and x[2] else "") for i, x in enumerate(s["steps"])]
    if t == "table":
        out.append("")
        out.append("| " + " | ".join(strip(h) for h in s["head"]) + " |")
        out.append("|" + "---|" * len(s["head"]))
        out += ["| " + " | ".join(strip(c) for c in r) + " |" for r in s["rows"]]
        out.append("")
    if t == "agenda":
        out += [f"  - {a} | {b} | {strip(c)} | {d}" for a, b, c, d in s["rows"]]
    if t == "act":
        if s.get("min"): out.append(f"- Masa aktiviti: {s['min']} minit")
        out += [f"  {i+1}. {strip(x)}" for i, x in enumerate(s.get("steps", []))]
        for pr in (s["prompt"] if isinstance(s["prompt"], list) else [s["prompt"]]):
            lbl, txt = pr if isinstance(pr, tuple) else ("Prompt", pr)
            out += [f"- {lbl}:", "", "```text", txt, "```", ""]
        out += [f"- {strip(a)}: {strip(b)}" for a, b in s.get("follow", [])]
    if t == "compare":
        for k in ("bad", "good"):
            d = s[k]
            out.append(f"- **{strip(d['label'])}**" + (f": `{d['pre']}`" if d.get("pre") and "\n" not in d["pre"] else ""))
            if d.get("pre") and "\n" in d["pre"]:
                out += ["", "```text", d["pre"], "```", ""]
            if d.get("p"): out.append(f"  - {strip(d['p'])}")
    if t == "lights":
        out += [f"  - **{strip(h_)}**: {strip(p)}" for _, h_, p in s["items"]]
    if t == "quiz":
        lab = {"g": "Hijau", "y": "Kuning", "r": "Merah"}
        out += [f"  {i+1}. {strip(a)} -> Jawapan: **{lab[c]}**. {strip(b)}" for i, (a, c, b) in enumerate(s["items"])]
    if t == "anatomy":
        out += [f"  {k}. {strip(x)}" for k, x in s["legend"]]
    if t == "email":
        m = s["mail"]
        out += [f"- Kepada: {m['to']}", f"- Perkara: {strip(m['subj'])}", f"- Baris pertama: {strip(m['first'])}", f"- Isi: {strip(m['body'])}"]
        out += [f"  - **{strip(a)}**: {strip(b)}" for a, b in s["www"]]
    if t == "case":
        out += [f"  - **{strip(l)}**: {strip(x)}" for _, l, x in s["facts"]]
    if t == "close":
        out += [f"  {n}. **{strip(h_)}**: {strip(p)}" for n, h_, p in s["items"]]
        if s.get("next"): out.append(f"- Seterusnya: {strip(s['next'][0])}")
    if t == "guess":
        out += [f"  - Foto {lab} (`slaid/{src}`): jawapan **{strip(ans)}**, {strip(det)}" for lab, src, ans, det in s["items"]]
    if t == "memo":
        out += ["", "```text", strip(s["memo"]), "```", ""]
        out += [f"  - **{strip(h_)}**: {strip(d)}" for _, h_, d in s["side"]]
    if s.get("note"): out.append(f"- Nota kaki slaid: {strip(s['note'])}")
    return out


MD_HEAD = """# {title}

> Fail ini ialah kandungan slaid demi slaid untuk {title}. Versi HTML siap guna: `slaid/{file}`.
> Untuk menjana semula dalam Gemini (Canvas) atau ChatGPT, tampal arahan di bawah diikuti seluruh fail ini.

**Arahan untuk Gemini / ChatGPT:**

```text
Anda pereka slaid profesional. Bina pembentangan 16:9 dalam Bahasa Melayu berdasarkan kandungan di bawah.
Ikut bilangan dan susunan slaid dengan tepat. Gunakan teks setiap slaid seperti yang diberi; jangan tambah fakta baharu.
Gaya: moden dan bersih; latar kertas cerah (#f6f3ec) untuk slaid kandungan; slaid tajuk dan seksyen berlatar biru tua (#062f63)
dengan nombor gergasi bergaris; warna utama #084c9e, aksen merah #d52b32, emas #f3bd2d; fon sans-serif tebal untuk tajuk
dan serif italik untuk satu perkataan penekanan. Ikut "Cadangan visual" bagi setiap slaid. Letakkan "Nota penceramah" dalam nota slaid.
Slaid "Cuba Sekarang" mesti memaparkan prompt dalam kotak gelap gaya terminal supaya mudah disalin.
```

---
"""


def build_deck(d):
    slides_html, md = [], [MD_HEAD.format(title=d["title"], file=d["file"])]
    n = len(d["slides"])
    for i, s in enumerate(d["slides"]):
        t = s["t"]
        cls = ["slide"]
        if t in DARK: cls.append("dark")
        if t == "section": cls.append("section")
        if t == "title": cls.append("title-slide")
        if s.get("compact_title"): cls.append("compact-title")
        if t == "act": cls.append("act")
        menu_title = strip(s.get("menu") or s["h"])
        body = RENDER[t](s, d)
        if s.get("image"):
            cls.append("illustrated")
            caption = H.escape(s.get("image_caption", "Ilustrasi dijana AI, situasi rekaan"))
            fit_class = {"contain": " visual-contain", "poster": " visual-poster"}.get(s.get("image_fit"), "")
            figure = f'<figure class="slide-visual{fit_class}"><img src="{H.escape(s["image"])}" alt="{H.escape(s["image_alt"])}"><figcaption>{caption}</figcaption></figure>'
            if s.get("image_download"):
                figure = figure.replace("</figure>", f'<a class="visual-download" href="{H.escape(s["image"])}" download>Muat turun gambar simulasi CS9</a></figure>')
            body = f'<div class="illustrated-layout"><div class="illustrated-copy">{body}</div>{figure}</div>'
        notes = f'<aside class="notes"><p>{s["notes"]}</p></aside>' if s.get("notes") else ""
        chrome = f'<div class="chrome"><span class="mod"><i></i>{d["label"]}</span><span class="pg">{i+1:02d} / {n:02d}</span></div>'
        foot = f'<div class="foot"><b style="width:{(i+1)/n*100:.1f}%"></b></div>'
        slides_html.append(f'<section class="{" ".join(cls)}" data-title="{H.escape(re.sub(r"<[^>]+>", "", H.unescape(s.get("menu") or s["h"])).strip())}">{chrome}{body}{notes}{foot}</section>')
        md.append(f"## Slaid {i+1}: {menu_title}\n")
        md.append(f"**Susun atur:** {t}\n")
        md.append("\n".join(md_body(s)) + "\n")
        if s.get("image"):
            md.append(f"**Imej:** `slaid/{s['image']}`. {s['image_alt']}\n")

        md.append(f"**Cadangan visual:** {s.get('visual') or VISUAL[t]}\n")
        if s.get("notes"): md.append(f"**Nota penceramah:** {strip(s['notes'])}\n")
        md.append("---\n")

    page = f'''<!doctype html>
<html lang="ms">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Slaid {H.escape(strip(d["title"]))} | Kursus AI JKR</title>
<meta name="description" content="{H.escape(d["desc"])}">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@1,9..144,500&family=JetBrains+Mono:wght@400;700&family=Plus+Jakarta+Sans:wght@400;600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="../assets/slides.css">
</head>
<body data-deck="{H.escape(strip(d["title"]))}">
<!-- Dijana oleh slaid/bina.py daripada slaid/kandungan.py. Jangan sunting terus. -->
<div class="viewport"><div class="stage">
{chr(10).join(slides_html)}
</div></div>
<script src="../assets/slides.js"></script>
</body>
</html>
'''
    (HERE / d["file"]).write_text(page, encoding="utf-8")
    (HERE / "md").mkdir(exist_ok=True)
    (HERE / "md" / d["file"].replace(".html", ".md")).write_text("\n".join(md), encoding="utf-8")
    return n


if __name__ == "__main__":
    for d in DECKS:
        print(f'{d["file"]}: {build_deck(d)} slaid')
