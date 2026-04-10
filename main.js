document.addEventListener('DOMContentLoaded', () => {
    // Smooth Scroll Logic for anchor links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            const targetId = this.getAttribute('href');
            if(targetId === '#') return;
            const targetElement = document.querySelector(targetId);
            if(targetElement) {
                e.preventDefault();
                targetElement.scrollIntoView({
                    behavior: 'smooth'
                });
            }
        });
    });

    // Mobile Menu Toggle
    const menuBtn = document.getElementById('mobileMenuBtn');
    const mobileMenu = document.getElementById('mobileMenu');
    
    if (menuBtn && mobileMenu) {
        menuBtn.addEventListener('click', () => {
            if (mobileMenu.classList.contains('mobile-hidden')) {
                mobileMenu.classList.remove('mobile-hidden');
                mobileMenu.classList.add('mobile-visible');
                menuBtn.textContent = 'CLOSE';
            } else {
                mobileMenu.classList.add('mobile-hidden');
                mobileMenu.classList.remove('mobile-visible');
                menuBtn.textContent = 'MENU';
            }
        });
    }

    // Hover Effect Logic for Gallery
    const galleryImages = document.querySelectorAll('.gallery-img');
    galleryImages.forEach(img => {
        img.addEventListener('mouseenter', () => {
            img.style.transform = "scale(1.05)";
        });
        img.addEventListener('mouseleave', () => {
            img.style.transform = "scale(1)";
        });
    });
});
