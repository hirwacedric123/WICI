(() => {
  const navLinks = document.querySelectorAll('.navbar .nav-link');
  const currentPath = window.location.pathname.replace(/\/+$/, '') || '/';

  navLinks.forEach((link) => {
    const href = (link.getAttribute('href') || '').replace(/\/+$/, '') || '/';
    const isActive = href === '/'
      ? currentPath === '/'
      : currentPath === href || currentPath.startsWith(`${href}/`);

    if (isActive) {
      link.classList.add('active');
      link.setAttribute('aria-current', 'page');
    }
  });
})();

(() => {
  const body = document.body;
  if (!body) return;

  const prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  if (prefersReducedMotion) {
    body.classList.add('reduced-motion');
  }

  // Phase 1: shared reveal animation system.
  const revealTargets = document.querySelectorAll(
    '.page-header, .section-intro, .hero-stack, .hero-impact-card, .cta-section, .content-glass-card, .info-card, .program-card, .impact-card, .event-card, .join-box, .contact-form, .contact-faq, .contact-utility-card, .platform-visual-wrap'
  );

  revealTargets.forEach((el, index) => {
    if (el.classList.contains('hero-stack')) {
      el.classList.add('reveal');
      return;
    }

    el.classList.add('reveal', index % 2 === 0 ? 'reveal-up' : 'reveal-up-soft');
    if (index % 3 === 1) el.classList.add('delay-1');
    if (index % 3 === 2) el.classList.add('delay-2');
  });

  const revealObserver =
    !prefersReducedMotion && 'IntersectionObserver' in window
      ? new IntersectionObserver(
          (entries, observer) => {
            entries.forEach((entry) => {
              if (!entry.isIntersecting) return;
              entry.target.classList.add('is-visible');
              observer.unobserve(entry.target);
            });
          },
          { threshold: 0.14, rootMargin: '0px 0px -5% 0px' }
        )
      : null;

  document.querySelectorAll('.reveal').forEach((el) => {
    if (prefersReducedMotion) {
      el.classList.add('is-visible');
      return;
    }
    if (revealObserver) revealObserver.observe(el);
    else el.classList.add('is-visible');
  });

  // Phase 2: hero/page heading text animation.
  const headingTargets = document.querySelectorAll('.hero-title, .page-header h1');
  headingTargets.forEach((heading) => {
    heading.classList.add('text-reveal');
  });

  // Phase 3: stagger card/grid items by page section.
  const gridItems = document.querySelectorAll('.card-grid > [class*="col-"]');
  gridItems.forEach((item, index) => {
    const card = item.querySelector('.info-card, .program-card, .event-card, .impact-card, .content-glass-card');
    if (!card) return;
    card.classList.add('reveal', 'reveal-up-soft');
    card.style.setProperty('--stagger-delay', `${(index % 6) * 70}ms`);
    card.classList.add('stagger-reveal');
  });

  // Phase 3: timeline and model cards motion hooks.
  document.querySelectorAll('.about-timeline-item, .partner-model').forEach((el, index) => {
    el.classList.add('reveal', 'reveal-left');
    if (index % 2 === 1) el.classList.replace('reveal-left', 'reveal-right');
    if (index % 3 === 1) el.classList.add('delay-1');
    if (index % 3 === 2) el.classList.add('delay-2');
  });

  // Phase 3: gallery card hover affordance classes.
  document.querySelectorAll('.media-cover').forEach((media) => {
    const card = media.closest('.info-card');
    if (card) card.classList.add('media-gallery-card');
  });

  // Phase 3: FAQ accordion state class for smoother open/close.
  document.querySelectorAll('.accordion .accordion-collapse').forEach((collapse) => {
    collapse.addEventListener('show.bs.collapse', () => {
      collapse.closest('.accordion-item')?.classList.add('is-open');
    });
    collapse.addEventListener('hide.bs.collapse', () => {
      collapse.closest('.accordion-item')?.classList.remove('is-open');
    });
  });

  // Phase 2: count up numeric values.
  const statSelectors = '.hero-metric-value, .hero-impact-value';
  const statElements = Array.from(document.querySelectorAll(statSelectors)).filter((el) => /\d/.test(el.textContent || ''));

  const animateCount = (el) => {
    const source = (el.textContent || '').trim();
    const match = source.match(/(\d+(?:\.\d+)?)/);
    if (!match) return;

    const target = Number.parseFloat(match[1]);
    if (Number.isNaN(target)) return;

    const prefix = source.slice(0, match.index);
    const suffix = source.slice((match.index || 0) + match[1].length);
    const useDecimals = match[1].includes('.');
    const duration = 1100;
    const startAt = performance.now();

    const step = (now) => {
      const elapsed = Math.min((now - startAt) / duration, 1);
      const eased = 1 - Math.pow(1 - elapsed, 3);
      const current = target * eased;
      const value = useDecimals ? current.toFixed(1) : Math.round(current).toString();
      el.textContent = `${prefix}${value}${suffix}`;
      if (elapsed < 1) requestAnimationFrame(step);
    };

    requestAnimationFrame(step);
  };

  if (statElements.length > 0 && !prefersReducedMotion && 'IntersectionObserver' in window) {
    const countObserver = new IntersectionObserver(
      (entries, observer) => {
        entries.forEach((entry) => {
          if (!entry.isIntersecting) return;
          animateCount(entry.target);
          observer.unobserve(entry.target);
        });
      },
      { threshold: 0.4 }
    );
    statElements.forEach((el) => countObserver.observe(el));
  }

  // Phase 2: contact form and button micro-interactions.
  const form = document.querySelector('.contact-form');
  if (form) {
    const controls = form.querySelectorAll('input, select, textarea');
    controls.forEach((field) => {
      field.classList.add('interactive-field');

      field.addEventListener('focus', () => field.classList.add('is-focused'));
      field.addEventListener('blur', () => {
        field.classList.remove('is-focused');
        if (field.hasAttribute('required') && !field.value.trim()) {
          field.classList.add('is-invalid-animated');
        } else {
          field.classList.remove('is-invalid-animated');
        }
      });

      field.addEventListener('input', () => {
        field.classList.remove('is-invalid-animated');
      });
    });

    const submitButton = form.querySelector('button[type="submit"]');
    if (submitButton) {
      submitButton.addEventListener('click', () => {
        submitButton.classList.add('is-loading');
        window.setTimeout(() => {
          submitButton.classList.remove('is-loading');
        }, 750);
      });
    }
  }
})();
