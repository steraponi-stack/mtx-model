# Briefing per Claude Code
## Sistema "MtX Model"
*ACF Fiorentina 2026/27 — Stefano Raponi*

---

## Obiettivo

Costruire un sito HTML statico navigabile che rappresenta il framework metodologico e identitario del gruppo di lavoro. Nessun server richiesto — funziona come cartella locale o su hosting statico semplice. Nessun framework JavaScript (no React, no Vue, no Next). HTML5 + CSS3 + JavaScript minimale.

---

## File di riferimento da leggere prima di iniziare

1. `homepage_prototipo.html` — prototipo funzionante della homepage con grafico SVG e panel laterale
2. `architettura_sistema.md` — architettura completa con tutti i nodi, stati e connessioni
3. `Sistema_Design_MtX_Model.md` — design system (tipografia, cromia, componenti)

---

## Struttura cartelle da costruire

```
/mtx-model/
├── index.html                        ← Homepage con mappa SVG navigabile
├── assets/
│   ├── css/
│   │   └── design-system.css         ← CSS condiviso per tutto il sito
│   └── fonts/                        ← Inter self-hosted (opzionale)
├── perche/
│   └── scopo.html                    ← Placeholder
├── come/
│   ├── valori/
│   │   ├── index.html                ← Overview 5 valori
│   │   ├── rispetto.html
│   │   ├── coraggio.html
│   │   ├── umilta.html
│   │   ├── unione.html
│   │   └── ambizione.html
│   ├── metodologia/
│   │   └── index.html                ← Placeholder
│   └── modello-gioco/
│       ├── index.html                ← Modello di gioco (wrappa modello_di_gioco_slide)
│       ├── principi-fondamentali/
│       │   ├── index.html
│       │   ├── percezione.html
│       │   ├── partecipazione.html
│       │   ├── legame.html
│       │   ├── penetrazione.html
│       │   └── mobilita.html
│       ├── dimensioni.html
│       └── fasi/
│           ├── possesso.html         ← wrappa possesso_slide.html
│           ├── recupero.html         ← wrappa recupero_slide.html
│           └── transizioni.html      ← wrappa transizioni_slide.html
└── cosa/
    ├── modello-allenamento/
    │   ├── index.html
    │   ├── morfociclo.html           ← Placeholder
    │   ├── sessione.html             ← Placeholder
    │   └── compiti.html              ← wrappa tipologia_compiti_slide.html
    ├── framework-2sf.html            ← Placeholder
    ├── mezzi.html                    ← wrappa nomenclatura_guide.html
    └── sviluppo-individuale.html     ← Placeholder
```

---

## Design system CSS — specifiche

### Font
```css
/* Google Fonts import */
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');

:root {
  --font-primary: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
}
```

### Cromia base (neutro — default per qualsiasi club)
```css
:root {
  --color-black:      #0A0A0A;
  --color-text:       #0A0A0A;
  --color-text-muted: #666666;
  --color-text-faint: #999999;
  --color-border:     #E0E0E0;
  --color-border-mid: #CCCCCC;
  --color-bg:         #FFFFFF;
  --color-bg-subtle:  #F5F5F5;
  --color-bg-card:    #F0F0F0;

  /* Accento — variabile per club, default neutro */
  --color-accent:     #0A0A0A;
  --color-accent-alt: #555555;
}

/* Override Fiorentina */
[data-club="fiorentina"] {
  --color-accent:     #482e92;
  --color-accent-alt: #a29160;
}
```

### Tipografia
```css
:root {
  --text-xs:   10px;
  --text-sm:   12px;
  --text-base: 14px;
  --text-md:   16px;
  --text-lg:   20px;
  --text-xl:   28px;
  --text-2xl:  36px;

  --weight-light:   300;
  --weight-regular: 400;
  --weight-medium:  500;
  --weight-semibold:600;
  --weight-bold:    700;

  --leading-tight:  1.25;
  --leading-normal: 1.55;
  --leading-loose:  1.75;
}
```

### Spaziatura e layout
```css
:root {
  --margin-page-desktop: 80px;
  --margin-page-mobile:  22px;
  --gap-section:         48px;
  --gap-item:            16px;
  --radius-card:         6px;
  --border-main:         1.5px solid var(--color-black);
  --border-subtle:       0.5px solid var(--color-border);
  --border-bottom-bar:   3px solid var(--color-black);
}
```

### Componenti riutilizzabili da includere nel design system

**Nav breadcrumb** — presente in ogni pagina di livello 1 e 2
```
← [sezione padre] / [pagina corrente]
```

**Status badge** — indica lo stato del nodo
- `●` nero = prodotto
- `●` grigio = in aggiornamento
- `○` bianco/bordo = in costruzione

**Card nodo** — usata nel panel della homepage e nelle pagine indice
```
[status] Nome nodo          [tag sezione →]
```

**Separatore orizzontale** — `1.5px solid #0A0A0A`

**Bottom bar** — `3px solid #0A0A0A` in fondo ad ogni pagina

---

## Homepage — specifiche tecniche

### Layout
- Header globale fisso: titolo sistema + stagione
- Due entry point in cima (Contesto / Chi siamo) come barra orizzontale
- Corpo: grafico SVG a sinistra + panel reattivo a destra
- Footer: firma + versione

