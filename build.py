#!/usr/bin/env python3
import json
import html
from pathlib import Path

ROOT = Path("/Users/furkanturkkan/parklunasan")
raw = (ROOT / "assets/data.js").read_text()
data = json.loads(raw[raw.index("{") : raw.rindex("}") + 1])
RIDES = data["rides"]
NOTES = data["notes"]
GALLERY = data["gallery"]
ARTICLE = data["article"]

FONTS = "https://fonts.googleapis.com/css2?family=Figtree:wght@400;500;600&family=Syne:wght@500;700&display=swap"
HERO = "https://www.parklunasan.com.tr/data/2011/06/01-7.jpg"
PARK = "https://www.parklunasan.com.tr/themes/default/file/slides/4.jpg"


def e(value):
    return html.escape(str(value), quote=True)


def rel(depth):
    return "../" * depth


def head(title, depth, description):
    r = rel(depth)
    return f"""<!DOCTYPE html>
<html lang="tr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(title)}</title>
<meta name="description" content="{e(description)}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="{FONTS}" rel="stylesheet">
<link rel="icon" href="{r}assets/brand/mark.png">
<link rel="stylesheet" href="{r}css/site.css">
</head>
<body>
"""


def chrome(depth, solid=True):
    r = rel(depth)
    kind = "site-header solid" if solid else "site-header"
    return f"""<header class="{kind}">
  <a class="brand" href="{r or './'}"><img class="brand-logo" src="{r}assets/brand/mark.png" alt="Park Lunasan"></a>
  <button class="nav-toggle" aria-label="Menü" aria-expanded="false"><span></span></button>
  <nav class="nav">
    <div class="drop">
      <a href="{r}takimlar/">Takımlar</a>
      <div class="drop-panel">
        <a href="{r}takimlar/yetiskin/">Yetişkin Takımları</a>
        <a href="{r}takimlar/cocuk/">Çocuk Takımları</a>
        <a href="{r}takimlar/">Tüm takımlar</a>
      </div>
    </div>
    <div class="drop">
      <a href="{r}kurumsal/">Park</a>
      <div class="drop-panel">
        <a href="{r}kurumsal/">Park Lunasan</a>
        <a href="{r}haber/">Haberler</a>
        <a href="{r}defter/">Ziyaretçi Defteri</a>
        <a href="{r}etkinlik/">Etkinlikler</a>
        <a href="{r}kayip/">Kayıp Eşyalar</a>
        <a href="{r}online/">Kamera</a>
      </div>
    </div>
    <a href="{r}insan-kaynaklari/">İK</a>
    <a href="https://www.parklunasan.com.tr/yedek-parca.pdf" target="_blank" rel="noreferrer">Yedek Parça</a>
    <a href="{r}iletisim/">İletişim</a>
    <a href="tel:+905323445274">0532 344 5274</a>
  </nav>
</header>
"""


def footer(depth):
    r = rel(depth)
    return f"""<footer class="site-footer">
  <div class="foot-grid">
    <div>
      <img class="foot-logo" src="{r}assets/brand/logo.png" alt="Park Lunasan">
      <p>Lunasan Eğlence Turizm İşletmecilik Tic. ve San. A.Ş.<br>Kocaeli Fuarı Parkı Lunasan, İzmit / Kocaeli</p>
      <p><a href="tel:+902623215274">(0262) 321 5274</a><br><a href="tel:+905323445274">(0532) 344 5274</a></p>
    </div>
    <div>
      <h2>Park</h2>
      <ul>
        <li><a href="{r}kurumsal/">Park Lunasan</a></li>
        <li><a href="{r}kurumsal/#galeri">Fotoğraf Galerisi</a></li>
        <li><a href="{r}haber/">Haberler</a></li>
        <li><a href="{r}defter/">Ziyaretçi Defteri</a></li>
        <li><a href="{r}insan-kaynaklari/">İnsan Kaynakları</a></li>
      </ul>
    </div>
    <div>
      <h2>Takımlar</h2>
      <ul>
        <li><a href="{r}takimlar/yetiskin/">Yetişkin Takımları</a></li>
        <li><a href="{r}takimlar/cocuk/">Çocuk Takımları</a></li>
        <li><a href="{r}etkinlik/">Etkinlikler</a></li>
        <li><a href="{r}kayip/">Kayıp Eşyalar</a></li>
        <li><a href="{r}online/">Kamera</a></li>
        <li><a href="{r}iletisim/">İletişim</a></li>
      </ul>
    </div>
  </div>
  <div class="legal"><span>Park Lunasan</span><span>İzmit, Kocaeli</span></div>
</footer>
<script src="{r}js/site.js"></script>
</body>
</html>
"""


