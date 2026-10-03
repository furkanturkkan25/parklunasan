# Park Lunasan

Kocaeli Fuarı’ndaki Park Lunasan’ın sitesi. Takımlar, park bilgisi, insan kaynakları, kayıp eşya ve iletişim ayrı sayfalarda.

The site for Park Lunasan at the Kocaeli Fair. Rides, park info, careers, lost and found, and contact each have their own page.

![Ana sayfa / Home](ekran/ana.png)

![Takımlar / Rides](ekran/takimlar.png)

![Körfez Güneşi](ekran/korfez-gunesi.png)

![Kayıp eşyalar / Lost and found](ekran/kayip.png)

## Kurulum / Setup

```bash
cd parklunasan
python3 -m http.server 8080
```

Aç / Open: http://127.0.0.1:8080

Takım sayfaları `takimlar/` altında. Yetişkin ve çocuk listeleri `takimlar/yetiskin/` ve `takimlar/cocuk/`.

Ride pages are under `takimlar/`. Adult and child lists are `takimlar/yetiskin/` and `takimlar/cocuk/`.

## Teknoloji / Stack

Çok sayfalı **statik HTML**. Ortak menü ve stiller `assets/styles.css`, `css/site.css` ve `assets/site.js`. Takım kayıtları `assets/rides.js` ve `assets/data.js` içinde. Her oyuncağın kendi `index.html` dosyası var.

Multi-page **static HTML**. The shared menu and styles are `assets/styles.css`, `css/site.css`, and `assets/site.js`. Ride records are in `assets/rides.js` and `assets/data.js`. Each ride has its own `index.html`.
