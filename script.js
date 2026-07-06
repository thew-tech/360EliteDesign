document.addEventListener('DOMContentLoaded', () => {
    // 1. Sticky Navbar & Scroll Styling
    const navbar = document.getElementById('navbar');
    
    window.addEventListener('scroll', () => {
        if (window.scrollY > 50) {
            navbar.classList.add('scrolled');
        } else {
            navbar.classList.remove('scrolled');
        }
    });

    // 2. Smooth Scrolling for Anchor Links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            
            const targetId = this.getAttribute('href');
            if (targetId === '#') return;
            
            const targetElement = document.querySelector(targetId);
            if (targetElement) {
                const headerOffset = 80;
                const elementPosition = targetElement.getBoundingClientRect().top;
                const offsetPosition = elementPosition + window.pageYOffset - headerOffset;
  
                window.scrollTo({
                    top: offsetPosition,
                    behavior: 'smooth'
                });
            }
        });
    });

    // 3. Scroll Reveal Animations (Intersection Observer)
    const revealElements = document.querySelectorAll('.slide-up');
    
    const revealOptions = {
        threshold: 0.15,
        rootMargin: "0px 0px -50px 0px"
    };

    const revealOnScroll = new IntersectionObserver(function(entries, observer) {
        entries.forEach(entry => {
            if (!entry.isIntersecting) {
                return;
            } else {
                entry.target.classList.add('visible');
                observer.unobserve(entry.target);
            }
        });
    }, revealOptions);

    revealElements.forEach(el => {
        revealOnScroll.observe(el);
    });

    // 4. Number Counter Animation for Stats
    const counters = document.querySelectorAll('.counter');
    let hasAnimated = false;

    const animateCounters = () => {
        counters.forEach(counter => {
            const target = +counter.getAttribute('data-target');
            const duration = 2000; // ms
            const increment = target / (duration / 16); // 60fps
            
            let currentNum = 0;
            
            const updateCounter = () => {
                currentNum += increment;
                if(currentNum < target) {
                    counter.innerText = Math.ceil(currentNum);
                    requestAnimationFrame(updateCounter);
                } else {
                    counter.innerText = target;
                }
            };
            
            updateCounter();
        });
    };

    // Observer specifically for the stats section
    const statsSection = document.getElementById('stats');
    if (statsSection) {
        const statsObserver = new IntersectionObserver((entries) => {
            if(entries[0].isIntersecting && !hasAnimated) {
                hasAnimated = true;
                animateCounters();
            }
        }, { threshold: 0.5 });
        
        statsObserver.observe(statsSection);
    }

    // 5. Mobile Menu Toggle (Basic implementation)
    const mobileBtn = document.querySelector('.mobile-menu-btn');
    const navLinks = document.querySelector('.nav-links');
    
    if (mobileBtn) {
        mobileBtn.addEventListener('click', () => {
            // A simple toggle logic. For a real app, you'd want a nicer slide-out drawer
            if (navLinks.style.display === 'flex') {
                navLinks.style.display = 'none';
            } else {
                navLinks.style.display = 'flex';
                navLinks.style.flexDirection = 'column';
                navLinks.style.position = 'absolute';
                navLinks.style.top = '100%';
                navLinks.style.left = '0';
                navLinks.style.width = '100%';
                navLinks.style.background = 'white';
                navLinks.style.padding = '20px';
                navLinks.style.boxShadow = '0 10px 20px rgba(0,0,0,0.1)';
            }
        });
    }

    // 6. Form Submission (Prevent Default)
    const form = document.querySelector('.contact-form');
    if (form) {
        form.addEventListener('submit', (e) => {
            e.preventDefault();
            const btn = form.querySelector('button');
            const originalText = btn.innerText;
            btn.innerText = 'Sending...';
            btn.style.opacity = '0.8';
            
            // Simulate network request
            setTimeout(() => {
                btn.innerText = 'Message Sent!';
                btn.style.background = '#28a745';
                btn.style.boxShadow = '0 8px 20px rgba(40, 167, 69, 0.3)';
                form.reset();
                
                setTimeout(() => {
                    btn.innerText = originalText;
                    btn.style.background = '';
                    btn.style.boxShadow = '';
                    btn.style.opacity = '1';
                }, 3000);
            }, 1500);
        });
    }
});
