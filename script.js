document.addEventListener('DOMContentLoaded', () => {

    // Mobile Navigation Toggle
    const mobileMenuToggle = document.querySelector('.mobile-menu-toggle');
    const mobileNavOverlay = document.querySelector('.mobile-nav-overlay');
    const mobileNavLinks = document.querySelectorAll('.mobile-nav-list a');

    mobileMenuToggle.addEventListener('click', () => {
        mobileNavOverlay.classList.toggle('active');

        // Transform hamburger to X (optional, simple CSS class toggle if needed, or just keep simple)
        // For now, the overlay sliding in is enough.
    });

    // Close mobile menu when a link is clicked
    mobileNavLinks.forEach(link => {
        link.addEventListener('click', () => {
            mobileNavOverlay.classList.remove('active');
        });
    });

    // Header Scroll Effect (Optional: add shadow on scroll)
    const header = document.querySelector('.header');
    window.addEventListener('scroll', () => {
        if (window.scrollY > 50) {
            header.style.boxShadow = "0 4px 20px rgba(0,0,0,0.1)";
        } else {
            header.style.boxShadow = "0 2px 10px rgba(0,0,0,0.05)";
        }
    });

});
