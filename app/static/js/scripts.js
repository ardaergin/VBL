// scripts.js

// Navbar Scroll Effect
let lastScrollY = window.scrollY;
const navbar = document.querySelector('.navbar');

function handleScroll() {
    if (window.scrollY > lastScrollY && window.scrollY > 50) {
        navbar.classList.add('hidden');
    } else if (window.scrollY < lastScrollY || window.scrollY <= 50) {
        navbar.classList.remove('hidden');
    }
    lastScrollY = window.scrollY;
}


window.addEventListener('scroll', handleScroll);

// Mobile Navigation Toggle
const hamburger = document.getElementById('hamburger');
const navLinks = document.querySelector('.nav-links');

hamburger.addEventListener('click', () => {
    navLinks.classList.toggle('active');
    hamburger.classList.toggle('open');
});

// Smooth Scrolling for Internal Links (Optional)
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function(e) {
        e.preventDefault();
        const targetElement = document.querySelector(this.getAttribute('href'));
        if (targetElement) {
            targetElement.scrollIntoView({
                behavior: 'smooth',
                block: 'start'
            });
        }
    });
});
