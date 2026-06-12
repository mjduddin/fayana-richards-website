"""Build the Fayana Richards portfolio website into ../fayana-richards-website."""
import json
import os

from templates import SITE_URL, page
import pages_core
import pages_work
import pages_other

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")


def jsonld(data):
    return '  <script type="application/ld+json">\n' + json.dumps(data, indent=2) + "\n  </script>\n"


PERSON = {
    "@context": "https://schema.org",
    "@type": "Person",
    "name": "Fayana Richards",
    "honorificPrefix": "Dr.",
    "honorificSuffix": "PhD, MPH, PMP",
    "jobTitle": "Public Health Program Strategy and Operations Leader",
    "description": "Public health strategist, medical anthropologist, program leader, researcher, and educator with more than 18 years of experience.",
    "email": "mailto:frichard84@gmail.com",
    "url": SITE_URL + "/",
    "sameAs": ["https://www.linkedin.com/in/fayanar/"],
    "alumniOf": [
        {"@type": "CollegeOrUniversity", "name": "Michigan State University"},
        {"@type": "CollegeOrUniversity", "name": "University of Arizona"},
    ],
    "hasCredential": [
        {"@type": "EducationalOccupationalCredential", "credentialCategory": "degree", "name": "Doctor of Philosophy in Medical Anthropology"},
        {"@type": "EducationalOccupationalCredential", "credentialCategory": "degree", "name": "Master of Public Health"},
        {"@type": "EducationalOccupationalCredential", "credentialCategory": "certification", "name": "Project Management Professional (PMP)", "recognizedBy": {"@type": "Organization", "name": "Project Management Institute"}},
    ],
    "knowsAbout": [
        "Public health", "Program management", "Project management", "Medical anthropology",
        "Health disparities", "Social determinants of health", "Aging", "Caregiving",
        "Chronic illness", "Program evaluation", "Community engagement", "Curriculum development",
        "Facilitation", "Research translation",
    ],
}

SERVICE = {
    "@context": "https://schema.org",
    "@type": "ProfessionalService",
    "name": "Dr. Fayana Richards, MPH, PMP — Public Health Program Strategy and Leadership",
    "url": SITE_URL + "/",
    "description": "Consulting, speaking, facilitation, and program leadership in public health, research program management, evaluation, and professional learning.",
    "founder": {"@type": "Person", "name": "Fayana Richards"},
    "areaServed": "United States",
    "knowsAbout": ["Public health program strategy", "Program and project management", "Research and evaluation", "Facilitation and professional learning"],
}


