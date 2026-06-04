#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generează paginile SEO (servicii + orașe), sitemap.xml și robots.txt
   pentru site-ul Valterm Invest (DDD Huși)."""

import os, html

BASE_URL = "https://alexandrumetzak.github.io/ddd-husi"
PHONE_DISPLAY = "0744 913 376"
PHONE_TEL = "+40744913376"
WA = "40744913376"
ROOT = os.path.dirname(os.path.abspath(__file__))

# ----------------------------------------------------------------------------
# DATE: SERVICII
# ----------------------------------------------------------------------------
SERVICES = [
    {
        "slug": "combatere-gandaci",
        "name": "Combatere gândaci",
        "icon": "🪳",
        "title": "Combatere gândaci în Huși și Moldova | Scapă definitiv de gândaci",
        "desc": "Servicii profesionale de combatere a gândacilor de bucătărie și gândacilor negri în Huși și toată Moldova. Tratament cu gel și pulverizare, garanție. Sună acum!",
        "h1": "Combatere gândaci — scapă definitiv de gândaci de bucătărie",
        "lead": "Ai gândaci în bucătărie, baie sau în spatele electrocasnicelor? Aplicăm tratamente profesionale cu gel și pulverizare care elimină gândacii din rădăcină, inclusiv ouăle.",
        "sections": [
            ("De ce apar gândacii și de ce revin", [
                "Gândacii de bucătărie (Blattella germanica) se înmulțesc extrem de rapid — o singură femelă poate genera sute de urmași. De aceea soluțiile din comerț (spray-uri, capcane) maschează problema, dar nu o rezolvă.",
                "Noi tratăm atât adulții, cât și ouăle și căile de acces, astfel încât infestarea să nu reapară.",
            ]),
            ("Cum decurge tratamentul nostru", [
                "Inspectăm spațiul și identificăm focarele și căile de acces.",
                "Aplicăm gel insecticid în zonele cheie (sub mobilier, lângă electrocasnice, în crăpături).",
                "Completăm, unde e nevoie, cu pulverizare reziduală pe suprafețe.",
                "Îți dăm recomandări de igienă și revenim pentru control dacă e cazul.",
            ]),
            ("Pentru ce spații", [
                "Apartamente și case", "Restaurante, baruri și bucătării profesionale",
                "Magazine alimentare și depozite", "Blocuri și asociații de proprietari",
            ]),
        ],
        "faq": [
            ("Cât de repede dispar gândacii?", "De obicei observi o scădere semnificativă în primele 3–7 zile, iar eliminarea completă în 2–3 săptămâni, pe măsură ce sunt afectate și ouăle."),
            ("Substanțele sunt periculoase?", "Folosim doar produse avizate de Ministerul Sănătății, aplicate țintit. Îți spunem exact ce măsuri să iei pentru siguranța copiilor și a animalelor."),
            ("Trebuie să golesc bucătăria?", "Nu complet. Îți dăm instrucțiuni simple de pregătire înainte de intervenție."),
        ],
    },
    {
        "slug": "combatere-plosnite",
        "name": "Combatere ploșnițe",
        "icon": "🛏️",
        "title": "Combatere ploșnițe de pat în Huși și Moldova | Tratament garantat",
        "desc": "Eliminăm ploșnițele de pat prin tratamente profesionale reziduale și termice. Inspecție, intervenție și revenire de control în Huși și toată Moldova.",
        "h1": "Combatere ploșnițe de pat — tratament profesional cu garanție",
        "lead": "Te trezești cu înțepături pe piele și pete mici pe așternuturi? Sunt semne clasice de ploșnițe. Intervenim discret și eficient, cu tratamente care le elimină complet.",
        "sections": [
            ("De ce ploșnițele sunt greu de eliminat singur", [
                "Ploșnițele se ascund în cusături de saltea, tăblii de pat, prize, plinte și mobilier. Sunt active noaptea și rezistă la multe soluții din comerț.",
                "Un tratament profesional ajunge în toate ascunzișurile și tratează și stadiul de ou, ceea ce previne reinfestarea.",
            ]),
            ("Metodele noastre", [
                "Inspecție detaliată pentru localizarea focarelor.",
                "Tratament rezidual în toate ascunzișurile și pe trasee.",
                "Tratament termic (la cerere) pentru infestări puternice.",
                "Revenire de control pentru rezultat garantat.",
            ]),
            ("Unde intervenim", [
                "Locuințe și apartamente", "Hoteluri, pensiuni și cazări",
                "Cămine și internate", "Spații închiriate",
            ]),
        ],
        "faq": [
            ("Trebuie să arunc salteaua sau mobila?", "În cele mai multe cazuri, nu. Tratamentul profesional salvează mobilierul. Îți spunem clar dacă ceva chiar nu mai poate fi recuperat."),
            ("Cât durează până scap de ploșnițe?", "În funcție de gradul infestării, de obicei sunt necesare 1–2 intervenții. Revenim pentru control."),
            ("Pot rămâne în locuință?", "Da, după respectarea perioadei de aerisire indicate. Îți dăm toate instrucțiunile."),
        ],
    },
    {
        "slug": "combatere-soareci-sobolani",
        "name": "Deratizare (șoareci & șobolani)",
        "icon": "🐀",
        "title": "Deratizare Huși și Moldova | Combatere șoareci și șobolani",
        "desc": "Servicii de deratizare pentru eliminarea șoarecilor și șobolanilor. Stații de intoxicare securizate, momeli profesionale, contracte pentru firme. Huși și toată Moldova.",
        "h1": "Deratizare — combatere șoareci și șobolani eficient și sigur",
        "lead": "Auzi zgârieturi în pereți, găsești excremente sau ambalaje roase? Rozătoarele transmit boli și produc pagube. Le eliminăm cu stații securizate și momeli profesionale.",
        "sections": [
            ("De ce e importantă deratizarea profesională", [
                "Șoarecii și șobolanii se reproduc rapid și roade cabluri, instalații și alimente, provocând pagube și riscuri de incendiu sau contaminare.",
                "Folosim stații de intoxicare securizate (sigure pentru copii și animale) amplasate strategic, plus un plan de monitorizare.",
            ]),
            ("Cum lucrăm", [
                "Evaluăm gradul de infestare și traseele rozătoarelor.",
                "Amplasăm stații de intoxicare securizate în punctele cheie.",
                "Monitorizăm și completăm momeala periodic.",
                "Pentru firme: hărți de amplasare și documentație HACCP/DSV.",
            ]),
            ("Pentru cine", [
                "Locuințe, curți și anexe", "Depozite și spații de producție",
                "Magazine și restaurante", "Instituții și spații comerciale",
            ]),
        ],
        "faq": [
            ("Stațiile sunt periculoase pentru copii sau câini?", "Nu. Sunt stații închise, securizate, în care momeala nu poate fi accesată decât de rozătoare."),
            ("Oferiți contracte pentru firme?", "Da, abonamente cu intervenții periodice și toată documentația necesară pentru controale (HACCP, DSV)."),
            ("Cât de des e nevoie de intervenții?", "Pentru locuințe, de obicei o intervenție cu o revenire. Pentru firme recomandăm monitorizare periodică."),
        ],
    },
    {
        "slug": "combatere-tantari-capuse",
        "name": "Combatere țânțari & căpușe",
        "icon": "🦟",
        "title": "Combatere țânțari și căpușe Huși și Moldova | Tratament curți și grădini",
        "desc": "Tratamente împotriva țânțarilor și căpușelor pentru curți, grădini, terase și spații verzi. Protejează familia și clienții de înțepături. Huși și toată Moldova.",
        "h1": "Combatere țânțari și căpușe — bucură-te de curte fără înțepături",
        "lead": "Țânțarii și căpușele transformă curtea într-un loc de nestat și transmit boli. Aplicăm tratamente pentru spații verzi care reduc drastic populația de insecte.",
        "sections": [
            ("Când e nevoie de tratament", [
                "Primăvara și vara, în zonele cu vegetație, umezeală sau ape stătătoare, țânțarii și căpușele se înmulțesc rapid.",
                "Un tratament aplicat la timp protejează familia, copiii și animalele de companie pe tot sezonul cald.",
            ]),
            ("Ce includem", [
                "Pulverizare pe vegetație, garduri vii și zone umbrite.",
                "Tratament pentru terase, curți și spații de joacă.",
                "Soluții pentru evenimente în aer liber (nunți, petreceri).",
                "Recomandări pentru reducerea surselor de înmulțire.",
            ]),
            ("Locuri tratate", [
                "Curți și grădini private", "Terase de restaurant și evenimente",
                "Parcuri, spații verzi și incinte", "Pensiuni și zone de cazare",
            ]),
        ],
        "faq": [
            ("Cât ține efectul?", "În general câteva săptămâni, în funcție de vreme și de vegetație. Pentru sezonul cald recomandăm tratamente repetate."),
            ("Pot folosi curtea după tratament?", "Da, după perioada de uscare indicată (de regulă câteva ore)."),
            ("Tratați și împotriva căpușelor?", "Da, aceeași intervenție vizează și căpușele din iarbă și vegetație."),
        ],
    },
    {
        "slug": "dezinfectie-spatii",
        "name": "Dezinfecție spații",
        "icon": "🧴",
        "title": "Dezinfecție spații Huși și Moldova | Nebulizare ULV profesională",
        "desc": "Servicii de dezinfecție prin nebulizare ULV pentru spații comerciale, medicale și locuințe. Eliminăm bacterii, virusuri și mucegai cu substanțe avizate.",
        "h1": "Dezinfecție profesională a spațiilor prin nebulizare ULV",
        "lead": "Dezinfecția corectă elimină bacteriile, virusurile și mucegaiul de pe suprafețe și din aer. Folosim nebulizare ULV care acoperă uniform tot spațiul, inclusiv zonele greu accesibile.",
        "sections": [
            ("Când e recomandată dezinfecția", [
                "După cazuri de boală, în spații aglomerate, în unități medicale sau alimentare, după inundații ori în spații cu mucegai și mirosuri persistente.",
                "Nebulizarea ULV creează o ceață fină care acoperă pereți, mobilier și aer, fără să ude suprafețele.",
            ]),
            ("Ce oferim", [
                "Dezinfecție spații comerciale, birouri și cabinete.",
                "Tratament anti-mucegai și eliminarea mirosurilor.",
                "Igienizare după evenimente sau renovări.",
                "Documentație pentru firme și instituții.",
            ]),
            ("Spații deservite", [
                "Cabinete medicale și clinici", "Restaurante, magazine și birouri",
                "Școli, grădinițe și instituții", "Locuințe și spații închiriate",
            ]),
        ],
        "faq": [
            ("Substanțele lasă urme sau miros?", "Folosim produse avizate care nu lasă reziduuri vizibile. Eventualul miros ușor dispare după aerisire."),
            ("Cât durează?", "În funcție de suprafață, de regulă între 30 de minute și câteva ore."),
            ("Când pot reintra în spațiu?", "După perioada de aerisire indicată, de obicei 1–2 ore."),
        ],
    },
]

# ----------------------------------------------------------------------------
# DATE: ORAȘE / ZONE
# ----------------------------------------------------------------------------
CITIES = [
    {"slug": "husi", "name": "Huși", "judet": "Vaslui",
     "ctx": "Huși este orașul nostru de bază, așa că ajungem rapid la orice adresă, de la cartiere rezidențiale la spații comerciale și instituții."},
    {"slug": "vaslui", "name": "Vaslui", "judet": "Vaslui",
     "ctx": "Deservim întreg județul Vaslui, inclusiv municipiul Vaslui, pentru locuințe, firme și instituții publice."},
    {"slug": "barlad", "name": "Bârlad", "judet": "Vaslui",
     "ctx": "Intervenim în Bârlad și împrejurimi, pentru apartamente, case, restaurante și unități comerciale."},
    {"slug": "iasi", "name": "Iași", "judet": "Iași",
     "ctx": "Acoperim municipiul Iași și zona metropolitană, cu soluții DDD pentru locuințe, HoReCa, birouri și depozite."},
    {"slug": "bacau", "name": "Bacău", "judet": "Bacău",
     "ctx": "Ne deplasăm în Bacău și localitățile din jur pentru intervenții de dezinsecție, deratizare și dezinfecție."},
    {"slug": "roman", "name": "Roman", "judet": "Neamț",
     "ctx": "Oferim servicii DDD în Roman pentru clienți rezidențiali și pentru firme cu spații de producție sau depozitare."},
    {"slug": "galati", "name": "Galați", "judet": "Galați",
     "ctx": "Intervenim în Galați pentru locuințe, blocuri, restaurante și spații comerciale, cu programări flexibile."},
    {"slug": "focsani", "name": "Focșani", "judet": "Vrancea",
     "ctx": "Deservim Focșani și județul Vrancea, cu soluții complete pentru persoane fizice și juridice."},
    {"slug": "piatra-neamt", "name": "Piatra Neamț", "judet": "Neamț",
     "ctx": "Ajungem în Piatra Neamț și împrejurimi pentru tratamente profesionale împotriva dăunătorilor."},
    {"slug": "botosani", "name": "Botoșani", "judet": "Botoșani",
     "ctx": "Oferim servicii DDD în Botoșani pentru locuințe, instituții și unități comerciale."},
    {"slug": "suceava", "name": "Suceava", "judet": "Suceava",
     "ctx": "Ne deplasăm în Suceava și zona Bucovinei pentru intervenții de dezinsecție, deratizare și dezinfecție."},
]

# ----------------------------------------------------------------------------
# TEMPLATE
# ----------------------------------------------------------------------------
def head(title, desc, canonical, schema):
    return f"""<!DOCTYPE html>
