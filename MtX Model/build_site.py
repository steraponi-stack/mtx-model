#!/usr/bin/env python3
# Generatore pagine statiche — MtX Model
# Nessuna dipendenza. Produce HTML standalone (funziona da file://).

import os

ROOT = "/Users/sraponii/Desktop/MtX Model/mtx-model"
SEASON = "ACF Fiorentina · 2026/27"
SIGN = "MtX Model · Stefano Raponi"
VERSION = "v1.0 · Settembre 2026"


def rel(depth):
    """prefisso relativo verso la root del sito"""
    return "../" * depth if depth else "./"


def doc(depth, title, body, extra_head=""):
    css = rel(depth) + "assets/css/design-system.css"
    return f"""<!DOCTYPE html>
<html lang="it" data-club="fiorentina">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title} — MtX Model</title>
<link rel="stylesheet" href="{css}">{extra_head}
</head>
<body>
{body}
</body>
</html>
"""


def header(depth, crumbs):
    """crumbs: lista di (label, href|None). L'ultimo è la pagina corrente."""
    home = rel(depth) + "index.html"
    parts = []
    norm = [c if isinstance(c, tuple) else (c, None) for c in crumbs]
    for i, (label, href) in enumerate(norm):
        last = i == len(norm) - 1
        if last or not href:
            parts.append(f'<span class="current">{label}</span>')
        else:
            parts.append(f'<a href="{href}">{label}</a>')
    trail = '<span class="sep">/</span>'.join(parts)
    return f"""<header class="site-header">
  <a class="home-link" href="{home}">← Sistema</a>
  <span class="breadcrumb">{trail}</span>
  <span class="season">{SEASON}</span>
</header>"""


def linkify(depth, href):
    """href sempre relativo alla root del sito → relativo alla pagina corrente"""
    if href.startswith(("http://", "https://", "mailto:")):
        return href
    return rel(depth) + href


def footer(depth, links):
    """links: lista di (label, href) — href relativo alla root del sito"""
    nav = "\n    ".join(
        f'<a href="{linkify(depth, href)}">{label}</a>'
        for label, href in links
    )
    return f"""<footer class="site-footer">
  <nav class="footer-nav">
    {nav}
  </nav>
  <span class="footer-sign">{SIGN} · {VERSION}</span>
</footer>"""


def write(path_parts, html):
    full = os.path.join(ROOT, *path_parts)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w", encoding="utf-8") as f:
        f.write(html)
    print("  ✓", "/".join(path_parts))


# ---------------------------------------------------------------------------
# 1. PAGINE PLACEHOLDER  (nodi 🔴 in costruzione)
# ---------------------------------------------------------------------------
def placeholder(depth, crumbs, title, desc_paras, related, foot):
    paras = "\n    ".join(f"<p>{p}</p>" for p in desc_paras)
    rel_html = ""
    if related:
        items = "\n      ".join(
            f'<a class="node-card" href="{linkify(depth, h)}"><span class="node-status {s}"></span>'
            f'<span class="node-body"><span class="node-name">{l}</span></span></a>'
            for l, h, s in related
        )
        rel_html = f"""
    <div class="related">
      <div class="related-label">Sezioni correlate già disponibili</div>
      <div class="node-list">
      {items}
      </div>
    </div>"""
    body = f"""{header(depth, crumbs)}
<main>
  <div class="placeholder-block">
    <span class="status-badge todo">In costruzione</span>
    <h1>{title}</h1>
    {paras}{rel_html}
  </div>
</main>
{footer(depth, foot)}"""
    return doc(depth, title, body)


