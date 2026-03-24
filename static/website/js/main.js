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
