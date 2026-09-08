# Architettura del Sistema — "MtX Model"
### Documento di riferimento per Claude Code e Claude Design
*ACF Fiorentina 2026/27 — Stefano Raponi*

---

## 1. Visione del sistema

Un ipertesto navigabile che rappresenta l'intero framework metodologico e identitario del gruppo di lavoro. Struttura concentrica: dal generale al particolare, dal Perché al Cosa. Ogni nodo è una pagina o sezione con il proprio contenuto e grafico dedicato. Il sistema serve due target: **staff tecnico** (uso quotidiano, profondità metodologica) e **dirigenti** (visione d'insieme, linguaggio accessibile).

**Principio di navigazione:** si entra dalla mappa generale e si scende per livelli. Ogni livello ha il proprio grafico sintetico che introduce il contenuto del livello successivo.

---

## 2. Struttura dei livelli

```
LIVELLO -1 (cornice esterna)
├── Contesto Socio-Culturale
└── Chi Siamo: Staff, Organigramma, Compiti

LIVELLO 0 (homepage — mappa navigabile)
└── Grafico concentrico Perché / Come / Cosa
    con anello esterno = Contesto

LIVELLO 1 (rami principali)
├── PERCHÉ
│   └── Scopo / Credo / Visione del Mister
├── COME
│   ├── Valori
│   ├── Metodologia
│   └── Modello di Gioco
│       ├── Principi fondamentali (5P + 4 Dimensioni)
│       └── Principi specifici
│           ├── Possesso
│           ├── Recupero
│           └── Transizioni
└── COSA
    └── Pratiche
        ├── Modello di Allenamento (Morfociclo · Sessione · Compiti)
        ├── Framework 2SF
        ├── Mezzi di Allenamento
        └── Sviluppo Sistemico Individuale

LIVELLO 2 (approfondimenti per nodo)
└── [vedi sezione 4]
```

---

## 3. Nodi — specifiche complete

---

### CORNICE ESTERNA

#### C1 — Contesto Socio-Culturale
**Posizione:** anello esterno al grafico, entry point separato nella homepage
**Contenuto:** Firenze e la Fiorentina — storia, identità della città, cultura calcistica, tifoseria, centenario (1926-2026), contesto societario (Commisso, Paratici, Goretti)
**Formato:** pagina narrativa con immagini, nessun grafico tecnico
**File esistente:** `fiorentina_contesto_mobile.html` ✅ prodotto
**Stato:** ✅ prodotto · da aggiornare periodicamente
**Target:** entrambi
**Connessioni:** → homepage

#### C2 — Chi Siamo
**Posizione:** anello esterno al grafico, entry point separato nella homepage
**Contenuto:** organigramma staff, ruoli e compiti di ciascuno, struttura T-shaped (Raponi / Vaccariello), aree di coordinamento (Tecnica, Analisi, Fisica/Performance, Portieri)
**Formato:** pagina con schema grafico organigramma + schede ruolo
**File esistente:** nessuno
**Stato:** 🔴 da costruire
**Target:** entrambi (versione dirigenti più sintetica)
**Connessioni:** → homepage

---

### LIVELLO 0 — Homepage

#### L0 — Mappa navigabile (homepage)
**Contenuto:** grafico concentrico SVG interattivo con tre anelli (Perché / Come / Cosa) + anello esterno (Contesto). Ogni nodo è cliccabile e apre il livello 1 corrispondente. Nodi con contenuto già prodotto evidenziati diversamente da quelli in costruzione.
**Formato:** SVG interattivo su sfondo bianco, Inter font, colori neutri con un accento (intercambiabile per club)
**Stato:** 🔴 da costruire — è la priorità assoluta
**Target:** entrambi
**Note per Claude Code:** navigazione client-side, nessun server richiesto, file HTML standalone o con routing semplice
**Note per Claude Design:** il grafico concentrico è l'elemento visivo centrale del sistema — deve essere elegante, leggibile su desktop e mobile, e coerente con il design system già stabilito (Inter, cromia neutra B&N con un accento)

---

### LIVELLO 1A — PERCHÉ