PLACEHOLDERS = [
    # (path_parts, depth, crumbs, title, paragraphs, related, footer_links)
    # NB: perche/scopo.html è ora una pagina a mano (grafico identitario) — non rigenerarla qui.

    (["come", "metodologia", "index.html"], 2,
     [("Come", None), ("Metodologia")],
     "Metodologia",
     ['Il modello ecologico come fondamento metodologico: perché questa scelta, cosa implica, come orienta tutto il lavoro.',
      'Sotto-nodi previsti: <strong>Modello Ecologico</strong> (il calcio come ecosistema, cognizione e apprendimento, CLA e auto-organizzazione) e <strong>Principi Metodologici</strong> (design dei vincoli, manipolazione dell\'ambiente, feedback implicito vs esplicito).'],
     [("Modello di Gioco", "come/modello-gioco/index.html", "partial"),
      ("Valori", "come/valori/index.html", "done")],
     [("Come — Modello di Gioco", "come/modello-gioco/index.html"), ("Home", "index.html")]),

    (["cosa", "modello-allenamento", "morfociclo.html"], 2,
     [("Cosa", None), ("Modello di Allenamento", "index.html"), ("Morfociclo")],
     "Morfociclo",
     ['Struttura della settimana tipo, principi di periodizzazione, distribuzione dei carichi per fase.',
      'Sotto-nodi previsti: <strong>Progettazione</strong> (come si costruisce la settimana) e <strong>Tipologie di settimana</strong>.'],
     [("Tipologia Compiti", "cosa/modello-allenamento/compiti.html", "done"),
      ("Modello di Gioco", "come/modello-gioco/index.html", "partial")],
     [("Modello di Allenamento", "cosa/modello-allenamento/index.html"), ("Home", "index.html")]),

    (["cosa", "modello-allenamento", "sessione.html"], 2,
     [("Cosa", None), ("Modello di Allenamento", "index.html"), ("Sessione")],
     "Struttura della Sessione",
     ['Struttura della sessione tipo — introduttivi → ottimizzazione → completamento — e logica di costruzione.',
      'Sotto-nodi previsti: <strong>Struttura</strong> e <strong>Principi di costruzione</strong>.'],
     [("Tipologia Compiti", "cosa/modello-allenamento/compiti.html", "done")],
     [("Modello di Allenamento", "cosa/modello-allenamento/index.html"), ("Home", "index.html")]),

    (["cosa", "framework-2sf.html"], 1,
     [("Cosa", None), ("Framework 2SF")],
     "Framework 2SF",
     ['<strong>Sfida · Struttura · Focus · Feedback</strong>. Il framework per la progettazione dei mezzi di allenamento.',
      'La pagina conterrà il grafico 2SF e la spiegazione applicata a partire dalla guida pratica MtX Model.'],
     [("Mezzi e Nomenclatura", "cosa/mezzi.html", "done"),
      ("Tipologia Compiti", "cosa/modello-allenamento/compiti.html", "done")],
     [("Mezzi", "cosa/mezzi.html"), ("Modello di Allenamento", "cosa/modello-allenamento/index.html"), ("Home", "index.html")]),

    (["cosa", "sviluppo-individuale.html"], 1,
     [("Cosa", None), ("Sviluppo Sistemico Individuale")],
     "Sviluppo Sistemico Individuale",
     ['Framework di lettura integrata del singolo calciatore: tecnica, tattica, fisica, mentale, emotiva, bio-energetica.',
      'Fase 1 a uso interno; Fase 2 in sviluppo con l\'area Fisica/Performance. Solo staff tecnico.'],
     [("Modello di Gioco", "come/modello-gioco/index.html", "partial"),
      ("Mezzi e Nomenclatura", "cosa/mezzi.html", "done")],
     [("Home", "index.html")]),

    (["contesto", "chi-siamo.html"], 1,
     [("Cornice esterna", None), ("Chi Siamo")],
     "Chi Siamo — Staff & Organigramma",
     ['Organigramma staff, ruoli e compiti di ciascuno, struttura T-shaped (Raponi / Vaccariello), aree di coordinamento: Tecnica, Analisi, Fisica/Performance, Portieri.',
      'Pagina con schema grafico dell\'organigramma e schede ruolo. Versione dirigenti più sintetica.'],
     [("Contesto Socio-Culturale", "contesto/socio-culturale.html", "done")],
     [("Contesto Socio-Culturale", "contesto/socio-culturale.html"), ("Home", "index.html")]),

    (["come", "modello-gioco", "dimensioni.html"], 2,
     [("Come", None), ("Modello di Gioco", "index.html"), ("Le 4 Dimensioni")],
     "Le 4 Dimensioni",
     ['<strong>Intensità, Ritmo, Continuità, Adattabilità</strong>: cosa significano in campo, come si misurano, come si allena ciascuna.',
      'Contenuto in costruzione a partire dalle slide del Modello di Gioco.'],
     [("5 Principi Fondamentali", "come/modello-gioco/principi-fondamentali/index.html", "partial"),
      ("Fasi di Gioco — Possesso", "come/modello-gioco/fasi/possesso.html", "done")],
     [("Modello di Gioco", "come/modello-gioco/index.html"), ("Home", "index.html")]),
]

