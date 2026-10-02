(function () {
  const page = document.body.dataset.page;
  const nav = [
    ["index.html", "Anasayfa", "home"],
    ["takimlar.html", "Takımlar", "rides"],
    ["https://www.parklunasan.com.tr/yedek-parca.pdf", "Çarpışan Oto Yedek Parça", "parts"],
    ["kurumsal.html", "Park Lunasan", "about"],
    ["ik.html", "İK", "jobs"],
    ["defter.html", "Ziyaretçi Defteri", "book"],
    ["iletisim.html", "İletişim", "contact"],
  ];

  const header = document.getElementById("chrome-header");
  header.className = "site-header";
  header.innerHTML =
    '<a class="brand" href="index.html">Park Lunasan</a>' +
    '<button class="menu-toggle" type="button" aria-expanded="false">Menü</button>' +
    '<nav class="site-nav">' +
    nav
      .map(function (item) {
        const external = item[0].indexOf("http") === 0;
        const current = item[2] === page ? ' aria-current="page"' : "";
        const extra = external ? ' target="_blank" rel="noopener"' : "";
        return '<a href="' + item[0] + '"' + extra + current + ">" + item[1] + "</a>";
      })
      .join("") +
    "</nav>" +
    '<a class="phone" href="tel:+905323445274">0532 344 5274</a>';

  header.querySelector(".menu-toggle").addEventListener("click", function () {
    const open = header.classList.toggle("nav-open");
    this.setAttribute("aria-expanded", open ? "true" : "false");
  });

  if (document.body.classList.contains("has-hero")) {
    const onScroll = function () {
      header.classList.toggle("is-stuck", window.scrollY > 24);
    };
    onScroll();
    window.addEventListener("scroll", onScroll, { passive: true });
  }

  const footer = document.getElementById("chrome-footer");
  footer.className = "site-footer";
  footer.innerHTML =
    '<div><h2>Kurumsal</h2><ul>' +
    '<li><a href="kurumsal.html#galeri">Fotoğraf Galerisi</a></li>' +
    '<li><a href="kurumsal.html">Park Lunasan</a></li>' +
    '<li><a href="kurumsal.html#tarihce">Tarihçe</a></li>' +
    '<li><a href="ik.html">Bizimle Çalışmak İster misiniz ?</a></li>' +
    "</ul></div>" +
    '<div><h2>Park</h2><ul>' +
    '<li><a href="kurumsal.html">Park Özellikleri</a></li>' +
    '<li><a href="kurumsal.html#galeri">Fotoğraflar</a></li>' +
    '<li><a href="takimlar.html">Takımlar</a></li>' +
    "</ul></div>" +
    '<div><h2>Etkinlikler</h2><ul>' +
    '<li><a href="etkinlik.html">Gelecek Etkinlikler</a></li>' +
    '<li><a href="etkinlik.html#kacan">Kaçan Etkinlikler</a></li>' +
    "</ul></div>" +
    '<div><h2>Lunasan Online</h2><ul>' +
    '<li><a href="defter.html">Ziyaretçi Defterleri</a></li>' +
    '<li><a href="kayip.html">Kayıp Eşyalar</a></li>' +
    '<li><a href="online.html">Kamera</a></li>' +
    "</ul></div>" +
    '<div><h2>Bize Ulaşım</h2><ul>' +
    '<li><a href="ik.html">İnsan Kaynakları</a></li>' +
    '<li><a href="iletisim.html">İletişim</a></li>' +
    '<li><a href="iletisim.html#harita">Harita</a></li>' +
    "</ul>" +
    "<h2>Haberim Olsun</h2>" +
    "<p>Yeniliklerden haberdar olmak için haber aboneliğine katılabilirsiniz.</p>" +
    '<form class="news-form" id="news-form">' +
    '<input name="name" required placeholder="Ad Soyad" aria-label="Ad Soyad">' +
    '<input name="email" type="email" required placeholder="E Posta Adresi" aria-label="E Posta Adresi">' +
    '<button class="primary" type="submit">Katıl</button>' +
    '<p class="form-note" role="status"></p>' +
    "</form></div>" +
    '<p class="legal">Lunasan Eğlence Turizm İşletmecilik Tic. ve San. A.Ş. · Kocaeli Fuarı Parkı Lunasan, İzmit / Kocaeli · (0262) 321 5274</p>';

  footer.querySelector("#news-form").addEventListener("submit", function (event) {
    event.preventDefault();
    footer.querySelector(".form-note").textContent = "Kaydınız alındı.";
    event.currentTarget.reset();
  });

  document.querySelectorAll("form[data-local]").forEach(function (form) {
    form.addEventListener("submit", function (event) {
      event.preventDefault();
      const note = form.querySelector(".form-note");
      if (note) note.textContent = form.dataset.done || "Gönderildi.";
      form.reset();
    });
  });

  const dialog = document.createElement("dialog");
  dialog.innerHTML = '<button type="button">Kapat</button><img alt="">';
  document.body.appendChild(dialog);
  dialog.querySelector("button").addEventListener("click", function () {
    dialog.close();
  });
  document.addEventListener("click", function (event) {
    const link = event.target.closest("[data-full]");
    if (!link) return;
    event.preventDefault();
    const img = dialog.querySelector("img");
    img.src = link.getAttribute("href");
    img.alt = link.dataset.full || "";
    dialog.showModal();
  });
})();
