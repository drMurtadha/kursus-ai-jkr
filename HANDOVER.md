# HANDOVER: Laman Kursus AI JKR (untuk manusia dan AI)

> **Untuk AI (ChatGPT, Gemini, Claude, Codex dan lain-lain):** baca fail ini sepenuhnya sebelum menyunting apa-apa.
> Ia menerangkan fail mana yang perlu disunting bagi setiap jenis perubahan, fail mana yang **dijana** (jangan disunting terus),
> dan langkah semakan sebelum pemilik membuat `git push`.

## 1. Ringkasan projek

- **Apa:** laman web statik (HTML, CSS, JS biasa, tiada framework) untuk Hari 1 *Kursus Aplikasi AI dalam Tugas Rasmi*, JKRCreate, CREaTE, 7 Oktober 2026.
- **Pemilik:** PM Dr Mohd Murtadha Mohamad (penceramah Hari 1). Fasilitator: PM Ts Dr Mohd Shahizan Othman.
- **Repo:** `https://github.com/drMurtadha/kursus-ai-jkr` (cawangan `main`), diterbitkan melalui GitHub Pages dari folder root.
- **Folder setempat:** `~/Documents/JKRCreate Petabyte/kursus-ai-jkr`
- **Bahasa kandungan:** Bahasa Melayu rasmi. Istilah Inggeris dibenarkan jika lazim (prompt, Gem, Canvas).
- **Alat utama peserta:** Gemini (akaun jabatan).

## 2. Peta fail: sunting yang mana?

| Mahu ubah | Sunting fail ini | Kemudian jalankan |
|---|---|---|
| Kandungan **slaid** (teks, prompt, nota penceramah, susunan) | `slaid/kandungan.py` | `python3 slaid/bina.py` |
| Rupa bentuk **slaid** (warna, saiz, susun atur) | `assets/slides.css` | tiada |
| Kelakuan **slaid** (kekunci, menu modul, pemasa, kuiz) | `assets/slides.js` | tiada |
| Jenis slaid baharu (layout baharu) | `slaid/bina.py` (fungsi `r_<jenis>`) + `assets/slides.css` | `python3 slaid/bina.py` |
| Gambar dalam slaid | letak dalam `slaid/img/`, rujuk sebagai `img/nama.jpg` dalam `kandungan.py` | `python3 slaid/bina.py` |
| Halaman nota **modul** | `modul-1.html`, `modul-2.html`, `modul-3.html`, `hands-on.html` | `python3 build.py` jika prompt berubah |
| **Prompt** dalam Bank Prompt | blok `<div class="prompt">` dalam halaman modul di atas | `python3 build.py` |
| Rupa Bank Prompt (bukan isi) | `prompt.template.html` | `python3 build.py` |
| Halaman utama, tentatif, pautan Pra-Ujian | `index.html` | tiada |
| Halaman menu slaid (tab, kad, bilangan slaid) | `slaid.html` | tiada |
| Menu atas, pil pantas, footer semua halaman | `assets/app.js` (tatasusunan `nav` dan blok `pills`) | tiada |
| Rupa hub (bukan slaid) | `assets/style.css` | tiada |

### Fail DIJANA: jangan sunting terus

Perubahan terus pada fail ini akan **hilang** apabila skrip dijalankan semula.

- `prompt.html` dijana oleh `build.py`.
- `slaid/modul-1.html`, `slaid/modul-2.html`, `slaid/modul-3.html`, `slaid/hands-on.html` dijana oleh `slaid/bina.py`.
- `slaid/md/*.md` dijana oleh `slaid/bina.py` (kandungan slaid dalam Markdown, termasuk arahan untuk menjana semula slaid dalam Gemini/ChatGPT).

## 3. Struktur folder

```
kursus-ai-jkr/
├── HANDOVER.md            fail ini
├── README.md              ringkasan pendek
├── index.html             utama + tentatif Hari 1
├── modul-1.html … hands-on.html   nota modul (sumber prompt)
├── prompt.template.html   templat Bank Prompt
├── prompt.html            DIJANA
├── build.py               jana prompt.html
├── slaid.html             menu slaid (pratonton iframe + kad)
├── assets/
│   ├── style.css, app.js        hub
│   └── slides.css, slides.js    enjin slaid
└── slaid/
    ├── kandungan.py       SUMBER kandungan semua slaid
    ├── bina.py            penjana slaid HTML + MD
    ├── img/               gambar slaid (foto-a/b/c.jpg: ujian foto AI, Modul 1)
    ├── md/                DIJANA
    └── modul-1.html …     DIJANA
```

