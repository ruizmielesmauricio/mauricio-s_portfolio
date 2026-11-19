'use strict';
const menu = document.querySelector('.menu-toggle');
const nav = document.querySelector('#main-nav');
function closeMenu() { nav?.classList.remove('is-open'); menu?.setAttribute('aria-expanded', 'false'); }
menu?.addEventListener('click', () => { const open = menu.getAttribute('aria-expanded') !== 'true'; menu.setAttribute('aria-expanded', String(open)); nav.classList.toggle('is-open', open); });
nav?.querySelectorAll('a').forEach(a => a.addEventListener('click', closeMenu));
document.addEventListener('keydown', event => { if (event.key === 'Escape') closeMenu(); });
document.querySelectorAll('[data-filter]').forEach(button => button.addEventListener('click', () => {
 const category = button.dataset.filter;
 document.querySelectorAll('[data-filter]').forEach(b => b.setAttribute('aria-pressed', String(b === button)));
 let count = 0;
 document.querySelectorAll('.project-card').forEach(card => { card.hidden = category !== 'All' && card.dataset.category !== category; if (!card.hidden) count++; });
 const status = document.querySelector('#filter-status'); if (status) status.textContent = `${count} project${count === 1 ? '' : 's'} shown`;
}));
const dialog = document.querySelector('#assistant-dialog');
let assistantOpener;
document.querySelectorAll('[data-open-assistant]').forEach(button => button.addEventListener('click', () => {
 if (!dialog?.showModal) { window.open('https://mauricio-ai-cv-assistant.streamlit.app', '_blank', 'noopener,noreferrer'); return; }
 assistantOpener = button;
 const iframe = dialog.querySelector('iframe');
 if (!iframe.hasAttribute('src')) iframe.src = iframe.dataset.src;
 dialog.showModal(); document.body.style.overflow = 'hidden';
}));
dialog?.querySelector('.close-dialog').addEventListener('click', () => dialog.close());
dialog?.addEventListener('click', event => { const rect = dialog.getBoundingClientRect(); if (event.target === dialog && (event.clientX < rect.left || event.clientX > rect.right || event.clientY < rect.top || event.clientY > rect.bottom)) dialog.close(); });
dialog?.addEventListener('close', () => { document.body.style.overflow = ''; assistantOpener?.focus(); });
document.querySelectorAll('[data-year]').forEach(el => el.textContent = new Date().getFullYear());
// Decorative illustration, deliberately not presented as measured project data.
const points = document.querySelector('#data-points');
if (points) { let seed = 74; const random = () => { seed = (seed * 16807) % 2147483647; return (seed - 1) / 2147483646; }; for (let i = 0; i < 105; i++) { const x = 42 + random() * 378; const y = Math.max(35, Math.min(284, 310 - x * .5 + (random() - .5) * 130)); const c = document.createElementNS('http://www.w3.org/2000/svg', 'circle'); c.setAttribute('cx', x); c.setAttribute('cy', y); c.setAttribute('r', 2.5 + random() * 2); c.setAttribute('opacity', .2 + random() * .55); points.appendChild(c); } }


// Life in Data: discover published Jekyll articles directly from the blog feed.
// The existing two HTML cards remain visible if this feed cannot load.
(async function loadLatestBlogPosts() {
 const container = document.querySelector('#latest-blog-posts');
 if (!container) return;
 try {
  const response = await fetch('https://ruizmielesmauricio.github.io/posts.json', { cache: 'no-cache' });
  if (!response.ok) throw new Error('Blog feed unavailable');
  const data = await response.json();
  if (!data || !Array.isArray(data.posts)) throw new Error('Invalid blog feed');
  const posts = data.posts.filter(post => {
   if (!post || typeof post.title !== 'string' || typeof post.url !== 'string') return false;
   try { return new URL(post.url).origin === 'https://ruizmielesmauricio.github.io'; }
   catch { return false; }
  }).slice(0, 3);
  if (!posts.length) return;
  const fragment = document.createDocumentFragment();
  posts.forEach(post => {
   const card = document.createElement('a');
   card.className = 'writing-card';
   card.href = post.url;
   card.target = '_blank';
   card.rel = 'noopener noreferrer';
   const meta = document.createElement('span');
   meta.className = 'eyebrow';
   const category = (post.category || 'Article').toUpperCase();
   meta.textContent = category + (post.date ? ' / ' + post.date.toUpperCase() : '');
   const heading = document.createElement('h3');
   heading.textContent = post.title;
   const description = document.createElement('p');
   description.textContent = post.description || 'Read this article on Life in Data.';
   const link = document.createElement('span');
   link.className = 'text-link';
   link.textContent = 'Read the story ↗';
   card.append(meta, heading, description, link);
   fragment.appendChild(card);
  });
  container.replaceChildren(fragment);
 } catch (error) {
  console.warn('Using fallback blog cards:', error);
 }
})();
