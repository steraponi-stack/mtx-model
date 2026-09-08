/* slide-fit.js — MtX Model
   1) scala le slide 1280×720 (o dimensioni custom) dentro il wrapper
   2) mostra un fallback se la slide non è raggiungibile (404 / vuota)
   Nessuna dipendenza. Si auto-inizializza. */
(function () {
  function fit(box) {
    var iframe = box.querySelector('iframe');
    if (!iframe) return;
    var sw = parseFloat(getComputedStyle(box).getPropertyValue('--slide-w')) || 1280;
    var scale = box.clientWidth / sw;
    iframe.style.transform = 'scale(' + scale + ')';
  }
  function fitAll() { document.querySelectorAll('.slide-embed').forEach(fit); }

  window.mtxSlideCheck = function (iframe) {
    var box = iframe.closest('.slide-embed');
    var fallback = box && box.querySelector('.slide-missing');
    var broken = false;
    try {
      var d = iframe.contentDocument;
      if (!d) {
        broken = false; // cross-origin: presumiamo ok
      } else {
        var t = (d.body ? d.body.innerText : '').trim();
        var title = (d.title || '').toLowerCase();
        if (!t ||
            title.indexOf('error') !== -1 ||
            /error code:\s*404|not found|http\s*404/i.test(t.slice(0, 400))) {
          broken = true;
        }
      }
    } catch (e) { broken = false; }
    if (broken && fallback) {
      iframe.style.display = 'none';
      fallback.style.display = 'flex';
    } else {
      fit(box);
    }
  };

  window.addEventListener('resize', fitAll);
  window.addEventListener('load', fitAll);
  document.addEventListener('DOMContentLoaded', fitAll);
  fitAll();
})();