#### P1 — Scopo / Credo / Visione del Mister
**Posizione:** nodo radice del ramo Perché
**Contenuto:**
- La frase centrale: *"Saremo capaci di vincere se riusciremo ad essere forti quando saremo deboli"* — Fabio Grosso
- Spiegazione del Perché come bussola identitaria
- Contesto: perché questo Perché, cosa significa in pratica per il gruppo
**Formato:** pagina narrativa con la frase in grande, testo di contesto, nessun grafico tecnico
**File esistente:** contenuto dentro `fiorentina_identita_guide.html` (tab Perché) ✅
**Stato:** 🟡 parzialmente prodotto · da estrarre e formattare come pagina autonoma
**Target:** entrambi
**Connessioni:** → L1A valori, → L1B metodologia

---

### LIVELLO 1B — COME

#### V0 — Valori (nodo radice)
**Contenuto:** i 5 valori con grafico introduttivo (il pentagono/cerchio dei valori già prodotto)
**Formato:** grafico + lista valori cliccabili
**File esistente:** `fiorentina_identita_guide.html` ✅
**Stato:** 🟡 da aggiornare con Rispetto/Coraggio nuovi
**Target:** entrambi
**Connessioni:** → V1 Rispetto, → V2 Coraggio, → V3 Umiltà, → V4 Unione, → V5 Ambizione

#### V1 — Rispetto
**Claim:** *"Più di ogni regola."*
**Descrizione:** Rispettare persone e cose significa riconoscere l'importanza di ogni relazione e saper vedere nell'altro la sua unicità e il suo potenziale.
**Stato:** 🟡 testo definito · pagina da costruire
**Target:** entrambi

#### V2 — Coraggio
**Claim:** *"Affronta ogni momento. Fino in fondo."*
**Descrizione:** Affrontare pienamente ogni momento e senza paura di sbagliare. Il coraggio è la condizione dell'eccellenza.
**Stato:** 🟡 testo definito · pagina da costruire
**Target:** entrambi

#### V3 — Umiltà
**Claim:** *"A testa alta, ma con i piedi per terra."*
**Descrizione:** Ogni corsa in più è un tributo a chi ci sostiene. Incarnare con generosità totale il nostro spirito e lo spirito di questa città.
**Stato:** 🟡 testo definito · pagina da costruire
**Target:** entrambi

#### V4 — Unione
**Claim:** *"Gioca per il compagno."*
**Descrizione:** Il NOI prevale sempre sull'IO. L'unicità ha senso solo al servizio della squadra. È dall'interazione dei singoli che emerge la forza del collettivo.
**Stato:** 🟡 testo definito · pagina da costruire
**Target:** entrambi

#### V5 — Ambizione
**Claim:** *"Punta in alto. Ogni giorno è una nuova sfida."*
**Descrizione:** Non accontentarsi mai di quello che si era ieri. Affrontare da protagonisti sfide sempre nuove.
**Stato:** 🟡 testo definito · pagina da costruire
**Target:** entrambi

#### M0 — Metodologia (nodo radice)
**Contenuto:** introduzione al modello ecologico come fondamento metodologico — perché questa scelta, cosa implica, come orienta tutto il lavoro
**Formato:** pagina narrativa + grafico introduttivo dell'ecosistema calcio
**File esistente:** *MtX Model* (PDF in project knowledge)
**Stato:** 🔴 da costruire
**Target:** staff principalmente, versione semplificata per dirigenti
**Connessioni:** → M1 Modello Ecologico, → M2 Principi Metodologici

#### M1 — Modello Ecologico
**Sotto-nodi:**
- Il calcio come ecosistema
- Cognizione e apprendimento (affordance, percezione-azione, cognizione incarnata)
- CLA e auto-organizzazione (Constraints-Led Approach, vincoli, emergenza)
**Stato:** 🔴 da costruire · base in *MtX Model*
**Target:** staff

#### M2 — Principi Metodologici
**Contenuto:** come il modello ecologico si traduce in scelte pratiche di allenamento — design dei vincoli, manipolazione dell'ambiente, feedback implicito vs esplicito
**Stato:** 🔴 da costruire
**Target:** staff

---

### LIVELLO 1C — COME / Modello di Gioco

#### G0 — Modello di Gioco (nodo radice)
**Contenuto:** il grafico concentrico del modello (cerchio con principi e dimensioni), intenzione di gioco, ciclo del gioco
**Frase al centro:** *"Conoscere, riconoscere, risolvere insieme"* — con Percezione-Azione
**Intenzione di gioco:** "Avere la palla per giocare in modo propositivo ed essere protagonisti"
**Formato:** slide/pagina con grafico + testo esplicativo
**File esistente:** `modello_di_gioco_slide.html` ✅ (da aggiornare con nuova frase centrale)
**Stato:** 🟡 prodotto · da aggiornare
**Target:** entrambi
**Connessioni:** → G1 Principi fondamentali, → G2 4 Dimensioni, → G3 Principi specifici, → G4 Fasi di gioco

