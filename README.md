# Dr. Fayana Richards, MPH, PMP — Portfolio Website

A complete static portfolio website: semantic HTML, modern CSS, and vanilla JavaScript. No framework, no build step required to deploy.

## File structure

```
fayana-richards-website/
├── index.html                  Home
├── about/index.html            About
├── program-leadership/         Program and Project Leadership
├── work/                       Selected Work index + 6 case studies
│   ├── public-health-consulting/
│   ├── aging-caregiving-research/
│   ├── research-development-program/
│   ├── curriculum-development/
│   ├── research-project-coordination/
│   └── science-communication/
├── experience/                 Experience
├── research-writing/           Research and Writing
├── teaching-facilitation/      Teaching and Facilitation
├── speaking/                   Speaking
├── resume/                     Résumé
├── contact/                    Contact (form)
├── accessibility/              Accessibility statement
├── privacy/                    Privacy statement
├── 404.html                    Custom not-found page
├── css/styles.css              Design system (colors, typography, components)
├── js/main.js                  Menu, filters, form validation
├── data/                       Structured content files (profile, experience, projects, publications, presentations)
├── assets/                     Icons, images, downloads
├── docs/                       INTERNAL: source ledger, unresolved items, quality report — do not deploy if you prefer
├── sitemap.xml
└── robots.txt
```

## Local preview

From this folder run `python3 -m http.server 8000` and open `http://localhost:8000`. (Pages also open directly from disk because links are relative.)

## Deployment

### Netlify (recommended — easiest contact form)
1. Create a free Netlify account and drag this folder into "Deploy manually," or connect a Git repository.
2. The contact form is already configured for Netlify Forms (`data-netlify="true"`, honeypot spam protection). After the first deploy, open Site settings → Forms → Form notifications and add an email notification to **frichard84@gmail.com**.
3. Set the custom domain, then update `SITE_URL` (see "Domain" below).

### GitHub Pages
1. Create a repository and push this folder's contents to the root (or `/docs`).
2. Settings → Pages → deploy from branch.
3. GitHub Pages has no form backend. Use Formspree: create a free form at formspree.io linked to **frichard84@gmail.com**, then in `contact/index.html` change the form tag's `action` to your Formspree endpoint (e.g. `https://formspree.io/f/XXXXXXXX`), remove `data-netlify="true"`, and add `<input type="hidden" name="_next" value="https://YOUR-DOMAIN/contact/?submitted=true">` so the success message displays.

No credentials or private keys live in this code; form routing is handled entirely by the chosen service.

### Domain
All metadata currently uses the placeholder `https://fayanarichards.com`. When the final domain is confirmed, find-and-replace that value across the HTML files, `sitemap.xml`, and `robots.txt`.

## Editing content

- **Page text:** edit the HTML pages directly; each section is plainly marked. Shared header/footer markup is identical across pages — if you change navigation, change it on every page (or use the generator in `_build/` if you have it).
- **Structured content:** `data/*.json` mirrors the site content (profile, experience, projects, publications, presentations) with verification status and source fields. Treat it as the content source of truth and keep it in sync with the pages.
- **Add the résumé PDF:** save the approved file as `assets/downloads/Fayana Richards Resume.pdf`, then in `resume/index.html` replace the "being prepared" empty state with the commented-out download button just below it.
- **Add the headshot:** save as `assets/images/fayana-richards-headshot.webp` and replace the `portrait-placeholder` block in `index.html` with `<img src="assets/images/fayana-richards-headshot.webp" alt="Dr. Fayana Richards" width="280" height="350">`.
- **Add publications/presentations:** only verified entries. Add the citation to the relevant JSON file and replace the matching empty state on the page with the formatted entry.
- **Factual guardrails:** before publishing anything new, check `docs/source-ledger.md` and `docs/unresolved-items.md`. Never publish unverified metrics, clients, outcomes, or testimonials.

## Design system quick reference

Colors: aubergine `#2B0423` (primary), bronze `#A86527` (accent — decorative/large elements), bronze-ink `#8A4F1D` (link text, darkened for WCAG AA), warm neutral `#EDEAE8`, charcoal `#22272B`, slate `#5D6870` (a darkened `#4D575E` is used for small secondary text to pass AA). Fonts: Source Serif 4 (headings) and Source Sans 3 (body) via Google Fonts.
