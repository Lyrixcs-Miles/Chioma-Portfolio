// Lettie Portfolio — Main JS
// Nav toggle, portfolio filters, lightbox, etc.

document.addEventListener('DOMContentLoaded', () => {
  initNavToggle();
  initPortfolioFilters();
  initLightbox();
});

function initNavToggle() {
  const toggle = document.querySelector('.nav-toggle');
  const nav = document.querySelector('.site-nav ul');
  if (!toggle || !nav) return;

  toggle.addEventListener('click', () => {
    nav.classList.toggle('open');
  });
}

function initPortfolioFilters() {
  const filterButtons = document.querySelectorAll('[data-filter]');
  const items = document.querySelectorAll('[data-category]');
  if (!filterButtons.length || !items.length) return;

  filterButtons.forEach((button) => {
    button.addEventListener('click', () => {
      const filter = button.dataset.filter;

      items.forEach((item) => {
        const show = filter === 'all' || item.dataset.category === filter;
        item.style.display = show ? '' : 'none';
      });

      filterButtons.forEach((b) => b.classList.remove('active'));
      button.classList.add('active');
    });
  });
}

function initLightbox() {
  const triggers = document.querySelectorAll('[data-lightbox]');
  if (!triggers.length) return;

  triggers.forEach((trigger) => {
    trigger.addEventListener('click', (e) => {
      e.preventDefault();
      // TODO: implement lightbox display
    });
  });
}