<html lang="ro">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{html.escape(title)}</title>
  <meta name="description" content="{html.escape(desc)}" />
  <meta name="robots" content="index, follow" />
  <link rel="canonical" href="{canonical}" />
  <meta property="og:type" content="website" />
  <meta property="og:title" content="{html.escape(title)}" />
  <meta property="og:description" content="{html.escape(desc)}" />
  <meta property="og:locale" content="ro_RO" />
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@500;600;700;800&family=Inter:wght@400;500;600&display=swap" rel="stylesheet" />
  <link rel="stylesheet" href="../assets/styles.css" />
  <link rel="icon" type="image/svg+xml" href="../assets/logo.svg" />
  <script type="application/ld+json">
{schema}
  </script>
</head>
<body>"""

def header_html():
    return f"""
  <header class="site-header" id="top">
    <div class="container nav-inner">
      <a href="../index.html" class="brand">
        <img src="../assets/logo.svg" alt="Valterm Invest" class="brand-mark" />
        <span class="brand-text">
          <strong>Valterm Invest</strong>
          <small>Dezinsecție · Deratizare · Dezinfecție</small>
        </span>
      </a>
      <nav class="nav-links" id="navLinks">
        <a href="../index.html#servicii">Servicii</a>
        <a href="../index.html#business">Firme</a>
        <a href="../index.html#zona">Zona</a>
        <a href="../index.html#contact" class="nav-cta">Cere ofertă</a>
      </nav>
      <button class="nav-toggle" id="navToggle" aria-label="Meniu"><span></span><span></span><span></span></button>
    </div>
  </header>"""

def footer_html():
    return f"""
  <footer class="site-footer">
    <div class="container footer-inner">
      <div class="footer-brand">
        <img src="../assets/logo.svg" alt="Valterm Invest" class="brand-mark" />
        <strong>Valterm Invest SRL</strong>
        <p>Dezinsecție · Deratizare · Dezinfecție în Huși și toată Moldova. Personal autorizat, substanțe avizate, garanție.</p>
      </div>
      <div class="footer-col">
        <h4>Servicii</h4>
        <a href="../index.html#servicii">Dezinsecție</a>
        <a href="../index.html#servicii">Deratizare</a>
        <a href="../index.html#servicii">Dezinfecție</a>
      </div>
      <div class="footer-col">
        <h4>Companie</h4>
        <a href="../index.html#de-ce-noi">De ce noi</a>
        <a href="../index.html#proces">Cum lucrăm</a>
        <a href="../index.html#contact">Contact</a>
      </div>
      <div class="footer-col">
        <h4>Contact</h4>
        <a href="tel:{PHONE_TEL}">{PHONE_DISPLAY}</a>
        <a href="https://wa.me/{WA}" target="_blank" rel="noopener">WhatsApp</a>
        <span>Huși, jud. Vaslui</span>
      </div>
    </div>
    <div class="footer-bottom"><div class="container">
      <span>© 2026 S.C. Valterm Invest S.R.L · CUI RO16277092 · J37/195/2004 · Toate drepturile rezervate.</span>
    </div></div>
  </footer>
  <div class="float-actions">
    <a href="https://wa.me/{WA}" class="float-btn whatsapp" target="_blank" rel="noopener" aria-label="WhatsApp">💬</a>
    <a href="tel:{PHONE_TEL}" class="float-btn call" aria-label="Sună">📞</a>
  </div>
  <script src="../assets/script.js"></script>