#### G1 — I 5 Principi Fondamentali
**Contenuto:** Percezione, Partecipazione, Legame, Penetrazione, Mobilità — definizione e relazioni tra loro
**Formato:** pagina con grafico dei 5 principi + descrizioni
**Stato:** 🟡 contenuto prodotto in slide · da espandere in pagina con approfondimento
**Target:** staff principalmente
**Connessioni:** → G1a Percezione, → G1b Partecipazione, → G1c Legame, → G1d Penetrazione, → G1e Mobilità

#### G1a-e — I 5 Principi (pagine individuali)
**Contenuto per ciascuno:** definizione ecologica, come si manifesta in campo, come si allena, indicatori di osservazione, esempi situazionali
**Stato:** 🔴 da costruire
**Target:** staff

#### G2 — Le 4 Dimensioni
**Contenuto:** Intensità, Ritmo, Continuità, Adattabilità — cosa significano in campo, come si misurano, come si allena ciascuna
**Stato:** 🔴 da costruire
**Target:** staff

#### G3 — Principi Specifici Possesso/Recupero
**Contenuto:** Superiorità/Vantaggio (numerica, posizionale, qualitativa, relazionale), Organizzazione S/T — SIDF (Occupazione, Funzioni, Interazioni), Progressione nelle fasi
**Formato:** pagina con tabella/grafico comparativo possesso/recupero
**File esistente:** `possesso_slide.html` ✅, `recupero_slide.html` ✅
**Stato:** 🟡 slide prodotte · da integrare in pagina navigabile con approfondimento
**Target:** staff
**Connessioni:** → G4 Fasi di gioco

#### G4 — Fasi di Gioco
**Contenuto introduttivo:** il gioco presenta due condizioni che si rincorrono — Possesso (abbiamo la palla) e Recupero (dobbiamo riprenderla). Dentro questi momenti si distinguono le fasi.
**Connessioni:** → G4a Possesso, → G4b Recupero, → G4c Transizioni

#### G4a — Possesso
**Sotto-fasi:** Costruzione, Sviluppo, Finalizzazione
**Principi specifici:** Attacco organizzato — mantenimento per penetrare
**File esistente:** `possesso_slide.html` ✅
**Stato:** ✅ prodotto come slide · da integrare

#### G4b — Recupero
**Sotto-fasi:** Pressing (blocco alto), Contenimento (blocco medio), Protezione (blocco basso)
**Principi specifici:** Difesa organizzata — pressione e compattezza
**File esistente:** `recupero_slide.html` ✅
**Stato:** ✅ prodotto come slide · da integrare

#### G4c — Transizioni
**Tipo:** Transizione Offensiva (T+) e Transizione Difensiva (T-)
**File esistente:** `transizioni_slide.html` ✅
**Stato:** ✅ prodotto come slide · da integrare

---

### LIVELLO 1D — COSA / Pratiche

> **Nota architetturale:** i Principi di gioco (fondamentali e specifici) appartengono al COME — sono la visione di come si gioca il calcio. Le Pratiche appartengono al COSA — sono gli strumenti operativi con cui si realizza quella visione in campo e in allenamento.

#### A0 — Modello di Allenamento (nodo radice)
**Contenuto:** come il modello di gioco si traduce in allenamento — il morfociclo, la sessione, i compiti
**Formato:** pagina introduttiva con grafico struttura
**Stato:** 🔴 da costruire
**Connessioni:** → A1 Morfociclo, → A2 Sessione, → A3 Compiti

#### A1 — Morfociclo
**Contenuto:** struttura della settimana tipo, principi di periodizzazione, distribuzione dei carichi per fase
**Sotto-nodi:** Progettazione (come si costruisce), Tipologie di settimana
**Stato:** 🔴 da costruire

#### A2 — Sessione
**Contenuto:** struttura della sessione tipo (introduttivi → ottimizzazione → completamento), logica di costruzione
**Sotto-nodi:** Struttura, Principi di costruzione
**Stato:** 🔴 da costruire