print("PLACEHOLDER:")
for pp, d, cr, t, ps, rl, ft in PLACEHOLDERS:
    write(pp, placeholder(d, cr, t, ps, rl, ft))


# ---------------------------------------------------------------------------
# 2. VALORI
# ---------------------------------------------------------------------------
VALORI = [
    ("rispetto", "Rispetto", "Più di ogni regola.",
     "Rispettare persone e cose significa riconoscere l'importanza di ogni relazione e saper vedere nell'altro la sua unicità e il suo potenziale."),
    ("coraggio", "Coraggio", "Affronta ogni momento. Fino in fondo.",
     "Affrontare pienamente ogni momento e senza paura di sbagliare. Il coraggio è la condizione dell'eccellenza."),
    ("umilta", "Umiltà", "A testa alta, ma con i piedi per terra.",
     "Ogni corsa in più è un tributo a chi ci sostiene. Incarnare con generosità totale il nostro spirito e lo spirito di questa città."),
    ("unione", "Unione", "Gioca per il compagno.",
     "Il NOI prevale sempre sull'IO. L'unicità ha senso solo al servizio della squadra. È dall'interazione dei singoli che emerge la forza del collettivo."),
    ("ambizione", "Ambizione", "Punta in alto. Ogni giorno è una nuova sfida.",
     "Non accontentarsi mai di quello che si era ieri. Affrontare da protagonisti sfide sempre nuove."),
]

def valore_page(slug, name, claim, desc, prev_v, next_v):
    depth = 2
    crumbs = [("Come", None), ("Valori", "index.html"), (name)]
    base = "come/valori/"
    nav = []
    if prev_v:
        nav.append(("← " + prev_v[1], base + prev_v[0] + ".html"))
    nav.append(("Tutti i valori", base + "index.html"))
    if next_v:
        nav.append((next_v[1] + " →", base + next_v[0] + ".html"))
    body = f"""{header(depth, crumbs)}
<main>
  <section class="page-intro">
    <div class="kicker">Come · Valori</div>
    <h1>{name}</h1>
    <p class="claim">«{claim}»</p>
  </section>
  <section class="page-content">
    <p>{desc}</p>
    <h3>Come si riconosce nei comportamenti</h3>
    <p>Sezione in sviluppo: indicatori osservabili, esempi situazionali in campo e fuori, cosa lo rafforza e cosa lo tradisce.</p>
  </section>
</main>
{footer(depth, nav)}"""
    return doc(depth, name + " — Valori", body)

print("VALORI:")
for i, (slug, name, claim, desc) in enumerate(VALORI):
    prev_v = (VALORI[i-1][0], VALORI[i-1][1]) if i > 0 else None
    next_v = (VALORI[i+1][0], VALORI[i+1][1]) if i < len(VALORI)-1 else None
    write(["come", "valori", slug + ".html"], valore_page(slug, name, claim, desc, prev_v, next_v))

# indice valori
depth = 2
val_cards = "\n      ".join(
    f'<a class="node-card" href="{slug}.html"><span class="node-status done"></span>'
    f'<span class="node-body"><span class="node-name">{name}</span>'
    f'<span class="node-desc">«{claim}»</span></span>'
    f'<span class="node-tag">V{i+1}</span></a>'
    for i, (slug, name, claim, desc) in enumerate(VALORI)
)
valori_head = """
<style>
  .identita-hero { margin: 0 0 var(--gap-section); background:#fff; border: var(--border-subtle); border-radius: var(--radius-card); overflow: hidden; }
  .identita-hero img { width: 100%; height: auto; display: block; }
  .identita-hero figcaption { font-size: var(--text-xs); color: var(--color-text-faint); letter-spacing: 0.04em; padding: 10px 14px; border-top: var(--border-subtle); }
  .identita-missing { padding: 48px 24px; text-align: center; font-size: var(--text-sm); color: var(--color-text-muted); }
  .identita-missing strong { display: block; color: var(--color-black); font-weight: var(--weight-semibold); margin-bottom: 6px; }
</style>"""