def page_hero(image, kicker, title, alt=""):
    return f"""<section class="intro">
  <img src="{e(image)}" alt="{e(alt or title)}">
  <div class="intro-copy"><p class="kicker">{e(kicker)}</p><h1>{e(title)}</h1></div>
</section>
"""


def write(path, html_text):
    dest = ROOT / path
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(html_text)
    print(path)


def mosaic(rides, depth):
    r = rel(depth)
    cards = []
    for ride in rides:
        img = ride["images"][0] if ride["images"] else HERO
        cards.append(
            f'<a class="tile" href="{r}takimlar/{ride["slug"]}/"><img src="{e(img)}" alt=""><strong>{e(ride["name"])}</strong></a>'
        )
    return '<div class="mosaic">' + "".join(cards) + "</div>"


def cat_rows(depth):
    r = rel(depth)
    adult = next(x for x in RIDES if x["slug"] == "korfez-gunesi-15")
    kid = next(x for x in RIDES if x["slug"] == "atli-karinca-9")
    return f"""<div class="lanes">
  <a class="lane" href="{r}takimlar/yetiskin/">
    <span class="lane-photo"><img src="{e(adult["images"][0])}" alt=""></span>
    <div><p class="kicker">Park</p><h2>Yetişkin Takımları</h2><p>11 takım</p></div>
  </a>
  <a class="lane lane-flip" href="{r}takimlar/cocuk/">
    <span class="lane-photo"><img src="{e(kid["images"][0])}" alt=""></span>
    <div><p class="kicker">Park</p><h2>Çocuk Takımları</h2><p>18 takım</p></div>
  </a>
</div>
"""


desc = "1974'ten beri Kocaeli Fuarı'nda Türkiye'nin en büyük açık hava eğlence parkı."

home = head("Park Lunasan", 0, desc)
home += chrome(0, solid=False)
home += f"""
<section class="stage">
  <img class="stage-photo" src="{HERO}" alt="Körfez Güneşi, Park Lunasan">
  <div class="stage-caption">
    <div>
      <p class="kicker">Kocaeli Fuarı · İzmit</p>
      <h1>Park Lunasan</h1>
    </div>
    <p>Türkiye'nin en büyük açık hava eğlence parkı. Parkımızda bulunan birbirinden eğlenceli oyun takımları.</p>
    <div class="actions">
      <a class="btn" href="takimlar/">Takımları gör</a>
      <a class="link-quiet" href="tel:+905323445274">0532 344 5274</a>
    </div>
  </div>
</section>
<section class="band">
  <div class="split">
    <figure class="frame"><img src="{PARK}" alt="Park Lunasan"></figure>
    <div class="copy">
      <p class="kicker">Kuruluş</p>
      <h2>1974, Zaman Lunapark</h2>
      <p>Lunapark işletmeciliği dalında faaliyet göstermek üzere 1974 yılında Kocaeli Fuarı içerisinde 14.000 m² açık alan üzerine “Zaman Lunapark” adıyla da bilinen Mustafa Pehlivan tarafından kurulmuştur.</p>
      <p>2000 yılında Lunasan Lunapark Eğlence Turizim İşletmecilik Ticaret ve Sanayi A.Ş. olarak ünvan değişikliği yapmış ve kurulu bulunduğu alana 7.000 m² ilave ederek toplamda 21.000 m² de hizmet veren Türkiye'nin en büyük açık hava eğlence parkı haline gelmiştir.</p>
      <p><a class="btn" href="kurumsal/">Parkı tanıyın</a></p>
    </div>
  </div>
</section>
<section class="band sea">
  <div class="split">
    <div class="copy">
      <p class="kicker">Misyon</p>
      <h2>Huzurlu ve güvenli bir hizmet</h2>
      <p>Eğlence parkımızı ziyaret eden her yaştaki insanımıza huzurlu ve güvenli bir hizmet vermektir.</p>
      <p>Öncelikle Kocaeli başta olmak üzere Marmara Bölgesi ve daha sonra tüm Türkiye'de bilinen, tercih edilen, güvenilir ve saygın bir eğlence parkı olmaktır.</p>
    </div>
    <figure class="frame"><img src="{e(next(x for x in RIDES if x['slug']=='crazy-dance-12')['images'][0])}" alt="Crazy Dance"></figure>
  </div>
</section>
<section class="band">
  <p class="kicker">Eğlence takımları</p>
  <h2>Takımlar</h2>
  <p class="muted">Parkımızda bulunan birbirinden eğlenceli oyun takımları</p>
  {cat_rows(0)}
</section>
"""
home += footer(0)
write("index.html", home)