#### A3 — Tipologia Compiti e Nomenclatura
**Contenuto:** tutte le tipologie di compiti con claim, descrizione, forme di gioco
**File esistente:** `tipologia_compiti_slide.html` ✅, `nomenclatura_guide.html` ✅
**Stato:** ✅ prodotto · da integrare come pagina navigabile
**Connessioni:** → nomenclatura dettagliata

#### B0 — Framework 2SF
**Contenuto:** Sfida / Struttura / Focus / Feedback — il framework per la progettazione dei mezzi di allenamento
**Formato:** pagina con grafico 2SF + spiegazione applicata
**Stato:** 🔴 da costruire · base in *MtX Model*
**Target:** staff

#### C0 — Mezzi di Allenamento
**Contenuto:** catalogo completo dei mezzi con nomenclatura, strutture tipo, esempi
**File esistente:** `nomenclatura_guide.html` ✅
**Stato:** 🟡 nomenclatura prodotta · da espandere con esempi e schede
**Target:** staff

#### D0 — Sviluppo Sistemico Individuale
**Contenuto:** framework di lettura integrata del singolo calciatore (tecnica, tattica, fisica, mentale, emotiva, bio-energetica)
**Stato:** 🔴 da costruire — Fase 1 solo interna, Fase 2 con Vaccariello
**Target:** solo staff tecnico

---

## 4. Mappa degli stati

*Nota: Valori, Metodologia e Modello di Gioco (inclusi tutti i principi) sono nel COME. Le Pratiche sono nel COSA.*


| Nodo | Stato | File esistente |
|------|-------|---------------|
| L0 Homepage | 🔴 da costruire | — |
| C1 Contesto socio-culturale | ✅ prodotto | fiorentina_contesto_mobile.html |
| C2 Chi siamo | 🔴 da costruire | — |
| P1 Scopo/Credo | 🟡 parziale | fiorentina_identita_guide.html |
| V0-V5 Valori | 🟡 parziale | fiorentina_identita_guide.html |
| M0-M2 Metodologia | 🔴 da costruire | PDF Verso un'Ecologia |
| G0 Modello di Gioco | 🟡 da aggiornare | modello_di_gioco_slide.html |
| G1 5 Principi | 🟡 parziale | dentro modello_di_gioco_slide |
| G1a-e Principi individuali | 🔴 da costruire | — |
| G2 4 Dimensioni | 🔴 da costruire | — |
| G3 Principi Specifici | 🟡 parziale | possesso_slide + recupero_slide |
| G4a Possesso | ✅ prodotto | possesso_slide.html |
| G4b Recupero | ✅ prodotto | recupero_slide.html |
| G4c Transizioni | ✅ prodotto | transizioni_slide.html |
| A0-A2 Modello Allenamento | 🔴 da costruire | — |
| A3 Tipologia Compiti | ✅ prodotto | tipologia_compiti_slide.html |
| B0 Framework 2SF | 🔴 da costruire | PDF Verso un'Ecologia |
| C0 Mezzi/Nomenclatura | ✅ prodotto | nomenclatura_guide.html |
| D0 Sviluppo Individuale | 🔴 da costruire | — |

**Legenda:** ✅ prodotto · 🟡 parziale/da aggiornare · 🔴 da costruire

---

## 5. Design System

### Tipografia
- Font: **Inter** (tutti i pesi)
- Titoli: 700, nero `#0A0A0A`
- Corpo: 300-400, grigio scuro `#333`
- Claim valori/principi: 600, italic

### Cromia base (neutro)
- Sfondo: `#FFFFFF`
- Testo: `#0A0A0A`
- Grigio testo secondario: `#666`
- Grigio bordi: `#E0E0E0`
- Grigio sfondo card: `#F5F5F5`
- **Accento (variabile per club):** `#0A0A0A` default neutro

### Accento Fiorentina (quando applicato)
- Viola: `#482e92`
- Oro: `#a29160`

### Griglia e margini
- Margini pagina: 80px desktop, 22px mobile
- Separatore principale: linea 1.5px `#0A0A0A`
- Bottom bar slide: 3px `#0A0A0A`

### Componenti già definiti
- Tab navigation (radio buttons, CSS only)
- Card con header nero e badge numerati
- Tabella nomenclatura (3 colonne: descrizione / sigla / breve)
- Grafico concentrico (SVG, da costruire interattivo)
- Slide 16:9 1280×720

---

## 6. Architettura file suggerita

