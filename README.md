# Mauricio Ruiz — portfolio

A dependency-free, responsive portfolio for GitHub Pages. Includes five project case studies, professional experience, a Life in Data section and an on-demand embedded Streamlit assistant.

## Edit and build

- Edit project and page copy in `scripts/build.py`, then run `python scripts/build.py`.
- Edit styling in `assets/style.css` and interactions in `assets/main.js`.
- Replace `assets/mauricio-ruiz-profile.pdf` with a preferred general CV and update button labels if desired. The included PDF is a concise professional profile based on the public experience documents, not an imported application CV.
- Real project screenshots are local assets. The hero graphic is an illustrative SVG, not project results.
- The blog cards use published post URLs. Update them when adding new posts or changing blog permalinks.

## Hosting

Serve the repository root through GitHub Pages. `.nojekyll` keeps the HTML/CSS/JS files as authored. No npm installation, backend, API key or build service is needed. The assistant remains hosted independently at Streamlit and loads only after a visitor opens it; a direct link is available if embedding fails.

## Content sources

Professional experience and education: public Markdown in `personal-ai-cv-assistant/data/`. Projects: original portfolio and linked project reports. No client data or internal dashboards are published. The earlier homepage copy is retained in `docs/legacy-portfolio.md`.