identita_fig = (
    '  <figure class="identita-hero">\n'
    '    <img src="../../assets/img/identita_slide.png"\n'
    '         alt="Identità — Il nostro Perché e i nostri Come: la frase di Fabio Grosso al centro, i cinque valori (Ambizione, Rispetto, Coraggio, Umiltà, Unione) con claim e descrizione."\n'
    '         onerror="this.closest(\'.identita-hero\').innerHTML=\'&lt;div class=\\\'identita-missing\\\'&gt;&lt;strong&gt;Slide «Identità» non disponibile&lt;/strong&gt;Carica &lt;code&gt;identita_slide.png&lt;/code&gt; in &lt;code&gt;assets/img/&lt;/code&gt;.&lt;/div&gt;\';">\n'
    '    <figcaption>Slide «Identità» — il Perché al centro, i 5 valori intorno. Il testo per valore è ripreso qui sotto in ogni pagina.</figcaption>\n'
    '  </figure>\n'
    '  <div class="slide-actions" style="margin-bottom:var(--gap-section);">\n'
    '    <a class="btn ghost" href="../../assets/img/identita_slide.png" target="_blank" rel="noopener">Apri la slide a schermo intero ↗</a>\n'
    '  </div>'
)

body = f"""{header(depth, [("Come", None), ("Valori")])}
<main>
  <section class="page-intro">
    <div class="kicker">Come</div>
    <h1>I 5 Valori</h1>
    <p class="subtitle">I principi che guidano i comportamenti e ci rendono unici e riconoscibili.</p>
    <p class="lead">I valori non sono uno slogan: sono il criterio con cui leggiamo ogni scelta, dentro e fuori dal campo. Cinque parole, un solo modo di stare nel gruppo.</p>
  </section>
{identita_fig}
  <div class="update-note">Guida identitaria completa in aggiornamento — Rispetto e Coraggio nella nuova formulazione.</div>
  <section class="page-content">
    <div class="node-list">
      {val_cards}
    </div>
  </section>
</main>
{footer(depth, [("Perché — Scopo", "perche/scopo.html"), ("Modello di Gioco", "come/modello-gioco/index.html"), ("Home", "index.html")])}"""
write(["come", "valori", "index.html"], doc(depth, "I 5 Valori", body, extra_head=valori_head))


# ---------------------------------------------------------------------------
# 3. PRINCIPI FONDAMENTALI
# ---------------------------------------------------------------------------
PRINCIPI = [
    ("percezione", "Percezione", "Conoscere e riconoscere prima di agire.",
     "La lettura continua di spazio, compagni, avversari e palla. Orientare il corpo per vedere più campo e anticipare l'evoluzione del gioco."),
    ("partecipazione", "Partecipazione", "Essere sempre dentro il gioco.",
     "Ogni giocatore è coinvolto nell'azione, con o senza palla. Dare costantemente soluzioni e riferimenti al possessore."),
    ("legame", "Legame", "Muoversi in relazione, non da soli.",
     "Le distanze e i sincronismi che tengono la squadra collegata. Appoggi e mobilità in funzione del codice palla (aperta / chiusa)."),
    ("penetrazione", "Penetrazione", "Cercare sempre di superare la linea.",
     "L'intenzione di progredire e attaccare la profondità. Attrarre per liberare, invadere lo spazio generato."),
    ("mobilita", "Mobilità", "Cambiare posizione per cambiare il problema all'avversario.",
     "Il movimento coordinato che rompe i riferimenti difensivi, crea superiorità e sposta il centro del gioco."),
]

def principio_page(slug, name, claim, desc, prev_p, next_p):
    depth = 3
    crumbs = [("Come", None), ("Modello di Gioco", "../index.html"),
              ("5 Principi", "index.html"), (name)]
    base = "come/modello-gioco/principi-fondamentali/"
    nav = []
    if prev_p:
        nav.append(("← " + prev_p[1], base + prev_p[0] + ".html"))
    nav.append(("I 5 Principi", base + "index.html"))
    if next_p:
        nav.append((next_p[1] + " →", base + next_p[0] + ".html"))
    body = f"""{header(depth, crumbs)}
<main>
  <section class="page-intro">
    <div class="kicker">Modello di Gioco · Principio fondamentale</div>
    <h1>{name}</h1>
    <p class="claim">{claim}</p>
  </section>
  <section class="page-content">
    <p>{desc}</p>
    <h3>Definizione ecologica</h3>
    <p>In sviluppo: come il principio nasce dall'interazione giocatore-ambiente, quali affordance apre, quali vincoli lo favoriscono.</p>
    <h3>Come si manifesta in campo</h3>
    <p>In sviluppo: comportamenti tipici, riferimenti spaziali, relazioni con gli altri principi.</p>
    <h3>Come si allena</h3>
    <p>In sviluppo: forme di gioco, manipolazione dei vincoli, indicatori di osservazione.</p>
  </section>
</main>
{footer(depth, nav)}"""
    return doc(depth, name + " — Principi Fondamentali", body)

