// Eullie Portfolio — Main JS
// Nav toggle, portfolio filters, lightbox, etc.

document.addEventListener('DOMContentLoaded', () => {
  initNavToggle();
  initPortfolioFilters();
  initLightbox();
  initRipples();
});

// Tactile click/tap feedback on solid buttons, filter pills, and
// portfolio tiles. Skipped entirely under reduced motion, and skipped
// for keyboard activation (no pointer coordinate, no visual to anchor).
const RIPPLE_SELECTOR = '.btn-primary, .btn-primary-inverse, .portfolio-filters button, .portfolio-item, .lightbox-close, .nav-toggle';

function createRipple(x, y, el) {
  const rect = el.getBoundingClientRect();
  const size = Math.max(rect.width, rect.height) * 2;
  const span = document.createElement('span');
  span.className = 'ripple';
  span.style.width = `${size}px`;
  span.style.height = `${size}px`;
  span.style.left = `${x - rect.left - size / 2}px`;
  span.style.top = `${y - rect.top - size / 2}px`;
  el.appendChild(span);
  span.addEventListener('animationend', () => span.remove());
}

function attachRipple(el) {
  el.classList.add('ripple-surface');
  el.addEventListener('pointerdown', (e) => {
    if (e.pointerType === 'mouse' && e.button !== 0) return;
    createRipple(e.clientX, e.clientY, el);
  });
}

function initRipples() {
  if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) return;
  document.querySelectorAll(RIPPLE_SELECTOR).forEach(attachRipple);
}

function initNavToggle() {
  const toggle = document.querySelector('.nav-toggle');
  const collapse = document.querySelector('.nav-collapse');
  if (!toggle || !collapse) return;

  toggle.addEventListener('click', () => {
    const isOpen = collapse.classList.toggle('open');
    toggle.setAttribute('aria-expanded', String(isOpen));
  });
}

function initPortfolioFilters() {
  const filterButtons = document.querySelectorAll('[data-filter]');
  const items = document.querySelectorAll('[data-category]');
  if (!filterButtons.length || !items.length) return;

  function setItemVisible(item, visible) {
    if (visible) {
      item.hidden = false;
      requestAnimationFrame(() => {
        requestAnimationFrame(() => item.classList.remove('is-hidden'));
      });
    } else {
      item.classList.add('is-hidden');
      window.setTimeout(() => {
        item.hidden = true;
      }, 350);
    }
  }

  filterButtons.forEach((button) => {
    button.addEventListener('click', () => {
      const filter = button.dataset.filter;

      items.forEach((item) => {
        const show = filter === 'all' || item.dataset.category === filter;
        setItemVisible(item, show);
      });

      filterButtons.forEach((b) => b.classList.remove('active'));
      button.classList.add('active');
    });
  });
}

function initLightbox() {
  const triggers = document.querySelectorAll('[data-lightbox]');
  const overlay = document.querySelector('.lightbox-overlay');
  const stage = overlay ? overlay.querySelector('.lightbox-content') : null;
  if (!triggers.length || !overlay || !stage) return;

  let lastTrigger = null;

  function close() {
    overlay.classList.remove('is-open');
    overlay.setAttribute('aria-hidden', 'true');
    document.body.style.overflow = '';
    if (lastTrigger) lastTrigger.focus();
  }

  function open(trigger) {
    lastTrigger = trigger;
    const swatchClass = trigger.dataset.swatch || '';
    const category = trigger.dataset.label || trigger.dataset.category || '';

    stage.innerHTML = '';

    const closeBtn = document.createElement('button');
    closeBtn.type = 'button';
    closeBtn.className = 'lightbox-close';
    closeBtn.setAttribute('aria-label', 'Close');
    closeBtn.innerHTML = '&times;';
    closeBtn.addEventListener('click', close);
    if (!window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
      attachRipple(closeBtn);
    }

    const panel = document.createElement('div');
    panel.className = `lightbox-panel ${swatchClass}`;
    if (category) {
      const tag = document.createElement('span');
      tag.className = 'work-tag';
      tag.textContent = category;
      panel.appendChild(tag);
    }

    const caption = document.createElement('p');
    caption.className = 'lightbox-caption';
    caption.textContent = 'Placeholder composition. Real photography to come.';

    stage.appendChild(closeBtn);
    stage.appendChild(panel);
    stage.appendChild(caption);

    overlay.classList.add('is-open');
    overlay.setAttribute('aria-hidden', 'false');
    document.body.style.overflow = 'hidden';
    closeBtn.focus();
  }

  triggers.forEach((trigger) => {
    trigger.addEventListener('click', (e) => {
      e.preventDefault();
      open(trigger);
    });
  });

  overlay.addEventListener('click', (e) => {
    if (e.target === overlay) close();
  });

  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape' && overlay.classList.contains('is-open')) close();
  });
}
