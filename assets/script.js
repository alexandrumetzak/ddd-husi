// Mobile nav toggle
const navToggle = document.getElementById('navToggle');
const navLinks = document.getElementById('navLinks');
navToggle?.addEventListener('click', () => navLinks.classList.toggle('open'));
navLinks?.querySelectorAll('a').forEach(a =>
  a.addEventListener('click', () => navLinks.classList.remove('open'))
);

// Current year in footer (elementul există doar pe unele pagini)
const yearEl = document.getElementById('year');
if (yearEl) yearEl.textContent = new Date().getFullYear();

// Numărul de WhatsApp al firmei (format internațional, fără +, spații sau 0 inițial)
const WHATSAPP_NUMBER = '40744913376';

// Form handling — trimite cererea direct pe WhatsApp
function handleForm(form, e) {
  e.preventDefault();
  const data = Object.fromEntries(new FormData(form).entries());

  const etichete = {
    nume: 'Nume', telefon: 'Telefon', localitate: 'Localitate',
    serviciu: 'Serviciu', mesaj: 'Mesaj'
  };
  const detalii = Object.entries(data)
    .filter(([, v]) => v)
    .map(([k, v]) => `${etichete[k] || k}: ${v}`)
    .join('\n');

  const text = `Bună ziua! Aș dori o ofertă pentru servicii DDD.\n\n${detalii}`;
  const url = `https://wa.me/${WHATSAPP_NUMBER}?text=${encodeURIComponent(text)}`;

  window.open(url, '_blank');
  form.reset();
}

document.getElementById('quickForm')?.addEventListener('submit', function (e) { handleForm(this, e); });
document.getElementById('contactForm')?.addEventListener('submit', function (e) { handleForm(this, e); });