print("PRINCIPI FONDAMENTALI:")
for i, (slug, name, claim, desc) in enumerate(PRINCIPI):
    prev_p = (PRINCIPI[i-1][0], PRINCIPI[i-1][1]) if i > 0 else None
    next_p = (PRINCIPI[i+1][0], PRINCIPI[i+1][1]) if i < len(PRINCIPI)-1 else None
    write(["come", "modello-gioco", "principi-fondamentali", slug + ".html"],
          principio_page(slug, name, claim, desc, prev_p, next_p))

depth = 3
pf_cards = "\n      ".join(
    f'<a class="node-card" href="{slug}.html"><span class="node-status todo"></span>'
    f'<span class="node-body"><span class="node-name">{name}</span>'
    f'<span class="node-desc">{claim}</span></span>'
    f'<span class="node-tag">{i+1}P</span></a>'
    for i, (slug, name, claim, desc) in enumerate(PRINCIPI)
)
body = f"""{header(depth, [("Come", None), ("Modello di Gioco", "../index.html"), ("5 Principi Fondamentali")])}
<main>
  <section class="page-intro">
    <div class="kicker">Come · Modello di Gioco</div>
    <h1>I 5 Principi Fondamentali</h1>
    <p class="subtitle">Percezione · Partecipazione · Legame · Penetrazione · Mobilità</p>
    <p class="lead">I cinque principi descrivono <em>come</em> stiamo dentro il gioco in ogni momento. Non sono fasi: agiscono sempre, insieme, e si rinforzano a vicenda attorno al ciclo percezione-azione.</p>
  </section>
  <div class="update-note">Contenuto prodotto nelle slide del Modello di Gioco — pagine di approfondimento in costruzione.</div>
  <section class="page-content">
    <div class="node-list">
      {pf_cards}
    </div>
  </section>
</main>
{footer(depth, [("Modello di Gioco", "come/modello-gioco/index.html"), ("Le 4 Dimensioni", "come/modello-gioco/dimensioni.html"), ("Home", "index.html")])}"""
write(["come", "modello-gioco", "principi-fondamentali", "index.html"],
      doc(depth, "I 5 Principi Fondamentali", body))


# ---------------------------------------------------------------------------
# 4. WRAPPER SLIDE
# ---------------------------------------------------------------------------
def slide_wrapper(depth, crumbs, title, kicker, lead, slide_file, status, foot,
                  related=None):
    slide_src = rel(depth) + "assets/slides/" + slide_file
    note = ""
    if status == "partial":
        note = '<div class="update-note">Slide prodotta — pagina di approfondimento in aggiornamento.</div>\n  '
    rel_html = ""
    if related:
        items = "\n      ".join(
            f'<a class="node-card" href="{linkify(depth, h)}"><span class="node-status {s}"></span>'
            f'<span class="node-body"><span class="node-name">{l}</span></span></a>'
            for l, h, s in related
        )
        rel_html = f"""
  <section class="page-content">
    <h2>Sezioni correlate</h2>
    <div class="node-list">
      {items}
    </div>
  </section>"""
    body = f"""{header(depth, crumbs)}
<main>
  <section class="page-intro">
    <div class="kicker">{kicker}</div>
    <h1>{title}</h1>
    <p class="lead">{lead}</p>
  </section>
  {note}<div class="slide-embed">
    <iframe src="{slide_src}" title="{title} — slide" loading="lazy"
            onload="window.mtxSlideCheck && window.mtxSlideCheck(this)"
            onerror="this.style.display='none';this.nextElementSibling.style.display='flex';"></iframe>
    <div class="slide-missing" style="display:none">
      <strong>Slide non ancora disponibile</strong>
      <span>Aggiungi <code>{slide_file}</code> in <code>assets/slides/</code>.</span>
    </div>
  </div>
  <div class="slide-actions">
    <a class="btn" href="{slide_src}" target="_blank" rel="noopener">Apri la slide a schermo intero ↗</a>
  </div>{rel_html}
</main>
{footer(depth, foot)}
<script src="{rel(depth)}assets/js/slide-fit.js"></script>"""
    return doc(depth, title, body)