### Grafico SVG concentrico
Il grafico del prototipo è funzionante ma da migliorare:
- Tre anelli concentrici: Perché (centro pieno nero) / Come (anello medio) / Cosa (anello esterno)
- Anello tratteggiato esterno: Contesto (non cliccabile, solo visivo)
- Nodi posizionati sugli anelli Come e Cosa
- Ogni nodo: cerchio con label, stato visivo (pieno/grigio/outline)
- Comportamento click: aggiorna il panel a destra senza ricaricare la pagina
- Tooltip su hover con nome e descrizione breve
- Responsive: su mobile il grafico va sopra, il panel sotto

### Nodi da includere nel grafico

**Anello PERCHÉ (centro):**
- Scopo/Credo (cerchio centrale nero)

**Anello COME:**
- Valori (✅ prodotto)
- Metodologia (🔴 in costruzione)
- Modello di Gioco (🟡 in aggiornamento)

**Anello COSA:**
- Modello di Allenamento (🟡 parziale)
- Framework 2SF (🔴 in costruzione)
- Mezzi e Nomenclatura (✅ prodotto)
- Sviluppo Individuale (🔴 in costruzione)

---

## Template pagina Livello 1 — specifiche

Ogni pagina di livello 1 deve avere:

```html
<!-- HEADER GLOBALE -->
<header class="site-header">
  <a href="/">← Sistema</a>
  <span class="breadcrumb">Come / Modello di Gioco</span>
</header>

<!-- CONTENUTO -->
<main>
  <section class="page-intro">
    <!-- Titolo, sottotitolo, descrizione breve -->
  </section>

  <section class="page-content">
    <!-- Slide esistente integrata come iframe o contenuto diretto -->
    <!-- oppure lista di sotto-nodi con card -->
  </section>
</main>

<!-- FOOTER -->
<footer class="site-footer">
  <!-- navigazione verso sezioni correlate -->
</footer>
```

### Come integrare le slide esistenti
Le slide HTML esistenti (possesso_slide.html, recupero_slide.html, ecc.) vanno integrate come contenuto della pagina, NON come iframe. Il modo corretto è:

1. Copiare il contenuto visivo della slide dentro la pagina wrapper
2. Aggiungere header con breadcrumb e navigazione
3. Aggiungere footer con link a sezioni correlate

---

## Template pagina Placeholder — specifiche

Per i nodi 🔴 in costruzione, creare una pagina minima:

```html
<!-- stessa struttura header/footer -->
<main>
  <div class="placeholder-block">
    <div class="status-badge todo">In costruzione</div>
    <h1>Nome sezione</h1>
    <p>Contenuto in sviluppo.</p>
    <!-- link a sezioni correlate già prodotte -->
  </div>
</main>
```

---

## File già prodotti — da integrare nel sistema

| File | Destinazione nel sito | Stato |
|------|----------------------|-------|
| `fiorentina_contesto_mobile.html` | `/contesto/socio-culturale.html` | ✅ |
| `fiorentina_identita_guide.html` | `/come/valori/index.html` | ✅ |
| `modello_di_gioco_slide.html` | `/come/modello-gioco/index.html` | 🟡 |
| `possesso_slide.html` | `/come/modello-gioco/fasi/possesso.html` | ✅ |
| `recupero_slide.html` | `/come/modello-gioco/fasi/recupero.html` | ✅ |
| `transizioni_slide.html` | `/come/modello-gioco/fasi/transizioni.html` | ✅ |
| `tipologia_compiti_slide.html` | `/cosa/modello-allenamento/compiti.html` | ✅ |
| `nomenclatura_guide.html` | `/cosa/mezzi.html` | ✅ |
| `grosso_pattern_guide.html` | Non incluso nel sito — uso interno | — |

---

## Priorità di costruzione

**Fase 1 — struttura base (consegna minima)**
1. `design-system.css` completo
2. `index.html` homepage con SVG navigabile
3. Tutte le pagine wrapper per file già prodotti (8 pagine)
4. Pagine placeholder per nodi in costruzione

**Fase 2 — contenuto valori**
5. `/come/valori/index.html` con i 5 valori
6. Una pagina per ogni valore (5 pagine)

**Fase 3 — principi fondamentali**
7. `/come/modello-gioco/principi-fondamentali/` (6 pagine)
8. `/come/modello-gioco/dimensioni.html`

---

## Requisiti tecnici

- **Compatibilità:** Chrome, Safari, Firefox — ultimi 2 anni
- **Responsive:** breakpoint a 768px (mobile) e 1280px (desktop ottimale)
- **Standalone:** funziona aprendo index.html dal filesystem locale (no server)
- **Nessuna dipendenza:** Google Fonts è l'unica dipendenza esterna accettata
- **JavaScript:** solo per interazione SVG (click nodi → aggiorna panel) e tooltip. Nessun framework.
- **Performance:** nessuna immagine pesante, SVG inline, CSS minimale

---

## Note finali

- Il sistema è progettato per essere **portabile tra club**: l'unica variabile cromatica è `--color-accent`. Per applicare i colori Fiorentina aggiungere `data-club="fiorentina"` al tag `<html>`.
- Ogni pagina deve funzionare anche **standalone** (senza navigazione dal sito) perché alcune vengono condivise direttamente via link.
- Il sistema cresce per **aggiunta progressiva**: ogni nuovo nodo prodotto diventa una pagina. La struttura non va mai riscritta, solo estesa.

---

*Briefing versione 1.0 — Settembre 2026*
