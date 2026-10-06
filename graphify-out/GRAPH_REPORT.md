# Graph Report - kursus-ai-jkr  (2026-10-06)

## Corpus Check
- 15 files · ~73,642 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 149 nodes · 169 edges · 15 communities
- Extraction: 99% EXTRACTED · 1% INFERRED · 0% AMBIGUOUS · INFERRED: 1 edges (avg confidence: 0.5)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `1c19b64d`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- bina.py
- Modul 1: Asas AI dan Generative AI
- Modul 3: AI untuk Komunikasi, Dokumentasi dan Mesyuarat
- Hands-on 1: Bina Minit Mesyuarat menggunakan Prompt AI
- Modul 2: Seni Membina Prompt
- HANDOVER: Laman Kursus AI JKR (untuk manusia dan AI)
- Kursus Aplikasi AI dalam Tugas Rasmi: Hari 1
- build.py
- P
- Ilustrasi Modul 1

## God Nodes (most connected - your core abstractions)
1. `Modul 1: Asas AI dan Generative AI` - 24 edges
2. `Modul 3: AI untuk Komunikasi, Dokumentasi dan Mesyuarat` - 21 edges
3. `Hands-on 1: Bina Minit Mesyuarat menggunakan Prompt AI` - 16 edges
4. `Modul 2: Seni Membina Prompt` - 16 edges
5. `head()` - 15 edges
6. `note()` - 10 edges
7. `HANDOVER: Laman Kursus AI JKR (untuk manusia dan AI)` - 9 edges
8. `ic()` - 6 edges
9. `Kursus Aplikasi AI dalam Tugas Rasmi: Hari 1` - 5 edges
10. `Ilustrasi Modul 1` - 5 edges

## Surprising Connections (you probably didn't know these)
- None detected - all connections are within the same source files.

## Import Cycles
- None detected.

## Communities (15 total, 0 thin omitted)

### Community 0 - "bina.py"
Cohesion: 0.17
Nodes (23): build_deck(), code_html(), head(), ic(), md_body(), note(), r_act(), r_agenda() (+15 more)

### Community 1 - "Modul 1: Asas AI dan Generative AI"
Cohesion: 0.08
Nodes (24): Modul 1: Asas AI dan Generative AI, Slaid 10: Apa itu *AI*?, Slaid 11: AI ialah pembantu digital yang menghasilkan cadangan berdasarkan arahan kita., Slaid 12: Pembantu baharu yang *sangat rajin*, Slaid 13: Tidak semua AI adalah *AI generatif*, Slaid 14: Satu alat, *lima jenis* hasil, Slaid 15: Gemini alat utama; yang lain untuk *perbandingan*, Slaid 16: Setiap jawatan ada *kegunaan* sendiri (+16 more)

### Community 2 - "Modul 3: AI untuk Komunikasi, Dokumentasi dan Mesyuarat"
Cohesion: 0.09
Nodes (21): Modul 3: AI untuk Komunikasi, Dokumentasi dan Mesyuarat, Slaid 10: Struktur laporan, Slaid 11: CS9: Laporan daripada gambar, Slaid 12: AI menghurai, pegawai menilai, Slaid 13: Laporan kepada *taklimat*, Slaid 14: CS10: Taklimat 5 slaid, Slaid 15: Video *AI*, Slaid 16: Formula video (+13 more)

### Community 3 - "Hands-on 1: Bina Minit Mesyuarat menggunakan Prompt AI"
Cohesion: 0.12
Nodes (16): Hands-on 1: Bina Minit Mesyuarat menggunakan Prompt AI, Slaid 10: Langkah 5: Semakan kendiri, Slaid 11: Langkah 6: E-mel dan infografik, Slaid 12: Rubrik semakan, Slaid 13: Tiga minit, *tiga* perkara, Slaid 14: Bina Gem sendiri, Slaid 15: Satu tugas, satu prompt, *minggu depan*, Slaid 1: Bina *minit mesyuarat* menggunakan prompt AI (+8 more)

### Community 4 - "Modul 2: Seni Membina Prompt"
Cohesion: 0.12
Nodes (16): Modul 2: Seni Membina Prompt, Slaid 10: CS5: Aktiviti, Slaid 11: Empat teknik untuk *kerja pejabat*, Slaid 12: Kesilapan *biasa*, Slaid 13: CS6: Infografik, Slaid 14: Sebelum guna, *semak* lima perkara, Slaid 15: Prompt yang baik ialah *arahan kerja* yang baik, Slaid 1: Seni Membina *Prompt* (+8 more)

### Community 5 - "HANDOVER: Laman Kursus AI JKR (untuk manusia dan AI)"
Cohesion: 0.15
Nodes (12): 1. Ringkasan projek, 2. Peta fail: sunting yang mana?, 3. Struktur folder, 4. Cara menyunting slaid (`slaid/kandungan.py`), 5. Peraturan gaya dan kandungan (wajib), 6. Uji secara setempat sebelum push, 7. Push, 8. Perkara terbuka (+4 more)

### Community 6 - "Kursus Aplikasi AI dalam Tugas Rasmi: Hari 1"
Cohesion: 0.33
Nodes (5): Halaman, Kursus Aplikasi AI dalam Tugas Rasmi: Hari 1, Mengemas kini prompt, Mengemas kini slaid, Terbit di GitHub Pages

### Community 7 - "build.py"
Cohesion: 0.50
Nodes (4): blocks(), main(), Jana prompt.html daripada blok .prompt dalam halaman modul.  Sumber tunggal: kem, Pulangkan setiap <div class="prompt">...</div> lengkap (div bersarang dikira).

### Community 9 - "P"
Cohesion: 0.67
Nodes (3): P(), r_title(), Teks dengan HTML ringkas dibenarkan (b, em, code).

### Community 14 - "Ilustrasi Modul 1"
Cohesion: 0.33
Nodes (5): data-selamat.jpg, Ilustrasi Modul 1, manusia-ai.jpg, pejabat-ai.jpg, tapak-selamat.jpg

## Knowledge Gaps
- **90 isolated node(s):** `1. Ringkasan projek`, `Fail DIJANA: jangan sunting terus`, `3. Struktur folder`, `Contoh: tambah satu slaid aktiviti selepas slaid tertentu`, `Menambah dek slaid baharu (contoh Modul 4)` (+85 more)
  These have ≤1 connection - possible missing edges or undocumented components.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **What connects `Jana prompt.html daripada blok .prompt dalam halaman modul.  Sumber tunggal: kem`, `Pulangkan setiap <div class="prompt">...</div> lengkap (div bersarang dikira).`, `Jana slaid HTML dan fail MD daripada kandungan.py.  Sumber tunggal: sunting slai` to the rest of the system?**
  _94 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `Modul 1: Asas AI dan Generative AI` be split into smaller, more focused modules?**
  _Cohesion score 0.08 - nodes in this community are weakly interconnected._
- **Should `Modul 3: AI untuk Komunikasi, Dokumentasi dan Mesyuarat` be split into smaller, more focused modules?**
  _Cohesion score 0.09090909090909091 - nodes in this community are weakly interconnected._
- **Should `Hands-on 1: Bina Minit Mesyuarat menggunakan Prompt AI` be split into smaller, more focused modules?**
  _Cohesion score 0.11764705882352941 - nodes in this community are weakly interconnected._
- **Should `Modul 2: Seni Membina Prompt` be split into smaller, more focused modules?**
  _Cohesion score 0.11764705882352941 - nodes in this community are weakly interconnected._