print("WRAPPER SLIDE:")

# G0 — Modello di Gioco (index)
write(["come", "modello-gioco", "index.html"], slide_wrapper(
    2,
    [("Come", None), ("Modello di Gioco")],
    "Modello di Gioco", "Come",
    "L'intenzione: «avere la palla per giocare in modo propositivo ed essere protagonisti». Al centro, il ciclo <em>conoscere, riconoscere, risolvere insieme</em> attraverso percezione-azione.",
    "modello_di_gioco_slide.html", "partial",
    [("5 Principi Fondamentali", "come/modello-gioco/principi-fondamentali/index.html"),
     ("Le 4 Dimensioni", "come/modello-gioco/dimensioni.html"),
     ("Fasi di Gioco — Possesso", "come/modello-gioco/fasi/possesso.html"),
     ("Home", "index.html")],
    related=[
        ("I 5 Principi Fondamentali", "come/modello-gioco/principi-fondamentali/index.html", "partial"),
        ("Le 4 Dimensioni", "come/modello-gioco/dimensioni.html", "todo"),
        ("Fase di Possesso", "come/modello-gioco/fasi/possesso.html", "done"),
        ("Fase di Recupero", "come/modello-gioco/fasi/recupero.html", "done"),
        ("Transizioni", "come/modello-gioco/fasi/transizioni.html", "done"),
    ]))

# G4a — Possesso
write(["come", "modello-gioco", "fasi", "possesso.html"], slide_wrapper(
    3,
    [("Come", None), ("Modello di Gioco", "../index.html"), ("Fasi", None), ("Possesso")],
    "Possesso", "Modello di Gioco · Fasi di gioco",
    "Cosa facciamo quando abbiamo la palla. Sotto-fasi: costruzione, sviluppo, finalizzazione. Principio: mantenere per penetrare.",
    "possesso_slide.html", "done",
    [("Recupero", "come/modello-gioco/fasi/recupero.html"),
     ("Transizioni", "come/modello-gioco/fasi/transizioni.html"),
     ("Modello di Gioco", "come/modello-gioco/index.html"), ("Home", "index.html")],
    related=[
        ("Recupero", "come/modello-gioco/fasi/recupero.html", "done"),
        ("Transizioni", "come/modello-gioco/fasi/transizioni.html", "done"),
        ("5 Principi Fondamentali", "come/modello-gioco/principi-fondamentali/index.html", "partial"),
    ]))

# G4b — Recupero
write(["come", "modello-gioco", "fasi", "recupero.html"], slide_wrapper(
    3,
    [("Come", None), ("Modello di Gioco", "../index.html"), ("Fasi", None), ("Recupero")],
    "Recupero", "Modello di Gioco · Fasi di gioco",
    "Cosa facciamo quando dobbiamo riprendere la palla. Sotto-fasi: pressing (blocco alto), contenimento (blocco medio), protezione (blocco basso). Principio: pressione e compattezza.",
    "recupero_slide.html", "done",
    [("← Possesso", "come/modello-gioco/fasi/possesso.html"),
     ("Transizioni", "come/modello-gioco/fasi/transizioni.html"),
     ("Modello di Gioco", "come/modello-gioco/index.html"), ("Home", "index.html")],
    related=[
        ("Possesso", "come/modello-gioco/fasi/possesso.html", "done"),
        ("Transizioni", "come/modello-gioco/fasi/transizioni.html", "done"),
    ]))

# G4c — Transizioni
write(["come", "modello-gioco", "fasi", "transizioni.html"], slide_wrapper(
    3,
    [("Come", None), ("Modello di Gioco", "../index.html"), ("Fasi", None), ("Transizioni")],
    "Transizioni", "Modello di Gioco · Fasi di gioco",
    "I momenti di cambio di condizione: transizione offensiva (T+) subito dopo la riconquista, transizione difensiva (T−) subito dopo la perdita.",
    "transizioni_slide.html", "done",
    [("← Possesso", "come/modello-gioco/fasi/possesso.html"),
     ("← Recupero", "come/modello-gioco/fasi/recupero.html"),
     ("Modello di Gioco", "come/modello-gioco/index.html"), ("Home", "index.html")],
    related=[
        ("Possesso", "come/modello-gioco/fasi/possesso.html", "done"),
        ("Recupero", "come/modello-gioco/fasi/recupero.html", "done"),
    ]))

