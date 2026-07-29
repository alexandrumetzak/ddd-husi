#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generează paginile SEO (servicii + orașe), sitemap.xml și robots.txt
   pentru site-ul Valterm Invest (DDD Huși)."""

import os, html, datetime

BASE_URL = "https://ddd-husi.ro"
OG_IMAGE = BASE_URL + "/assets/og-image.png"
TODAY = datetime.date.today().isoformat()
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
    {
        "slug": "combatere-furnici",
        "name": "Combatere furnici",
        "icon": "🐜",
        "title": "Combatere furnici în Huși și Moldova | Scapă de furnici în casă",
        "desc": "Servicii profesionale de combatere a furnicilor în locuințe, curți și firme. Tratament cu gel și pulverizare care elimină furnicarul. Huși și toată Moldova.",
        "h1": "Combatere furnici — elimină furnicarul, nu doar furnicile vizibile",
        "lead": "Furnicile apar în bucătărie, pe pervaze sau în curte și se înmulțesc rapid. Tratamentul nostru vizează colonia și regina, nu doar furnicile pe care le vezi.",
        "sections": [
            ("De ce nu ajută spray-urile obișnuite", [
                "Spray-urile din comerț omoară doar furnicile vizibile, în timp ce colonia și regina rămân ascunse și produc constant noi furnici.",
                "Folosim geluri și soluții pe care furnicile le duc în furnicar, eliminând colonia de la sursă.",
            ]),
            ("Cum lucrăm", [
                "Identificăm traseele și locul probabil al cuibului.",
                "Aplicăm gel insecticid pe traseele de acces.",
                "Tratăm prin pulverizare punctele de intrare în locuință.",
                "Recomandări pentru a preveni reapariția.",
            ]),
            ("Unde intervenim", [
                "Locuințe, bucătării și cămări", "Curți, terase și grădini",
                "Magazine și spații alimentare", "Depozite și firme",
            ]),
        ],
        "faq": [
            ("Scap definitiv de furnici?", "Da, prin eliminarea coloniei. Dacă apar din exterior (curte, vecini), recomandăm și un tratament preventiv periodic."),
            ("E sigur pentru copii și animale?", "Da, aplicăm produse avizate, țintit, în locuri inaccesibile copiilor și animalelor."),
            ("Tratați și furnicile de grădină?", "Da, tratăm atât furnicile din interior, cât și furnicarele din curte."),
        ],
    },
    {
        "slug": "combatere-muste",
        "name": "Combatere muște",
        "icon": "🪰",
        "title": "Combatere muște în Huși și Moldova | Soluții pentru firme și locuințe",
        "desc": "Tratamente împotriva muștelor pentru restaurante, ferme, depozite și locuințe. Pulverizare, capcane și soluții profesionale. Huși și toată Moldova.",
        "h1": "Combatere muște — control eficient pentru spații curate",
        "lead": "Muștele contaminează alimentele și transmit boli, fiind o problemă serioasă mai ales pentru restaurante, ferme și magazine alimentare. Oferim soluții profesionale de control.",
        "sections": [
            ("De ce e nevoie de control profesional", [
                "Muștele se înmulțesc exploziv în jurul gunoaielor, resturilor alimentare și zonelor cu animale. O infestare scapă rapid de sub control.",
                "Combinăm tratamentul cu pulverizare reziduală, capcane și recomandări de igienă pentru un efect de durată.",
            ]),
            ("Ce includem", [
                "Pulverizare reziduală pe suprafețele de odihnă ale muștelor.",
                "Montare de capcane și dispozitive (la cerere).",
                "Tratament pentru zone exterioare și de depozitare a deșeurilor.",
                "Plan de control pentru firme și ferme.",
            ]),
            ("Pentru cine", [
                "Restaurante și bucătării profesionale", "Ferme și gospodării cu animale",
                "Magazine și depozite alimentare", "Locuințe și curți",
            ]),
        ],
        "faq": [
            ("Cât de repede se văd rezultatele?", "Efectul este vizibil în câteva ore până la o zi după tratament."),
            ("Oferiți soluții pentru restaurante?", "Da, cu plan de control periodic și documentație pentru HACCP."),
            ("Tratamentul afectează alimentele?", "Nu, aplicăm țintit, cu respectarea normelor de siguranță alimentară."),
        ],
    },
    {
        "slug": "combatere-purici",
        "name": "Combatere purici",
        "icon": "🦟",
        "title": "Combatere purici în Huși și Moldova | Tratament locuințe și curți",
        "desc": "Eliminăm puricii din locuințe, curți și spații cu animale prin tratamente profesionale. Pulverizare reziduală sigură pentru familie. Huși și toată Moldova.",
        "h1": "Combatere purici — scapă de înțepături în casă și curte",
        "lead": "Puricii pătrund în casă prin animale de companie sau din curte și se înmulțesc în covoare, mochete și crăpături. Tratamentul profesional îi elimină complet, inclusiv larvele.",
        "sections": [
            ("De ce puricii revin după tratamente simple", [
                "Doar o mică parte din populația de purici se află pe animale; restul (ouă, larve, pupe) este în mediu — covoare, paturi, fisuri.",
                "Tratăm întreg mediul, vizând toate stadiile de dezvoltare, pentru a opri ciclul de înmulțire.",
            ]),
            ("Cum decurge intervenția", [
                "Inspectăm zonele de risc (locurile preferate ale animalelor).",
                "Aplicăm pulverizare reziduală pe pardoseli, covoare și crăpături.",
                "Tratăm și curtea sau zonele exterioare, dacă e cazul.",
                "Recomandări pentru tratarea animalelor la veterinar.",
            ]),
            ("Unde intervenim", [
                "Apartamente și case", "Curți și grădini",
                "Spații cu animale de companie", "Pensiuni și cazări",
            ]),
        ],
        "faq": [
            ("Trebuie să-mi tratez și animalul?", "Da, recomandăm tratarea animalelor la medicul veterinar, în paralel cu tratarea spațiului."),
            ("Pot sta în casă în timpul tratamentului?", "Pe durata aplicării și a aerisirii, nu. Îți dăm toate instrucțiunile."),
            ("E nevoie de o singură intervenție?", "De multe ori da, dar pentru infestări mari putem recomanda o revenire."),
        ],
    },
    {
        "slug": "combatere-capuse",
        "name": "Combatere căpușe",
        "icon": "🕷️",
        "title": "Combatere căpușe în Huși și Moldova | Tratament curți și spații verzi",
        "desc": "Tratamente împotriva căpușelor pentru curți, grădini, parcuri și spații verzi. Protejează familia și animalele de boli transmise de căpușe. Huși și toată Moldova.",
        "h1": "Combatere căpușe — curte sigură pentru copii și animale",
        "lead": "Căpușele transmit boli grave (boala Lyme, encefalită) și se ascund în iarbă și vegetație. Tratăm spațiile verzi pentru a reduce drastic riscul de înțepături.",
        "sections": [
            ("De ce e importantă combaterea căpușelor", [
                "Căpușele se găsesc în iarba înaltă, tufișuri și zone umbrite, de unde se prind de oameni și animale.",
                "Un tratament aplicat la începutul sezonului cald reduce considerabil populația și riscul de îmbolnăvire.",
            ]),
            ("Ce oferim", [
                "Pulverizare pe gazon, vegetație și garduri vii.",
                "Tratament pentru zone de joacă și locuri de relaxare.",
                "Soluții pentru parcuri, incinte și spații verzi mari.",
                "Recomandări pentru protejarea animalelor de companie.",
            ]),
            ("Locuri tratate", [
                "Curți și grădini private", "Parcuri și spații verzi",
                "Pensiuni, cazări și terenuri de eveniment", "Incinte de firme și instituții",
            ]),
        ],
        "faq": [
            ("Cât ține efectul tratamentului?", "În general câteva săptămâni; pentru sezonul cald recomandăm repetarea."),
            ("Este periculos pentru animale?", "Aplicăm produse avizate; după uscare, curtea poate fi folosită în siguranță."),
            ("Când e cel mai bun moment?", "Primăvara și la începutul verii, când căpușele devin active."),
        ],
    },
    {
        "slug": "combatere-viespi",
        "name": "Combatere viespi",
        "icon": "🐝",
        "title": "Combatere viespi și gărgăuni Huși și Moldova | Îndepărtare cuiburi",
        "desc": "Îndepărtăm cuiburile de viespi și gărgăuni în siguranță, din poduri, streașini, copaci și curți. Intervenție rapidă în Huși și toată Moldova.",
        "h1": "Combatere viespi și gărgăuni — îndepărtarea cuiburilor în siguranță",
        "lead": "Un cuib de viespi sau gărgăuni lângă casă este periculos, mai ales pentru copii și persoanele alergice. Îl îndepărtăm în siguranță, cu echipament de protecție profesional.",
        "sections": [
            ("De ce să nu încerci singur", [
                "Viespile și gărgăunii devin agresivi când cuibul este deranjat, iar înțepăturile multiple pot fi periculoase, uneori chiar fatale pentru persoanele alergice.",
                "Intervenim cu echipament de protecție și substanțe profesionale, neutralizând cuibul complet.",
            ]),
            ("Cum lucrăm", [
                "Localizăm cuibul și evaluăm riscul.",
                "Tratăm și neutralizăm cuibul în siguranță.",
                "Îndepărtăm cuibul, acolo unde este posibil.",
                "Recomandări pentru prevenirea revenirii.",
            ]),
            ("Unde intervenim", [
                "Poduri, streașini și acoperișuri", "Copaci, garduri și curți",
                "Balcoane și pereți exteriori", "Spații comerciale și instituții",
            ]),
        ],
        "faq": [
            ("Cât de repede puteți veni?", "Tratăm aceste situații cu prioritate, de multe ori chiar în aceeași zi, în funcție de zonă."),
            ("Este periculos pentru cei din casă?", "Vă spunem exact cum să procedați în timpul intervenției pentru siguranța tuturor."),
            ("Reveniți dacă apare alt cuib?", "Da, oferim recomandări preventive și putem reveni la nevoie."),
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
    {"slug": "pascani", "name": "Pașcani", "judet": "Iași",
     "ctx": "Oferim servicii DDD în Pașcani pentru locuințe, blocuri, firme și spații comerciale."},
    {"slug": "negresti", "name": "Negrești", "judet": "Vaslui",
     "ctx": "Fiind aproape de baza noastră din Huși, ajungem rapid în Negrești și satele din jur."},
    {"slug": "tecuci", "name": "Tecuci", "judet": "Galați",
     "ctx": "Intervenim în Tecuci și împrejurimi pentru persoane fizice și firme."},
    {"slug": "adjud", "name": "Adjud", "judet": "Vrancea",
     "ctx": "Deservim Adjud și zona de nord a județului Vrancea pentru tratamente DDD complete."},
    {"slug": "onesti", "name": "Onești", "judet": "Bacău",
     "ctx": "Oferim servicii de dezinsecție, deratizare și dezinfecție în Onești și localitățile vecine."},
    {"slug": "comanesti", "name": "Comănești", "judet": "Bacău",
     "ctx": "Ne deplasăm în Comănești și valea Trotușului pentru intervenții împotriva dăunătorilor."},
    {"slug": "moinesti", "name": "Moinești", "judet": "Bacău",
     "ctx": "Intervenim în Moinești pentru locuințe, firme și instituții, cu programări flexibile."},
    {"slug": "targu-neamt", "name": "Târgu Neamț", "judet": "Neamț",
     "ctx": "Oferim servicii DDD în Târgu Neamț și zona Cetății, pentru clienți rezidențiali și firme."},
    {"slug": "falticeni", "name": "Fălticeni", "judet": "Suceava",
     "ctx": "Ne deplasăm în Fălticeni și împrejurimi pentru dezinsecție, deratizare și dezinfecție."},
    {"slug": "radauti", "name": "Rădăuți", "judet": "Suceava",
     "ctx": "Deservim Rădăuți și nordul Bucovinei pentru tratamente profesionale împotriva dăunătorilor."},
    {"slug": "dorohoi", "name": "Dorohoi", "judet": "Botoșani",
     "ctx": "Oferim servicii DDD în Dorohoi pentru locuințe, firme și spații comerciale."},
    {"slug": "targu-frumos", "name": "Târgu Frumos", "judet": "Iași",
     "ctx": "Intervenim în Târgu Frumos și satele din jur, atât pentru persoane fizice, cât și pentru firme."},
    {"slug": "harlau", "name": "Hârlău", "judet": "Iași",
     "ctx": "Ne deplasăm în Hârlău și împrejurimi pentru intervenții de dezinsecție, deratizare și dezinfecție."},
]

# ----------------------------------------------------------------------------
# DATE: ARTICOLE (resurse / blog) — pentru SEO informativ și AEO
# ----------------------------------------------------------------------------
ARTICLES = [
    {
        "slug": "cum-scapi-de-gandaci",
        "title": "Cum scapi definitiv de gândaci în casă — ghid complet 2026",
        "desc": "Ghid practic: de ce apar gândacii, ce funcționează cu adevărat și când e nevoie de o firmă de dezinsecție. Sfaturi de la profesioniști DDD.",
        "h1": "Cum scapi definitiv de gândaci în casă",
        "intro": "Gândacii de bucătărie sunt printre cei mai persistenți dăunători din locuințe. Apar peste noapte, se ascund în spatele electrocasnicelor și revin oricât de des ai curăța. În acest ghid îți explicăm de ce apar, ce poți face singur și când merită să chemi o firmă specializată.",
        "sections": [
            ("De ce apar gândacii în casă?", [
                "Gândacii caută trei lucruri: căldură, umezeală și hrană. Bucătăria și baia le oferă pe toate. Ei pot pătrunde prin canalizare, prin fisuri, prin ambalaje aduse din magazin sau dintr-un apartament vecin infestat.",
                "Important de știut: prezența gândacilor nu înseamnă neapărat lipsă de igienă. Chiar și în case curate pot apărea dacă există o sursă în bloc sau în vecinătate.",
            ]),
            ("Ce poți face singur", [
                "Elimină sursele de apă și hrană: șterge firimiturile, nu lăsa vase nespălate, repară robinetele care picură.",
                "Astupă fisurile și spațiile din spatele plintelor și din jurul țevilor.",
                "Folosește capcane adezive pentru a estima amploarea problemei.",
            ]),
            ("De ce metodele din comerț nu sunt suficiente", [
                "Spray-urile din comerț omoară gândacii vizibili, dar nu ajung la cuib și nu afectează ouăle. O singură femelă poate produce sute de urmași, așa că infestarea revine rapid.",
                "Tratamentele profesionale folosesc geluri și substanțe reziduale pe care gândacii le duc în ascunzișuri, eliminând și colonia, și generația următoare.",
            ]),
            ("Când să chemi o firmă de dezinsecție", [
                "Dacă vezi gândaci ziua (semn de infestare mare), dacă revin după tratamentele tale sau dacă locuiești la bloc, o firmă specializată rezolvă problema de durată, cu garanție.",
            ]),
        ],
        "cta_service": ("combatere-gandaci", "Vezi serviciul de combatere gândaci"),
        "faq": [
            ("Cât durează să scap complet de gândaci?", "Cu un tratament profesional, vezi o scădere mare în prima săptămână și eliminare completă în 2–3 săptămâni, pe măsură ce sunt afectate și ouăle."),
            ("Gândacii înseamnă că am casa murdară?", "Nu neapărat. Pot apărea și în case curate, mai ales la bloc, dacă există o sursă în vecinătate."),
        ],
    },
    {
        "slug": "cat-costa-deratizarea",
        "title": "Cât costă o deratizare? Ghid de prețuri 2026",
        "desc": "De ce variază prețul unei deratizări, ce influențează costul și cum obții o ofertă corectă pentru locuință sau firmă. Explicat de specialiști DDD.",
        "h1": "Cât costă o deratizare? La ce să te aștepți",
        "intro": "Una dintre primele întrebări când apar șoareci sau șobolani este „cât costă să scap de ei?”. Răspunsul corect este: depinde. În acest articol îți explicăm ce influențează prețul unei deratizări, ca să știi la ce să te aștepți și cum eviți surprizele.",
        "sections": [
            ("Ce influențează prețul unei deratizări", [
                "Mărimea spațiului — un apartament costă mai puțin decât un depozit sau o hală.",
                "Gradul de infestare — o problemă incipientă se rezolvă mai ușor decât o infestare avansată.",
                "Tipul spațiului — casele cu curte, firmele alimentare sau spațiile cu cerințe HACCP necesită soluții specifice.",
                "Numărul de intervenții — uneori e nevoie de o revenire de control sau de un plan de monitorizare.",
            ]),
            ("De ce nu există un preț fix afișat", [
                "O firmă serioasă nu îți dă un preț final fără să știe situația, pentru că ar fi fie prea mare, fie nereal de mic. De aceea oferim o evaluare și o ofertă gratuită, adaptată cazului tău.",
            ]),
            ("Cum obții o ofertă corectă", [
                "Descrie cât mai exact problema (ce ai văzut, de când, în ce spațiu).",
                "Cere o ofertă clară, care include eventualele reveniri.",
                "Verifică dacă firma folosește substanțe avizate și oferă documente (important pentru firme).",
            ]),
        ],
        "cta_service": ("combatere-soareci-sobolani", "Vezi serviciul de deratizare"),
        "faq": [
            ("Deratizarea se face o singură dată?", "Pentru locuințe, de obicei o intervenție cu o revenire de control. Firmele au nevoie de un plan periodic de monitorizare."),
            ("Cum primesc un preț?", "Sună-ne sau scrie-ne pe WhatsApp cu detaliile spațiului și îți dăm o ofertă gratuită, fără obligații."),
        ],
    },
    {
        "slug": "cum-recunosti-plosnitele",
        "title": "Cum recunoști ploșnițele de pat și cum scapi de ele",
        "desc": "Semnele clare ale unei infestări cu ploșnițe, unde se ascund și de ce tratamentul profesional este singura soluție de durată.",
        "h1": "Cum recunoști ploșnițele de pat și cum scapi de ele",
        "intro": "Ploșnițele de pat sunt printre cei mai neplăcuți dăunători: se ascund bine, sunt active noaptea și se înmulțesc rapid. Recunoașterea timpurie face diferența. Iată semnele la care să fii atent și ce poți face.",
        "sections": [
            ("Semnele unei infestări cu ploșnițe", [
                "Înțepături în șir sau grupate, pe zonele expuse în timpul somnului (brațe, gât, picioare).",
                "Pete mici, închise la culoare, pe așternuturi sau saltea (excremente).",
                "Pete de sânge pe cearșafuri și un miros dulceag, neplăcut, la infestări mari.",
                "Ploșnițe vii sau pielițe lăsate în urmă, în cusăturile saltelei și ale tăbliei.",
            ]),
            ("Unde se ascund", [
                "În cusăturile saltelei și ale tăbliei de pat, în plinte, prize, rame de tablouri și mobilier, oriunde aproape de locul unde dormi.",
            ]),
            ("De ce tratamentul profesional este necesar", [
                "Ploșnițele rezistă la multe soluții din comerț și se ascund în locuri greu accesibile. Un tratament profesional ajunge în toate ascunzișurile și tratează și ouăle, prevenind reinfestarea. La nevoie folosim și tratament termic.",
            ]),
        ],
        "cta_service": ("combatere-plosnite", "Vezi serviciul de combatere ploșnițe"),
        "faq": [
            ("Trebuie să arunc salteaua?", "În cele mai multe cazuri, nu. Tratamentul profesional salvează mobilierul."),
            ("Ploșnițele transmit boli?", "Nu sunt cunoscute ca transmițătoare de boli, dar înțepăturile pot provoca mâncărimi, reacții alergice și un disconfort major."),
        ],
    },
    {
        "slug": "ddd-restaurant-haccp",
        "title": "DDD pentru restaurante: ce cere HACCP și de ce contează",
        "desc": "Ghid pentru restaurante și HoReCa: ce presupune un contract DDD, ce documente cere HACCP/DSV și cum eviți amenzile la control.",
        "h1": "DDD pentru restaurante: ce cere HACCP",
        "intro": "Pentru orice restaurant, magazin alimentar sau unitate HoReCa, serviciile DDD nu sunt opționale — sunt o cerință legală și o condiție pentru a trece controalele DSV. Iată ce trebuie să știi.",
        "sections": [
            ("De ce au restaurantele nevoie de DDD", [
                "Prezența dăunătorilor într-un spațiu alimentar înseamnă risc de contaminare, amenzi și chiar închiderea unității. Un program DDD constant previne aceste probleme.",
            ]),
            ("Ce documente cere HACCP / DSV", [
                "Contract DDD cu o firmă autorizată.",
                "Grafic și procese-verbale ale intervențiilor.",
                "Fișe tehnice și avize pentru substanțele folosite.",
                "Hărți de amplasare a stațiilor de deratizare.",
            ]),
            ("Cum funcționează un contract DDD pentru firme", [
                "Stabilim un plan de intervenții periodice (lunar sau trimestrial), amplasăm stații de monitorizare securizate și îți furnizăm toată documentația necesară pentru controale.",
            ]),
        ],
        "cta_service": ("dezinfectie-spatii", "Vezi serviciile pentru firme"),
        "faq": [
            ("Cât de des trebuie făcut DDD într-un restaurant?", "Recomandarea uzuală este lunar sau trimestrial, în funcție de specific, plus intervenții la nevoie."),
            ("Primesc documente pentru control?", "Da. Oferim toate documentele cerute de HACCP și DSV: contract, procese-verbale, fișe tehnice și hărți de amplasare."),
        ],
    },
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
  <meta name="theme-color" content="#1f9d55" />
  <link rel="canonical" href="{canonical}" />
  <meta property="og:type" content="website" />
  <meta property="og:url" content="{canonical}" />
  <meta property="og:title" content="{html.escape(title)}" />
  <meta property="og:description" content="{html.escape(desc)}" />
  <meta property="og:locale" content="ro_RO" />
  <meta property="og:image" content="{OG_IMAGE}" />
  <meta name="twitter:card" content="summary_large_image" />
  <meta name="twitter:image" content="{OG_IMAGE}" />
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@500;600;700;800&family=Inter:wght@400;500;600&display=swap" rel="stylesheet" />
  <link rel="stylesheet" href="../assets/styles.css" />
  <link rel="icon" type="image/svg+xml" href="../assets/logo.svg" />
  {('<script type="application/ld+json">' + chr(10) + schema + chr(10) + '  </script>') if schema else ''}
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
        <h4>Legal</h4>
        <a href="../politica-confidentialitate.html">Politică de confidențialitate</a>
        <a href="../termeni-si-conditii.html">Termeni și condiții</a>
        <a href="https://anpc.ro/ce-este-sal/" target="_blank" rel="noopener">ANPC — SAL</a>
        <a href="https://ec.europa.eu/consumers/odr" target="_blank" rel="noopener">ANPC — SOL</a>
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

def breadcrumb_schema(items):
    li = ",".join(
        '{"@type":"ListItem","position":%d,"name":"%s","item":"%s"}'
        % (i + 1, name.replace('"', "'"), url) for i, (name, url) in enumerate(items))
    return '{"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[%s]}' % li

def join_schemas(*schemas):
    sep = "\n  </script>\n  <script type=\"application/ld+json\">\n"
    return sep.join(s for s in schemas if s)

def howto_schema(name, steps):
    st = ",".join(
        '{"@type":"HowToStep","position":%d,"name":"%s","text":"%s"}'
        % (i + 1, s.replace('"', "'")[:60], s.replace('"', "'")) for i, s in enumerate(steps))
    return ('{"@context":"https://schema.org","@type":"HowTo","name":"%s","step":[%s]}'
            % (name.replace('"', "'"), st))

def process_steps(sections):
    """Întoarce pașii dintr-o secțiune de tip 'Cum lucrăm/decurge', dacă există."""
    for title, items in sections:
        t = title.lower()
        if t.startswith("cum") or "metod" in t or t.startswith("ce includem"):
            return title, items
    return None, None

# FAQ comun adăugat pe fiecare pagină (preț + programare) — important pentru AEO
PRICE_FAQ = [
    ("Cât costă serviciul?", "Prețul depinde de mărimea spațiului și de gradul infestării. Îți oferim o evaluare și o ofertă gratuită, cu un preț corect și fără costuri ascunse. Sună la " + PHONE_DISPLAY + "."),
    ("Cât de repede puteți veni?", "De multe ori intervenim chiar în aceeași zi sau a doua zi, în funcție de zonă și de programul nostru."),
]

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
    for c in CITIES:
        if kind == "city" and c["slug"] == current_slug:
            continue
        links.append((f'../zone/{c["slug"]}.html', f'📍 DDD {c["name"]}'))
    for a in ARTICLES:
        if kind == "article" and a["slug"] == current_slug:
            continue
        links.append((f'../resurse/{a["slug"]}.html', f'📖 {a["h1"]}'))
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
    faqs = s["faq"] + PRICE_FAQ
    crumb = breadcrumb_schema([("Acasă", f"{BASE_URL}/"), ("Servicii", f"{BASE_URL}/#servicii"), (s["name"], canonical)])
    p_title, p_steps = process_steps(s["sections"])
    howto = howto_schema(f"{s['name']} — cum decurge", p_steps) if p_steps and all(len(i) < 120 for i in p_steps) else ""
    schema = join_schemas(service_schema(s, canonical), faq_schema(faqs), howto, crumb)
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
{faq_html(faqs)}
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
    ] + PRICE_FAQ
    schema = ('{"@context":"https://schema.org","@type":"PestControlService","name":"Valterm Invest SRL – DDD %s",'
              '"telephone":"%s","areaServed":"%s, România",'
              '"address":{"@type":"PostalAddress","addressLocality":"Huși","addressRegion":"Vaslui","addressCountry":"RO"},'
              '"url":"%s"}' % (c['name'], PHONE_TEL, c['name'], canonical))
    crumb = breadcrumb_schema([("Acasă", f"{BASE_URL}/"), ("Zone", f"{BASE_URL}/#zona"), (c["name"], canonical)])
    schema = join_schemas(schema, faq_schema(faqs), crumb)
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

def build_article(a):
    canonical = f"{BASE_URL}/resurse/{a['slug']}.html"
    svc_slug, svc_label = a["cta_service"]
    article_schema = ('{"@context":"https://schema.org","@type":"Article","headline":"%s",'
                      '"description":"%s","author":{"@type":"Organization","name":"Valterm Invest SRL"},'
                      '"publisher":{"@type":"Organization","name":"Valterm Invest SRL","logo":{"@type":"ImageObject","url":"%s"}},'
                      '"image":"%s","mainEntityOfPage":"%s"}'
                      % (a["title"].replace('"', "'"), a["desc"].replace('"', "'"),
                         BASE_URL + "/assets/logo.svg", OG_IMAGE, canonical))
    crumb = breadcrumb_schema([("Acasă", f"{BASE_URL}/"), ("Resurse", f"{BASE_URL}/resurse/"), (a["h1"], canonical)])
    schema = join_schemas(article_schema, faq_schema(a["faq"]), crumb)
    page = head(a["title"], a["desc"], canonical, schema)
    page += header_html()
    page += f"""
  <section class="lp-hero">
    <div class="container">
      <div class="breadcrumb"><a href="../index.html">Acasă</a><span>›</span> Resurse <span>›</span> {html.escape(a['h1'])}</div>
      <h1>{html.escape(a['h1'])}</h1>
      <p class="lp-lead">{html.escape(a['intro'])}</p>
    </div>
  </section>
  <section class="lp-body">
    <div class="container lp-grid">
      <div class="prose">
{prose_sections(a['sections'])}
      <h2>Ai nevoie de ajutor profesionist?</h2>
      <p>Dacă problema persistă sau vrei să fii sigur că dispare definitiv, echipa noastră intervine rapid în Huși și toată Moldova, cu garanție. <a href="../servicii/{svc_slug}.html">{html.escape(svc_label)}</a> sau sună la <a href="tel:{PHONE_TEL}">{PHONE_DISPLAY}</a>.</p>
{faq_html(a['faq'])}
      </div>
{aside_html('Spune-ne pe scurt ce problemă ai.')}
    </div>
  </section>"""
    page += related_html(a["slug"], "article")
    page += footer_html()
    path = os.path.join(ROOT, "resurse", f"{a['slug']}.html")
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(page)
    return canonical

def build_404():
    page = head("Pagina nu a fost găsită | Valterm Invest", "Pagina căutată nu există. Întoarce-te la pagina principală sau contactează-ne.", f"{BASE_URL}/404.html", "")
    # Pagina 404 e la rădăcină => căile relative trebuie să fie fără "../"
    page = page.replace('href="../', 'href="').replace('src="../', 'src="')
    body = f"""
  <header class="site-header" id="top">
    <div class="container nav-inner">
      <a href="/" class="brand">
        <img src="/assets/logo.svg" alt="Valterm Invest" class="brand-mark" />
        <span class="brand-text"><strong>Valterm Invest</strong><small>Dezinsecție · Deratizare · Dezinfecție</small></span>
      </a>
    </div>
  </header>
  <section class="lp-hero" style="text-align:center;padding:90px 0;">
    <div class="container">
      <h1 style="margin:0 auto;">404 — Pagina nu a fost găsită</h1>
      <p class="lp-lead" style="margin:18px auto 28px;">Ne pare rău, pagina căutată nu există sau a fost mutată.</p>
      <div class="lp-actions" style="justify-content:center;">
        <a href="/" class="btn btn-primary">Mergi la pagina principală</a>
        <a href="tel:{PHONE_TEL}" class="btn btn-ghost">📞 {PHONE_DISPLAY}</a>
      </div>
    </div>
  </section>
</body>
</html>"""
    with open(os.path.join(ROOT, "404.html"), "w", encoding="utf-8") as f:
        f.write(page + body)

def main():
    urls = [f"{BASE_URL}/"]
    for s in SERVICES:
        urls.append(build_service(s))
    for c in CITIES:
        urls.append(build_city(c))
    for a in ARTICLES:
        urls.append(build_article(a))
    build_404()

    # sitemap.xml (cu lastmod)
    entries = "\n".join(
        f"  <url><loc>{u}</loc><lastmod>{TODAY}</lastmod><changefreq>monthly</changefreq>"
        f"<priority>{'1.0' if u.endswith('/') else '0.8'}</priority></url>"
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

    print(f"Generate: {len(SERVICES)} servicii, {len(CITIES)} orașe, {len(ARTICLES)} articole, sitemap cu {len(urls)} URL-uri.")

if __name__ == "__main__":
    main()