</body>
</html>"""

def aside_html(title_ctx):
    return f"""
        <aside class="lp-aside">
          <div class="aside-card accent">
            <h3>Cere o ofertă gratuită</h3>
            <p>{title_ctx} Te sunăm înapoi sau îți răspundem rapid pe WhatsApp.</p>
            <a href="tel:{PHONE_TEL}" class="btn btn-primary">📞 {PHONE_DISPLAY}</a>
            <a href="https://wa.me/{WA}" class="btn btn-ghost" target="_blank" rel="noopener">💬 Scrie pe WhatsApp</a>
          </div>
          <div class="aside-card">
            <h3>De ce Valterm Invest?</h3>
            <ul class="prose" style="margin:0;padding:0;">
              <li>Personal autorizat</li>
              <li>Substanțe avizate</li>
              <li>Garanție pentru lucrări</li>
              <li>Intervenție rapidă, inclusiv weekend</li>
            </ul>
          </div>
        </aside>"""

def faq_html(faqs):
    items = "\n".join(
        f'        <details><summary>{html.escape(q)}</summary><p>{html.escape(a)}</p></details>'
        for q, a in faqs)
    return f"""
      <h2>Întrebări frecvente</h2>
      <div class="faq">
{items}
      </div>"""

def faq_schema(faqs):
    q = ",".join(
        '{"@type":"Question","name":"%s","acceptedAnswer":{"@type":"Answer","text":"%s"}}'
        % (q.replace('"', "'"), a.replace('"', "'")) for q, a in faqs)
    return '{"@context":"https://schema.org","@type":"FAQPage","mainEntity":[%s]}' % q

def service_schema(s, canonical):
    return ('{"@context":"https://schema.org","@type":"Service",'
            '"serviceType":"%s","provider":{"@type":"PestControlService","name":"Valterm Invest SRL",'
            '"telephone":"%s","areaServed":"Moldova, România",'
            '"address":{"@type":"PostalAddress","addressLocality":"Huși","addressRegion":"Vaslui","addressCountry":"RO"}},'
            '"areaServed":"Moldova, România","url":"%s"}'
            % (s["name"].replace('"', "'"), PHONE_TEL, canonical))

def prose_sections(sections):
    out = []
    for title, items in sections:
        out.append(f"      <h2>{html.escape(title)}</h2>")
        # Heuristic: dacă elementele sunt fraze lungi -> paragrafe; scurte -> listă
        if all(len(i) < 60 for i in items):
            out.append("      <ul>")
            out += [f"        <li>{html.escape(i)}</li>" for i in items]
            out.append("      </ul>")
        else:
            out += [f"      <p>{html.escape(i)}</p>" for i in items]
    return "\n".join(out)

def related_html(current_slug, kind):
    links = []
    for s in SERVICES:
        if kind == "service" and s["slug"] == current_slug:
            continue
        links.append((f'../servicii/{s["slug"]}.html', f'{s["icon"]} {s["name"]}'))
    for c in CITIES[:8]:
        if kind == "city" and c["slug"] == current_slug:
            continue
        links.append((f'../zone/{c["slug"]}.html', f'📍 DDD {c["name"]}'))
    cells = "\n".join(f'        <a href="{u}">{html.escape(t)}</a>' for u, t in links)
    return f"""
  <section class="related">
    <div class="container">
      <h2>Alte servicii și zone</h2>
      <div class="related-grid">
{cells}
      </div>
    </div>
  </section>"""

# ----------------------------------------------------------------------------
# GENERARE
# ----------------------------------------------------------------------------
def build_service(s):
    canonical = f"{BASE_URL}/servicii/{s['slug']}.html"
    schema = service_schema(s, canonical) + "\n  </script>\n  <script type=\"application/ld+json\">\n" + faq_schema(s["faq"])
    page = head(s["title"], s["desc"], canonical, schema)
    page += header_html()
    page += f"""
  <section class="lp-hero">
    <div class="container">
      <div class="breadcrumb"><a href="../index.html">Acasă</a><span>›</span> Servicii <span>›</span> {html.escape(s['name'])}</div>
      <h1>{html.escape(s['h1'])}</h1>
      <p class="lp-lead">{html.escape(s['lead'])}</p>
      <div class="lp-actions">
        <a href="tel:{PHONE_TEL}" class="btn btn-primary">📞 Sună acum</a>
        <a href="https://wa.me/{WA}" class="btn btn-ghost" target="_blank" rel="noopener">💬 WhatsApp</a>
      </div>
    </div>
  </section>
  <section class="lp-body">
    <div class="container lp-grid">
      <div class="prose">
{prose_sections(s['sections'])}
{faq_html(s['faq'])}
      </div>
{aside_html('Spune-ne pe scurt ce problemă ai.')}
    </div>
  </section>"""
    page += related_html(s["slug"], "service")
    page += footer_html()
    path = os.path.join(ROOT, "servicii", f"{s['slug']}.html")
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(page)
    return canonical

def build_city(c):
    canonical = f"{BASE_URL}/zone/{c['slug']}.html"
    title = f"DDD {c['name']} | Dezinsecție, Deratizare, Dezinfecție în {c['name']}"
    desc = (f"Servicii DDD în {c['name']} ({c['judet']}): dezinsecție, deratizare și dezinfecție "
            f"pentru locuințe și firme. Personal autorizat, substanțe avizate, intervenție rapidă. Sună la {PHONE_DISPLAY}.")
    faqs = [
        (f"Ajungeți în {c['name']}?", f"Da. {c['ctx']} Sună-ne pentru a stabili o programare."),
        ("Ce servicii oferiți?", "Dezinsecție (gândaci, ploșnițe, țânțari), deratizare (șoareci, șobolani) și dezinfecție profesională."),
        ("Lucrați și cu firme?", "Da, avem contracte și documentație completă pentru HACCP și DSV, pentru restaurante, magazine, depozite și instituții."),
    ]
    schema = ('{"@context":"https://schema.org","@type":"PestControlService","name":"Valterm Invest SRL – DDD %s",'
              '"telephone":"%s","areaServed":"%s, România",'
              '"address":{"@type":"PostalAddress","addressLocality":"Huși","addressRegion":"Vaslui","addressCountry":"RO"},'
              '"url":"%s"}' % (c['name'], PHONE_TEL, c['name'], canonical))
    schema += "\n  </script>\n  <script type=\"application/ld+json\">\n" + faq_schema(faqs)
    page = head(title, desc, canonical, schema)
    page += header_html()
    page += f"""
  <section class="lp-hero">
    <div class="container">
      <div class="breadcrumb"><a href="../index.html">Acasă</a><span>›</span> Zone <span>›</span> {html.escape(c['name'])}</div>
      <h1>Servicii DDD în <span class="accent">{html.escape(c['name'])}</span> — Dezinsecție, Deratizare, Dezinfecție</h1>
      <p class="lp-lead">Ai nevoie de o firmă de dezinsecție, deratizare sau dezinfecție în {html.escape(c['name'])} ({html.escape(c['judet'])})? Valterm Invest intervine rapid, cu personal autorizat și substanțe avizate.</p>
      <div class="lp-actions">
        <a href="tel:{PHONE_TEL}" class="btn btn-primary">📞 Sună acum</a>
        <a href="https://wa.me/{WA}" class="btn btn-ghost" target="_blank" rel="noopener">💬 WhatsApp</a>
      </div>
    </div>
  </section>
  <section class="lp-body">
    <div class="container lp-grid">
      <div class="prose">
      <h2>Firmă de DDD pentru {html.escape(c['name'])} și împrejurimi</h2>
      <p>{html.escape(c['ctx'])}</p>
      <p>Oferim soluții complete atât pentru persoane fizice (apartamente, case, curți), cât și pentru firme și instituții din {html.escape(c['name'])}. Toate intervențiile se fac cu produse avizate de Ministerul Sănătății, sigure pentru copii și animale de companie.</p>
      <h2>Ce servicii oferim în {html.escape(c['name'])}</h2>
      <ul>
        <li>Dezinsecție — gândaci, ploșnițe, furnici, țânțari, căpușe, muște</li>
        <li>Deratizare — șoareci și șobolani, cu stații securizate</li>
        <li>Dezinfecție — nebulizare ULV pentru bacterii, virusuri și mucegai</li>
        <li>Contracte DDD pentru firme, cu documentație HACCP și DSV</li>
      </ul>
      <h2>De ce să alegi Valterm Invest în {html.escape(c['name'])}</h2>
      <ul>
        <li>Personal autorizat și echipament profesional</li>
        <li>Intervenție rapidă, inclusiv în weekend</li>
        <li>Discreție totală — fără uniforme vizibile</li>
        <li>Garanție pentru lucrările efectuate</li>
      </ul>
{faq_html(faqs)}
      </div>
{aside_html(f'Programări DDD în {html.escape(c["name"])} și împrejurimi.')}
    </div>
  </section>"""
    page += related_html(c["slug"], "city")
    page += footer_html()
    path = os.path.join(ROOT, "zone", f"{c['slug']}.html")
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(page)
    return canonical

def main():
    urls = [f"{BASE_URL}/", f"{BASE_URL}/index.html"]
    for s in SERVICES:
        urls.append(build_service(s))
    for c in CITIES:
        urls.append(build_city(c))

    # sitemap.xml
    entries = "\n".join(
        f"  <url><loc>{u}</loc><changefreq>monthly</changefreq><priority>{'1.0' if u.endswith('/') else '0.8'}</priority></url>"
        for u in urls)
    sitemap = f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
{entries}
</urlset>
"""
    with open(os.path.join(ROOT, "sitemap.xml"), "w", encoding="utf-8") as f:
        f.write(sitemap)

    # robots.txt
    robots = f"""User-agent: *
Allow: /

Sitemap: {BASE_URL}/sitemap.xml
"""
    with open(os.path.join(ROOT, "robots.txt"), "w", encoding="utf-8") as f:
        f.write(robots)

    print(f"Generate: {len(SERVICES)} servicii, {len(CITIES)} orașe, sitemap cu {len(urls)} URL-uri.")

if __name__ == "__main__":
    main()