def breadcrumb_ld(trail):
    items = []
    for i, (label, path) in enumerate(trail, start=1):
        item = {"@type": "ListItem", "position": i, "name": label}
        if path is not None:
            item["item"] = SITE_URL + path
        items.append(item)
    return {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": items}


def write(path, content):
    full = os.path.join(OUT, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w", encoding="utf-8") as f:
        f.write(content)
    print("wrote", path)


PAGES = []  # (path, lastmod-priority ignored; used for sitemap)


def add_page(filename, sitepath, title, description, depth, content,
             active=None, trail=None, extra_ld=""):
    html = page(title, description, sitepath, depth, content,
                active_path=active, trail=trail, extra_jsonld=extra_ld)
    write(filename, html)
    PAGES.append(sitepath)


def main():
    # Home
    add_page(
        "index.html", "/",
        "Dr. Fayana Richards, MPH, PMP | Public Health and Program Leadership",
        "Fayana Richards is a public health strategist, medical anthropologist, program leader, researcher, and educator with more than 18 years of experience in public health, community engagement, research, and program implementation.",
        0, pages_core.home(0),
        extra_ld=jsonld(PERSON) + jsonld(SERVICE),
    )

    # About
    add_page(
        "about/index.html", "/about/",
        "About | Dr. Fayana Richards, MPH, PMP",
        "Professional biography, philosophy, leadership approach, research perspective, education, and credentials of Dr. Fayana Richards, public health strategist and medical anthropologist.",
        1, pages_core.about(1),
        trail=[("Home", "/"), ("About", None)],
        extra_ld=jsonld(breadcrumb_ld([("Home", "/"), ("About", "/about/")])),
    )

    # Program leadership
    add_page(
        "program-leadership/index.html", "/program-leadership/",
        "Program and Project Leadership | Dr. Fayana Richards, MPH, PMP",
        "How Fayana Richards plans, scopes, coordinates, and monitors complex public health programs — from risk and issue management to partnerships, performance, and team development.",
        1, pages_core.leadership(1),
        trail=[("Home", "/"), ("Program and Project Leadership", None)],
        extra_ld=jsonld(breadcrumb_ld([("Home", "/"), ("Program and Project Leadership", "/program-leadership/")])),
    )

    # Selected work
    add_page(
        "work/index.html", "/work/",
        "Selected Work | Dr. Fayana Richards, MPH, PMP",
        "Case studies in public health consulting, community-engaged research, program design, curriculum development, research coordination, and science communication.",
        1, pages_work.work_index(1),
        trail=[("Home", "/"), ("Selected Work", None)],
        extra_ld=jsonld(breadcrumb_ld([("Home", "/"), ("Selected Work", "/work/")])),
    )

    # Case studies
    for cs in pages_work.CASE_STUDIES:
        sitepath = f"/work/{cs['slug']}/"
        add_page(
            f"work/{cs['slug']}/index.html", sitepath,
            f"{cs['title']} | Dr. Fayana Richards, MPH, PMP",
            cs["summary"],
            2, pages_work.case_study(cs, 2),
            active="/work/",
            trail=[("Home", "/"), ("Selected Work", "/work/"), (cs["title"], None)],
            extra_ld=jsonld(breadcrumb_ld([("Home", "/"), ("Selected Work", "/work/"), (cs["title"], sitepath)])),
        )

    # Experience
    add_page(
        "experience/index.html", "/experience/",
        "Experience | Dr. Fayana Richards, MPH, PMP",
        "The professional experience of Dr. Fayana Richards across public health consulting, higher education, research, community engagement, and science communication.",
        1, pages_core.experience(1),
        trail=[("Home", "/"), ("Experience", None)],
        extra_ld=jsonld(breadcrumb_ld([("Home", "/"), ("Experience", "/experience/")])),
    )

    # Research and writing
    add_page(
        "research-writing/index.html", "/research-writing/",
        "Research and Writing | Dr. Fayana Richards, MPH, PMP",
        "Research interests, methods, publications, and public scholarship addressing aging, caregiving, chronic illness, race and health, and the social conditions shaping health outcomes.",
        1, pages_other.research(1),
        trail=[("Home", "/"), ("Research and Writing", None)],
        extra_ld=jsonld(breadcrumb_ld([("Home", "/"), ("Research and Writing", "/research-writing/")])),
    )

    # Teaching and facilitation
    add_page(
        "teaching-facilitation/index.html", "/teaching-facilitation/",
        "Teaching and Facilitation | Dr. Fayana Richards, MPH, PMP",
        "University teaching, curriculum development, workshop facilitation, virtual learning, mentoring, and professional development programs led by Dr. Fayana Richards.",
        1, pages_other.teaching(1),
        trail=[("Home", "/"), ("Teaching and Facilitation", None)],
        extra_ld=jsonld(breadcrumb_ld([("Home", "/"), ("Teaching and Facilitation", "/teaching-facilitation/")])),
    )

    # Speaking
    add_page(
        "speaking/index.html", "/speaking/",
        "Speaking | Dr. Fayana Richards, MPH, PMP",
        "Conference presentations, invited lectures, workshops, webinars, and podcast work by Dr. Fayana Richards. Speaking and facilitation invitations are welcome.",
        1, pages_other.speaking(1),
        active="/teaching-facilitation/",
        trail=[("Home", "/"), ("Speaking", None)],
        extra_ld=jsonld(breadcrumb_ld([("Home", "/"), ("Speaking", "/speaking/")])),
    )

    # Résumé
    add_page(
        "resume/index.html", "/resume/",
        "Résumé | Dr. Fayana Richards, MPH, PMP",
        "Download the résumé of Dr. Fayana Richards, public health program strategy and operations leader and medical anthropologist, or review her experience and credentials.",
        1, pages_other.resume(1),
        trail=[("Home", "/"), ("Résumé", None)],
        extra_ld=jsonld(breadcrumb_ld([("Home", "/"), ("Résumé", "/resume/")])),
    )

    # Contact
    add_page(
        "contact/index.html", "/contact/",
        "Contact | Dr. Fayana Richards, MPH, PMP",
        "Contact Dr. Fayana Richards about program leadership, strategic initiatives, research collaboration, academic programming, facilitation, or speaking opportunities.",
        1, pages_other.contact(1),
        trail=[("Home", "/"), ("Contact", None)],
        extra_ld=jsonld(breadcrumb_ld([("Home", "/"), ("Contact", "/contact/")])),
    )

    # Accessibility and privacy
    add_page(
        "accessibility/index.html", "/accessibility/",
        "Accessibility Statement | Dr. Fayana Richards, MPH, PMP",
        "The accessibility commitments of this website, designed to conform to WCAG 2.2 Level AA, and how to report an accessibility barrier.",
        1, pages_other.accessibility_page(1),
        active="/_none_/",
        trail=[("Home", "/"), ("Accessibility Statement", None)],
        extra_ld=jsonld(breadcrumb_ld([("Home", "/"), ("Accessibility Statement", "/accessibility/")])),
    )
    add_page(
        "privacy/index.html", "/privacy/",
        "Privacy Statement | Dr. Fayana Richards, MPH, PMP",
        "How this website handles contact form submissions and visitor information.",
        1, pages_other.privacy_page(1),
        active="/_none_/",
        trail=[("Home", "/"), ("Privacy Statement", None)],
        extra_ld=jsonld(breadcrumb_ld([("Home", "/"), ("Privacy Statement", "/privacy/")])),
    )

    # 404 (root-level file; not in sitemap)
    html_404 = page(
        "Page Not Found | Dr. Fayana Richards, MPH, PMP",
        "The requested page could not be found.",
        "/404.html", 0, pages_other.not_found(0), active_path="/_none_/",
    )
    write("404.html", html_404)

    # Sitemap
    urls = "\n".join(
        f"  <url>\n    <loc>{SITE_URL}{p}</loc>\n  </url>" for p in PAGES
    )
    write("sitemap.xml", f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{urls}\n</urlset>\n')

    # Robots
    write("robots.txt", f"User-agent: *\nAllow: /\n\nSitemap: {SITE_URL}/sitemap.xml\n")

    # Favicon
    write("assets/icons/favicon.svg",
          '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64">'
          '<rect width="64" height="64" rx="8" fill="#2B0423"/>'
          '<text x="32" y="42" font-family="Georgia, serif" font-size="28" font-weight="700" fill="#EDEAE8" text-anchor="middle">FR</text>'
          '</svg>\n')

    print(f"\nBuilt {len(PAGES)} pages plus 404, sitemap, robots, favicon.")


if __name__ == "__main__":
    main()