tak = head("Eğlence Takımları — Park Lunasan", 1, "Parkımızda bulunan birbirinden eğlenceli oyun takımları")
tak += chrome(1)
tak += page_hero(HERO, "Park Lunasan", "Eğlence Takımları", "Körfez Güneşi")
tak += cat_rows(1)
tak += mosaic(RIDES, 1)
tak += footer(1)
write("takimlar/index.html", tak)

for group, slug, title, count in (
    ("adult", "yetiskin", "Yetişkin Takımları", 11),
    ("kid", "cocuk", "Çocuk Takımları", 18),
):
    group_rides = [r for r in RIDES if r["group"] == group]
    img = group_rides[0]["images"][0]
    body = head(f"{title} — Park Lunasan", 2, "Parkımızda bulunan birbirinden eğlenceli oyun takımları")
    body += chrome(2)
    body += page_hero(img, "Eğlence Takımları", title)
    body += f'<div class="band" style="padding-bottom:1.2rem"><p class="muted">{count} takım</p></div>'
    body += mosaic(group_rides, 2)
    body += footer(2)
    write(f"takimlar/{slug}/index.html", body)

for ride in RIDES:
    siblings = [r for r in RIDES if r["group"] == ride["group"] and r["slug"] != ride["slug"]]
    group_name = "Yetişkin Takımları" if ride["group"] == "adult" else "Çocuk Takımları"
    group_href = "yetiskin/" if ride["group"] == "adult" else "cocuk/"
    hero_img = ride["images"][0] if ride["images"] else HERO
    paras = []
    for paragraph in ride["paragraphs"]:
        cls = ' class="caution"' if "sakıncalıdır" in paragraph else ""
        paras.append(f"<p{cls}>{e(paragraph)}</p>")
    thumbs = []
    for i, src in enumerate(ride["images"]):
        current = "true" if i == 0 else "false"
        thumbs.append(
            f'<button type="button" data-src="{e(src)}" data-alt="{e(ride["name"])}" aria-current="{current}"><img src="{e(src)}" alt=""></button>'
        )
    sib = "".join(f'<a href="../{s["slug"]}/">{e(s["name"])}</a>' for s in siblings)
    body = head(f'{ride["name"]} — Park Lunasan', 2, ride["paragraphs"][0] if ride["paragraphs"] else ride["name"])
    body += chrome(2)
    body += page_hero(hero_img, group_name, ride["name"], ride["name"])
    gallery = ""
    if ride["images"]:
        gallery = f"""<div>
      <img class="gallery-main" data-main src="{e(ride["images"][0])}" alt="{e(ride["name"])}">
      <div class="thumbs">{''.join(thumbs)}</div>
    </div>"""
    body += f"""<section class="band">
  <div class="unit-layout" data-gallery>
    {gallery}
    <div class="copy">
      <div class="prose">{''.join(paras)}</div>
      <p style="margin-top:1.6rem"><a class="btn" href="../../iletisim/">İletişime geç</a></p>
      <div class="siblings"><span class="muted"><a href="../{group_href}">{e(group_name)}</a></span>{sib}</div>
    </div>
  </div>
</section>
"""
    body += footer(2)
    write(f'takimlar/{ride["slug"]}/index.html', body)

