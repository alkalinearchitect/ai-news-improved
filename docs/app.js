// AI News - Interactive Features
document.addEventListener('DOMContentLoaded', function() {
  document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function(e) {
      e.preventDefault();
      const target = document.querySelector(this.getAttribute('href'));
      if (target) { target.scrollIntoView({ behavior: 'smooth' }); }
    });
  });
  if ('IntersectionObserver' in window) {
    const imageObserver = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          entry.target.src = entry.target.dataset.src || entry.target.src;
          entry.target.classList.remove('lazy');
          imageObserver.unobserve(entry.target);
        }
      });
    });
    document.querySelectorAll('img[loading="lazy"]').forEach(img => imageObserver.observe(img));
  }
});