## 4. Cara menyunting slaid (`slaid/kandungan.py`)

Setiap dek ialah `dict` (`M1`, `M2`, `M3`, `H1`) dengan senarai `slides`. Setiap slaid ialah `dict(t="<jenis>", ...)`.
Susunan dalam senarai = susunan slaid. Senarai `DECKS` di hujung fail menentukan dek yang dijana.

**Medan biasa untuk semua jenis:**
- `h` tajuk (HTML ringkas dibenarkan; `<em>perkataan</em>` = penekanan italik berwarna, `<b>`, `<code>`, `<br>`)
- `kicker` label kecil di atas tajuk; `sub` subtajuk; `note` nota kaki pada slaid
- `notes` nota penceramah (dipapar dengan kekunci N, tidak kelihatan kepada peserta)
- `menu` tajuk pendek dalam menu slaid (jika tiada, `h` digunakan)
- `visual` cadangan visual khusus untuk fail MD (pilihan)

**Jenis slaid dan medan khusus:**

| `t=` | Kegunaan | Medan khusus |
|---|---|---|
| `title` | Slaid tajuk modul (gelap) | `giant` (nombor besar), `eyebrow`, `pills` (senarai) |
| `section` | Pemisah seksyen (warna utama) | `giant`, `eyebrow`, `pills` |
| `big` | Pernyataan besar | `h`, `sub` |
| `quote` | Petikan | `h` (teks petikan), `src` (sumber) |
| `points` | Senarai bernombor | `items` = senarai `(tajuk, huraian)`; `style` = `""`, `"check"`, `"warn"` |
| `cards` | Grid kad | `cols` (2 hingga 5), `cards` = senarai `dict(lab, icon, h, p, hl=True/False, bigicon=True/False)` |
| `flow` | Aliran langkah | `steps` = senarai `(nombor, tajuk, huraian)`; `on` = indeks kotak gelap |
| `table` | Jadual | `head` (senarai), `rows` (senarai senarai) |
| `agenda` | Garis masa | `rows` = senarai `(masa, kod, perkara, jenis)`; jenis `"Cuba Sekarang"` diserlah emas |
| `act` | Aktiviti Cuba Sekarang | `prompt` = `(label, teks)` atau senarai beberapa `(label, teks)`; `steps`; `min` (pemasa minit); `follow` = senarai `(label, teks)`; `badge`; `size` = `""`, `"sm"`, `"xs"` untuk prompt panjang |
| `compare` | Sebelum / selepas | `bad`, `good` = `dict(label, pre, p)` |
| `lights` | Lampu isyarat data | `items` = senarai `(g/y/r, tajuk, huraian)` |
| `quiz` | Kuiz klik-dedah | `items` = senarai `(senario, g/y/r, sebab)` |
| `guess` | Teka foto (klik-dedah) | `items` = senarai `(label, "img/fail.jpg", jawapan, butiran)` |
| `anatomy` | Lakaran surat berlabel | `doc` = baris `(no, jenis, teks)`; `legend` = `(no, teks)` |
| `email` | Lakaran e-mel | `mail` = `dict(to, subj, first, body)`; `www` = senarai `(tajuk, kecil)` |
| `case` | Senario kes + peta | `facts` = senarai `(ikon, label, teks)` |
| `memo` | Nota tulisan tangan | `memo` (teks, `<mark>` serlah, `<mark class="r">` merah), `side` = `(ikon, tajuk, huraian)` |
| `close` | Rumusan + modul seterusnya | `items` = `(nombor, tajuk, huraian)`; `next` = `(teks, pautan, label butang)` |

**Ikon yang tersedia** (untuk `icon` / ikon fakta): text, image, music, video, eye, check, x, alert, clock, mail, users, user, spark, slides, shield, cpu, trend, list, chat, hat, gem, search, pen, target, map, cal, route, cone, globe, lock, repeat, link, q. Ikon baharu ditambah dalam `ICONS` di `slaid/bina.py`.

**Label prompt** `Peranan:`, `Konteks:`, `Tugasan:`, `Output:`, `Kekangan:`, `Templat:`, `Nota:`, `Susulan:` pada awal baris akan diwarnakan secara automatik.

### Contoh: tambah satu slaid aktiviti selepas slaid tertentu

