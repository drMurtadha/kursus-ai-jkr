# Kursus Aplikasi AI dalam Tugas Rasmi: Hari 1

Hub web Hari 1 (7 Oktober 2026) untuk kursus JKRCreate di CREaTE.
Penceramah: PM Dr Mohd Murtadha Mohamad. Fasilitator: PM Ts Dr Mohd Shahizan Othman (UTM).

## Halaman

| Fail | Kandungan |
| --- | --- |
| `index.html` | Utama, tentatif Hari 1, persediaan |
| `modul-1.html` | Asas AI dan Generative AI, keselamatan data |
| `modul-2.html` | Seni membina prompt |
| `modul-3.html` | Surat, e-mel, laporan, slaid, video AI |
| `hands-on.html` | Hands-on 1: minit mesyuarat |
| `prompt.html` | Bank Prompt (dijana, jangan sunting terus) |
| `slaid.html` | Menu slaid: pratonton dan pautan setiap dek |
| `slaid/*.html` | Slaid Modul 1, 2, 3 dan Hands-on 1 (dijana) |
| `slaid/md/*.md` | Kandungan slaid dalam Markdown, untuk Gemini/ChatGPT |

## Mengemas kini prompt

Prompt hanya ditulis dalam halaman modul dan `hands-on.html`. Selepas menyunting, jalankan:

```
python3 build.py
```

## Mengemas kini slaid

Sunting `slaid/kandungan.py`, kemudian jalankan:

```
python3 slaid/bina.py
```

Kekunci dalam slaid: anak panah (tukar slaid), M (menu modul), O (semua slaid), N (nota penceramah), F (skrin penuh). Butang cetak menyimpan dek sebagai PDF, satu slaid satu halaman.

## Terbit di GitHub Pages

Settings, Pages, Deploy from a branch, `main`, folder `/ (root)`.

Semua contoh menggunakan data rekaan.