about = head("Park Lunasan", 1, desc)
about += chrome(1)
about += page_hero(PARK, "Kurumsal", "Parkımızı daha yakından tanıyın.", "Park Lunasan")
about += f"""<section class="band" id="tarihce">
  <div class="split">
    <div class="copy prose">
      <p>Lunapark işletmeciliği dalında faaliyet göstermek üzere 1974 yılında Kocaeli Fuarı içerisinde 14.000 m² açık alan üzerine “Zaman Lunapark” adıyla da bilinen Mustafa Pehlivan tarafından kurulmuştur.</p>
      <p>İlerleyen yıllarda gelişen teknoloji ile üretilen lunapark oyuncakları yurt dışından ithal edilerek tüm Kocaeli halkının eğleneceği saygın işletmelerden biri olmuştur. 2000 yılında ihtiyaçlara daha iyi cevap verebilmek amacıyla Lunasan Lunapark Eğlence Turizim İşletmecilik Ticaret ve Sanayi A.Ş. olarak ünvan değişikliği yapmış ve kurulu bulunduğu alana 7.000 m² ilave ederek toplamda 21.000 m² de hizmet veren Türkiye'nin en büyük açık hava eğlence parkı haline gelmiştir.</p>
      <p>Şirket yönetim kurulu başkanı Mustafa Pehlivan başta olmak üzere, çok deneyimli yönetim ve teknik kadrosu ile birlikte emin adımlarla daha iyisini yapabilmek için çalışmalarına devam etmektedir.</p>
    </div>
    <figure class="frame"><img src="https://www.parklunasan.com.tr/themes/default/file/kurumsal_bg.jpg" alt="Park Lunasan"></figure>
  </div>
  <div class="split" style="margin-top:3rem">
    <div><p class="kicker">Misyon</p><p>Eğlence parkımızı ziyaret eden her yaştaki insanımıza huzurlu ve güvenli bir hizmet vermektir.</p></div>
    <div><p class="kicker">Vizyon</p><p>Öncelikle Kocaeli başta olmak üzere Marmara Bölgesi ve daha sonra tüm Türkiye'de bilinen, tercih edilen, güvenilir ve saygın bir eğlence parkı olmaktır.</p></div>
  </div>
</section>
<section class="band" id="galeri" style="padding-top:0">
  <p class="kicker">Park</p>
  <h2>Fotoğraf Galerisi</h2>
</section>
<div class="mosaic">{''.join(f'<a class="tile" href="{e(src)}" target="_blank" rel="noreferrer"><img src="{e(src)}" alt="Park Lunasan"><strong>Park Lunasan</strong></a>' for src in GALLERY)}</div>
"""
about += footer(1)
write("kurumsal/index.html", about)

contact = head("İletişim — Park Lunasan", 1, "Bize iletmek istediğiniz bir mesajınız mı var.")
contact += chrome(1)
contact += page_hero(HERO, "İletişim", "Bize yazın", "Park Lunasan")
contact += """<section class="band">
  <div class="contact-grid">
    <div>
      <p class="kicker">İzmit</p>
      <p>Lunasan Eğlence Turizm İşletmecilik Tic. ve San. A.Ş.</p>
      <p style="margin-top:.6rem">Merkez<br>Kocaeli Fuarı Parkı Lunasan<br>İzmit / Kocaeli</p>
      <a class="big" href="tel:+902623215274">(0262) 321 5274</a>
      <a class="big" href="tel:+905323445274">(0532) 344 5274</a>
      <p style="margin-top:1rem">Aşağıdaki form ile her türlü düşünce, öneri ya da şikayetinizi tarafımıza iletebilirsiniz.</p>
      <iframe class="map" title="Park Lunasan" src="https://maps.google.com/maps?q=Park%20Lunasan%20Kocaeli%20Fuar%C4%B1%20%C4%B0zmit&output=embed"></iframe>
    </div>
    <form data-contact data-done="Mesajınız iletildi.">
      <input name="konu" required placeholder="Konu" aria-label="Konu">
      <input name="name" required placeholder="İsim" aria-label="İsim">
      <input name="phone" placeholder="Telefon" aria-label="Telefon">
      <input name="email" type="email" required placeholder="E.Posta" aria-label="E.Posta">
      <textarea name="message" required placeholder="Mesajınız" aria-label="Mesajınız"></textarea>
      <button class="btn" type="submit">Gönder</button>
      <p class="note"></p>
    </form>
  </div>
</section>
"""
contact += footer(1)
write("iletisim/index.html", contact)