```python
dict(t="act", h="Ringkaskan pekeliling", min=8, menu="CS-X: Ringkasan",
     steps=["Tampal teks pekeliling awam.", "Jalankan prompt.", "Semak angka dan tarikh."],
     prompt=("CS-X &middot; Teks", "Peranan: Anda pegawai tadbir JKR.\nTugasan: Ringkaskan teks di bawah dalam 5 poin.\nKekangan: Jangan tambah maklumat baharu."),
     notes="Nota untuk penceramah."),
```

### Menambah dek slaid baharu (contoh Modul 4)

1. `slaid/kandungan.py`: cipta `M4 = dict(file="modul-4.html", label="Modul 4 &middot; ...", title=..., desc=..., slides=[...])` dan tambah ke `DECKS`.
2. `assets/slides.js`: tambah baris dalam tatasusunan `DECKS` di atas fail (menu modul dalam slaid).
3. `slaid.html`: tambah butang tab (`data-deck="modul-4"`), kad dalam grid, dan nama dalam senarai semakan hash di skrip bawah.
4. Jalankan `python3 slaid/bina.py`.

## 5. Peraturan gaya dan kandungan (wajib)

- **Data rekaan sahaja.** Tiada nama sebenar orang awam, nombor IC, akaun bank atau dokumen terperingkat. Nama tempat contoh: Jalan Kg. Contoh, Rembau; Syarikat Contoh Sdn Bhd.
- **Prinsip kursus:** "AI mencadang, manusia memutuskan." Setiap aktiviti berakhir dengan semakan manusia.
- **Formula prompt rasmi:** Peranan + Konteks + Tugasan + Output + Kekangan (tahap ringkas: Siapa + Apa + Cara). Kekalkan konsisten di semua halaman.
- **Kod aktiviti:** CS1 hingga CS11 (Modul 1 hingga 3), H1-1 hingga H1-6 (Hands-on). Kod yang sama mesti sepadan antara halaman modul, Bank Prompt dan slaid.
- **Tiada em dash (—).** Guna koma, titik bertindih atau ayat berasingan. Julat guna tanda sempang biasa (8.30-9.30).
- **Fakta dan sumber:** jangan reka nombor pekeliling, statistik atau sumber. Jika tidak pasti, tandakan untuk disemak pemilik.
- **Prompt dalam slaid dan halaman modul mesti sama.** Jika mengubah prompt CS dalam `modul-*.html`, kemas kini juga slaid yang sepadan dalam `slaid/kandungan.py` (dan sebaliknya).

## 6. Uji secara setempat sebelum push

```bash
cd ~/Documents/"JKRCreate Petabyte"/kursus-ai-jkr
python3 build.py            # jika prompt modul berubah
python3 slaid/bina.py       # jika slaid berubah
python3 -m http.server 8000 # buka http://localhost:8000 dalam pelayar
```

Senarai semak:
- [ ] `slaid.html`: setiap tab memaparkan dek dalam bingkai pratonton.
- [ ] Dalam slaid: anak panah, M (menu modul), O (semua slaid), N (nota), F (skrin penuh) berfungsi.
- [ ] Butang **Salin** pada slaid aktiviti menyalin prompt.
- [ ] Tiada teks melimpah keluar slaid (paling kerap pada slaid `act` dengan prompt panjang; guna `size="sm"` atau `"xs"`).
- [ ] Bilangan slaid dalam kad `slaid.html` sepadan dengan output `bina.py`.
- [ ] `grep -rn "—" --include=*.html --include=*.py --include=*.md .` tidak memulangkan apa-apa.

## 7. Push

```bash
git add -A
git commit -m "Ringkasan perubahan"
git push
```

GitHub Pages mengemas kini dalam 1 hingga 2 minit. `__pycache__/` dan `.DS_Store` telah diabaikan dalam `.gitignore`.

## 8. Perkara terbuka

- Ujian foto AI (Modul 1, slaid "Yang mana foto asli?"): padanan foto A, B, C kepada Gemini Thinking, Flash, Pro diandaikan mengikut susunan muat naik. Sahkan dan ubah dalam `kandungan.py` jika perlu.
- Semakan SynthID dalam Gemini (nota penceramah Modul 1): sahkan ciri tersedia pada akaun jabatan sebelum demo.
- Kuiz CS3: enam senario ditulis untuk slaid; sahkan selaras dengan dasar data jabatan.
- Anatomi surat (Modul 3): cogan kata dan format ialah contoh; selaraskan dengan templat rasmi JKR.
- Hari 2 (Modul 4, Modul 5) belum ada dalam laman ini; bahan oleh PM Ts Dr Mohd Shahizan Othman.
