// Enjin slaid Kursus AI JKR: navigasi, menu modul, nota penceramah, paparan keseluruhan, pemasa, salin prompt.
(function () {
  const DECKS = [
    ["modul-1.html", "Modul 1", "Asas AI"],
    ["modul-2.html", "Modul 2", "Seni Membina Prompt"],
    ["modul-3.html", "Modul 3", "Komunikasi & Dokumentasi"],
    ["hands-on.html", "Hands-on 1", "Minit Mesyuarat"],
  ];
  const IC = {
    menu: '<path d="M4 6h16M4 12h16M4 18h16"/>',
    prev: '<path d="m15 18-6-6 6-6"/>',
    next: '<path d="m9 18 6-6-6-6"/>',
    grid: '<rect x="3" y="3" width="7" height="7" rx="1.5"/><rect x="14" y="3" width="7" height="7" rx="1.5"/><rect x="3" y="14" width="7" height="7" rx="1.5"/><rect x="14" y="14" width="7" height="7" rx="1.5"/>',
    notes: '<path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><path d="M14 2v6h6M16 13H8M16 17H8"/>',
    full: '<path d="M8 3H5a2 2 0 0 0-2 2v3M21 8V5a2 2 0 0 0-2-2h-3M3 16v3a2 2 0 0 0 2 2h3M16 21h3a2 2 0 0 0 2-2v-3"/>',
    print: '<path d="M6 9V2h12v7M6 18H4a2 2 0 0 1-2-2v-5a2 2 0 0 1 2-2h16a2 2 0 0 1 2 2v5a2 2 0 0 1-2 2h-2"/><rect x="6" y="14" width="12" height="8"/>',
    home: '<path d="m3 10 9-7 9 7v10a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/><path d="M9 22V12h6v10"/>',
  };
  const svg = (k) => `<svg class="ic" viewBox="0 0 24 24" aria-hidden="true">${IC[k]}</svg>`;
  const store = { get(k) { try { return localStorage.getItem(k); } catch (e) { return null; } } };

  const root = document.documentElement;
  const pal = store.get("palette");
  if (pal && pal !== "biru") root.dataset.palette = pal;

  const embed = window.self !== window.top || /[?&]embed/.test(location.search);
  if (embed) document.body.classList.add("embed");

  const stage = document.querySelector(".stage");
  const slides = [...stage.querySelectorAll(".slide")];
  const here = location.pathname.split("/").pop() || "";
  const deckTitle = document.body.dataset.deck || document.title;
  let cur = 0;

  // Skala pentas
  const fit = () => {
    const s = Math.min(innerWidth / 1280, innerHeight / 720);
    stage.style.transform = `translate(-50%,-50%) scale(${s})`;
  };
  addEventListener("resize", fit); addEventListener("load", fit); fit(); requestAnimationFrame(fit);
  if (window.ResizeObserver) new ResizeObserver(fit).observe(document.documentElement);

  // Kawalan
  const ctrl = document.createElement("div");
  ctrl.className = "ctrl";
  ctrl.innerHTML = `
    <button data-a="menu" title="Menu slaid (M)" aria-label="Menu slaid">${svg("menu")}</button>
    <button data-a="prev" title="Sebelum (←)" aria-label="Slaid sebelum">${svg("prev")}</button>
    <span class="cnt" aria-live="polite"></span>
    <button data-a="next" title="Seterusnya (→)" aria-label="Slaid seterusnya">${svg("next")}</button>
    <button data-a="grid" title="Semua slaid (O)" aria-label="Paparan semua slaid">${svg("grid")}</button>
    <button data-a="notes" title="Nota penceramah (N)" aria-label="Nota penceramah">${svg("notes")}</button>
    <button data-a="full" title="Skrin penuh (F)" aria-label="Skrin penuh">${svg("full")}</button>
    <button data-a="print" title="Cetak / simpan PDF" aria-label="Cetak atau simpan PDF">${svg("print")}</button>`;
  document.body.append(ctrl);
  const cnt = ctrl.querySelector(".cnt");

  const top = document.createElement("div");
  top.className = "toplink";
  top.innerHTML = `<button data-a="menu">${svg("menu")} Modul &amp; slaid</button>`;
  document.body.append(top);

  // Laci menu: tukar modul + senarai slaid
  const scrim = document.createElement("div"); scrim.className = "scrim";
  const drawer = document.createElement("nav");
  drawer.className = "drawer"; drawer.setAttribute("aria-label", "Menu slaid");
  drawer.innerHTML = `
    <header><p>Slaid Kursus AI JKR</p><h4>${deckTitle}</h4></header>
    <div class="mods">${DECKS.map(([h, a, b]) => `<a href="${h}"${h === here ? ' aria-current="page"' : ""}>${a}<small>${b}</small></a>`).join("")}</div>
    <div class="links"><a href="../slaid.html">Semua slaid</a><a href="../index.html">Hub kursus</a><a href="../prompt.html">Bank Prompt</a><a href="md/${here.replace(".html", ".md")}">Fail MD</a></div>
    <ol>${slides.map((s, i) => `<li class="${s.classList.contains("section") || s.classList.contains("title-slide") ? "sec" : ""}"><button data-go="${i}"><span>${String(i + 1).padStart(2, "0")}</span>${s.dataset.title || "Slaid " + (i + 1)}</button></li>`).join("")}</ol>`;
  document.body.append(scrim, drawer);
  const openDrawer = (on) => { drawer.classList.toggle("open", on); scrim.classList.toggle("on", on); };

  // Nota penceramah
  const notes = document.createElement("div"); notes.className = "notes-panel";
  document.body.append(notes);

  // Paparan keseluruhan
  const ov = document.createElement("div"); ov.className = "overview";
  document.body.append(ov);
  let ovBuilt = false;
  const buildOv = () => {
    ov.innerHTML = `<h4>${deckTitle} &middot; ${slides.length} slaid</h4><div class="ov-grid"></div>`;
    const g = ov.querySelector(".ov-grid");
    slides.forEach((s, i) => {
      const it = document.createElement("div"); it.className = "ov-item"; it.dataset.go = i;
      const th = document.createElement("div"); th.className = "ov-thumb";
      const c = s.cloneNode(true); c.classList.add("active"); c.removeAttribute("id");
      th.append(c); it.append(th);
      const p = document.createElement("p"); p.textContent = `${i + 1}. ${s.dataset.title || ""}`; it.append(p);
      g.append(it);
    });
    ovBuilt = true;
  };
  const scaleOv = () => ov.querySelectorAll(".ov-thumb").forEach((t) => { t.firstChild.style.transform = `scale(${t.clientWidth / 1280})`; });
  const toggleOv = (on) => {
    if (on && !ovBuilt) buildOv();
    ov.classList.toggle("on", on);
    if (on) {
      scaleOv();
      ov.querySelectorAll(".ov-item").forEach((x, i) => x.classList.toggle("cur", i === cur));
      const c = ov.querySelector(".ov-item.cur"); if (c) c.scrollIntoView({ block: "center" });
    }
  };
  addEventListener("resize", () => { if (ov.classList.contains("on")) scaleOv(); });

  const show = (i, push = true) => {
    cur = Math.max(0, Math.min(slides.length - 1, i));
    slides.forEach((s, k) => s.classList.toggle("active", k === cur));
    cnt.textContent = `${cur + 1} / ${slides.length}`;
    drawer.querySelectorAll("[data-go]").forEach((b) => b.classList.toggle("cur", +b.dataset.go === cur));
    const n = slides[cur].querySelector("aside.notes");
    notes.innerHTML = `<p class="h">Nota penceramah &middot; slaid ${cur + 1}</p>${n ? n.innerHTML : "<p>Tiada nota.</p>"}`;
    if (push) history.replaceState(null, "", "#" + (cur + 1));
  };
  const go = (d) => show(cur + d);

  const act = (a) => {
    if (a === "next") go(1);
    if (a === "prev") go(-1);
    if (a === "menu") openDrawer(!drawer.classList.contains("open"));
    if (a === "grid") toggleOv(!ov.classList.contains("on"));
    if (a === "notes") notes.classList.toggle("on");
    if (a === "full") {
      if (!document.fullscreenElement) document.documentElement.requestFullscreen && document.documentElement.requestFullscreen();
      else document.exitFullscreen();
    }
    if (a === "print") window.print();
  };
  document.addEventListener("click", (e) => {
    const b = e.target.closest("[data-a]"); if (b) { act(b.dataset.a); return; }
    const g = e.target.closest("[data-go]");
    if (g) { show(+g.dataset.go); openDrawer(false); toggleOv(false); return; }
    if (e.target === scrim) openDrawer(false);
  });

  document.addEventListener("keydown", (e) => {
    if (e.target.closest("input,textarea") || e.metaKey || e.ctrlKey || e.altKey) return;
    const k = e.key;
    if (["ArrowRight", "PageDown", " ", "Enter"].includes(k)) { e.preventDefault(); go(1); }
    else if (["ArrowLeft", "PageUp", "Backspace"].includes(k)) { e.preventDefault(); go(-1); }
    else if (k === "Home") show(0);
    else if (k === "End") show(slides.length - 1);
    else if (k === "m" || k === "M") act("menu");
    else if (k === "o" || k === "O") act("grid");
    else if (k === "n" || k === "N") act("notes");
    else if (k === "f" || k === "F") act("full");
    else if (k === "Escape") { openDrawer(false); toggleOv(false); notes.classList.remove("on"); }
  });

  // Leret di skrin sentuh
  let sx = null, sy = null;
  stage.addEventListener("touchstart", (e) => { sx = e.touches[0].clientX; sy = e.touches[0].clientY; }, { passive: true });
  stage.addEventListener("touchend", (e) => {
    if (sx === null) return;
    const dx = e.changedTouches[0].clientX - sx, dy = e.changedTouches[0].clientY - sy;
    if (Math.abs(dx) > 50 && Math.abs(dx) > Math.abs(dy)) go(dx < 0 ? 1 : -1);
    sx = null;
  });

  // Sembunyi kawalan apabila tetikus diam
  let idle;
  const wake = () => { document.body.classList.remove("idle"); clearTimeout(idle); idle = setTimeout(() => document.body.classList.add("idle"), 2800); };
  addEventListener("mousemove", wake); wake();

  // Salin prompt
  stage.querySelectorAll(".code").forEach((c) => {
    const btn = c.querySelector(".copy"); const pre = c.querySelector("pre");
    if (!btn || !pre) return;
    btn.addEventListener("click", async (e) => {
      e.stopPropagation();
      const t = pre.innerText;
      try { await navigator.clipboard.writeText(t); }
      catch (err) { const ta = document.createElement("textarea"); ta.value = t; document.body.append(ta); ta.select(); document.execCommand("copy"); ta.remove(); }
      btn.textContent = "Disalin"; btn.classList.add("done");
      setTimeout(() => { btn.textContent = "Salin"; btn.classList.remove("done"); }, 1600);
    });
  });

  // Kuiz: klik untuk dedah jawapan
  stage.querySelectorAll(".qz,.gf").forEach((q) => q.addEventListener("click", () => q.classList.toggle("show")));

  // Pemasa aktiviti
  stage.querySelectorAll(".timer").forEach((t) => {
    const total = +t.dataset.min * 60; let left = total, iv = null;
    const out = t.querySelector("span");
    const fmt = (s) => `${Math.floor(s / 60)}:${String(s % 60).padStart(2, "0")}`;
    out.textContent = fmt(left);
    t.addEventListener("click", () => {
      if (t.classList.contains("end")) { left = total; t.classList.remove("end"); out.textContent = fmt(left); return; }
      if (iv) { clearInterval(iv); iv = null; t.classList.remove("run"); return; }
      t.classList.add("run");
      iv = setInterval(() => {
        left--; out.textContent = fmt(Math.max(0, left));
        if (left <= 0) { clearInterval(iv); iv = null; t.classList.remove("run"); t.classList.add("end"); out.textContent = "Masa tamat"; }
      }, 1000);
    });
  });

  const h = parseInt(location.hash.slice(1), 10);
  show(isNaN(h) ? 0 : h - 1, false);
})();