jobs = head("İnsan Kaynakları — Park Lunasan", 1, "Parkımıza çalışmak üzere gösterdiğiniz ilgiden ötürü teşekkür ederiz.")
jobs += chrome(1)
jobs += page_hero(PARK, "İnsan Kaynakları", "İş Başvuru Formu")
jobs += """<section class="band">
  <p style="max-width:46rem">Parkımıza çalışmak üzere gösterdiğiniz ilgiden ötürü teşekkür ederiz. Aşağıdaki formu eksiksiz olarak doldurup iş başvurunuzu yapabileceğiniz gibi Kocaeli Fuarı Parklunasan adresinden de başvuru yapabilirsiniz.</p>
  <form class="form-wide" data-contact data-done="Başvurunuz alındı." style="margin-top:2rem">
    <h2>Kişisel Bilgiler</h2>
    <input name="isim" required placeholder="İsim" aria-label="İsim">
    <fieldset><legend>Cinsiyet</legend><div class="checks"><label><input type="radio" name="cinsiyet" value="Bay"> Bay</label><label><input type="radio" name="cinsiyet" value="Bayan"> Bayan</label></div></fieldset>
    <input name="dogum" type="date" aria-label="Doğum Tarihi">
    <input name="eposta" type="email" required placeholder="E.Posta" aria-label="E.Posta">
    <input name="telefon" type="tel" required placeholder="Telefon" aria-label="Telefon">
    <h2>Adres Bilgileri</h2>
    <textarea name="adres" placeholder="Adres" aria-label="Adres"></textarea>
    <input name="il" placeholder="İl" aria-label="İl">
    <input name="ilce" placeholder="İlçe" aria-label="İlçe">
    <input name="pk" placeholder="P.Kodu" aria-label="P.Kodu">
    <h2>Eğitim Bilgileri</h2>
    <input name="egitim" placeholder="Eğitim Durumu" aria-label="Eğitim Durumu">
    <input name="okul" placeholder="Okul" aria-label="Okul">
    <input name="bolum" placeholder="Bölüm" aria-label="Bölüm">
    <input name="mezuniyet" placeholder="Mezuniyet" aria-label="Mezuniyet">
    <h2>Kişisel Nitelikler</h2>
    <fieldset><legend>Ehliyet</legend><div class="checks"><label><input type="radio" name="ehliyet" value="Var"> Var</label><label><input type="radio" name="ehliyet" value="Yok"> Yok</label></div></fieldset>
    <fieldset><legend>Bilgisayar</legend><div class="checks"><label><input type="radio" name="bilgisayar" value="Kötü"> Kötü</label><label><input type="radio" name="bilgisayar" value="Az"> Az</label><label><input type="radio" name="bilgisayar" value="Orta"> Orta</label><label><input type="radio" name="bilgisayar" value="İyi"> İyi</label></div></fieldset>
    <fieldset><legend>Alışkanlıklarınız</legend><div class="checks"><label><input type="checkbox" name="sigara"> Sigara</label><label><input type="checkbox" name="alkol"> Alkol</label></div></fieldset>
    <fieldset><legend>Yabancı Dil</legend><div class="checks"><label><input type="checkbox" name="ingilizce"> İngilizce</label><label><input type="checkbox" name="almanca"> Almanca</label><label><input type="checkbox" name="fransizca"> Fransızca</label><label><input type="checkbox" name="diger"> Diğer</label></div></fieldset>
    <h2>Cv Yükle</h2>
    <p class="muted">Cv’leriniz 256 KB boyutunda .DOC veya .PDF olmalıdır.</p>
    <input name="cv" type="file" accept=".doc,.docx,.pdf" aria-label="Dosya">
    <button class="btn" type="submit">Gönder</button>
    <p class="note"></p>
  </form>
</section>
"""
jobs += footer(1)
write("insan-kaynaklari/index.html", jobs)

book = head("Ziyaretçi Defteri — Park Lunasan", 1, "Parkımıza gelmiş ziyaretçilerimizin izlenimlerini paylaştıkları ziyaretçi defterimiz.")
book += chrome(1)
book += page_hero(PARK, "Ziyaretçi Defteri", "Ne demişler")
items = []
for note in NOTES:
    items.append(f"<li><h3>{e(note['name'])}</h3><time>{e(note['time'])}</time><p>{e(note['text'])}</p></li>")
