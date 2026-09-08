# MtX Model — Sito

Sito statico navigabile del framework metodologico e identitario.
*ACF Fiorentina 2026/27 — Stefano Raponi*

## Come si apre

Nessun server richiesto. Doppio click su `index.html`.
(Se il browser blocca il caricamento delle slide da `file://`, servi la cartella
con un server statico qualsiasi, es. `python3 -m http.server` dentro `mtx-model/`.)

## Struttura

```
mtx-model/
├── index.html                  Homepage — mappa SVG concentrica navigabile
├── assets/
│   ├── css/design-system.css   Design system condiviso (tutti i token + componenti)
│   └── js/slide-fit.js          Scala le slide 1280×720 nei wrapper + fallback
├── assets/slides/              Copie locali delle slide già prodotte
├── perche/scopo.html
├── come/
│   ├── valori/                 index + 5 valori
│   ├── metodologia/            placeholder
│   └── modello-gioco/
│       ├── index.html          wrapper slide "Modello di Gioco"
│       ├── principi-fondamentali/  index + 5 principi
│       ├── dimensioni.html     placeholder
│       └── fasi/               possesso · recupero · transizioni (wrapper slide)
├── cosa/
│   ├── modello-allenamento/    index + morfociclo/sessione (placeholder) + compiti (wrapper)
│   ├── framework-2sf.html      placeholder
│   ├── mezzi.html              wrapper slide "Nomenclatura"
│   └── sviluppo-individuale.html  placeholder
└── contesto/
    ├── socio-culturale.html    wrapper guida contesto
    └── chi-siamo.html          placeholder
```

## Portabilità tra club

L'unica variabile cromatica è `--color-accent` in `assets/css/design-system.css`.
Il preset Fiorentina è già attivo via `<html data-club="fiorentina">`.
Per un altro club: cambiare il blocco `[data-club="..."]` o rimuovere l'attributo
per tornare al neutro bianco/nero.

## Stati dei nodi

- ● nero — prodotto (link attivo)
- ● grigio — in aggiornamento (link attivo, con nota)
- ○ bordo — in costruzione (placeholder)

## Slide sorgente da aggiungere

Queste pagine mostrano un fallback finché il file non è in `assets/slides/`:

| Pagina                          | File atteso                       |
|---------------------------------|-----------------------------------|
| `cosa/mezzi.html`               | `nomenclatura_guide.html`         |
| `contesto/socio-culturale.html` | `fiorentina_contesto_mobile.html` |

Le altre slide (`modello_di_gioco_slide.html`, `possesso_slide.html`,
`recupero_slide.html`, `transizioni_slide.html`, `tipologia_compiti_slide.html`)
sono già presenti.

## Rigenerare le pagine

Le pagine ripetitive sono generate da uno script Python (nessuna dipendenza).
Vedi `build_site.py` (fuori dalla cartella del sito). Rilanciarlo riscrive
placeholder, valori, principi e wrapper; `index.html` e il CSS sono a mano.
