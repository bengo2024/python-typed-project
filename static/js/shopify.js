// Shopify E-Commerce - JavaScript

// Auto-hide flash messages after 5 seconds
document.addEventListener('DOMContentLoaded', function() {
    const flashMessages = document.querySelectorAll('.flash');
    
    flashMessages.forEach(function(flash) {
        setTimeout(function() {
            flash.style.animation = 'slideOut 0.3s ease-out';
            setTimeout(function() {
                flash.remove();
            }, 300);
        }, 5000);
    });
});

// Animation pour slideOut
const style = document.createElement('style');
style.textContent = `
    @keyframes slideOut {
        from {
            transform: translateX(0);
            opacity: 1;
        }
        to {
            transform: translateX(400px);
            opacity: 0;
        }
    }
`;
document.head.appendChild(style);

// Smooth scroll
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute('href'));
        if (target) {
            target.scrollIntoView({
                behavior: 'smooth',
                block: 'start'
            });
        }
    });
});

// Confirmation avant suppression
document.querySelectorAll('form[action*="remove"]').forEach(form => {
    form.addEventListener('submit', function(e) {
        if (!confirm('Êtes-vous sûr de vouloir retirer cet article ?')) {
            e.preventDefault();
        }
    });
});

console.log('🛍️ Shopify E-Commerce chargé avec succès !');
console.log('✅ Intégré avec CI/CD (MyPy + Ruff + Chatbot)');

