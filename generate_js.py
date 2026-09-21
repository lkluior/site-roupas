import os

js_content = """/**
 * STREET VIBE - Premium Streetwear Catalog
 * JS Principal - Vanilla JS
 */

const CONFIG = {
  whatsappNumber: '5511999999999', // Coloque seu número aqui (Ex: 5511999999999)
  storeName: 'STREET VIBE',
  defaultMessage: 'Olá! Tenho interesse na peça {product}. Gostaria de saber mais informações.',
  genericMessage: 'Olá! Gostaria de falar com o atendimento da STREET VIBE.',
};

document.addEventListener('DOMContentLoaded', () => {
  initHeader();
  initMobileMenu();
  initSmoothScroll();
  initScrollReveal();
  initInfiniteCarousel();
  initBrandFilters();
  initGalleryLightbox();
  initWhatsAppButtons();
});

// ==========================================
// HEADER SCROLL EFFECT
// ==========================================
function initHeader() {
  const header = document.querySelector('.header');
  if (!header) return;

  let ticking = false;
  window.addEventListener('scroll', () => {
    if (!ticking) {
      window.requestAnimationFrame(() => {
        if (window.scrollY > 50) {
          header.classList.add('scrolled');
        } else {
          header.classList.remove('scrolled');
        }
        ticking = false;
      });
      ticking = true;
    }
  });
}

// ==========================================
// MOBILE MENU
// ==========================================
function initMobileMenu() {
  const hamburger = document.querySelector('.hamburger');
  const navMenu = document.querySelector('.nav-menu');
  const navLinks = document.querySelectorAll('.nav-link');

  if (!hamburger || !navMenu) return;

  const toggleMenu = () => {
    hamburger.classList.toggle('active');
    navMenu.classList.toggle('active');
    document.body.style.overflow = navMenu.classList.contains('active') ? 'hidden' : '';
  };

  hamburger.addEventListener('click', toggleMenu);

  navLinks.forEach(link => {
    link.addEventListener('click', () => {
      hamburger.classList.remove('active');
      navMenu.classList.remove('active');
      document.body.style.overflow = '';
    });
  });

  document.addEventListener('click', (e) => {
    if (navMenu.classList.contains('active') && !navMenu.contains(e.target) && !hamburger.contains(e.target)) {
      hamburger.classList.remove('active');
      navMenu.classList.remove('active');
      document.body.style.overflow = '';
    }
  });
}

// ==========================================
// SMOOTH SCROLL
// ==========================================
function initSmoothScroll() {
  document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
      const targetId = this.getAttribute('href');
      if (targetId === '#') return;
      
      const targetElement = document.querySelector(targetId);
      if (targetElement) {
        e.preventDefault();
        const headerOffset = document.querySelector('header')?.offsetHeight || 80;
        const elementPosition = targetElement.getBoundingClientRect().top;
        const offsetPosition = elementPosition + window.pageYOffset - headerOffset;

        window.scrollTo({
          top: offsetPosition,
          behavior: 'smooth'
        });
      }
    });
  });
}

// ==========================================
// SCROLL REVEAL (INTERSECTION OBSERVER)
// ==========================================
function initScrollReveal() {
  const revealElements = document.querySelectorAll('.reveal');
  if (!('IntersectionObserver' in window)) {
    revealElements.forEach(el => el.classList.add('active'));
    return;
  }
  const observer = new IntersectionObserver((entries, observer) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('active');
        observer.unobserve(entry.target);
      }
    });
  }, { threshold: 0.1 });
  revealElements.forEach(el => observer.observe(el));
}

// ==========================================
// INFINITE CAROUSEL
// ==========================================
function initInfiniteCarousel() {
  const track = document.querySelector('.carousel-track');
  if (!track) return;
  
  // Clona os itens para efeito de scroll infinito sem JS pesado
  const items = track.querySelectorAll('.carousel-item');
  items.forEach(item => {
    const clone = item.cloneNode(true);
    track.appendChild(clone);
  });

  track.addEventListener('mouseenter', () => track.style.animationPlayState = 'paused');
  track.addEventListener('mouseleave', () => track.style.animationPlayState = 'running');
  
  let isDown = false;
  let startX;
  let scrollLeft;
  track.addEventListener('mousedown', (e) => {
    isDown = true;
    track.classList.add('active');
    startX = e.pageX - track.offsetLeft;
    scrollLeft = track.scrollLeft;
    track.style.animationPlayState = 'paused';
  });
  track.addEventListener('mouseleave', () => {
    isDown = false;
    track.classList.remove('active');
    track.style.animationPlayState = 'running';
  });
  track.addEventListener('mouseup', () => {
    isDown = false;
    track.classList.remove('active');
    track.style.animationPlayState = 'running';
  });
  track.addEventListener('mousemove', (e) => {
    if (!isDown) return;
    e.preventDefault();
    const x = e.pageX - track.offsetLeft;
    const walk = (x - startX) * 2;
    track.scrollLeft = scrollLeft - walk;
  });
}

// ==========================================
// FILTROS POR MARCA
// ==========================================
function initBrandFilters() {
  const filterBtns = document.querySelectorAll('.filter-btn');
  const products = document.querySelectorAll('.product-card');

  filterBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      filterBtns.forEach(b => b.classList.remove('active'));
      btn.classList.add('active');

      const selectedBrand = btn.getAttribute('data-brand');
      const productsGrid = document.querySelector('.products-grid');
      
      productsGrid.style.opacity = '0'; // Fade out
      
      setTimeout(() => {
        products.forEach(card => {
          const cardBrand = card.getAttribute('data-brand');
          if (selectedBrand === 'Todas' || cardBrand === selectedBrand) {
            card.style.display = 'flex'; 
          } else {
            card.style.display = 'none'; 
          }
        });
        productsGrid.style.opacity = '1'; // Fade in
      }, 300);
    });
  });
}

// ==========================================
// GALERIA & LIGHTBOX
// ==========================================
function initGalleryLightbox() {
  const galleryItems = document.querySelectorAll('.gallery-item img');
  const lightbox = document.getElementById('lightbox');
  
  if (!lightbox || galleryItems.length === 0) return;

  const lightboxImg = lightbox.querySelector('#lightbox-img');
  const closeBtn = lightbox.querySelector('.lightbox-close');
  const prevBtn = lightbox.querySelector('.lightbox-prev');
  const nextBtn = lightbox.querySelector('.lightbox-next');
  
  let currentImageIndex = 0;
  const images = Array.from(galleryItems).map(img => img.src);

  galleryItems.forEach((img, index) => {
    img.parentElement.addEventListener('click', () => {
      currentImageIndex = index;
      updateLightboxImage();
      lightbox.showModal();
    });
  });

  const updateLightboxImage = () => {
    if(lightboxImg) lightboxImg.src = images[currentImageIndex];
  };

  const showNext = () => {
    currentImageIndex = (currentImageIndex + 1) % images.length;
    updateLightboxImage();
  };

  const showPrev = () => {
    currentImageIndex = (currentImageIndex - 1 + images.length) % images.length;
    updateLightboxImage();
  };

  if(closeBtn) closeBtn.addEventListener('click', () => lightbox.close());
  if(nextBtn) nextBtn.addEventListener('click', showNext);
  if(prevBtn) prevBtn.addEventListener('click', showPrev);

  lightbox.addEventListener('click', (e) => {
    if (e.target === lightbox) lightbox.close();
  });
  lightbox.addEventListener('keydown', (e) => {
    if (e.key === 'ArrowRight') showNext();
    if (e.key === 'ArrowLeft') showPrev();
  });
}

// ==========================================
// WHATSAPP
// ==========================================
function initWhatsAppButtons() {
  const productBtns = document.querySelectorAll('.whatsapp-btn');
  productBtns.forEach(btn => {
    btn.addEventListener('click', (e) => {
      e.preventDefault();
      const productName = btn.getAttribute('data-product');
      openWhatsApp(productName);
    });
  });
  
  const floatBtn = document.getElementById('whatsapp-float');
  if (floatBtn) {
    setTimeout(() => {
      floatBtn.classList.add('visible');
    }, 1000);
  }
}

function openWhatsApp(productName = null) {
  let message = productName && productName !== 'null'
    ? CONFIG.defaultMessage.replace('{product}', productName) 
    : CONFIG.genericMessage;
  const encodedMessage = encodeURIComponent(message);
  const url = `https://api.whatsapp.com/send?phone=${CONFIG.whatsappNumber}&text=${encodedMessage}`;
  window.open(url, '_blank');
}
"""

with open(r'c:\Users\luka\Desktop\site de roupas\js\script.js', 'w', encoding='utf-8') as f:
    f.write(js_content)
print('JS rewritten.')
