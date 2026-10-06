// Header, footer, alat paparan, salin prompt, carian.
(function () {
  const page = document.body.dataset.page || "";
  const nav = [
    ["index.html", "Utama", "utama"],
    ["modul-1.html", "Modul 1", "m1"],
    ["modul-2.html", "Modul 2", "m2"],
    ["modul-3.html", "Modul 3", "m3"],
    ["hands-on.html", "Hands-on 1", "h1"],
    ["slaid.html", "Slaid", "slaid"],
  ];
  const store = {
    get(k) { try { return localStorage.getItem(k); } catch (e) { return null; } },
    set(k, v) { try { localStorage.setItem(k, v); } catch (e) {} },
  };

  const palettes = [
    ["biru", "Biru Rasmi", ["#084c9e", "#062f63", "#d52b32", "#f3bd2d"]],
    ["hijau", "Hijau Hutan", ["#1b7a4b", "#0f3d2a", "#c2410c", "#e9b949"]],
    ["teal", "Teal Laut", ["#0f766e", "#134e4a", "#e11d48", "#f59e0b"]],
    ["ungu", "Ungu Diraja", ["#5b3cc4", "#2e1a6b", "#db2777", "#f2c14e"]],
    ["bata", "Bata Senja", ["#b4462b", "#4a1d12", "#1d4ed8", "#e0a526"]],
    ["korporat", "Kelabu Korporat", ["#334155", "#0f172a", "#0284c7", "#eab308"]],
  ];
  const header = document.createElement("header");
  header.className = "site";
  header.innerHTML = `
    <div class="wrap bar">
      <a class="brand" href="index.html"><span class="logo">AI</span>
        <span><b>Kursus AI JKR</b><small>Aplikasi AI dalam Tugas Rasmi</small></span></a>
      <nav class="main" id="mainnav">
        ${nav.map(([h, t, k]) => `<a href="${h}"${k === page ? ' aria-current="page"' : ""}>${t}</a>`).join("")}
        <a class="cta" href="prompt.html"${page === "prompt" ? ' aria-current="page"' : ""}>Bank Prompt &#8599;</a>
      </nav>
      <div class="tools">
        <button type="button" data-act="minus" title="Kecilkan teks" aria-label="Kecilkan teks">A&minus;</button>
        <button type="button" data-act="plus" title="Besarkan teks" aria-label="Besarkan teks">A+</button>
        <span class="palette-wrap"><button type="button" data-act="palette" title="Pilih palet warna" aria-label="Pilih palet warna" aria-expanded="false" aria-controls="palpop"><svg viewBox="0 0 16 16" aria-hidden="true"><circle cx="5" cy="6" r="2.2" fill="currentColor"/><circle cx="11" cy="6" r="2.2" fill="currentColor" opacity=".6"/><circle cx="8" cy="11" r="2.2" fill="currentColor" opacity=".35"/></svg></button><div class="palette-pop" id="palpop" hidden><p>Palet warna</p>${palettes.map(([k, n, c]) => `<button type="button" class="sw" data-pal="${k}" aria-pressed="false"><i>${c.map((x) => `<b style="background:${x}"></b>`).join("")}</i>${n}</button>`).join("")}</div></span>
        <button type="button" data-act="theme" title="Mod gelap" aria-label="Tukar mod gelap"><svg viewBox="0 0 16 16" aria-hidden="true"><circle cx="8" cy="8" r="6.5" fill="none" stroke="currentColor" stroke-width="1.5"/><path d="M8 1.5a6.5 6.5 0 0 1 0 13z" fill="currentColor"/></svg></button>
        <button type="button" class="menu-btn" data-act="menu" aria-label="Menu"><svg viewBox="0 0 16 16" aria-hidden="true"><path d="M2 4h12M2 8h12M2 12h12" stroke="currentColor" stroke-width="1.6"/></svg></button>
      </div>
    </div>
    <div class="wrap pills">
      <a class="pill-hot" href="https://forms.gle/FSYdBjMboPMZMFoG7" target="_blank" rel="noopener">Pra-Ujian &#8599;</a>
      <a href="index.html#tentatif">Tentatif</a>
      <a href="slaid.html">Slaid</a>
      <a href="modul-1.html">Asas AI</a>
      <a href="modul-2.html#formula">Formula Prompt</a>
      <a href="modul-3.html">Surat, Laporan, Slaid</a>
      <a href="modul-3.html#video">Video AI</a>
      <a href="hands-on.html">Minit Mesyuarat</a>
      <a href="modul-1.html#keselamatan">Keselamatan Data</a>
      <a href="prompt.html">Bank Prompt</a>
    </div>`;
  document.body.prepend(header);
  const bar = document.createElement("div");
  bar.className = "progress";
  document.body.prepend(bar);

  const footer = document.createElement("footer");
  footer.innerHTML = `<div class="wrap">
    <p><b>Kursus Aplikasi AI dalam Tugas Rasmi</b> &middot; 7-8 Oktober 2026 &middot; CREaTE, JKR</p>
    <p>Hari 1: PM Dr Mohd Murtadha Mohamad (penceramah), PM Ts Dr Mohd Shahizan Othman (fasilitator), Fakulti Komputeran, Universiti Teknologi Malaysia.</p>
    <p>Semua contoh dalam laman ini menggunakan data rekaan. AI mencadang, manusia menyemak dan memutuskan.</p>
  </div>`;
  document.body.append(footer);
  const top = document.createElement("button");
  top.className = "totop"; top.setAttribute("aria-label", "Ke atas"); top.innerHTML = "&uarr;";
  top.onclick = () => window.scrollTo({ top: 0 });
  document.body.append(top);

  const root = document.documentElement;
  let scale = parseFloat(store.get("fs") || "1");
  const applyScale = () => root.style.setProperty("--font-scale", scale);
  applyScale();
  const pop = header.querySelector("#palpop");
  const palBtn = header.querySelector('[data-act="palette"]');
  const setPalette = (k) => {
    if (k && k !== "biru") root.dataset.palette = k; else delete root.dataset.palette;
    pop.querySelectorAll(".sw").forEach((b) => b.setAttribute("aria-pressed", String(b.dataset.pal === (k || "biru"))));
  };
  setPalette(store.get("palette"));
  pop.addEventListener("click", (e) => {
    const b = e.target.closest(".sw"); if (!b) return;
    setPalette(b.dataset.pal); store.set("palette", b.dataset.pal);
  });
  const closePop = () => { pop.hidden = true; palBtn.setAttribute("aria-expanded", "false"); };
  document.addEventListener("click", (e) => { if (!e.target.closest(".palette-wrap")) closePop(); });
  document.addEventListener("keydown", (e) => { if (e.key === "Escape") closePop(); });
  const savedTheme = store.get("theme");
  if (savedTheme) root.dataset.theme = savedTheme;
  else if (window.matchMedia && matchMedia("(prefers-color-scheme: dark)").matches) root.dataset.theme = "dark";

  header.addEventListener("click", (e) => {
    const b = e.target.closest("button"); if (!b) return;
    const a = b.dataset.act;
    if (a === "plus") scale = Math.min(1.3, +(scale + 0.1).toFixed(1));
    if (a === "minus") scale = Math.max(0.9, +(scale - 0.1).toFixed(1));
    if (a === "plus" || a === "minus") { applyScale(); store.set("fs", scale); }
    if (a === "theme") { root.dataset.theme = root.dataset.theme === "dark" ? "light" : "dark"; store.set("theme", root.dataset.theme); }
    if (a === "palette") { pop.hidden = !pop.hidden; palBtn.setAttribute("aria-expanded", String(!pop.hidden)); }
    if (a === "menu") document.getElementById("mainnav").classList.toggle("open");
  });

  const onScroll = () => {
    const h = document.documentElement.scrollHeight - innerHeight;
    root.style.setProperty("--scroll", (h > 0 ? (scrollY / h) * 100 : 0) + "%");
    top.classList.toggle("show", scrollY > 500);
  };
  addEventListener("scroll", onScroll, { passive: true }); onScroll();

  // Butang salin pada setiap prompt
  document.querySelectorAll(".prompt").forEach((p) => {
    const pre = p.querySelector("pre"); const head = p.querySelector(".prompt-head");
    if (!pre || !head) return;
    const btn = document.createElement("button");
    btn.className = "copy"; btn.type = "button"; btn.textContent = "Salin";
    btn.onclick = async () => {
      const text = pre.innerText;
      try { await navigator.clipboard.writeText(text); }
      catch (e) { const t = document.createElement("textarea"); t.value = text; document.body.append(t); t.select(); document.execCommand("copy"); t.remove(); }
      btn.textContent = "Disalin"; btn.classList.add("done");
      setTimeout(() => { btn.textContent = "Salin"; btn.classList.remove("done"); }, 1600);
    };
    head.append(btn);
  });

  // Carian dan penapis (Bank Prompt)
  const q = document.getElementById("q");
  if (q) {
    const items = [...document.querySelectorAll(".prompt")];
    const empty = document.querySelector(".empty");
    let cat = "semua";
    const run = () => {
      const s = q.value.trim().toLowerCase(); let n = 0;
      items.forEach((it) => {
        const ok = (cat === "semua" || it.dataset.cat.includes(cat)) && (!s || it.innerText.toLowerCase().includes(s));
        it.hidden = !ok; if (ok) n++;
      });
      if (empty) empty.style.display = n ? "none" : "block";
    };
    q.addEventListener("input", run);
    document.querySelectorAll(".filters button").forEach((b) => b.addEventListener("click", () => {
      document.querySelectorAll(".filters button").forEach((x) => x.classList.remove("on"));
      b.classList.add("on"); cat = b.dataset.cat; run();
    }));
  }
})();
