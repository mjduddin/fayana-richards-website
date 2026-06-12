"""Shared HTML templates for the Fayana Richards portfolio website."""

SITE_URL = "https://fayanarichards.com"  # Update before launch; see README.
SITE_NAME = "Dr. Fayana Richards, MPH, PMP"

NAV = [
    ("Home", "/"),
    ("About", "/about/"),
    ("Program Leadership", "/program-leadership/"),
    ("Selected Work", "/work/"),
    ("Experience", "/experience/"),
    ("Research and Writing", "/research-writing/"),
    ("Teaching and Speaking", "/teaching-facilitation/"),
    ("Résumé", "/resume/"),
    ("Contact", "/contact/"),
]

FOOTER_EXPLORE = [
    ("About", "/about/"),
    ("Program and Project Leadership", "/program-leadership/"),
    ("Selected Work", "/work/"),
    ("Experience", "/experience/"),
    ("Research and Writing", "/research-writing/"),
    ("Teaching and Facilitation", "/teaching-facilitation/"),
    ("Speaking", "/speaking/"),
    ("Résumé", "/resume/"),
    ("Contact", "/contact/"),
]

FOOTER_SITE = [
    ("Accessibility Statement", "/accessibility/"),
    ("Privacy Statement", "/privacy/"),
]


def rel(path, depth):
    """Convert a site-absolute path like /about/ to a relative href for a page at the given depth."""
    prefix = "../" * depth
    if path == "/":
        return prefix if prefix else "./"
    return prefix + path.lstrip("/")


def head(title, description, path, depth, og_type="website", extra_jsonld=""):
    css = rel("/css/styles.css", depth)
    favicon = rel("/assets/icons/favicon.svg", depth)
    canonical = SITE_URL + path
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title}</title>
  <meta name="description" content="{description}">
  <link rel="canonical" href="{canonical}">
  <meta property="og:type" content="{og_type}">
  <meta property="og:title" content="{title}">
  <meta property="og:description" content="{description}">
  <meta property="og:url" content="{canonical}">
  <meta property="og:site_name" content="{SITE_NAME}">
  <meta name="twitter:card" content="summary">
  <meta name="twitter:title" content="{title}">
  <meta name="twitter:description" content="{description}">
  <link rel="icon" type="image/svg+xml" href="{favicon}">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Source+Serif+4:wght@600;700&family=Source+Sans+3:ital,wght@0,400;0,600;1,400&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="{css}">
{extra_jsonld}</head>
"""


def header(active_path, depth):
    items = []
    for label, path in NAV:
        href = rel(path, depth)
        current = ' aria-current="page"' if path == active_path else ""
        items.append(f'        <li><a href="{href}"{current}>{label}</a></li>')
    nav_items = "\n".join(items)
    home_href = rel("/", depth)
    return f"""<body>
<a class="skip-link" href="#main-content">Skip to main content</a>
<header class="site-header">
  <div class="container header-inner">
    <a class="wordmark" href="{home_href}">Dr.&nbsp;Fayana&nbsp;Richards, <span class="wordmark-credentials">MPH, PMP</span></a>
    <button class="menu-toggle" type="button" aria-expanded="false" aria-controls="primary-navigation">
      <span class="menu-toggle-bar" aria-hidden="true"></span>
      <span class="menu-toggle-label">Menu</span>
    </button>
    <nav aria-label="Primary">
      <ul id="primary-navigation" class="primary-nav">
{nav_items}
      </ul>
    </nav>
  </div>
</header>
<main id="main-content">
"""


def breadcrumbs(trail, depth):
    """trail: list of (label, path or None for current page)."""
    parts = []
    for label, path in trail:
        if path is None:
            parts.append(f'      <li aria-current="page">{label}</li>')
        else:
            parts.append(f'      <li><a href="{rel(path, depth)}">{label}</a></li>')
    items = "\n".join(parts)
    return f"""  <nav class="breadcrumbs" aria-label="Breadcrumb">
    <ol class="container">
{items}
    </ol>
  </nav>
"""


def breadcrumb_jsonld(trail):
    items = []
    for i, (label, path) in enumerate(trail, start=1):
        item = {"@type": "ListItem", "position": i, "name": label}
        if path is not None:
            item["itemListElement"] = None
        items.append(item)
    # Built manually in build.py where needed; kept simple here.
    return ""


def footer(depth):
    explore = "\n".join(
        f'          <li><a href="{rel(p, depth)}">{l}</a></li>' for l, p in FOOTER_EXPLORE
    )
    site_links = "\n".join(
        f'          <li><a href="{rel(p, depth)}">{l}</a></li>' for l, p in FOOTER_SITE
    )
    js = rel("/js/main.js", depth)
    return f"""</main>
<footer class="site-footer">
  <div class="container footer-grid">
    <div class="footer-brand">
      <p class="footer-wordmark">Dr. Fayana Richards, MPH, PMP</p>
      <p>Public health program strategy and operations leader, and medical anthropologist.</p>
      <ul class="footer-contact-list">
        <li><a href="mailto:frichard84@gmail.com">frichard84@gmail.com</a></li>
        <li><a href="https://www.linkedin.com/in/fayanar/" rel="me noopener" target="_blank">LinkedIn profile<span class="visually-hidden"> (opens in a new tab)</span></a></li>
      </ul>
    </div>
    <nav aria-label="Footer">
      <h2 class="footer-heading">Explore</h2>
      <ul class="footer-links">
{explore}
      </ul>
    </nav>
    <div>
      <h2 class="footer-heading">Site</h2>
      <ul class="footer-links">
{site_links}
      </ul>
    </div>
  </div>
  <div class="container footer-legal">
    <p>&copy; <span id="footer-year">2026</span> Fayana Richards. All rights reserved.</p>
  </div>
</footer>
<script src="{js}"></script>
</body>
</html>
"""


def page(title, description, path, depth, content, active_path=None,
         trail=None, og_type="website", extra_jsonld=""):
    active = active_path if active_path is not None else path
    html = head(title, description, path, depth, og_type, extra_jsonld)
    html += header(active, depth)
    if trail:
        html += breadcrumbs(trail, depth)
    html += content
    html += footer(depth)
    return html
