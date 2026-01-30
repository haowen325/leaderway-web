/**
 * Main JavaScript for 力偉板金機械股份有限公司 Website
 * Features: Mobile navigation, header scroll effects, back-to-top button
 */

document.addEventListener('DOMContentLoaded', () => {

    // ===== MOBILE NAVIGATION TOGGLE =====
    const mobileMenuToggle = document.querySelector('.mobile-menu-toggle');
    const mobileNavOverlay = document.querySelector('.mobile-nav-overlay');
    const mobileNavLinks = document.querySelectorAll('.mobile-nav-list a');

    // Toggle mobile menu visibility and update aria-expanded
    mobileMenuToggle.addEventListener('click', () => {
        const isOpen = mobileNavOverlay.classList.toggle('active');
        mobileMenuToggle.setAttribute('aria-expanded', isOpen);
    });

    // Close mobile menu when a link is clicked
    mobileNavLinks.forEach(link => {
        link.addEventListener('click', () => {
            mobileNavOverlay.classList.remove('active');
            mobileMenuToggle.setAttribute('aria-expanded', 'false');
        });
    });

    // ===== HEADER SCROLL EFFECT =====
    // Add shadow to header when user scrolls down
    const header = document.querySelector('.header');
    window.addEventListener('scroll', () => {
        if (window.scrollY > 50) {
            header.style.boxShadow = "0 4px 20px rgba(0,0,0,0.1)";
        } else {
            header.style.boxShadow = "0 2px 10px rgba(0,0,0,0.05)";
        }
    });

    // ===== BACK TO TOP BUTTON =====
    const backToTopBtn = document.getElementById('back-to-top');

    if (backToTopBtn) {
        // Show/hide button based on scroll position
        window.addEventListener('scroll', () => {
            if (window.scrollY > 300) {
                backToTopBtn.classList.add('show');
            } else {
                backToTopBtn.classList.remove('show');
            }
        });

        // Smooth scroll to top when button is clicked
        backToTopBtn.addEventListener('click', () => {
            window.scrollTo({
                top: 0,
                behavior: 'smooth'
            });
        });
    }

});