# A3 — Compiti
write(["cosa", "modello-allenamento", "compiti.html"], slide_wrapper(
    2,
    [("Cosa", None), ("Modello di Allenamento", "index.html"), ("Tipologia Compiti")],
    "Tipologia di Compiti", "Cosa · Modello di Allenamento",
    "Tutte le tipologie di compiti con claim, descrizione e forme di gioco. La base operativa con cui si costruisce la sessione.",
    "tipologia_compiti_slide.html", "done",
    [("Mezzi e Nomenclatura", "cosa/mezzi.html"), ("Morfociclo", "cosa/modello-allenamento/morfociclo.html"),
     ("Home", "index.html")],
    related=[
        ("Mezzi e Nomenclatura", "cosa/mezzi.html", "done"),
        ("Morfociclo", "cosa/modello-allenamento/morfociclo.html", "todo"),
        ("Struttura della Sessione", "cosa/modello-allenamento/sessione.html", "todo"),
    ]))

# C0 — Mezzi  (nomenclatura_guide.html — file non ancora presente: fallback gestito)
write(["cosa", "mezzi.html"], slide_wrapper(
    1,
    [("Cosa", None), ("Mezzi e Nomenclatura")],
    "Mezzi e Nomenclatura", "Cosa · Pratiche",
    "Il sistema di nomenclatura per fasi di gioco, mezzi di allenamento, strutture tipo e forme. Il linguaggio comune dello staff.",
    "nomenclatura_guide.html", "done",
    [("Tipologia Compiti", "cosa/modello-allenamento/compiti.html"),
     ("Framework 2SF", "cosa/framework-2sf.html"), ("Home", "index.html")],
    related=[
        ("Tipologia Compiti", "cosa/modello-allenamento/compiti.html", "done"),
        ("Framework 2SF", "cosa/framework-2sf.html", "todo"),
        ("Modello di Allenamento", "cosa/modello-allenamento/index.html", "partial"),
    ]))


# ---------------------------------------------------------------------------
# 5. INDICE — Modello di Allenamento (A0)
# ---------------------------------------------------------------------------
depth = 2
cards = [
    ("Morfociclo", "morfociclo.html", "todo", "Settimana tipo, periodizzazione, carichi per fase"),
    ("Struttura della Sessione", "sessione.html", "todo", "Introduttivi → ottimizzazione → completamento"),
    ("Tipologia di Compiti", "compiti.html", "done", "Claim, descrizione e forme di gioco per ogni compito"),
]
cards_html = "\n      ".join(
    f'<a class="node-card" href="{h}"><span class="node-status {s}"></span>'
    f'<span class="node-body"><span class="node-name">{l}</span>'
    f'<span class="node-desc">{d}</span></span></a>'
    for l, h, s, d in cards
)
body = f"""{header(depth, [("Cosa", None), ("Modello di Allenamento")])}
<main>
  <section class="page-intro">
    <div class="kicker">Cosa · Pratiche</div>
    <h1>Modello di Allenamento</h1>
    <p class="subtitle">Come il modello di gioco si traduce in allenamento.</p>
    <p class="lead">Il modello di gioco dice <em>come</em> vogliamo giocare. Il modello di allenamento è lo strumento con cui quel gioco viene costruito in campo: la settimana, la sessione, i compiti.</p>
  </section>
  <section class="page-content">
    <div class="node-list">
      {cards_html}
    </div>
  </section>
</main>
{footer(depth, [("Modello di Gioco", "come/modello-gioco/index.html"), ("Mezzi e Nomenclatura", "cosa/mezzi.html"), ("Framework 2SF", "cosa/framework-2sf.html"), ("Home", "index.html")])}"""
write(["cosa", "modello-allenamento", "index.html"], doc(depth, "Modello di Allenamento", body))


# ---------------------------------------------------------------------------
# 6. CONTESTO — socio-culturale
# ---------------------------------------------------------------------------
# NB: contesto/socio-culturale.html è ora una pagina a mano (accordion a 7 sezioni
# con testo estratto da fiorentina_contesto_mobile.html + fiorentina_identita_guida_bozza.html).
# Non rigenerarla qui.

print("\nFatto.")
