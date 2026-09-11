/* ============================================================
   MtX Model — Menu di navigazione persistente
   Componente unico: iniettato con <script src="...assets/js/nav.js" defer></script>
   Un solo punto da aggiornare per aggiungere/abilitare una voce — MENU qui sotto.
   Il breadcrumb di ogni pagina resta invariato: questo menu è un livello
   aggiuntivo ("dove posso andare"), non sostituisce il breadcrumb ("dove sono").
   ============================================================ */
(function () {
  'use strict';

  var scriptEl = document.currentScript || (function () {
    var scripts = document.getElementsByTagName('script');
    return scripts[scripts.length - 1];
  })();

  // Risolve la root del sito dalla posizione dello script stesso — funziona
  // sia in locale (file://) sia su GitHub Pages (sotto-percorso /mtx-model/),
  // qualunque sia la profondità della pagina corrente.
  var BASE = scriptEl.src.replace(/assets\/js\/nav\.js(?:\?.*)?$/, '');

  var MENU = [
    { label: 'Identità', href: 'perche/scopo.html' },
    {
      label: 'Principi',
      items: [
        { label: 'Metodologia', href: 'come/metodologia/index.html' },
        { label: 'Modello di Gioco', href: 'come/modello-gioco/index.html' },
        {
          label: 'Organizzazione di Gioco',
          href: 'come/organizzazione-di-gioco/index.html',
          items: [
            { label: 'Possesso', href: 'come/organizzazione-di-gioco/possesso.html' },
            { label: 'Recupero', href: 'come/organizzazione-di-gioco/recupero.html' },
            { label: 'Transizioni', href: 'come/organizzazione-di-gioco/transizioni.html' }
          ]
        },
        { label: 'Modello di Allenamento', href: 'cosa/modello-allenamento/index.html' }
      ]
    },
    {
      label: 'Strumenti',
      items: [
        { label: 'Sviluppo Individuale', href: 'cosa/sviluppo-individuale.html' },
        { label: 'Mezzi Allenamento', href: 'cosa/mezzi.html' },
        { label: 'Framework 2SF', disabled: true },
        { label: 'Performance', disabled: true },
        { label: 'Analysis', disabled: true }
      ]
    },
    { label: 'Contesto', href: 'contesto/socio-culturale.html' },
    { label: 'Chi Siamo', href: 'contesto/chi-siamo.html' }
  ];

  function injectStyle() {
    if (document.getElementById('mtx-nav-style')) return;
    var style = document.createElement('style');
    style.id = 'mtx-nav-style';
    style.textContent = [
      '.mtx-nav { position: sticky; top: 0; z-index: 500; background: var(--color-bg, #fff); border-bottom: var(--border-main, 1.5px solid #0A0A0A); font-family: var(--font-primary, sans-serif); }',
      '.mtx-nav-bar { display: flex; align-items: center; gap: 20px; padding: 12px var(--margin-page-desktop, 80px); }',
      '.mtx-nav-brand { font-size: var(--text-sm, 12px); font-weight: var(--weight-bold, 700); letter-spacing: 0.08em; text-transform: uppercase; text-decoration: none; color: var(--color-black, #0A0A0A); white-space: nowrap; }',
      '.mtx-nav-brand:hover { color: var(--color-accent, #0A0A0A); }',
      '.mtx-nav-toggle { display: none; margin-left: auto; width: 30px; height: 26px; background: none; border: none; cursor: pointer; padding: 0; position: relative; }',
      '.mtx-nav-toggle-bars, .mtx-nav-toggle-bars::before, .mtx-nav-toggle-bars::after { content: ""; display: block; width: 22px; height: 1.5px; background: var(--color-black, #0A0A0A); position: absolute; left: 4px; transition: transform .2s ease, opacity .2s ease; }',
      '.mtx-nav-toggle-bars { top: 12px; }',
      '.mtx-nav-toggle-bars::before { top: -7px; }',
      '.mtx-nav-toggle-bars::after { top: 7px; }',
      '.mtx-nav.is-menu-open .mtx-nav-toggle-bars { background: transparent; }',
      '.mtx-nav.is-menu-open .mtx-nav-toggle-bars::before { top: 0; transform: rotate(45deg); }',
      '.mtx-nav.is-menu-open .mtx-nav-toggle-bars::after { top: 0; transform: rotate(-45deg); }',
      '.mtx-nav-list { list-style: none; display: flex; align-items: stretch; gap: 4px; margin: 0; padding: 0; }',
      '.mtx-nav-item { position: relative; }',
      '.mtx-nav-row { display: flex; align-items: center; }',
      '.mtx-nav-label { font-size: var(--text-sm, 12px); font-weight: var(--weight-semibold, 600); color: var(--color-text-muted, #666); text-decoration: none; padding: 8px 6px; background: none; border: none; font-family: inherit; cursor: pointer; white-space: nowrap; }',
      'a.mtx-nav-label:hover, button.mtx-nav-label-btn:hover { color: var(--color-black, #0A0A0A); }',
      '.mtx-nav-item.is-open > .mtx-nav-row .mtx-nav-label { color: var(--color-black, #0A0A0A); }',
      '.mtx-nav-label-disabled { font-size: var(--text-sm, 12px); font-weight: var(--weight-semibold, 600); color: var(--color-border-mid, #CCC); padding: 8px 6px; white-space: nowrap; cursor: default; }',
      '.mtx-nav-caret-btn { display: inline-flex; background: none; border: none; padding: 8px 4px; color: var(--color-text-faint, #999); font-size: 11px; }',
      '.mtx-nav-row-toggle { cursor: pointer; }',
      '.mtx-nav-row-toggle .mtx-nav-caret-btn { cursor: pointer; }',
      '.mtx-nav-caret-spacer { visibility: hidden; cursor: default; }',
      '.mtx-nav-caret { display: inline-block; transition: transform .2s ease; }',
      '.mtx-nav-item.is-open > .mtx-nav-row .mtx-nav-caret { transform: rotate(180deg); }',
      '.mtx-nav-panel { display: grid; grid-template-rows: 0fr; transition: grid-template-rows .25s ease; }',
      '.mtx-nav-item.is-open > .mtx-nav-panel { grid-template-rows: 1fr; }',
      '.mtx-nav-panel-inner { overflow: hidden; min-height: 0; }',
      '.mtx-nav-sub { list-style: none; margin: 0; padding: 0; }',
      '.mtx-nav-sub .mtx-nav-row { padding-left: 0; }',
      '.mtx-nav-sub .mtx-nav-sub { border-left: 2px solid var(--color-border, #E0E0E0); padding-left: 12px; margin-left: 10px; }',
      /* Desktop: dropdown flottante a livello 0, accordion in-flow sotto */
      '@media (min-width: 901px) {',
      '  .mtx-nav-list > .mtx-nav-item > .mtx-nav-panel { position: absolute; top: 100%; left: 0; min-width: 230px; background: var(--color-bg, #fff); border: var(--border-subtle, 0.5px solid #E0E0E0); border-top: none; box-shadow: 0 10px 24px rgba(0,0,0,0.08); grid-template-rows: 0fr; }',
      '  .mtx-nav-list > .mtx-nav-item.is-open > .mtx-nav-panel { grid-template-rows: 1fr; }',
      '  .mtx-nav-sub > .mtx-nav-item { padding: 2px 14px; }',
      '  .mtx-nav-sub > .mtx-nav-item > .mtx-nav-row .mtx-nav-label,',
      '  .mtx-nav-sub > .mtx-nav-item > .mtx-nav-row .mtx-nav-label-disabled { display: block; padding: 8px 2px; white-space: normal; }',
      '}',
      /* Mobile: tendina a comparsa, tutto in-flow */
      '@media (max-width: 900px) {',
      '  .mtx-nav-bar { padding: 14px var(--margin-page-mobile, 22px); flex-wrap: wrap; }',
      '  .mtx-nav-toggle { display: block; }',
      '  .mtx-nav-list { display: none; flex-direction: column; width: 100%; order: 3; margin-top: 10px; gap: 0; }',
      '  .mtx-nav.is-menu-open .mtx-nav-list { display: flex; }',
      '  .mtx-nav-item { border-top: var(--border-subtle, 0.5px solid #E0E0E0); }',
      '  .mtx-nav-row { justify-content: space-between; }',
      '  .mtx-nav-label, .mtx-nav-label-disabled { padding: 12px 4px; flex: 1; }',
      '  .mtx-nav-sub > .mtx-nav-item { padding-left: 14px; }',
      '}'
    ].join('\n');
    document.head.appendChild(style);
  }

  function closeSiblings(li) {
    var parentList = li.parentElement;
    Array.prototype.forEach.call(parentList.children, function (sib) {
      if (sib === li) return;
      sib.classList.remove('is-open');
      var sibCaret = sib.querySelector(':scope > .mtx-nav-row > .mtx-nav-caret-btn');
      if (sibCaret && sibCaret.tagName === 'BUTTON') sibCaret.setAttribute('aria-expanded', 'false');
    });
  }

  function closeAll(root) {
    root.querySelectorAll('.mtx-nav-item.is-open').forEach(function (li) {
      li.classList.remove('is-open');
      var caret = li.querySelector(':scope > .mtx-nav-row > .mtx-nav-caret-btn');
      if (caret && caret.tagName === 'BUTTON') caret.setAttribute('aria-expanded', 'false');
    });
  }

  function renderItem(item, depth) {
    var li = document.createElement('li');
    li.className = 'mtx-nav-item';

    var row = document.createElement('div');
    row.className = 'mtx-nav-row';
    li.appendChild(row);

    var hasChildren = item.items && item.items.length > 0;

    if (item.disabled) {
      var span = document.createElement('span');
      span.className = 'mtx-nav-label-disabled';
      span.textContent = item.label;
      span.setAttribute('aria-disabled', 'true');
      row.appendChild(span);
    } else if (item.href) {
      var a = document.createElement('a');
      a.className = 'mtx-nav-label';
      a.href = BASE + item.href;
      a.textContent = item.label;
      row.appendChild(a);
    } else {
      var b = document.createElement('button');
      b.type = 'button';
      b.className = 'mtx-nav-label mtx-nav-label-btn';
      b.textContent = item.label;
      row.appendChild(b);
    }

    // Slot per la freccia — riservato su ogni voce, anche quando vuoto
    // (nessun sottomenu), così le voci senza dropdown restano allineate
    // con quelle che ce l'hanno.
    if (hasChildren) {
      var caretBtn = document.createElement('button');
      caretBtn.type = 'button';
      caretBtn.className = 'mtx-nav-caret-btn';
      caretBtn.setAttribute('aria-expanded', 'false');
      caretBtn.setAttribute('aria-label', 'Espandi ' + item.label);
      caretBtn.innerHTML = '<span class="mtx-nav-caret" aria-hidden="true">⌄</span>';
      row.appendChild(caretBtn);
      row.classList.add('mtx-nav-row-toggle');

      var panel = document.createElement('div');
      panel.className = 'mtx-nav-panel';
      var inner = document.createElement('div');
      inner.className = 'mtx-nav-panel-inner';
      var sub = document.createElement('ul');
      sub.className = 'mtx-nav-sub';
      item.items.forEach(function (child) {
        sub.appendChild(renderItem(child, depth + 1));
      });
      inner.appendChild(sub);
      panel.appendChild(inner);
      li.appendChild(panel);

      var toggle = function (evt) {
        evt.stopPropagation();
        var willOpen = !li.classList.contains('is-open');
        closeSiblings(li);
        li.classList.toggle('is-open', willOpen);
        caretBtn.setAttribute('aria-expanded', String(willOpen));
      };
      caretBtn.addEventListener('click', toggle);
      var labelBtn = row.querySelector('.mtx-nav-label-btn');
      if (labelBtn) labelBtn.addEventListener('click', toggle);
      // Il target di tocco copre l'intera riga, non solo la freccia: un
      // click sullo spazio vuoto tra etichetta e freccia apre/chiude
      // comunque (i listener su etichetta/freccia fermano la propagazione,
      // quindi qui arrivano solo i click "a vuoto", senza doppio toggle).
      row.addEventListener('click', toggle);
    } else {
      var spacer = document.createElement('span');
      spacer.className = 'mtx-nav-caret-btn mtx-nav-caret-spacer';
      spacer.setAttribute('aria-hidden', 'true');
      spacer.innerHTML = '<span class="mtx-nav-caret" aria-hidden="true">⌄</span>';
      row.appendChild(spacer);
    }

    return li;
  }

  function buildNav() {
    var nav = document.createElement('nav');
    nav.className = 'mtx-nav';
    nav.setAttribute('aria-label', 'Navigazione principale');

    var bar = document.createElement('div');
    bar.className = 'mtx-nav-bar';

    var brand = document.createElement('a');
    brand.className = 'mtx-nav-brand';
    brand.href = BASE + 'index.html';
    brand.textContent = 'MtX Model';
    bar.appendChild(brand);

    var toggle = document.createElement('button');
    toggle.type = 'button';
    toggle.className = 'mtx-nav-toggle';
    toggle.setAttribute('aria-expanded', 'false');
    toggle.setAttribute('aria-controls', 'mtxNavList');
    toggle.setAttribute('aria-label', 'Apri il menu di navigazione');
    toggle.innerHTML = '<span class="mtx-nav-toggle-bars" aria-hidden="true"></span>';
    bar.appendChild(toggle);

    var list = document.createElement('ul');
    list.className = 'mtx-nav-list';
    list.id = 'mtxNavList';
    MENU.forEach(function (item) {
      list.appendChild(renderItem(item, 0));
    });
    bar.appendChild(list);

    nav.appendChild(bar);

    toggle.addEventListener('click', function () {
      var willOpen = !nav.classList.contains('is-menu-open');
      nav.classList.toggle('is-menu-open', willOpen);
      toggle.setAttribute('aria-expanded', String(willOpen));
      if (!willOpen) closeAll(nav);
    });

    document.addEventListener('click', function (evt) {
      if (!nav.contains(evt.target)) {
        closeAll(nav);
        nav.classList.remove('is-menu-open');
        toggle.setAttribute('aria-expanded', 'false');
      }
    });
    document.addEventListener('keydown', function (evt) {
      if (evt.key === 'Escape') {
        closeAll(nav);
        nav.classList.remove('is-menu-open');
        toggle.setAttribute('aria-expanded', 'false');
      }
    });

    return nav;
  }

  function mount() {
    injectStyle();
    var nav = buildNav();
    document.body.insertBefore(nav, document.body.firstChild);
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', mount);
  } else {
    mount();
  }
})();