book += f"""<section class="band">
  <h2>Ziyaretçi Defterine Birşeyler Yazın !</h2>
  <p style="margin-top:.8rem;max-width:40rem">Ziyaretçi defterine yazdığınız mesajlar yönetici kontrolünden geçtikten sonra yayınlanacaktır.</p>
  <form class="form-wide" data-contact data-done="Mesajınız yönetici kontrolüne iletildi." style="margin-top:1.4rem">
    <input name="ad" required placeholder="Adınız" aria-label="Adınız">
    <input name="soyad" required placeholder="Soyadınız" aria-label="Soyadınız">
    <input name="eposta" type="email" required placeholder="E.Posta" aria-label="E.Posta">
    <textarea name="mesaj" required placeholder="Mesajınızı bu alana yazabilirsiniz." aria-label="Mesaj"></textarea>
    <button class="btn" type="submit">Gönder</button>
    <p class="note"></p>
  </form>
  <h2 style="margin-top:3rem">Ne Demişler</h2>
  <ul class="messages">{''.join(items)}</ul>
</section>
"""
book += footer(1)
write("defter/index.html", book)

paras = []
for link in ARTICLE["links"]:
    paras.append(f'<p><a href="{e(link["href"])}" target="_blank" rel="noreferrer">{e(link["label"])}</a></p>')
for paragraph in ARTICLE["paragraphs"]:
    if len(paragraph) < 40:
        paras.append(f"<h2>{e(paragraph)}</h2>")
    else:
        paras.append(f"<p>{e(paragraph)}</p>")
news = head("Haberler — Park Lunasan", 1, ARTICLE["intro"])
news += chrome(1)
news += page_hero("https://www.parklunasan.com.tr/data/2012/12/sam0391-thumb.jpg", ARTICLE["kicker"], ARTICLE["title"])
news += f"""<section class="band"><div class="prose" style="max-width:46rem"><p class="muted">{e(ARTICLE["intro"])}</p>{''.join(paras)}</div></section>"""
news += footer(1)
write("haber/index.html", news)

events = head("Etkinlikler — Park Lunasan", 1, "Kocaeli Fuarı'nda düzenlenen etkinlikleri bu sayfalardan takip edebilirsiniz.")
events += chrome(1)
events += page_hero(PARK, "Etkinlikler", "Kocaeli Fuarı")
events += """<section class="band">
  <p>Kocaeli Fuarı'nda düzenlenen etkinlikleri bu sayfalardan takip edebilirsiniz.</p>
  <div class="siblings" style="margin-top:1.4rem"><a href="#hafta">Bu Hafta</a><a href="#ay">Bu Ay</a><a href="#kacan">Kaçan Etkinlikler</a></div>
  <p class="empty" id="hafta" style="margin-top:2rem">Bu listede etkinlik yok.</p>
  <p id="ay"></p><p id="kacan"></p>
</section>
"""
events += footer(1)
write("etkinlik/index.html", events)

lost = head("Kayıp Eşyalar — Park Lunasan", 1, "Siz değerli ziyaretçilerimizin zaman zaman parkımızda unuttukları eşyalar tarafımızca korunmaktadır.")
lost += chrome(1)
lost += page_hero(PARK, "Park Lunasan", "Kayıp Eşyalar")
lost += """<section class="band"><div class="prose" style="max-width:40rem">
  <p>Siz değerli ziyaretçilerimizin zaman zaman parkımızda unuttukları eşyalar tarafımızca korunmaktadır.</p>
  <p>Kayıp eşyalarınız hakkında iletişim sayfamız üzerinden irtibat kurabilirsiniz.</p>
  <p style="margin-top:1.4rem"><a class="btn" href="../iletisim/">İletişim</a></p>
</div></section>
"""
lost += footer(1)
write("kayip/index.html", lost)

cams = head("Canlı Kameralar — Park Lunasan", 1, "Parkımızı internet üzerinden canlı olarak izleyin.")
cams += chrome(1)
cams += page_hero(HERO, "Canlı Kameralar", "Parkı izleyin")
cams += """<section class="band"><ul class="refs">
  <li>Dogu Kapı Park Kamerası</li>
  <li>Dogu Kapı Park Kamerası</li>
  <li>Dogu Kapı Park Kamerası</li>
  <li>Dogu Kapı Park Kamerası</li>
</ul></section>
"""
cams += footer(1)
write("online/index.html", cams)
print("done", len(RIDES))