```
/sistema-mtx-model/
├── index.html                    ← Homepage con mappa navigabile
├── assets/
│   ├── css/
│   │   └── design-system.css     ← Design system condiviso
│   ├── fonts/                    ← Inter self-hosted
│   └── svg/
│       └── mappa-concentrica.svg ← Grafico principale
├── perche/
│   └── scopo.html
├── come/
│   ├── valori/
│   │   ├── index.html            ← Overview valori
│   │   ├── rispetto.html
│   │   ├── coraggio.html
│   │   ├── umilta.html
│   │   ├── unione.html
│   │   └── ambizione.html
│   └── metodologia/
│       ├── index.html
│       ├── modello-ecologico.html
│       └── principi-metodologici.html
├── cosa/
│   ├── principi/
│   │   ├── modello-gioco.html
│   │   ├── principi-fondamentali/
│   │   │   ├── percezione.html
│   │   │   ├── partecipazione.html
│   │   │   ├── legame.html
│   │   │   ├── penetrazione.html
│   │   │   └── mobilita.html
│   │   ├── dimensioni.html
│   │   ├── principi-specifici.html
│   │   └── fasi/
│   │       ├── possesso.html
│   │       ├── recupero.html
│   │       └── transizioni.html
│   └── pratiche/
│       ├── modello-allenamento/
│       │   ├── morfociclo.html
│       │   ├── sessione.html
│       │   └── compiti.html
│       ├── framework-2sf.html
│       ├── mezzi.html
│       └── sviluppo-individuale.html
└── contesto/
    ├── socio-culturale.html
    └── chi-siamo.html
```

---

## 7. Briefing per Claude Code

**Obiettivo:** sito HTML statico, nessun server richiesto, funziona come cartella locale o su hosting semplice.

**Requisiti tecnici:**
- HTML5 puro, CSS3, JavaScript minimale (solo per SVG interattivo)
- Navigazione client-side senza framework (no React, no Vue)
- Responsive: desktop 1280px e mobile 375px
- Font Inter caricato da Google Fonts o self-hosted
- Nessuna dipendenza da CDN per il funzionamento base

**Priorità di costruzione:**
1. Design system CSS condiviso
2. Homepage con mappa SVG navigabile (placeholder per nodi non ancora prodotti)
3. Pagine esistenti integrate nella struttura (possesso, recupero, transizioni, compiti, nomenclatura)
4. Pagine valori (contenuto già disponibile)
5. Pagine principi fondamentali (da scrivere)

**Comportamento nodi:**
- Nodi ✅ → link attivo, apre la pagina
- Nodi 🟡 → link attivo, apre pagina con nota "in aggiornamento"
- Nodi 🔴 → visibili ma non cliccabili, con indicatore "in costruzione"

---

## 8. Briefing per Claude Design

**Obiettivo:** visual system coerente per homepage e tutte le pagine del sito.

**Elementi da progettare:**
1. **Grafico concentrico SVG** — tre anelli (Perché/Come/Cosa) + anello esterno (Contesto). Ogni nodo ha stato visivo (attivo/parziale/in costruzione). Deve funzionare su desktop e mobile.
2. **Homepage layout** — mappa centrale, due entry point (Contesto / Chi siamo) in alto, navigazione essenziale
3. **Template pagina Livello 1** — header con breadcrumb, grafico introduttivo, contenuto, navigazione verso livello 2
4. **Template pagina Livello 2** — testo + eventuali grafici specifici, navigazione verso livello 1 e verso nodi correlati
5. **Componenti condivisi** — header globale, footer, indicatori di stato nodo

**Riferimento design system:** documento `Sistema_Design_MtX_Model.md` già prodotto.

**Vincolo principale:** il sistema deve funzionare in bianco/nero/grigio di default, con un unico colore di accento intercambiabile per club. Priorità a leggibilità e navigabilità rispetto all'estetica.

---

## 9. Prossimi passi immediati

1. **Approvazione di questa architettura** — conferma struttura, correzioni, nodi mancanti
2. **Prototipo homepage** — grafico concentrico cliccabile con stati visivi, costruibile in questa sessione
3. **Aggiornamento fiorentina_identita_guide.html** — nuovi valori (Rispetto/Coraggio aggiornati)
4. **Briefing finale Claude Code** — documento tecnico derivato da questo
5. **Prima sessione Claude Design** — partendo dal design system già definito

---

*Documento versione 1.0 — settembre 2026*
*Da aggiornare progressivamente con ogni nuovo nodo prodotto*
